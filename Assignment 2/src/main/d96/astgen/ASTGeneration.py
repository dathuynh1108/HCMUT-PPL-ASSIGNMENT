from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(class_declaration) for class_declaration in ctx.class_declaration()])
    
    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        # Have parent
        if ctx.COLON(): 
            # Class body not empty
            if ctx.class_body():
                return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.class_body()), Id(ctx.ID(1).getText()))
            return ClassDecl(Id(ctx.ID(0).getText()), [], Id(ctx.ID(1).getText()))
        
        if ctx.class_body():
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.class_body()))
        return ClassDecl(Id(ctx.ID(0).getText()), [])
    
    def visitClass_body(self, ctx: D96Parser.Class_bodyContext):
        # Visit list of member declaration
        return [self.visit(class_member_declaration) for class_member_declaration in ctx.class_member_declaration()]
    
    def visitClass_member_declaration(self, ctx: D96Parser.Class_member_declarationContext):
        # Pass, visit to children
        return self.visitChildren(ctx)

    def visitAttribute_declaration(self, ctx: D96Parser.Attribute_declarationContext):
        # Mutable or Imutable
        # Instance or Static
        return "Attribute"

    def visitMethod_declaration(self, ctx: D96Parser.Method_declarationContext):
        return "Method"
