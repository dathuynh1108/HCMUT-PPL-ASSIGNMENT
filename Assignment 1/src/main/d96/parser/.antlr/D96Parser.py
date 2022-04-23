# Generated from d:\Workspace\PPL\Assignment\Assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u023a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\6\2x\n\2\r\2\16\2y\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0082")
        buf.write("\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u008e")
        buf.write("\n\5\f\5\16\5\u0091\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u0099")
        buf.write("\n\6\f\6\16\6\u009c\13\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5")
        buf.write("\7\u00a5\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00ae\n\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00b6\n\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u00c3\n\f\f\f\16")
        buf.write("\f\u00c6\13\f\3\r\3\r\3\r\7\r\u00cb\n\r\f\r\16\r\u00ce")
        buf.write("\13\r\3\r\3\r\3\r\3\16\3\16\3\16\5\16\u00d6\n\16\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\5\20\u00de\n\20\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\5\22\u00e8\n\22\3\23\3\23")
        buf.write("\3\24\3\24\5\24\u00ee\n\24\3\25\3\25\3\25\5\25\u00f3\n")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\7\26\u00fa\n\26\f\26\16\26")
        buf.write("\u00fd\13\26\3\27\3\27\3\27\5\27\u0102\n\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\7\30\u0109\n\30\f\30\16\30\u010c\13\30")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u0115\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u011c\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\7\34\u0124\n\34\f\34\16\34\u0127\13\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u012f\n\35\f\35\16")
        buf.write("\35\u0132\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u013a")
        buf.write("\n\36\f\36\16\36\u013d\13\36\3\37\3\37\3\37\5\37\u0142")
        buf.write("\n\37\3 \3 \3 \5 \u0147\n \3!\3!\3!\3!\3!\3!\3!\3!\7!")
        buf.write("\u0151\n!\f!\16!\u0154\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\5\"\u015e\n\"\3\"\3\"\3\"\3\"\7\"\u0164\n\"\f\"\16")
        buf.write("\"\u0167\13\"\3#\3#\3#\3#\3#\5#\u016e\n#\3#\3#\3#\3#\3")
        buf.write("#\5#\u0175\n#\3$\3$\3$\3$\5$\u017b\n$\3$\3$\5$\u017f\n")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0189\n%\3&\3&\3&\3&\5&\u018f")
        buf.write("\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\7")
        buf.write("*\u01a0\n*\f*\16*\u01a3\13*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\5+\u01b0\n+\3,\3,\3,\3,\3,\3,\7,\u01b8\n,\f,\16")
        buf.write(",\u01bb\13,\3,\3,\3,\3,\3-\3-\3-\5-\u01c4\n-\3.\3.\3.")
        buf.write("\3.\3.\3.\3.\7.\u01cd\n.\f.\16.\u01d0\13.\3.\3.\3.\3/")
        buf.write("\3/\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\7")
        buf.write("\61\u01e2\n\61\f\61\16\61\u01e5\13\61\3\61\5\61\u01e8")
        buf.write("\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01fc\n")
        buf.write("\64\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\5\67\u020d\n\67\38\38\58\u0211")
        buf.write("\n8\38\38\39\39\39\39\39\59\u021a\n9\39\39\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\5:\u0226\n:\3:\3:\3:\3:\7:\u022c\n:\f:\16")
        buf.write(":\u022f\13:\3;\3;\3;\3;\3;\5;\u0236\n;\3;\3;\3;\2\b\66")
        buf.write("8:@Br<\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt\2\13\3\2")
        buf.write("\n\13\3\2<=\3\2\26\31\3\2\32\36\3\2./\4\2\'\')-\3\2%&")
        buf.write("\3\2\37 \3\2!#\2\u0241\2w\3\2\2\2\4}\3\2\2\2\6\u0087\3")
        buf.write("\2\2\2\b\u008f\3\2\2\2\n\u0092\3\2\2\2\f\u00a4\3\2\2\2")
        buf.write("\16\u00a6\3\2\2\2\20\u00aa\3\2\2\2\22\u00b2\3\2\2\2\24")
        buf.write("\u00ba\3\2\2\2\26\u00bf\3\2\2\2\30\u00c7\3\2\2\2\32\u00d5")
        buf.write("\3\2\2\2\34\u00d7\3\2\2\2\36\u00d9\3\2\2\2 \u00e3\3\2")
        buf.write("\2\2\"\u00e7\3\2\2\2$\u00e9\3\2\2\2&\u00ed\3\2\2\2(\u00ef")
        buf.write("\3\2\2\2*\u00f6\3\2\2\2,\u00fe\3\2\2\2.\u0105\3\2\2\2")
        buf.write("\60\u010d\3\2\2\2\62\u0114\3\2\2\2\64\u011b\3\2\2\2\66")
        buf.write("\u011d\3\2\2\28\u0128\3\2\2\2:\u0133\3\2\2\2<\u0141\3")
        buf.write("\2\2\2>\u0146\3\2\2\2@\u0148\3\2\2\2B\u0155\3\2\2\2D\u0174")
        buf.write("\3\2\2\2F\u017e\3\2\2\2H\u0188\3\2\2\2J\u018e\3\2\2\2")
        buf.write("L\u0190\3\2\2\2N\u0194\3\2\2\2P\u0198\3\2\2\2R\u019d\3")
        buf.write("\2\2\2T\u01af\3\2\2\2V\u01b1\3\2\2\2X\u01c3\3\2\2\2Z\u01c5")
        buf.write("\3\2\2\2\\\u01d4\3\2\2\2^\u01d9\3\2\2\2`\u01db\3\2\2\2")
        buf.write("b\u01e9\3\2\2\2d\u01ef\3\2\2\2f\u01f2\3\2\2\2h\u0200\3")
        buf.write("\2\2\2j\u0203\3\2\2\2l\u020c\3\2\2\2n\u0210\3\2\2\2p\u0214")
        buf.write("\3\2\2\2r\u021d\3\2\2\2t\u0230\3\2\2\2vx\5\4\3\2wv\3\2")
        buf.write("\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z{\3\2\2\2{|\7\2\2\3")
        buf.write("|\3\3\2\2\2}~\7\24\2\2~\u0081\5\6\4\2\177\u0080\78\2\2")
        buf.write("\u0080\u0082\5\6\4\2\u0081\177\3\2\2\2\u0081\u0082\3\2")
        buf.write("\2\2\u0082\u0083\3\2\2\2\u0083\u0084\7:\2\2\u0084\u0085")
        buf.write("\5\b\5\2\u0085\u0086\7;\2\2\u0086\5\3\2\2\2\u0087\u0088")
        buf.write("\7<\2\2\u0088\7\3\2\2\2\u0089\u008e\5\n\6\2\u008a\u008e")
        buf.write("\5\20\t\2\u008b\u008e\5\22\n\2\u008c\u008e\5\24\13\2\u008d")
        buf.write("\u0089\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3")
        buf.write("\2\2\2\u008f\u0090\3\2\2\2\u0090\t\3\2\2\2\u0091\u008f")
        buf.write("\3\2\2\2\u0092\u0093\t\2\2\2\u0093\u0094\t\3\2\2\u0094")
        buf.write("\u009a\b\6\1\2\u0095\u0096\7\66\2\2\u0096\u0097\t\3\2")
        buf.write("\2\u0097\u0099\b\6\1\2\u0098\u0095\3\2\2\2\u0099\u009c")
        buf.write("\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009e\78\2\2")
        buf.write("\u009e\u009f\5\32\16\2\u009f\u00a0\5\f\7\2\u00a0\13\3")
        buf.write("\2\2\2\u00a1\u00a2\7(\2\2\u00a2\u00a5\5\16\b\2\u00a3\u00a5")
        buf.write("\7\67\2\2\u00a4\u00a1\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\r\3\2\2\2\u00a6\u00a7\5\60\31\2\u00a7\u00a8\7\66\2\2")
        buf.write("\u00a8\u00a9\5\60\31\2\u00a9\17\3\2\2\2\u00aa\u00ab\t")
        buf.write("\3\2\2\u00ab\u00ad\7\60\2\2\u00ac\u00ae\5\26\f\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b0\7\61\2\2\u00b0\u00b1\5R*\2\u00b1\21\3\2\2")
        buf.write("\2\u00b2\u00b3\7\21\2\2\u00b3\u00b5\7\60\2\2\u00b4\u00b6")
        buf.write("\5\26\f\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00b8\7\61\2\2\u00b8\u00b9\5R*\2")
        buf.write("\u00b9\23\3\2\2\2\u00ba\u00bb\7\22\2\2\u00bb\u00bc\7\60")
        buf.write("\2\2\u00bc\u00bd\7\61\2\2\u00bd\u00be\5R*\2\u00be\25\3")
        buf.write("\2\2\2\u00bf\u00c4\5\30\r\2\u00c0\u00c1\7\67\2\2\u00c1")
        buf.write("\u00c3\5\30\r\2\u00c2\u00c0\3\2\2\2\u00c3\u00c6\3\2\2")
        buf.write("\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\27\3")
        buf.write("\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00cc\7<\2\2\u00c8\u00c9")
        buf.write("\7\66\2\2\u00c9\u00cb\7<\2\2\u00ca\u00c8\3\2\2\2\u00cb")
        buf.write("\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7")
        buf.write("8\2\2\u00d0\u00d1\5\32\16\2\u00d1\31\3\2\2\2\u00d2\u00d6")
        buf.write("\5\34\17\2\u00d3\u00d6\5\36\20\2\u00d4\u00d6\5 \21\2\u00d5")
        buf.write("\u00d2\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2")
        buf.write("\u00d6\33\3\2\2\2\u00d7\u00d8\t\4\2\2\u00d8\35\3\2\2\2")
        buf.write("\u00d9\u00da\7\25\2\2\u00da\u00dd\7\62\2\2\u00db\u00de")
        buf.write("\5\34\17\2\u00dc\u00de\5\36\20\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\7\66\2")
        buf.write("\2\u00e0\u00e1\7\33\2\2\u00e1\u00e2\7\63\2\2\u00e2\37")
        buf.write("\3\2\2\2\u00e3\u00e4\7<\2\2\u00e4!\3\2\2\2\u00e5\u00e8")
        buf.write("\5&\24\2\u00e6\u00e8\5$\23\2\u00e7\u00e5\3\2\2\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e8#\3\2\2\2\u00e9\u00ea\t\5\2\2\u00ea")
        buf.write("%\3\2\2\2\u00eb\u00ee\5,\27\2\u00ec\u00ee\5(\25\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\'\3\2\2\2\u00ef")
        buf.write("\u00f0\7\25\2\2\u00f0\u00f2\7\60\2\2\u00f1\u00f3\5*\26")
        buf.write("\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\7\61\2\2\u00f5)\3\2\2\2\u00f6\u00fb")
        buf.write("\5&\24\2\u00f7\u00f8\7\66\2\2\u00f8\u00fa\5&\24\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fc\3\2\2\2\u00fc+\3\2\2\2\u00fd\u00fb\3\2\2")
        buf.write("\2\u00fe\u00ff\7\25\2\2\u00ff\u0101\7\60\2\2\u0100\u0102")
        buf.write("\5.\30\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\u0104\7\61\2\2\u0104-\3\2\2\2\u0105")
        buf.write("\u010a\5\60\31\2\u0106\u0107\7\66\2\2\u0107\u0109\5\60")
        buf.write("\31\2\u0108\u0106\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010b/\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010d\u010e\5\62\32\2\u010e\61\3\2\2\2\u010f")
        buf.write("\u0110\5\64\33\2\u0110\u0111\t\6\2\2\u0111\u0112\5\64")
        buf.write("\33\2\u0112\u0115\3\2\2\2\u0113\u0115\5\64\33\2\u0114")
        buf.write("\u010f\3\2\2\2\u0114\u0113\3\2\2\2\u0115\63\3\2\2\2\u0116")
        buf.write("\u0117\5\66\34\2\u0117\u0118\t\7\2\2\u0118\u0119\5\66")
        buf.write("\34\2\u0119\u011c\3\2\2\2\u011a\u011c\5\66\34\2\u011b")
        buf.write("\u0116\3\2\2\2\u011b\u011a\3\2\2\2\u011c\65\3\2\2\2\u011d")
        buf.write("\u011e\b\34\1\2\u011e\u011f\58\35\2\u011f\u0125\3\2\2")
        buf.write("\2\u0120\u0121\f\4\2\2\u0121\u0122\t\b\2\2\u0122\u0124")
        buf.write("\58\35\2\u0123\u0120\3\2\2\2\u0124\u0127\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\67\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0128\u0129\b\35\1\2\u0129\u012a\5:\36")
        buf.write("\2\u012a\u0130\3\2\2\2\u012b\u012c\f\4\2\2\u012c\u012d")
        buf.write("\t\t\2\2\u012d\u012f\5:\36\2\u012e\u012b\3\2\2\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u01319\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0134\b\36\1")
        buf.write("\2\u0134\u0135\5<\37\2\u0135\u013b\3\2\2\2\u0136\u0137")
        buf.write("\f\4\2\2\u0137\u0138\t\n\2\2\u0138\u013a\5<\37\2\u0139")
        buf.write("\u0136\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c;\3\2\2\2\u013d\u013b\3\2\2")
        buf.write("\2\u013e\u013f\7$\2\2\u013f\u0142\5<\37\2\u0140\u0142")
        buf.write("\5> \2\u0141\u013e\3\2\2\2\u0141\u0140\3\2\2\2\u0142=")
        buf.write("\3\2\2\2\u0143\u0144\7 \2\2\u0144\u0147\5> \2\u0145\u0147")
        buf.write("\5@!\2\u0146\u0143\3\2\2\2\u0146\u0145\3\2\2\2\u0147?")
        buf.write("\3\2\2\2\u0148\u0149\b!\1\2\u0149\u014a\5B\"\2\u014a\u0152")
        buf.write("\3\2\2\2\u014b\u014c\f\4\2\2\u014c\u014d\7\62\2\2\u014d")
        buf.write("\u014e\5\60\31\2\u014e\u014f\7\63\2\2\u014f\u0151\3\2")
        buf.write("\2\2\u0150\u014b\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150")
        buf.write("\3\2\2\2\u0152\u0153\3\2\2\2\u0153A\3\2\2\2\u0154\u0152")
        buf.write("\3\2\2\2\u0155\u0156\b\"\1\2\u0156\u0157\5D#\2\u0157\u0165")
        buf.write("\3\2\2\2\u0158\u0159\f\5\2\2\u0159\u015a\7\64\2\2\u015a")
        buf.write("\u015b\7<\2\2\u015b\u015d\7\60\2\2\u015c\u015e\5.\30\2")
        buf.write("\u015d\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015f\u0164\7\61\2\2\u0160\u0161\f\4\2\2\u0161")
        buf.write("\u0162\7\64\2\2\u0162\u0164\7<\2\2\u0163\u0158\3\2\2\2")
        buf.write("\u0163\u0160\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0165\u0166\3\2\2\2\u0166C\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0168\u0169\7<\2\2\u0169\u016a\79\2\2\u016a\u016b")
        buf.write("\7=\2\2\u016b\u016d\7\60\2\2\u016c\u016e\5.\30\2\u016d")
        buf.write("\u016c\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0175\7\61\2\2\u0170\u0171\7<\2\2\u0171\u0172\7")
        buf.write("9\2\2\u0172\u0175\7=\2\2\u0173\u0175\5F$\2\u0174\u0168")
        buf.write("\3\2\2\2\u0174\u0170\3\2\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("E\3\2\2\2\u0176\u0177\7\20\2\2\u0177\u0178\7<\2\2\u0178")
        buf.write("\u017a\7\60\2\2\u0179\u017b\5.\30\2\u017a\u0179\3\2\2")
        buf.write("\2\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017f")
        buf.write("\7\61\2\2\u017d\u017f\5H%\2\u017e\u0176\3\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017fG\3\2\2\2\u0180\u0189\7<\2\2\u0181")
        buf.write("\u0189\7\f\2\2\u0182\u0189\5\"\22\2\u0183\u0189\7\23\2")
        buf.write("\2\u0184\u0185\7\60\2\2\u0185\u0186\5\60\31\2\u0186\u0187")
        buf.write("\7\61\2\2\u0187\u0189\3\2\2\2\u0188\u0180\3\2\2\2\u0188")
        buf.write("\u0181\3\2\2\2\u0188\u0182\3\2\2\2\u0188\u0183\3\2\2\2")
        buf.write("\u0188\u0184\3\2\2\2\u0189I\3\2\2\2\u018a\u018f\5L\'\2")
        buf.write("\u018b\u018f\5N(\2\u018c\u018f\5P)\2\u018d\u018f\7<\2")
        buf.write("\2\u018e\u018a\3\2\2\2\u018e\u018b\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018e\u018d\3\2\2\2\u018fK\3\2\2\2\u0190\u0191")
        buf.write("\5B\"\2\u0191\u0192\7\64\2\2\u0192\u0193\7<\2\2\u0193")
        buf.write("M\3\2\2\2\u0194\u0195\5\6\4\2\u0195\u0196\79\2\2\u0196")
        buf.write("\u0197\7=\2\2\u0197O\3\2\2\2\u0198\u0199\5@!\2\u0199\u019a")
        buf.write("\7\62\2\2\u019a\u019b\5\60\31\2\u019b\u019c\7\63\2\2\u019c")
        buf.write("Q\3\2\2\2\u019d\u01a1\7:\2\2\u019e\u01a0\5T+\2\u019f\u019e")
        buf.write("\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a4\u01a5\7;\2\2\u01a5S\3\2\2\2\u01a6\u01b0\5V,\2\u01a7")
        buf.write("\u01b0\5\\/\2\u01a8\u01b0\5`\61\2\u01a9\u01b0\5f\64\2")
        buf.write("\u01aa\u01b0\5h\65\2\u01ab\u01b0\5j\66\2\u01ac\u01b0\5")
        buf.write("l\67\2\u01ad\u01b0\5n8\2\u01ae\u01b0\5R*\2\u01af\u01a6")
        buf.write("\3\2\2\2\u01af\u01a7\3\2\2\2\u01af\u01a8\3\2\2\2\u01af")
        buf.write("\u01a9\3\2\2\2\u01af\u01aa\3\2\2\2\u01af\u01ab\3\2\2\2")
        buf.write("\u01af\u01ac\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01ae\3")
        buf.write("\2\2\2\u01b0U\3\2\2\2\u01b1\u01b2\t\2\2\2\u01b2\u01b3")
        buf.write("\7<\2\2\u01b3\u01b9\b,\1\2\u01b4\u01b5\7\66\2\2\u01b5")
        buf.write("\u01b6\7<\2\2\u01b6\u01b8\b,\1\2\u01b7\u01b4\3\2\2\2\u01b8")
        buf.write("\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2")
        buf.write("\u01ba\u01bc\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\7")
        buf.write("8\2\2\u01bd\u01be\5\32\16\2\u01be\u01bf\5X-\2\u01bfW\3")
        buf.write("\2\2\2\u01c0\u01c1\7(\2\2\u01c1\u01c4\5Z.\2\u01c2\u01c4")
        buf.write("\7\67\2\2\u01c3\u01c0\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("Y\3\2\2\2\u01c5\u01c6\5\60\31\2\u01c6\u01ce\b.\1\2\u01c7")
        buf.write("\u01c8\6.\b\3\u01c8\u01c9\7\66\2\2\u01c9\u01ca\5\60\31")
        buf.write("\2\u01ca\u01cb\b.\1\2\u01cb\u01cd\3\2\2\2\u01cc\u01c7")
        buf.write("\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d1\u01d2\6.\t\3\u01d2\u01d3\7\67\2\2\u01d3[\3\2\2")
        buf.write("\2\u01d4\u01d5\5^\60\2\u01d5\u01d6\7(\2\2\u01d6\u01d7")
        buf.write("\5\60\31\2\u01d7\u01d8\7\67\2\2\u01d8]\3\2\2\2\u01d9\u01da")
        buf.write("\5J&\2\u01da_\3\2\2\2\u01db\u01dc\7\6\2\2\u01dc\u01dd")
        buf.write("\7\60\2\2\u01dd\u01de\5\60\31\2\u01de\u01df\7\61\2\2\u01df")
        buf.write("\u01e3\5R*\2\u01e0\u01e2\5b\62\2\u01e1\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e8\5")
        buf.write("d\63\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8a")
        buf.write("\3\2\2\2\u01e9\u01ea\7\7\2\2\u01ea\u01eb\7\60\2\2\u01eb")
        buf.write("\u01ec\5\60\31\2\u01ec\u01ed\7\61\2\2\u01ed\u01ee\5R*")
        buf.write("\2\u01eec\3\2\2\2\u01ef\u01f0\7\b\2\2\u01f0\u01f1\5R*")
        buf.write("\2\u01f1e\3\2\2\2\u01f2\u01f3\7\t\2\2\u01f3\u01f4\7\60")
        buf.write("\2\2\u01f4\u01f5\5J&\2\u01f5\u01f6\7\16\2\2\u01f6\u01f7")
        buf.write("\5\60\31\2\u01f7\u01f8\7\65\2\2\u01f8\u01fb\5\60\31\2")
        buf.write("\u01f9\u01fa\7\17\2\2\u01fa\u01fc\5\60\31\2\u01fb\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd")
        buf.write("\u01fe\7\61\2\2\u01fe\u01ff\5R*\2\u01ffg\3\2\2\2\u0200")
        buf.write("\u0201\7\4\2\2\u0201\u0202\7\67\2\2\u0202i\3\2\2\2\u0203")
        buf.write("\u0204\7\5\2\2\u0204\u0205\7\67\2\2\u0205k\3\2\2\2\u0206")
        buf.write("\u0207\7\r\2\2\u0207\u0208\5\60\31\2\u0208\u0209\7\67")
        buf.write("\2\2\u0209\u020d\3\2\2\2\u020a\u020b\7\r\2\2\u020b\u020d")
        buf.write("\7\67\2\2\u020c\u0206\3\2\2\2\u020c\u020a\3\2\2\2\u020d")
        buf.write("m\3\2\2\2\u020e\u0211\5p9\2\u020f\u0211\5t;\2\u0210\u020e")
        buf.write("\3\2\2\2\u0210\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write("\u0213\7\67\2\2\u0213o\3\2\2\2\u0214\u0215\5r:\2\u0215")
        buf.write("\u0216\7\64\2\2\u0216\u0217\7<\2\2\u0217\u0219\7\60\2")
        buf.write("\2\u0218\u021a\5.\30\2\u0219\u0218\3\2\2\2\u0219\u021a")
        buf.write("\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c\7\61\2\2\u021c")
        buf.write("q\3\2\2\2\u021d\u021e\b:\1\2\u021e\u021f\5D#\2\u021f\u022d")
        buf.write("\3\2\2\2\u0220\u0221\f\5\2\2\u0221\u0222\7\64\2\2\u0222")
        buf.write("\u0223\7<\2\2\u0223\u0225\7\60\2\2\u0224\u0226\5.\30\2")
        buf.write("\u0225\u0224\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\3")
        buf.write("\2\2\2\u0227\u022c\7\61\2\2\u0228\u0229\f\4\2\2\u0229")
        buf.write("\u022a\7\64\2\2\u022a\u022c\7<\2\2\u022b\u0220\3\2\2\2")
        buf.write("\u022b\u0228\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3")
        buf.write("\2\2\2\u022d\u022e\3\2\2\2\u022es\3\2\2\2\u022f\u022d")
        buf.write("\3\2\2\2\u0230\u0231\5\6\4\2\u0231\u0232\79\2\2\u0232")
        buf.write("\u0233\7=\2\2\u0233\u0235\7\60\2\2\u0234\u0236\5.\30\2")
        buf.write("\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0237\3")
        buf.write("\2\2\2\u0237\u0238\7\61\2\2\u0238u\3\2\2\2\64y\u0081\u008d")
        buf.write("\u008f\u009a\u00a4\u00ad\u00b5\u00c4\u00cc\u00d5\u00dd")
        buf.write("\u00e7\u00ed\u00f2\u00fb\u0101\u010a\u0114\u011b\u0125")
        buf.write("\u0130\u013b\u0141\u0146\u0152\u015d\u0163\u0165\u016d")
        buf.write("\u0174\u017a\u017e\u0188\u018e\u01a1\u01af\u01b9\u01c3")
        buf.write("\u01ce\u01e3\u01e7\u01fb\u020c\u0210\u0219\u0225\u022b")
        buf.write("\u022d\u0235")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Var'", 
                     "'Val'", "'Self'", "'Return'", "'In'", "'By'", "'New'", 
                     "'Constructor'", "'Destructor'", "'Null'", "'Class'", 
                     "'Array'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'==.'", "'+.'", "'('", "')'", "'['", 
                     "']'", "'.'", "'..'", "','", "';'", "':'", "'::'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "VAR", "VAL", "SELF", 
                      "RETURN", "IN", "BY", "NEW", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NULL", "CLASS", "ARRAY", "INTEGER", "FLOAT", "BOOLEAN", 
                      "STRING", "ZERO_INTEGER", "INTEGER_LITERAL", "STRING_LITERAL", 
                      "BOOLEAN_LITERAL", "FLOAT_LITERAL", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
                      "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", "GTE", "STRING_EQUAL", 
                      "STRING_ADD", "LP", "RP", "LSB", "RSB", "DOT", "DOUBLE_DOT", 
                      "COMMA", "SEMI", "COLON", "DOUBLE_COLON", "LCB", "RCB", 
                      "ID", "DOLLAR_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_class_name = 2
    RULE_class_body = 3
    RULE_attribute_declaration = 4
    RULE_attribute_initialization = 5
    RULE_attribute_initialization_list = 6
    RULE_method_declaration = 7
    RULE_constructor_declaration = 8
    RULE_destructor_declaration = 9
    RULE_list_of_parameters = 10
    RULE_parameter_declaration = 11
    RULE_type_name = 12
    RULE_primitive_type = 13
    RULE_array_type = 14
    RULE_class_type = 15
    RULE_literal = 16
    RULE_primitive_literal = 17
    RULE_array_literal = 18
    RULE_multi_demensional_array = 19
    RULE_array_literal_list = 20
    RULE_indexed_array = 21
    RULE_list_of_expressions = 22
    RULE_expression = 23
    RULE_string_expression = 24
    RULE_relation_expression = 25
    RULE_logical_expression = 26
    RULE_adding_expression = 27
    RULE_multiplying_expression = 28
    RULE_negative_expression = 29
    RULE_sign_expression = 30
    RULE_index_expression = 31
    RULE_instance_access_expression = 32
    RULE_static_access_expression = 33
    RULE_object_creation_expression = 34
    RULE_operand = 35
    RULE_scalar_variable = 36
    RULE_scalar_instance_access = 37
    RULE_scalar_static_access = 38
    RULE_scalar_index = 39
    RULE_block_statement = 40
    RULE_statement = 41
    RULE_variable_and_const_declaration = 42
    RULE_variable_initialization = 43
    RULE_variable_initialization_list = 44
    RULE_assign_statement = 45
    RULE_left_hand_side = 46
    RULE_if_statement = 47
    RULE_elseif_statement = 48
    RULE_else_statement = 49
    RULE_foreach_statement = 50
    RULE_break_statement = 51
    RULE_continue_statement = 52
    RULE_return_statement = 53
    RULE_method_invocation_statement = 54
    RULE_instance_method_invocation = 55
    RULE_prefix_instance_method_invocation = 56
    RULE_static_method_invocation = 57

    ruleNames =  [ "program", "class_declaration", "class_name", "class_body", 
                   "attribute_declaration", "attribute_initialization", 
                   "attribute_initialization_list", "method_declaration", 
                   "constructor_declaration", "destructor_declaration", 
                   "list_of_parameters", "parameter_declaration", "type_name", 
                   "primitive_type", "array_type", "class_type", "literal", 
                   "primitive_literal", "array_literal", "multi_demensional_array", 
                   "array_literal_list", "indexed_array", "list_of_expressions", 
                   "expression", "string_expression", "relation_expression", 
                   "logical_expression", "adding_expression", "multiplying_expression", 
                   "negative_expression", "sign_expression", "index_expression", 
                   "instance_access_expression", "static_access_expression", 
                   "object_creation_expression", "operand", "scalar_variable", 
                   "scalar_instance_access", "scalar_static_access", "scalar_index", 
                   "block_statement", "statement", "variable_and_const_declaration", 
                   "variable_initialization", "variable_initialization_list", 
                   "assign_statement", "left_hand_side", "if_statement", 
                   "elseif_statement", "else_statement", "foreach_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "method_invocation_statement", "instance_method_invocation", 
                   "prefix_instance_method_invocation", "static_method_invocation" ]

    EOF = Token.EOF
    COMMENT=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    VAR=8
    VAL=9
    SELF=10
    RETURN=11
    IN=12
    BY=13
    NEW=14
    CONSTRUCTOR=15
    DESTRUCTOR=16
    NULL=17
    CLASS=18
    ARRAY=19
    INTEGER=20
    FLOAT=21
    BOOLEAN=22
    STRING=23
    ZERO_INTEGER=24
    INTEGER_LITERAL=25
    STRING_LITERAL=26
    BOOLEAN_LITERAL=27
    FLOAT_LITERAL=28
    ADD=29
    SUB=30
    MUL=31
    DIV=32
    MOD=33
    NOT=34
    AND=35
    OR=36
    EQUAL=37
    ASSIGN=38
    NOT_EQUAL=39
    LT=40
    LTE=41
    GT=42
    GTE=43
    STRING_EQUAL=44
    STRING_ADD=45
    LP=46
    RP=47
    LSB=48
    RSB=49
    DOT=50
    DOUBLE_DOT=51
    COMMA=52
    SEMI=53
    COLON=54
    DOUBLE_COLON=55
    LCB=56
    RCB=57
    ID=58
    DOLLAR_ID=59
    WS=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_TOKEN=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.class_declaration()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 121
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def class_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_nameContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_nameContext,i)


        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(D96Parser.CLASS)
            self.state = 124
            self.class_name()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 125
                self.match(D96Parser.COLON)
                self.state = 126
                self.class_name()


            self.state = 129
            self.match(D96Parser.LCB)
            self.state = 130
            self.class_body()
            self.state = 131
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_name




    def class_name(self):

        localctx = D96Parser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Attribute_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,i)


        def method_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Method_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Method_declarationContext,i)


        def constructor_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Constructor_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Constructor_declarationContext,i)


        def destructor_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Destructor_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Destructor_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 139
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAR, D96Parser.VAL]:
                    self.state = 135
                    self.attribute_declaration()
                    pass
                elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 136
                    self.method_declaration()
                    pass
                elif token in [D96Parser.CONSTRUCTOR]:
                    self.state = 137
                    self.constructor_declaration()
                    pass
                elif token in [D96Parser.DESTRUCTOR]:
                    self.state = 138
                    self.destructor_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number_attribute = 0

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def attribute_initialization(self):
            return self.getTypedRuleContext(D96Parser.Attribute_initializationContext,0)


        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def DOLLAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_ID)
            else:
                return self.getToken(D96Parser.DOLLAR_ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            getInvokingContext(4).number_attribute+=1
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 147
                self.match(D96Parser.COMMA)
                self.state = 148
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                getInvokingContext(4).number_attribute+=1
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(D96Parser.COLON)
            self.state = 156
            self.type_name()
            self.state = 157
            self.attribute_initialization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_initializationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def attribute_initialization_list(self):
            return self.getTypedRuleContext(D96Parser.Attribute_initialization_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_initialization




    def attribute_initialization(self):

        localctx = D96Parser.Attribute_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute_initialization)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(D96Parser.ASSIGN)
                self.state = 160
                self.attribute_initialization_list()
                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(D96Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_initialization_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_initialization_list




    def attribute_initialization_list(self):

        localctx = D96Parser.Attribute_initialization_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_initialization_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.expression()
            self.state = 165
            self.match(D96Parser.COMMA)
            self.state = 166
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 169
            self.match(D96Parser.LP)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 170
                self.list_of_parameters()


            self.state = 173
            self.match(D96Parser.RP)
            self.state = 174
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_declaration




    def constructor_declaration(self):

        localctx = D96Parser.Constructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 177
            self.match(D96Parser.LP)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 178
                self.list_of_parameters()


            self.state = 181
            self.match(D96Parser.RP)
            self.state = 182
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_declaration




    def destructor_declaration(self):

        localctx = D96Parser.Destructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destructor_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(D96Parser.DESTRUCTOR)
            self.state = 185
            self.match(D96Parser.LP)
            self.state = 186
            self.match(D96Parser.RP)
            self.state = 187
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Parameter_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Parameter_declarationContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_of_parameters




    def list_of_parameters(self):

        localctx = D96Parser.List_of_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_of_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.parameter_declaration()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 190
                self.match(D96Parser.SEMI)
                self.state = 191
                self.parameter_declaration()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter_declaration




    def parameter_declaration(self):

        localctx = D96Parser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(D96Parser.ID)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 198
                self.match(D96Parser.COMMA)
                self.state = 199
                self.match(D96Parser.ID)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(D96Parser.COLON)
            self.state = 206
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_type_name




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_name)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(D96Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(D96Parser.ARRAY)
            self.state = 216
            self.match(D96Parser.LSB)
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 217
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 218
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 221
            self.match(D96Parser.COMMA)
            self.state = 222
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 223
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal(self):
            return self.getTypedRuleContext(D96Parser.Array_literalContext,0)


        def primitive_literal(self):
            return self.getTypedRuleContext(D96Parser.Primitive_literalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.array_literal()
                pass
            elif token in [D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.primitive_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO_INTEGER(self):
            return self.getToken(D96Parser.ZERO_INTEGER, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_literal




    def primitive_literal(self):

        localctx = D96Parser.Primitive_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primitive_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def multi_demensional_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_demensional_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_literal




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_literal)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.indexed_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.multi_demensional_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_demensional_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def array_literal_list(self):
            return self.getTypedRuleContext(D96Parser.Array_literal_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_multi_demensional_array




    def multi_demensional_array(self):

        localctx = D96Parser.Multi_demensional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multi_demensional_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(D96Parser.ARRAY)
            self.state = 238
            self.match(D96Parser.LP)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ARRAY:
                self.state = 239
                self.array_literal_list()


            self.state = 242
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Array_literalContext)
            else:
                return self.getTypedRuleContext(D96Parser.Array_literalContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_literal_list




    def array_literal_list(self):

        localctx = D96Parser.Array_literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_literal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.array_literal()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 245
                self.match(D96Parser.COMMA)
                self.state = 246
                self.array_literal()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(D96Parser.ARRAY)
            self.state = 253
            self.match(D96Parser.LP)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                self.state = 254
                self.list_of_expressions()


            self.state = 257
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_expressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_of_expressions




    def list_of_expressions(self):

        localctx = D96Parser.List_of_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_of_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.expression()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 260
                self.match(D96Parser.COMMA)
                self.state = 261
                self.expression()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expression(self):
            return self.getTypedRuleContext(D96Parser.String_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.string_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Relation_expressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.Relation_expressionContext,i)


        def STRING_ADD(self):
            return self.getToken(D96Parser.STRING_ADD, 0)

        def STRING_EQUAL(self):
            return self.getToken(D96Parser.STRING_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_expression




    def string_expression(self):

        localctx = D96Parser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_string_expression)
        self._la = 0 # Token type
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.relation_expression()
                self.state = 270
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRING_EQUAL or _la==D96Parser.STRING_ADD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 271
                self.relation_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.relation_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Logical_expressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.Logical_expressionContext,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relation_expression




    def relation_expression(self):

        localctx = D96Parser.Relation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_relation_expression)
        self._la = 0 # Token type
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.logical_expression(0)
                self.state = 277
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LT) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 278
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.logical_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expression(self):
            return self.getTypedRuleContext(D96Parser.Adding_expressionContext,0)


        def logical_expression(self):
            return self.getTypedRuleContext(D96Parser.Logical_expressionContext,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_logical_expression



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.adding_expression(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expression(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_expressionContext,0)


        def adding_expression(self):
            return self.getTypedRuleContext(D96Parser.Adding_expressionContext,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_adding_expression



    def adding_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Adding_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_adding_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 299
                    self.multiplying_expression(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negative_expression(self):
            return self.getTypedRuleContext(D96Parser.Negative_expressionContext,0)


        def multiplying_expression(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_expressionContext,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multiplying_expression



    def multiplying_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Multiplying_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_multiplying_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.negative_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.negative_expression() 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Negative_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def negative_expression(self):
            return self.getTypedRuleContext(D96Parser.Negative_expressionContext,0)


        def sign_expression(self):
            return self.getTypedRuleContext(D96Parser.Sign_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_negative_expression




    def negative_expression(self):

        localctx = D96Parser.Negative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_negative_expression)
        try:
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(D96Parser.NOT)
                self.state = 317
                self.negative_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.SUB, D96Parser.LP, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.sign_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def sign_expression(self):
            return self.getTypedRuleContext(D96Parser.Sign_expressionContext,0)


        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sign_expression




    def sign_expression(self):

        localctx = D96Parser.Sign_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_sign_expression)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(D96Parser.SUB)
                self.state = 322
                self.sign_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.LP, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.index_expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Instance_access_expressionContext,0)


        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index_expression



    def index_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_index_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.instance_access_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    self.match(D96Parser.LSB)
                    self.state = 331
                    self.expression()
                    self.state = 332
                    self.match(D96Parser.RSB) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Instance_access_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Static_access_expressionContext,0)


        def instance_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Instance_access_expressionContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_access_expression



    def instance_access_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Instance_access_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_instance_access_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.static_access_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 353
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Instance_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access_expression)
                        self.state = 342
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 343
                        self.match(D96Parser.DOT)
                        self.state = 344
                        self.match(D96Parser.ID)
                        self.state = 345
                        self.match(D96Parser.LP)
                        self.state = 347
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                            self.state = 346
                            self.list_of_expressions()


                        self.state = 349
                        self.match(D96Parser.RP)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Instance_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access_expression)
                        self.state = 350
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 351
                        self.match(D96Parser.DOT)
                        self.state = 352
                        self.match(D96Parser.ID)
                        pass

             
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_access_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def object_creation_expression(self):
            return self.getTypedRuleContext(D96Parser.Object_creation_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_access_expression




    def static_access_expression(self):

        localctx = D96Parser.Static_access_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_static_access_expression)
        self._la = 0 # Token type
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(D96Parser.ID)
                self.state = 359
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 360
                self.match(D96Parser.DOLLAR_ID)
                self.state = 361
                self.match(D96Parser.LP)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                    self.state = 362
                    self.list_of_expressions()


                self.state = 365
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(D96Parser.ID)
                self.state = 367
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 368
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 369
                self.object_creation_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creation_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_creation_expression




    def object_creation_expression(self):

        localctx = D96Parser.Object_creation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_object_creation_expression)
        self._la = 0 # Token type
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(D96Parser.NEW)
                self.state = 373
                self.match(D96Parser.ID)
                self.state = 374
                self.match(D96Parser.LP)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                    self.state = 375
                    self.list_of_expressions()


                self.state = 378
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.SELF, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.LP, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operand




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_operand)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.literal()
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 386
                self.match(D96Parser.LP)
                self.state = 387
                self.expression()
                self.state = 388
                self.match(D96Parser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_instance_access(self):
            return self.getTypedRuleContext(D96Parser.Scalar_instance_accessContext,0)


        def scalar_static_access(self):
            return self.getTypedRuleContext(D96Parser.Scalar_static_accessContext,0)


        def scalar_index(self):
            return self.getTypedRuleContext(D96Parser.Scalar_indexContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalar_variable




    def scalar_variable(self):

        localctx = D96Parser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_scalar_variable)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.scalar_instance_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.scalar_static_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                self.scalar_index()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_instance_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Instance_access_expressionContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalar_instance_access




    def scalar_instance_access(self):

        localctx = D96Parser.Scalar_instance_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_scalar_instance_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.instance_access_expression(0)
            self.state = 399
            self.match(D96Parser.DOT)
            self.state = 400
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_static_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalar_static_access




    def scalar_static_access(self):

        localctx = D96Parser.Scalar_static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_scalar_static_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.class_name()
            self.state = 403
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 404
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalar_index




    def scalar_index(self):

        localctx = D96Parser.Scalar_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_scalar_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.index_expression(0)
            self.state = 407
            self.match(D96Parser.LSB)
            self.state = 408
            self.expression()
            self.state = 409
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_statement




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(D96Parser.LCB)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.SELF) | (1 << D96Parser.RETURN) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.LP) | (1 << D96Parser.LCB) | (1 << D96Parser.ID))) != 0):
                self.state = 412
                self.statement()
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 418
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_and_const_declaration(self):
            return self.getTypedRuleContext(D96Parser.Variable_and_const_declarationContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def foreach_statement(self):
            return self.getTypedRuleContext(D96Parser.Foreach_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext,0)


        def method_invocation_statement(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_statement)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.variable_and_const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 422
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 423
                self.foreach_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 424
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 425
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 426
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 427
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 428
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_and_const_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number_variable = 0

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def variable_initialization(self):
            return self.getTypedRuleContext(D96Parser.Variable_initializationContext,0)


        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_and_const_declaration




    def variable_and_const_declaration(self):

        localctx = D96Parser.Variable_and_const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_variable_and_const_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 432
            self.match(D96Parser.ID)
            getInvokingContext(42).number_variable+=1
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 434
                self.match(D96Parser.COMMA)

                self.state = 435
                self.match(D96Parser.ID)
                getInvokingContext(42).number_variable+=1
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 442
            self.match(D96Parser.COLON)
            self.state = 443
            self.type_name()
            self.state = 444
            self.variable_initialization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_initializationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def variable_initialization_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_initialization_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_initialization




    def variable_initialization(self):

        localctx = D96Parser.Variable_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_variable_initialization)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(D96Parser.ASSIGN)
                self.state = 447
                self.variable_initialization_list()
                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(D96Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_initialization_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_initialization_list




    def variable_initialization_list(self):

        localctx = D96Parser.Variable_initialization_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_variable_initialization_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.expression()
            getInvokingContext(42).number_variable -= 1
            self.state = 460
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 453
                    if not getInvokingContext(42).number_variable > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$variable_and_const_declaration::number_variable > 0")
                    self.state = 454
                    self.match(D96Parser.COMMA)
                    self.state = 455
                    self.expression()
                    getInvokingContext(42).number_variable -= 1
                    			 
                self.state = 462
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 463
            if not getInvokingContext(42).number_variable == 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$variable_and_const_declaration::number_variable == 0")
            self.state = 464
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_hand_side(self):
            return self.getTypedRuleContext(D96Parser.Left_hand_sideContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.left_hand_side()
            self.state = 467
            self.match(D96Parser.ASSIGN)
            self.state = 468
            self.expression()
            self.state = 469
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_hand_sideContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_left_hand_side




    def left_hand_side(self):

        localctx = D96Parser.Left_hand_sideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_left_hand_side)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.scalar_variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def elseif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elseif_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elseif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(D96Parser.IF)
            self.state = 474
            self.match(D96Parser.LP)
            self.state = 475
            self.expression()
            self.state = 476
            self.match(D96Parser.RP)
            self.state = 477
            self.block_statement()
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 478
                self.elseif_statement()
                self.state = 483
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 485
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 484
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_statement




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(D96Parser.ELSEIF)
            self.state = 488
            self.match(D96Parser.LP)
            self.state = 489
            self.expression()
            self.state = 490
            self.match(D96Parser.RP)
            self.state = 491
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statement




    def else_statement(self):

        localctx = D96Parser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(D96Parser.ELSE)
            self.state = 494
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_statement




    def foreach_statement(self):

        localctx = D96Parser.Foreach_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(D96Parser.FOREACH)
            self.state = 497
            self.match(D96Parser.LP)
            self.state = 498
            self.scalar_variable()
            self.state = 499
            self.match(D96Parser.IN)
            self.state = 500
            self.expression()
            self.state = 501
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 502
            self.expression()
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 503
                self.match(D96Parser.BY)
                self.state = 504
                self.expression()


            self.state = 507
            self.match(D96Parser.RP)
            self.state = 508
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(D96Parser.BREAK)
            self.state = 511
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(D96Parser.CONTINUE)
            self.state = 514
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_statement




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_return_statement)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(D96Parser.RETURN)
                self.state = 517
                self.expression()
                self.state = 518
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.match(D96Parser.RETURN)
                self.state = 521
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def instance_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invocationContext,0)


        def static_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 524
                self.instance_method_invocation()
                pass

            elif la_ == 2:
                self.state = 525
                self.static_method_invocation()
                pass


            self.state = 528
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefix_instance_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Prefix_instance_method_invocationContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_invocation




    def instance_method_invocation(self):

        localctx = D96Parser.Instance_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_instance_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.prefix_instance_method_invocation(0)
            self.state = 531
            self.match(D96Parser.DOT)
            self.state = 532
            self.match(D96Parser.ID)
            self.state = 533
            self.match(D96Parser.LP)
            self.state = 535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                self.state = 534
                self.list_of_expressions()


            self.state = 537
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_instance_method_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Static_access_expressionContext,0)


        def prefix_instance_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Prefix_instance_method_invocationContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_prefix_instance_method_invocation



    def prefix_instance_method_invocation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Prefix_instance_method_invocationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_prefix_instance_method_invocation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.static_access_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 555
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 553
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Prefix_instance_method_invocationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_instance_method_invocation)
                        self.state = 542
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 543
                        self.match(D96Parser.DOT)
                        self.state = 544
                        self.match(D96Parser.ID)
                        self.state = 545
                        self.match(D96Parser.LP)
                        self.state = 547
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                            self.state = 546
                            self.list_of_expressions()


                        self.state = 549
                        self.match(D96Parser.RP)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Prefix_instance_method_invocationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_instance_method_invocation)
                        self.state = 550
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 551
                        self.match(D96Parser.DOT)
                        self.state = 552
                        self.match(D96Parser.ID)
                        pass

             
                self.state = 557
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_method_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invocation




    def static_method_invocation(self):

        localctx = D96Parser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.class_name()
            self.state = 559
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 560
            self.match(D96Parser.DOLLAR_ID)
            self.state = 561
            self.match(D96Parser.LP)
            self.state = 563
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                self.state = 562
                self.list_of_expressions()


            self.state = 565
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.logical_expression_sempred
        self._predicates[27] = self.adding_expression_sempred
        self._predicates[28] = self.multiplying_expression_sempred
        self._predicates[31] = self.index_expression_sempred
        self._predicates[32] = self.instance_access_expression_sempred
        self._predicates[44] = self.variable_initialization_list_sempred
        self._predicates[56] = self.prefix_instance_method_invocation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def index_expression_sempred(self, localctx:Index_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def instance_access_expression_sempred(self, localctx:Instance_access_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def variable_initialization_list_sempred(self, localctx:Variable_initialization_listContext, predIndex:int):
            if predIndex == 6:
                return getInvokingContext(42).number_variable > 0
         

            if predIndex == 7:
                return getInvokingContext(42).number_variable == 0
         

    def prefix_instance_method_invocation_sempred(self, localctx:Prefix_instance_method_invocationContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




