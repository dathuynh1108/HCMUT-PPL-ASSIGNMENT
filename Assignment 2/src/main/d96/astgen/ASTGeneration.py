from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

from main.d96.utils.AST import *
from main.d96.parser.D96Parser import D96Parser
from main.d96.parser.D96Visitor import D96Visitor


class ASTGeneration(D96Visitor):
    def visitProgram(self, context: D96Parser.ProgramContext):
        return Program([self.visit(class_declaration) for class_declaration in context.class_declaration()])

    def visitClass_declaration(self, context: D96Parser.Class_declarationContext):
        # Have parent
        if context.COLON():
            return ClassDecl(Id(context.ID(0).getText()), self.visit(context.class_body()), Id(context.ID(1).getText()))
        return ClassDecl(Id(context.ID(0).getText()), self.visit(context.class_body()))

    def visitClass_body(self, context: D96Parser.Class_bodyContext):
        # Visit list of member declaration
        result = []
        if (not context.class_member_declaration()): return []
        for class_member_declaration in context.class_member_declaration():
            visited_member = self.visit(class_member_declaration)
            # Attribute declaration return list of AttributeDecl
            # Method declaration return a MethodDecl object
            if (isinstance(visited_member, list)):
                result += visited_member
            else:
                result.append(visited_member)
        return result

    def visitClass_member_declaration(self, context: D96Parser.Class_member_declarationContext):
        # Pass, visit to children
        return self.visitChildren(context)

    def visitAttribute_declaration(self, context: D96Parser.Attribute_declarationContext):
        # Mutable or Imutable
        # Instance or Static
        mutable_or_imutable = VarDecl if context.VAR() else ConstDecl
        attribute_list = [self.visit(attribute_name)
                          for attribute_name in context.attribute_name()]
        type_name = self.visit(context.type_name())
        initialization_list = self.visit(context.initialization())

        attribute_declaration_list = []

        for i in range(0, len(attribute_list)):
            if attribute_list[i].name[0] == '$':
                instance_or_static = Static()
            else:
                instance_or_static = Instance()
            if initialization_list:
                attribute_declaration_list.append(AttributeDecl(instance_or_static, mutable_or_imutable(
                    attribute_list[i].name, type_name, initialization_list[i])))
            else:
                attribute_declaration_list.append(AttributeDecl(
                    instance_or_static, mutable_or_imutable(attribute_list[i].name, type_name)))
        return attribute_declaration_list

    def visitAttribute_name(self, context: D96Parser.Attribute_nameContext):
        if (context.ID()):
            return Id(context.ID().getText())
        return Id(context.DOLLAR_ID().getText())

    def visitType_name(self, context: D96Parser.Type_nameContext):
        # Pass, visit children
        return self.visitChildren(context)

    def visitPrimitive_type(self, context: D96Parser.Primitive_typeContext):
        if context.INTEGER():
            return IntType()
        if context.FLOAT():
            return FloatType()
        if context.STRING():
            return StringType()
        if context.BOOLEAN():
            return BoolType()

    def visitArray_type(self, context: D96Parser.Array_typeContext):
        size = int(context.INTEGER_LITERAL().getText())
        if context.primitive_type():
            element_type = self.visit(context.primitive_type())
        else:
            element_type = self.visit(context.array_type())
        return ArrayType(size, element_type)

    def visitClass_type(self, context: D96Parser.Class_typeContext):
        return ClassType(Id(context.ID().getText()))

    def visitInitialization(self, context: D96Parser.InitializationContext):
        if (context.ASSIGN()):
            return self.visit(context.initialization_list())
        return []

    def visitInitialization_list(self, context: D96Parser.Initialization_listContext):
        return [self.visit(expression) for expression in context.expression()]

    def visitMethod_declaration(self, context: D96Parser.Method_declarationContext):
        return "Method"

    def visitExpression(self, context: D96Parser.ExpressionContext):
        return "Exp"
