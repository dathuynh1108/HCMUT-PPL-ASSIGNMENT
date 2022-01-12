# Generated from d:\Workspace\PPL\Assignment\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u025b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\5\4\u00c5\n\4\3\5\3\5\7\5\u00c9\n\5\f\5\16\5\u00cc")
        buf.write("\13\5\3\5\7\5\u00cf\n\5\f\5\16\5\u00d2\13\5\3\5\5\5\u00d5")
        buf.write("\n\5\3\6\3\6\6\6\u00d9\n\6\r\6\16\6\u00da\3\7\3\7\3\7")
        buf.write("\6\7\u00e0\n\7\r\7\16\7\u00e1\3\b\3\b\3\b\6\b\u00e7\n")
        buf.write("\b\r\b\16\b\u00e8\3\t\3\t\3\t\5\t\u00ee\n\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00fa\n\f\3\r\3")
        buf.write("\r\3\16\3\16\7\16\u0100\n\16\f\16\16\16\u0103\13\16\3")
        buf.write("\17\3\17\5\17\u0107\n\17\3\20\3\20\5\20\u010b\n\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\7\21\u0113\n\21\f\21\16\21\u0116")
        buf.write("\13\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\5*\u01b1")
        buf.write("\n*\3*\3*\3+\3+\7+\u01b7\n+\f+\16+\u01ba\13+\3+\3+\3+")
        buf.write("\3,\3,\5,\u01c1\n,\3-\3-\3-\5-\u01c6\n-\3-\3-\3-\3-\3")
        buf.write("-\3-\5-\u01ce\n-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\67\3\67\38\38\38\39\39\3:\3:\3:\3;\3;\3<")
        buf.write("\3<\3<\3=\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3")
        buf.write("C\3C\3D\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\3I\3I\3J\3J\3")
        buf.write("K\3K\7K\u0219\nK\fK\16K\u021c\13K\3L\3L\3L\7L\u0221\n")
        buf.write("L\fL\16L\u0224\13L\3M\6M\u0227\nM\rM\16M\u0228\3M\3M\3")
        buf.write("N\3N\3N\3N\7N\u0231\nN\fN\16N\u0234\13N\3N\3N\3N\3N\3")
        buf.write("N\7N\u023b\nN\fN\16N\u023e\13N\3N\3N\5N\u0242\nN\3N\3")
        buf.write("N\3O\3O\7O\u0248\nO\fO\16O\u024b\13O\3O\3O\3P\3P\7P\u0251")
        buf.write("\nP\fP\16P\u0254\13P\3P\3P\3P\3Q\3Q\3Q\2\2R\3\3\5\4\7")
        buf.write("\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35")
        buf.write("\2\37\2!\5#\6%\7\'\b)\t+\n-\13/\2\61\2\63\f\65\r\67\16")
        buf.write("9\17;\20=\21?\22A\23C\24E\25G\26I\27K\30M\31O\32Q\33S")
        buf.write("\34U\35W\36Y\37[ ]!_\"a#c$e%g&i\'k(m)o*q+s,u-w.y/{\60")
        buf.write("}\61\177\62\u0081\63\u0083\64\u0085\65\u0087\66\u0089")
        buf.write("\67\u008b8\u008d9\u008f:\u0091;\u0093<\u0095=\u0097>\u0099")
        buf.write("?\u009b@\u009dA\u009fB\u00a1C\3\2\23\3\2%%\3\2\63;\3\2")
        buf.write("\62;\3\2\629\4\2DDdd\3\2\62\63\4\2ZZzz\5\2\62;CHch\7\2")
        buf.write("\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2$$\4\2--//\4\2\62")
        buf.write(";aa\4\2GGgg\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"")
        buf.write("\"\2\u0269\2\3\3\2\2\2\2\5\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\3\u00a3\3\2\2\2\5\u00ac\3\2\2\2\7\u00c4\3\2\2")
        buf.write("\2\t\u00d4\3\2\2\2\13\u00d6\3\2\2\2\r\u00dc\3\2\2\2\17")
        buf.write("\u00e3\3\2\2\2\21\u00ed\3\2\2\2\23\u00ef\3\2\2\2\25\u00f2")
        buf.write("\3\2\2\2\27\u00f9\3\2\2\2\31\u00fb\3\2\2\2\33\u00fd\3")
        buf.write("\2\2\2\35\u0104\3\2\2\2\37\u0108\3\2\2\2!\u010e\3\2\2")
        buf.write("\2#\u011c\3\2\2\2%\u0122\3\2\2\2\'\u012b\3\2\2\2)\u012e")
        buf.write("\3\2\2\2+\u0135\3\2\2\2-\u013a\3\2\2\2/\u0142\3\2\2\2")
        buf.write("\61\u0147\3\2\2\2\63\u014d\3\2\2\2\65\u0151\3\2\2\2\67")
        buf.write("\u0155\3\2\2\29\u015a\3\2\2\2;\u0161\3\2\2\2=\u0164\3")
        buf.write("\2\2\2?\u0167\3\2\2\2A\u016b\3\2\2\2C\u0177\3\2\2\2E\u0182")
        buf.write("\3\2\2\2G\u0187\3\2\2\2I\u018d\3\2\2\2K\u0193\3\2\2\2")
        buf.write("M\u0197\3\2\2\2O\u019d\3\2\2\2Q\u01a5\3\2\2\2S\u01b0\3")
        buf.write("\2\2\2U\u01b4\3\2\2\2W\u01c0\3\2\2\2Y\u01cd\3\2\2\2[\u01d1")
        buf.write("\3\2\2\2]\u01d3\3\2\2\2_\u01d5\3\2\2\2a\u01d7\3\2\2\2")
        buf.write("c\u01d9\3\2\2\2e\u01db\3\2\2\2g\u01dd\3\2\2\2i\u01e0\3")
        buf.write("\2\2\2k\u01e3\3\2\2\2m\u01e6\3\2\2\2o\u01e8\3\2\2\2q\u01eb")
        buf.write("\3\2\2\2s\u01ed\3\2\2\2u\u01f0\3\2\2\2w\u01f2\3\2\2\2")
        buf.write("y\u01f5\3\2\2\2{\u01f9\3\2\2\2}\u01fc\3\2\2\2\177\u01fe")
        buf.write("\3\2\2\2\u0081\u0200\3\2\2\2\u0083\u0202\3\2\2\2\u0085")
        buf.write("\u0204\3\2\2\2\u0087\u0206\3\2\2\2\u0089\u0209\3\2\2\2")
        buf.write("\u008b\u020b\3\2\2\2\u008d\u020d\3\2\2\2\u008f\u020f\3")
        buf.write("\2\2\2\u0091\u0212\3\2\2\2\u0093\u0214\3\2\2\2\u0095\u0216")
        buf.write("\3\2\2\2\u0097\u021d\3\2\2\2\u0099\u0226\3\2\2\2\u009b")
        buf.write("\u0241\3\2\2\2\u009d\u0245\3\2\2\2\u009f\u024e\3\2\2\2")
        buf.write("\u00a1\u0258\3\2\2\2\u00a3\u00a4\7E\2\2\u00a4\u00a5\7")
        buf.write("j\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8")
        buf.write("\7\"\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab")
        buf.write("\7o\2\2\u00ab\4\3\2\2\2\u00ac\u00ad\7E\2\2\u00ad\u00ae")
        buf.write("\7j\2\2\u00ae\u00af\7\u00c8\2\2\u00af\u00b0\7\u00b2\2")
        buf.write("\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7\"\2\2\u00b2\u00b3")
        buf.write("\7d\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7\u00e3\2\2\u00b5")
        buf.write("\u00b6\7\u00bc\2\2\u00b6\u00b7\7\u00c1\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7\"\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7\u0104\2\2\u00bb\u00bc\7\u00a2\2\2\u00bc\u00bd\7o\2")
        buf.write("\2\u00bd\u00be\7\"\2\2\u00be\u00bf\7<\2\2\u00bf\u00c0")
        buf.write("\7+\2\2\u00c0\6\3\2\2\2\u00c1\u00c5\n\2\2\2\u00c2\u00c3")
        buf.write("\7%\2\2\u00c3\u00c5\n\2\2\2\u00c4\u00c1\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c5\b\3\2\2\2\u00c6\u00d0\t\3\2\2\u00c7")
        buf.write("\u00c9\7a\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2")
        buf.write("\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd\3")
        buf.write("\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00cf\t\4\2\2\u00ce\u00ca")
        buf.write("\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\u00d5\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d3\u00d5\7\62\2\2\u00d4\u00c6\3\2\2\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5\n\3\2\2\2\u00d6\u00d8\7\62\2\2\u00d7\u00d9")
        buf.write("\t\5\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\f\3\2\2\2\u00dc")
        buf.write("\u00dd\7\62\2\2\u00dd\u00df\t\6\2\2\u00de\u00e0\t\7\2")
        buf.write("\2\u00df\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\16\3\2\2\2\u00e3\u00e4")
        buf.write("\7\62\2\2\u00e4\u00e6\t\b\2\2\u00e5\u00e7\t\t\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\20\3\2\2\2\u00ea\u00ee\n\n")
        buf.write("\2\2\u00eb\u00ee\5\23\n\2\u00ec\u00ee\5\25\13\2\u00ed")
        buf.write("\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2")
        buf.write("\u00ee\22\3\2\2\2\u00ef\u00f0\7^\2\2\u00f0\u00f1\t\13")
        buf.write("\2\2\u00f1\24\3\2\2\2\u00f2\u00f3\7)\2\2\u00f3\u00f4\7")
        buf.write("$\2\2\u00f4\26\3\2\2\2\u00f5\u00f6\7^\2\2\u00f6\u00fa")
        buf.write("\n\13\2\2\u00f7\u00f8\7)\2\2\u00f8\u00fa\n\f\2\2\u00f9")
        buf.write("\u00f5\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\30\3\2\2\2\u00fb")
        buf.write("\u00fc\t\r\2\2\u00fc\32\3\2\2\2\u00fd\u0101\t\4\2\2\u00fe")
        buf.write("\u0100\t\16\2\2\u00ff\u00fe\3\2\2\2\u0100\u0103\3\2\2")
        buf.write("\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102\34\3")
        buf.write("\2\2\2\u0103\u0101\3\2\2\2\u0104\u0106\7\60\2\2\u0105")
        buf.write("\u0107\5\33\16\2\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2")
        buf.write("\2\u0107\36\3\2\2\2\u0108\u010a\t\17\2\2\u0109\u010b\5")
        buf.write("\31\r\2\u010a\u0109\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c\u010d\5\33\16\2\u010d \3\2\2\2\u010e")
        buf.write("\u010f\7%\2\2\u010f\u0110\7%\2\2\u0110\u0114\3\2\2\2\u0111")
        buf.write("\u0113\5\7\4\2\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3")
        buf.write("\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\7%\2\2\u0118\u0119")
        buf.write("\7%\2\2\u0119\u011a\3\2\2\2\u011a\u011b\b\21\2\2\u011b")
        buf.write("\"\3\2\2\2\u011c\u011d\7D\2\2\u011d\u011e\7t\2\2\u011e")
        buf.write("\u011f\7g\2\2\u011f\u0120\7c\2\2\u0120\u0121\7m\2\2\u0121")
        buf.write("$\3\2\2\2\u0122\u0123\7E\2\2\u0123\u0124\7q\2\2\u0124")
        buf.write("\u0125\7p\2\2\u0125\u0126\7v\2\2\u0126\u0127\7k\2\2\u0127")
        buf.write("\u0128\7p\2\2\u0128\u0129\7w\2\2\u0129\u012a\7g\2\2\u012a")
        buf.write("&\3\2\2\2\u012b\u012c\7K\2\2\u012c\u012d\7h\2\2\u012d")
        buf.write("(\3\2\2\2\u012e\u012f\7G\2\2\u012f\u0130\7n\2\2\u0130")
        buf.write("\u0131\7u\2\2\u0131\u0132\7g\2\2\u0132\u0133\7k\2\2\u0133")
        buf.write("\u0134\7h\2\2\u0134*\3\2\2\2\u0135\u0136\7G\2\2\u0136")
        buf.write("\u0137\7n\2\2\u0137\u0138\7u\2\2\u0138\u0139\7g\2\2\u0139")
        buf.write(",\3\2\2\2\u013a\u013b\7H\2\2\u013b\u013c\7q\2\2\u013c")
        buf.write("\u013d\7t\2\2\u013d\u013e\7g\2\2\u013e\u013f\7c\2\2\u013f")
        buf.write("\u0140\7e\2\2\u0140\u0141\7j\2\2\u0141.\3\2\2\2\u0142")
        buf.write("\u0143\7V\2\2\u0143\u0144\7t\2\2\u0144\u0145\7w\2\2\u0145")
        buf.write("\u0146\7g\2\2\u0146\60\3\2\2\2\u0147\u0148\7H\2\2\u0148")
        buf.write("\u0149\7c\2\2\u0149\u014a\7n\2\2\u014a\u014b\7u\2\2\u014b")
        buf.write("\u014c\7g\2\2\u014c\62\3\2\2\2\u014d\u014e\7X\2\2\u014e")
        buf.write("\u014f\7c\2\2\u014f\u0150\7t\2\2\u0150\64\3\2\2\2\u0151")
        buf.write("\u0152\7X\2\2\u0152\u0153\7c\2\2\u0153\u0154\7n\2\2\u0154")
        buf.write("\66\3\2\2\2\u0155\u0156\7U\2\2\u0156\u0157\7g\2\2\u0157")
        buf.write("\u0158\7n\2\2\u0158\u0159\7h\2\2\u01598\3\2\2\2\u015a")
        buf.write("\u015b\7T\2\2\u015b\u015c\7g\2\2\u015c\u015d\7v\2\2\u015d")
        buf.write("\u015e\7w\2\2\u015e\u015f\7t\2\2\u015f\u0160\7p\2\2\u0160")
        buf.write(":\3\2\2\2\u0161\u0162\7K\2\2\u0162\u0163\7p\2\2\u0163")
        buf.write("<\3\2\2\2\u0164\u0165\7D\2\2\u0165\u0166\7{\2\2\u0166")
        buf.write(">\3\2\2\2\u0167\u0168\7P\2\2\u0168\u0169\7g\2\2\u0169")
        buf.write("\u016a\7y\2\2\u016a@\3\2\2\2\u016b\u016c\7E\2\2\u016c")
        buf.write("\u016d\7q\2\2\u016d\u016e\7p\2\2\u016e\u016f\7u\2\2\u016f")
        buf.write("\u0170\7v\2\2\u0170\u0171\7t\2\2\u0171\u0172\7w\2\2\u0172")
        buf.write("\u0173\7e\2\2\u0173\u0174\7v\2\2\u0174\u0175\7q\2\2\u0175")
        buf.write("\u0176\7t\2\2\u0176B\3\2\2\2\u0177\u0178\7F\2\2\u0178")
        buf.write("\u0179\7g\2\2\u0179\u017a\7u\2\2\u017a\u017b\7v\2\2\u017b")
        buf.write("\u017c\7t\2\2\u017c\u017d\7w\2\2\u017d\u017e\7e\2\2\u017e")
        buf.write("\u017f\7v\2\2\u017f\u0180\7q\2\2\u0180\u0181\7t\2\2\u0181")
        buf.write("D\3\2\2\2\u0182\u0183\7P\2\2\u0183\u0184\7w\2\2\u0184")
        buf.write("\u0185\7n\2\2\u0185\u0186\7n\2\2\u0186F\3\2\2\2\u0187")
        buf.write("\u0188\7E\2\2\u0188\u0189\7n\2\2\u0189\u018a\7c\2\2\u018a")
        buf.write("\u018b\7u\2\2\u018b\u018c\7u\2\2\u018cH\3\2\2\2\u018d")
        buf.write("\u018e\7C\2\2\u018e\u018f\7t\2\2\u018f\u0190\7t\2\2\u0190")
        buf.write("\u0191\7c\2\2\u0191\u0192\7{\2\2\u0192J\3\2\2\2\u0193")
        buf.write("\u0194\7K\2\2\u0194\u0195\7p\2\2\u0195\u0196\7v\2\2\u0196")
        buf.write("L\3\2\2\2\u0197\u0198\7H\2\2\u0198\u0199\7n\2\2\u0199")
        buf.write("\u019a\7q\2\2\u019a\u019b\7c\2\2\u019b\u019c\7v\2\2\u019c")
        buf.write("N\3\2\2\2\u019d\u019e\7D\2\2\u019e\u019f\7q\2\2\u019f")
        buf.write("\u01a0\7q\2\2\u01a0\u01a1\7n\2\2\u01a1\u01a2\7g\2\2\u01a2")
        buf.write("\u01a3\7c\2\2\u01a3\u01a4\7p\2\2\u01a4P\3\2\2\2\u01a5")
        buf.write("\u01a6\7U\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8\7t\2\2\u01a8")
        buf.write("\u01a9\7k\2\2\u01a9\u01aa\7p\2\2\u01aa\u01ab\7i\2\2\u01ab")
        buf.write("R\3\2\2\2\u01ac\u01b1\5\t\5\2\u01ad\u01b1\5\13\6\2\u01ae")
        buf.write("\u01b1\5\17\b\2\u01af\u01b1\5\r\7\2\u01b0\u01ac\3\2\2")
        buf.write("\2\u01b0\u01ad\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\b*\3\2\u01b3")
        buf.write("T\3\2\2\2\u01b4\u01b8\7$\2\2\u01b5\u01b7\5\21\t\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3")
        buf.write("\2\2\2\u01bb\u01bc\7$\2\2\u01bc\u01bd\b+\4\2\u01bdV\3")
        buf.write("\2\2\2\u01be\u01c1\5/\30\2\u01bf\u01c1\5\61\31\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1X\3\2\2\2\u01c2")
        buf.write("\u01c3\5\33\16\2\u01c3\u01c5\5\35\17\2\u01c4\u01c6\5\37")
        buf.write("\20\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01ce")
        buf.write("\3\2\2\2\u01c7\u01c8\5\33\16\2\u01c8\u01c9\5\37\20\2\u01c9")
        buf.write("\u01ce\3\2\2\2\u01ca\u01cb\5\35\17\2\u01cb\u01cc\5\37")
        buf.write("\20\2\u01cc\u01ce\3\2\2\2\u01cd\u01c2\3\2\2\2\u01cd\u01c7")
        buf.write("\3\2\2\2\u01cd\u01ca\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d0\b-\5\2\u01d0Z\3\2\2\2\u01d1\u01d2\7-\2\2\u01d2")
        buf.write("\\\3\2\2\2\u01d3\u01d4\7/\2\2\u01d4^\3\2\2\2\u01d5\u01d6")
        buf.write("\7,\2\2\u01d6`\3\2\2\2\u01d7\u01d8\7\61\2\2\u01d8b\3\2")
        buf.write("\2\2\u01d9\u01da\7\'\2\2\u01dad\3\2\2\2\u01db\u01dc\7")
        buf.write("#\2\2\u01dcf\3\2\2\2\u01dd\u01de\7(\2\2\u01de\u01df\7")
        buf.write("(\2\2\u01dfh\3\2\2\2\u01e0\u01e1\7~\2\2\u01e1\u01e2\7")
        buf.write("~\2\2\u01e2j\3\2\2\2\u01e3\u01e4\7?\2\2\u01e4\u01e5\7")
        buf.write("?\2\2\u01e5l\3\2\2\2\u01e6\u01e7\7?\2\2\u01e7n\3\2\2\2")
        buf.write("\u01e8\u01e9\7#\2\2\u01e9\u01ea\7?\2\2\u01eap\3\2\2\2")
        buf.write("\u01eb\u01ec\7>\2\2\u01ecr\3\2\2\2\u01ed\u01ee\7>\2\2")
        buf.write("\u01ee\u01ef\7?\2\2\u01eft\3\2\2\2\u01f0\u01f1\7@\2\2")
        buf.write("\u01f1v\3\2\2\2\u01f2\u01f3\7@\2\2\u01f3\u01f4\7?\2\2")
        buf.write("\u01f4x\3\2\2\2\u01f5\u01f6\7?\2\2\u01f6\u01f7\7?\2\2")
        buf.write("\u01f7\u01f8\7\60\2\2\u01f8z\3\2\2\2\u01f9\u01fa\7-\2")
        buf.write("\2\u01fa\u01fb\7\60\2\2\u01fb|\3\2\2\2\u01fc\u01fd\7*")
        buf.write("\2\2\u01fd~\3\2\2\2\u01fe\u01ff\7+\2\2\u01ff\u0080\3\2")
        buf.write("\2\2\u0200\u0201\7]\2\2\u0201\u0082\3\2\2\2\u0202\u0203")
        buf.write("\7_\2\2\u0203\u0084\3\2\2\2\u0204\u0205\7\60\2\2\u0205")
        buf.write("\u0086\3\2\2\2\u0206\u0207\7\60\2\2\u0207\u0208\7\60\2")
        buf.write("\2\u0208\u0088\3\2\2\2\u0209\u020a\7.\2\2\u020a\u008a")
        buf.write("\3\2\2\2\u020b\u020c\7=\2\2\u020c\u008c\3\2\2\2\u020d")
        buf.write("\u020e\7<\2\2\u020e\u008e\3\2\2\2\u020f\u0210\7<\2\2\u0210")
        buf.write("\u0211\7<\2\2\u0211\u0090\3\2\2\2\u0212\u0213\7}\2\2\u0213")
        buf.write("\u0092\3\2\2\2\u0214\u0215\7\177\2\2\u0215\u0094\3\2\2")
        buf.write("\2\u0216\u021a\t\20\2\2\u0217\u0219\t\21\2\2\u0218\u0217")
        buf.write("\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u0096\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021d\u021e\7&\2\2\u021e\u0222\t\20\2\2\u021f\u0221\t")
        buf.write("\21\2\2\u0220\u021f\3\2\2\2\u0221\u0224\3\2\2\2\u0222")
        buf.write("\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0098\3\2\2\2")
        buf.write("\u0224\u0222\3\2\2\2\u0225\u0227\t\22\2\2\u0226\u0225")
        buf.write("\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0226\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b\bM\2\2")
        buf.write("\u022b\u009a\3\2\2\2\u022c\u022d\7%\2\2\u022d\u022e\7")
        buf.write("%\2\2\u022e\u0232\3\2\2\2\u022f\u0231\5\7\4\2\u0230\u022f")
        buf.write("\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0232")
        buf.write("\u0233\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0232\3\2\2\2")
        buf.write("\u0235\u0242\7\2\2\3\u0236\u0237\7%\2\2\u0237\u0238\7")
        buf.write("%\2\2\u0238\u023c\3\2\2\2\u0239\u023b\n\2\2\2\u023a\u0239")
        buf.write("\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023c")
        buf.write("\u023d\3\2\2\2\u023d\u023f\3\2\2\2\u023e\u023c\3\2\2\2")
        buf.write("\u023f\u0240\7%\2\2\u0240\u0242\7\2\2\3\u0241\u022c\3")
        buf.write("\2\2\2\u0241\u0236\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0244")
        buf.write("\bN\6\2\u0244\u009c\3\2\2\2\u0245\u0249\7$\2\2\u0246\u0248")
        buf.write("\5\21\t\2\u0247\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249")
        buf.write("\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024c\3\2\2\2")
        buf.write("\u024b\u0249\3\2\2\2\u024c\u024d\bO\7\2\u024d\u009e\3")
        buf.write("\2\2\2\u024e\u0252\7$\2\2\u024f\u0251\5\21\t\2\u0250\u024f")
        buf.write("\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250\3\2\2\2\u0252")
        buf.write("\u0253\3\2\2\2\u0253\u0255\3\2\2\2\u0254\u0252\3\2\2\2")
        buf.write("\u0255\u0256\5\27\f\2\u0256\u0257\bP\b\2\u0257\u00a0\3")
        buf.write("\2\2\2\u0258\u0259\13\2\2\2\u0259\u025a\bQ\t\2\u025a\u00a2")
        buf.write("\3\2\2\2\35\2\u00c4\u00ca\u00d0\u00d4\u00da\u00e1\u00e8")
        buf.write("\u00ed\u00f9\u0101\u0106\u010a\u0114\u01b0\u01b8\u01c0")
        buf.write("\u01c5\u01cd\u021a\u0222\u0228\u0232\u023c\u0241\u0249")
        buf.write("\u0252\n\b\2\2\3*\2\3+\3\3-\4\3N\5\3O\6\3P\7\3Q\b")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    COMMENT = 3
    BREAK = 4
    CONTINUE = 5
    IF = 6
    ELSEIF = 7
    ELSE = 8
    FOREACH = 9
    VAR = 10
    VAL = 11
    SELF = 12
    RETURN = 13
    IN = 14
    BY = 15
    NEW = 16
    CONSTRUCTOR = 17
    DESTRUCTOR = 18
    NULL = 19
    CLASS = 20
    ARRAY = 21
    INTEGER = 22
    FLOAT = 23
    BOOLEAN = 24
    STRING = 25
    INTEGER_LITERAL = 26
    STRING_LITERAL = 27
    BOOLEAN_LITERAL = 28
    FLOAT_LITERAL = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL = 38
    ASSIGN = 39
    NOT_EQUAL = 40
    LT = 41
    LTE = 42
    GT = 43
    GTE = 44
    STRING_EQUAL = 45
    STRING_ADD = 46
    LP = 47
    RP = 48
    LSB = 49
    RSB = 50
    DOT = 51
    DOUBLE_DOT = 52
    COMMA = 53
    SEMI = 54
    COLON = 55
    DOUBLE_COLON = 56
    LCB = 57
    RCB = 58
    ID = 59
    DOLLAR_ID = 60
    WS = 61
    UNTERMINATED_COMMENT = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ERROR_TOKEN = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Chua lam'", "'Ch\u00C6\u00B0a bi\u00E1\u00BA\u00BFt l\u0102\u00A0m :)'", 
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
            "RCB", "ID", "DOLLAR_ID", "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "T__1", "COMMENT_CHAR", "DEC_INTEGER_LITERAL", 
                  "OCT_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", "HEX_INTEGER_LITERAL", 
                  "STRING_CHAR", "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_CHAR", 
                  "ILLEGAL_SEQUENCE", "SIGN", "FLOAT_INTEGER_PART", "FLOAT_DECIMAL_PART", 
                  "FLOAT_EXPONENT_PART", "COMMENT", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "VAR", 
                  "VAL", "SELF", "RETURN", "IN", "BY", "NEW", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NULL", "CLASS", "ARRAY", "INTEGER", "FLOAT", 
                  "BOOLEAN", "STRING", "INTEGER_LITERAL", "STRING_LITERAL", 
                  "BOOLEAN_LITERAL", "FLOAT_LITERAL", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                  "LT", "LTE", "GT", "GTE", "STRING_EQUAL", "STRING_ADD", 
                  "LP", "RP", "LSB", "RSB", "DOT", "DOUBLE_DOT", "COMMA", 
                  "SEMI", "COLON", "DOUBLE_COLON", "LCB", "RCB", "ID", "DOLLAR_ID", 
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
            actions[40] = self.INTEGER_LITERAL_action 
            actions[41] = self.STRING_LITERAL_action 
            actions[43] = self.FLOAT_LITERAL_action 
            actions[76] = self.UNTERMINATED_COMMENT_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ILLEGAL_ESCAPE_action 
            actions[79] = self.ERROR_TOKEN_action 
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

            	raise UnterminatedComment()

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise UncloseString(self.text[1:]);

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                raise ErrorToken(self.text)

     


