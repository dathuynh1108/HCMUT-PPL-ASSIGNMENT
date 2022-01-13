# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\u023b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\7\2f\n\2\f\2\16")
        buf.write("\2i\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3q\n\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\5\3\5\7\5}\n\5\f\5\16\5\u0080\13")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\5\6\u0087\n\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\7\7\u0093\n\7\f\7\16\7\u0096\13")
        buf.write("\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u009f\n\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\5\n\u00a7\n\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\7\f\u00b4\n\f\f\f\16\f\u00b7\13")
        buf.write("\f\3\r\3\r\3\r\7\r\u00bc\n\r\f\r\16\r\u00bf\13\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\5\16\u00c6\n\16\3\17\3\17\3\20\3\20\5")
        buf.write("\20\u00cc\n\20\3\21\3\21\3\21\5\21\u00d1\n\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\5\22\u00d8\n\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\7\23\u00df\n\23\f\23\16\23\u00e2\13\23\3\24\3\24\3")
        buf.write("\24\5\24\u00e7\n\24\3\25\3\25\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u00ef\n\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\7")
        buf.write("\30\u00f9\n\30\f\30\16\30\u00fc\13\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0108\n\31\3\32")
        buf.write("\3\32\3\32\3\32\7\32\u010e\n\32\f\32\16\32\u0111\13\32")
        buf.write("\3\32\3\32\3\32\5\32\u0116\n\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0123\n\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\6\35\u0138\n\35\r")
        buf.write("\35\16\35\u0139\3\35\3\35\3\35\3\35\3\35\3\35\6\35\u0142")
        buf.write("\n\35\r\35\16\35\u0143\3\35\3\35\5\35\u0148\n\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \5 \u015c\n \3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\5#\u016d\n#\3$\3$\3$\3%\3%\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\5&\u017d\n&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0198\n\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\7(\u01a3\n(\f(\16(\u01a6\13(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\7)\u01b1\n)\f)\16)\u01b4\13)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\7*\u01c2\n*\f*\16*\u01c5")
        buf.write("\13*\3+\3+\3+\5+\u01ca\n+\3,\3,\3,\3,\3,\5,\u01d1\n,\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01e3")
        buf.write("\n-\3-\3-\3-\3-\3-\7-\u01ea\n-\f-\16-\u01ed\13-\3.\3.")
        buf.write("\3.\3.\3.\3.\3.\3.\3.\5.\u01f8\n.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\5.\u0203\n.\3.\3.\5.\u0207\n.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\5.\u0211\n.\3.\7.\u0214\n.\f.\16.\u0217\13.\3")
        buf.write("/\3/\3/\5/\u021c\n/\3/\3/\3\60\3\60\3\60\3\60\5\60\u0224")
        buf.write("\n\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u0231\n\61\3\62\3\62\3\62\7\62\u0236\n\62\f")
        buf.write("\62\16\62\u0239\13\62\3\62\2\b\fNPRXZ\63\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`b\2\7\3\2\n\13\3\2;<\3\2\32\35\3\2\26\31")
        buf.write("\4\2\f\f;;\2\u0258\2g\3\2\2\2\4l\3\2\2\2\6v\3\2\2\2\b")
        buf.write("~\3\2\2\2\n\u0081\3\2\2\2\f\u008a\3\2\2\2\16\u0097\3\2")
        buf.write("\2\2\20\u009b\3\2\2\2\22\u00a3\3\2\2\2\24\u00ab\3\2\2")
        buf.write("\2\26\u00b0\3\2\2\2\30\u00b8\3\2\2\2\32\u00c5\3\2\2\2")
        buf.write("\34\u00c7\3\2\2\2\36\u00cb\3\2\2\2 \u00cd\3\2\2\2\"\u00d4")
        buf.write("\3\2\2\2$\u00db\3\2\2\2&\u00e6\3\2\2\2(\u00e8\3\2\2\2")
        buf.write("*\u00ea\3\2\2\2,\u00f4\3\2\2\2.\u00f6\3\2\2\2\60\u0107")
        buf.write("\3\2\2\2\62\u0109\3\2\2\2\64\u0119\3\2\2\2\66\u0122\3")
        buf.write("\2\2\28\u0147\3\2\2\2:\u0149\3\2\2\2<\u014f\3\2\2\2>\u0152")
        buf.write("\3\2\2\2@\u0160\3\2\2\2B\u0163\3\2\2\2D\u016c\3\2\2\2")
        buf.write("F\u016e\3\2\2\2H\u0171\3\2\2\2J\u017c\3\2\2\2L\u0197\3")
        buf.write("\2\2\2N\u0199\3\2\2\2P\u01a7\3\2\2\2R\u01b5\3\2\2\2T\u01c9")
        buf.write("\3\2\2\2V\u01d0\3\2\2\2X\u01e2\3\2\2\2Z\u0206\3\2\2\2")
        buf.write("\\\u0218\3\2\2\2^\u021f\3\2\2\2`\u0230\3\2\2\2b\u0232")
        buf.write("\3\2\2\2df\5\4\3\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2")
        buf.write("\2\2hj\3\2\2\2ig\3\2\2\2jk\7\2\2\3k\3\3\2\2\2lm\7\24\2")
        buf.write("\2mp\5\6\4\2no\7\67\2\2oq\5\6\4\2pn\3\2\2\2pq\3\2\2\2")
        buf.write("qr\3\2\2\2rs\79\2\2st\5\b\5\2tu\7:\2\2u\5\3\2\2\2vw\7")
        buf.write(";\2\2w\7\3\2\2\2x}\5\n\6\2y}\5\20\t\2z}\5\22\n\2{}\5\24")
        buf.write("\13\2|x\3\2\2\2|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2}\u0080\3")
        buf.write("\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\t\3\2\2\2\u0080~\3\2")
        buf.write("\2\2\u0081\u0082\t\2\2\2\u0082\u0083\5\f\7\2\u0083\u0084")
        buf.write("\7\67\2\2\u0084\u0086\5&\24\2\u0085\u0087\5\16\b\2\u0086")
        buf.write("\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0089\7\66\2\2\u0089\13\3\2\2\2\u008a\u008b\b\7")
        buf.write("\1\2\u008b\u008c\t\3\2\2\u008c\u008d\b\7\1\2\u008d\u0094")
        buf.write("\3\2\2\2\u008e\u008f\f\4\2\2\u008f\u0090\7\65\2\2\u0090")
        buf.write("\u0091\t\3\2\2\u0091\u0093\b\7\1\2\u0092\u008e\3\2\2\2")
        buf.write("\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3")
        buf.write("\2\2\2\u0095\r\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098")
        buf.write("\7\'\2\2\u0098\u0099\5b\62\2\u0099\u009a\b\b\1\2\u009a")
        buf.write("\17\3\2\2\2\u009b\u009c\t\3\2\2\u009c\u009e\7/\2\2\u009d")
        buf.write("\u009f\5\26\f\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2")
        buf.write("\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\7\60\2\2\u00a1\u00a2")
        buf.write("\5.\30\2\u00a2\21\3\2\2\2\u00a3\u00a4\7\21\2\2\u00a4\u00a6")
        buf.write("\7/\2\2\u00a5\u00a7\5\26\f\2\u00a6\u00a5\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\7\60\2")
        buf.write("\2\u00a9\u00aa\5.\30\2\u00aa\23\3\2\2\2\u00ab\u00ac\7")
        buf.write("\22\2\2\u00ac\u00ad\7/\2\2\u00ad\u00ae\7\60\2\2\u00ae")
        buf.write("\u00af\5.\30\2\u00af\25\3\2\2\2\u00b0\u00b5\5\30\r\2\u00b1")
        buf.write("\u00b2\7\66\2\2\u00b2\u00b4\5\30\r\2\u00b3\u00b1\3\2\2")
        buf.write("\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\27\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00bd")
        buf.write("\7;\2\2\u00b9\u00ba\7\65\2\2\u00ba\u00bc\7;\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd\3")
        buf.write("\2\2\2\u00c0\u00c1\7\67\2\2\u00c1\u00c2\5&\24\2\u00c2")
        buf.write("\31\3\2\2\2\u00c3\u00c6\5\36\20\2\u00c4\u00c6\5\34\17")
        buf.write("\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\33\3")
        buf.write("\2\2\2\u00c7\u00c8\t\4\2\2\u00c8\35\3\2\2\2\u00c9\u00cc")
        buf.write("\5 \21\2\u00ca\u00cc\5\"\22\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cc\37\3\2\2\2\u00cd\u00ce\7\25\2\2\u00ce")
        buf.write("\u00d0\7/\2\2\u00cf\u00d1\5b\62\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7")
        buf.write("\60\2\2\u00d3!\3\2\2\2\u00d4\u00d5\7\25\2\2\u00d5\u00d7")
        buf.write("\7/\2\2\u00d6\u00d8\5$\23\2\u00d7\u00d6\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\7\60\2")
        buf.write("\2\u00da#\3\2\2\2\u00db\u00e0\5\36\20\2\u00dc\u00dd\7")
        buf.write("\65\2\2\u00dd\u00df\5\36\20\2\u00de\u00dc\3\2\2\2\u00df")
        buf.write("\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1%\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e7\5(\25")
        buf.write("\2\u00e4\u00e7\5*\26\2\u00e5\u00e7\5,\27\2\u00e6\u00e3")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7")
        buf.write("\'\3\2\2\2\u00e8\u00e9\t\5\2\2\u00e9)\3\2\2\2\u00ea\u00eb")
        buf.write("\7\25\2\2\u00eb\u00ee\7\61\2\2\u00ec\u00ef\5(\25\2\u00ed")
        buf.write("\u00ef\5*\26\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2")
        buf.write("\u00ef\u00f0\3\2\2\2\u00f0\u00f1\7\65\2\2\u00f1\u00f2")
        buf.write("\7\32\2\2\u00f2\u00f3\7\62\2\2\u00f3+\3\2\2\2\u00f4\u00f5")
        buf.write("\7;\2\2\u00f5-\3\2\2\2\u00f6\u00fa\79\2\2\u00f7\u00f9")
        buf.write("\5\60\31\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fd\3\2\2\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fd\u00fe\7:\2\2\u00fe/\3\2\2\2")
        buf.write("\u00ff\u0108\5\62\32\2\u0100\u0108\5\64\33\2\u0101\u0108")
        buf.write("\58\35\2\u0102\u0108\5> \2\u0103\u0108\5@!\2\u0104\u0108")
        buf.write("\5B\"\2\u0105\u0108\5D#\2\u0106\u0108\5F$\2\u0107\u00ff")
        buf.write("\3\2\2\2\u0107\u0100\3\2\2\2\u0107\u0101\3\2\2\2\u0107")
        buf.write("\u0102\3\2\2\2\u0107\u0103\3\2\2\2\u0107\u0104\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108\61\3\2")
        buf.write("\2\2\u0109\u010a\t\2\2\2\u010a\u010f\7;\2\2\u010b\u010c")
        buf.write("\7\65\2\2\u010c\u010e\7;\2\2\u010d\u010b\3\2\2\2\u010e")
        buf.write("\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u0112\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\7")
        buf.write("\67\2\2\u0113\u0115\5&\24\2\u0114\u0116\5\16\b\2\u0115")
        buf.write("\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u0118\7\66\2\2\u0118\63\3\2\2\2\u0119\u011a\5\66")
        buf.write("\34\2\u011a\u011b\7\'\2\2\u011b\u011c\5H%\2\u011c\u011d")
        buf.write("\7\66\2\2\u011d\65\3\2\2\2\u011e\u0123\7;\2\2\u011f\u0123")
        buf.write("\7<\2\2\u0120\u0123\5X-\2\u0121\u0123\5Z.\2\u0122\u011e")
        buf.write("\3\2\2\2\u0122\u011f\3\2\2\2\u0122\u0120\3\2\2\2\u0122")
        buf.write("\u0121\3\2\2\2\u0123\67\3\2\2\2\u0124\u0125\7\6\2\2\u0125")
        buf.write("\u0126\7/\2\2\u0126\u0127\5H%\2\u0127\u0128\7\60\2\2\u0128")
        buf.write("\u0129\5.\30\2\u0129\u0148\3\2\2\2\u012a\u012b\7\6\2\2")
        buf.write("\u012b\u012c\7/\2\2\u012c\u012d\5H%\2\u012d\u012e\7\60")
        buf.write("\2\2\u012e\u012f\5.\30\2\u012f\u0130\5<\37\2\u0130\u0148")
        buf.write("\3\2\2\2\u0131\u0132\7\6\2\2\u0132\u0133\7/\2\2\u0133")
        buf.write("\u0134\5H%\2\u0134\u0135\7\60\2\2\u0135\u0137\5.\30\2")
        buf.write("\u0136\u0138\5:\36\2\u0137\u0136\3\2\2\2\u0138\u0139\3")
        buf.write("\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0148")
        buf.write("\3\2\2\2\u013b\u013c\7\6\2\2\u013c\u013d\7/\2\2\u013d")
        buf.write("\u013e\5H%\2\u013e\u013f\7\60\2\2\u013f\u0141\5.\30\2")
        buf.write("\u0140\u0142\5:\36\2\u0141\u0140\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0146\5<\37\2\u0146\u0148\3\2\2\2\u0147")
        buf.write("\u0124\3\2\2\2\u0147\u012a\3\2\2\2\u0147\u0131\3\2\2\2")
        buf.write("\u0147\u013b\3\2\2\2\u01489\3\2\2\2\u0149\u014a\7\7\2")
        buf.write("\2\u014a\u014b\7/\2\2\u014b\u014c\5H%\2\u014c\u014d\7")
        buf.write("\60\2\2\u014d\u014e\5.\30\2\u014e;\3\2\2\2\u014f\u0150")
        buf.write("\7\b\2\2\u0150\u0151\5.\30\2\u0151=\3\2\2\2\u0152\u0153")
        buf.write("\7\t\2\2\u0153\u0154\7/\2\2\u0154\u0155\t\3\2\2\u0155")
        buf.write("\u0156\7\16\2\2\u0156\u0157\5H%\2\u0157\u0158\7\64\2\2")
        buf.write("\u0158\u015b\5H%\2\u0159\u015a\7\17\2\2\u015a\u015c\5")
        buf.write("H%\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u015e\7\60\2\2\u015e\u015f\5.\30\2\u015f")
        buf.write("?\3\2\2\2\u0160\u0161\7\4\2\2\u0161\u0162\7\66\2\2\u0162")
        buf.write("A\3\2\2\2\u0163\u0164\7\5\2\2\u0164\u0165\7\66\2\2\u0165")
        buf.write("C\3\2\2\2\u0166\u0167\7\r\2\2\u0167\u0168\5H%\2\u0168")
        buf.write("\u0169\7\66\2\2\u0169\u016d\3\2\2\2\u016a\u016b\7\r\2")
        buf.write("\2\u016b\u016d\7\66\2\2\u016c\u0166\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016dE\3\2\2\2\u016e\u016f\5Z.\2\u016f\u0170")
        buf.write("\7\66\2\2\u0170G\3\2\2\2\u0171\u0172\5J&\2\u0172I\3\2")
        buf.write("\2\2\u0173\u0174\5L\'\2\u0174\u0175\7.\2\2\u0175\u0176")
        buf.write("\5L\'\2\u0176\u017d\3\2\2\2\u0177\u0178\5L\'\2\u0178\u0179")
        buf.write("\7-\2\2\u0179\u017a\5L\'\2\u017a\u017d\3\2\2\2\u017b\u017d")
        buf.write("\5L\'\2\u017c\u0173\3\2\2\2\u017c\u0177\3\2\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017dK\3\2\2\2\u017e\u017f\5N(\2\u017f")
        buf.write("\u0180\7&\2\2\u0180\u0181\5N(\2\u0181\u0198\3\2\2\2\u0182")
        buf.write("\u0183\5N(\2\u0183\u0184\7(\2\2\u0184\u0185\5N(\2\u0185")
        buf.write("\u0198\3\2\2\2\u0186\u0187\5N(\2\u0187\u0188\7)\2\2\u0188")
        buf.write("\u0189\5N(\2\u0189\u0198\3\2\2\2\u018a\u018b\5N(\2\u018b")
        buf.write("\u018c\7*\2\2\u018c\u018d\5N(\2\u018d\u0198\3\2\2\2\u018e")
        buf.write("\u018f\5N(\2\u018f\u0190\7+\2\2\u0190\u0191\5N(\2\u0191")
        buf.write("\u0198\3\2\2\2\u0192\u0193\5N(\2\u0193\u0194\7,\2\2\u0194")
        buf.write("\u0195\5N(\2\u0195\u0198\3\2\2\2\u0196\u0198\5N(\2\u0197")
        buf.write("\u017e\3\2\2\2\u0197\u0182\3\2\2\2\u0197\u0186\3\2\2\2")
        buf.write("\u0197\u018a\3\2\2\2\u0197\u018e\3\2\2\2\u0197\u0192\3")
        buf.write("\2\2\2\u0197\u0196\3\2\2\2\u0198M\3\2\2\2\u0199\u019a")
        buf.write("\b(\1\2\u019a\u019b\5P)\2\u019b\u01a4\3\2\2\2\u019c\u019d")
        buf.write("\f\5\2\2\u019d\u019e\7$\2\2\u019e\u01a3\5P)\2\u019f\u01a0")
        buf.write("\f\4\2\2\u01a0\u01a1\7%\2\2\u01a1\u01a3\5P)\2\u01a2\u019c")
        buf.write("\3\2\2\2\u01a2\u019f\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5O\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01a8\b)\1\2\u01a8\u01a9\5R*\2\u01a9")
        buf.write("\u01b2\3\2\2\2\u01aa\u01ab\f\5\2\2\u01ab\u01ac\7\36\2")
        buf.write("\2\u01ac\u01b1\5R*\2\u01ad\u01ae\f\4\2\2\u01ae\u01af\7")
        buf.write("\37\2\2\u01af\u01b1\5R*\2\u01b0\u01aa\3\2\2\2\u01b0\u01ad")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3Q\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b6\b*\1\2\u01b6\u01b7\5T+\2\u01b7\u01c3\3\2\2\2\u01b8")
        buf.write("\u01b9\f\6\2\2\u01b9\u01ba\7 \2\2\u01ba\u01c2\5T+\2\u01bb")
        buf.write("\u01bc\f\5\2\2\u01bc\u01bd\7!\2\2\u01bd\u01c2\5T+\2\u01be")
        buf.write("\u01bf\f\4\2\2\u01bf\u01c0\7\"\2\2\u01c0\u01c2\5T+\2\u01c1")
        buf.write("\u01b8\3\2\2\2\u01c1\u01bb\3\2\2\2\u01c1\u01be\3\2\2\2")
        buf.write("\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4S\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7")
        buf.write("\7#\2\2\u01c7\u01ca\5T+\2\u01c8\u01ca\5V,\2\u01c9\u01c6")
        buf.write("\3\2\2\2\u01c9\u01c8\3\2\2\2\u01caU\3\2\2\2\u01cb\u01cc")
        buf.write("\7\37\2\2\u01cc\u01d1\5V,\2\u01cd\u01d1\5X-\2\u01ce\u01d1")
        buf.write("\5Z.\2\u01cf\u01d1\5`\61\2\u01d0\u01cb\3\2\2\2\u01d0\u01cd")
        buf.write("\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1")
        buf.write("W\3\2\2\2\u01d2\u01d3\b-\1\2\u01d3\u01d4\5Z.\2\u01d4\u01d5")
        buf.write("\7\61\2\2\u01d5\u01d6\5H%\2\u01d6\u01d7\7\62\2\2\u01d7")
        buf.write("\u01e3\3\2\2\2\u01d8\u01d9\7;\2\2\u01d9\u01da\7\61\2\2")
        buf.write("\u01da\u01db\5H%\2\u01db\u01dc\7\62\2\2\u01dc\u01e3\3")
        buf.write("\2\2\2\u01dd\u01de\7<\2\2\u01de\u01df\7\61\2\2\u01df\u01e0")
        buf.write("\5H%\2\u01e0\u01e1\7\62\2\2\u01e1\u01e3\3\2\2\2\u01e2")
        buf.write("\u01d2\3\2\2\2\u01e2\u01d8\3\2\2\2\u01e2\u01dd\3\2\2\2")
        buf.write("\u01e3\u01eb\3\2\2\2\u01e4\u01e5\f\6\2\2\u01e5\u01e6\7")
        buf.write("\61\2\2\u01e6\u01e7\5H%\2\u01e7\u01e8\7\62\2\2\u01e8\u01ea")
        buf.write("\3\2\2\2\u01e9\u01e4\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ecY\3\2\2\2\u01ed")
        buf.write("\u01eb\3\2\2\2\u01ee\u01ef\b.\1\2\u01ef\u01f0\7;\2\2\u01f0")
        buf.write("\u01f1\78\2\2\u01f1\u0207\7<\2\2\u01f2\u01f3\7;\2\2\u01f3")
        buf.write("\u01f4\78\2\2\u01f4\u01f5\7<\2\2\u01f5\u01f7\7/\2\2\u01f6")
        buf.write("\u01f8\5b\62\2\u01f7\u01f6\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9\u0207\7\60\2\2\u01fa\u01fb")
        buf.write("\t\6\2\2\u01fb\u01fc\7\63\2\2\u01fc\u0207\7;\2\2\u01fd")
        buf.write("\u01fe\t\6\2\2\u01fe\u01ff\7\63\2\2\u01ff\u0200\7;\2\2")
        buf.write("\u0200\u0202\7/\2\2\u0201\u0203\5b\62\2\u0202\u0201\3")
        buf.write("\2\2\2\u0202\u0203\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0207")
        buf.write("\7\60\2\2\u0205\u0207\5\\/\2\u0206\u01ee\3\2\2\2\u0206")
        buf.write("\u01f2\3\2\2\2\u0206\u01fa\3\2\2\2\u0206\u01fd\3\2\2\2")
        buf.write("\u0206\u0205\3\2\2\2\u0207\u0215\3\2\2\2\u0208\u0209\f")
        buf.write("\t\2\2\u0209\u020a\7\63\2\2\u020a\u0214\7;\2\2\u020b\u020c")
        buf.write("\f\b\2\2\u020c\u020d\7\63\2\2\u020d\u020e\7;\2\2\u020e")
        buf.write("\u0210\7/\2\2\u020f\u0211\5b\62\2\u0210\u020f\3\2\2\2")
        buf.write("\u0210\u0211\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0214\7")
        buf.write("\60\2\2\u0213\u0208\3\2\2\2\u0213\u020b\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216[\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u0219\t\3\2")
        buf.write("\2\u0219\u021b\7/\2\2\u021a\u021c\5b\62\2\u021b\u021a")
        buf.write("\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write("\u021e\7\60\2\2\u021e]\3\2\2\2\u021f\u0220\7\20\2\2\u0220")
        buf.write("\u0221\7;\2\2\u0221\u0223\7/\2\2\u0222\u0224\5b\62\2\u0223")
        buf.write("\u0222\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0225\3\2\2\2")
        buf.write("\u0225\u0226\7\60\2\2\u0226_\3\2\2\2\u0227\u0231\5^\60")
        buf.write("\2\u0228\u0231\7<\2\2\u0229\u0231\7;\2\2\u022a\u0231\5")
        buf.write("\32\16\2\u022b\u0231\7\f\2\2\u022c\u022d\7/\2\2\u022d")
        buf.write("\u022e\5H%\2\u022e\u022f\7\60\2\2\u022f\u0231\3\2\2\2")
        buf.write("\u0230\u0227\3\2\2\2\u0230\u0228\3\2\2\2\u0230\u0229\3")
        buf.write("\2\2\2\u0230\u022a\3\2\2\2\u0230\u022b\3\2\2\2\u0230\u022c")
        buf.write("\3\2\2\2\u0231a\3\2\2\2\u0232\u0237\5H%\2\u0233\u0234")
        buf.write("\7\65\2\2\u0234\u0236\5H%\2\u0235\u0233\3\2\2\2\u0236")
        buf.write("\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3\2\2\2")
        buf.write("\u0238c\3\2\2\2\u0239\u0237\3\2\2\2\63gp|~\u0086\u0094")
        buf.write("\u009e\u00a6\u00b5\u00bd\u00c5\u00cb\u00d0\u00d7\u00e0")
        buf.write("\u00e6\u00ee\u00fa\u0107\u010f\u0115\u0122\u0139\u0143")
        buf.write("\u0147\u015b\u016c\u017c\u0197\u01a2\u01a4\u01b0\u01b2")
        buf.write("\u01c1\u01c3\u01c9\u01d0\u01e2\u01eb\u01f7\u0202\u0206")
        buf.write("\u0210\u0213\u0215\u021b\u0223\u0230\u0237")
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
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'.'", 
                     "'..'", "','", "';'", "':'", "'::'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "VAR", "VAL", "SELF", 
                      "RETURN", "IN", "BY", "NEW", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NULL", "CLASS", "ARRAY", "INTEGER", "FLOAT", "BOOLEAN", 
                      "STRING", "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "LT", "LTE", "GT", "GTE", "STRING_EQUAL", "STRING_ADD", 
                      "LP", "RP", "LSB", "RSB", "DOT", "DOUBLE_DOT", "COMMA", 
                      "SEMI", "COLON", "DOUBLE_COLON", "LCB", "RCB", "ID", 
                      "DOLLAR_ID", "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_class_name = 2
    RULE_class_body = 3
    RULE_attribute_declaration = 4
    RULE_declare_variable_list = 5
    RULE_initialization = 6
    RULE_method_declaration = 7
    RULE_constructor_declaration = 8
    RULE_destructor_declaration = 9
    RULE_list_of_parameters = 10
    RULE_parameter_declaration = 11
    RULE_literal = 12
    RULE_primitive_literal = 13
    RULE_array_literal = 14
    RULE_indexed_array = 15
    RULE_multi_demensional_array = 16
    RULE_array_literal_list = 17
    RULE_type_name = 18
    RULE_primitive_type = 19
    RULE_array_type = 20
    RULE_class_type = 21
    RULE_block_statement = 22
    RULE_statement = 23
    RULE_variable_and_const_declaration = 24
    RULE_assign_statement = 25
    RULE_left_hand_side = 26
    RULE_if_statement = 27
    RULE_elseif_statement = 28
    RULE_else_statement = 29
    RULE_foreach_statement = 30
    RULE_break_statement = 31
    RULE_continue_statement = 32
    RULE_return_statement = 33
    RULE_method_invocation_statement = 34
    RULE_expression = 35
    RULE_string_expression = 36
    RULE_relation_expression = 37
    RULE_logical_expression = 38
    RULE_adding_expression = 39
    RULE_multiplying_expression = 40
    RULE_negative_expression = 41
    RULE_sign_expression = 42
    RULE_index_expression = 43
    RULE_member_access_expression = 44
    RULE_self_method_call = 45
    RULE_object_creation_expression = 46
    RULE_operand = 47
    RULE_list_of_expressions = 48

    ruleNames =  [ "program", "class_declaration", "class_name", "class_body", 
                   "attribute_declaration", "declare_variable_list", "initialization", 
                   "method_declaration", "constructor_declaration", "destructor_declaration", 
                   "list_of_parameters", "parameter_declaration", "literal", 
                   "primitive_literal", "array_literal", "indexed_array", 
                   "multi_demensional_array", "array_literal_list", "type_name", 
                   "primitive_type", "array_type", "class_type", "block_statement", 
                   "statement", "variable_and_const_declaration", "assign_statement", 
                   "left_hand_side", "if_statement", "elseif_statement", 
                   "else_statement", "foreach_statement", "break_statement", 
                   "continue_statement", "return_statement", "method_invocation_statement", 
                   "expression", "string_expression", "relation_expression", 
                   "logical_expression", "adding_expression", "multiplying_expression", 
                   "negative_expression", "sign_expression", "index_expression", 
                   "member_access_expression", "self_method_call", "object_creation_expression", 
                   "operand", "list_of_expressions" ]

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
    INTEGER_LITERAL=24
    STRING_LITERAL=25
    BOOLEAN_LITERAL=26
    FLOAT_LITERAL=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    NOT=33
    AND=34
    OR=35
    EQUAL=36
    ASSIGN=37
    NOT_EQUAL=38
    LT=39
    LTE=40
    GT=41
    GTE=42
    STRING_EQUAL=43
    STRING_ADD=44
    LP=45
    RP=46
    LSB=47
    RSB=48
    DOT=49
    DOUBLE_DOT=50
    COMMA=51
    SEMI=52
    COLON=53
    DOUBLE_COLON=54
    LCB=55
    RCB=56
    ID=57
    DOLLAR_ID=58
    WS=59
    UNTERMINATED_COMMENT=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_TOKEN=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CLASS:
                self.state = 98
                self.class_declaration()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(D96Parser.CLASS)
            self.state = 107
            self.class_name()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 108
                self.match(D96Parser.COLON)
                self.state = 109
                self.class_name()


            self.state = 112
            self.match(D96Parser.LCB)
            self.state = 113
            self.class_body()
            self.state = 114
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_name" ):
                return visitor.visitClass_name(self)
            else:
                return visitor.visitChildren(self)




    def class_name(self):

        localctx = D96Parser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 122
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAR, D96Parser.VAL]:
                    self.state = 118
                    self.attribute_declaration()
                    pass
                elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 119
                    self.method_declaration()
                    pass
                elif token in [D96Parser.CONSTRUCTOR]:
                    self.state = 120
                    self.constructor_declaration()
                    pass
                elif token in [D96Parser.DESTRUCTOR]:
                    self.state = 121
                    self.destructor_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 126
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number_variable = 0

        def declare_variable_list(self):
            return self.getTypedRuleContext(D96Parser.Declare_variable_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def initialization(self):
            return self.getTypedRuleContext(D96Parser.InitializationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declaration" ):
                return visitor.visitAttribute_declaration(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 128
            self.declare_variable_list(0)
            self.state = 129
            self.match(D96Parser.COLON)
            self.state = 130
            self.type_name()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 131
                self.initialization()


            self.state = 134
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_variable_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def declare_variable_list(self):
            return self.getTypedRuleContext(D96Parser.Declare_variable_listContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_declare_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_variable_list" ):
                return visitor.visitDeclare_variable_list(self)
            else:
                return visitor.visitChildren(self)



    def declare_variable_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Declare_variable_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_declare_variable_list, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.getInvokingContext(4).number_variable+=1
            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Declare_variable_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declare_variable_list)
                    self.state = 140
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 141
                    self.match(D96Parser.COMMA)
                    self.state = 142
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.getInvokingContext(4).number_variable+=1 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = D96Parser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(D96Parser.ASSIGN)
            self.state = 150
            self.list_of_expressions()

            print(self.getInvokingContext(4).number_variable)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 154
            self.match(D96Parser.LP)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 155
                self.list_of_parameters()


            self.state = 158
            self.match(D96Parser.RP)
            self.state = 159
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_declaration" ):
                return visitor.visitConstructor_declaration(self)
            else:
                return visitor.visitChildren(self)




    def constructor_declaration(self):

        localctx = D96Parser.Constructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 162
            self.match(D96Parser.LP)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 163
                self.list_of_parameters()


            self.state = 166
            self.match(D96Parser.RP)
            self.state = 167
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_declaration" ):
                return visitor.visitDestructor_declaration(self)
            else:
                return visitor.visitChildren(self)




    def destructor_declaration(self):

        localctx = D96Parser.Destructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destructor_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(D96Parser.DESTRUCTOR)
            self.state = 170
            self.match(D96Parser.LP)
            self.state = 171
            self.match(D96Parser.RP)
            self.state = 172
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_parameters" ):
                return visitor.visitList_of_parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_of_parameters(self):

        localctx = D96Parser.List_of_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_of_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.parameter_declaration()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 175
                self.match(D96Parser.SEMI)
                self.state = 176
                self.parameter_declaration()
                self.state = 181
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = D96Parser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(D96Parser.ID)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 183
                self.match(D96Parser.COMMA)
                self.state = 184
                self.match(D96Parser.ID)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.match(D96Parser.COLON)
            self.state = 191
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal(self):
            return self.getTypedRuleContext(D96Parser.Array_literalContext,0)


        def primitive_literal(self):
            return self.getTypedRuleContext(D96Parser.Primitive_literalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literal)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.array_literal()
                pass
            elif token in [D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_literal" ):
                return visitor.visitPrimitive_literal(self)
            else:
                return visitor.visitChildren(self)




    def primitive_literal(self):

        localctx = D96Parser.Primitive_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL))) != 0)):
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def multi_demensional_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_demensional_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_literal)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.indexed_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.multi_demensional_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(D96Parser.ARRAY)
            self.state = 204
            self.match(D96Parser.LP)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 205
                self.list_of_expressions()


            self.state = 208
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_demensional_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_demensional_array" ):
                return visitor.visitMulti_demensional_array(self)
            else:
                return visitor.visitChildren(self)




    def multi_demensional_array(self):

        localctx = D96Parser.Multi_demensional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_multi_demensional_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(D96Parser.ARRAY)
            self.state = 211
            self.match(D96Parser.LP)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ARRAY:
                self.state = 212
                self.array_literal_list()


            self.state = 215
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_list" ):
                return visitor.visitArray_literal_list(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_list(self):

        localctx = D96Parser.Array_literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_literal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.array_literal()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 218
                self.match(D96Parser.COMMA)
                self.state = 219
                self.array_literal()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type_name)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(D96Parser.ARRAY)
            self.state = 233
            self.match(D96Parser.LSB)
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 234
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 235
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 238
            self.match(D96Parser.COMMA)
            self.state = 239
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 240
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(D96Parser.LCB)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.SELF) | (1 << D96Parser.RETURN) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 245
                self.statement()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.variable_and_const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.foreach_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 259
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 260
                self.method_invocation_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_and_const_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def initialization(self):
            return self.getTypedRuleContext(D96Parser.InitializationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_and_const_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_and_const_declaration" ):
                return visitor.visitVariable_and_const_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_and_const_declaration(self):

        localctx = D96Parser.Variable_and_const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_variable_and_const_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 264
            self.match(D96Parser.ID)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 265
                self.match(D96Parser.COMMA)
                self.state = 266
                self.match(D96Parser.ID)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self.match(D96Parser.COLON)
            self.state = 273
            self.type_name()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 274
                self.initialization()


            self.state = 277
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.left_hand_side()
            self.state = 280
            self.match(D96Parser.ASSIGN)
            self.state = 281
            self.expression()
            self.state = 282
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_hand_sideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_left_hand_side

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_hand_side" ):
                return visitor.visitLeft_hand_side(self)
            else:
                return visitor.visitChildren(self)




    def left_hand_side(self):

        localctx = D96Parser.Left_hand_sideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_left_hand_side)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.index_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 287
                self.member_access_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def elseif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elseif_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elseif_statementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(D96Parser.IF)
                self.state = 291
                self.match(D96Parser.LP)
                self.state = 292
                self.expression()
                self.state = 293
                self.match(D96Parser.RP)
                self.state = 294
                self.block_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(D96Parser.IF)
                self.state = 297
                self.match(D96Parser.LP)
                self.state = 298
                self.expression()
                self.state = 299
                self.match(D96Parser.RP)
                self.state = 300
                self.block_statement()
                self.state = 301
                self.else_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(D96Parser.IF)
                self.state = 304
                self.match(D96Parser.LP)
                self.state = 305
                self.expression()
                self.state = 306
                self.match(D96Parser.RP)
                self.state = 307
                self.block_statement()
                self.state = 309 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 308
                    self.elseif_statement()
                    self.state = 311 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.match(D96Parser.IF)
                self.state = 314
                self.match(D96Parser.LP)
                self.state = 315
                self.expression()
                self.state = 316
                self.match(D96Parser.RP)
                self.state = 317
                self.block_statement()
                self.state = 319 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 318
                    self.elseif_statement()
                    self.state = 321 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                self.state = 323
                self.else_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_statement" ):
                return visitor.visitElseif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(D96Parser.ELSEIF)
            self.state = 328
            self.match(D96Parser.LP)
            self.state = 329
            self.expression()
            self.state = 330
            self.match(D96Parser.RP)
            self.state = 331
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = D96Parser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(D96Parser.ELSE)
            self.state = 334
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

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


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach_statement" ):
                return visitor.visitForeach_statement(self)
            else:
                return visitor.visitChildren(self)




    def foreach_statement(self):

        localctx = D96Parser.Foreach_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(D96Parser.FOREACH)
            self.state = 337
            self.match(D96Parser.LP)
            self.state = 338
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 339
            self.match(D96Parser.IN)
            self.state = 340
            self.expression()
            self.state = 341
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 342
            self.expression()
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 343
                self.match(D96Parser.BY)
                self.state = 344
                self.expression()


            self.state = 347
            self.match(D96Parser.RP)
            self.state = 348
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(D96Parser.BREAK)
            self.state = 351
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(D96Parser.CONTINUE)
            self.state = 354
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_return_statement)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(D96Parser.RETURN)
                self.state = 357
                self.expression()
                self.state = 358
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(D96Parser.RETURN)
                self.state = 361
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.member_access_expression(0)
            self.state = 365
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expression(self):
            return self.getTypedRuleContext(D96Parser.String_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.string_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression" ):
                return visitor.visitString_expression(self)
            else:
                return visitor.visitChildren(self)




    def string_expression(self):

        localctx = D96Parser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_string_expression)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.relation_expression()
                self.state = 370
                self.match(D96Parser.STRING_ADD)
                self.state = 371
                self.relation_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.relation_expression()
                self.state = 374
                self.match(D96Parser.STRING_EQUAL)
                self.state = 375
                self.relation_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_expression" ):
                return visitor.visitRelation_expression(self)
            else:
                return visitor.visitChildren(self)




    def relation_expression(self):

        localctx = D96Parser.Relation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_relation_expression)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.logical_expression(0)
                self.state = 381
                self.match(D96Parser.EQUAL)
                self.state = 382
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.logical_expression(0)
                self.state = 385
                self.match(D96Parser.NOT_EQUAL)
                self.state = 386
                self.logical_expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
                self.logical_expression(0)
                self.state = 389
                self.match(D96Parser.LT)
                self.state = 390
                self.logical_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 392
                self.logical_expression(0)
                self.state = 393
                self.match(D96Parser.LTE)
                self.state = 394
                self.logical_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 396
                self.logical_expression(0)
                self.state = 397
                self.match(D96Parser.GT)
                self.state = 398
                self.logical_expression(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 400
                self.logical_expression(0)
                self.state = 401
                self.match(D96Parser.GTE)
                self.state = 402
                self.logical_expression(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 404
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_logical_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 416
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                        self.state = 410
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 411
                        self.match(D96Parser.AND)
                        self.state = 412
                        self.adding_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                        self.state = 413
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 414
                        self.match(D96Parser.OR)
                        self.state = 415
                        self.adding_expression(0)
                        pass

             
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expression" ):
                return visitor.visitAdding_expression(self)
            else:
                return visitor.visitChildren(self)



    def adding_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Adding_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_adding_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 430
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                        self.state = 424
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 425
                        self.match(D96Parser.ADD)
                        self.state = 426
                        self.multiplying_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                        self.state = 427
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 428
                        self.match(D96Parser.SUB)
                        self.state = 429
                        self.multiplying_expression(0)
                        pass

             
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expression" ):
                return visitor.visitMultiplying_expression(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Multiplying_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_multiplying_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.negative_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 449
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 447
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                        self.state = 438
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 439
                        self.match(D96Parser.MUL)
                        self.state = 440
                        self.negative_expression()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                        self.state = 441
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 442
                        self.match(D96Parser.DIV)
                        self.state = 443
                        self.negative_expression()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                        self.state = 444
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 445
                        self.match(D96Parser.MOD)
                        self.state = 446
                        self.negative_expression()
                        pass

             
                self.state = 451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Negative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative_expression" ):
                return visitor.visitNegative_expression(self)
            else:
                return visitor.visitChildren(self)




    def negative_expression(self):

        localctx = D96Parser.Negative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_negative_expression)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(D96Parser.NOT)
                self.state = 453
                self.negative_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.ARRAY, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.SUB, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def sign_expression(self):
            return self.getTypedRuleContext(D96Parser.Sign_expressionContext,0)


        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sign_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expression" ):
                return visitor.visitSign_expression(self)
            else:
                return visitor.visitChildren(self)




    def sign_expression(self):

        localctx = D96Parser.Sign_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_sign_expression)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(D96Parser.SUB)
                self.state = 458
                self.sign_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.index_expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 460
                self.member_access_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 461
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)



    def index_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_index_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 465
                self.member_access_expression(0)
                self.state = 466
                self.match(D96Parser.LSB)
                self.state = 467
                self.expression()
                self.state = 468
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.state = 470
                self.match(D96Parser.ID)
                self.state = 471
                self.match(D96Parser.LSB)
                self.state = 472
                self.expression()
                self.state = 473
                self.match(D96Parser.RSB)
                pass

            elif la_ == 3:
                self.state = 475
                self.match(D96Parser.DOLLAR_ID)
                self.state = 476
                self.match(D96Parser.LSB)
                self.state = 477
                self.expression()
                self.state = 478
                self.match(D96Parser.RSB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 489
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression)
                    self.state = 482
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 483
                    self.match(D96Parser.LSB)
                    self.state = 484
                    self.expression()
                    self.state = 485
                    self.match(D96Parser.RSB) 
                self.state = 491
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Member_access_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

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


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def self_method_call(self):
            return self.getTypedRuleContext(D96Parser.Self_method_callContext,0)


        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_expression" ):
                return visitor.visitMember_access_expression(self)
            else:
                return visitor.visitChildren(self)



    def member_access_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Member_access_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_member_access_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 493
                self.match(D96Parser.ID)
                self.state = 494
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 495
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.state = 496
                self.match(D96Parser.ID)
                self.state = 497
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 498
                self.match(D96Parser.DOLLAR_ID)
                self.state = 499
                self.match(D96Parser.LP)
                self.state = 501
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                    self.state = 500
                    self.list_of_expressions()


                self.state = 503
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.state = 504
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 505
                self.match(D96Parser.DOT)
                self.state = 506
                self.match(D96Parser.ID)
                pass

            elif la_ == 4:
                self.state = 507
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 508
                self.match(D96Parser.DOT)
                self.state = 509
                self.match(D96Parser.ID)
                self.state = 510
                self.match(D96Parser.LP)
                self.state = 512
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                    self.state = 511
                    self.list_of_expressions()


                self.state = 514
                self.match(D96Parser.RP)
                pass

            elif la_ == 5:
                self.state = 515
                self.self_method_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 531
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 529
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Member_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expression)
                        self.state = 518
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 519
                        self.match(D96Parser.DOT)
                        self.state = 520
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Member_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expression)
                        self.state = 521
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 522
                        self.match(D96Parser.DOT)
                        self.state = 523
                        self.match(D96Parser.ID)
                        self.state = 524
                        self.match(D96Parser.LP)
                        self.state = 526
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                            self.state = 525
                            self.list_of_expressions()


                        self.state = 528
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 533
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Self_method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_self_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_method_call" ):
                return visitor.visitSelf_method_call(self)
            else:
                return visitor.visitChildren(self)




    def self_method_call(self):

        localctx = D96Parser.Self_method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_self_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 535
            self.match(D96Parser.LP)
            self.state = 537
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 536
                self.list_of_expressions()


            self.state = 539
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creation_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def getRuleIndex(self):
            return D96Parser.RULE_object_creation_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_creation_expression" ):
                return visitor.visitObject_creation_expression(self)
            else:
                return visitor.visitChildren(self)




    def object_creation_expression(self):

        localctx = D96Parser.Object_creation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_object_creation_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(D96Parser.NEW)
            self.state = 542
            self.match(D96Parser.ID)
            self.state = 543
            self.match(D96Parser.LP)
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 544
                self.list_of_expressions()


            self.state = 547
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_creation_expression(self):
            return self.getTypedRuleContext(D96Parser.Object_creation_expressionContext,0)


        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_operand)
        try:
            self.state = 558
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 549
                self.object_creation_expression()
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 551
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 552
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 553
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 554
                self.match(D96Parser.LP)
                self.state = 555
                self.expression()
                self.state = 556
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


    class List_of_expressionsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_expressions" ):
                return visitor.visitList_of_expressions(self)
            else:
                return visitor.visitChildren(self)




    def list_of_expressions(self):

        localctx = D96Parser.List_of_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_list_of_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.expression()
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 561
                self.match(D96Parser.COMMA)
                self.state = 562
                self.expression()
                self.state = 567
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self._predicates[5] = self.declare_variable_list_sempred
        self._predicates[38] = self.logical_expression_sempred
        self._predicates[39] = self.adding_expression_sempred
        self._predicates[40] = self.multiplying_expression_sempred
        self._predicates[43] = self.index_expression_sempred
        self._predicates[44] = self.member_access_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def declare_variable_list_sempred(self, localctx:Declare_variable_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def index_expression_sempred(self, localctx:Index_expressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

    def member_access_expression_sempred(self, localctx:Member_access_expressionContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 6)
         




