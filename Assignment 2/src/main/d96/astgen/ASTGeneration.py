from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([FuncDecl(Id("main"),
                                 [],
                                 self.visit(ctx.mptype()),
                                 Block([], [self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self, ctx: D96Parser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return VoidType()

    def visitBody(self, ctx: D96Parser.BodyContext):
        return self.visit(ctx.funcall())

    def visitFuncall(self, ctx: D96Parser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self, ctx: D96Parser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return IntLiteral(int(ctx.INTLIT().getText()))
