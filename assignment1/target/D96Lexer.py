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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u023f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\5\2\u00a3\n\2\3\3\3\3")
        buf.write("\7\3\u00a7\n\3\f\3\16\3\u00aa\13\3\3\3\7\3\u00ad\n\3\f")
        buf.write("\3\16\3\u00b0\13\3\3\3\5\3\u00b3\n\3\3\4\3\4\6\4\u00b7")
        buf.write("\n\4\r\4\16\4\u00b8\3\5\3\5\3\5\6\5\u00be\n\5\r\5\16\5")
        buf.write("\u00bf\3\6\3\6\3\6\6\6\u00c5\n\6\r\6\16\6\u00c6\3\7\3")
        buf.write("\7\3\7\5\7\u00cc\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u00d8\n\n\3\13\3\13\3\f\3\f\7\f\u00de\n\f\f")
        buf.write("\f\16\f\u00e1\13\f\3\f\7\f\u00e4\n\f\f\f\16\f\u00e7\13")
        buf.write("\f\3\r\3\r\5\r\u00eb\n\r\3\16\3\16\5\16\u00ef\n\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\7\17\u00f7\n\17\f\17\16\17\u00fa")
        buf.write("\13\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\5(\u0195\n(\3(\3(\3)\3)\7)\u019b")
        buf.write("\n)\f)\16)\u019e\13)\3)\3)\3)\3*\3*\5*\u01a5\n*\3+\3+")
        buf.write("\3+\5+\u01aa\n+\3+\3+\3+\3+\3+\3+\5+\u01b2\n+\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\38\38\38\39\39\3:\3:\3:\3;\3;\3;\3;\3")
        buf.write("<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3B\3C\3C\3")
        buf.write("D\3D\3E\3E\3F\3F\3F\3G\3G\3H\3H\3I\3I\7I\u01fd\nI\fI\16")
        buf.write("I\u0200\13I\3J\3J\3J\7J\u0205\nJ\fJ\16J\u0208\13J\3K\6")
        buf.write("K\u020b\nK\rK\16K\u020c\3K\3K\3L\3L\3L\3L\7L\u0215\nL")
        buf.write("\fL\16L\u0218\13L\3L\3L\3L\3L\3L\7L\u021f\nL\fL\16L\u0222")
        buf.write("\13L\3L\3L\5L\u0226\nL\3L\3L\3M\3M\7M\u022c\nM\fM\16M")
        buf.write("\u022f\13M\3M\3M\3N\3N\7N\u0235\nN\fN\16N\u0238\13N\3")
        buf.write("N\3N\3N\3O\3O\3O\2\2P\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21")
        buf.write("\2\23\2\25\2\27\2\31\2\33\2\35\3\37\4!\5#\6%\7\'\b)\t")
        buf.write("+\2-\2/\n\61\13\63\f\65\r\67\169\17;\20=\21?\22A\23C\24")
        buf.write("E\25G\26I\27K\30M\31O\32Q\33S\34U\35W\36Y\37[ ]!_\"a#")
        buf.write("c$e%g&i\'k(m)o*q+s,u-w.y/{\60}\61\177\62\u0081\63\u0083")
        buf.write("\64\u0085\65\u0087\66\u0089\67\u008b8\u008d9\u008f:\u0091")
        buf.write(";\u0093<\u0095=\u0097>\u0099?\u009b@\u009dA\3\2\22\3\2")
        buf.write("%%\3\2\63;\3\2\62;\3\2\629\4\2DDdd\3\2\62\63\4\2ZZzz\5")
        buf.write("\2\62;CHch\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv\3\2$")
        buf.write("$\4\2--//\4\2GGgg\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16")
        buf.write("\17\"\"\2\u024e\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\3\u00a2")
        buf.write("\3\2\2\2\5\u00b2\3\2\2\2\7\u00b4\3\2\2\2\t\u00ba\3\2\2")
        buf.write("\2\13\u00c1\3\2\2\2\r\u00cb\3\2\2\2\17\u00cd\3\2\2\2\21")
        buf.write("\u00d0\3\2\2\2\23\u00d7\3\2\2\2\25\u00d9\3\2\2\2\27\u00db")
        buf.write("\3\2\2\2\31\u00e8\3\2\2\2\33\u00ec\3\2\2\2\35\u00f2\3")
        buf.write("\2\2\2\37\u0100\3\2\2\2!\u0106\3\2\2\2#\u010f\3\2\2\2")
        buf.write("%\u0112\3\2\2\2\'\u0119\3\2\2\2)\u011e\3\2\2\2+\u0126")
        buf.write("\3\2\2\2-\u012b\3\2\2\2/\u0131\3\2\2\2\61\u0135\3\2\2")
        buf.write("\2\63\u0139\3\2\2\2\65\u013e\3\2\2\2\67\u0145\3\2\2\2")
        buf.write("9\u0148\3\2\2\2;\u014b\3\2\2\2=\u014f\3\2\2\2?\u015b\3")
        buf.write("\2\2\2A\u0166\3\2\2\2C\u016b\3\2\2\2E\u0171\3\2\2\2G\u0177")
        buf.write("\3\2\2\2I\u017b\3\2\2\2K\u0181\3\2\2\2M\u0189\3\2\2\2")
        buf.write("O\u0194\3\2\2\2Q\u0198\3\2\2\2S\u01a4\3\2\2\2U\u01b1\3")
        buf.write("\2\2\2W\u01b5\3\2\2\2Y\u01b7\3\2\2\2[\u01b9\3\2\2\2]\u01bb")
        buf.write("\3\2\2\2_\u01bd\3\2\2\2a\u01bf\3\2\2\2c\u01c1\3\2\2\2")
        buf.write("e\u01c4\3\2\2\2g\u01c7\3\2\2\2i\u01ca\3\2\2\2k\u01cc\3")
        buf.write("\2\2\2m\u01cf\3\2\2\2o\u01d1\3\2\2\2q\u01d4\3\2\2\2s\u01d6")
        buf.write("\3\2\2\2u\u01d9\3\2\2\2w\u01dd\3\2\2\2y\u01e0\3\2\2\2")
        buf.write("{\u01e2\3\2\2\2}\u01e4\3\2\2\2\177\u01e6\3\2\2\2\u0081")
        buf.write("\u01e8\3\2\2\2\u0083\u01ea\3\2\2\2\u0085\u01ed\3\2\2\2")
        buf.write("\u0087\u01ef\3\2\2\2\u0089\u01f1\3\2\2\2\u008b\u01f3\3")
        buf.write("\2\2\2\u008d\u01f6\3\2\2\2\u008f\u01f8\3\2\2\2\u0091\u01fa")
        buf.write("\3\2\2\2\u0093\u0201\3\2\2\2\u0095\u020a\3\2\2\2\u0097")
        buf.write("\u0225\3\2\2\2\u0099\u0229\3\2\2\2\u009b\u0232\3\2\2\2")
        buf.write("\u009d\u023c\3\2\2\2\u009f\u00a3\n\2\2\2\u00a0\u00a1\7")
        buf.write("%\2\2\u00a1\u00a3\n\2\2\2\u00a2\u009f\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a3\4\3\2\2\2\u00a4\u00ae\t\3\2\2\u00a5\u00a7")
        buf.write("\7a\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00ab\u00ad\t\4\2\2\u00ac\u00a8\3")
        buf.write("\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b3\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1")
        buf.write("\u00b3\7\62\2\2\u00b2\u00a4\3\2\2\2\u00b2\u00b1\3\2\2")
        buf.write("\2\u00b3\6\3\2\2\2\u00b4\u00b6\7\62\2\2\u00b5\u00b7\t")
        buf.write("\5\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\b\3\2\2\2\u00ba\u00bb")
        buf.write("\7\62\2\2\u00bb\u00bd\t\6\2\2\u00bc\u00be\t\7\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\n\3\2\2\2\u00c1\u00c2\7\62")
        buf.write("\2\2\u00c2\u00c4\t\b\2\2\u00c3\u00c5\t\t\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\f\3\2\2\2\u00c8\u00cc\n\n\2\2\u00c9")
        buf.write("\u00cc\5\17\b\2\u00ca\u00cc\5\21\t\2\u00cb\u00c8\3\2\2")
        buf.write("\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\16\3")
        buf.write("\2\2\2\u00cd\u00ce\7^\2\2\u00ce\u00cf\t\13\2\2\u00cf\20")
        buf.write("\3\2\2\2\u00d0\u00d1\7)\2\2\u00d1\u00d2\7$\2\2\u00d2\22")
        buf.write("\3\2\2\2\u00d3\u00d4\7^\2\2\u00d4\u00d8\n\13\2\2\u00d5")
        buf.write("\u00d6\7)\2\2\u00d6\u00d8\n\f\2\2\u00d7\u00d3\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d8\24\3\2\2\2\u00d9\u00da\t\r")
        buf.write("\2\2\u00da\26\3\2\2\2\u00db\u00e5\t\4\2\2\u00dc\u00de")
        buf.write("\7a\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e2\3\2\2\2")
        buf.write("\u00e1\u00df\3\2\2\2\u00e2\u00e4\t\4\2\2\u00e3\u00df\3")
        buf.write("\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\30\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00ea")
        buf.write("\7\60\2\2\u00e9\u00eb\5\27\f\2\u00ea\u00e9\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\32\3\2\2\2\u00ec\u00ee\t\16\2\2\u00ed")
        buf.write("\u00ef\5\25\13\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2")
        buf.write("\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\5\27\f\2\u00f1\34\3")
        buf.write("\2\2\2\u00f2\u00f3\7%\2\2\u00f3\u00f4\7%\2\2\u00f4\u00f8")
        buf.write("\3\2\2\2\u00f5\u00f7\5\3\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fc\7")
        buf.write("%\2\2\u00fc\u00fd\7%\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff")
        buf.write("\b\17\2\2\u00ff\36\3\2\2\2\u0100\u0101\7D\2\2\u0101\u0102")
        buf.write("\7t\2\2\u0102\u0103\7g\2\2\u0103\u0104\7c\2\2\u0104\u0105")
        buf.write("\7m\2\2\u0105 \3\2\2\2\u0106\u0107\7E\2\2\u0107\u0108")
        buf.write("\7q\2\2\u0108\u0109\7p\2\2\u0109\u010a\7v\2\2\u010a\u010b")
        buf.write("\7k\2\2\u010b\u010c\7p\2\2\u010c\u010d\7w\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e\"\3\2\2\2\u010f\u0110\7K\2\2\u0110\u0111")
        buf.write("\7h\2\2\u0111$\3\2\2\2\u0112\u0113\7G\2\2\u0113\u0114")
        buf.write("\7n\2\2\u0114\u0115\7u\2\2\u0115\u0116\7g\2\2\u0116\u0117")
        buf.write("\7k\2\2\u0117\u0118\7h\2\2\u0118&\3\2\2\2\u0119\u011a")
        buf.write("\7G\2\2\u011a\u011b\7n\2\2\u011b\u011c\7u\2\2\u011c\u011d")
        buf.write("\7g\2\2\u011d(\3\2\2\2\u011e\u011f\7H\2\2\u011f\u0120")
        buf.write("\7q\2\2\u0120\u0121\7t\2\2\u0121\u0122\7g\2\2\u0122\u0123")
        buf.write("\7c\2\2\u0123\u0124\7e\2\2\u0124\u0125\7j\2\2\u0125*\3")
        buf.write("\2\2\2\u0126\u0127\7V\2\2\u0127\u0128\7t\2\2\u0128\u0129")
        buf.write("\7w\2\2\u0129\u012a\7g\2\2\u012a,\3\2\2\2\u012b\u012c")
        buf.write("\7H\2\2\u012c\u012d\7c\2\2\u012d\u012e\7n\2\2\u012e\u012f")
        buf.write("\7u\2\2\u012f\u0130\7g\2\2\u0130.\3\2\2\2\u0131\u0132")
        buf.write("\7X\2\2\u0132\u0133\7c\2\2\u0133\u0134\7t\2\2\u0134\60")
        buf.write("\3\2\2\2\u0135\u0136\7X\2\2\u0136\u0137\7c\2\2\u0137\u0138")
        buf.write("\7n\2\2\u0138\62\3\2\2\2\u0139\u013a\7U\2\2\u013a\u013b")
        buf.write("\7g\2\2\u013b\u013c\7n\2\2\u013c\u013d\7h\2\2\u013d\64")
        buf.write("\3\2\2\2\u013e\u013f\7T\2\2\u013f\u0140\7g\2\2\u0140\u0141")
        buf.write("\7v\2\2\u0141\u0142\7w\2\2\u0142\u0143\7t\2\2\u0143\u0144")
        buf.write("\7p\2\2\u0144\66\3\2\2\2\u0145\u0146\7K\2\2\u0146\u0147")
        buf.write("\7p\2\2\u01478\3\2\2\2\u0148\u0149\7D\2\2\u0149\u014a")
        buf.write("\7{\2\2\u014a:\3\2\2\2\u014b\u014c\7P\2\2\u014c\u014d")
        buf.write("\7g\2\2\u014d\u014e\7y\2\2\u014e<\3\2\2\2\u014f\u0150")
        buf.write("\7E\2\2\u0150\u0151\7q\2\2\u0151\u0152\7p\2\2\u0152\u0153")
        buf.write("\7u\2\2\u0153\u0154\7v\2\2\u0154\u0155\7t\2\2\u0155\u0156")
        buf.write("\7w\2\2\u0156\u0157\7e\2\2\u0157\u0158\7v\2\2\u0158\u0159")
        buf.write("\7q\2\2\u0159\u015a\7t\2\2\u015a>\3\2\2\2\u015b\u015c")
        buf.write("\7F\2\2\u015c\u015d\7g\2\2\u015d\u015e\7u\2\2\u015e\u015f")
        buf.write("\7v\2\2\u015f\u0160\7t\2\2\u0160\u0161\7w\2\2\u0161\u0162")
        buf.write("\7e\2\2\u0162\u0163\7v\2\2\u0163\u0164\7q\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165@\3\2\2\2\u0166\u0167\7P\2\2\u0167\u0168")
        buf.write("\7w\2\2\u0168\u0169\7n\2\2\u0169\u016a\7n\2\2\u016aB\3")
        buf.write("\2\2\2\u016b\u016c\7E\2\2\u016c\u016d\7n\2\2\u016d\u016e")
        buf.write("\7c\2\2\u016e\u016f\7u\2\2\u016f\u0170\7u\2\2\u0170D\3")
        buf.write("\2\2\2\u0171\u0172\7C\2\2\u0172\u0173\7t\2\2\u0173\u0174")
        buf.write("\7t\2\2\u0174\u0175\7c\2\2\u0175\u0176\7{\2\2\u0176F\3")
        buf.write("\2\2\2\u0177\u0178\7K\2\2\u0178\u0179\7p\2\2\u0179\u017a")
        buf.write("\7v\2\2\u017aH\3\2\2\2\u017b\u017c\7H\2\2\u017c\u017d")
        buf.write("\7n\2\2\u017d\u017e\7q\2\2\u017e\u017f\7c\2\2\u017f\u0180")
        buf.write("\7v\2\2\u0180J\3\2\2\2\u0181\u0182\7D\2\2\u0182\u0183")
        buf.write("\7q\2\2\u0183\u0184\7q\2\2\u0184\u0185\7n\2\2\u0185\u0186")
        buf.write("\7g\2\2\u0186\u0187\7c\2\2\u0187\u0188\7p\2\2\u0188L\3")
        buf.write("\2\2\2\u0189\u018a\7U\2\2\u018a\u018b\7v\2\2\u018b\u018c")
        buf.write("\7t\2\2\u018c\u018d\7k\2\2\u018d\u018e\7p\2\2\u018e\u018f")
        buf.write("\7i\2\2\u018fN\3\2\2\2\u0190\u0195\5\5\3\2\u0191\u0195")
        buf.write("\5\7\4\2\u0192\u0195\5\13\6\2\u0193\u0195\5\t\5\2\u0194")
        buf.write("\u0190\3\2\2\2\u0194\u0191\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\b")
        buf.write("(\3\2\u0197P\3\2\2\2\u0198\u019c\7$\2\2\u0199\u019b\5")
        buf.write("\r\7\2\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019f\u01a0\7$\2\2\u01a0\u01a1\b)\4\2\u01a1")
        buf.write("R\3\2\2\2\u01a2\u01a5\5+\26\2\u01a3\u01a5\5-\27\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5T\3\2\2\2\u01a6")
        buf.write("\u01a7\5\27\f\2\u01a7\u01a9\5\31\r\2\u01a8\u01aa\5\33")
        buf.write("\16\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01b2")
        buf.write("\3\2\2\2\u01ab\u01ac\5\27\f\2\u01ac\u01ad\5\33\16\2\u01ad")
        buf.write("\u01b2\3\2\2\2\u01ae\u01af\5\31\r\2\u01af\u01b0\5\33\16")
        buf.write("\2\u01b0\u01b2\3\2\2\2\u01b1\u01a6\3\2\2\2\u01b1\u01ab")
        buf.write("\3\2\2\2\u01b1\u01ae\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b4\b+\5\2\u01b4V\3\2\2\2\u01b5\u01b6\7-\2\2\u01b6")
        buf.write("X\3\2\2\2\u01b7\u01b8\7/\2\2\u01b8Z\3\2\2\2\u01b9\u01ba")
        buf.write("\7,\2\2\u01ba\\\3\2\2\2\u01bb\u01bc\7\61\2\2\u01bc^\3")
        buf.write("\2\2\2\u01bd\u01be\7\'\2\2\u01be`\3\2\2\2\u01bf\u01c0")
        buf.write("\7#\2\2\u01c0b\3\2\2\2\u01c1\u01c2\7(\2\2\u01c2\u01c3")
        buf.write("\7(\2\2\u01c3d\3\2\2\2\u01c4\u01c5\7~\2\2\u01c5\u01c6")
        buf.write("\7~\2\2\u01c6f\3\2\2\2\u01c7\u01c8\7?\2\2\u01c8\u01c9")
        buf.write("\7?\2\2\u01c9h\3\2\2\2\u01ca\u01cb\7?\2\2\u01cbj\3\2\2")
        buf.write("\2\u01cc\u01cd\7#\2\2\u01cd\u01ce\7?\2\2\u01cel\3\2\2")
        buf.write("\2\u01cf\u01d0\7>\2\2\u01d0n\3\2\2\2\u01d1\u01d2\7>\2")
        buf.write("\2\u01d2\u01d3\7?\2\2\u01d3p\3\2\2\2\u01d4\u01d5\7@\2")
        buf.write("\2\u01d5r\3\2\2\2\u01d6\u01d7\7@\2\2\u01d7\u01d8\7?\2")
        buf.write("\2\u01d8t\3\2\2\2\u01d9\u01da\7?\2\2\u01da\u01db\7?\2")
        buf.write("\2\u01db\u01dc\7\60\2\2\u01dcv\3\2\2\2\u01dd\u01de\7-")
        buf.write("\2\2\u01de\u01df\7\60\2\2\u01dfx\3\2\2\2\u01e0\u01e1\7")
        buf.write("*\2\2\u01e1z\3\2\2\2\u01e2\u01e3\7+\2\2\u01e3|\3\2\2\2")
        buf.write("\u01e4\u01e5\7]\2\2\u01e5~\3\2\2\2\u01e6\u01e7\7_\2\2")
        buf.write("\u01e7\u0080\3\2\2\2\u01e8\u01e9\7\60\2\2\u01e9\u0082")
        buf.write("\3\2\2\2\u01ea\u01eb\7\60\2\2\u01eb\u01ec\7\60\2\2\u01ec")
        buf.write("\u0084\3\2\2\2\u01ed\u01ee\7.\2\2\u01ee\u0086\3\2\2\2")
        buf.write("\u01ef\u01f0\7=\2\2\u01f0\u0088\3\2\2\2\u01f1\u01f2\7")
        buf.write("<\2\2\u01f2\u008a\3\2\2\2\u01f3\u01f4\7<\2\2\u01f4\u01f5")
        buf.write("\7<\2\2\u01f5\u008c\3\2\2\2\u01f6\u01f7\7}\2\2\u01f7\u008e")
        buf.write("\3\2\2\2\u01f8\u01f9\7\177\2\2\u01f9\u0090\3\2\2\2\u01fa")
        buf.write("\u01fe\t\17\2\2\u01fb\u01fd\t\20\2\2\u01fc\u01fb\3\2\2")
        buf.write("\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff")
        buf.write("\3\2\2\2\u01ff\u0092\3\2\2\2\u0200\u01fe\3\2\2\2\u0201")
        buf.write("\u0202\7&\2\2\u0202\u0206\t\17\2\2\u0203\u0205\t\20\2")
        buf.write("\2\u0204\u0203\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0204")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0094\3\2\2\2\u0208")
        buf.write("\u0206\3\2\2\2\u0209\u020b\t\21\2\2\u020a\u0209\3\2\2")
        buf.write("\2\u020b\u020c\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\bK\2\2\u020f")
        buf.write("\u0096\3\2\2\2\u0210\u0211\7%\2\2\u0211\u0212\7%\2\2\u0212")
        buf.write("\u0216\3\2\2\2\u0213\u0215\5\3\2\2\u0214\u0213\3\2\2\2")
        buf.write("\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3")
        buf.write("\2\2\2\u0217\u0219\3\2\2\2\u0218\u0216\3\2\2\2\u0219\u0226")
        buf.write("\7\2\2\3\u021a\u021b\7%\2\2\u021b\u021c\7%\2\2\u021c\u0220")
        buf.write("\3\2\2\2\u021d\u021f\n\2\2\2\u021e\u021d\3\2\2\2\u021f")
        buf.write("\u0222\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2")
        buf.write("\u0221\u0223\3\2\2\2\u0222\u0220\3\2\2\2\u0223\u0224\7")
        buf.write("%\2\2\u0224\u0226\7\2\2\3\u0225\u0210\3\2\2\2\u0225\u021a")
        buf.write("\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0228\bL\6\2\u0228")
        buf.write("\u0098\3\2\2\2\u0229\u022d\7$\2\2\u022a\u022c\5\r\7\2")
        buf.write("\u022b\u022a\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3")
        buf.write("\2\2\2\u022d\u022e\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u022d")
        buf.write("\3\2\2\2\u0230\u0231\bM\7\2\u0231\u009a\3\2\2\2\u0232")
        buf.write("\u0236\7$\2\2\u0233\u0235\5\r\7\2\u0234\u0233\3\2\2\2")
        buf.write("\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3")
        buf.write("\2\2\2\u0237\u0239\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a")
        buf.write("\5\23\n\2\u023a\u023b\bN\b\2\u023b\u009c\3\2\2\2\u023c")
        buf.write("\u023d\13\2\2\2\u023d\u023e\bO\t\2\u023e\u009e\3\2\2\2")
        buf.write("\36\2\u00a2\u00a8\u00ae\u00b2\u00b8\u00bf\u00c6\u00cb")
        buf.write("\u00d7\u00df\u00e5\u00ea\u00ee\u00f8\u0194\u019c\u01a4")
        buf.write("\u01a9\u01b1\u01fe\u0206\u020c\u0216\u0220\u0225\u022d")
        buf.write("\u0236\n\b\2\2\3(\2\3)\3\3+\4\3L\5\3M\6\3N\7\3O\b")
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
    UNTERMINATED_COMMENT = 60
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
            "BOOLEAN", "STRING", "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
            "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", 
            "STRING_EQUAL", "STRING_ADD", "LP", "RP", "LSB", "RSB", "DOT", 
            "DOUBLE_DOT", "COMMA", "SEMI", "COLON", "DOUBLE_COLON", "LCB", 
            "RCB", "ID", "DOLLAR_ID", "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "COMMENT_CHAR", "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", 
                  "BIN_INTEGER_LITERAL", "HEX_INTEGER_LITERAL", "STRING_CHAR", 
                  "ESCAPE_SEQUENCE", "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", 
                  "SIGN", "FLOAT_INTEGER_PART", "FLOAT_DECIMAL_PART", "FLOAT_EXPONENT_PART", 
                  "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "VAR", "VAL", "SELF", "RETURN", 
                  "IN", "BY", "NEW", "CONSTRUCTOR", "DESTRUCTOR", "NULL", 
                  "CLASS", "ARRAY", "INTEGER", "FLOAT", "BOOLEAN", "STRING", 
                  "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                  "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", 
                  "GT", "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", 
                  "LSB", "RSB", "DOT", "DOUBLE_DOT", "COMMA", "SEMI", "COLON", 
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
            actions[74] = self.UNTERMINATED_COMMENT_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            actions[77] = self.ERROR_TOKEN_action 
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

     


