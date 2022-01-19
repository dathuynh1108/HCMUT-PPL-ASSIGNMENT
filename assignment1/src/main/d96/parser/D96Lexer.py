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
        buf.write("L\4M\tM\3\2\3\2\5\2\u009e\n\2\3\2\7\2\u00a1\n\2\f\2\16")
        buf.write("\2\u00a4\13\2\3\2\5\2\u00a7\n\2\3\3\3\3\3\3\5\3\u00ac")
        buf.write("\n\3\3\3\7\3\u00af\n\3\f\3\16\3\u00b2\13\3\3\3\3\3\5\3")
        buf.write("\u00b6\n\3\3\4\3\4\3\4\3\4\5\4\u00bc\n\4\3\4\7\4\u00bf")
        buf.write("\n\4\f\4\16\4\u00c2\13\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00ca")
        buf.write("\n\4\3\5\3\5\3\5\3\5\5\5\u00d0\n\5\3\5\7\5\u00d3\n\5\f")
        buf.write("\5\16\5\u00d6\13\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00de\n")
        buf.write("\5\3\6\3\6\3\6\5\6\u00e3\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\5\t\u00ef\n\t\3\n\3\n\3\13\3\13\5\13\u00f5")
        buf.write("\n\13\3\13\7\13\u00f8\n\13\f\13\16\13\u00fb\13\13\3\f")
        buf.write("\3\f\7\f\u00ff\n\f\f\f\16\f\u0102\13\f\3\r\3\r\5\r\u0106")
        buf.write("\n\r\3\r\6\r\u0109\n\r\r\r\16\r\u010a\3\16\3\16\3\16\3")
        buf.write("\16\7\16\u0111\n\16\f\16\16\16\u0114\13\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\5\'\u01af\n\'\3\'\3\'\3(\3(\7(\u01b5")
        buf.write("\n(\f(\16(\u01b8\13(\3(\3(\3(\3)\3)\5)\u01bf\n)\3*\3*")
        buf.write("\3*\5*\u01c4\n*\3*\3*\3*\3*\3*\3*\5*\u01cc\n*\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\3\67\38\38\39\39\39\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3A\3B\3B\3")
        buf.write("C\3C\3D\3D\3E\3E\3E\3F\3F\3G\3G\3H\3H\7H\u0217\nH\fH\16")
        buf.write("H\u021a\13H\3I\3I\6I\u021e\nI\rI\16I\u021f\3J\6J\u0223")
        buf.write("\nJ\rJ\16J\u0224\3J\3J\3K\3K\7K\u022b\nK\fK\16K\u022e")
        buf.write("\13K\3K\3K\3L\3L\7L\u0234\nL\fL\16L\u0237\13L\3L\3L\3")
        buf.write("L\3M\3M\3M\3\u0112\2N\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21")
        buf.write("\2\23\2\25\2\27\2\31\2\33\3\35\4\37\5!\6#\7%\b\'\t)\2")
        buf.write("+\2-\n/\13\61\f\63\r\65\16\67\179\20;\21=\22?\23A\24C")
        buf.write("\25E\26G\27I\30K\31M\32O\33Q\34S\35U\36W\37Y [!]\"_#a")
        buf.write("$c%e&g\'i(k)m*o+q,s-u.w/y\60{\61}\62\177\63\u0081\64\u0083")
        buf.write("\65\u0085\66\u0087\67\u00898\u008b9\u008d:\u008f;\u0091")
        buf.write("<\u0093=\u0095>\u0097?\u0099@\3\2\24\3\2\63;\3\2\62;\3")
        buf.write("\2\639\3\2\629\4\2DDdd\3\2\63\63\3\2\62\63\4\2ZZzz\4\2")
        buf.write("\63;CH\4\2\62;CH\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttv")
        buf.write("v\3\2$$\4\2--//\4\2GGgg\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\16\17\"\"\2\u0253\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u00a6\3\2\2\2\5\u00b5")
        buf.write("\3\2\2\2\7\u00c9\3\2\2\2\t\u00dd\3\2\2\2\13\u00e2\3\2")
        buf.write("\2\2\r\u00e4\3\2\2\2\17\u00e7\3\2\2\2\21\u00ee\3\2\2\2")
        buf.write("\23\u00f0\3\2\2\2\25\u00f2\3\2\2\2\27\u00fc\3\2\2\2\31")
        buf.write("\u0103\3\2\2\2\33\u010c\3\2\2\2\35\u011a\3\2\2\2\37\u0120")
        buf.write("\3\2\2\2!\u0129\3\2\2\2#\u012c\3\2\2\2%\u0133\3\2\2\2")
        buf.write("\'\u0138\3\2\2\2)\u0140\3\2\2\2+\u0145\3\2\2\2-\u014b")
        buf.write("\3\2\2\2/\u014f\3\2\2\2\61\u0153\3\2\2\2\63\u0158\3\2")
        buf.write("\2\2\65\u015f\3\2\2\2\67\u0162\3\2\2\29\u0165\3\2\2\2")
        buf.write(";\u0169\3\2\2\2=\u0175\3\2\2\2?\u0180\3\2\2\2A\u0185\3")
        buf.write("\2\2\2C\u018b\3\2\2\2E\u0191\3\2\2\2G\u0195\3\2\2\2I\u019b")
        buf.write("\3\2\2\2K\u01a3\3\2\2\2M\u01ae\3\2\2\2O\u01b2\3\2\2\2")
        buf.write("Q\u01be\3\2\2\2S\u01cb\3\2\2\2U\u01cf\3\2\2\2W\u01d1\3")
        buf.write("\2\2\2Y\u01d3\3\2\2\2[\u01d5\3\2\2\2]\u01d7\3\2\2\2_\u01d9")
        buf.write("\3\2\2\2a\u01db\3\2\2\2c\u01de\3\2\2\2e\u01e1\3\2\2\2")
        buf.write("g\u01e4\3\2\2\2i\u01e6\3\2\2\2k\u01e9\3\2\2\2m\u01eb\3")
        buf.write("\2\2\2o\u01ee\3\2\2\2q\u01f0\3\2\2\2s\u01f3\3\2\2\2u\u01f7")
        buf.write("\3\2\2\2w\u01fa\3\2\2\2y\u01fc\3\2\2\2{\u01fe\3\2\2\2")
        buf.write("}\u0200\3\2\2\2\177\u0202\3\2\2\2\u0081\u0204\3\2\2\2")
        buf.write("\u0083\u0207\3\2\2\2\u0085\u0209\3\2\2\2\u0087\u020b\3")
        buf.write("\2\2\2\u0089\u020d\3\2\2\2\u008b\u0210\3\2\2\2\u008d\u0212")
        buf.write("\3\2\2\2\u008f\u0214\3\2\2\2\u0091\u021b\3\2\2\2\u0093")
        buf.write("\u0222\3\2\2\2\u0095\u0228\3\2\2\2\u0097\u0231\3\2\2\2")
        buf.write("\u0099\u023b\3\2\2\2\u009b\u00a2\t\2\2\2\u009c\u009e\7")
        buf.write("a\2\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\u00a1\t\3\2\2\u00a0\u009d\3\2\2\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a7\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7\7")
        buf.write("\62\2\2\u00a6\u009b\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\4\3\2\2\2\u00a8\u00a9\7\62\2\2\u00a9\u00b0\t\4\2\2\u00aa")
        buf.write("\u00ac\7a\2\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00af\t\5\2\2\u00ae\u00ab\3")
        buf.write("\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00b6\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write("\u00b4\7\62\2\2\u00b4\u00b6\7\62\2\2\u00b5\u00a8\3\2\2")
        buf.write("\2\u00b5\u00b3\3\2\2\2\u00b6\6\3\2\2\2\u00b7\u00b8\7\62")
        buf.write("\2\2\u00b8\u00b9\t\6\2\2\u00b9\u00c0\t\7\2\2\u00ba\u00bc")
        buf.write("\7a\2\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00bf\t\b\2\2\u00be\u00bb\3\2\2\2")
        buf.write("\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1\u00ca\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4")
        buf.write("\7\62\2\2\u00c4\u00c5\7d\2\2\u00c5\u00ca\7\62\2\2\u00c6")
        buf.write("\u00c7\7\62\2\2\u00c7\u00c8\7D\2\2\u00c8\u00ca\7\62\2")
        buf.write("\2\u00c9\u00b7\3\2\2\2\u00c9\u00c3\3\2\2\2\u00c9\u00c6")
        buf.write("\3\2\2\2\u00ca\b\3\2\2\2\u00cb\u00cc\7\62\2\2\u00cc\u00cd")
        buf.write("\t\t\2\2\u00cd\u00d4\t\n\2\2\u00ce\u00d0\7a\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d3\t\13\2\2\u00d2\u00cf\3\2\2\2\u00d3\u00d6")
        buf.write("\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\u00de\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\7\62\2")
        buf.write("\2\u00d8\u00d9\7z\2\2\u00d9\u00de\7\62\2\2\u00da\u00db")
        buf.write("\7\62\2\2\u00db\u00dc\7Z\2\2\u00dc\u00de\7\62\2\2\u00dd")
        buf.write("\u00cb\3\2\2\2\u00dd\u00d7\3\2\2\2\u00dd\u00da\3\2\2\2")
        buf.write("\u00de\n\3\2\2\2\u00df\u00e3\n\f\2\2\u00e0\u00e3\5\r\7")
        buf.write("\2\u00e1\u00e3\5\17\b\2\u00e2\u00df\3\2\2\2\u00e2\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\f\3\2\2\2\u00e4\u00e5")
        buf.write("\7^\2\2\u00e5\u00e6\t\r\2\2\u00e6\16\3\2\2\2\u00e7\u00e8")
        buf.write("\7)\2\2\u00e8\u00e9\7$\2\2\u00e9\20\3\2\2\2\u00ea\u00eb")
        buf.write("\7^\2\2\u00eb\u00ef\n\r\2\2\u00ec\u00ed\7)\2\2\u00ed\u00ef")
        buf.write("\n\16\2\2\u00ee\u00ea\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef")
        buf.write("\22\3\2\2\2\u00f0\u00f1\t\17\2\2\u00f1\24\3\2\2\2\u00f2")
        buf.write("\u00f9\t\3\2\2\u00f3\u00f5\7a\2\2\u00f4\u00f3\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\t")
        buf.write("\3\2\2\u00f7\u00f4\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\26\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\u0100\7\60\2\2\u00fd\u00ff\t\3\2\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0100\u0101\3\2\2\2\u0101\30\3\2\2\2\u0102\u0100\3\2")
        buf.write("\2\2\u0103\u0105\t\20\2\2\u0104\u0106\5\23\n\2\u0105\u0104")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107")
        buf.write("\u0109\t\3\2\2\u0108\u0107\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\32\3\2")
        buf.write("\2\2\u010c\u010d\7%\2\2\u010d\u010e\7%\2\2\u010e\u0112")
        buf.write("\3\2\2\2\u010f\u0111\13\2\2\2\u0110\u010f\3\2\2\2\u0111")
        buf.write("\u0114\3\2\2\2\u0112\u0113\3\2\2\2\u0112\u0110\3\2\2\2")
        buf.write("\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116\7")
        buf.write("%\2\2\u0116\u0117\7%\2\2\u0117\u0118\3\2\2\2\u0118\u0119")
        buf.write("\b\16\2\2\u0119\34\3\2\2\2\u011a\u011b\7D\2\2\u011b\u011c")
        buf.write("\7t\2\2\u011c\u011d\7g\2\2\u011d\u011e\7c\2\2\u011e\u011f")
        buf.write("\7m\2\2\u011f\36\3\2\2\2\u0120\u0121\7E\2\2\u0121\u0122")
        buf.write("\7q\2\2\u0122\u0123\7p\2\2\u0123\u0124\7v\2\2\u0124\u0125")
        buf.write("\7k\2\2\u0125\u0126\7p\2\2\u0126\u0127\7w\2\2\u0127\u0128")
        buf.write("\7g\2\2\u0128 \3\2\2\2\u0129\u012a\7K\2\2\u012a\u012b")
        buf.write("\7h\2\2\u012b\"\3\2\2\2\u012c\u012d\7G\2\2\u012d\u012e")
        buf.write("\7n\2\2\u012e\u012f\7u\2\2\u012f\u0130\7g\2\2\u0130\u0131")
        buf.write("\7k\2\2\u0131\u0132\7h\2\2\u0132$\3\2\2\2\u0133\u0134")
        buf.write("\7G\2\2\u0134\u0135\7n\2\2\u0135\u0136\7u\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137&\3\2\2\2\u0138\u0139\7H\2\2\u0139\u013a")
        buf.write("\7q\2\2\u013a\u013b\7t\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\7c\2\2\u013d\u013e\7e\2\2\u013e\u013f\7j\2\2\u013f(\3")
        buf.write("\2\2\2\u0140\u0141\7V\2\2\u0141\u0142\7t\2\2\u0142\u0143")
        buf.write("\7w\2\2\u0143\u0144\7g\2\2\u0144*\3\2\2\2\u0145\u0146")
        buf.write("\7H\2\2\u0146\u0147\7c\2\2\u0147\u0148\7n\2\2\u0148\u0149")
        buf.write("\7u\2\2\u0149\u014a\7g\2\2\u014a,\3\2\2\2\u014b\u014c")
        buf.write("\7X\2\2\u014c\u014d\7c\2\2\u014d\u014e\7t\2\2\u014e.\3")
        buf.write("\2\2\2\u014f\u0150\7X\2\2\u0150\u0151\7c\2\2\u0151\u0152")
        buf.write("\7n\2\2\u0152\60\3\2\2\2\u0153\u0154\7U\2\2\u0154\u0155")
        buf.write("\7g\2\2\u0155\u0156\7n\2\2\u0156\u0157\7h\2\2\u0157\62")
        buf.write("\3\2\2\2\u0158\u0159\7T\2\2\u0159\u015a\7g\2\2\u015a\u015b")
        buf.write("\7v\2\2\u015b\u015c\7w\2\2\u015c\u015d\7t\2\2\u015d\u015e")
        buf.write("\7p\2\2\u015e\64\3\2\2\2\u015f\u0160\7K\2\2\u0160\u0161")
        buf.write("\7p\2\2\u0161\66\3\2\2\2\u0162\u0163\7D\2\2\u0163\u0164")
        buf.write("\7{\2\2\u01648\3\2\2\2\u0165\u0166\7P\2\2\u0166\u0167")
        buf.write("\7g\2\2\u0167\u0168\7y\2\2\u0168:\3\2\2\2\u0169\u016a")
        buf.write("\7E\2\2\u016a\u016b\7q\2\2\u016b\u016c\7p\2\2\u016c\u016d")
        buf.write("\7u\2\2\u016d\u016e\7v\2\2\u016e\u016f\7t\2\2\u016f\u0170")
        buf.write("\7w\2\2\u0170\u0171\7e\2\2\u0171\u0172\7v\2\2\u0172\u0173")
        buf.write("\7q\2\2\u0173\u0174\7t\2\2\u0174<\3\2\2\2\u0175\u0176")
        buf.write("\7F\2\2\u0176\u0177\7g\2\2\u0177\u0178\7u\2\2\u0178\u0179")
        buf.write("\7v\2\2\u0179\u017a\7t\2\2\u017a\u017b\7w\2\2\u017b\u017c")
        buf.write("\7e\2\2\u017c\u017d\7v\2\2\u017d\u017e\7q\2\2\u017e\u017f")
        buf.write("\7t\2\2\u017f>\3\2\2\2\u0180\u0181\7P\2\2\u0181\u0182")
        buf.write("\7w\2\2\u0182\u0183\7n\2\2\u0183\u0184\7n\2\2\u0184@\3")
        buf.write("\2\2\2\u0185\u0186\7E\2\2\u0186\u0187\7n\2\2\u0187\u0188")
        buf.write("\7c\2\2\u0188\u0189\7u\2\2\u0189\u018a\7u\2\2\u018aB\3")
        buf.write("\2\2\2\u018b\u018c\7C\2\2\u018c\u018d\7t\2\2\u018d\u018e")
        buf.write("\7t\2\2\u018e\u018f\7c\2\2\u018f\u0190\7{\2\2\u0190D\3")
        buf.write("\2\2\2\u0191\u0192\7K\2\2\u0192\u0193\7p\2\2\u0193\u0194")
        buf.write("\7v\2\2\u0194F\3\2\2\2\u0195\u0196\7H\2\2\u0196\u0197")
        buf.write("\7n\2\2\u0197\u0198\7q\2\2\u0198\u0199\7c\2\2\u0199\u019a")
        buf.write("\7v\2\2\u019aH\3\2\2\2\u019b\u019c\7D\2\2\u019c\u019d")
        buf.write("\7q\2\2\u019d\u019e\7q\2\2\u019e\u019f\7n\2\2\u019f\u01a0")
        buf.write("\7g\2\2\u01a0\u01a1\7c\2\2\u01a1\u01a2\7p\2\2\u01a2J\3")
        buf.write("\2\2\2\u01a3\u01a4\7U\2\2\u01a4\u01a5\7v\2\2\u01a5\u01a6")
        buf.write("\7t\2\2\u01a6\u01a7\7k\2\2\u01a7\u01a8\7p\2\2\u01a8\u01a9")
        buf.write("\7i\2\2\u01a9L\3\2\2\2\u01aa\u01af\5\3\2\2\u01ab\u01af")
        buf.write("\5\5\3\2\u01ac\u01af\5\t\5\2\u01ad\u01af\5\7\4\2\u01ae")
        buf.write("\u01aa\3\2\2\2\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\b")
        buf.write("\'\3\2\u01b1N\3\2\2\2\u01b2\u01b6\7$\2\2\u01b3\u01b5\5")
        buf.write("\13\6\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b9\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7$\2\2\u01ba\u01bb\b")
        buf.write("(\4\2\u01bbP\3\2\2\2\u01bc\u01bf\5)\25\2\u01bd\u01bf\5")
        buf.write("+\26\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfR")
        buf.write("\3\2\2\2\u01c0\u01c1\5\25\13\2\u01c1\u01c3\5\27\f\2\u01c2")
        buf.write("\u01c4\5\31\r\2\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3\2\2")
        buf.write("\2\u01c4\u01cc\3\2\2\2\u01c5\u01c6\5\25\13\2\u01c6\u01c7")
        buf.write("\5\31\r\2\u01c7\u01cc\3\2\2\2\u01c8\u01c9\5\27\f\2\u01c9")
        buf.write("\u01ca\5\31\r\2\u01ca\u01cc\3\2\2\2\u01cb\u01c0\3\2\2")
        buf.write("\2\u01cb\u01c5\3\2\2\2\u01cb\u01c8\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u01ce\b*\5\2\u01ceT\3\2\2\2\u01cf\u01d0")
        buf.write("\7-\2\2\u01d0V\3\2\2\2\u01d1\u01d2\7/\2\2\u01d2X\3\2\2")
        buf.write("\2\u01d3\u01d4\7,\2\2\u01d4Z\3\2\2\2\u01d5\u01d6\7\61")
        buf.write("\2\2\u01d6\\\3\2\2\2\u01d7\u01d8\7\'\2\2\u01d8^\3\2\2")
        buf.write("\2\u01d9\u01da\7#\2\2\u01da`\3\2\2\2\u01db\u01dc\7(\2")
        buf.write("\2\u01dc\u01dd\7(\2\2\u01ddb\3\2\2\2\u01de\u01df\7~\2")
        buf.write("\2\u01df\u01e0\7~\2\2\u01e0d\3\2\2\2\u01e1\u01e2\7?\2")
        buf.write("\2\u01e2\u01e3\7?\2\2\u01e3f\3\2\2\2\u01e4\u01e5\7?\2")
        buf.write("\2\u01e5h\3\2\2\2\u01e6\u01e7\7#\2\2\u01e7\u01e8\7?\2")
        buf.write("\2\u01e8j\3\2\2\2\u01e9\u01ea\7>\2\2\u01eal\3\2\2\2\u01eb")
        buf.write("\u01ec\7>\2\2\u01ec\u01ed\7?\2\2\u01edn\3\2\2\2\u01ee")
        buf.write("\u01ef\7@\2\2\u01efp\3\2\2\2\u01f0\u01f1\7@\2\2\u01f1")
        buf.write("\u01f2\7?\2\2\u01f2r\3\2\2\2\u01f3\u01f4\7?\2\2\u01f4")
        buf.write("\u01f5\7?\2\2\u01f5\u01f6\7\60\2\2\u01f6t\3\2\2\2\u01f7")
        buf.write("\u01f8\7-\2\2\u01f8\u01f9\7\60\2\2\u01f9v\3\2\2\2\u01fa")
        buf.write("\u01fb\7*\2\2\u01fbx\3\2\2\2\u01fc\u01fd\7+\2\2\u01fd")
        buf.write("z\3\2\2\2\u01fe\u01ff\7]\2\2\u01ff|\3\2\2\2\u0200\u0201")
        buf.write("\7_\2\2\u0201~\3\2\2\2\u0202\u0203\7\60\2\2\u0203\u0080")
        buf.write("\3\2\2\2\u0204\u0205\7\60\2\2\u0205\u0206\7\60\2\2\u0206")
        buf.write("\u0082\3\2\2\2\u0207\u0208\7.\2\2\u0208\u0084\3\2\2\2")
        buf.write("\u0209\u020a\7=\2\2\u020a\u0086\3\2\2\2\u020b\u020c\7")
        buf.write("<\2\2\u020c\u0088\3\2\2\2\u020d\u020e\7<\2\2\u020e\u020f")
        buf.write("\7<\2\2\u020f\u008a\3\2\2\2\u0210\u0211\7}\2\2\u0211\u008c")
        buf.write("\3\2\2\2\u0212\u0213\7\177\2\2\u0213\u008e\3\2\2\2\u0214")
        buf.write("\u0218\t\21\2\2\u0215\u0217\t\22\2\2\u0216\u0215\3\2\2")
        buf.write("\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219")
        buf.write("\3\2\2\2\u0219\u0090\3\2\2\2\u021a\u0218\3\2\2\2\u021b")
        buf.write("\u021d\7&\2\2\u021c\u021e\t\22\2\2\u021d\u021c\3\2\2\2")
        buf.write("\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3")
        buf.write("\2\2\2\u0220\u0092\3\2\2\2\u0221\u0223\t\23\2\2\u0222")
        buf.write("\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0224\u0225\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\b")
        buf.write("J\2\2\u0227\u0094\3\2\2\2\u0228\u022c\7$\2\2\u0229\u022b")
        buf.write("\5\13\6\2\u022a\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c")
        buf.write("\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\3\2\2\2")
        buf.write("\u022e\u022c\3\2\2\2\u022f\u0230\bK\6\2\u0230\u0096\3")
        buf.write("\2\2\2\u0231\u0235\7$\2\2\u0232\u0234\5\13\6\2\u0233\u0232")
        buf.write("\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235")
        buf.write("\u0236\3\2\2\2\u0236\u0238\3\2\2\2\u0237\u0235\3\2\2\2")
        buf.write("\u0238\u0239\5\21\t\2\u0239\u023a\bL\7\2\u023a\u0098\3")
        buf.write("\2\2\2\u023b\u023c\13\2\2\2\u023c\u023d\bM\b\2\u023d\u009a")
        buf.write("\3\2\2\2!\2\u009d\u00a2\u00a6\u00ab\u00b0\u00b5\u00bb")
        buf.write("\u00c0\u00c9\u00cf\u00d4\u00dd\u00e2\u00ee\u00f4\u00f9")
        buf.write("\u0100\u0105\u010a\u0112\u01ae\u01b6\u01be\u01c3\u01cb")
        buf.write("\u0218\u021f\u0224\u022c\u0235\t\b\2\2\3\'\2\3(\3\3*\4")
        buf.write("\3K\5\3L\6\3M\7")
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

     


