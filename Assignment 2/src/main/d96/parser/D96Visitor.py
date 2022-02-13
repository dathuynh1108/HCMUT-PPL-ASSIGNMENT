# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_member_declaration.
    def visitClass_member_declaration(self, ctx:D96Parser.Class_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_initialization.
    def visitAttribute_initialization(self, ctx:D96Parser.Attribute_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_initialization_list.
    def visitAttribute_initialization_list(self, ctx:D96Parser.Attribute_initialization_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declaration.
    def visitMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor_declaration.
    def visitConstructor_declaration(self, ctx:D96Parser.Constructor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor_declaration.
    def visitDestructor_declaration(self, ctx:D96Parser.Destructor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_parameters.
    def visitList_of_parameters(self, ctx:D96Parser.List_of_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_declaration.
    def visitParameter_declaration(self, ctx:D96Parser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_name.
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_literal.
    def visitPrimitive_literal(self, ctx:D96Parser.Primitive_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_literal.
    def visitArray_literal(self, ctx:D96Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_demensional_array.
    def visitMulti_demensional_array(self, ctx:D96Parser.Multi_demensional_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_literal_list.
    def visitArray_literal_list(self, ctx:D96Parser.Array_literal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_expressions.
    def visitList_of_expressions(self, ctx:D96Parser.List_of_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_expression.
    def visitString_expression(self, ctx:D96Parser.String_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relation_expression.
    def visitRelation_expression(self, ctx:D96Parser.Relation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_expression.
    def visitLogical_expression(self, ctx:D96Parser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#adding_expression.
    def visitAdding_expression(self, ctx:D96Parser.Adding_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiplying_expression.
    def visitMultiplying_expression(self, ctx:D96Parser.Multiplying_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#negative_expression.
    def visitNegative_expression(self, ctx:D96Parser.Negative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#sign_expression.
    def visitSign_expression(self, ctx:D96Parser.Sign_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_expression.
    def visitIndex_expression(self, ctx:D96Parser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_access_expression.
    def visitInstance_access_expression(self, ctx:D96Parser.Instance_access_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_access_expression.
    def visitStatic_access_expression(self, ctx:D96Parser.Static_access_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_creation_expression.
    def visitObject_creation_expression(self, ctx:D96Parser.Object_creation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_variable.
    def visitScalar_variable(self, ctx:D96Parser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_instance_access.
    def visitScalar_instance_access(self, ctx:D96Parser.Scalar_instance_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_static_access.
    def visitScalar_static_access(self, ctx:D96Parser.Scalar_static_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_index.
    def visitScalar_index(self, ctx:D96Parser.Scalar_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statement.
    def visitBlock_statement(self, ctx:D96Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_and_const_declaration.
    def visitVariable_and_const_declaration(self, ctx:D96Parser.Variable_and_const_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_initialization.
    def visitVariable_initialization(self, ctx:D96Parser.Variable_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_initialization_list.
    def visitVariable_initialization_list(self, ctx:D96Parser.Variable_initialization_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_statement.
    def visitAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#left_hand_side.
    def visitLeft_hand_side(self, ctx:D96Parser.Left_hand_sideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statement.
    def visitIf_statement(self, ctx:D96Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_statement.
    def visitElseif_statement(self, ctx:D96Parser.Elseif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_statement.
    def visitElse_statement(self, ctx:D96Parser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#foreach_statement.
    def visitForeach_statement(self, ctx:D96Parser.Foreach_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statement.
    def visitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statement.
    def visitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statement.
    def visitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocation_statement.
    def visitMethod_invocation_statement(self, ctx:D96Parser.Method_invocation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method_invocation.
    def visitInstance_method_invocation(self, ctx:D96Parser.Instance_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#prefix_instance_method_invocation.
    def visitPrefix_instance_method_invocation(self, ctx:D96Parser.Prefix_instance_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method_invocation.
    def visitStatic_method_invocation(self, ctx:D96Parser.Static_method_invocationContext):
        return self.visitChildren(ctx)



del D96Parser