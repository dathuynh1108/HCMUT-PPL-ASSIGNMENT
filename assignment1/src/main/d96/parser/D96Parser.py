# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u0119\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\7\2@\n\2\f\2\16\2C\13\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3K\n\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4S\n\4\f\4")
        buf.write("\16\4V\13\4\3\5\3\5\3\5\3\5\7\5\\\n\5\f\5\16\5_\13\5\3")
        buf.write("\5\3\5\3\5\5\5d\n\5\3\5\3\5\3\6\3\6\5\6j\n\6\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\7\r\u0088\n\r\f\r\16\r\u008b\13\r\3\16\3\16\3\16\7\16")
        buf.write("\u0090\n\16\f\16\16\16\u0093\13\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\7\17\u009a\n\17\f\17\16\17\u009d\13\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00a9\n")
        buf.write("\20\3\21\3\21\3\21\3\21\7\21\u00af\n\21\f\21\16\21\u00b2")
        buf.write("\13\21\3\21\3\21\3\21\5\21\u00b7\n\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00c3\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\6\24\u00d8\n\24\r")
        buf.write("\24\16\24\u00d9\3\24\3\24\3\24\3\24\3\24\3\24\6\24\u00e2")
        buf.write("\n\24\r\24\16\24\u00e3\3\24\3\24\5\24\u00e8\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00fc\n\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u010d\n\32\3\33\3\33\3\34\3\34\3")
        buf.write("\35\3\35\3\36\3\36\3\37\3\37\3\37\2\2 \2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<\2\5\3")
        buf.write("\2\13\f\3\2<=\3\2\25\30\2\u0116\2A\3\2\2\2\4F\3\2\2\2")
        buf.write("\6T\3\2\2\2\bW\3\2\2\2\ni\3\2\2\2\fk\3\2\2\2\16m\3\2\2")
        buf.write("\2\20s\3\2\2\2\22u\3\2\2\2\24{\3\2\2\2\26\u0081\3\2\2")
        buf.write("\2\30\u0089\3\2\2\2\32\u008c\3\2\2\2\34\u0097\3\2\2\2")
        buf.write("\36\u00a8\3\2\2\2 \u00aa\3\2\2\2\"\u00ba\3\2\2\2$\u00c2")
        buf.write("\3\2\2\2&\u00e7\3\2\2\2(\u00e9\3\2\2\2*\u00ef\3\2\2\2")
        buf.write(",\u00f2\3\2\2\2.\u0100\3\2\2\2\60\u0103\3\2\2\2\62\u010c")
        buf.write("\3\2\2\2\64\u010e\3\2\2\2\66\u0110\3\2\2\28\u0112\3\2")
        buf.write("\2\2:\u0114\3\2\2\2<\u0116\3\2\2\2>@\5\4\3\2?>\3\2\2\2")
        buf.write("@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2CA\3\2\2\2DE\7")
        buf.write("\2\2\3E\3\3\2\2\2FG\7\23\2\2GJ\7<\2\2HI\78\2\2IK\7<\2")
        buf.write("\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\7:\2\2MN\5\6\4\2NO")
        buf.write("\7;\2\2O\5\3\2\2\2PS\5\b\5\2QS\5\22\n\2RP\3\2\2\2RQ\3")
        buf.write("\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\7\3\2\2\2VT\3\2")
        buf.write("\2\2WX\t\2\2\2X]\t\3\2\2YZ\7\66\2\2Z\\\t\3\2\2[Y\3\2\2")
        buf.write("\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2")
        buf.write("`a\78\2\2ac\5\n\6\2bd\5\20\t\2cb\3\2\2\2cd\3\2\2\2de\3")
        buf.write("\2\2\2ef\7\67\2\2f\t\3\2\2\2gj\5\f\7\2hj\5\16\b\2ig\3")
        buf.write("\2\2\2ih\3\2\2\2j\13\3\2\2\2kl\t\4\2\2l\r\3\2\2\2mn\7")
        buf.write("\24\2\2no\7\62\2\2op\5\f\7\2pq\7\66\2\2qr\7\63\2\2r\17")
        buf.write("\3\2\2\2st\7\3\2\2t\21\3\2\2\2uv\t\3\2\2vw\7\60\2\2wx")
        buf.write("\5\30\r\2xy\7\61\2\2yz\5\34\17\2z\23\3\2\2\2{|\7\21\2")
        buf.write("\2|}\7\60\2\2}~\5\30\r\2~\177\7\61\2\2\177\u0080\5\34")
        buf.write("\17\2\u0080\25\3\2\2\2\u0081\u0082\7\22\2\2\u0082\u0083")
        buf.write("\7\60\2\2\u0083\u0084\7\61\2\2\u0084\u0085\5\34\17\2\u0085")
        buf.write("\27\3\2\2\2\u0086\u0088\5\32\16\2\u0087\u0086\3\2\2\2")
        buf.write("\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3")
        buf.write("\2\2\2\u008a\31\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u0091")
        buf.write("\7<\2\2\u008d\u008e\7\66\2\2\u008e\u0090\7<\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0091\3")
        buf.write("\2\2\2\u0094\u0095\78\2\2\u0095\u0096\5\n\6\2\u0096\33")
        buf.write("\3\2\2\2\u0097\u009b\7:\2\2\u0098\u009a\5\36\20\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009e\u009f\7;\2\2\u009f\35\3\2\2\2\u00a0\u00a9")
        buf.write("\5 \21\2\u00a1\u00a9\5\"\22\2\u00a2\u00a9\5&\24\2\u00a3")
        buf.write("\u00a9\5,\27\2\u00a4\u00a9\5.\30\2\u00a5\u00a9\5\60\31")
        buf.write("\2\u00a6\u00a9\5\62\32\2\u00a7\u00a9\5\64\33\2\u00a8\u00a0")
        buf.write("\3\2\2\2\u00a8\u00a1\3\2\2\2\u00a8\u00a2\3\2\2\2\u00a8")
        buf.write("\u00a3\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a5\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\37\3\2")
        buf.write("\2\2\u00aa\u00ab\t\2\2\2\u00ab\u00b0\7<\2\2\u00ac\u00ad")
        buf.write("\7\66\2\2\u00ad\u00af\7<\2\2\u00ae\u00ac\3\2\2\2\u00af")
        buf.write("\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\7")
        buf.write("8\2\2\u00b4\u00b6\5\n\6\2\u00b5\u00b7\5\20\t\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\u00b9\7\67\2\2\u00b9!\3\2\2\2\u00ba\u00bb\5$\23\2\u00bb")
        buf.write("\u00bc\7&\2\2\u00bc\u00bd\5\66\34\2\u00bd\u00be\7\67\2")
        buf.write("\2\u00be#\3\2\2\2\u00bf\u00c3\7<\2\2\u00c0\u00c3\7=\2")
        buf.write("\2\u00c1\u00c3\58\35\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3%\3\2\2\2\u00c4\u00c5")
        buf.write("\7\7\2\2\u00c5\u00c6\7\60\2\2\u00c6\u00c7\5\66\34\2\u00c7")
        buf.write("\u00c8\7\61\2\2\u00c8\u00c9\5\34\17\2\u00c9\u00e8\3\2")
        buf.write("\2\2\u00ca\u00cb\7\7\2\2\u00cb\u00cc\7\60\2\2\u00cc\u00cd")
        buf.write("\5\66\34\2\u00cd\u00ce\7\61\2\2\u00ce\u00cf\5\34\17\2")
        buf.write("\u00cf\u00d0\5*\26\2\u00d0\u00e8\3\2\2\2\u00d1\u00d2\7")
        buf.write("\7\2\2\u00d2\u00d3\7\60\2\2\u00d3\u00d4\5\66\34\2\u00d4")
        buf.write("\u00d5\7\61\2\2\u00d5\u00d7\5\34\17\2\u00d6\u00d8\5(\25")
        buf.write("\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00e8\3\2\2\2\u00db")
        buf.write("\u00dc\7\7\2\2\u00dc\u00dd\7\60\2\2\u00dd\u00de\5\66\34")
        buf.write("\2\u00de\u00df\7\61\2\2\u00df\u00e1\5\34\17\2\u00e0\u00e2")
        buf.write("\5(\25\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e6\5*\26\2\u00e6\u00e8\3\2\2\2\u00e7\u00c4\3")
        buf.write("\2\2\2\u00e7\u00ca\3\2\2\2\u00e7\u00d1\3\2\2\2\u00e7\u00db")
        buf.write("\3\2\2\2\u00e8\'\3\2\2\2\u00e9\u00ea\7\b\2\2\u00ea\u00eb")
        buf.write("\7\60\2\2\u00eb\u00ec\5\66\34\2\u00ec\u00ed\7\61\2\2\u00ed")
        buf.write("\u00ee\5\34\17\2\u00ee)\3\2\2\2\u00ef\u00f0\7\t\2\2\u00f0")
        buf.write("\u00f1\5\34\17\2\u00f1+\3\2\2\2\u00f2\u00f3\7\n\2\2\u00f3")
        buf.write("\u00f4\7\60\2\2\u00f4\u00f5\t\3\2\2\u00f5\u00f6\7\17\2")
        buf.write("\2\u00f6\u00f7\5\66\34\2\u00f7\u00f8\7\65\2\2\u00f8\u00fb")
        buf.write("\5\66\34\2\u00f9\u00fa\7\20\2\2\u00fa\u00fc\5\66\34\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\u00fe\7\61\2\2\u00fe\u00ff\5\34\17\2\u00ff")
        buf.write("-\3\2\2\2\u0100\u0101\7\5\2\2\u0101\u0102\7\67\2\2\u0102")
        buf.write("/\3\2\2\2\u0103\u0104\7\6\2\2\u0104\u0105\7\67\2\2\u0105")
        buf.write("\61\3\2\2\2\u0106\u0107\7\16\2\2\u0107\u0108\5\66\34\2")
        buf.write("\u0108\u0109\7\67\2\2\u0109\u010d\3\2\2\2\u010a\u010b")
        buf.write("\7\16\2\2\u010b\u010d\7\67\2\2\u010c\u0106\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010d\63\3\2\2\2\u010e\u010f\7\3\2\2\u010f")
        buf.write("\65\3\2\2\2\u0110\u0111\7\3\2\2\u0111\67\3\2\2\2\u0112")
        buf.write("\u0113\7\3\2\2\u01139\3\2\2\2\u0114\u0115\7\3\2\2\u0115")
        buf.write(";\3\2\2\2\u0116\u0117\7\3\2\2\u0117=\3\2\2\2\25AJRT]c")
        buf.write("i\u0089\u0091\u009b\u00a8\u00b0\u00b6\u00c2\u00d9\u00e3")
        buf.write("\u00e7\u00fb\u010c")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Chua lam'", "<INVALID>", "'Break'", 
                     "'Continue'", "'If'", "'Elseif'", "'Else'", "'For'", 
                     "'var'", "'val'", "'self'", "'return'", "'In'", "'By'", 
                     "'constructor'", "'destructor'", "'class'", "'Array'", 
                     "'Int'", "'Float'", "'Boolean'", "'String'", "'Null'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'==.'", "'+.'", "'new'", "'('", "')'", "'['", "']'", 
                     "'.'", "'..'", "','", "';'", "':'", "'::'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOR", "VAR", "VAL", "SELF", 
                      "RETURN", "IN", "BY", "CONSTRUCTOR", "DESTRUCTOR", 
                      "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "NULL", "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "LT", "LTE", "GT", "GTE", "STRING_EQUAL", "STRING_ADD", 
                      "NEW", "LP", "RP", "LSB", "RSB", "DOT", "DOUBLE_DOT", 
                      "COMMA", "SEMI", "COLON", "DOUBLE_COLON", "LCB", "RCB", 
                      "ID", "DOLLAR_ID", "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_class_body = 2
    RULE_attribute_declaration = 3
    RULE_type_name = 4
    RULE_normal_type = 5
    RULE_array_type = 6
    RULE_initialization = 7
    RULE_method_declaration = 8
    RULE_constructor_declaration = 9
    RULE_destructor_declaration = 10
    RULE_parameter_list = 11
    RULE_parameter_declaration = 12
    RULE_block_statement = 13
    RULE_statement = 14
    RULE_variable_and_const_declaration = 15
    RULE_assign_statement = 16
    RULE_left_hand_side = 17
    RULE_if_statement = 18
    RULE_elseif_statement = 19
    RULE_else_statement = 20
    RULE_foreach_statement = 21
    RULE_break_statement = 22
    RULE_continue_statement = 23
    RULE_return_statement = 24
    RULE_method_invocation_statement = 25
    RULE_expression = 26
    RULE_index_expression = 27
    RULE_array_literal = 28
    RULE_normal_literal = 29

    ruleNames =  [ "program", "class_declaration", "class_body", "attribute_declaration", 
                   "type_name", "normal_type", "array_type", "initialization", 
                   "method_declaration", "constructor_declaration", "destructor_declaration", 
                   "parameter_list", "parameter_declaration", "block_statement", 
                   "statement", "variable_and_const_declaration", "assign_statement", 
                   "left_hand_side", "if_statement", "elseif_statement", 
                   "else_statement", "foreach_statement", "break_statement", 
                   "continue_statement", "return_statement", "method_invocation_statement", 
                   "expression", "index_expression", "array_literal", "normal_literal" ]

    EOF = Token.EOF
    T__0=1
    COMMENT=2
    BREAK=3
    CONTINUE=4
    IF=5
    ELSEIF=6
    ELSE=7
    FOR=8
    VAR=9
    VAL=10
    SELF=11
    RETURN=12
    IN=13
    BY=14
    CONSTRUCTOR=15
    DESTRUCTOR=16
    CLASS=17
    ARRAY=18
    INT=19
    FLOAT=20
    BOOLEAN=21
    STRING=22
    NULL=23
    INTEGER_LITERAL=24
    STRING_LITERAL=25
    BOOLEAN_LITERAL=26
    FLOAT_LITERAL=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    NOT=33
    AND=34
    OR=35
    EQUAL=36
    ASSIGN=37
    NOT_EQUAL=38
    LT=39
    LTE=40
    GT=41
    GTE=42
    STRING_EQUAL=43
    STRING_ADD=44
    NEW=45
    LP=46
    RP=47
    LSB=48
    RSB=49
    DOT=50
    DOUBLE_DOT=51
    COMMA=52
    SEMI=53
    COLON=54
    DOUBLE_COLON=55
    LCB=56
    RCB=57
    ID=58
    DOLLAR_ID=59
    WS=60
    UNTERMINATED_COMMENT=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_TOKEN=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CLASS:
                self.state = 60
                self.class_declaration()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(D96Parser.CLASS)
            self.state = 69
            self.match(D96Parser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 70
                self.match(D96Parser.COLON)
                self.state = 71
                self.match(D96Parser.ID)


            self.state = 74
            self.match(D96Parser.LCB)
            self.state = 75
            self.class_body()
            self.state = 76
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Attribute_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,i)


        def method_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Method_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Method_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAR, D96Parser.VAL]:
                    self.state = 78
                    self.attribute_declaration()
                    pass
                elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 79
                    self.method_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def DOLLAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_ID)
            else:
                return self.getToken(D96Parser.DOLLAR_ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def initialization(self):
            return self.getTypedRuleContext(D96Parser.InitializationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declaration" ):
                return visitor.visitAttribute_declaration(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 87
                self.match(D96Parser.COMMA)
                self.state = 88
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(D96Parser.COLON)
            self.state = 95
            self.type_name()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__0:
                self.state = 96
                self.initialization()


            self.state = 99
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_type(self):
            return self.getTypedRuleContext(D96Parser.Normal_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_name)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.normal_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_normal_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_type" ):
                return visitor.visitNormal_type(self)
            else:
                return visitor.visitChildren(self)




    def normal_type(self):

        localctx = D96Parser.Normal_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normal_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def normal_type(self):
            return self.getTypedRuleContext(D96Parser.Normal_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(D96Parser.ARRAY)
            self.state = 108
            self.match(D96Parser.LSB)
            self.state = 109
            self.normal_type()
            self.state = 110
            self.match(D96Parser.COMMA)
            self.state = 111
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = D96Parser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(D96Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 116
            self.match(D96Parser.LP)
            self.state = 117
            self.parameter_list()
            self.state = 118
            self.match(D96Parser.RP)
            self.state = 119
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_declaration" ):
                return visitor.visitConstructor_declaration(self)
            else:
                return visitor.visitChildren(self)




    def constructor_declaration(self):

        localctx = D96Parser.Constructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constructor_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 122
            self.match(D96Parser.LP)
            self.state = 123
            self.parameter_list()
            self.state = 124
            self.match(D96Parser.RP)
            self.state = 125
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_declaration" ):
                return visitor.visitDestructor_declaration(self)
            else:
                return visitor.visitChildren(self)




    def destructor_declaration(self):

        localctx = D96Parser.Destructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_destructor_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(D96Parser.DESTRUCTOR)
            self.state = 128
            self.match(D96Parser.LP)
            self.state = 129
            self.match(D96Parser.RP)
            self.state = 130
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Parameter_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Parameter_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = D96Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ID:
                self.state = 132
                self.parameter_declaration()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = D96Parser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(D96Parser.ID)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 139
                self.match(D96Parser.COMMA)
                self.state = 140
                self.match(D96Parser.ID)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(D96Parser.COLON)
            self.state = 147
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(D96Parser.LCB)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.T__0) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOR) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.RETURN) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 150
                self.statement()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_and_const_declaration(self):
            return self.getTypedRuleContext(D96Parser.Variable_and_const_declarationContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def foreach_statement(self):
            return self.getTypedRuleContext(D96Parser.Foreach_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext,0)


        def method_invocation_statement(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.variable_and_const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.foreach_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 164
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 165
                self.method_invocation_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_and_const_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def initialization(self):
            return self.getTypedRuleContext(D96Parser.InitializationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_and_const_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_and_const_declaration" ):
                return visitor.visitVariable_and_const_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_and_const_declaration(self):

        localctx = D96Parser.Variable_and_const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_variable_and_const_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 169
            self.match(D96Parser.ID)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 170
                self.match(D96Parser.COMMA)
                self.state = 171
                self.match(D96Parser.ID)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self.match(D96Parser.COLON)
            self.state = 178
            self.type_name()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__0:
                self.state = 179
                self.initialization()


            self.state = 182
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_hand_side(self):
            return self.getTypedRuleContext(D96Parser.Left_hand_sideContext,0)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.left_hand_side()
            self.state = 185
            self.match(D96Parser.EQUAL)
            self.state = 186
            self.expression()
            self.state = 187
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_hand_sideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_left_hand_side

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_hand_side" ):
                return visitor.visitLeft_hand_side(self)
            else:
                return visitor.visitChildren(self)




    def left_hand_side(self):

        localctx = D96Parser.Left_hand_sideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_left_hand_side)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.index_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def elseif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elseif_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elseif_statementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(D96Parser.IF)
                self.state = 195
                self.match(D96Parser.LP)
                self.state = 196
                self.expression()
                self.state = 197
                self.match(D96Parser.RP)
                self.state = 198
                self.block_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(D96Parser.IF)
                self.state = 201
                self.match(D96Parser.LP)
                self.state = 202
                self.expression()
                self.state = 203
                self.match(D96Parser.RP)
                self.state = 204
                self.block_statement()
                self.state = 205
                self.else_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(D96Parser.IF)
                self.state = 208
                self.match(D96Parser.LP)
                self.state = 209
                self.expression()
                self.state = 210
                self.match(D96Parser.RP)
                self.state = 211
                self.block_statement()
                self.state = 213 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 212
                    self.elseif_statement()
                    self.state = 215 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.match(D96Parser.IF)
                self.state = 218
                self.match(D96Parser.LP)
                self.state = 219
                self.expression()
                self.state = 220
                self.match(D96Parser.RP)
                self.state = 221
                self.block_statement()
                self.state = 223 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 222
                    self.elseif_statement()
                    self.state = 225 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                self.state = 227
                self.else_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_statement" ):
                return visitor.visitElseif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(D96Parser.ELSEIF)
            self.state = 232
            self.match(D96Parser.LP)
            self.state = 233
            self.expression()
            self.state = 234
            self.match(D96Parser.RP)
            self.state = 235
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = D96Parser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(D96Parser.ELSE)
            self.state = 238
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(D96Parser.FOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach_statement" ):
                return visitor.visitForeach_statement(self)
            else:
                return visitor.visitChildren(self)




    def foreach_statement(self):

        localctx = D96Parser.Foreach_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(D96Parser.FOR)
            self.state = 241
            self.match(D96Parser.LP)
            self.state = 242
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 243
            self.match(D96Parser.IN)
            self.state = 244
            self.expression()
            self.state = 245
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 246
            self.expression()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 247
                self.match(D96Parser.BY)
                self.state = 248
                self.expression()


            self.state = 251
            self.match(D96Parser.RP)
            self.state = 252
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(D96Parser.BREAK)
            self.state = 255
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(D96Parser.CONTINUE)
            self.state = 258
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_return_statement)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(D96Parser.RETURN)
                self.state = 261
                self.expression()
                self.state = 262
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(D96Parser.RETURN)
                self.state = 265
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(D96Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(D96Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)




    def index_expression(self):

        localctx = D96Parser.Index_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_index_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(D96Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(D96Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_normal_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_literal" ):
                return visitor.visitNormal_literal(self)
            else:
                return visitor.visitChildren(self)




    def normal_literal(self):

        localctx = D96Parser.Normal_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_normal_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(D96Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





