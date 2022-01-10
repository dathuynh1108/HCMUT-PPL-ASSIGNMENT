# Generated from d:\Workspace\PPL\Assignment\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01ff\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\5\2\u0095")
        buf.write("\n\2\3\3\3\3\3\3\7\3\u009a\n\3\f\3\16\3\u009d\13\3\5\3")
        buf.write("\u009f\n\3\3\4\3\4\6\4\u00a3\n\4\r\4\16\4\u00a4\3\5\3")
        buf.write("\5\3\5\6\5\u00aa\n\5\r\5\16\5\u00ab\3\6\3\6\3\6\6\6\u00b1")
        buf.write("\n\6\r\6\16\6\u00b2\3\7\3\7\3\7\5\7\u00b8\n\7\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00c5\n\n\3\13")
        buf.write("\3\13\3\f\3\f\7\f\u00cb\n\f\f\f\16\f\u00ce\13\f\3\r\3")
        buf.write("\r\5\r\u00d2\n\r\3\16\3\16\5\16\u00d6\n\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\7\17\u00de\n\17\f\17\16\17\u00e1\13")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\5!\u014f\n!\3!\3!\3\"")
        buf.write("\3\"\7\"\u0155\n\"\f\"\16\"\u0158\13\"\3\"\3\"\3\"\3#")
        buf.write("\3#\5#\u015f\n#\3$\3$\3$\5$\u0164\n$\3$\3$\3$\3$\3$\3")
        buf.write("$\5$\u016c\n$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3?\3")
        buf.write("@\3@\3A\3A\3B\3B\7B\u01b8\nB\fB\16B\u01bb\13B\3C\5C\u01be")
        buf.write("\nC\3C\3C\7C\u01c2\nC\fC\16C\u01c5\13C\3D\6D\u01c8\nD")
        buf.write("\rD\16D\u01c9\3D\3D\3E\3E\3E\3E\7E\u01d2\nE\fE\16E\u01d5")
        buf.write("\13E\3E\3E\3E\3E\3E\7E\u01dc\nE\fE\16E\u01df\13E\3E\3")
        buf.write("E\5E\u01e3\nE\3E\3E\3F\3F\7F\u01e9\nF\fF\16F\u01ec\13")
        buf.write("F\3F\5F\u01ef\nF\3F\3F\3G\3G\7G\u01f5\nG\fG\16G\u01f8")
        buf.write("\13G\3G\3G\3G\3H\3H\3H\2\2I\3\2\5\2\7\2\t\2\13\2\r\2\17")
        buf.write("\2\21\2\23\2\25\2\27\2\31\2\33\2\35\3\37\4!\5#\6%\7\'")
        buf.write("\b)\t+\2-\2/\n\61\13\63\f\65\r\67\169\17;\20=\21?\22A")
        buf.write("\23C\24E\25G\26I\27K\30M\31O\32Q\33S\34U\35W\36Y\37[ ")
        buf.write("]!_\"a#c$e%g&i\'k(m)o*q+s,u-w.y/{\60}\61\177\62\u0081")
        buf.write("\63\u0083\64\u0085\65\u0087\66\u0089\67\u008b8\u008d9")
        buf.write("\u008f:\3\2\25\3\2%%\3\2\63;\4\2\62;aa\3\2\629\4\2DDd")
        buf.write("d\3\2\62\63\4\2ZZzz\5\2\62;CHch\7\2\n\f\16\17$$))^^\t")
        buf.write("\2))^^ddhhppttvv\3\2$$\3\2^^\4\2--//\3\2\62;\4\2GGgg\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\7\3\n\f\16")
        buf.write("\17$$))^^\2\u020e\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0094")
        buf.write("\3\2\2\2\5\u009e\3\2\2\2\7\u00a0\3\2\2\2\t\u00a6\3\2\2")
        buf.write("\2\13\u00ad\3\2\2\2\r\u00b7\3\2\2\2\17\u00b9\3\2\2\2\21")
        buf.write("\u00bc\3\2\2\2\23\u00c4\3\2\2\2\25\u00c6\3\2\2\2\27\u00c8")
        buf.write("\3\2\2\2\31\u00cf\3\2\2\2\33\u00d3\3\2\2\2\35\u00d9\3")
        buf.write("\2\2\2\37\u00e7\3\2\2\2!\u00ed\3\2\2\2#\u00f6\3\2\2\2")
        buf.write("%\u00f9\3\2\2\2\'\u0100\3\2\2\2)\u0105\3\2\2\2+\u010d")
        buf.write("\3\2\2\2-\u0112\3\2\2\2/\u0118\3\2\2\2\61\u011c\3\2\2")
        buf.write("\2\63\u0120\3\2\2\2\65\u0126\3\2\2\2\67\u012c\3\2\2\2")
        buf.write("9\u0130\3\2\2\2;\u0136\3\2\2\2=\u013e\3\2\2\2?\u0145\3")
        buf.write("\2\2\2A\u014e\3\2\2\2C\u0152\3\2\2\2E\u015e\3\2\2\2G\u016b")
        buf.write("\3\2\2\2I\u016f\3\2\2\2K\u0171\3\2\2\2M\u0173\3\2\2\2")
        buf.write("O\u0175\3\2\2\2Q\u0177\3\2\2\2S\u0179\3\2\2\2U\u017b\3")
        buf.write("\2\2\2W\u017e\3\2\2\2Y\u0181\3\2\2\2[\u0184\3\2\2\2]\u0186")
        buf.write("\3\2\2\2_\u0189\3\2\2\2a\u018b\3\2\2\2c\u018e\3\2\2\2")
        buf.write("e\u0190\3\2\2\2g\u0193\3\2\2\2i\u0197\3\2\2\2k\u019a\3")
        buf.write("\2\2\2m\u019e\3\2\2\2o\u01a0\3\2\2\2q\u01a2\3\2\2\2s\u01a4")
        buf.write("\3\2\2\2u\u01a6\3\2\2\2w\u01a8\3\2\2\2y\u01aa\3\2\2\2")
        buf.write("{\u01ac\3\2\2\2}\u01ae\3\2\2\2\177\u01b1\3\2\2\2\u0081")
        buf.write("\u01b3\3\2\2\2\u0083\u01b5\3\2\2\2\u0085\u01bd\3\2\2\2")
        buf.write("\u0087\u01c7\3\2\2\2\u0089\u01e2\3\2\2\2\u008b\u01e6\3")
        buf.write("\2\2\2\u008d\u01f2\3\2\2\2\u008f\u01fc\3\2\2\2\u0091\u0095")
        buf.write("\n\2\2\2\u0092\u0093\7%\2\2\u0093\u0095\n\2\2\2\u0094")
        buf.write("\u0091\3\2\2\2\u0094\u0092\3\2\2\2\u0095\4\3\2\2\2\u0096")
        buf.write("\u009f\7\62\2\2\u0097\u009b\t\3\2\2\u0098\u009a\t\4\2")
        buf.write("\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009f\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u0096\3\2\2\2\u009e\u0097\3\2\2\2")
        buf.write("\u009f\6\3\2\2\2\u00a0\u00a2\7\62\2\2\u00a1\u00a3\t\5")
        buf.write("\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\b\3\2\2\2\u00a6\u00a7")
        buf.write("\7\62\2\2\u00a7\u00a9\t\6\2\2\u00a8\u00aa\t\7\2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ac\3\2\2\2\u00ac\n\3\2\2\2\u00ad\u00ae\7\62")
        buf.write("\2\2\u00ae\u00b0\t\b\2\2\u00af\u00b1\t\t\2\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\f\3\2\2\2\u00b4\u00b8\n\n\2\2\u00b5")
        buf.write("\u00b8\5\17\b\2\u00b6\u00b8\5\21\t\2\u00b7\u00b4\3\2\2")
        buf.write("\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\16\3")
        buf.write("\2\2\2\u00b9\u00ba\7^\2\2\u00ba\u00bb\t\13\2\2\u00bb\20")
        buf.write("\3\2\2\2\u00bc\u00bd\7)\2\2\u00bd\u00be\7$\2\2\u00be\22")
        buf.write("\3\2\2\2\u00bf\u00c0\7^\2\2\u00c0\u00c5\n\13\2\2\u00c1")
        buf.write("\u00c2\7)\2\2\u00c2\u00c5\n\f\2\2\u00c3\u00c5\n\r\2\2")
        buf.write("\u00c4\u00bf\3\2\2\2\u00c4\u00c1\3\2\2\2\u00c4\u00c3\3")
        buf.write("\2\2\2\u00c5\24\3\2\2\2\u00c6\u00c7\t\16\2\2\u00c7\26")
        buf.write("\3\2\2\2\u00c8\u00cc\t\17\2\2\u00c9\u00cb\t\4\2\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cd\30\3\2\2\2\u00ce\u00cc\3\2")
        buf.write("\2\2\u00cf\u00d1\7\60\2\2\u00d0\u00d2\5\27\f\2\u00d1\u00d0")
        buf.write("\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\32\3\2\2\2\u00d3\u00d5")
        buf.write("\t\20\2\2\u00d4\u00d6\5\25\13\2\u00d5\u00d4\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\5\27\f")
        buf.write("\2\u00d8\34\3\2\2\2\u00d9\u00da\7%\2\2\u00da\u00db\7%")
        buf.write("\2\2\u00db\u00df\3\2\2\2\u00dc\u00de\5\3\2\2\u00dd\u00dc")
        buf.write("\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2")
        buf.write("\u00e2\u00e3\7%\2\2\u00e3\u00e4\7%\2\2\u00e4\u00e5\3\2")
        buf.write("\2\2\u00e5\u00e6\b\17\2\2\u00e6\36\3\2\2\2\u00e7\u00e8")
        buf.write("\7D\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb")
        buf.write("\7c\2\2\u00eb\u00ec\7m\2\2\u00ec \3\2\2\2\u00ed\u00ee")
        buf.write("\7E\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7w\2\2\u00f4\u00f5\7g\2\2\u00f5\"\3\2\2\2\u00f6\u00f7")
        buf.write("\7K\2\2\u00f7\u00f8\7h\2\2\u00f8$\3\2\2\2\u00f9\u00fa")
        buf.write("\7G\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7u\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7h\2\2\u00ff&\3")
        buf.write("\2\2\2\u0100\u0101\7G\2\2\u0101\u0102\7n\2\2\u0102\u0103")
        buf.write("\7u\2\2\u0103\u0104\7g\2\2\u0104(\3\2\2\2\u0105\u0106")
        buf.write("\7H\2\2\u0106\u0107\7q\2\2\u0107\u0108\7t\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010a\7c\2\2\u010a\u010b\7e\2\2\u010b\u010c")
        buf.write("\7j\2\2\u010c*\3\2\2\2\u010d\u010e\7V\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7w\2\2\u0110\u0111\7g\2\2\u0111,\3")
        buf.write("\2\2\2\u0112\u0113\7H\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7n\2\2\u0115\u0116\7u\2\2\u0116\u0117\7g\2\2\u0117.\3")
        buf.write("\2\2\2\u0118\u0119\7x\2\2\u0119\u011a\7c\2\2\u011a\u011b")
        buf.write("\7t\2\2\u011b\60\3\2\2\2\u011c\u011d\7x\2\2\u011d\u011e")
        buf.write("\7c\2\2\u011e\u011f\7n\2\2\u011f\62\3\2\2\2\u0120\u0121")
        buf.write("\7e\2\2\u0121\u0122\7n\2\2\u0122\u0123\7c\2\2\u0123\u0124")
        buf.write("\7u\2\2\u0124\u0125\7u\2\2\u0125\64\3\2\2\2\u0126\u0127")
        buf.write("\7C\2\2\u0127\u0128\7t\2\2\u0128\u0129\7t\2\2\u0129\u012a")
        buf.write("\7c\2\2\u012a\u012b\7{\2\2\u012b\66\3\2\2\2\u012c\u012d")
        buf.write("\7K\2\2\u012d\u012e\7p\2\2\u012e\u012f\7v\2\2\u012f8\3")
        buf.write("\2\2\2\u0130\u0131\7H\2\2\u0131\u0132\7n\2\2\u0132\u0133")
        buf.write("\7q\2\2\u0133\u0134\7c\2\2\u0134\u0135\7v\2\2\u0135:\3")
        buf.write("\2\2\2\u0136\u0137\7D\2\2\u0137\u0138\7q\2\2\u0138\u0139")
        buf.write("\7q\2\2\u0139\u013a\7n\2\2\u013a\u013b\7g\2\2\u013b\u013c")
        buf.write("\7c\2\2\u013c\u013d\7p\2\2\u013d<\3\2\2\2\u013e\u013f")
        buf.write("\7U\2\2\u013f\u0140\7v\2\2\u0140\u0141\7t\2\2\u0141\u0142")
        buf.write("\7k\2\2\u0142\u0143\7p\2\2\u0143\u0144\7i\2\2\u0144>\3")
        buf.write("\2\2\2\u0145\u0146\7P\2\2\u0146\u0147\7w\2\2\u0147\u0148")
        buf.write("\7n\2\2\u0148\u0149\7n\2\2\u0149@\3\2\2\2\u014a\u014f")
        buf.write("\5\5\3\2\u014b\u014f\5\7\4\2\u014c\u014f\5\13\6\2\u014d")
        buf.write("\u014f\5\t\5\2\u014e\u014a\3\2\2\2\u014e\u014b\3\2\2\2")
        buf.write("\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\u0151\b!\3\2\u0151B\3\2\2\2\u0152\u0156\7")
        buf.write("$\2\2\u0153\u0155\5\r\7\2\u0154\u0153\3\2\2\2\u0155\u0158")
        buf.write("\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\7$\2\2")
        buf.write("\u015a\u015b\b\"\4\2\u015bD\3\2\2\2\u015c\u015f\5+\26")
        buf.write("\2\u015d\u015f\5-\27\2\u015e\u015c\3\2\2\2\u015e\u015d")
        buf.write("\3\2\2\2\u015fF\3\2\2\2\u0160\u0161\5\27\f\2\u0161\u0163")
        buf.write("\5\31\r\2\u0162\u0164\5\33\16\2\u0163\u0162\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u016c\3\2\2\2\u0165\u0166\5\27\f")
        buf.write("\2\u0166\u0167\5\33\16\2\u0167\u016c\3\2\2\2\u0168\u0169")
        buf.write("\5\31\r\2\u0169\u016a\5\33\16\2\u016a\u016c\3\2\2\2\u016b")
        buf.write("\u0160\3\2\2\2\u016b\u0165\3\2\2\2\u016b\u0168\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\u016e\b$\5\2\u016eH\3\2\2\2")
        buf.write("\u016f\u0170\7-\2\2\u0170J\3\2\2\2\u0171\u0172\7/\2\2")
        buf.write("\u0172L\3\2\2\2\u0173\u0174\7,\2\2\u0174N\3\2\2\2\u0175")
        buf.write("\u0176\7\61\2\2\u0176P\3\2\2\2\u0177\u0178\7\'\2\2\u0178")
        buf.write("R\3\2\2\2\u0179\u017a\7#\2\2\u017aT\3\2\2\2\u017b\u017c")
        buf.write("\7(\2\2\u017c\u017d\7(\2\2\u017dV\3\2\2\2\u017e\u017f")
        buf.write("\7~\2\2\u017f\u0180\7~\2\2\u0180X\3\2\2\2\u0181\u0182")
        buf.write("\7?\2\2\u0182\u0183\7?\2\2\u0183Z\3\2\2\2\u0184\u0185")
        buf.write("\7?\2\2\u0185\\\3\2\2\2\u0186\u0187\7#\2\2\u0187\u0188")
        buf.write("\7?\2\2\u0188^\3\2\2\2\u0189\u018a\7>\2\2\u018a`\3\2\2")
        buf.write("\2\u018b\u018c\7>\2\2\u018c\u018d\7?\2\2\u018db\3\2\2")
        buf.write("\2\u018e\u018f\7@\2\2\u018fd\3\2\2\2\u0190\u0191\7@\2")
        buf.write("\2\u0191\u0192\7?\2\2\u0192f\3\2\2\2\u0193\u0194\7?\2")
        buf.write("\2\u0194\u0195\7?\2\2\u0195\u0196\7\60\2\2\u0196h\3\2")
        buf.write("\2\2\u0197\u0198\7-\2\2\u0198\u0199\7\60\2\2\u0199j\3")
        buf.write("\2\2\2\u019a\u019b\7p\2\2\u019b\u019c\7g\2\2\u019c\u019d")
        buf.write("\7y\2\2\u019dl\3\2\2\2\u019e\u019f\7*\2\2\u019fn\3\2\2")
        buf.write("\2\u01a0\u01a1\7+\2\2\u01a1p\3\2\2\2\u01a2\u01a3\7]\2")
        buf.write("\2\u01a3r\3\2\2\2\u01a4\u01a5\7_\2\2\u01a5t\3\2\2\2\u01a6")
        buf.write("\u01a7\7\60\2\2\u01a7v\3\2\2\2\u01a8\u01a9\7.\2\2\u01a9")
        buf.write("x\3\2\2\2\u01aa\u01ab\7=\2\2\u01abz\3\2\2\2\u01ac\u01ad")
        buf.write("\7<\2\2\u01ad|\3\2\2\2\u01ae\u01af\7<\2\2\u01af\u01b0")
        buf.write("\7<\2\2\u01b0~\3\2\2\2\u01b1\u01b2\7}\2\2\u01b2\u0080")
        buf.write("\3\2\2\2\u01b3\u01b4\7\177\2\2\u01b4\u0082\3\2\2\2\u01b5")
        buf.write("\u01b9\t\21\2\2\u01b6\u01b8\t\22\2\2\u01b7\u01b6\3\2\2")
        buf.write("\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba")
        buf.write("\3\2\2\2\u01ba\u0084\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc")
        buf.write("\u01be\7&\2\2\u01bd\u01bc\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c3\t\21\2\2\u01c0\u01c2")
        buf.write("\t\22\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u0086\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c8\t\23\2\2\u01c7\u01c6")
        buf.write("\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\bD\2\2")
        buf.write("\u01cc\u0088\3\2\2\2\u01cd\u01ce\7%\2\2\u01ce\u01cf\7")
        buf.write("%\2\2\u01cf\u01d3\3\2\2\2\u01d0\u01d2\5\3\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01e3\7\2\2\3\u01d7\u01d8\7%\2\2\u01d8\u01d9\7")
        buf.write("%\2\2\u01d9\u01dd\3\2\2\2\u01da\u01dc\n\2\2\2\u01db\u01da")
        buf.write("\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01dd\3\2\2\2")
        buf.write("\u01e0\u01e1\7%\2\2\u01e1\u01e3\7\2\2\3\u01e2\u01cd\3")
        buf.write("\2\2\2\u01e2\u01d7\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5")
        buf.write("\bE\6\2\u01e5\u008a\3\2\2\2\u01e6\u01ea\7$\2\2\u01e7\u01e9")
        buf.write("\5\r\7\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea")
        buf.write("\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ee\3\2\2\2")
        buf.write("\u01ec\u01ea\3\2\2\2\u01ed\u01ef\t\24\2\2\u01ee\u01ed")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\bF\7\2\u01f1")
        buf.write("\u008c\3\2\2\2\u01f2\u01f6\7$\2\2\u01f3\u01f5\5\r\7\2")
        buf.write("\u01f4\u01f3\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3")
        buf.write("\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01f6")
        buf.write("\3\2\2\2\u01f9\u01fa\5\23\n\2\u01fa\u01fb\bG\b\2\u01fb")
        buf.write("\u008e\3\2\2\2\u01fc\u01fd\13\2\2\2\u01fd\u01fe\bH\t\2")
        buf.write("\u01fe\u0090\3\2\2\2\36\2\u0094\u009b\u009e\u00a4\u00ab")
        buf.write("\u00b2\u00b7\u00c4\u00cc\u00d1\u00d5\u00df\u014e\u0156")
        buf.write("\u015e\u0163\u016b\u01b9\u01bd\u01c3\u01c9\u01d3\u01dd")
        buf.write("\u01e2\u01ea\u01ee\u01f6\n\b\2\2\3!\2\3\"\3\3$\4\3E\5")
        buf.write("\3F\6\3G\7\3H\b")
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
    CLASS = 10
    ARRAY = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    STRING = 15
    NULL = 16
    INTEGER_LITERAL = 17
    STRING_LITERAL = 18
    BOOLEAN_LITERAL = 19
    FLOAT_LITERAL = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    NOT = 26
    AND = 27
    OR = 28
    EQUAL = 29
    ASSIGN = 30
    NOT_EQUAL = 31
    LT = 32
    LTE = 33
    GT = 34
    GTE = 35
    STRING_EQUAL = 36
    STRING_ADD = 37
    NEW = 38
    LP = 39
    RP = 40
    LSB = 41
    RSB = 42
    DOT = 43
    COMMA = 44
    SEMI = 45
    COLON = 46
    DOUBLE_COLON = 47
    LCB = 48
    RCB = 49
    ID = 50
    DOLLAR_ID = 51
    WS = 52
    UNTERMINATED_COMMENT = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55
    ERROR_TOKEN = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'var'", "'val'", "'class'", "'Array'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Null'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'==.'", "'+.'", "'new'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'::'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "VAR", "VAL", "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "NULL", "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
            "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", 
            "STRING_EQUAL", "STRING_ADD", "NEW", "LP", "RP", "LSB", "RSB", 
            "DOT", "COMMA", "SEMI", "COLON", "DOUBLE_COLON", "LCB", "RCB", 
            "ID", "DOLLAR_ID", "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "COMMENT_CHAR", "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", 
                  "BIN_INTEGER_LITERAL", "HEX_INTEGER_LITERAL", "STRING_CHAR", 
                  "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", 
                  "SIGN", "FLOAT_INTEGER_PART", "FLOAT_DECIMAL_PART", "FLOAT_EXPONENT_PART", 
                  "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "VAR", "VAL", "CLASS", "ARRAY", 
                  "INT", "FLOAT", "BOOLEAN", "STRING", "NULL", "INTEGER_LITERAL", 
                  "STRING_LITERAL", "BOOLEAN_LITERAL", "FLOAT_LITERAL", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", 
                  "STRING_EQUAL", "STRING_ADD", "NEW", "LP", "RP", "LSB", 
                  "RSB", "DOT", "COMMA", "SEMI", "COLON", "DOUBLE_COLON", 
                  "LCB", "RCB", "ID", "DOLLAR_ID", "WS", "UNTERMINATED_COMMENT", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[31] = self.INTEGER_LITERAL_action 
            actions[32] = self.STRING_LITERAL_action 
            actions[34] = self.FLOAT_LITERAL_action 
            actions[67] = self.UNTERMINATED_COMMENT_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_TOKEN_action 
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

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise UNTERMINATED_COMMENT()

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                y = str(self.text)
                possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
                if y[-1] in possible:
                    raise UNCLOSE_STRING(y[1:-1])
                else:
                    raise UNCLOSE_STRING(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise ILLEGAL_ESCAPE(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                raise ERROR_TOKEN(self.text)

     


