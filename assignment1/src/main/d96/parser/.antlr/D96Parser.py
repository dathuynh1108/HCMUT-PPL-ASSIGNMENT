# Generated from d:\Workspace\PPL\Assignment\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\20\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\2\3\2\3")
        buf.write("\3\3\3\3\3\2\2\4\2\4\2\2\2\16\2\7\3\2\2\2\4\r\3\2\2\2")
        buf.write("\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7\3\2\2\2\t\n\3")
        buf.write("\2\2\2\n\13\3\2\2\2\13\f\7\2\2\3\f\3\3\2\2\2\r\16\13\2")
        buf.write("\2\2\16\5\3\2\2\2\3\t")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'var'", 
                     "'val'", "'class'", "'Array'", "'Int'", "'Float'", 
                     "'Boolean'", "'String'", "'Null'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'==.'", "'+.'", "'new'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'::'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "VAR", "VAL", "CLASS", 
                      "ARRAY", "INT", "FLOAT", "BOOLEAN", "STRING", "NULL", 
                      "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "LT", "LTE", "GT", "GTE", "STRING_EQUAL", "STRING_ADD", 
                      "NEW", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", 
                      "COLON", "DOUBLE_COLON", "LCB", "RCB", "ID", "DOLLAR_ID", 
                      "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_class_declaration = 1

    ruleNames =  [ "program", "class_declaration" ]

    EOF = Token.EOF
    COMMENT=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    VAR=8
    VAL=9
    CLASS=10
    ARRAY=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    STRING=15
    NULL=16
    INTEGER_LITERAL=17
    STRING_LITERAL=18
    BOOLEAN_LITERAL=19
    FLOAT_LITERAL=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    NOT=26
    AND=27
    OR=28
    EQUAL=29
    ASSIGN=30
    NOT_EQUAL=31
    LT=32
    LTE=33
    GT=34
    GTE=35
    STRING_EQUAL=36
    STRING_ADD=37
    NEW=38
    LP=39
    RP=40
    LSB=41
    RSB=42
    DOT=43
    COMMA=44
    SEMI=45
    COLON=46
    DOUBLE_COLON=47
    LCB=48
    RCB=49
    ID=50
    DOLLAR_ID=51
    WS=52
    UNTERMINATED_COMMENT=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55
    ERROR_TOKEN=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.class_declaration()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.COMMENT) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.ELSEIF) | (1 << D96Parser.ELSE) | (1 << D96Parser.FOREACH) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CLASS) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.ADD) | (1 << D96Parser.SUB) | (1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD) | (1 << D96Parser.NOT) | (1 << D96Parser.AND) | (1 << D96Parser.OR) | (1 << D96Parser.EQUAL) | (1 << D96Parser.ASSIGN) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LT) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.STRING_EQUAL) | (1 << D96Parser.STRING_ADD) | (1 << D96Parser.NEW) | (1 << D96Parser.LP) | (1 << D96Parser.RP) | (1 << D96Parser.LSB) | (1 << D96Parser.RSB) | (1 << D96Parser.DOT) | (1 << D96Parser.COMMA) | (1 << D96Parser.SEMI) | (1 << D96Parser.COLON) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.LCB) | (1 << D96Parser.RCB) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.WS) | (1 << D96Parser.UNTERMINATED_COMMENT) | (1 << D96Parser.UNCLOSE_STRING) | (1 << D96Parser.ILLEGAL_ESCAPE) | (1 << D96Parser.ERROR_TOKEN))) != 0)):
                    break

            self.state = 9
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





