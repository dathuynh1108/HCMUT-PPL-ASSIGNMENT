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
        buf.write("\u0232\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\7\2d\n\2\f\2\16\2g\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3o\n\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\7\5{\n\5\f\5\16\5~\13\5\3\6\3\6\3\6")
        buf.write("\3\6\7\6\u0084\n\6\f\6\16\6\u0087\13\6\3\6\3\6\3\6\5\6")
        buf.write("\u008c\n\6\3\6\3\6\3\7\3\7\3\7\5\7\u0093\n\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\5\b\u009b\n\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\7\n\u00a8\n\n\f\n\16\n\u00ab\13\n\3")
        buf.write("\13\3\13\3\13\7\13\u00b0\n\13\f\13\16\13\u00b3\13\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\5\f\u00ba\n\f\3\r\3\r\3\16\3\16")
        buf.write("\5\16\u00c0\n\16\3\17\3\17\3\17\5\17\u00c5\n\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\5\20\u00cc\n\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\7\21\u00d3\n\21\f\21\16\21\u00d6\13\21\3\22\3\22")
        buf.write("\3\22\5\22\u00db\n\22\3\23\3\23\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u00e3\n\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\7\27\u00f0\n\27\f\27\16\27\u00f3\13\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u00ff\n\30\3\31\3\31\3\31\3\31\7\31\u0105\n\31\f\31\16")
        buf.write("\31\u0108\13\31\3\31\3\31\3\31\5\31\u010d\n\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u011a\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\6\34\u012f\n\34\r\34\16\34\u0130\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\6\34\u0139\n\34\r\34\16\34\u013a\3\34\3\34")
        buf.write("\5\34\u013f\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u0153\n\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\5\"\u0164\n\"\3#\3#\3#\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\5%\u0174\n%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\5&\u018f\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'")
        buf.write("\u019a\n\'\f\'\16\'\u019d\13\'\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\7(\u01a8\n(\f(\16(\u01ab\13(\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\7)\u01b9\n)\f)\16)\u01bc\13)\3*\3*\3")
        buf.write("*\5*\u01c1\n*\3+\3+\3+\3+\3+\5+\u01c8\n+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01da\n,\3,\3,\3")
        buf.write(",\3,\3,\7,\u01e1\n,\f,\16,\u01e4\13,\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\5-\u01ef\n-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01fa")
        buf.write("\n-\3-\3-\5-\u01fe\n-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0208")
        buf.write("\n-\3-\7-\u020b\n-\f-\16-\u020e\13-\3.\3.\3.\5.\u0213")
        buf.write("\n.\3.\3.\3/\3/\3/\3/\5/\u021b\n/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0228\n\60\3\61\3")
        buf.write("\61\3\61\7\61\u022d\n\61\f\61\16\61\u0230\13\61\3\61\2")
        buf.write("\7LNPVX\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\7\3\2\n\13\3")
        buf.write("\2;<\3\2\32\35\3\2\26\31\4\2\f\f;;\2\u0250\2e\3\2\2\2")
        buf.write("\4j\3\2\2\2\6t\3\2\2\2\b|\3\2\2\2\n\177\3\2\2\2\f\u008f")
        buf.write("\3\2\2\2\16\u0097\3\2\2\2\20\u009f\3\2\2\2\22\u00a4\3")
        buf.write("\2\2\2\24\u00ac\3\2\2\2\26\u00b9\3\2\2\2\30\u00bb\3\2")
        buf.write("\2\2\32\u00bf\3\2\2\2\34\u00c1\3\2\2\2\36\u00c8\3\2\2")
        buf.write("\2 \u00cf\3\2\2\2\"\u00da\3\2\2\2$\u00dc\3\2\2\2&\u00de")
        buf.write("\3\2\2\2(\u00e8\3\2\2\2*\u00ea\3\2\2\2,\u00ed\3\2\2\2")
        buf.write(".\u00fe\3\2\2\2\60\u0100\3\2\2\2\62\u0110\3\2\2\2\64\u0119")
        buf.write("\3\2\2\2\66\u013e\3\2\2\28\u0140\3\2\2\2:\u0146\3\2\2")
        buf.write("\2<\u0149\3\2\2\2>\u0157\3\2\2\2@\u015a\3\2\2\2B\u0163")
        buf.write("\3\2\2\2D\u0165\3\2\2\2F\u0168\3\2\2\2H\u0173\3\2\2\2")
        buf.write("J\u018e\3\2\2\2L\u0190\3\2\2\2N\u019e\3\2\2\2P\u01ac\3")
        buf.write("\2\2\2R\u01c0\3\2\2\2T\u01c7\3\2\2\2V\u01d9\3\2\2\2X\u01fd")
        buf.write("\3\2\2\2Z\u020f\3\2\2\2\\\u0216\3\2\2\2^\u0227\3\2\2\2")
        buf.write("`\u0229\3\2\2\2bd\5\4\3\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2")
        buf.write("\2ef\3\2\2\2fh\3\2\2\2ge\3\2\2\2hi\7\2\2\3i\3\3\2\2\2")
        buf.write("jk\7\24\2\2kn\5\6\4\2lm\7\67\2\2mo\5\6\4\2nl\3\2\2\2n")
        buf.write("o\3\2\2\2op\3\2\2\2pq\79\2\2qr\5\b\5\2rs\7:\2\2s\5\3\2")
        buf.write("\2\2tu\7;\2\2u\7\3\2\2\2v{\5\n\6\2w{\5\f\7\2x{\5\16\b")
        buf.write("\2y{\5\20\t\2zv\3\2\2\2zw\3\2\2\2zx\3\2\2\2zy\3\2\2\2")
        buf.write("{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\t\3\2\2\2~|\3\2\2\2\177")
        buf.write("\u0080\t\2\2\2\u0080\u0085\t\3\2\2\u0081\u0082\7\65\2")
        buf.write("\2\u0082\u0084\t\3\2\2\u0083\u0081\3\2\2\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u0088\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\7\67\2")
        buf.write("\2\u0089\u008b\5\"\22\2\u008a\u008c\5*\26\2\u008b\u008a")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008e\7\66\2\2\u008e\13\3\2\2\2\u008f\u0090\t\3\2\2\u0090")
        buf.write("\u0092\7/\2\2\u0091\u0093\5\22\n\2\u0092\u0091\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\7")
        buf.write("\60\2\2\u0095\u0096\5,\27\2\u0096\r\3\2\2\2\u0097\u0098")
        buf.write("\7\21\2\2\u0098\u009a\7/\2\2\u0099\u009b\5\22\n\2\u009a")
        buf.write("\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c\u009d\7\60\2\2\u009d\u009e\5,\27\2\u009e\17\3\2")
        buf.write("\2\2\u009f\u00a0\7\22\2\2\u00a0\u00a1\7/\2\2\u00a1\u00a2")
        buf.write("\7\60\2\2\u00a2\u00a3\5,\27\2\u00a3\21\3\2\2\2\u00a4\u00a9")
        buf.write("\5\24\13\2\u00a5\u00a6\7\66\2\2\u00a6\u00a8\5\24\13\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\23\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ac\u00b1\7;\2\2\u00ad\u00ae\7\65\2\2\u00ae")
        buf.write("\u00b0\7;\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b3\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3")
        buf.write("\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7\67\2\2\u00b5")
        buf.write("\u00b6\5\"\22\2\u00b6\25\3\2\2\2\u00b7\u00ba\5\32\16\2")
        buf.write("\u00b8\u00ba\5\30\r\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8")
        buf.write("\3\2\2\2\u00ba\27\3\2\2\2\u00bb\u00bc\t\4\2\2\u00bc\31")
        buf.write("\3\2\2\2\u00bd\u00c0\5\34\17\2\u00be\u00c0\5\36\20\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\33\3\2\2\2\u00c1")
        buf.write("\u00c2\7\25\2\2\u00c2\u00c4\7/\2\2\u00c3\u00c5\5`\61\2")
        buf.write("\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3")
        buf.write("\2\2\2\u00c6\u00c7\7\60\2\2\u00c7\35\3\2\2\2\u00c8\u00c9")
        buf.write("\7\25\2\2\u00c9\u00cb\7/\2\2\u00ca\u00cc\5 \21\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00ce\7\60\2\2\u00ce\37\3\2\2\2\u00cf\u00d4\5\32")
        buf.write("\16\2\u00d0\u00d1\7\65\2\2\u00d1\u00d3\5\32\16\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5!\3\2\2\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d7\u00db\5$\23\2\u00d8\u00db\5&\24\2\u00d9\u00db")
        buf.write("\5(\25\2\u00da\u00d7\3\2\2\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00db#\3\2\2\2\u00dc\u00dd\t\5\2\2\u00dd")
        buf.write("%\3\2\2\2\u00de\u00df\7\25\2\2\u00df\u00e2\7\61\2\2\u00e0")
        buf.write("\u00e3\5$\23\2\u00e1\u00e3\5&\24\2\u00e2\u00e0\3\2\2\2")
        buf.write("\u00e2\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7")
        buf.write("\65\2\2\u00e5\u00e6\7\32\2\2\u00e6\u00e7\7\62\2\2\u00e7")
        buf.write("\'\3\2\2\2\u00e8\u00e9\7;\2\2\u00e9)\3\2\2\2\u00ea\u00eb")
        buf.write("\7\'\2\2\u00eb\u00ec\5`\61\2\u00ec+\3\2\2\2\u00ed\u00f1")
        buf.write("\79\2\2\u00ee\u00f0\5.\30\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\7")
        buf.write(":\2\2\u00f5-\3\2\2\2\u00f6\u00ff\5\60\31\2\u00f7\u00ff")
        buf.write("\5\62\32\2\u00f8\u00ff\5\66\34\2\u00f9\u00ff\5<\37\2\u00fa")
        buf.write("\u00ff\5> \2\u00fb\u00ff\5@!\2\u00fc\u00ff\5B\"\2\u00fd")
        buf.write("\u00ff\5D#\2\u00fe\u00f6\3\2\2\2\u00fe\u00f7\3\2\2\2\u00fe")
        buf.write("\u00f8\3\2\2\2\u00fe\u00f9\3\2\2\2\u00fe\u00fa\3\2\2\2")
        buf.write("\u00fe\u00fb\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3")
        buf.write("\2\2\2\u00ff/\3\2\2\2\u0100\u0101\t\2\2\2\u0101\u0106")
        buf.write("\7;\2\2\u0102\u0103\7\65\2\2\u0103\u0105\7;\2\2\u0104")
        buf.write("\u0102\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3")
        buf.write("\2\2\2\u0109\u010a\7\67\2\2\u010a\u010c\5\"\22\2\u010b")
        buf.write("\u010d\5*\26\2\u010c\u010b\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e\u010f\7\66\2\2\u010f\61\3\2")
        buf.write("\2\2\u0110\u0111\5\64\33\2\u0111\u0112\7\'\2\2\u0112\u0113")
        buf.write("\5F$\2\u0113\u0114\7\66\2\2\u0114\63\3\2\2\2\u0115\u011a")
        buf.write("\7;\2\2\u0116\u011a\7<\2\2\u0117\u011a\5V,\2\u0118\u011a")
        buf.write("\5X-\2\u0119\u0115\3\2\2\2\u0119\u0116\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u0119\u0118\3\2\2\2\u011a\65\3\2\2\2\u011b\u011c")
        buf.write("\7\6\2\2\u011c\u011d\7/\2\2\u011d\u011e\5F$\2\u011e\u011f")
        buf.write("\7\60\2\2\u011f\u0120\5,\27\2\u0120\u013f\3\2\2\2\u0121")
        buf.write("\u0122\7\6\2\2\u0122\u0123\7/\2\2\u0123\u0124\5F$\2\u0124")
        buf.write("\u0125\7\60\2\2\u0125\u0126\5,\27\2\u0126\u0127\5:\36")
        buf.write("\2\u0127\u013f\3\2\2\2\u0128\u0129\7\6\2\2\u0129\u012a")
        buf.write("\7/\2\2\u012a\u012b\5F$\2\u012b\u012c\7\60\2\2\u012c\u012e")
        buf.write("\5,\27\2\u012d\u012f\58\35\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131\u013f\3\2\2\2\u0132\u0133\7\6\2\2\u0133\u0134\7")
        buf.write("/\2\2\u0134\u0135\5F$\2\u0135\u0136\7\60\2\2\u0136\u0138")
        buf.write("\5,\27\2\u0137\u0139\58\35\2\u0138\u0137\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013d\5:\36\2\u013d\u013f\3")
        buf.write("\2\2\2\u013e\u011b\3\2\2\2\u013e\u0121\3\2\2\2\u013e\u0128")
        buf.write("\3\2\2\2\u013e\u0132\3\2\2\2\u013f\67\3\2\2\2\u0140\u0141")
        buf.write("\7\7\2\2\u0141\u0142\7/\2\2\u0142\u0143\5F$\2\u0143\u0144")
        buf.write("\7\60\2\2\u0144\u0145\5,\27\2\u01459\3\2\2\2\u0146\u0147")
        buf.write("\7\b\2\2\u0147\u0148\5,\27\2\u0148;\3\2\2\2\u0149\u014a")
        buf.write("\7\t\2\2\u014a\u014b\7/\2\2\u014b\u014c\t\3\2\2\u014c")
        buf.write("\u014d\7\16\2\2\u014d\u014e\5F$\2\u014e\u014f\7\64\2\2")
        buf.write("\u014f\u0152\5F$\2\u0150\u0151\7\17\2\2\u0151\u0153\5")
        buf.write("F$\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154\u0155\7\60\2\2\u0155\u0156\5,\27\2\u0156")
        buf.write("=\3\2\2\2\u0157\u0158\7\4\2\2\u0158\u0159\7\66\2\2\u0159")
        buf.write("?\3\2\2\2\u015a\u015b\7\5\2\2\u015b\u015c\7\66\2\2\u015c")
        buf.write("A\3\2\2\2\u015d\u015e\7\r\2\2\u015e\u015f\5F$\2\u015f")
        buf.write("\u0160\7\66\2\2\u0160\u0164\3\2\2\2\u0161\u0162\7\r\2")
        buf.write("\2\u0162\u0164\7\66\2\2\u0163\u015d\3\2\2\2\u0163\u0161")
        buf.write("\3\2\2\2\u0164C\3\2\2\2\u0165\u0166\5X-\2\u0166\u0167")
        buf.write("\7\66\2\2\u0167E\3\2\2\2\u0168\u0169\5H%\2\u0169G\3\2")
        buf.write("\2\2\u016a\u016b\5J&\2\u016b\u016c\7.\2\2\u016c\u016d")
        buf.write("\5J&\2\u016d\u0174\3\2\2\2\u016e\u016f\5J&\2\u016f\u0170")
        buf.write("\7-\2\2\u0170\u0171\5J&\2\u0171\u0174\3\2\2\2\u0172\u0174")
        buf.write("\5J&\2\u0173\u016a\3\2\2\2\u0173\u016e\3\2\2\2\u0173\u0172")
        buf.write("\3\2\2\2\u0174I\3\2\2\2\u0175\u0176\5L\'\2\u0176\u0177")
        buf.write("\7&\2\2\u0177\u0178\5L\'\2\u0178\u018f\3\2\2\2\u0179\u017a")
        buf.write("\5L\'\2\u017a\u017b\7(\2\2\u017b\u017c\5L\'\2\u017c\u018f")
        buf.write("\3\2\2\2\u017d\u017e\5L\'\2\u017e\u017f\7)\2\2\u017f\u0180")
        buf.write("\5L\'\2\u0180\u018f\3\2\2\2\u0181\u0182\5L\'\2\u0182\u0183")
        buf.write("\7*\2\2\u0183\u0184\5L\'\2\u0184\u018f\3\2\2\2\u0185\u0186")
        buf.write("\5L\'\2\u0186\u0187\7+\2\2\u0187\u0188\5L\'\2\u0188\u018f")
        buf.write("\3\2\2\2\u0189\u018a\5L\'\2\u018a\u018b\7,\2\2\u018b\u018c")
        buf.write("\5L\'\2\u018c\u018f\3\2\2\2\u018d\u018f\5L\'\2\u018e\u0175")
        buf.write("\3\2\2\2\u018e\u0179\3\2\2\2\u018e\u017d\3\2\2\2\u018e")
        buf.write("\u0181\3\2\2\2\u018e\u0185\3\2\2\2\u018e\u0189\3\2\2\2")
        buf.write("\u018e\u018d\3\2\2\2\u018fK\3\2\2\2\u0190\u0191\b\'\1")
        buf.write("\2\u0191\u0192\5N(\2\u0192\u019b\3\2\2\2\u0193\u0194\f")
        buf.write("\5\2\2\u0194\u0195\7$\2\2\u0195\u019a\5N(\2\u0196\u0197")
        buf.write("\f\4\2\2\u0197\u0198\7%\2\2\u0198\u019a\5N(\2\u0199\u0193")
        buf.write("\3\2\2\2\u0199\u0196\3\2\2\2\u019a\u019d\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019cM\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019e\u019f\b(\1\2\u019f\u01a0\5P)\2\u01a0")
        buf.write("\u01a9\3\2\2\2\u01a1\u01a2\f\5\2\2\u01a2\u01a3\7\36\2")
        buf.write("\2\u01a3\u01a8\5P)\2\u01a4\u01a5\f\4\2\2\u01a5\u01a6\7")
        buf.write("\37\2\2\u01a6\u01a8\5P)\2\u01a7\u01a1\3\2\2\2\u01a7\u01a4")
        buf.write("\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aaO\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01ad\b)\1\2\u01ad\u01ae\5R*\2\u01ae\u01ba\3\2\2\2\u01af")
        buf.write("\u01b0\f\6\2\2\u01b0\u01b1\7 \2\2\u01b1\u01b9\5R*\2\u01b2")
        buf.write("\u01b3\f\5\2\2\u01b3\u01b4\7!\2\2\u01b4\u01b9\5R*\2\u01b5")
        buf.write("\u01b6\f\4\2\2\u01b6\u01b7\7\"\2\2\u01b7\u01b9\5R*\2\u01b8")
        buf.write("\u01af\3\2\2\2\u01b8\u01b2\3\2\2\2\u01b8\u01b5\3\2\2\2")
        buf.write("\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3")
        buf.write("\2\2\2\u01bbQ\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be")
        buf.write("\7#\2\2\u01be\u01c1\5R*\2\u01bf\u01c1\5T+\2\u01c0\u01bd")
        buf.write("\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1S\3\2\2\2\u01c2\u01c3")
        buf.write("\7\37\2\2\u01c3\u01c8\5T+\2\u01c4\u01c8\5V,\2\u01c5\u01c8")
        buf.write("\5X-\2\u01c6\u01c8\5^\60\2\u01c7\u01c2\3\2\2\2\u01c7\u01c4")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8")
        buf.write("U\3\2\2\2\u01c9\u01ca\b,\1\2\u01ca\u01cb\5X-\2\u01cb\u01cc")
        buf.write("\7\61\2\2\u01cc\u01cd\5F$\2\u01cd\u01ce\7\62\2\2\u01ce")
        buf.write("\u01da\3\2\2\2\u01cf\u01d0\7;\2\2\u01d0\u01d1\7\61\2\2")
        buf.write("\u01d1\u01d2\5F$\2\u01d2\u01d3\7\62\2\2\u01d3\u01da\3")
        buf.write("\2\2\2\u01d4\u01d5\7<\2\2\u01d5\u01d6\7\61\2\2\u01d6\u01d7")
        buf.write("\5F$\2\u01d7\u01d8\7\62\2\2\u01d8\u01da\3\2\2\2\u01d9")
        buf.write("\u01c9\3\2\2\2\u01d9\u01cf\3\2\2\2\u01d9\u01d4\3\2\2\2")
        buf.write("\u01da\u01e2\3\2\2\2\u01db\u01dc\f\6\2\2\u01dc\u01dd\7")
        buf.write("\61\2\2\u01dd\u01de\5F$\2\u01de\u01df\7\62\2\2\u01df\u01e1")
        buf.write("\3\2\2\2\u01e0\u01db\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3W\3\2\2\2\u01e4")
        buf.write("\u01e2\3\2\2\2\u01e5\u01e6\b-\1\2\u01e6\u01e7\7;\2\2\u01e7")
        buf.write("\u01e8\78\2\2\u01e8\u01fe\7<\2\2\u01e9\u01ea\7;\2\2\u01ea")
        buf.write("\u01eb\78\2\2\u01eb\u01ec\7<\2\2\u01ec\u01ee\7/\2\2\u01ed")
        buf.write("\u01ef\5`\61\2\u01ee\u01ed\3\2\2\2\u01ee\u01ef\3\2\2\2")
        buf.write("\u01ef\u01f0\3\2\2\2\u01f0\u01fe\7\60\2\2\u01f1\u01f2")
        buf.write("\t\6\2\2\u01f2\u01f3\7\63\2\2\u01f3\u01fe\7;\2\2\u01f4")
        buf.write("\u01f5\t\6\2\2\u01f5\u01f6\7\63\2\2\u01f6\u01f7\7;\2\2")
        buf.write("\u01f7\u01f9\7/\2\2\u01f8\u01fa\5`\61\2\u01f9\u01f8\3")
        buf.write("\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fe")
        buf.write("\7\60\2\2\u01fc\u01fe\5Z.\2\u01fd\u01e5\3\2\2\2\u01fd")
        buf.write("\u01e9\3\2\2\2\u01fd\u01f1\3\2\2\2\u01fd\u01f4\3\2\2\2")
        buf.write("\u01fd\u01fc\3\2\2\2\u01fe\u020c\3\2\2\2\u01ff\u0200\f")
        buf.write("\t\2\2\u0200\u0201\7\63\2\2\u0201\u020b\7;\2\2\u0202\u0203")
        buf.write("\f\b\2\2\u0203\u0204\7\63\2\2\u0204\u0205\7;\2\2\u0205")
        buf.write("\u0207\7/\2\2\u0206\u0208\5`\61\2\u0207\u0206\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020b\7")
        buf.write("\60\2\2\u020a\u01ff\3\2\2\2\u020a\u0202\3\2\2\2\u020b")
        buf.write("\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020dY\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0210\t\3\2")
        buf.write("\2\u0210\u0212\7/\2\2\u0211\u0213\5`\61\2\u0212\u0211")
        buf.write("\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0215\7\60\2\2\u0215[\3\2\2\2\u0216\u0217\7\20\2\2\u0217")
        buf.write("\u0218\7;\2\2\u0218\u021a\7/\2\2\u0219\u021b\5`\61\2\u021a")
        buf.write("\u0219\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021c\u021d\7\60\2\2\u021d]\3\2\2\2\u021e\u0228\5\\/")
        buf.write("\2\u021f\u0228\7<\2\2\u0220\u0228\7;\2\2\u0221\u0228\5")
        buf.write("\26\f\2\u0222\u0228\7\f\2\2\u0223\u0224\7/\2\2\u0224\u0225")
        buf.write("\5F$\2\u0225\u0226\7\60\2\2\u0226\u0228\3\2\2\2\u0227")
        buf.write("\u021e\3\2\2\2\u0227\u021f\3\2\2\2\u0227\u0220\3\2\2\2")
        buf.write("\u0227\u0221\3\2\2\2\u0227\u0222\3\2\2\2\u0227\u0223\3")
        buf.write("\2\2\2\u0228_\3\2\2\2\u0229\u022e\5F$\2\u022a\u022b\7")
        buf.write("\65\2\2\u022b\u022d\5F$\2\u022c\u022a\3\2\2\2\u022d\u0230")
        buf.write("\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f")
        buf.write("a\3\2\2\2\u0230\u022e\3\2\2\2\63enz|\u0085\u008b\u0092")
        buf.write("\u009a\u00a9\u00b1\u00b9\u00bf\u00c4\u00cb\u00d4\u00da")
        buf.write("\u00e2\u00f1\u00fe\u0106\u010c\u0119\u0130\u013a\u013e")
        buf.write("\u0152\u0163\u0173\u018e\u0199\u019b\u01a7\u01a9\u01b8")
        buf.write("\u01ba\u01c0\u01c7\u01d9\u01e2\u01ee\u01f9\u01fd\u0207")
        buf.write("\u020a\u020c\u0212\u021a\u0227\u022e")
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
    RULE_method_declaration = 5
    RULE_constructor_declaration = 6
    RULE_destructor_declaration = 7
    RULE_list_of_parameters = 8
    RULE_parameter_declaration = 9
    RULE_literal = 10
    RULE_primitive_literal = 11
    RULE_array_literal = 12
    RULE_indexed_array = 13
    RULE_multi_demensional_array = 14
    RULE_array_literal_list = 15
    RULE_type_name = 16
    RULE_primitive_type = 17
    RULE_array_type = 18
    RULE_class_type = 19
    RULE_initialization = 20
    RULE_block_statement = 21
    RULE_statement = 22
    RULE_variable_and_const_declaration = 23
    RULE_assign_statement = 24
    RULE_left_hand_side = 25
    RULE_if_statement = 26
    RULE_elseif_statement = 27
    RULE_else_statement = 28
    RULE_foreach_statement = 29
    RULE_break_statement = 30
    RULE_continue_statement = 31
    RULE_return_statement = 32
    RULE_method_invocation_statement = 33
    RULE_expression = 34
    RULE_string_expression = 35
    RULE_relation_expression = 36
    RULE_logical_expression = 37
    RULE_adding_expression = 38
    RULE_multiplying_expression = 39
    RULE_negative_expression = 40
    RULE_sign_expression = 41
    RULE_index_expression = 42
    RULE_member_access_expression = 43
    RULE_self_method_call = 44
    RULE_object_creation_expression = 45
    RULE_operand = 46
    RULE_list_of_expressions = 47

    ruleNames =  [ "program", "class_declaration", "class_name", "class_body", 
                   "attribute_declaration", "method_declaration", "constructor_declaration", 
                   "destructor_declaration", "list_of_parameters", "parameter_declaration", 
                   "literal", "primitive_literal", "array_literal", "indexed_array", 
                   "multi_demensional_array", "array_literal_list", "type_name", 
                   "primitive_type", "array_type", "class_type", "initialization", 
                   "block_statement", "statement", "variable_and_const_declaration", 
                   "assign_statement", "left_hand_side", "if_statement", 
                   "elseif_statement", "else_statement", "foreach_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "method_invocation_statement", "expression", "string_expression", 
                   "relation_expression", "logical_expression", "adding_expression", 
                   "multiplying_expression", "negative_expression", "sign_expression", 
                   "index_expression", "member_access_expression", "self_method_call", 
                   "object_creation_expression", "operand", "list_of_expressions" ]

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
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CLASS:
                self.state = 96
                self.class_declaration()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
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
            self.state = 104
            self.match(D96Parser.CLASS)
            self.state = 105
            self.class_name()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 106
                self.match(D96Parser.COLON)
                self.state = 107
                self.class_name()


            self.state = 110
            self.match(D96Parser.LCB)
            self.state = 111
            self.class_body()
            self.state = 112
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
            self.state = 114
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
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 120
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAR, D96Parser.VAL]:
                    self.state = 116
                    self.attribute_declaration()
                    pass
                elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 117
                    self.method_declaration()
                    pass
                elif token in [D96Parser.CONSTRUCTOR]:
                    self.state = 118
                    self.constructor_declaration()
                    pass
                elif token in [D96Parser.DESTRUCTOR]:
                    self.state = 119
                    self.destructor_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 124
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
            self.state = 125
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 126
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 127
                self.match(D96Parser.COMMA)
                self.state = 128
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(D96Parser.COLON)
            self.state = 135
            self.type_name()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 136
                self.initialization()


            self.state = 139
            self.match(D96Parser.SEMI)
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
        self.enterRule(localctx, 10, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 142
            self.match(D96Parser.LP)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 143
                self.list_of_parameters()


            self.state = 146
            self.match(D96Parser.RP)
            self.state = 147
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
        self.enterRule(localctx, 12, self.RULE_constructor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 150
            self.match(D96Parser.LP)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 151
                self.list_of_parameters()


            self.state = 154
            self.match(D96Parser.RP)
            self.state = 155
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
        self.enterRule(localctx, 14, self.RULE_destructor_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(D96Parser.DESTRUCTOR)
            self.state = 158
            self.match(D96Parser.LP)
            self.state = 159
            self.match(D96Parser.RP)
            self.state = 160
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
        self.enterRule(localctx, 16, self.RULE_list_of_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.parameter_declaration()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 163
                self.match(D96Parser.SEMI)
                self.state = 164
                self.parameter_declaration()
                self.state = 169
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
        self.enterRule(localctx, 18, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(D96Parser.ID)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 171
                self.match(D96Parser.COMMA)
                self.state = 172
                self.match(D96Parser.ID)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(D96Parser.COLON)
            self.state = 179
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
        self.enterRule(localctx, 20, self.RULE_literal)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.array_literal()
                pass
            elif token in [D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
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
        self.enterRule(localctx, 22, self.RULE_primitive_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
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
        self.enterRule(localctx, 24, self.RULE_array_literal)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.indexed_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
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
        self.enterRule(localctx, 26, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(D96Parser.ARRAY)
            self.state = 192
            self.match(D96Parser.LP)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 193
                self.list_of_expressions()


            self.state = 196
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
        self.enterRule(localctx, 28, self.RULE_multi_demensional_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(D96Parser.ARRAY)
            self.state = 199
            self.match(D96Parser.LP)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ARRAY:
                self.state = 200
                self.array_literal_list()


            self.state = 203
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
        self.enterRule(localctx, 30, self.RULE_array_literal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.array_literal()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 206
                self.match(D96Parser.COMMA)
                self.state = 207
                self.array_literal()
                self.state = 212
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
        self.enterRule(localctx, 32, self.RULE_type_name)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
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
        self.enterRule(localctx, 34, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
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
        self.enterRule(localctx, 36, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(D96Parser.ARRAY)
            self.state = 221
            self.match(D96Parser.LSB)
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 222
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 223
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 226
            self.match(D96Parser.COMMA)
            self.state = 227
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 228
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
        self.enterRule(localctx, 38, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 40, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(D96Parser.ASSIGN)
            self.state = 233
            self.list_of_expressions()
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
        self.enterRule(localctx, 42, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(D96Parser.LCB)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.SELF) | (1 << D96Parser.RETURN) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 236
                self.statement()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
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
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.variable_and_const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.foreach_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 249
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 251
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
        self.enterRule(localctx, 46, self.RULE_variable_and_const_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 255
            self.match(D96Parser.ID)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 256
                self.match(D96Parser.COMMA)
                self.state = 257
                self.match(D96Parser.ID)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self.match(D96Parser.COLON)
            self.state = 264
            self.type_name()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 265
                self.initialization()


            self.state = 268
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
        self.enterRule(localctx, 48, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.left_hand_side()
            self.state = 271
            self.match(D96Parser.ASSIGN)
            self.state = 272
            self.expression()
            self.state = 273
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
        self.enterRule(localctx, 50, self.RULE_left_hand_side)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.index_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 278
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
        self.enterRule(localctx, 52, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(D96Parser.IF)
                self.state = 282
                self.match(D96Parser.LP)
                self.state = 283
                self.expression()
                self.state = 284
                self.match(D96Parser.RP)
                self.state = 285
                self.block_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(D96Parser.IF)
                self.state = 288
                self.match(D96Parser.LP)
                self.state = 289
                self.expression()
                self.state = 290
                self.match(D96Parser.RP)
                self.state = 291
                self.block_statement()
                self.state = 292
                self.else_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.match(D96Parser.IF)
                self.state = 295
                self.match(D96Parser.LP)
                self.state = 296
                self.expression()
                self.state = 297
                self.match(D96Parser.RP)
                self.state = 298
                self.block_statement()
                self.state = 300 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 299
                    self.elseif_statement()
                    self.state = 302 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 304
                self.match(D96Parser.IF)
                self.state = 305
                self.match(D96Parser.LP)
                self.state = 306
                self.expression()
                self.state = 307
                self.match(D96Parser.RP)
                self.state = 308
                self.block_statement()
                self.state = 310 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 309
                    self.elseif_statement()
                    self.state = 312 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                self.state = 314
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
        self.enterRule(localctx, 54, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(D96Parser.ELSEIF)
            self.state = 319
            self.match(D96Parser.LP)
            self.state = 320
            self.expression()
            self.state = 321
            self.match(D96Parser.RP)
            self.state = 322
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
        self.enterRule(localctx, 56, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(D96Parser.ELSE)
            self.state = 325
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
        self.enterRule(localctx, 58, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(D96Parser.FOREACH)
            self.state = 328
            self.match(D96Parser.LP)
            self.state = 329
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 330
            self.match(D96Parser.IN)
            self.state = 331
            self.expression()
            self.state = 332
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 333
            self.expression()
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 334
                self.match(D96Parser.BY)
                self.state = 335
                self.expression()


            self.state = 338
            self.match(D96Parser.RP)
            self.state = 339
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
        self.enterRule(localctx, 60, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(D96Parser.BREAK)
            self.state = 342
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
        self.enterRule(localctx, 62, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(D96Parser.CONTINUE)
            self.state = 345
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
        self.enterRule(localctx, 64, self.RULE_return_statement)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(D96Parser.RETURN)
                self.state = 348
                self.expression()
                self.state = 349
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(D96Parser.RETURN)
                self.state = 352
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
        self.enterRule(localctx, 66, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.member_access_expression(0)
            self.state = 356
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
        self.enterRule(localctx, 68, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
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
        self.enterRule(localctx, 70, self.RULE_string_expression)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.relation_expression()
                self.state = 361
                self.match(D96Parser.STRING_ADD)
                self.state = 362
                self.relation_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.relation_expression()
                self.state = 365
                self.match(D96Parser.STRING_EQUAL)
                self.state = 366
                self.relation_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
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
        self.enterRule(localctx, 72, self.RULE_relation_expression)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.logical_expression(0)
                self.state = 372
                self.match(D96Parser.EQUAL)
                self.state = 373
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.logical_expression(0)
                self.state = 376
                self.match(D96Parser.NOT_EQUAL)
                self.state = 377
                self.logical_expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.logical_expression(0)
                self.state = 380
                self.match(D96Parser.LT)
                self.state = 381
                self.logical_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 383
                self.logical_expression(0)
                self.state = 384
                self.match(D96Parser.LTE)
                self.state = 385
                self.logical_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 387
                self.logical_expression(0)
                self.state = 388
                self.match(D96Parser.GT)
                self.state = 389
                self.logical_expression(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 391
                self.logical_expression(0)
                self.state = 392
                self.match(D96Parser.GTE)
                self.state = 393
                self.logical_expression(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 395
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_logical_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 407
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                        self.state = 401
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 402
                        self.match(D96Parser.AND)
                        self.state = 403
                        self.adding_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                        self.state = 404
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 405
                        self.match(D96Parser.OR)
                        self.state = 406
                        self.adding_expression(0)
                        pass

             
                self.state = 411
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_adding_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 421
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                        self.state = 415
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 416
                        self.match(D96Parser.ADD)
                        self.state = 417
                        self.multiplying_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                        self.state = 418
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 419
                        self.match(D96Parser.SUB)
                        self.state = 420
                        self.multiplying_expression(0)
                        pass

             
                self.state = 425
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_multiplying_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.negative_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 438
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                        self.state = 429
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 430
                        self.match(D96Parser.MUL)
                        self.state = 431
                        self.negative_expression()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                        self.state = 432
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 433
                        self.match(D96Parser.DIV)
                        self.state = 434
                        self.negative_expression()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                        self.state = 435
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 436
                        self.match(D96Parser.MOD)
                        self.state = 437
                        self.negative_expression()
                        pass

             
                self.state = 442
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
        self.enterRule(localctx, 80, self.RULE_negative_expression)
        try:
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.match(D96Parser.NOT)
                self.state = 444
                self.negative_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.ARRAY, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.SUB, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
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
        self.enterRule(localctx, 82, self.RULE_sign_expression)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.match(D96Parser.SUB)
                self.state = 449
                self.sign_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.index_expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.member_access_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 452
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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_index_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 456
                self.member_access_expression(0)
                self.state = 457
                self.match(D96Parser.LSB)
                self.state = 458
                self.expression()
                self.state = 459
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.state = 461
                self.match(D96Parser.ID)
                self.state = 462
                self.match(D96Parser.LSB)
                self.state = 463
                self.expression()
                self.state = 464
                self.match(D96Parser.RSB)
                pass

            elif la_ == 3:
                self.state = 466
                self.match(D96Parser.DOLLAR_ID)
                self.state = 467
                self.match(D96Parser.LSB)
                self.state = 468
                self.expression()
                self.state = 469
                self.match(D96Parser.RSB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 480
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression)
                    self.state = 473
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 474
                    self.match(D96Parser.LSB)
                    self.state = 475
                    self.expression()
                    self.state = 476
                    self.match(D96Parser.RSB) 
                self.state = 482
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_member_access_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 484
                self.match(D96Parser.ID)
                self.state = 485
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 486
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.state = 487
                self.match(D96Parser.ID)
                self.state = 488
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 489
                self.match(D96Parser.DOLLAR_ID)
                self.state = 490
                self.match(D96Parser.LP)
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                    self.state = 491
                    self.list_of_expressions()


                self.state = 494
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.state = 495
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 496
                self.match(D96Parser.DOT)
                self.state = 497
                self.match(D96Parser.ID)
                pass

            elif la_ == 4:
                self.state = 498
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 499
                self.match(D96Parser.DOT)
                self.state = 500
                self.match(D96Parser.ID)
                self.state = 501
                self.match(D96Parser.LP)
                self.state = 503
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                    self.state = 502
                    self.list_of_expressions()


                self.state = 505
                self.match(D96Parser.RP)
                pass

            elif la_ == 5:
                self.state = 506
                self.self_method_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 522
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 520
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Member_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expression)
                        self.state = 509
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 510
                        self.match(D96Parser.DOT)
                        self.state = 511
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Member_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expression)
                        self.state = 512
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 513
                        self.match(D96Parser.DOT)
                        self.state = 514
                        self.match(D96Parser.ID)
                        self.state = 515
                        self.match(D96Parser.LP)
                        self.state = 517
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                            self.state = 516
                            self.list_of_expressions()


                        self.state = 519
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 524
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
        self.enterRule(localctx, 88, self.RULE_self_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 526
            self.match(D96Parser.LP)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 527
                self.list_of_expressions()


            self.state = 530
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
        self.enterRule(localctx, 90, self.RULE_object_creation_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(D96Parser.NEW)
            self.state = 533
            self.match(D96Parser.ID)
            self.state = 534
            self.match(D96Parser.LP)
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 535
                self.list_of_expressions()


            self.state = 538
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
        self.enterRule(localctx, 92, self.RULE_operand)
        try:
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.object_creation_expression()
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 542
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 543
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 544
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 545
                self.match(D96Parser.LP)
                self.state = 546
                self.expression()
                self.state = 547
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
        self.enterRule(localctx, 94, self.RULE_list_of_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.expression()
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 552
                self.match(D96Parser.COMMA)
                self.state = 553
                self.expression()
                self.state = 558
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
        self._predicates[37] = self.logical_expression_sempred
        self._predicates[38] = self.adding_expression_sempred
        self._predicates[39] = self.multiplying_expression_sempred
        self._predicates[42] = self.index_expression_sempred
        self._predicates[43] = self.member_access_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def index_expression_sempred(self, localctx:Index_expressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

    def member_access_expression_sempred(self, localctx:Member_access_expressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 6)
         




