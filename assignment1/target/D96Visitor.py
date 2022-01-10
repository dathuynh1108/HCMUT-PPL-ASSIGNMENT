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


    # Visit a parse tree produced by D96Parser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_declaration.
    def visitVar_declaration(self, ctx:D96Parser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#val_declaration.
    def visitVal_declaration(self, ctx:D96Parser.Val_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_name.
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal_type.
    def visitNormal_type(self, ctx:D96Parser.Normal_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
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


    # Visit a parse tree produced by D96Parser#parameter_list.
    def visitParameter_list(self, ctx:D96Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_declaration.
    def visitParameter_declaration(self, ctx:D96Parser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statement.
    def visitBlock_statement(self, ctx:D96Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#initialization.
    def visitInitialization(self, ctx:D96Parser.InitializationContext):
        return self.visitChildren(ctx)



del D96Parser