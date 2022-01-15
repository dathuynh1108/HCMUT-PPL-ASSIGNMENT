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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u021d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\5\2\u009e\n\2\3\2\7\2\u00a1\n\2\f\2\16")
        buf.write("\2\u00a4\13\2\3\2\5\2\u00a7\n\2\3\3\3\3\6\3\u00ab\n\3")
        buf.write("\r\3\16\3\u00ac\3\4\3\4\3\4\6\4\u00b2\n\4\r\4\16\4\u00b3")
        buf.write("\3\5\3\5\3\5\6\5\u00b9\n\5\r\5\16\5\u00ba\3\6\3\6\3\6")
        buf.write("\5\6\u00c0\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00cc\n\t\3\n\3\n\3\13\3\13\5\13\u00d2\n\13\3\13")
        buf.write("\7\13\u00d5\n\13\f\13\16\13\u00d8\13\13\3\f\3\f\7\f\u00dc")
        buf.write("\n\f\f\f\16\f\u00df\13\f\3\r\3\r\5\r\u00e3\n\r\3\r\6\r")
        buf.write("\u00e6\n\r\r\r\16\r\u00e7\3\16\3\16\3\16\3\16\7\16\u00ee")
        buf.write("\n\16\f\16\16\16\u00f1\13\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\5\'\u018c\n\'\3\'\3\'\3(\3(\7(\u0192\n(\f(\16(\u0195")
        buf.write("\13(\3(\3(\3(\3)\3)\5)\u019c\n)\3*\3*\3*\5*\u01a1\n*\3")
        buf.write("*\3*\3*\3*\3*\3*\5*\u01a9\n*\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\39\39\39\3:\3:\3:\3:\3;\3;\3;\3<\3<\3=\3=")
        buf.write("\3>\3>\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3")
        buf.write("E\3F\3F\3G\3G\3H\3H\7H\u01f4\nH\fH\16H\u01f7\13H\3I\3")
        buf.write("I\3I\7I\u01fc\nI\fI\16I\u01ff\13I\3J\6J\u0202\nJ\rJ\16")
        buf.write("J\u0203\3J\3J\3K\3K\7K\u020a\nK\fK\16K\u020d\13K\3K\3")
        buf.write("K\3L\3L\7L\u0213\nL\fL\16L\u0216\13L\3L\3L\3L\3M\3M\3")
        buf.write("M\3\u00ef\2N\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25")
        buf.write("\2\27\2\31\2\33\3\35\4\37\5!\6#\7%\b\'\t)\2+\2-\n/\13")
        buf.write("\61\f\63\r\65\16\67\179\20;\21=\22?\23A\24C\25E\26G\27")
        buf.write("I\30K\31M\32O\33Q\34S\35U\36W\37Y [!]\"_#a$c%e&g\'i(k")
        buf.write(")m*o+q,s-u.w/y\60{\61}\62\177\63\u0081\64\u0083\65\u0085")
        buf.write("\66\u0087\67\u00898\u008b9\u008d:\u008f;\u0091<\u0093")
        buf.write("=\u0095>\u0097?\u0099@\3\2\21\3\2\63;\3\2\62;\3\2\629")
        buf.write("\4\2DDdd\3\2\62\63\4\2ZZzz\5\2\62;CHch\7\2\f\f\17\17$")
        buf.write("$))^^\t\2))^^ddhhppttvv\3\2$$\4\2--//\4\2GGgg\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\2\u022a\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\3\u00a6\3\2\2\2\5\u00a8\3\2\2\2\7\u00ae\3\2\2\2\t\u00b5")
        buf.write("\3\2\2\2\13\u00bf\3\2\2\2\r\u00c1\3\2\2\2\17\u00c4\3\2")
        buf.write("\2\2\21\u00cb\3\2\2\2\23\u00cd\3\2\2\2\25\u00cf\3\2\2")
        buf.write("\2\27\u00d9\3\2\2\2\31\u00e0\3\2\2\2\33\u00e9\3\2\2\2")
        buf.write("\35\u00f7\3\2\2\2\37\u00fd\3\2\2\2!\u0106\3\2\2\2#\u0109")
        buf.write("\3\2\2\2%\u0110\3\2\2\2\'\u0115\3\2\2\2)\u011d\3\2\2\2")
        buf.write("+\u0122\3\2\2\2-\u0128\3\2\2\2/\u012c\3\2\2\2\61\u0130")
        buf.write("\3\2\2\2\63\u0135\3\2\2\2\65\u013c\3\2\2\2\67\u013f\3")
        buf.write("\2\2\29\u0142\3\2\2\2;\u0146\3\2\2\2=\u0152\3\2\2\2?\u015d")
        buf.write("\3\2\2\2A\u0162\3\2\2\2C\u0168\3\2\2\2E\u016e\3\2\2\2")
        buf.write("G\u0172\3\2\2\2I\u0178\3\2\2\2K\u0180\3\2\2\2M\u018b\3")
        buf.write("\2\2\2O\u018f\3\2\2\2Q\u019b\3\2\2\2S\u01a8\3\2\2\2U\u01ac")
        buf.write("\3\2\2\2W\u01ae\3\2\2\2Y\u01b0\3\2\2\2[\u01b2\3\2\2\2")
        buf.write("]\u01b4\3\2\2\2_\u01b6\3\2\2\2a\u01b8\3\2\2\2c\u01bb\3")
        buf.write("\2\2\2e\u01be\3\2\2\2g\u01c1\3\2\2\2i\u01c3\3\2\2\2k\u01c6")
        buf.write("\3\2\2\2m\u01c8\3\2\2\2o\u01cb\3\2\2\2q\u01cd\3\2\2\2")
        buf.write("s\u01d0\3\2\2\2u\u01d4\3\2\2\2w\u01d7\3\2\2\2y\u01d9\3")
        buf.write("\2\2\2{\u01db\3\2\2\2}\u01dd\3\2\2\2\177\u01df\3\2\2\2")
        buf.write("\u0081\u01e1\3\2\2\2\u0083\u01e4\3\2\2\2\u0085\u01e6\3")
        buf.write("\2\2\2\u0087\u01e8\3\2\2\2\u0089\u01ea\3\2\2\2\u008b\u01ed")
        buf.write("\3\2\2\2\u008d\u01ef\3\2\2\2\u008f\u01f1\3\2\2\2\u0091")
        buf.write("\u01f8\3\2\2\2\u0093\u0201\3\2\2\2\u0095\u0207\3\2\2\2")
        buf.write("\u0097\u0210\3\2\2\2\u0099\u021a\3\2\2\2\u009b\u00a2\t")
        buf.write("\2\2\2\u009c\u009e\7a\2\2\u009d\u009c\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1\t\3\2\2\u00a0")
        buf.write("\u009d\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a7\3\2\2\2\u00a4\u00a2\3")
        buf.write("\2\2\2\u00a5\u00a7\7\62\2\2\u00a6\u009b\3\2\2\2\u00a6")
        buf.write("\u00a5\3\2\2\2\u00a7\4\3\2\2\2\u00a8\u00aa\7\62\2\2\u00a9")
        buf.write("\u00ab\t\4\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\6\3\2\2")
        buf.write("\2\u00ae\u00af\7\62\2\2\u00af\u00b1\t\5\2\2\u00b0\u00b2")
        buf.write("\t\6\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\b\3\2\2\2\u00b5")
        buf.write("\u00b6\7\62\2\2\u00b6\u00b8\t\7\2\2\u00b7\u00b9\t\b\2")
        buf.write("\2\u00b8\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\n\3\2\2\2\u00bc\u00c0")
        buf.write("\n\t\2\2\u00bd\u00c0\5\r\7\2\u00be\u00c0\5\17\b\2\u00bf")
        buf.write("\u00bc\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2")
        buf.write("\u00c0\f\3\2\2\2\u00c1\u00c2\7^\2\2\u00c2\u00c3\t\n\2")
        buf.write("\2\u00c3\16\3\2\2\2\u00c4\u00c5\7)\2\2\u00c5\u00c6\7$")
        buf.write("\2\2\u00c6\20\3\2\2\2\u00c7\u00c8\7^\2\2\u00c8\u00cc\n")
        buf.write("\n\2\2\u00c9\u00ca\7)\2\2\u00ca\u00cc\n\13\2\2\u00cb\u00c7")
        buf.write("\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\22\3\2\2\2\u00cd\u00ce")
        buf.write("\t\f\2\2\u00ce\24\3\2\2\2\u00cf\u00d6\t\3\2\2\u00d0\u00d2")
        buf.write("\7a\2\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d5\t\3\2\2\u00d4\u00d1\3\2\2\2")
        buf.write("\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3")
        buf.write("\2\2\2\u00d7\26\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00dd")
        buf.write("\7\60\2\2\u00da\u00dc\t\3\2\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write("\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\30\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e2\t\r")
        buf.write("\2\2\u00e1\u00e3\5\23\n\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e6\t\3\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e5\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\32\3\2\2\2\u00e9\u00ea\7%\2")
        buf.write("\2\u00ea\u00eb\7%\2\2\u00eb\u00ef\3\2\2\2\u00ec\u00ee")
        buf.write("\13\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f2\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7%\2\2\u00f3\u00f4\7")
        buf.write("%\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\b\16\2\2\u00f6\34")
        buf.write("\3\2\2\2\u00f7\u00f8\7D\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7m\2\2\u00fc\36")
        buf.write("\3\2\2\2\u00fd\u00fe\7E\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7v\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write("\7p\2\2\u0103\u0104\7w\2\2\u0104\u0105\7g\2\2\u0105 \3")
        buf.write("\2\2\2\u0106\u0107\7K\2\2\u0107\u0108\7h\2\2\u0108\"\3")
        buf.write("\2\2\2\u0109\u010a\7G\2\2\u010a\u010b\7n\2\2\u010b\u010c")
        buf.write("\7u\2\2\u010c\u010d\7g\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7h\2\2\u010f$\3\2\2\2\u0110\u0111\7G\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114\7g\2\2\u0114&\3")
        buf.write("\2\2\2\u0115\u0116\7H\2\2\u0116\u0117\7q\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7g\2\2\u0119\u011a\7c\2\2\u011a\u011b")
        buf.write("\7e\2\2\u011b\u011c\7j\2\2\u011c(\3\2\2\2\u011d\u011e")
        buf.write("\7V\2\2\u011e\u011f\7t\2\2\u011f\u0120\7w\2\2\u0120\u0121")
        buf.write("\7g\2\2\u0121*\3\2\2\2\u0122\u0123\7H\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7n\2\2\u0125\u0126\7u\2\2\u0126\u0127")
        buf.write("\7g\2\2\u0127,\3\2\2\2\u0128\u0129\7X\2\2\u0129\u012a")
        buf.write("\7c\2\2\u012a\u012b\7t\2\2\u012b.\3\2\2\2\u012c\u012d")
        buf.write("\7X\2\2\u012d\u012e\7c\2\2\u012e\u012f\7n\2\2\u012f\60")
        buf.write("\3\2\2\2\u0130\u0131\7U\2\2\u0131\u0132\7g\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133\u0134\7h\2\2\u0134\62\3\2\2\2\u0135\u0136")
        buf.write("\7T\2\2\u0136\u0137\7g\2\2\u0137\u0138\7v\2\2\u0138\u0139")
        buf.write("\7w\2\2\u0139\u013a\7t\2\2\u013a\u013b\7p\2\2\u013b\64")
        buf.write("\3\2\2\2\u013c\u013d\7K\2\2\u013d\u013e\7p\2\2\u013e\66")
        buf.write("\3\2\2\2\u013f\u0140\7D\2\2\u0140\u0141\7{\2\2\u01418")
        buf.write("\3\2\2\2\u0142\u0143\7P\2\2\u0143\u0144\7g\2\2\u0144\u0145")
        buf.write("\7y\2\2\u0145:\3\2\2\2\u0146\u0147\7E\2\2\u0147\u0148")
        buf.write("\7q\2\2\u0148\u0149\7p\2\2\u0149\u014a\7u\2\2\u014a\u014b")
        buf.write("\7v\2\2\u014b\u014c\7t\2\2\u014c\u014d\7w\2\2\u014d\u014e")
        buf.write("\7e\2\2\u014e\u014f\7v\2\2\u014f\u0150\7q\2\2\u0150\u0151")
        buf.write("\7t\2\2\u0151<\3\2\2\2\u0152\u0153\7F\2\2\u0153\u0154")
        buf.write("\7g\2\2\u0154\u0155\7u\2\2\u0155\u0156\7v\2\2\u0156\u0157")
        buf.write("\7t\2\2\u0157\u0158\7w\2\2\u0158\u0159\7e\2\2\u0159\u015a")
        buf.write("\7v\2\2\u015a\u015b\7q\2\2\u015b\u015c\7t\2\2\u015c>\3")
        buf.write("\2\2\2\u015d\u015e\7P\2\2\u015e\u015f\7w\2\2\u015f\u0160")
        buf.write("\7n\2\2\u0160\u0161\7n\2\2\u0161@\3\2\2\2\u0162\u0163")
        buf.write("\7E\2\2\u0163\u0164\7n\2\2\u0164\u0165\7c\2\2\u0165\u0166")
        buf.write("\7u\2\2\u0166\u0167\7u\2\2\u0167B\3\2\2\2\u0168\u0169")
        buf.write("\7C\2\2\u0169\u016a\7t\2\2\u016a\u016b\7t\2\2\u016b\u016c")
        buf.write("\7c\2\2\u016c\u016d\7{\2\2\u016dD\3\2\2\2\u016e\u016f")
        buf.write("\7K\2\2\u016f\u0170\7p\2\2\u0170\u0171\7v\2\2\u0171F\3")
        buf.write("\2\2\2\u0172\u0173\7H\2\2\u0173\u0174\7n\2\2\u0174\u0175")
        buf.write("\7q\2\2\u0175\u0176\7c\2\2\u0176\u0177\7v\2\2\u0177H\3")
        buf.write("\2\2\2\u0178\u0179\7D\2\2\u0179\u017a\7q\2\2\u017a\u017b")
        buf.write("\7q\2\2\u017b\u017c\7n\2\2\u017c\u017d\7g\2\2\u017d\u017e")
        buf.write("\7c\2\2\u017e\u017f\7p\2\2\u017fJ\3\2\2\2\u0180\u0181")
        buf.write("\7U\2\2\u0181\u0182\7v\2\2\u0182\u0183\7t\2\2\u0183\u0184")
        buf.write("\7k\2\2\u0184\u0185\7p\2\2\u0185\u0186\7i\2\2\u0186L\3")
        buf.write("\2\2\2\u0187\u018c\5\3\2\2\u0188\u018c\5\5\3\2\u0189\u018c")
        buf.write("\5\t\5\2\u018a\u018c\5\7\4\2\u018b\u0187\3\2\2\2\u018b")
        buf.write("\u0188\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018d\u018e\b\'\3\2\u018eN\3\2\2")
        buf.write("\2\u018f\u0193\7$\2\2\u0190\u0192\5\13\6\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0196\u0197\7$\2\2\u0197\u0198\b(\4\2\u0198P\3\2\2\2")
        buf.write("\u0199\u019c\5)\25\2\u019a\u019c\5+\26\2\u019b\u0199\3")
        buf.write("\2\2\2\u019b\u019a\3\2\2\2\u019cR\3\2\2\2\u019d\u019e")
        buf.write("\5\25\13\2\u019e\u01a0\5\27\f\2\u019f\u01a1\5\31\r\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a9\3\2\2\2")
        buf.write("\u01a2\u01a3\5\25\13\2\u01a3\u01a4\5\31\r\2\u01a4\u01a9")
        buf.write("\3\2\2\2\u01a5\u01a6\5\27\f\2\u01a6\u01a7\5\31\r\2\u01a7")
        buf.write("\u01a9\3\2\2\2\u01a8\u019d\3\2\2\2\u01a8\u01a2\3\2\2\2")
        buf.write("\u01a8\u01a5\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\b")
        buf.write("*\5\2\u01abT\3\2\2\2\u01ac\u01ad\7-\2\2\u01adV\3\2\2\2")
        buf.write("\u01ae\u01af\7/\2\2\u01afX\3\2\2\2\u01b0\u01b1\7,\2\2")
        buf.write("\u01b1Z\3\2\2\2\u01b2\u01b3\7\61\2\2\u01b3\\\3\2\2\2\u01b4")
        buf.write("\u01b5\7\'\2\2\u01b5^\3\2\2\2\u01b6\u01b7\7#\2\2\u01b7")
        buf.write("`\3\2\2\2\u01b8\u01b9\7(\2\2\u01b9\u01ba\7(\2\2\u01ba")
        buf.write("b\3\2\2\2\u01bb\u01bc\7~\2\2\u01bc\u01bd\7~\2\2\u01bd")
        buf.write("d\3\2\2\2\u01be\u01bf\7?\2\2\u01bf\u01c0\7?\2\2\u01c0")
        buf.write("f\3\2\2\2\u01c1\u01c2\7?\2\2\u01c2h\3\2\2\2\u01c3\u01c4")
        buf.write("\7#\2\2\u01c4\u01c5\7?\2\2\u01c5j\3\2\2\2\u01c6\u01c7")
        buf.write("\7>\2\2\u01c7l\3\2\2\2\u01c8\u01c9\7>\2\2\u01c9\u01ca")
        buf.write("\7?\2\2\u01can\3\2\2\2\u01cb\u01cc\7@\2\2\u01ccp\3\2\2")
        buf.write("\2\u01cd\u01ce\7@\2\2\u01ce\u01cf\7?\2\2\u01cfr\3\2\2")
        buf.write("\2\u01d0\u01d1\7?\2\2\u01d1\u01d2\7?\2\2\u01d2\u01d3\7")
        buf.write("\60\2\2\u01d3t\3\2\2\2\u01d4\u01d5\7-\2\2\u01d5\u01d6")
        buf.write("\7\60\2\2\u01d6v\3\2\2\2\u01d7\u01d8\7*\2\2\u01d8x\3\2")
        buf.write("\2\2\u01d9\u01da\7+\2\2\u01daz\3\2\2\2\u01db\u01dc\7]")
        buf.write("\2\2\u01dc|\3\2\2\2\u01dd\u01de\7_\2\2\u01de~\3\2\2\2")
        buf.write("\u01df\u01e0\7\60\2\2\u01e0\u0080\3\2\2\2\u01e1\u01e2")
        buf.write("\7\60\2\2\u01e2\u01e3\7\60\2\2\u01e3\u0082\3\2\2\2\u01e4")
        buf.write("\u01e5\7.\2\2\u01e5\u0084\3\2\2\2\u01e6\u01e7\7=\2\2\u01e7")
        buf.write("\u0086\3\2\2\2\u01e8\u01e9\7<\2\2\u01e9\u0088\3\2\2\2")
        buf.write("\u01ea\u01eb\7<\2\2\u01eb\u01ec\7<\2\2\u01ec\u008a\3\2")
        buf.write("\2\2\u01ed\u01ee\7}\2\2\u01ee\u008c\3\2\2\2\u01ef\u01f0")
        buf.write("\7\177\2\2\u01f0\u008e\3\2\2\2\u01f1\u01f5\t\16\2\2\u01f2")
        buf.write("\u01f4\t\17\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f7\3\2\2")
        buf.write("\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u0090")
        buf.write("\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01f9\7&\2\2\u01f9")
        buf.write("\u01fd\t\16\2\2\u01fa\u01fc\t\17\2\2\u01fb\u01fa\3\2\2")
        buf.write("\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u0092\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200")
        buf.write("\u0202\t\20\2\2\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2")
        buf.write("\2\u0203\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205\u0206\bJ\2\2\u0206\u0094\3\2\2\2\u0207")
        buf.write("\u020b\7$\2\2\u0208\u020a\5\13\6\2\u0209\u0208\3\2\2\2")
        buf.write("\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3")
        buf.write("\2\2\2\u020c\u020e\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u020f")
        buf.write("\bK\6\2\u020f\u0096\3\2\2\2\u0210\u0214\7$\2\2\u0211\u0213")
        buf.write("\5\13\6\2\u0212\u0211\3\2\2\2\u0213\u0216\3\2\2\2\u0214")
        buf.write("\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0217\3\2\2\2")
        buf.write("\u0216\u0214\3\2\2\2\u0217\u0218\5\21\t\2\u0218\u0219")
        buf.write("\bL\7\2\u0219\u0098\3\2\2\2\u021a\u021b\13\2\2\2\u021b")
        buf.write("\u021c\bM\b\2\u021c\u009a\3\2\2\2\33\2\u009d\u00a2\u00a6")
        buf.write("\u00ac\u00b3\u00ba\u00bf\u00cb\u00d1\u00d6\u00dd\u00e2")
        buf.write("\u00e7\u00ef\u018b\u0193\u019b\u01a0\u01a8\u01f5\u01fd")
        buf.write("\u0203\u020b\u0214\t\b\2\2\3\'\2\3(\3\3*\4\3K\5\3L\6\3")
        buf.write("M\7")
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
    VAR = 8
    VAL = 9
    SELF = 10
    RETURN = 11
    IN = 12
    BY = 13
    NEW = 14
    CONSTRUCTOR = 15
    DESTRUCTOR = 16
    NULL = 17
    CLASS = 18
    ARRAY = 19
    INTEGER = 20
    FLOAT = 21
    BOOLEAN = 22
    STRING = 23
    INTEGER_LITERAL = 24
    STRING_LITERAL = 25
    BOOLEAN_LITERAL = 26
    FLOAT_LITERAL = 27
    ADD = 28
    SUB = 29
    MUL = 30
    DIV = 31
    MOD = 32
    NOT = 33
    AND = 34
    OR = 35
    EQUAL = 36
    ASSIGN = 37
    NOT_EQUAL = 38
    LT = 39
    LTE = 40
    GT = 41
    GTE = 42
    STRING_EQUAL = 43
    STRING_ADD = 44
    LP = 45
    RP = 46
    LSB = 47
    RSB = 48
    DOT = 49
    DOUBLE_DOT = 50
    COMMA = 51
    SEMI = 52
    COLON = 53
    DOUBLE_COLON = 54
    LCB = 55
    RCB = 56
    ID = 57
    DOLLAR_ID = 58
    WS = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_TOKEN = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Var'", "'Val'", "'Self'", "'Return'", "'In'", "'By'", "'New'", 
            "'Constructor'", "'Destructor'", "'Null'", "'Class'", "'Array'", 
            "'Int'", "'Float'", "'Boolean'", "'String'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'==.'", "'+.'", "'('", "')'", 
            "'['", "']'", "'.'", "'..'", "','", "';'", "':'", "'::'", "'{'", 
            "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "VAR", "VAL", "SELF", "RETURN", "IN", "BY", "NEW", "CONSTRUCTOR", 
            "DESTRUCTOR", "NULL", "CLASS", "ARRAY", "INTEGER", "FLOAT", 
            "BOOLEAN", "STRING", "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
            "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", 
            "STRING_EQUAL", "STRING_ADD", "LP", "RP", "LSB", "RSB", "DOT", 
            "DOUBLE_DOT", "COMMA", "SEMI", "COLON", "DOUBLE_COLON", "LCB", 
            "RCB", "ID", "DOLLAR_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_TOKEN" ]

    ruleNames = [ "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", 
                  "HEX_INTEGER_LITERAL", "STRING_CHAR", "ESCAPE_SEQUENCE", 
                  "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", "SIGN", "FLOAT_INTEGER_PART", 
                  "FLOAT_DECIMAL_PART", "FLOAT_EXPONENT_PART", "COMMENT", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "VAR", "VAL", "SELF", "RETURN", "IN", 
                  "BY", "NEW", "CONSTRUCTOR", "DESTRUCTOR", "NULL", "CLASS", 
                  "ARRAY", "INTEGER", "FLOAT", "BOOLEAN", "STRING", "INTEGER_LITERAL", 
                  "STRING_LITERAL", "BOOLEAN_LITERAL", "FLOAT_LITERAL", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", 
                  "STRING_EQUAL", "STRING_ADD", "LP", "RP", "LSB", "RSB", 
                  "DOT", "DOUBLE_DOT", "COMMA", "SEMI", "COLON", "DOUBLE_COLON", 
                  "LCB", "RCB", "ID", "DOLLAR_ID", "WS", "UNCLOSE_STRING", 
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
            actions[37] = self.INTEGER_LITERAL_action 
            actions[38] = self.STRING_LITERAL_action 
            actions[40] = self.FLOAT_LITERAL_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text.translate(str.maketrans('','','_'))

     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text[1:-1]

     

    def FLOAT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text.translate(str.maketrans('','','_'))

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise UncloseString(self.text[1:]);

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise ErrorToken(self.text)

     


