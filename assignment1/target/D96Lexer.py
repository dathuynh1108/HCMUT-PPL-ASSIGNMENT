# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\7\2\u0087\n\2\f\2\16\2\u008a\13\2\5\2\u008c\n\2\3\3\3")
        buf.write("\3\6\3\u0090\n\3\r\3\16\3\u0091\3\4\3\4\3\4\6\4\u0097")
        buf.write("\n\4\r\4\16\4\u0098\3\5\3\5\3\5\6\5\u009e\n\5\r\5\16\5")
        buf.write("\u009f\3\6\3\6\3\6\5\6\u00a5\n\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\5\t\u00b0\n\t\3\n\3\n\3\13\6\13\u00b5\n")
        buf.write("\13\r\13\16\13\u00b6\3\f\3\f\3\f\3\r\3\r\5\r\u00be\n\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\7\16\u00c6\n\16\f\16\16\16")
        buf.write("\u00c9\13\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00d1")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\58\u016c\n8\38\3")
        buf.write("8\78\u0170\n8\f8\168\u0173\138\39\39\39\39\59\u0179\n")
        buf.write("9\39\39\3:\3:\7:\u017f\n:\f:\16:\u0182\13:\3:\3:\3:\3")
        buf.write(";\3;\5;\u0189\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\6=\u0196")
        buf.write("\n=\r=\16=\u0197\3=\3=\3>\3>\3>\3>\3>\3>\5>\u01a2\n>\5")
        buf.write(">\u01a4\n>\3>\3>\3>\3?\3?\7?\u01ab\n?\f?\16?\u01ae\13")
        buf.write("?\3?\5?\u01b1\n?\3?\3?\3@\3@\7@\u01b7\n@\f@\16@\u01ba")
        buf.write("\13@\3@\3@\3@\3A\3A\3A\3\u00c7\2B\3\2\5\2\7\2\t\2\13\2")
        buf.write("\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\3\35\4\37\5!\6#")
        buf.write("\7%\b\'\t)\n+\13-\f/\r\61\16\63\17\65\20\67\219\22;\23")
        buf.write("=\24?\25A\26C\27E\30G\31I\32K\33M\34O\35Q\36S\37U W!Y")
        buf.write("\"[#]$_%a&c\'e(g)i*k+m,o-q.s/u\60w\61y\62{\63}\64\177")
        buf.write("\65\u0081\66\3\2\23\4\2\63;aa\4\2\62;aa\4\2\629aa\4\2")
        buf.write("DDdd\4\2\62\63aa\4\2ZZzz\6\2\62;CHaach\7\2\n\f\16\17$")
        buf.write("$))^^\t\2))^^ddhhppttvv\3\2^^\4\2--//\4\2GGgg\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\3\2%%\7\3\n\f\16")
        buf.write("\17$$))^^\2\u01cc\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\3\u008b\3\2\2\2\5\u008d\3\2\2\2")
        buf.write("\7\u0093\3\2\2\2\t\u009a\3\2\2\2\13\u00a4\3\2\2\2\r\u00a6")
        buf.write("\3\2\2\2\17\u00a9\3\2\2\2\21\u00af\3\2\2\2\23\u00b1\3")
        buf.write("\2\2\2\25\u00b4\3\2\2\2\27\u00b8\3\2\2\2\31\u00bb\3\2")
        buf.write("\2\2\33\u00c1\3\2\2\2\35\u00d2\3\2\2\2\37\u00d8\3\2\2")
        buf.write("\2!\u00e1\3\2\2\2#\u00e4\3\2\2\2%\u00eb\3\2\2\2\'\u00f0")
        buf.write("\3\2\2\2)\u00f8\3\2\2\2+\u00fd\3\2\2\2-\u0103\3\2\2\2")
        buf.write("/\u0109\3\2\2\2\61\u010f\3\2\2\2\63\u0113\3\2\2\2\65\u0119")
        buf.write("\3\2\2\2\67\u0121\3\2\2\29\u0128\3\2\2\2;\u012d\3\2\2")
        buf.write("\2=\u012f\3\2\2\2?\u0131\3\2\2\2A\u0133\3\2\2\2C\u0135")
        buf.write("\3\2\2\2E\u0137\3\2\2\2G\u0139\3\2\2\2I\u013c\3\2\2\2")
        buf.write("K\u013f\3\2\2\2M\u0142\3\2\2\2O\u0144\3\2\2\2Q\u0147\3")
        buf.write("\2\2\2S\u0149\3\2\2\2U\u014c\3\2\2\2W\u014e\3\2\2\2Y\u0151")
        buf.write("\3\2\2\2[\u0155\3\2\2\2]\u0158\3\2\2\2_\u015a\3\2\2\2")
        buf.write("a\u015c\3\2\2\2c\u015e\3\2\2\2e\u0160\3\2\2\2g\u0162\3")
        buf.write("\2\2\2i\u0164\3\2\2\2k\u0166\3\2\2\2m\u0168\3\2\2\2o\u016b")
        buf.write("\3\2\2\2q\u0178\3\2\2\2s\u017c\3\2\2\2u\u0188\3\2\2\2")
        buf.write("w\u018a\3\2\2\2y\u0195\3\2\2\2{\u019b\3\2\2\2}\u01a8\3")
        buf.write("\2\2\2\177\u01b4\3\2\2\2\u0081\u01be\3\2\2\2\u0083\u008c")
        buf.write("\7\62\2\2\u0084\u0088\t\2\2\2\u0085\u0087\t\3\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3")
        buf.write("\2\2\2\u008b\u0083\3\2\2\2\u008b\u0084\3\2\2\2\u008c\4")
        buf.write("\3\2\2\2\u008d\u008f\7\62\2\2\u008e\u0090\t\4\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\6\3\2\2\2\u0093\u0094\7\62")
        buf.write("\2\2\u0094\u0096\t\5\2\2\u0095\u0097\t\6\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\b\3\2\2\2\u009a\u009b\7\62\2\2\u009b")
        buf.write("\u009d\t\7\2\2\u009c\u009e\t\b\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\n\3\2\2\2\u00a1\u00a5\n\t\2\2\u00a2\u00a5")
        buf.write("\5\r\7\2\u00a3\u00a5\5\17\b\2\u00a4\u00a1\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\f\3\2\2\2\u00a6")
        buf.write("\u00a7\7^\2\2\u00a7\u00a8\t\n\2\2\u00a8\16\3\2\2\2\u00a9")
        buf.write("\u00aa\7)\2\2\u00aa\u00ab\7$\2\2\u00ab\20\3\2\2\2\u00ac")
        buf.write("\u00ad\7^\2\2\u00ad\u00b0\n\n\2\2\u00ae\u00b0\n\13\2\2")
        buf.write("\u00af\u00ac\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\22\3\2")
        buf.write("\2\2\u00b1\u00b2\t\f\2\2\u00b2\24\3\2\2\2\u00b3\u00b5")
        buf.write("\t\3\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\26\3\2\2\2\u00b8")
        buf.write("\u00b9\13\2\2\2\u00b9\u00ba\5\25\13\2\u00ba\30\3\2\2\2")
        buf.write("\u00bb\u00bd\t\r\2\2\u00bc\u00be\5\23\n\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c0\5\25\13\2\u00c0\32\3\2\2\2\u00c1\u00c2\7%\2\2\u00c2")
        buf.write("\u00c3\7%\2\2\u00c3\u00c7\3\2\2\2\u00c4\u00c6\13\2\2\2")
        buf.write("\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c8\3")
        buf.write("\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00d0\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00ca\u00cb\7%\2\2\u00cb\u00cc\7%\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00d1\b\16\2\2\u00ce\u00cf\7\2\2\3\u00cf")
        buf.write("\u00d1\b\16\3\2\u00d0\u00ca\3\2\2\2\u00d0\u00ce\3\2\2")
        buf.write("\2\u00d1\34\3\2\2\2\u00d2\u00d3\7D\2\2\u00d3\u00d4\7t")
        buf.write("\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7m\2\2\u00d7\36\3\2\2\2\u00d8\u00d9\7E\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd")
        buf.write("\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7w\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0 \3\2\2\2\u00e1\u00e2\7K\2\2\u00e2\u00e3")
        buf.write("\7h\2\2\u00e3\"\3\2\2\2\u00e4\u00e5\7G\2\2\u00e5\u00e6")
        buf.write("\7n\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7h\2\2\u00ea$\3\2\2\2\u00eb\u00ec")
        buf.write("\7G\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef&\3\2\2\2\u00f0\u00f1\7H\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7\7j\2\2\u00f7(\3")
        buf.write("\2\2\2\u00f8\u00f9\7V\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7g\2\2\u00fc*\3\2\2\2\u00fd\u00fe")
        buf.write("\7H\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7n\2\2\u0100\u0101")
        buf.write("\7u\2\2\u0101\u0102\7g\2\2\u0102,\3\2\2\2\u0103\u0104")
        buf.write("\7e\2\2\u0104\u0105\7n\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7u\2\2\u0107\u0108\7u\2\2\u0108.\3\2\2\2\u0109\u010a")
        buf.write("\7C\2\2\u010a\u010b\7t\2\2\u010b\u010c\7t\2\2\u010c\u010d")
        buf.write("\7c\2\2\u010d\u010e\7{\2\2\u010e\60\3\2\2\2\u010f\u0110")
        buf.write("\7K\2\2\u0110\u0111\7p\2\2\u0111\u0112\7v\2\2\u0112\62")
        buf.write("\3\2\2\2\u0113\u0114\7H\2\2\u0114\u0115\7n\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\u0117\7c\2\2\u0117\u0118\7v\2\2\u0118\64")
        buf.write("\3\2\2\2\u0119\u011a\7D\2\2\u011a\u011b\7q\2\2\u011b\u011c")
        buf.write("\7q\2\2\u011c\u011d\7n\2\2\u011d\u011e\7g\2\2\u011e\u011f")
        buf.write("\7c\2\2\u011f\u0120\7p\2\2\u0120\66\3\2\2\2\u0121\u0122")
        buf.write("\7U\2\2\u0122\u0123\7v\2\2\u0123\u0124\7t\2\2\u0124\u0125")
        buf.write("\7k\2\2\u0125\u0126\7p\2\2\u0126\u0127\7i\2\2\u01278\3")
        buf.write("\2\2\2\u0128\u0129\7P\2\2\u0129\u012a\7w\2\2\u012a\u012b")
        buf.write("\7n\2\2\u012b\u012c\7n\2\2\u012c:\3\2\2\2\u012d\u012e")
        buf.write("\7-\2\2\u012e<\3\2\2\2\u012f\u0130\7/\2\2\u0130>\3\2\2")
        buf.write("\2\u0131\u0132\7,\2\2\u0132@\3\2\2\2\u0133\u0134\7\61")
        buf.write("\2\2\u0134B\3\2\2\2\u0135\u0136\7\'\2\2\u0136D\3\2\2\2")
        buf.write("\u0137\u0138\7#\2\2\u0138F\3\2\2\2\u0139\u013a\7(\2\2")
        buf.write("\u013a\u013b\7(\2\2\u013bH\3\2\2\2\u013c\u013d\7~\2\2")
        buf.write("\u013d\u013e\7~\2\2\u013eJ\3\2\2\2\u013f\u0140\7?\2\2")
        buf.write("\u0140\u0141\7?\2\2\u0141L\3\2\2\2\u0142\u0143\7?\2\2")
        buf.write("\u0143N\3\2\2\2\u0144\u0145\7#\2\2\u0145\u0146\7?\2\2")
        buf.write("\u0146P\3\2\2\2\u0147\u0148\7>\2\2\u0148R\3\2\2\2\u0149")
        buf.write("\u014a\7>\2\2\u014a\u014b\7?\2\2\u014bT\3\2\2\2\u014c")
        buf.write("\u014d\7@\2\2\u014dV\3\2\2\2\u014e\u014f\7@\2\2\u014f")
        buf.write("\u0150\7?\2\2\u0150X\3\2\2\2\u0151\u0152\7?\2\2\u0152")
        buf.write("\u0153\7?\2\2\u0153\u0154\7\60\2\2\u0154Z\3\2\2\2\u0155")
        buf.write("\u0156\7-\2\2\u0156\u0157\7\60\2\2\u0157\\\3\2\2\2\u0158")
        buf.write("\u0159\7*\2\2\u0159^\3\2\2\2\u015a\u015b\7+\2\2\u015b")
        buf.write("`\3\2\2\2\u015c\u015d\7]\2\2\u015db\3\2\2\2\u015e\u015f")
        buf.write("\7_\2\2\u015fd\3\2\2\2\u0160\u0161\7\60\2\2\u0161f\3\2")
        buf.write("\2\2\u0162\u0163\7.\2\2\u0163h\3\2\2\2\u0164\u0165\7=")
        buf.write("\2\2\u0165j\3\2\2\2\u0166\u0167\7}\2\2\u0167l\3\2\2\2")
        buf.write("\u0168\u0169\7\177\2\2\u0169n\3\2\2\2\u016a\u016c\7&\2")
        buf.write("\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016d\u0171\t\16\2\2\u016e\u0170\t\17\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2")
        buf.write("\u0171\u0172\3\2\2\2\u0172p\3\2\2\2\u0173\u0171\3\2\2")
        buf.write("\2\u0174\u0179\5\3\2\2\u0175\u0179\5\5\3\2\u0176\u0179")
        buf.write("\5\t\5\2\u0177\u0179\5\7\4\2\u0178\u0174\3\2\2\2\u0178")
        buf.write("\u0175\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017b\b9\4\2\u017br\3\2\2\2")
        buf.write("\u017c\u0180\7$\2\2\u017d\u017f\5\13\6\2\u017e\u017d\3")
        buf.write("\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0180\3\2\2\2\u0183")
        buf.write("\u0184\7$\2\2\u0184\u0185\b:\5\2\u0185t\3\2\2\2\u0186")
        buf.write("\u0189\5)\25\2\u0187\u0189\5+\26\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0187\3\2\2\2\u0189v\3\2\2\2\u018a\u018b\7C\2\2")
        buf.write("\u018b\u018c\7t\2\2\u018c\u018d\7t\2\2\u018d\u018e\7c")
        buf.write("\2\2\u018e\u018f\7{\2\2\u018f\u0190\3\2\2\2\u0190\u0191")
        buf.write("\7*\2\2\u0191\u0192\3\2\2\2\u0192\u0193\7+\2\2\u0193x")
        buf.write("\3\2\2\2\u0194\u0196\t\20\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199\u019a\b=\6\2\u019az\3\2\2\2")
        buf.write("\u019b\u019c\7%\2\2\u019c\u019d\7%\2\2\u019d\u01a3\3\2")
        buf.write("\2\2\u019e\u019f\n\21\2\2\u019f\u01a4\n\21\2\2\u01a0\u01a2")
        buf.write("\13\2\2\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a4\3\2\2\2\u01a3\u019e\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a6\7\2\2\3\u01a6\u01a7\b")
        buf.write(">\7\2\u01a7|\3\2\2\2\u01a8\u01ac\7$\2\2\u01a9\u01ab\5")
        buf.write("\13\6\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01b0\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01af\u01b1\t\22\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\b?\b\2\u01b3")
        buf.write("~\3\2\2\2\u01b4\u01b8\7$\2\2\u01b5\u01b7\5\13\6\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3")
        buf.write("\2\2\2\u01bb\u01bc\5\21\t\2\u01bc\u01bd\b@\t\2\u01bd\u0080")
        buf.write("\3\2\2\2\u01be\u01bf\13\2\2\2\u01bf\u01c0\bA\n\2\u01c0")
        buf.write("\u0082\3\2\2\2\31\2\u0088\u008b\u0091\u0098\u009f\u00a4")
        buf.write("\u00af\u00b6\u00bd\u00c7\u00d0\u016b\u0171\u0178\u0180")
        buf.write("\u0188\u0197\u01a1\u01a3\u01ac\u01b0\u01b8\13\3\16\2\3")
        buf.write("\16\3\39\4\3:\5\b\2\2\3>\6\3?\7\3@\b\3A\t")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSEIF = 5
    ELSE = 6
    FOREACH = 7
    TRUE = 8
    FALSE = 9
    CLASS = 10
    ARRAY = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    STRING = 15
    NULL = 16
    ADD = 17
    SUB = 18
    MUL = 19
    DIV = 20
    MOD = 21
    NOT = 22
    AND = 23
    OR = 24
    EQUAL = 25
    ASSIGN = 26
    NOT_EQUAL = 27
    LT = 28
    LTE = 29
    GT = 30
    GTE = 31
    STRING_EQUAL = 32
    STRING_ADD = 33
    LP = 34
    RP = 35
    LSB = 36
    RSB = 37
    DOT = 38
    COMMA = 39
    SEMI = 40
    LCB = 41
    RCB = 42
    ID = 43
    INTEGER_LITERAL = 44
    STRING_LITERAL = 45
    BOOLEAN_LITERAL = 46
    INDEXED_ARRAY = 47
    WS = 48
    UNTERMINATED_COMMENT = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_TOKEN = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'class'", "'Array'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Null'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'==.'", "'+.'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", 
            "STRING", "NULL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", 
            "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", "LSB", "RSB", 
            "DOT", "COMMA", "SEMI", "LCB", "RCB", "ID", "INTEGER_LITERAL", 
            "STRING_LITERAL", "BOOLEAN_LITERAL", "INDEXED_ARRAY", "WS", 
            "UNTERMINATED_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_TOKEN" ]

    ruleNames = [ "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", 
                  "HEX_INTEGER_LITERAL", "STRING_CHAR", "ESCAPE_SEQUENCE", 
                  "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", "SIGN", "FLOAT_INTEGER_PART", 
                  "FLOAT_DECIMAL_PART", "FLOAT_EXPONENT_PART", "COMMENT", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "NULL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", 
                  "GT", "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "SEMI", "LCB", "RCB", "ID", 
                  "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                  "INDEXED_ARRAY", "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[12] = self.COMMENT_action 
            actions[55] = self.INTEGER_LITERAL_action 
            actions[56] = self.STRING_LITERAL_action 
            actions[60] = self.UNTERMINATED_COMMENT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                channel(HIDDEN)

     

        if actionIndex == 1:

                raise UNTERMINATED_COMMENT(self.text)

     

    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text.translate(str.maketrans('','','_'))

     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	self.text = self.text[1:-1]

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise UNTERMINATED_COMMENT(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                y = str(self.text)
                possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
                if y[-1] in possible:
                    raise UNCLOSE_STRING(y[1:-1])
                else:
                    raise UNCLOSE_STRING(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                    raise ILLEGAL_ESCAPE(self.text[1:])
                
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

                    raise ERROR_TOKEN(self.text)
                
     


