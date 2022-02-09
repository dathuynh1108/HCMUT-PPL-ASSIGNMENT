# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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


    # Visit a parse tree produced by D96Parser#classdecls.
    def visitClassdecls(self, ctx:D96Parser.ClassdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#superclass.
    def visitSuperclass(self, ctx:D96Parser.SuperclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberlist.
    def visitMemberlist(self, ctx:D96Parser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr.
    def visitAttr(self, ctx:D96Parser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrtype.
    def visitAttrtype(self, ctx:D96Parser.AttrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ.
    def visitTyp(self, ctx:D96Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprlist.
    def visitExprlist(self, ctx:D96Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp11.
    def visitExp11(self, ctx:D96Parser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call.
    def visitCall(self, ctx:D96Parser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockstate.
    def visitBlockstate(self, ctx:D96Parser.BlockstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statements.
    def visitStatements(self, ctx:D96Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#sta.
    def visitSta(self, ctx:D96Parser.StaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifsta.
    def visitIfsta(self, ctx:D96Parser.IfstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#eliflist.
    def visitEliflist(self, ctx:D96Parser.EliflistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forsta.
    def visitForsta(self, ctx:D96Parser.ForstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breaksta.
    def visitBreaksta(self, ctx:D96Parser.BreakstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continuesta.
    def visitContinuesta(self, ctx:D96Parser.ContinuestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#returnsta.
    def visitReturnsta(self, ctx:D96Parser.ReturnstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodsta.
    def visitMethodsta(self, ctx:D96Parser.MethodstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexedarr.
    def visitIndexedarr(self, ctx:D96Parser.IndexedarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literals.
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit.
    def visitLit(self, ctx:D96Parser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiarr.
    def visitMultiarr(self, ctx:D96Parser.MultiarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrlist.
    def visitArrlist(self, ctx:D96Parser.ArrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr.
    def visitArr(self, ctx:D96Parser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrdecl.
    def visitArrdecl(self, ctx:D96Parser.ArrdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element.
    def visitElement(self, ctx:D96Parser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx:D96Parser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#eleexp.
    def visitEleexp(self, ctx:D96Parser.EleexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexop.
    def visitIndexop(self, ctx:D96Parser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance.
    def visitInstance(self, ctx:D96Parser.InstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staatr.
    def visitStaatr(self, ctx:D96Parser.StaatrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#imethodi.
    def visitImethodi(self, ctx:D96Parser.ImethodiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#smethodi.
    def visitSmethodi(self, ctx:D96Parser.SmethodiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#objcreate.
    def visitObjcreate(self, ctx:D96Parser.ObjcreateContext):
        return self.visitChildren(ctx)



del D96Parser