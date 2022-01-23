# Generated from d:\Workspace\PPL\Assignment\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u023e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\5\2\u00a0\n\2\3\2\7\2\u00a3\n\2")
        buf.write("\f\2\16\2\u00a6\13\2\3\3\3\3\3\3\5\3\u00ab\n\3\3\3\7\3")
        buf.write("\u00ae\n\3\f\3\16\3\u00b1\13\3\3\4\3\4\3\4\3\4\5\4\u00b7")
        buf.write("\n\4\3\4\7\4\u00ba\n\4\f\4\16\4\u00bd\13\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5\u00c3\n\5\3\5\7\5\u00c6\n\5\f\5\16\5\u00c9\13")
        buf.write("\5\3\6\3\6\3\6\5\6\u00ce\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\t\u00db\n\t\3\n\3\n\3\13\3\13\5\13")
        buf.write("\u00e1\n\13\3\13\7\13\u00e4\n\13\f\13\16\13\u00e7\13\13")
        buf.write("\3\13\5\13\u00ea\n\13\3\f\3\f\7\f\u00ee\n\f\f\f\16\f\u00f1")
        buf.write("\13\f\3\r\3\r\5\r\u00f5\n\r\3\r\6\r\u00f8\n\r\r\r\16\r")
        buf.write("\u00f9\3\16\3\16\3\16\3\16\7\16\u0100\n\16\f\16\16\16")
        buf.write("\u0103\13\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01a9\n\'\3(\3(\3")
        buf.write("(\3(\5(\u01af\n(\3(\3(\3)\3)\7)\u01b5\n)\f)\16)\u01b8")
        buf.write("\13)\3)\3)\3)\3*\3*\5*\u01bf\n*\3+\3+\3+\5+\u01c4\n+\3")
        buf.write("+\3+\3+\3+\3+\3+\5+\u01cc\n+\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38")
        buf.write("\38\38\39\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3=\3=\3>\3")
        buf.write(">\3?\3?\3@\3@\3A\3A\3B\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("F\3G\3G\3H\3H\3I\3I\7I\u0217\nI\fI\16I\u021a\13I\3J\3")
        buf.write("J\6J\u021e\nJ\rJ\16J\u021f\3K\6K\u0223\nK\rK\16K\u0224")
        buf.write("\3K\3K\3L\3L\7L\u022b\nL\fL\16L\u022e\13L\3L\3L\3M\3M")
        buf.write("\7M\u0234\nM\fM\16M\u0237\13M\3M\3M\3M\3N\3N\3N\3\u0101")
        buf.write("\2O\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\3\35\4\37\5!\6#\7%\b\'\t)\2+\2-\n/\13\61\f\63")
        buf.write("\r\65\16\67\179\20;\21=\22?\23A\24C\25E\26G\27I\30K\31")
        buf.write("M\32O\33Q\34S\35U\36W\37Y [!]\"_#a$c%e&g\'i(k)m*o+q,s")
        buf.write("-u.w/y\60{\61}\62\177\63\u0081\64\u0083\65\u0085\66\u0087")
        buf.write("\67\u00898\u008b9\u008d:\u008f;\u0091<\u0093=\u0095>\u0097")
        buf.write("?\u0099@\u009bA\3\2\24\3\2\63;\3\2\62;\3\2\639\3\2\62")
        buf.write("9\4\2DDdd\3\2\63\63\3\2\62\63\4\2ZZzz\4\2\63;CH\4\2\62")
        buf.write(";CH\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\3\2$$\4\2--//")
        buf.write("\4\2GGgg\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"")
        buf.write("\2\u0254\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2-\3\2\2\2\2/\3")
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
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\3\u009d\3\2\2\2\5\u00a7")
        buf.write("\3\2\2\2\7\u00b2\3\2\2\2\t\u00be\3\2\2\2\13\u00cd\3\2")
        buf.write("\2\2\r\u00cf\3\2\2\2\17\u00d2\3\2\2\2\21\u00da\3\2\2\2")
        buf.write("\23\u00dc\3\2\2\2\25\u00e9\3\2\2\2\27\u00eb\3\2\2\2\31")
        buf.write("\u00f2\3\2\2\2\33\u00fb\3\2\2\2\35\u0109\3\2\2\2\37\u010f")
        buf.write("\3\2\2\2!\u0118\3\2\2\2#\u011b\3\2\2\2%\u0122\3\2\2\2")
        buf.write("\'\u0127\3\2\2\2)\u012f\3\2\2\2+\u0134\3\2\2\2-\u013a")
        buf.write("\3\2\2\2/\u013e\3\2\2\2\61\u0142\3\2\2\2\63\u0147\3\2")
        buf.write("\2\2\65\u014e\3\2\2\2\67\u0151\3\2\2\29\u0154\3\2\2\2")
        buf.write(";\u0158\3\2\2\2=\u0164\3\2\2\2?\u016f\3\2\2\2A\u0174\3")
        buf.write("\2\2\2C\u017a\3\2\2\2E\u0180\3\2\2\2G\u0184\3\2\2\2I\u018a")
        buf.write("\3\2\2\2K\u0192\3\2\2\2M\u01a8\3\2\2\2O\u01ae\3\2\2\2")
        buf.write("Q\u01b2\3\2\2\2S\u01be\3\2\2\2U\u01cb\3\2\2\2W\u01cf\3")
        buf.write("\2\2\2Y\u01d1\3\2\2\2[\u01d3\3\2\2\2]\u01d5\3\2\2\2_\u01d7")
        buf.write("\3\2\2\2a\u01d9\3\2\2\2c\u01db\3\2\2\2e\u01de\3\2\2\2")
        buf.write("g\u01e1\3\2\2\2i\u01e4\3\2\2\2k\u01e6\3\2\2\2m\u01e9\3")
        buf.write("\2\2\2o\u01eb\3\2\2\2q\u01ee\3\2\2\2s\u01f0\3\2\2\2u\u01f3")
        buf.write("\3\2\2\2w\u01f7\3\2\2\2y\u01fa\3\2\2\2{\u01fc\3\2\2\2")
        buf.write("}\u01fe\3\2\2\2\177\u0200\3\2\2\2\u0081\u0202\3\2\2\2")
        buf.write("\u0083\u0204\3\2\2\2\u0085\u0207\3\2\2\2\u0087\u0209\3")
        buf.write("\2\2\2\u0089\u020b\3\2\2\2\u008b\u020d\3\2\2\2\u008d\u0210")
        buf.write("\3\2\2\2\u008f\u0212\3\2\2\2\u0091\u0214\3\2\2\2\u0093")
        buf.write("\u021b\3\2\2\2\u0095\u0222\3\2\2\2\u0097\u0228\3\2\2\2")
        buf.write("\u0099\u0231\3\2\2\2\u009b\u023b\3\2\2\2\u009d\u00a4\t")
        buf.write("\2\2\2\u009e\u00a0\7a\2\2\u009f\u009e\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\t\3\2\2\u00a2")
        buf.write("\u009f\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\4\3\2\2\2\u00a6\u00a4\3\2\2")
        buf.write("\2\u00a7\u00a8\7\62\2\2\u00a8\u00af\t\4\2\2\u00a9\u00ab")
        buf.write("\7a\2\2\u00aa\u00a9\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00ae\t\5\2\2\u00ad\u00aa\3\2\2\2")
        buf.write("\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3")
        buf.write("\2\2\2\u00b0\6\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b3")
        buf.write("\7\62\2\2\u00b3\u00b4\t\6\2\2\u00b4\u00bb\t\7\2\2\u00b5")
        buf.write("\u00b7\7a\2\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00b8\3\2\2\2\u00b8\u00ba\t\b\2\2\u00b9\u00b6\3")
        buf.write("\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc")
        buf.write("\3\2\2\2\u00bc\b\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf")
        buf.write("\7\62\2\2\u00bf\u00c0\t\t\2\2\u00c0\u00c7\t\n\2\2\u00c1")
        buf.write("\u00c3\7a\2\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\u00c6\t\13\2\2\u00c5\u00c2")
        buf.write("\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c8\3\2\2\2\u00c8\n\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00ce\n\f\2\2\u00cb\u00ce\5\r\7\2\u00cc\u00ce\5\17\b")
        buf.write("\2\u00cd\u00ca\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\f\3\2\2\2\u00cf\u00d0\7^\2\2\u00d0\u00d1")
        buf.write("\t\r\2\2\u00d1\16\3\2\2\2\u00d2\u00d3\7)\2\2\u00d3\u00d4")
        buf.write("\7$\2\2\u00d4\20\3\2\2\2\u00d5\u00d6\7^\2\2\u00d6\u00db")
        buf.write("\n\r\2\2\u00d7\u00d8\7)\2\2\u00d8\u00db\n\16\2\2\u00d9")
        buf.write("\u00db\7^\2\2\u00da\u00d5\3\2\2\2\u00da\u00d7\3\2\2\2")
        buf.write("\u00da\u00d9\3\2\2\2\u00db\22\3\2\2\2\u00dc\u00dd\t\17")
        buf.write("\2\2\u00dd\24\3\2\2\2\u00de\u00e5\t\2\2\2\u00df\u00e1")
        buf.write("\7a\2\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e4\t\3\2\2\u00e3\u00e0\3\2\2\2")
        buf.write("\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3")
        buf.write("\2\2\2\u00e6\u00ea\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00ea")
        buf.write("\7\62\2\2\u00e9\u00de\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea")
        buf.write("\26\3\2\2\2\u00eb\u00ef\7\60\2\2\u00ec\u00ee\t\3\2\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00ef\u00f0\3\2\2\2\u00f0\30\3\2\2\2\u00f1\u00ef\3\2")
        buf.write("\2\2\u00f2\u00f4\t\20\2\2\u00f3\u00f5\5\23\n\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f8\t\3\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\32\3\2")
        buf.write("\2\2\u00fb\u00fc\7%\2\2\u00fc\u00fd\7%\2\2\u00fd\u0101")
        buf.write("\3\2\2\2\u00fe\u0100\13\2\2\2\u00ff\u00fe\3\2\2\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u0102\3\2\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\7")
        buf.write("%\2\2\u0105\u0106\7%\2\2\u0106\u0107\3\2\2\2\u0107\u0108")
        buf.write("\b\16\2\2\u0108\34\3\2\2\2\u0109\u010a\7D\2\2\u010a\u010b")
        buf.write("\7t\2\2\u010b\u010c\7g\2\2\u010c\u010d\7c\2\2\u010d\u010e")
        buf.write("\7m\2\2\u010e\36\3\2\2\2\u010f\u0110\7E\2\2\u0110\u0111")
        buf.write("\7q\2\2\u0111\u0112\7p\2\2\u0112\u0113\7v\2\2\u0113\u0114")
        buf.write("\7k\2\2\u0114\u0115\7p\2\2\u0115\u0116\7w\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117 \3\2\2\2\u0118\u0119\7K\2\2\u0119\u011a")
        buf.write("\7h\2\2\u011a\"\3\2\2\2\u011b\u011c\7G\2\2\u011c\u011d")
        buf.write("\7n\2\2\u011d\u011e\7u\2\2\u011e\u011f\7g\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7h\2\2\u0121$\3\2\2\2\u0122\u0123")
        buf.write("\7G\2\2\u0123\u0124\7n\2\2\u0124\u0125\7u\2\2\u0125\u0126")
        buf.write("\7g\2\2\u0126&\3\2\2\2\u0127\u0128\7H\2\2\u0128\u0129")
        buf.write("\7q\2\2\u0129\u012a\7t\2\2\u012a\u012b\7g\2\2\u012b\u012c")
        buf.write("\7c\2\2\u012c\u012d\7e\2\2\u012d\u012e\7j\2\2\u012e(\3")
        buf.write("\2\2\2\u012f\u0130\7V\2\2\u0130\u0131\7t\2\2\u0131\u0132")
        buf.write("\7w\2\2\u0132\u0133\7g\2\2\u0133*\3\2\2\2\u0134\u0135")
        buf.write("\7H\2\2\u0135\u0136\7c\2\2\u0136\u0137\7n\2\2\u0137\u0138")
        buf.write("\7u\2\2\u0138\u0139\7g\2\2\u0139,\3\2\2\2\u013a\u013b")
        buf.write("\7X\2\2\u013b\u013c\7c\2\2\u013c\u013d\7t\2\2\u013d.\3")
        buf.write("\2\2\2\u013e\u013f\7X\2\2\u013f\u0140\7c\2\2\u0140\u0141")
        buf.write("\7n\2\2\u0141\60\3\2\2\2\u0142\u0143\7U\2\2\u0143\u0144")
        buf.write("\7g\2\2\u0144\u0145\7n\2\2\u0145\u0146\7h\2\2\u0146\62")
        buf.write("\3\2\2\2\u0147\u0148\7T\2\2\u0148\u0149\7g\2\2\u0149\u014a")
        buf.write("\7v\2\2\u014a\u014b\7w\2\2\u014b\u014c\7t\2\2\u014c\u014d")
        buf.write("\7p\2\2\u014d\64\3\2\2\2\u014e\u014f\7K\2\2\u014f\u0150")
        buf.write("\7p\2\2\u0150\66\3\2\2\2\u0151\u0152\7D\2\2\u0152\u0153")
        buf.write("\7{\2\2\u01538\3\2\2\2\u0154\u0155\7P\2\2\u0155\u0156")
        buf.write("\7g\2\2\u0156\u0157\7y\2\2\u0157:\3\2\2\2\u0158\u0159")
        buf.write("\7E\2\2\u0159\u015a\7q\2\2\u015a\u015b\7p\2\2\u015b\u015c")
        buf.write("\7u\2\2\u015c\u015d\7v\2\2\u015d\u015e\7t\2\2\u015e\u015f")
        buf.write("\7w\2\2\u015f\u0160\7e\2\2\u0160\u0161\7v\2\2\u0161\u0162")
        buf.write("\7q\2\2\u0162\u0163\7t\2\2\u0163<\3\2\2\2\u0164\u0165")
        buf.write("\7F\2\2\u0165\u0166\7g\2\2\u0166\u0167\7u\2\2\u0167\u0168")
        buf.write("\7v\2\2\u0168\u0169\7t\2\2\u0169\u016a\7w\2\2\u016a\u016b")
        buf.write("\7e\2\2\u016b\u016c\7v\2\2\u016c\u016d\7q\2\2\u016d\u016e")
        buf.write("\7t\2\2\u016e>\3\2\2\2\u016f\u0170\7P\2\2\u0170\u0171")
        buf.write("\7w\2\2\u0171\u0172\7n\2\2\u0172\u0173\7n\2\2\u0173@\3")
        buf.write("\2\2\2\u0174\u0175\7E\2\2\u0175\u0176\7n\2\2\u0176\u0177")
        buf.write("\7c\2\2\u0177\u0178\7u\2\2\u0178\u0179\7u\2\2\u0179B\3")
        buf.write("\2\2\2\u017a\u017b\7C\2\2\u017b\u017c\7t\2\2\u017c\u017d")
        buf.write("\7t\2\2\u017d\u017e\7c\2\2\u017e\u017f\7{\2\2\u017fD\3")
        buf.write("\2\2\2\u0180\u0181\7K\2\2\u0181\u0182\7p\2\2\u0182\u0183")
        buf.write("\7v\2\2\u0183F\3\2\2\2\u0184\u0185\7H\2\2\u0185\u0186")
        buf.write("\7n\2\2\u0186\u0187\7q\2\2\u0187\u0188\7c\2\2\u0188\u0189")
        buf.write("\7v\2\2\u0189H\3\2\2\2\u018a\u018b\7D\2\2\u018b\u018c")
        buf.write("\7q\2\2\u018c\u018d\7q\2\2\u018d\u018e\7n\2\2\u018e\u018f")
        buf.write("\7g\2\2\u018f\u0190\7c\2\2\u0190\u0191\7p\2\2\u0191J\3")
        buf.write("\2\2\2\u0192\u0193\7U\2\2\u0193\u0194\7v\2\2\u0194\u0195")
        buf.write("\7t\2\2\u0195\u0196\7k\2\2\u0196\u0197\7p\2\2\u0197\u0198")
        buf.write("\7i\2\2\u0198L\3\2\2\2\u0199\u01a9\7\62\2\2\u019a\u019b")
        buf.write("\7\62\2\2\u019b\u01a9\7\62\2\2\u019c\u019d\7\62\2\2\u019d")
        buf.write("\u019e\7d\2\2\u019e\u01a9\7\62\2\2\u019f\u01a0\7\62\2")
        buf.write("\2\u01a0\u01a1\7D\2\2\u01a1\u01a9\7\62\2\2\u01a2\u01a3")
        buf.write("\7\62\2\2\u01a3\u01a4\7z\2\2\u01a4\u01a9\7\62\2\2\u01a5")
        buf.write("\u01a6\7\62\2\2\u01a6\u01a7\7Z\2\2\u01a7\u01a9\7\62\2")
        buf.write("\2\u01a8\u0199\3\2\2\2\u01a8\u019a\3\2\2\2\u01a8\u019c")
        buf.write("\3\2\2\2\u01a8\u019f\3\2\2\2\u01a8\u01a2\3\2\2\2\u01a8")
        buf.write("\u01a5\3\2\2\2\u01a9N\3\2\2\2\u01aa\u01af\5\3\2\2\u01ab")
        buf.write("\u01af\5\5\3\2\u01ac\u01af\5\t\5\2\u01ad\u01af\5\7\4\2")
        buf.write("\u01ae\u01aa\3\2\2\2\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1")
        buf.write("\b(\3\2\u01b1P\3\2\2\2\u01b2\u01b6\7$\2\2\u01b3\u01b5")
        buf.write("\5\13\6\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b9\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7$\2\2\u01ba\u01bb\b")
        buf.write(")\4\2\u01bbR\3\2\2\2\u01bc\u01bf\5)\25\2\u01bd\u01bf\5")
        buf.write("+\26\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfT")
        buf.write("\3\2\2\2\u01c0\u01c1\5\25\13\2\u01c1\u01c3\5\27\f\2\u01c2")
        buf.write("\u01c4\5\31\r\2\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3\2\2")
        buf.write("\2\u01c4\u01cc\3\2\2\2\u01c5\u01c6\5\25\13\2\u01c6\u01c7")
        buf.write("\5\31\r\2\u01c7\u01cc\3\2\2\2\u01c8\u01c9\5\27\f\2\u01c9")
        buf.write("\u01ca\5\31\r\2\u01ca\u01cc\3\2\2\2\u01cb\u01c0\3\2\2")
        buf.write("\2\u01cb\u01c5\3\2\2\2\u01cb\u01c8\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u01ce\b+\5\2\u01ceV\3\2\2\2\u01cf\u01d0")
        buf.write("\7-\2\2\u01d0X\3\2\2\2\u01d1\u01d2\7/\2\2\u01d2Z\3\2\2")
        buf.write("\2\u01d3\u01d4\7,\2\2\u01d4\\\3\2\2\2\u01d5\u01d6\7\61")
        buf.write("\2\2\u01d6^\3\2\2\2\u01d7\u01d8\7\'\2\2\u01d8`\3\2\2\2")
        buf.write("\u01d9\u01da\7#\2\2\u01dab\3\2\2\2\u01db\u01dc\7(\2\2")
        buf.write("\u01dc\u01dd\7(\2\2\u01ddd\3\2\2\2\u01de\u01df\7~\2\2")
        buf.write("\u01df\u01e0\7~\2\2\u01e0f\3\2\2\2\u01e1\u01e2\7?\2\2")
        buf.write("\u01e2\u01e3\7?\2\2\u01e3h\3\2\2\2\u01e4\u01e5\7?\2\2")
        buf.write("\u01e5j\3\2\2\2\u01e6\u01e7\7#\2\2\u01e7\u01e8\7?\2\2")
        buf.write("\u01e8l\3\2\2\2\u01e9\u01ea\7>\2\2\u01ean\3\2\2\2\u01eb")
        buf.write("\u01ec\7>\2\2\u01ec\u01ed\7?\2\2\u01edp\3\2\2\2\u01ee")
        buf.write("\u01ef\7@\2\2\u01efr\3\2\2\2\u01f0\u01f1\7@\2\2\u01f1")
        buf.write("\u01f2\7?\2\2\u01f2t\3\2\2\2\u01f3\u01f4\7?\2\2\u01f4")
        buf.write("\u01f5\7?\2\2\u01f5\u01f6\7\60\2\2\u01f6v\3\2\2\2\u01f7")
        buf.write("\u01f8\7-\2\2\u01f8\u01f9\7\60\2\2\u01f9x\3\2\2\2\u01fa")
        buf.write("\u01fb\7*\2\2\u01fbz\3\2\2\2\u01fc\u01fd\7+\2\2\u01fd")
        buf.write("|\3\2\2\2\u01fe\u01ff\7]\2\2\u01ff~\3\2\2\2\u0200\u0201")
        buf.write("\7_\2\2\u0201\u0080\3\2\2\2\u0202\u0203\7\60\2\2\u0203")
        buf.write("\u0082\3\2\2\2\u0204\u0205\7\60\2\2\u0205\u0206\7\60\2")
        buf.write("\2\u0206\u0084\3\2\2\2\u0207\u0208\7.\2\2\u0208\u0086")
        buf.write("\3\2\2\2\u0209\u020a\7=\2\2\u020a\u0088\3\2\2\2\u020b")
        buf.write("\u020c\7<\2\2\u020c\u008a\3\2\2\2\u020d\u020e\7<\2\2\u020e")
        buf.write("\u020f\7<\2\2\u020f\u008c\3\2\2\2\u0210\u0211\7}\2\2\u0211")
        buf.write("\u008e\3\2\2\2\u0212\u0213\7\177\2\2\u0213\u0090\3\2\2")
        buf.write("\2\u0214\u0218\t\21\2\2\u0215\u0217\t\22\2\2\u0216\u0215")
        buf.write("\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u0092\3\2\2\2\u021a\u0218\3\2\2\2")
        buf.write("\u021b\u021d\7&\2\2\u021c\u021e\t\22\2\2\u021d\u021c\3")
        buf.write("\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220")
        buf.write("\3\2\2\2\u0220\u0094\3\2\2\2\u0221\u0223\t\23\2\2\u0222")
        buf.write("\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0224\u0225\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\b")
        buf.write("K\2\2\u0227\u0096\3\2\2\2\u0228\u022c\7$\2\2\u0229\u022b")
        buf.write("\5\13\6\2\u022a\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c")
        buf.write("\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\3\2\2\2")
        buf.write("\u022e\u022c\3\2\2\2\u022f\u0230\bL\6\2\u0230\u0098\3")
        buf.write("\2\2\2\u0231\u0235\7$\2\2\u0232\u0234\5\13\6\2\u0233\u0232")
        buf.write("\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235")
        buf.write("\u0236\3\2\2\2\u0236\u0238\3\2\2\2\u0237\u0235\3\2\2\2")
        buf.write("\u0238\u0239\5\21\t\2\u0239\u023a\bM\7\2\u023a\u009a\3")
        buf.write("\2\2\2\u023b\u023c\13\2\2\2\u023c\u023d\bN\b\2\u023d\u009c")
        buf.write("\3\2\2\2\37\2\u009f\u00a4\u00aa\u00af\u00b6\u00bb\u00c2")
        buf.write("\u00c7\u00cd\u00da\u00e0\u00e5\u00e9\u00ef\u00f4\u00f9")
        buf.write("\u0101\u01a8\u01ae\u01b6\u01be\u01c3\u01cb\u0218\u021f")
        buf.write("\u0224\u022c\u0235\t\b\2\2\3(\2\3)\3\3+\4\3L\5\3M\6\3")
        buf.write("N\7")
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
    ZERO_INTEGER = 24
    INTEGER_LITERAL = 25
    STRING_LITERAL = 26
    BOOLEAN_LITERAL = 27
    FLOAT_LITERAL = 28
    ADD = 29
    SUB = 30
    MUL = 31
    DIV = 32
    MOD = 33
    NOT = 34
    AND = 35
    OR = 36
    EQUAL = 37
    ASSIGN = 38
    NOT_EQUAL = 39
    LT = 40
    LTE = 41
    GT = 42
    GTE = 43
    STRING_EQUAL = 44
    STRING_ADD = 45
    LP = 46
    RP = 47
    LSB = 48
    RSB = 49
    DOT = 50
    DOUBLE_DOT = 51
    COMMA = 52
    SEMI = 53
    COLON = 54
    DOUBLE_COLON = 55
    LCB = 56
    RCB = 57
    ID = 58
    DOLLAR_ID = 59
    WS = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_TOKEN = 63

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
            "BOOLEAN", "STRING", "ZERO_INTEGER", "INTEGER_LITERAL", "STRING_LITERAL", 
            "BOOLEAN_LITERAL", "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", 
            "LTE", "GT", "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", 
            "LSB", "RSB", "DOT", "DOUBLE_DOT", "COMMA", "SEMI", "COLON", 
            "DOUBLE_COLON", "LCB", "RCB", "ID", "DOLLAR_ID", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", 
                  "HEX_INTEGER_LITERAL", "STRING_CHAR", "ESCAPE_SEQUENCE", 
                  "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", "SIGN", "FLOAT_INTEGER_PART", 
                  "FLOAT_DECIMAL_PART", "FLOAT_EXPONENT_PART", "COMMENT", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "VAR", "VAL", "SELF", "RETURN", "IN", 
                  "BY", "NEW", "CONSTRUCTOR", "DESTRUCTOR", "NULL", "CLASS", 
                  "ARRAY", "INTEGER", "FLOAT", "BOOLEAN", "STRING", "ZERO_INTEGER", 
                  "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                  "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", 
                  "GT", "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", 
                  "LSB", "RSB", "DOT", "DOUBLE_DOT", "COMMA", "SEMI", "COLON", 
                  "DOUBLE_COLON", "LCB", "RCB", "ID", "DOLLAR_ID", "WS", 
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
            actions[38] = self.INTEGER_LITERAL_action 
            actions[39] = self.STRING_LITERAL_action 
            actions[41] = self.FLOAT_LITERAL_action 
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

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise UncloseString(self.text[1:]);

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise ErrorToken(self.text)

     


