from numpy import isin
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce
from main.d96.utils.AST import *
from main.d96.parser.D96Parser import D96Parser
from main.d96.parser.D96Visitor import D96Visitor


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(class_declaration) for class_declaration in ctx.class_declaration()])

    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        # Have parent or not
        class_body = self.visit_program_class_body(ctx.class_body()) if ctx.ID(0).getText() == "Program" else self.visit(ctx.class_body())
        return ClassDecl(Id(ctx.ID(0).getText()), class_body, Id(ctx.ID(1).getText())) if ctx.COLON() else ClassDecl(Id(ctx.ID(0).getText()), class_body)

    def visitClass_body(self, ctx: D96Parser.Class_bodyContext):
        # Visit list of member declaration
        # Check is instance chạy nhanh hơn so với high-order function 1 dòng
        if (not ctx.class_member_declaration()):
            return []
        class_member_declaration_list = []
        for class_member_declaration in ctx.class_member_declaration():
            visit_result = self.visit(class_member_declaration)
            if isinstance(visit_result, list):
                class_member_declaration_list += visit_result
            else:
                class_member_declaration_list.append(visit_result)
        return class_member_declaration_list

    def visit_program_class_body(self, ctx: D96Parser.Class_bodyContext):
        if (not ctx.class_member_declaration()):
            return []
        class_member_declaration_list = []
        for class_member_declaration in ctx.class_member_declaration():
            visit_result = self.visit(class_member_declaration)
            if isinstance(visit_result, list):
                class_member_declaration_list += visit_result
            else:
                if visit_result.name.name == "main" and not visit_result.param:
                    visit_result.kind = Static()
                class_member_declaration_list.append(visit_result)
        return class_member_declaration_list

    def visitClass_member_declaration(self, ctx: D96Parser.Class_member_declarationContext):
        # Pass, visit to children
        return self.visitChildren(ctx)

    def visitAttribute_declaration(self, ctx: D96Parser.Attribute_declarationContext):
        # Mutable or Imutable
        # Instance or Static
        mutable_or_imutable = VarDecl if ctx.VAR() else ConstDecl
        attribute_list = [self.visit(attribute_name) for attribute_name in ctx.attribute_name()]
        type_name = self.visit(ctx.type_name())
        initialization_list = self.visit(ctx.initialization())
        attribute_declaration_list = []
        for i in range(0, len(attribute_list)):
            attribute_declaration_list.append(AttributeDecl(Static() if attribute_list[i].name[0] == '$' else Instance(), mutable_or_imutable(attribute_list[i].name, type_name, initialization_list[i])) if initialization_list else AttributeDecl(Static() if attribute_list[i].name[0] == '$' else Instance(), mutable_or_imutable(attribute_list[i].name, type_name, None)))
        return attribute_declaration_list  

    def visitAttribute_name(self, ctx: D96Parser.Attribute_nameContext):
        return Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.DOLLAR_ID().getText())

    def visitType_name(self, ctx: D96Parser.Type_nameContext):
        # Pass, visit children
        return self.visitChildren(ctx)

    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.INTEGER():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        return BoolType()
        

    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        def cast_to_integer(string):
            if string == '0':
                return 0
            if string[0:2] == '0x' or string[0:2] == '0X':
                return int(string, 16)
            if string[0:2] == '0b' or string[0:2] == '0B':
                return int(string, 2)
            if string[0] == '0':
                return int(string, 8)
            return int(string, 10)
        
        size = cast_to_integer(ctx.INTEGER_LITERAL().getText())
        element_type = self.visit(ctx.primitive_type(
        )) if ctx.primitive_type() else self.visit(ctx.array_type())
        return ArrayType(size, element_type)

    def visitClass_type(self, ctx: D96Parser.Class_typeContext):
        return ClassType(Id(ctx.ID().getText()))

    def visitInitialization(self, ctx: D96Parser.InitializationContext):
        return self.visit(ctx.initialization_list()) if ctx.ASSIGN() else []

    def visitInitialization_list(self, ctx: D96Parser.Initialization_listContext):
        return [self.visit(expression) for expression in ctx.expression()]

    def visitMethod_declaration(self, ctx: D96Parser.Method_declarationContext):
        method_name = ctx.ID().getText() if ctx.ID() else ctx.DOLLAR_ID().getText()
        instance_or_static = Static() if method_name[0] == '$' else Instance()
        list_of_parameters = self.visit(ctx.list_of_parameters()) if ctx.list_of_parameters() else []
        body = self.visit(ctx.block_statement())
        return MethodDecl(instance_or_static, Id(method_name), list_of_parameters, body)

    def visitList_of_parameters(self, ctx: D96Parser.List_of_parametersContext):
        list_of_parameters = []
        for parameter_declaration in ctx.parameter_declaration():
            list_of_parameters += self.visit(parameter_declaration)
        return list_of_parameters

    def visitParameter_declaration(self, ctx: D96Parser.Parameter_declarationContext):
        list_of_same_type_parameter = []
        type_name = self.visit(ctx.type_name())
        for parameter_name in [parameter_name.getText() for parameter_name in ctx.ID()]:
            list_of_same_type_parameter.append(VarDecl(Id(parameter_name), type_name, None))
        return list_of_same_type_parameter

    def visitConstructor_declaration(self, ctx: D96Parser.Constructor_declarationContext):
        list_of_parameters = self.visit(
            ctx.list_of_parameters()) if ctx.list_of_parameters() else []
        body = self.visit(ctx.block_statement())
        return MethodDecl(Instance(), Id("Constructor"), list_of_parameters, body)

    def visitDestructor_declaration(self, ctx: D96Parser.Destructor_declarationContext):
        body = self.visit(ctx.block_statement())
        return MethodDecl(Instance(), Id("Destructor"), [], body)

    def visitExpression(self, ctx: D96Parser.ExpressionContext):
        # Pass, visit children
        return self.visitChildren(ctx)

    def visitString_expression(self, ctx: D96Parser.String_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitRelation_expression(self, ctx: D96Parser.Relation_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    
    def visitLogical_expression(self, ctx: D96Parser.Logical_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    
    def visitAdding_expression(self, ctx: D96Parser.Adding_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitMultiplying_expression(self, ctx: D96Parser.Multiplying_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitNegative_expression(self, ctx: D96Parser.Negative_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))

    def visitSign_expression(self, ctx: D96Parser.Sign_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))

    def visitIndex_expression(self, ctx: D96Parser.Index_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return ArrayCell(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))
    
    def visitIndex_operator(self, ctx: D96Parser.Index_operatorContext):
        # [exp] return [exp]
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expression())]
        # [exp] index_op return [exp] + result of index_op      
        return [self.visit(ctx.expression())] + self.visit(ctx.index_operator())
    
    def visitInstance_access_expression(self, ctx: D96Parser.Instance_access_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        # Instance attribute access:
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.instance_access_expression()), Id(ctx.ID().getText()))
        # Instance method call:
        return CallExpr(self.visit(ctx.instance_access_expression()), Id(ctx.ID().getText()), self.visit(ctx.list_of_expressions()) if ctx.list_of_expressions() else [])
    
    def visitStatic_access_expression(self, ctx: D96Parser.Static_access_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        # Static attribute access:
        if ctx.getChildCount() == 3:
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()))
        # Static method call:
        return CallExpr(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.list_of_expressions()) if ctx.list_of_expressions() else [])
    
    def visitObject_creation_expression(self, ctx: D96Parser.Object_creation_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.list_of_expressions()) if ctx.list_of_expressions() else [])
    
    def visitOperand(self, ctx: D96Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.SELF():
            return SelfLiteral()
        if ctx.NULL():
            return NullLiteral()
        if ctx.literal():
            return self.visit(ctx.literal())
        return self.visit(ctx.expression())        

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        return self.visit(ctx.primitive_literal()) if ctx.primitive_literal() else self.visit(ctx.array_literal())

    def visitPrimitive_literal(self, ctx: D96Parser.Primitive_literalContext):
        def cast_to_integer(string):
            if string == '0': return 0
            if string[0:2] == '0x' or string[0:2] == '0X': return int(string, 16)
            if string[0:2] == '0b' or string[0:2] == '0B': return int(string, 2)
            if string[0] == '0': return int(string, 8)
            return int(string, 10)
        
        def cast_to_float(string):
            if string[0] == '.': string = '0' + string
            return float(string)

        if ctx.ZERO_INTEGER():
            return IntLiteral(cast_to_integer(ctx.ZERO_INTEGER().getText()))
        if ctx.INTEGER_LITERAL():
            return IntLiteral(cast_to_integer(ctx.INTEGER_LITERAL().getText()))
        if ctx.FLOAT_LITERAL():
            return FloatLiteral(cast_to_float(ctx.FLOAT_LITERAL().getText()))
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        return BooleanLiteral(bool(ctx.BOOLEAN_LITERAL().getText()))
    
    def visitArray_literal(self, ctx: D96Parser.Array_literalContext):
        return self.visit(ctx.indexed_array()) if ctx.indexed_array() else self.visit(ctx.multi_demensional_array())

    def visitIndexed_array(self, ctx: D96Parser.Indexed_arrayContext):
        return ArrayLiteral(self.visit(ctx.list_of_expressions()))

    def visitMulti_demensional_array(self, ctx: D96Parser.Multi_demensional_arrayContext):
        return ArrayLiteral(self.visit(ctx.array_literal_list()))
    
    def visitArray_literal_list(self, ctx: D96Parser.Array_literal_listContext):
        return [self.visit(array_literal) for array_literal in ctx.array_literal()]

    def visitList_of_expressions(self, ctx: D96Parser.List_of_expressionsContext):
       return [self.visit(expression) for expression in ctx.expression()]

    def visitBlock_statement(self, ctx: D96Parser.Block_statementContext):
        list_of_statement = []
        for statement in ctx.statement():
            visit_result = self.visit(statement)
            if isinstance(visit_result, list):
                list_of_statement += visit_result
            else:
                list_of_statement.append(visit_result)
        return Block(list_of_statement)
    
    def visitStatement(self, ctx: D96Parser.StatementContext):
        return self.visitChildren(ctx)

    def visitVariable_and_const_declaration(self, ctx: D96Parser.Variable_and_const_declarationContext):
        mutable_or_imutable = VarDecl if ctx.VAR() else ConstDecl
        variable_list = [Id(variable_name.getText()) for variable_name in ctx.ID()]
        type_name = self.visit(ctx.type_name())
        initialization_list = self.visit(ctx.initialization())
        variable_declaration_list = []
        for i in range(0, len(variable_list)):
            variable_declaration_list.append(mutable_or_imutable(variable_list[i].name, type_name, initialization_list[i]) if initialization_list else mutable_or_imutable(variable_list[i].name, type_name, None))
        return variable_declaration_list
    
    def visitAssign_statement(self, ctx: D96Parser.Assign_statementContext):
        return Assign(self.visit(ctx.left_hand_side()), self.visit(ctx.expression()))
    
    def visitLeft_hand_side(self, ctx: D96Parser.Left_hand_sideContext):
        return self.visitChildren(ctx)
        
    def visitScalar_variable(self, ctx: D96Parser.Scalar_variableContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visitChildren(ctx)

    def visitScalar_index(self, ctx: D96Parser.Scalar_indexContext):
        return ArrayCell(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))

    def visitScalar_instance_access(self, ctx: D96Parser.Scalar_instance_accessContext):
        return FieldAccess(self.visit(ctx.instance_access_expression()), Id(ctx.ID().getText()))

    def visitScalar_static_access(self, ctx: D96Parser.Scalar_static_accessContext):
        return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()))

    def visitIf_statement(self, ctx: D96Parser.If_statementContext):
        elseif_statement = [self.visit(elseif_statement) for elseif_statement in ctx.elseif_statement()] if ctx.elseif_statement() else None
        else_statement = self.visit(ctx.else_statement()) if ctx.else_statement() else None
        return "If statement"

    def visitElseif_statement(self, ctx: D96Parser.Elseif_statementContext):
        return "Elseif statement"

    def visitElse_statement(self, ctx: D96Parser.Else_statementContext):
        return "Else statement"

    def visitForeach_statement(self, ctx: D96Parser.Foreach_statementContext):
        expression_list = [self.visit(expression) for expression in ctx.expression()]
        return For(Id(ctx.ID().getText()), expression_list[0], expression_list[1], self.visit(ctx.block_statement()), expression_list[2] if len(expression_list) == 3 else None)
    
    def visitBreak_statement(self, ctx: D96Parser.Break_statementContext):
        return Break()

    def visitContinue_statement(self, ctx: D96Parser.Continue_statementContext):
        return Continue()
    
    def visitReturn_statement(self, ctx: D96Parser.Return_statementContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)
    
    def visitMethod_invocation_statement(self, ctx: D96Parser.Method_invocation_statementContext):
        return "Method inovation statement"

    