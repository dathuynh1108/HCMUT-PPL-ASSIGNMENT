# Generated from d:\Workspace\PPL\Assignment\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u01eb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\5\2\u008f\n\2\3\3\3\3\3\3\7")
        buf.write("\3\u0094\n\3\f\3\16\3\u0097\13\3\5\3\u0099\n\3\3\4\3\4")
        buf.write("\6\4\u009d\n\4\r\4\16\4\u009e\3\5\3\5\3\5\6\5\u00a4\n")
        buf.write("\5\r\5\16\5\u00a5\3\6\3\6\3\6\6\6\u00ab\n\6\r\6\16\6\u00ac")
        buf.write("\3\7\3\7\3\7\5\7\u00b2\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00bf\n\n\3\13\3\13\3\f\3\f\7\f\u00c5")
        buf.write("\n\f\f\f\16\f\u00c8\13\f\3\r\3\r\5\r\u00cc\n\r\3\16\3")
        buf.write("\16\5\16\u00d0\n\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17")
        buf.write("\u00d8\n\17\f\17\16\17\u00db\13\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!")
        buf.write("\3!\3!\3!\5!\u0149\n!\3!\3!\3\"\3\"\7\"\u014f\n\"\f\"")
        buf.write("\16\"\u0152\13\"\3\"\3\"\3\"\3#\3#\5#\u0159\n#\3$\3$\3")
        buf.write("$\5$\u015e\n$\3$\3$\3$\3$\3$\3$\5$\u0166\n$\3$\3$\3%\5")
        buf.write("%\u016b\n%\3%\3%\7%\u016f\n%\f%\16%\u0172\13%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\6A\u01b4\nA\rA\16A\u01b5\3A\3A\3B\3B\3B")
        buf.write("\3B\7B\u01be\nB\fB\16B\u01c1\13B\3B\3B\3B\3B\3B\7B\u01c8")
        buf.write("\nB\fB\16B\u01cb\13B\3B\3B\5B\u01cf\nB\3B\3B\3C\3C\7C")
        buf.write("\u01d5\nC\fC\16C\u01d8\13C\3C\5C\u01db\nC\3C\3C\3D\3D")
        buf.write("\7D\u01e1\nD\fD\16D\u01e4\13D\3D\3D\3D\3E\3E\3E\2\2F\3")
        buf.write("\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2")
        buf.write("\33\2\35\3\37\4!\5#\6%\7\'\b)\t+\2-\2/\n\61\13\63\f\65")
        buf.write("\r\67\169\17;\20=\21?\22A\23C\24E\25G\26I\27K\30M\31O")
        buf.write("\32Q\33S\34U\35W\36Y\37[ ]!_\"a#c$e%g&i\'k(m)o*q+s,u-")
        buf.write("w.y/{\60}\61\177\62\u0081\63\u0083\64\u0085\65\u0087\66")
        buf.write("\u0089\67\3\2\25\3\2%%\3\2\63;\4\2\62;aa\3\2\629\4\2D")
        buf.write("Ddd\3\2\62\63\4\2ZZzz\5\2\62;CHch\7\2\n\f\16\17$$))^^")
        buf.write("\t\2))^^ddhhppttvv\3\2$$\3\2^^\4\2--//\3\2\62;\4\2GGg")
        buf.write("g\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\7\3\n\f")
        buf.write("\16\17$$))^^\2\u01f9\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\3\u008e\3\2\2\2\5\u0098\3\2\2\2\7\u009a\3\2\2\2\t\u00a0")
        buf.write("\3\2\2\2\13\u00a7\3\2\2\2\r\u00b1\3\2\2\2\17\u00b3\3\2")
        buf.write("\2\2\21\u00b6\3\2\2\2\23\u00be\3\2\2\2\25\u00c0\3\2\2")
        buf.write("\2\27\u00c2\3\2\2\2\31\u00c9\3\2\2\2\33\u00cd\3\2\2\2")
        buf.write("\35\u00d3\3\2\2\2\37\u00e1\3\2\2\2!\u00e7\3\2\2\2#\u00f0")
        buf.write("\3\2\2\2%\u00f3\3\2\2\2\'\u00fa\3\2\2\2)\u00ff\3\2\2\2")
        buf.write("+\u0107\3\2\2\2-\u010c\3\2\2\2/\u0112\3\2\2\2\61\u0116")
        buf.write("\3\2\2\2\63\u011a\3\2\2\2\65\u0120\3\2\2\2\67\u0126\3")
        buf.write("\2\2\29\u012a\3\2\2\2;\u0130\3\2\2\2=\u0138\3\2\2\2?\u013f")
        buf.write("\3\2\2\2A\u0148\3\2\2\2C\u014c\3\2\2\2E\u0158\3\2\2\2")
        buf.write("G\u0165\3\2\2\2I\u016a\3\2\2\2K\u0173\3\2\2\2M\u0175\3")
        buf.write("\2\2\2O\u0177\3\2\2\2Q\u0179\3\2\2\2S\u017b\3\2\2\2U\u017d")
        buf.write("\3\2\2\2W\u017f\3\2\2\2Y\u0182\3\2\2\2[\u0185\3\2\2\2")
        buf.write("]\u0188\3\2\2\2_\u018a\3\2\2\2a\u018d\3\2\2\2c\u018f\3")
        buf.write("\2\2\2e\u0192\3\2\2\2g\u0194\3\2\2\2i\u0197\3\2\2\2k\u019b")
        buf.write("\3\2\2\2m\u019e\3\2\2\2o\u01a0\3\2\2\2q\u01a2\3\2\2\2")
        buf.write("s\u01a4\3\2\2\2u\u01a6\3\2\2\2w\u01a8\3\2\2\2y\u01aa\3")
        buf.write("\2\2\2{\u01ac\3\2\2\2}\u01ae\3\2\2\2\177\u01b0\3\2\2\2")
        buf.write("\u0081\u01b3\3\2\2\2\u0083\u01ce\3\2\2\2\u0085\u01d2\3")
        buf.write("\2\2\2\u0087\u01de\3\2\2\2\u0089\u01e8\3\2\2\2\u008b\u008f")
        buf.write("\n\2\2\2\u008c\u008d\7%\2\2\u008d\u008f\n\2\2\2\u008e")
        buf.write("\u008b\3\2\2\2\u008e\u008c\3\2\2\2\u008f\4\3\2\2\2\u0090")
        buf.write("\u0099\7\62\2\2\u0091\u0095\t\3\2\2\u0092\u0094\t\4\2")
        buf.write("\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0099\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0098\u0090\3\2\2\2\u0098\u0091\3\2\2\2")
        buf.write("\u0099\6\3\2\2\2\u009a\u009c\7\62\2\2\u009b\u009d\t\5")
        buf.write("\2\2\u009c\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\b\3\2\2\2\u00a0\u00a1")
        buf.write("\7\62\2\2\u00a1\u00a3\t\6\2\2\u00a2\u00a4\t\7\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\n\3\2\2\2\u00a7\u00a8\7\62")
        buf.write("\2\2\u00a8\u00aa\t\b\2\2\u00a9\u00ab\t\t\2\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\f\3\2\2\2\u00ae\u00b2\n\n\2\2\u00af")
        buf.write("\u00b2\5\17\b\2\u00b0\u00b2\5\21\t\2\u00b1\u00ae\3\2\2")
        buf.write("\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\16\3")
        buf.write("\2\2\2\u00b3\u00b4\7^\2\2\u00b4\u00b5\t\13\2\2\u00b5\20")
        buf.write("\3\2\2\2\u00b6\u00b7\7)\2\2\u00b7\u00b8\7$\2\2\u00b8\22")
        buf.write("\3\2\2\2\u00b9\u00ba\7^\2\2\u00ba\u00bf\n\13\2\2\u00bb")
        buf.write("\u00bc\7)\2\2\u00bc\u00bf\n\f\2\2\u00bd\u00bf\n\r\2\2")
        buf.write("\u00be\u00b9\3\2\2\2\u00be\u00bb\3\2\2\2\u00be\u00bd\3")
        buf.write("\2\2\2\u00bf\24\3\2\2\2\u00c0\u00c1\t\16\2\2\u00c1\26")
        buf.write("\3\2\2\2\u00c2\u00c6\t\17\2\2\u00c3\u00c5\t\4\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\30\3\2\2\2\u00c8\u00c6\3\2")
        buf.write("\2\2\u00c9\u00cb\7\60\2\2\u00ca\u00cc\5\27\f\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\32\3\2\2\2\u00cd\u00cf")
        buf.write("\t\20\2\2\u00ce\u00d0\5\25\13\2\u00cf\u00ce\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\5\27\f")
        buf.write("\2\u00d2\34\3\2\2\2\u00d3\u00d4\7%\2\2\u00d4\u00d5\7%")
        buf.write("\2\2\u00d5\u00d9\3\2\2\2\u00d6\u00d8\5\3\2\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00dc\u00dd\7%\2\2\u00dd\u00de\7%\2\2\u00de\u00df\3\2")
        buf.write("\2\2\u00df\u00e0\b\17\2\2\u00e0\36\3\2\2\2\u00e1\u00e2")
        buf.write("\7D\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5")
        buf.write("\7c\2\2\u00e5\u00e6\7m\2\2\u00e6 \3\2\2\2\u00e7\u00e8")
        buf.write("\7E\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7w\2\2\u00ee\u00ef\7g\2\2\u00ef\"\3\2\2\2\u00f0\u00f1")
        buf.write("\7K\2\2\u00f1\u00f2\7h\2\2\u00f2$\3\2\2\2\u00f3\u00f4")
        buf.write("\7G\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7h\2\2\u00f9&\3")
        buf.write("\2\2\2\u00fa\u00fb\7G\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd")
        buf.write("\7u\2\2\u00fd\u00fe\7g\2\2\u00fe(\3\2\2\2\u00ff\u0100")
        buf.write("\7H\2\2\u0100\u0101\7q\2\2\u0101\u0102\7t\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7c\2\2\u0104\u0105\7e\2\2\u0105\u0106")
        buf.write("\7j\2\2\u0106*\3\2\2\2\u0107\u0108\7V\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7w\2\2\u010a\u010b\7g\2\2\u010b,\3")
        buf.write("\2\2\2\u010c\u010d\7H\2\2\u010d\u010e\7c\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7u\2\2\u0110\u0111\7g\2\2\u0111.\3")
        buf.write("\2\2\2\u0112\u0113\7x\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7t\2\2\u0115\60\3\2\2\2\u0116\u0117\7x\2\2\u0117\u0118")
        buf.write("\7c\2\2\u0118\u0119\7n\2\2\u0119\62\3\2\2\2\u011a\u011b")
        buf.write("\7e\2\2\u011b\u011c\7n\2\2\u011c\u011d\7c\2\2\u011d\u011e")
        buf.write("\7u\2\2\u011e\u011f\7u\2\2\u011f\64\3\2\2\2\u0120\u0121")
        buf.write("\7C\2\2\u0121\u0122\7t\2\2\u0122\u0123\7t\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7{\2\2\u0125\66\3\2\2\2\u0126\u0127")
        buf.write("\7K\2\2\u0127\u0128\7p\2\2\u0128\u0129\7v\2\2\u01298\3")
        buf.write("\2\2\2\u012a\u012b\7H\2\2\u012b\u012c\7n\2\2\u012c\u012d")
        buf.write("\7q\2\2\u012d\u012e\7c\2\2\u012e\u012f\7v\2\2\u012f:\3")
        buf.write("\2\2\2\u0130\u0131\7D\2\2\u0131\u0132\7q\2\2\u0132\u0133")
        buf.write("\7q\2\2\u0133\u0134\7n\2\2\u0134\u0135\7g\2\2\u0135\u0136")
        buf.write("\7c\2\2\u0136\u0137\7p\2\2\u0137<\3\2\2\2\u0138\u0139")
        buf.write("\7U\2\2\u0139\u013a\7v\2\2\u013a\u013b\7t\2\2\u013b\u013c")
        buf.write("\7k\2\2\u013c\u013d\7p\2\2\u013d\u013e\7i\2\2\u013e>\3")
        buf.write("\2\2\2\u013f\u0140\7P\2\2\u0140\u0141\7w\2\2\u0141\u0142")
        buf.write("\7n\2\2\u0142\u0143\7n\2\2\u0143@\3\2\2\2\u0144\u0149")
        buf.write("\5\5\3\2\u0145\u0149\5\7\4\2\u0146\u0149\5\13\6\2\u0147")
        buf.write("\u0149\5\t\5\2\u0148\u0144\3\2\2\2\u0148\u0145\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014a\u014b\b!\3\2\u014bB\3\2\2\2\u014c\u0150\7")
        buf.write("$\2\2\u014d\u014f\5\r\7\2\u014e\u014d\3\2\2\2\u014f\u0152")
        buf.write("\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0153\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0154\7$\2\2")
        buf.write("\u0154\u0155\b\"\4\2\u0155D\3\2\2\2\u0156\u0159\5+\26")
        buf.write("\2\u0157\u0159\5-\27\2\u0158\u0156\3\2\2\2\u0158\u0157")
        buf.write("\3\2\2\2\u0159F\3\2\2\2\u015a\u015b\5\27\f\2\u015b\u015d")
        buf.write("\5\31\r\2\u015c\u015e\5\33\16\2\u015d\u015c\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\u0166\3\2\2\2\u015f\u0160\5\27\f")
        buf.write("\2\u0160\u0161\5\33\16\2\u0161\u0166\3\2\2\2\u0162\u0163")
        buf.write("\5\31\r\2\u0163\u0164\5\33\16\2\u0164\u0166\3\2\2\2\u0165")
        buf.write("\u015a\3\2\2\2\u0165\u015f\3\2\2\2\u0165\u0162\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0168\b$\5\2\u0168H\3\2\2\2")
        buf.write("\u0169\u016b\7&\2\2\u016a\u0169\3\2\2\2\u016a\u016b\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016c\u0170\t\21\2\2\u016d")
        buf.write("\u016f\t\22\2\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2")
        buf.write("\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171J\3\2")
        buf.write("\2\2\u0172\u0170\3\2\2\2\u0173\u0174\7-\2\2\u0174L\3\2")
        buf.write("\2\2\u0175\u0176\7/\2\2\u0176N\3\2\2\2\u0177\u0178\7,")
        buf.write("\2\2\u0178P\3\2\2\2\u0179\u017a\7\61\2\2\u017aR\3\2\2")
        buf.write("\2\u017b\u017c\7\'\2\2\u017cT\3\2\2\2\u017d\u017e\7#\2")
        buf.write("\2\u017eV\3\2\2\2\u017f\u0180\7(\2\2\u0180\u0181\7(\2")
        buf.write("\2\u0181X\3\2\2\2\u0182\u0183\7~\2\2\u0183\u0184\7~\2")
        buf.write("\2\u0184Z\3\2\2\2\u0185\u0186\7?\2\2\u0186\u0187\7?\2")
        buf.write("\2\u0187\\\3\2\2\2\u0188\u0189\7?\2\2\u0189^\3\2\2\2\u018a")
        buf.write("\u018b\7#\2\2\u018b\u018c\7?\2\2\u018c`\3\2\2\2\u018d")
        buf.write("\u018e\7>\2\2\u018eb\3\2\2\2\u018f\u0190\7>\2\2\u0190")
        buf.write("\u0191\7?\2\2\u0191d\3\2\2\2\u0192\u0193\7@\2\2\u0193")
        buf.write("f\3\2\2\2\u0194\u0195\7@\2\2\u0195\u0196\7?\2\2\u0196")
        buf.write("h\3\2\2\2\u0197\u0198\7?\2\2\u0198\u0199\7?\2\2\u0199")
        buf.write("\u019a\7\60\2\2\u019aj\3\2\2\2\u019b\u019c\7-\2\2\u019c")
        buf.write("\u019d\7\60\2\2\u019dl\3\2\2\2\u019e\u019f\7*\2\2\u019f")
        buf.write("n\3\2\2\2\u01a0\u01a1\7+\2\2\u01a1p\3\2\2\2\u01a2\u01a3")
        buf.write("\7]\2\2\u01a3r\3\2\2\2\u01a4\u01a5\7_\2\2\u01a5t\3\2\2")
        buf.write("\2\u01a6\u01a7\7\60\2\2\u01a7v\3\2\2\2\u01a8\u01a9\7.")
        buf.write("\2\2\u01a9x\3\2\2\2\u01aa\u01ab\7=\2\2\u01abz\3\2\2\2")
        buf.write("\u01ac\u01ad\7<\2\2\u01ad|\3\2\2\2\u01ae\u01af\7}\2\2")
        buf.write("\u01af~\3\2\2\2\u01b0\u01b1\7\177\2\2\u01b1\u0080\3\2")
        buf.write("\2\2\u01b2\u01b4\t\23\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b8\bA\2\2\u01b8\u0082\3\2\2\2")
        buf.write("\u01b9\u01ba\7%\2\2\u01ba\u01bb\7%\2\2\u01bb\u01bf\3\2")
        buf.write("\2\2\u01bc\u01be\5\3\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01cf\7\2\2\3")
        buf.write("\u01c3\u01c4\7%\2\2\u01c4\u01c5\7%\2\2\u01c5\u01c9\3\2")
        buf.write("\2\2\u01c6\u01c8\n\2\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01cc\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd\7%\2\2")
        buf.write("\u01cd\u01cf\7\2\2\3\u01ce\u01b9\3\2\2\2\u01ce\u01c3\3")
        buf.write("\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\bB\6\2\u01d1\u0084")
        buf.write("\3\2\2\2\u01d2\u01d6\7$\2\2\u01d3\u01d5\5\r\7\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3")
        buf.write("\2\2\2\u01d9\u01db\t\24\2\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01dd\bC\7\2\u01dd\u0086\3\2\2\2")
        buf.write("\u01de\u01e2\7$\2\2\u01df\u01e1\5\r\7\2\u01e0\u01df\3")
        buf.write("\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5")
        buf.write("\u01e6\5\23\n\2\u01e6\u01e7\bD\b\2\u01e7\u0088\3\2\2\2")
        buf.write("\u01e8\u01e9\13\2\2\2\u01e9\u01ea\bE\t\2\u01ea\u008a\3")
        buf.write("\2\2\2\35\2\u008e\u0095\u0098\u009e\u00a5\u00ac\u00b1")
        buf.write("\u00be\u00c6\u00cb\u00cf\u00d9\u0148\u0150\u0158\u015d")
        buf.write("\u0165\u016a\u0170\u01b5\u01bf\u01c9\u01ce\u01d6\u01da")
        buf.write("\u01e2\n\b\2\2\3!\2\3\"\3\3$\4\3B\5\3C\6\3D\7\3E\b")
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
    ID = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQUAL = 30
    ASSIGN = 31
    NOT_EQUAL = 32
    LT = 33
    LTE = 34
    GT = 35
    GTE = 36
    STRING_EQUAL = 37
    STRING_ADD = 38
    LP = 39
    RP = 40
    LSB = 41
    RSB = 42
    DOT = 43
    COMMA = 44
    SEMI = 45
    COLON = 46
    LCB = 47
    RCB = 48
    WS = 49
    UNTERMINATED_COMMENT = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52
    ERROR_TOKEN = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'var'", "'val'", "'class'", "'Array'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Null'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'==.'", "'+.'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "';'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "VAR", "VAL", "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "NULL", "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "FLOAT_LITERAL", "ID", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", 
            "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", "LSB", "RSB", 
            "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "WS", "UNTERMINATED_COMMENT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "COMMENT_CHAR", "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", 
                  "BIN_INTEGER_LITERAL", "HEX_INTEGER_LITERAL", "STRING_CHAR", 
                  "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", 
                  "SIGN", "FLOAT_INTEGER_PART", "FLOAT_DECIMAL_PART", "FLOAT_EXPONENT_PART", 
                  "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "VAR", "VAL", "CLASS", "ARRAY", 
                  "INT", "FLOAT", "BOOLEAN", "STRING", "NULL", "INTEGER_LITERAL", 
                  "STRING_LITERAL", "BOOLEAN_LITERAL", "FLOAT_LITERAL", 
                  "ID", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", 
                  "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", "LSB", 
                  "RSB", "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", 
                  "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_TOKEN" ]

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
            actions[64] = self.UNTERMINATED_COMMENT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_TOKEN_action 
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

     


