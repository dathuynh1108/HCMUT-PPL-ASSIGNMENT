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
        buf.write("\u024a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4\u00bf\n\4\3")
        buf.write("\5\3\5\3\5\7\5\u00c4\n\5\f\5\16\5\u00c7\13\5\5\5\u00c9")
        buf.write("\n\5\3\6\3\6\6\6\u00cd\n\6\r\6\16\6\u00ce\3\7\3\7\3\7")
        buf.write("\6\7\u00d4\n\7\r\7\16\7\u00d5\3\b\3\b\3\b\6\b\u00db\n")
        buf.write("\b\r\b\16\b\u00dc\3\t\3\t\3\t\5\t\u00e2\n\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00ef\n\f\3")
        buf.write("\r\3\r\3\16\3\16\7\16\u00f5\n\16\f\16\16\16\u00f8\13\16")
        buf.write("\3\17\3\17\5\17\u00fc\n\17\3\20\3\20\5\20\u0100\n\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\7\21\u0108\n\21\f\21\16\21")
        buf.write("\u010b\13\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\5\'\u019c")
        buf.write("\n\'\3\'\3\'\3(\3(\7(\u01a2\n(\f(\16(\u01a5\13(\3(\3(")
        buf.write("\3(\3)\3)\5)\u01ac\n)\3*\3*\3*\5*\u01b1\n*\3*\3*\3*\3")
        buf.write("*\3*\3*\5*\u01b9\n*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\39\39\39\3:\3:\3:\3:\3;\3;\3;\3<\3<\3<\3<\3=\3")
        buf.write("=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3E\3")
        buf.write("F\3F\3G\3G\3H\3H\7H\u0205\nH\fH\16H\u0208\13H\3I\3I\3")
        buf.write("I\7I\u020d\nI\fI\16I\u0210\13I\3J\6J\u0213\nJ\rJ\16J\u0214")
        buf.write("\3J\3J\3K\3K\3K\3K\7K\u021d\nK\fK\16K\u0220\13K\3K\3K")
        buf.write("\3K\3K\3K\7K\u0227\nK\fK\16K\u022a\13K\3K\3K\5K\u022e")
        buf.write("\nK\3K\3K\3L\3L\7L\u0234\nL\fL\16L\u0237\13L\3L\5L\u023a")
        buf.write("\nL\3L\3L\3M\3M\7M\u0240\nM\fM\16M\u0243\13M\3M\3M\3M")
        buf.write("\3N\3N\3N\2\2O\3\3\5\4\7\2\t\2\13\2\r\2\17\2\21\2\23\2")
        buf.write("\25\2\27\2\31\2\33\2\35\2\37\2!\5#\6%\7\'\b)\t+\n-\13")
        buf.write("/\2\61\2\63\f\65\r\67\169\17;\20=\21?\22A\23C\24E\25G")
        buf.write("\26I\27K\30M\31O\32Q\33S\34U\35W\36Y\37[ ]!_\"a#c$e%g")
        buf.write("&i\'k(m)o*q+s,u-w.y/{\60}\61\177\62\u0081\63\u0083\64")
        buf.write("\u0085\65\u0087\66\u0089\67\u008b8\u008d9\u008f:\u0091")
        buf.write(";\u0093<\u0095=\u0097>\u0099?\u009b@\3\2\25\3\2%%\3\2")
        buf.write("\63;\4\2\62;aa\3\2\629\4\2DDdd\3\2\62\63\4\2ZZzz\5\2\62")
        buf.write(";CHch\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2$$\3\2")
        buf.write("^^\4\2--//\3\2\62;\4\2GGgg\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\13\f\16\17\"\"\7\3\n\f\16\17$$))^^\2\u0258\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\3\u009d\3\2\2\2\5\u00ac\3\2\2\2\7\u00be\3\2\2\2\t\u00c8")
        buf.write("\3\2\2\2\13\u00ca\3\2\2\2\r\u00d0\3\2\2\2\17\u00d7\3\2")
        buf.write("\2\2\21\u00e1\3\2\2\2\23\u00e3\3\2\2\2\25\u00e6\3\2\2")
        buf.write("\2\27\u00ee\3\2\2\2\31\u00f0\3\2\2\2\33\u00f2\3\2\2\2")
        buf.write("\35\u00f9\3\2\2\2\37\u00fd\3\2\2\2!\u0103\3\2\2\2#\u0111")
        buf.write("\3\2\2\2%\u0117\3\2\2\2\'\u0120\3\2\2\2)\u0123\3\2\2\2")
        buf.write("+\u012a\3\2\2\2-\u012f\3\2\2\2/\u0137\3\2\2\2\61\u013c")
        buf.write("\3\2\2\2\63\u0142\3\2\2\2\65\u0146\3\2\2\2\67\u014a\3")
        buf.write("\2\2\29\u014f\3\2\2\2;\u0156\3\2\2\2=\u0162\3\2\2\2?\u016d")
        buf.write("\3\2\2\2A\u0173\3\2\2\2C\u0179\3\2\2\2E\u017d\3\2\2\2")
        buf.write("G\u0183\3\2\2\2I\u018b\3\2\2\2K\u0192\3\2\2\2M\u019b\3")
        buf.write("\2\2\2O\u019f\3\2\2\2Q\u01ab\3\2\2\2S\u01b8\3\2\2\2U\u01bc")
        buf.write("\3\2\2\2W\u01be\3\2\2\2Y\u01c0\3\2\2\2[\u01c2\3\2\2\2")
        buf.write("]\u01c4\3\2\2\2_\u01c6\3\2\2\2a\u01c8\3\2\2\2c\u01cb\3")
        buf.write("\2\2\2e\u01ce\3\2\2\2g\u01d1\3\2\2\2i\u01d3\3\2\2\2k\u01d6")
        buf.write("\3\2\2\2m\u01d8\3\2\2\2o\u01db\3\2\2\2q\u01dd\3\2\2\2")
        buf.write("s\u01e0\3\2\2\2u\u01e4\3\2\2\2w\u01e7\3\2\2\2y\u01eb\3")
        buf.write("\2\2\2{\u01ed\3\2\2\2}\u01ef\3\2\2\2\177\u01f1\3\2\2\2")
        buf.write("\u0081\u01f3\3\2\2\2\u0083\u01f5\3\2\2\2\u0085\u01f7\3")
        buf.write("\2\2\2\u0087\u01f9\3\2\2\2\u0089\u01fb\3\2\2\2\u008b\u01fe")
        buf.write("\3\2\2\2\u008d\u0200\3\2\2\2\u008f\u0202\3\2\2\2\u0091")
        buf.write("\u0209\3\2\2\2\u0093\u0212\3\2\2\2\u0095\u022d\3\2\2\2")
        buf.write("\u0097\u0231\3\2\2\2\u0099\u023d\3\2\2\2\u009b\u0247\3")
        buf.write("\2\2\2\u009d\u009e\7u\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3")
        buf.write("\7o\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6\u00a7\7\"\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\u00aa\7z\2\2\u00aa\u00ab\7k\2\2\u00ab\4")
        buf.write("\3\2\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af")
        buf.write("\7k\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7|\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8")
        buf.write("\7k\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7p\2\2\u00ba\6")
        buf.write("\3\2\2\2\u00bb\u00bf\n\2\2\2\u00bc\u00bd\7%\2\2\u00bd")
        buf.write("\u00bf\n\2\2\2\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00bf\b\3\2\2\2\u00c0\u00c9\7\62\2\2\u00c1\u00c5\t\3")
        buf.write("\2\2\u00c2\u00c4\t\4\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c0\3\2\2\2")
        buf.write("\u00c8\u00c1\3\2\2\2\u00c9\n\3\2\2\2\u00ca\u00cc\7\62")
        buf.write("\2\2\u00cb\u00cd\t\5\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\f\3\2\2\2\u00d0\u00d1\7\62\2\2\u00d1\u00d3\t\6\2\2\u00d2")
        buf.write("\u00d4\t\7\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\16\3\2")
        buf.write("\2\2\u00d7\u00d8\7\62\2\2\u00d8\u00da\t\b\2\2\u00d9\u00db")
        buf.write("\t\t\2\2\u00da\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\20\3\2\2\2\u00de")
        buf.write("\u00e2\n\n\2\2\u00df\u00e2\5\23\n\2\u00e0\u00e2\5\25\13")
        buf.write("\2\u00e1\u00de\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e2\22\3\2\2\2\u00e3\u00e4\7^\2\2\u00e4\u00e5")
        buf.write("\t\13\2\2\u00e5\24\3\2\2\2\u00e6\u00e7\7)\2\2\u00e7\u00e8")
        buf.write("\7$\2\2\u00e8\26\3\2\2\2\u00e9\u00ea\7^\2\2\u00ea\u00ef")
        buf.write("\n\13\2\2\u00eb\u00ec\7)\2\2\u00ec\u00ef\n\f\2\2\u00ed")
        buf.write("\u00ef\n\r\2\2\u00ee\u00e9\3\2\2\2\u00ee\u00eb\3\2\2\2")
        buf.write("\u00ee\u00ed\3\2\2\2\u00ef\30\3\2\2\2\u00f0\u00f1\t\16")
        buf.write("\2\2\u00f1\32\3\2\2\2\u00f2\u00f6\t\17\2\2\u00f3\u00f5")
        buf.write("\t\4\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\34\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f9\u00fb\7\60\2\2\u00fa\u00fc\5\33\16")
        buf.write("\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\36\3")
        buf.write("\2\2\2\u00fd\u00ff\t\20\2\2\u00fe\u0100\5\31\r\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u0102\5\33\16\2\u0102 \3\2\2\2\u0103\u0104\7%\2")
        buf.write("\2\u0104\u0105\7%\2\2\u0105\u0109\3\2\2\2\u0106\u0108")
        buf.write("\5\7\4\2\u0107\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109")
        buf.write("\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2")
        buf.write("\u010b\u0109\3\2\2\2\u010c\u010d\7%\2\2\u010d\u010e\7")
        buf.write("%\2\2\u010e\u010f\3\2\2\2\u010f\u0110\b\21\2\2\u0110\"")
        buf.write("\3\2\2\2\u0111\u0112\7D\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\u0115\7c\2\2\u0115\u0116\7m\2\2\u0116$\3")
        buf.write("\2\2\2\u0117\u0118\7E\2\2\u0118\u0119\7q\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011a\u011b\7v\2\2\u011b\u011c\7k\2\2\u011c\u011d")
        buf.write("\7p\2\2\u011d\u011e\7w\2\2\u011e\u011f\7g\2\2\u011f&\3")
        buf.write("\2\2\2\u0120\u0121\7K\2\2\u0121\u0122\7h\2\2\u0122(\3")
        buf.write("\2\2\2\u0123\u0124\7G\2\2\u0124\u0125\7n\2\2\u0125\u0126")
        buf.write("\7u\2\2\u0126\u0127\7g\2\2\u0127\u0128\7k\2\2\u0128\u0129")
        buf.write("\7h\2\2\u0129*\3\2\2\2\u012a\u012b\7G\2\2\u012b\u012c")
        buf.write("\7n\2\2\u012c\u012d\7u\2\2\u012d\u012e\7g\2\2\u012e,\3")
        buf.write("\2\2\2\u012f\u0130\7H\2\2\u0130\u0131\7q\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7e\2\2\u0135\u0136\7j\2\2\u0136.\3\2\2\2\u0137\u0138")
        buf.write("\7V\2\2\u0138\u0139\7t\2\2\u0139\u013a\7w\2\2\u013a\u013b")
        buf.write("\7g\2\2\u013b\60\3\2\2\2\u013c\u013d\7H\2\2\u013d\u013e")
        buf.write("\7c\2\2\u013e\u013f\7n\2\2\u013f\u0140\7u\2\2\u0140\u0141")
        buf.write("\7g\2\2\u0141\62\3\2\2\2\u0142\u0143\7x\2\2\u0143\u0144")
        buf.write("\7c\2\2\u0144\u0145\7t\2\2\u0145\64\3\2\2\2\u0146\u0147")
        buf.write("\7x\2\2\u0147\u0148\7c\2\2\u0148\u0149\7n\2\2\u0149\66")
        buf.write("\3\2\2\2\u014a\u014b\7u\2\2\u014b\u014c\7g\2\2\u014c\u014d")
        buf.write("\7n\2\2\u014d\u014e\7h\2\2\u014e8\3\2\2\2\u014f\u0150")
        buf.write("\7t\2\2\u0150\u0151\7g\2\2\u0151\u0152\7v\2\2\u0152\u0153")
        buf.write("\7w\2\2\u0153\u0154\7t\2\2\u0154\u0155\7p\2\2\u0155:\3")
        buf.write("\2\2\2\u0156\u0157\7e\2\2\u0157\u0158\7q\2\2\u0158\u0159")
        buf.write("\7p\2\2\u0159\u015a\7u\2\2\u015a\u015b\7v\2\2\u015b\u015c")
        buf.write("\7t\2\2\u015c\u015d\7w\2\2\u015d\u015e\7e\2\2\u015e\u015f")
        buf.write("\7v\2\2\u015f\u0160\7q\2\2\u0160\u0161\7t\2\2\u0161<\3")
        buf.write("\2\2\2\u0162\u0163\7f\2\2\u0163\u0164\7g\2\2\u0164\u0165")
        buf.write("\7u\2\2\u0165\u0166\7v\2\2\u0166\u0167\7t\2\2\u0167\u0168")
        buf.write("\7w\2\2\u0168\u0169\7e\2\2\u0169\u016a\7v\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016b\u016c\7t\2\2\u016c>\3\2\2\2\u016d\u016e")
        buf.write("\7e\2\2\u016e\u016f\7n\2\2\u016f\u0170\7c\2\2\u0170\u0171")
        buf.write("\7u\2\2\u0171\u0172\7u\2\2\u0172@\3\2\2\2\u0173\u0174")
        buf.write("\7C\2\2\u0174\u0175\7t\2\2\u0175\u0176\7t\2\2\u0176\u0177")
        buf.write("\7c\2\2\u0177\u0178\7{\2\2\u0178B\3\2\2\2\u0179\u017a")
        buf.write("\7K\2\2\u017a\u017b\7p\2\2\u017b\u017c\7v\2\2\u017cD\3")
        buf.write("\2\2\2\u017d\u017e\7H\2\2\u017e\u017f\7n\2\2\u017f\u0180")
        buf.write("\7q\2\2\u0180\u0181\7c\2\2\u0181\u0182\7v\2\2\u0182F\3")
        buf.write("\2\2\2\u0183\u0184\7D\2\2\u0184\u0185\7q\2\2\u0185\u0186")
        buf.write("\7q\2\2\u0186\u0187\7n\2\2\u0187\u0188\7g\2\2\u0188\u0189")
        buf.write("\7c\2\2\u0189\u018a\7p\2\2\u018aH\3\2\2\2\u018b\u018c")
        buf.write("\7U\2\2\u018c\u018d\7v\2\2\u018d\u018e\7t\2\2\u018e\u018f")
        buf.write("\7k\2\2\u018f\u0190\7p\2\2\u0190\u0191\7i\2\2\u0191J\3")
        buf.write("\2\2\2\u0192\u0193\7P\2\2\u0193\u0194\7w\2\2\u0194\u0195")
        buf.write("\7n\2\2\u0195\u0196\7n\2\2\u0196L\3\2\2\2\u0197\u019c")
        buf.write("\5\t\5\2\u0198\u019c\5\13\6\2\u0199\u019c\5\17\b\2\u019a")
        buf.write("\u019c\5\r\7\2\u019b\u0197\3\2\2\2\u019b\u0198\3\2\2\2")
        buf.write("\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3")
        buf.write("\2\2\2\u019d\u019e\b\'\3\2\u019eN\3\2\2\2\u019f\u01a3")
        buf.write("\7$\2\2\u01a0\u01a2\5\21\t\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\7")
        buf.write("$\2\2\u01a7\u01a8\b(\4\2\u01a8P\3\2\2\2\u01a9\u01ac\5")
        buf.write("/\30\2\u01aa\u01ac\5\61\31\2\u01ab\u01a9\3\2\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01acR\3\2\2\2\u01ad\u01ae\5\33\16\2\u01ae")
        buf.write("\u01b0\5\35\17\2\u01af\u01b1\5\37\20\2\u01b0\u01af\3\2")
        buf.write("\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b9\3\2\2\2\u01b2\u01b3")
        buf.write("\5\33\16\2\u01b3\u01b4\5\37\20\2\u01b4\u01b9\3\2\2\2\u01b5")
        buf.write("\u01b6\5\35\17\2\u01b6\u01b7\5\37\20\2\u01b7\u01b9\3\2")
        buf.write("\2\2\u01b8\u01ad\3\2\2\2\u01b8\u01b2\3\2\2\2\u01b8\u01b5")
        buf.write("\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\b*\5\2\u01bb")
        buf.write("T\3\2\2\2\u01bc\u01bd\7-\2\2\u01bdV\3\2\2\2\u01be\u01bf")
        buf.write("\7/\2\2\u01bfX\3\2\2\2\u01c0\u01c1\7,\2\2\u01c1Z\3\2\2")
        buf.write("\2\u01c2\u01c3\7\61\2\2\u01c3\\\3\2\2\2\u01c4\u01c5\7")
        buf.write("\'\2\2\u01c5^\3\2\2\2\u01c6\u01c7\7#\2\2\u01c7`\3\2\2")
        buf.write("\2\u01c8\u01c9\7(\2\2\u01c9\u01ca\7(\2\2\u01cab\3\2\2")
        buf.write("\2\u01cb\u01cc\7~\2\2\u01cc\u01cd\7~\2\2\u01cdd\3\2\2")
        buf.write("\2\u01ce\u01cf\7?\2\2\u01cf\u01d0\7?\2\2\u01d0f\3\2\2")
        buf.write("\2\u01d1\u01d2\7?\2\2\u01d2h\3\2\2\2\u01d3\u01d4\7#\2")
        buf.write("\2\u01d4\u01d5\7?\2\2\u01d5j\3\2\2\2\u01d6\u01d7\7>\2")
        buf.write("\2\u01d7l\3\2\2\2\u01d8\u01d9\7>\2\2\u01d9\u01da\7?\2")
        buf.write("\2\u01dan\3\2\2\2\u01db\u01dc\7@\2\2\u01dcp\3\2\2\2\u01dd")
        buf.write("\u01de\7@\2\2\u01de\u01df\7?\2\2\u01dfr\3\2\2\2\u01e0")
        buf.write("\u01e1\7?\2\2\u01e1\u01e2\7?\2\2\u01e2\u01e3\7\60\2\2")
        buf.write("\u01e3t\3\2\2\2\u01e4\u01e5\7-\2\2\u01e5\u01e6\7\60\2")
        buf.write("\2\u01e6v\3\2\2\2\u01e7\u01e8\7p\2\2\u01e8\u01e9\7g\2")
        buf.write("\2\u01e9\u01ea\7y\2\2\u01eax\3\2\2\2\u01eb\u01ec\7*\2")
        buf.write("\2\u01ecz\3\2\2\2\u01ed\u01ee\7+\2\2\u01ee|\3\2\2\2\u01ef")
        buf.write("\u01f0\7]\2\2\u01f0~\3\2\2\2\u01f1\u01f2\7_\2\2\u01f2")
        buf.write("\u0080\3\2\2\2\u01f3\u01f4\7\60\2\2\u01f4\u0082\3\2\2")
        buf.write("\2\u01f5\u01f6\7.\2\2\u01f6\u0084\3\2\2\2\u01f7\u01f8")
        buf.write("\7=\2\2\u01f8\u0086\3\2\2\2\u01f9\u01fa\7<\2\2\u01fa\u0088")
        buf.write("\3\2\2\2\u01fb\u01fc\7<\2\2\u01fc\u01fd\7<\2\2\u01fd\u008a")
        buf.write("\3\2\2\2\u01fe\u01ff\7}\2\2\u01ff\u008c\3\2\2\2\u0200")
        buf.write("\u0201\7\177\2\2\u0201\u008e\3\2\2\2\u0202\u0206\t\21")
        buf.write("\2\2\u0203\u0205\t\22\2\2\u0204\u0203\3\2\2\2\u0205\u0208")
        buf.write("\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u0090\3\2\2\2\u0208\u0206\3\2\2\2\u0209\u020a\7&\2\2")
        buf.write("\u020a\u020e\t\21\2\2\u020b\u020d\t\22\2\2\u020c\u020b")
        buf.write("\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e")
        buf.write("\u020f\3\2\2\2\u020f\u0092\3\2\2\2\u0210\u020e\3\2\2\2")
        buf.write("\u0211\u0213\t\23\2\2\u0212\u0211\3\2\2\2\u0213\u0214")
        buf.write("\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0217\bJ\2\2\u0217\u0094\3\2\2\2")
        buf.write("\u0218\u0219\7%\2\2\u0219\u021a\7%\2\2\u021a\u021e\3\2")
        buf.write("\2\2\u021b\u021d\5\7\4\2\u021c\u021b\3\2\2\2\u021d\u0220")
        buf.write("\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write("\u0221\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u022e\7\2\2\3")
        buf.write("\u0222\u0223\7%\2\2\u0223\u0224\7%\2\2\u0224\u0228\3\2")
        buf.write("\2\2\u0225\u0227\n\2\2\2\u0226\u0225\3\2\2\2\u0227\u022a")
        buf.write("\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("\u022b\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u022c\7%\2\2")
        buf.write("\u022c\u022e\7\2\2\3\u022d\u0218\3\2\2\2\u022d\u0222\3")
        buf.write("\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\bK\6\2\u0230\u0096")
        buf.write("\3\2\2\2\u0231\u0235\7$\2\2\u0232\u0234\5\21\t\2\u0233")
        buf.write("\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2")
        buf.write("\u0235\u0236\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0238\u023a\t\24\2\2\u0239\u0238\3\2\2\2\u023a")
        buf.write("\u023b\3\2\2\2\u023b\u023c\bL\7\2\u023c\u0098\3\2\2\2")
        buf.write("\u023d\u0241\7$\2\2\u023e\u0240\5\21\t\2\u023f\u023e\3")
        buf.write("\2\2\2\u0240\u0243\3\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242")
        buf.write("\3\2\2\2\u0242\u0244\3\2\2\2\u0243\u0241\3\2\2\2\u0244")
        buf.write("\u0245\5\27\f\2\u0245\u0246\bM\b\2\u0246\u009a\3\2\2\2")
        buf.write("\u0247\u0248\13\2\2\2\u0248\u0249\bN\t\2\u0249\u009c\3")
        buf.write("\2\2\2\35\2\u00be\u00c5\u00c8\u00ce\u00d5\u00dc\u00e1")
        buf.write("\u00ee\u00f6\u00fb\u00ff\u0109\u019b\u01a3\u01ab\u01b0")
        buf.write("\u01b8\u0206\u020e\u0214\u021e\u0228\u022d\u0235\u0239")
        buf.write("\u0241\n\b\2\2\3\'\2\3(\3\3*\4\3K\5\3L\6\3M\7\3N\b")
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
    CONSTRUCTOR = 14
    DESTRUCTOR = 15
    CLASS = 16
    ARRAY = 17
    INT = 18
    FLOAT = 19
    BOOLEAN = 20
    STRING = 21
    NULL = 22
    INTEGER_LITERAL = 23
    STRING_LITERAL = 24
    BOOLEAN_LITERAL = 25
    FLOAT_LITERAL = 26
    ADD = 27
    SUB = 28
    MUL = 29
    DIV = 30
    MOD = 31
    NOT = 32
    AND = 33
    OR = 34
    EQUAL = 35
    ASSIGN = 36
    NOT_EQUAL = 37
    LT = 38
    LTE = 39
    GT = 40
    GTE = 41
    STRING_EQUAL = 42
    STRING_ADD = 43
    NEW = 44
    LP = 45
    RP = 46
    LSB = 47
    RSB = 48
    DOT = 49
    COMMA = 50
    SEMI = 51
    COLON = 52
    DOUBLE_COLON = 53
    LCB = 54
    RCB = 55
    ID = 56
    DOLLAR_ID = 57
    WS = 58
    UNTERMINATED_COMMENT = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_TOKEN = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'statement lexi'", "'initialization'", "'Break'", "'Continue'", 
            "'If'", "'Elseif'", "'Else'", "'Foreach'", "'var'", "'val'", 
            "'self'", "'return'", "'constructor'", "'destructor'", "'class'", 
            "'Array'", "'Int'", "'Float'", "'Boolean'", "'String'", "'Null'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", "'+.'", 
            "'new'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
            "'::'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "VAR", "VAL", "SELF", "RETURN", "CONSTRUCTOR", "DESTRUCTOR", 
            "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", "STRING", "NULL", 
            "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", "FLOAT_LITERAL", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", "STRING_EQUAL", 
            "STRING_ADD", "NEW", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", 
            "SEMI", "COLON", "DOUBLE_COLON", "LCB", "RCB", "ID", "DOLLAR_ID", 
            "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "T__1", "COMMENT_CHAR", "DEC_INTEGER_LITERAL", 
                  "OCT_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", "HEX_INTEGER_LITERAL", 
                  "STRING_CHAR", "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_CHAR", 
                  "ILLEGAL_SEQUENCE", "SIGN", "FLOAT_INTEGER_PART", "FLOAT_DECIMAL_PART", 
                  "FLOAT_EXPONENT_PART", "COMMENT", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "VAR", 
                  "VAL", "SELF", "RETURN", "CONSTRUCTOR", "DESTRUCTOR", 
                  "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", "STRING", 
                  "NULL", "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                  "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", 
                  "GT", "GTE", "STRING_EQUAL", "STRING_ADD", "NEW", "LP", 
                  "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "DOUBLE_COLON", 
                  "LCB", "RCB", "ID", "DOLLAR_ID", "WS", "UNTERMINATED_COMMENT", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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
            actions[73] = self.UNTERMINATED_COMMENT_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.ERROR_TOKEN_action 
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

                y = str(self.text)
                possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
                if y[-1] in possible:
                    raise UncloseString(y[1:-1])
                else:
                    raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                raise ErrorToken(self.text)

     


