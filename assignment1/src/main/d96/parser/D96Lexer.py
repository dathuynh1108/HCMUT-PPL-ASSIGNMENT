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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0244\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\5\3\u00ae\n\3\3\4\3\4\7\4\u00b2\n")
        buf.write("\4\f\4\16\4\u00b5\13\4\3\4\7\4\u00b8\n\4\f\4\16\4\u00bb")
        buf.write("\13\4\3\4\5\4\u00be\n\4\3\5\3\5\6\5\u00c2\n\5\r\5\16\5")
        buf.write("\u00c3\3\6\3\6\3\6\6\6\u00c9\n\6\r\6\16\6\u00ca\3\7\3")
        buf.write("\7\3\7\6\7\u00d0\n\7\r\7\16\7\u00d1\3\b\3\b\3\b\5\b\u00d7")
        buf.write("\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00e4\n\13\3\f\3\f\3\r\3\r\7\r\u00ea\n\r\f\r\16")
        buf.write("\r\u00ed\13\r\3\16\3\16\5\16\u00f1\n\16\3\17\3\17\5\17")
        buf.write("\u00f5\n\17\3\17\3\17\3\20\3\20\3\20\3\20\7\20\u00fd\n")
        buf.write("\20\f\20\16\20\u0100\13\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\5")
        buf.write("(\u0193\n(\3(\3(\3)\3)\7)\u0199\n)\f)\16)\u019c\13)\3")
        buf.write(")\3)\3)\3*\3*\5*\u01a3\n*\3+\3+\3+\5+\u01a8\n+\3+\3+\3")
        buf.write("+\3+\3+\3+\5+\u01b0\n+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("8\39\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3=\3=\3=\3=\3>\3")
        buf.write(">\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3G\3H\3H\3I\3I\3J\3J\7J\u01ff\nJ\fJ\16J\u0202\13")
        buf.write("J\3K\3K\3K\7K\u0207\nK\fK\16K\u020a\13K\3L\6L\u020d\n")
        buf.write("L\rL\16L\u020e\3L\3L\3M\3M\3M\3M\7M\u0217\nM\fM\16M\u021a")
        buf.write("\13M\3M\3M\3M\3M\3M\7M\u0221\nM\fM\16M\u0224\13M\3M\3")
        buf.write("M\5M\u0228\nM\3M\3M\3N\3N\7N\u022e\nN\fN\16N\u0231\13")
        buf.write("N\3N\5N\u0234\nN\3N\3N\3O\3O\7O\u023a\nO\fO\16O\u023d")
        buf.write("\13O\3O\3O\3O\3P\3P\3P\2\2Q\3\3\5\2\7\2\t\2\13\2\r\2\17")
        buf.write("\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\4!\5#\6%\7\'")
        buf.write("\b)\t+\n-\2/\2\61\13\63\f\65\r\67\169\17;\20=\21?\22A")
        buf.write("\23C\24E\25G\26I\27K\30M\31O\32Q\33S\34U\35W\36Y\37[ ")
        buf.write("]!_\"a#c$e%g&i\'k(m)o*q+s,u-w.y/{\60}\61\177\62\u0081")
        buf.write("\63\u0083\64\u0085\65\u0087\66\u0089\67\u008b8\u008d9")
        buf.write("\u008f:\u0091;\u0093<\u0095=\u0097>\u0099?\u009b@\u009d")
        buf.write("A\u009fB\3\2\25\3\2%%\3\2\63;\3\2\62;\3\2\629\4\2DDdd")
        buf.write("\3\2\62\63\4\2ZZzz\5\2\62;CHch\7\2\n\f\16\17$$))^^\t\2")
        buf.write("))^^ddhhppttvv\3\2$$\3\2^^\4\2--//\4\2\62;aa\4\2GGgg\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\7\3\n\f\16")
        buf.write("\17$$))^^\2\u0253\2\3\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
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
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\3\u00a1\3\2\2\2\5\u00ad\3\2\2\2\7\u00bd\3\2\2")
        buf.write("\2\t\u00bf\3\2\2\2\13\u00c5\3\2\2\2\r\u00cc\3\2\2\2\17")
        buf.write("\u00d6\3\2\2\2\21\u00d8\3\2\2\2\23\u00db\3\2\2\2\25\u00e3")
        buf.write("\3\2\2\2\27\u00e5\3\2\2\2\31\u00e7\3\2\2\2\33\u00ee\3")
        buf.write("\2\2\2\35\u00f2\3\2\2\2\37\u00f8\3\2\2\2!\u0106\3\2\2")
        buf.write("\2#\u010c\3\2\2\2%\u0115\3\2\2\2\'\u0118\3\2\2\2)\u011f")
        buf.write("\3\2\2\2+\u0124\3\2\2\2-\u0128\3\2\2\2/\u012d\3\2\2\2")
        buf.write("\61\u0133\3\2\2\2\63\u0137\3\2\2\2\65\u013b\3\2\2\2\67")
        buf.write("\u0140\3\2\2\29\u0147\3\2\2\2;\u014a\3\2\2\2=\u014d\3")
        buf.write("\2\2\2?\u0159\3\2\2\2A\u0164\3\2\2\2C\u016a\3\2\2\2E\u0170")
        buf.write("\3\2\2\2G\u0174\3\2\2\2I\u017a\3\2\2\2K\u0182\3\2\2\2")
        buf.write("M\u0189\3\2\2\2O\u0192\3\2\2\2Q\u0196\3\2\2\2S\u01a2\3")
        buf.write("\2\2\2U\u01af\3\2\2\2W\u01b3\3\2\2\2Y\u01b5\3\2\2\2[\u01b7")
        buf.write("\3\2\2\2]\u01b9\3\2\2\2_\u01bb\3\2\2\2a\u01bd\3\2\2\2")
        buf.write("c\u01bf\3\2\2\2e\u01c2\3\2\2\2g\u01c5\3\2\2\2i\u01c8\3")
        buf.write("\2\2\2k\u01ca\3\2\2\2m\u01cd\3\2\2\2o\u01cf\3\2\2\2q\u01d2")
        buf.write("\3\2\2\2s\u01d4\3\2\2\2u\u01d7\3\2\2\2w\u01db\3\2\2\2")
        buf.write("y\u01de\3\2\2\2{\u01e2\3\2\2\2}\u01e4\3\2\2\2\177\u01e6")
        buf.write("\3\2\2\2\u0081\u01e8\3\2\2\2\u0083\u01ea\3\2\2\2\u0085")
        buf.write("\u01ec\3\2\2\2\u0087\u01ef\3\2\2\2\u0089\u01f1\3\2\2\2")
        buf.write("\u008b\u01f3\3\2\2\2\u008d\u01f5\3\2\2\2\u008f\u01f8\3")
        buf.write("\2\2\2\u0091\u01fa\3\2\2\2\u0093\u01fc\3\2\2\2\u0095\u0203")
        buf.write("\3\2\2\2\u0097\u020c\3\2\2\2\u0099\u0227\3\2\2\2\u009b")
        buf.write("\u022b\3\2\2\2\u009d\u0237\3\2\2\2\u009f\u0241\3\2\2\2")
        buf.write("\u00a1\u00a2\7E\2\2\u00a2\u00a3\7j\2\2\u00a3\u00a4\7w")
        buf.write("\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7\"\2\2\u00a6\u00a7")
        buf.write("\7n\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7o\2\2\u00a9\4")
        buf.write("\3\2\2\2\u00aa\u00ae\n\2\2\2\u00ab\u00ac\7%\2\2\u00ac")
        buf.write("\u00ae\n\2\2\2\u00ad\u00aa\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ae\6\3\2\2\2\u00af\u00b9\t\3\2\2\u00b0\u00b2\7a\2")
        buf.write("\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b6\u00b8\t\4\2\2\u00b7\u00b3\3\2\2\2")
        buf.write("\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3")
        buf.write("\2\2\2\u00ba\u00be\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00be")
        buf.write("\7\62\2\2\u00bd\u00af\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\b\3\2\2\2\u00bf\u00c1\7\62\2\2\u00c0\u00c2\t\5\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\n\3\2\2\2\u00c5\u00c6\7\62")
        buf.write("\2\2\u00c6\u00c8\t\6\2\2\u00c7\u00c9\t\7\2\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\f\3\2\2\2\u00cc\u00cd\7\62\2\2\u00cd")
        buf.write("\u00cf\t\b\2\2\u00ce\u00d0\t\t\2\2\u00cf\u00ce\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3")
        buf.write("\2\2\2\u00d2\16\3\2\2\2\u00d3\u00d7\n\n\2\2\u00d4\u00d7")
        buf.write("\5\21\t\2\u00d5\u00d7\5\23\n\2\u00d6\u00d3\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\20\3\2\2\2\u00d8")
        buf.write("\u00d9\7^\2\2\u00d9\u00da\t\13\2\2\u00da\22\3\2\2\2\u00db")
        buf.write("\u00dc\7)\2\2\u00dc\u00dd\7$\2\2\u00dd\24\3\2\2\2\u00de")
        buf.write("\u00df\7^\2\2\u00df\u00e4\n\13\2\2\u00e0\u00e1\7)\2\2")
        buf.write("\u00e1\u00e4\n\f\2\2\u00e2\u00e4\n\r\2\2\u00e3\u00de\3")
        buf.write("\2\2\2\u00e3\u00e0\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\26")
        buf.write("\3\2\2\2\u00e5\u00e6\t\16\2\2\u00e6\30\3\2\2\2\u00e7\u00eb")
        buf.write("\t\4\2\2\u00e8\u00ea\t\17\2\2\u00e9\u00e8\3\2\2\2\u00ea")
        buf.write("\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\32\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f0\7\60")
        buf.write("\2\2\u00ef\u00f1\5\31\r\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\34\3\2\2\2\u00f2\u00f4\t\20\2\2\u00f3\u00f5")
        buf.write("\5\27\f\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\u00f7\5\31\r\2\u00f7\36\3\2\2\2\u00f8")
        buf.write("\u00f9\7%\2\2\u00f9\u00fa\7%\2\2\u00fa\u00fe\3\2\2\2\u00fb")
        buf.write("\u00fd\5\5\3\2\u00fc\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\3")
        buf.write("\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\7%\2\2\u0102\u0103")
        buf.write("\7%\2\2\u0103\u0104\3\2\2\2\u0104\u0105\b\20\2\2\u0105")
        buf.write(" \3\2\2\2\u0106\u0107\7D\2\2\u0107\u0108\7t\2\2\u0108")
        buf.write("\u0109\7g\2\2\u0109\u010a\7c\2\2\u010a\u010b\7m\2\2\u010b")
        buf.write("\"\3\2\2\2\u010c\u010d\7E\2\2\u010d\u010e\7q\2\2\u010e")
        buf.write("\u010f\7p\2\2\u010f\u0110\7v\2\2\u0110\u0111\7k\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112\u0113\7w\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("$\3\2\2\2\u0115\u0116\7K\2\2\u0116\u0117\7h\2\2\u0117")
        buf.write("&\3\2\2\2\u0118\u0119\7G\2\2\u0119\u011a\7n\2\2\u011a")
        buf.write("\u011b\7u\2\2\u011b\u011c\7g\2\2\u011c\u011d\7k\2\2\u011d")
        buf.write("\u011e\7h\2\2\u011e(\3\2\2\2\u011f\u0120\7G\2\2\u0120")
        buf.write("\u0121\7n\2\2\u0121\u0122\7u\2\2\u0122\u0123\7g\2\2\u0123")
        buf.write("*\3\2\2\2\u0124\u0125\7H\2\2\u0125\u0126\7q\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127,\3\2\2\2\u0128\u0129\7V\2\2\u0129")
        buf.write("\u012a\7t\2\2\u012a\u012b\7w\2\2\u012b\u012c\7g\2\2\u012c")
        buf.write(".\3\2\2\2\u012d\u012e\7H\2\2\u012e\u012f\7c\2\2\u012f")
        buf.write("\u0130\7n\2\2\u0130\u0131\7u\2\2\u0131\u0132\7g\2\2\u0132")
        buf.write("\60\3\2\2\2\u0133\u0134\7x\2\2\u0134\u0135\7c\2\2\u0135")
        buf.write("\u0136\7t\2\2\u0136\62\3\2\2\2\u0137\u0138\7x\2\2\u0138")
        buf.write("\u0139\7c\2\2\u0139\u013a\7n\2\2\u013a\64\3\2\2\2\u013b")
        buf.write("\u013c\7u\2\2\u013c\u013d\7g\2\2\u013d\u013e\7n\2\2\u013e")
        buf.write("\u013f\7h\2\2\u013f\66\3\2\2\2\u0140\u0141\7t\2\2\u0141")
        buf.write("\u0142\7g\2\2\u0142\u0143\7v\2\2\u0143\u0144\7w\2\2\u0144")
        buf.write("\u0145\7t\2\2\u0145\u0146\7p\2\2\u01468\3\2\2\2\u0147")
        buf.write("\u0148\7K\2\2\u0148\u0149\7p\2\2\u0149:\3\2\2\2\u014a")
        buf.write("\u014b\7D\2\2\u014b\u014c\7{\2\2\u014c<\3\2\2\2\u014d")
        buf.write("\u014e\7e\2\2\u014e\u014f\7q\2\2\u014f\u0150\7p\2\2\u0150")
        buf.write("\u0151\7u\2\2\u0151\u0152\7v\2\2\u0152\u0153\7t\2\2\u0153")
        buf.write("\u0154\7w\2\2\u0154\u0155\7e\2\2\u0155\u0156\7v\2\2\u0156")
        buf.write("\u0157\7q\2\2\u0157\u0158\7t\2\2\u0158>\3\2\2\2\u0159")
        buf.write("\u015a\7f\2\2\u015a\u015b\7g\2\2\u015b\u015c\7u\2\2\u015c")
        buf.write("\u015d\7v\2\2\u015d\u015e\7t\2\2\u015e\u015f\7w\2\2\u015f")
        buf.write("\u0160\7e\2\2\u0160\u0161\7v\2\2\u0161\u0162\7q\2\2\u0162")
        buf.write("\u0163\7t\2\2\u0163@\3\2\2\2\u0164\u0165\7e\2\2\u0165")
        buf.write("\u0166\7n\2\2\u0166\u0167\7c\2\2\u0167\u0168\7u\2\2\u0168")
        buf.write("\u0169\7u\2\2\u0169B\3\2\2\2\u016a\u016b\7C\2\2\u016b")
        buf.write("\u016c\7t\2\2\u016c\u016d\7t\2\2\u016d\u016e\7c\2\2\u016e")
        buf.write("\u016f\7{\2\2\u016fD\3\2\2\2\u0170\u0171\7K\2\2\u0171")
        buf.write("\u0172\7p\2\2\u0172\u0173\7v\2\2\u0173F\3\2\2\2\u0174")
        buf.write("\u0175\7H\2\2\u0175\u0176\7n\2\2\u0176\u0177\7q\2\2\u0177")
        buf.write("\u0178\7c\2\2\u0178\u0179\7v\2\2\u0179H\3\2\2\2\u017a")
        buf.write("\u017b\7D\2\2\u017b\u017c\7q\2\2\u017c\u017d\7q\2\2\u017d")
        buf.write("\u017e\7n\2\2\u017e\u017f\7g\2\2\u017f\u0180\7c\2\2\u0180")
        buf.write("\u0181\7p\2\2\u0181J\3\2\2\2\u0182\u0183\7U\2\2\u0183")
        buf.write("\u0184\7v\2\2\u0184\u0185\7t\2\2\u0185\u0186\7k\2\2\u0186")
        buf.write("\u0187\7p\2\2\u0187\u0188\7i\2\2\u0188L\3\2\2\2\u0189")
        buf.write("\u018a\7P\2\2\u018a\u018b\7w\2\2\u018b\u018c\7n\2\2\u018c")
        buf.write("\u018d\7n\2\2\u018dN\3\2\2\2\u018e\u0193\5\7\4\2\u018f")
        buf.write("\u0193\5\t\5\2\u0190\u0193\5\r\7\2\u0191\u0193\5\13\6")
        buf.write("\2\u0192\u018e\3\2\2\2\u0192\u018f\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0195\b(\3\2\u0195P\3\2\2\2\u0196\u019a\7$\2\2\u0197")
        buf.write("\u0199\5\17\b\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2")
        buf.write("\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\7$\2\2\u019e")
        buf.write("\u019f\b)\4\2\u019fR\3\2\2\2\u01a0\u01a3\5-\27\2\u01a1")
        buf.write("\u01a3\5/\30\2\u01a2\u01a0\3\2\2\2\u01a2\u01a1\3\2\2\2")
        buf.write("\u01a3T\3\2\2\2\u01a4\u01a5\5\31\r\2\u01a5\u01a7\5\33")
        buf.write("\16\2\u01a6\u01a8\5\35\17\2\u01a7\u01a6\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01b0\3\2\2\2\u01a9\u01aa\5\31\r")
        buf.write("\2\u01aa\u01ab\5\35\17\2\u01ab\u01b0\3\2\2\2\u01ac\u01ad")
        buf.write("\5\33\16\2\u01ad\u01ae\5\35\17\2\u01ae\u01b0\3\2\2\2\u01af")
        buf.write("\u01a4\3\2\2\2\u01af\u01a9\3\2\2\2\u01af\u01ac\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u01b2\b+\5\2\u01b2V\3\2\2\2")
        buf.write("\u01b3\u01b4\7-\2\2\u01b4X\3\2\2\2\u01b5\u01b6\7/\2\2")
        buf.write("\u01b6Z\3\2\2\2\u01b7\u01b8\7,\2\2\u01b8\\\3\2\2\2\u01b9")
        buf.write("\u01ba\7\61\2\2\u01ba^\3\2\2\2\u01bb\u01bc\7\'\2\2\u01bc")
        buf.write("`\3\2\2\2\u01bd\u01be\7#\2\2\u01beb\3\2\2\2\u01bf\u01c0")
        buf.write("\7(\2\2\u01c0\u01c1\7(\2\2\u01c1d\3\2\2\2\u01c2\u01c3")
        buf.write("\7~\2\2\u01c3\u01c4\7~\2\2\u01c4f\3\2\2\2\u01c5\u01c6")
        buf.write("\7?\2\2\u01c6\u01c7\7?\2\2\u01c7h\3\2\2\2\u01c8\u01c9")
        buf.write("\7?\2\2\u01c9j\3\2\2\2\u01ca\u01cb\7#\2\2\u01cb\u01cc")
        buf.write("\7?\2\2\u01ccl\3\2\2\2\u01cd\u01ce\7>\2\2\u01cen\3\2\2")
        buf.write("\2\u01cf\u01d0\7>\2\2\u01d0\u01d1\7?\2\2\u01d1p\3\2\2")
        buf.write("\2\u01d2\u01d3\7@\2\2\u01d3r\3\2\2\2\u01d4\u01d5\7@\2")
        buf.write("\2\u01d5\u01d6\7?\2\2\u01d6t\3\2\2\2\u01d7\u01d8\7?\2")
        buf.write("\2\u01d8\u01d9\7?\2\2\u01d9\u01da\7\60\2\2\u01dav\3\2")
        buf.write("\2\2\u01db\u01dc\7-\2\2\u01dc\u01dd\7\60\2\2\u01ddx\3")
        buf.write("\2\2\2\u01de\u01df\7p\2\2\u01df\u01e0\7g\2\2\u01e0\u01e1")
        buf.write("\7y\2\2\u01e1z\3\2\2\2\u01e2\u01e3\7*\2\2\u01e3|\3\2\2")
        buf.write("\2\u01e4\u01e5\7+\2\2\u01e5~\3\2\2\2\u01e6\u01e7\7]\2")
        buf.write("\2\u01e7\u0080\3\2\2\2\u01e8\u01e9\7_\2\2\u01e9\u0082")
        buf.write("\3\2\2\2\u01ea\u01eb\7\60\2\2\u01eb\u0084\3\2\2\2\u01ec")
        buf.write("\u01ed\7\60\2\2\u01ed\u01ee\7\60\2\2\u01ee\u0086\3\2\2")
        buf.write("\2\u01ef\u01f0\7.\2\2\u01f0\u0088\3\2\2\2\u01f1\u01f2")
        buf.write("\7=\2\2\u01f2\u008a\3\2\2\2\u01f3\u01f4\7<\2\2\u01f4\u008c")
        buf.write("\3\2\2\2\u01f5\u01f6\7<\2\2\u01f6\u01f7\7<\2\2\u01f7\u008e")
        buf.write("\3\2\2\2\u01f8\u01f9\7}\2\2\u01f9\u0090\3\2\2\2\u01fa")
        buf.write("\u01fb\7\177\2\2\u01fb\u0092\3\2\2\2\u01fc\u0200\t\21")
        buf.write("\2\2\u01fd\u01ff\t\22\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0202")
        buf.write("\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201")
        buf.write("\u0094\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\7&\2\2")
        buf.write("\u0204\u0208\t\21\2\2\u0205\u0207\t\22\2\2\u0206\u0205")
        buf.write("\3\2\2\2\u0207\u020a\3\2\2\2\u0208\u0206\3\2\2\2\u0208")
        buf.write("\u0209\3\2\2\2\u0209\u0096\3\2\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020b\u020d\t\23\2\2\u020c\u020b\3\2\2\2\u020d\u020e")
        buf.write("\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u0210\u0211\bL\2\2\u0211\u0098\3\2\2\2")
        buf.write("\u0212\u0213\7%\2\2\u0213\u0214\7%\2\2\u0214\u0218\3\2")
        buf.write("\2\2\u0215\u0217\5\5\3\2\u0216\u0215\3\2\2\2\u0217\u021a")
        buf.write("\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u021b\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u0228\7\2\2\3")
        buf.write("\u021c\u021d\7%\2\2\u021d\u021e\7%\2\2\u021e\u0222\3\2")
        buf.write("\2\2\u021f\u0221\n\2\2\2\u0220\u021f\3\2\2\2\u0221\u0224")
        buf.write("\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223")
        buf.write("\u0225\3\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\7%\2\2")
        buf.write("\u0226\u0228\7\2\2\3\u0227\u0212\3\2\2\2\u0227\u021c\3")
        buf.write("\2\2\2\u0228\u0229\3\2\2\2\u0229\u022a\bM\6\2\u022a\u009a")
        buf.write("\3\2\2\2\u022b\u022f\7$\2\2\u022c\u022e\5\17\b\2\u022d")
        buf.write("\u022c\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2")
        buf.write("\u022f\u0230\3\2\2\2\u0230\u0233\3\2\2\2\u0231\u022f\3")
        buf.write("\2\2\2\u0232\u0234\t\24\2\2\u0233\u0232\3\2\2\2\u0234")
        buf.write("\u0235\3\2\2\2\u0235\u0236\bN\7\2\u0236\u009c\3\2\2\2")
        buf.write("\u0237\u023b\7$\2\2\u0238\u023a\5\17\b\2\u0239\u0238\3")
        buf.write("\2\2\2\u023a\u023d\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c")
        buf.write("\3\2\2\2\u023c\u023e\3\2\2\2\u023d\u023b\3\2\2\2\u023e")
        buf.write("\u023f\5\25\13\2\u023f\u0240\bO\b\2\u0240\u009e\3\2\2")
        buf.write("\2\u0241\u0242\13\2\2\2\u0242\u0243\bP\t\2\u0243\u00a0")
        buf.write("\3\2\2\2\36\2\u00ad\u00b3\u00b9\u00bd\u00c3\u00ca\u00d1")
        buf.write("\u00d6\u00e3\u00eb\u00f0\u00f4\u00fe\u0192\u019a\u01a2")
        buf.write("\u01a7\u01af\u0200\u0208\u020e\u0218\u0222\u0227\u022f")
        buf.write("\u0233\u023b\n\b\2\2\3(\2\3)\3\3+\4\3M\5\3N\6\3O\7\3P")
        buf.write("\b")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT = 2
    BREAK = 3
    CONTINUE = 4
    IF = 5
    ELSEIF = 6
    ELSE = 7
    FOR = 8
    VAR = 9
    VAL = 10
    SELF = 11
    RETURN = 12
    IN = 13
    BY = 14
    CONSTRUCTOR = 15
    DESTRUCTOR = 16
    CLASS = 17
    ARRAY = 18
    INT = 19
    FLOAT = 20
    BOOLEAN = 21
    STRING = 22
    NULL = 23
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
    NEW = 45
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
    UNTERMINATED_COMMENT = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_TOKEN = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Chua lam'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'For'", "'var'", "'val'", "'self'", "'return'", "'In'", "'By'", 
            "'constructor'", "'destructor'", "'class'", "'Array'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Null'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'==.'", "'+.'", "'new'", "'('", 
            "')'", "'['", "']'", "'.'", "'..'", "','", "';'", "':'", "'::'", 
            "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOR", 
            "VAR", "VAL", "SELF", "RETURN", "IN", "BY", "CONSTRUCTOR", "DESTRUCTOR", 
            "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", "STRING", "NULL", 
            "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", "FLOAT_LITERAL", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", "STRING_EQUAL", 
            "STRING_ADD", "NEW", "LP", "RP", "LSB", "RSB", "DOT", "DOUBLE_DOT", 
            "COMMA", "SEMI", "COLON", "DOUBLE_COLON", "LCB", "RCB", "ID", 
            "DOLLAR_ID", "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "COMMENT_CHAR", "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", 
                  "BIN_INTEGER_LITERAL", "HEX_INTEGER_LITERAL", "STRING_CHAR", 
                  "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", 
                  "SIGN", "FLOAT_INTEGER_PART", "FLOAT_DECIMAL_PART", "FLOAT_EXPONENT_PART", 
                  "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOR", "TRUE", "FALSE", "VAR", "VAL", "SELF", "RETURN", 
                  "IN", "BY", "CONSTRUCTOR", "DESTRUCTOR", "CLASS", "ARRAY", 
                  "INT", "FLOAT", "BOOLEAN", "STRING", "NULL", "INTEGER_LITERAL", 
                  "STRING_LITERAL", "BOOLEAN_LITERAL", "FLOAT_LITERAL", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", 
                  "STRING_EQUAL", "STRING_ADD", "NEW", "LP", "RP", "LSB", 
                  "RSB", "DOT", "DOUBLE_DOT", "COMMA", "SEMI", "COLON", 
                  "DOUBLE_COLON", "LCB", "RCB", "ID", "DOLLAR_ID", "WS", 
                  "UNTERMINATED_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_TOKEN" ]

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
            actions[38] = self.INTEGER_LITERAL_action 
            actions[39] = self.STRING_LITERAL_action 
            actions[41] = self.FLOAT_LITERAL_action 
            actions[75] = self.UNTERMINATED_COMMENT_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            actions[78] = self.ERROR_TOKEN_action 
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

     


