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
        buf.write("\u0262\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\6\2t\n")
        buf.write("\2\r\2\16\2u\3\2\3\2\3\3\3\3\3\3\3\3\5\3~\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u008a\n\5\f\5\16")
        buf.write("\5\u008d\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u0095\n\6\f")
        buf.write("\6\16\6\u0098\13\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u00a1")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00aa\n\b\f\b\16")
        buf.write("\b\u00ad\13\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00b5\n\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\5\n\u00bd\n\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u00ca\n\f\f\f\16")
        buf.write("\f\u00cd\13\f\3\r\3\r\3\r\7\r\u00d2\n\r\f\r\16\r\u00d5")
        buf.write("\13\r\3\r\3\r\3\r\3\16\3\16\3\16\5\16\u00dd\n\16\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\5\20\u00e5\n\20\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\5\22\u00ef\n\22\3\23\3\23")
        buf.write("\3\24\3\24\5\24\u00f5\n\24\3\25\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u00fc\n\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u0109\n\26\f\26\16\26\u010c\13\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u0113\n\27\3\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u011f\n\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0129\n")
        buf.write("\30\7\30\u012b\n\30\f\30\16\30\u012e\13\30\3\31\3\31\3")
        buf.write("\31\7\31\u0133\n\31\f\31\16\31\u0136\13\31\3\32\3\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u013f\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0146\n\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\7\35\u014e\n\35\f\35\16\35\u0151\13\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\7\36\u0159\n\36\f\36\16\36\u015c\13")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0164\n\37\f\37")
        buf.write("\16\37\u0167\13\37\3 \3 \3 \5 \u016c\n \3!\3!\3!\5!\u0171")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u017b\n\"\f\"")
        buf.write("\16\"\u017e\13\"\3#\3#\3#\5#\u0183\n#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\5#\u018d\n#\3#\7#\u0190\n#\f#\16#\u0193\13#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\5$\u019d\n$\3$\3$\5$\u01a1\n$\3")
        buf.write("%\3%\3%\5%\u01a6\n%\3%\3%\3&\3&\3&\3&\5&\u01ae\n&\3&\3")
        buf.write("&\5&\u01b2\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'")
        buf.write("\u01bd\n\'\3(\3(\7(\u01c1\n(\f(\16(\u01c4\13(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\5)\u01d0\n)\3*\3*\3*\3*\3*\3*\7")
        buf.write("*\u01d8\n*\f*\16*\u01db\13*\3*\3*\3*\3*\3+\3+\3+\5+\u01e4")
        buf.write("\n+\3,\3,\3,\3,\3,\3,\3,\7,\u01ed\n,\f,\16,\u01f0\13,")
        buf.write("\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\5.\u01ff\n.\3")
        buf.write("/\3/\3/\3/\3/\3/\7/\u0207\n/\f/\16/\u020a\13/\3/\5/\u020d")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0221\n")
        buf.write("\62\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\5\65\u0232\n\65\3\66\3\66\5")
        buf.write("\66\u0236\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u023f\n\67\3\67\3\67\38\38\38\38\58\u0247\n8\38\38\3")
        buf.write("8\38\38\38\38\38\58\u0251\n8\38\78\u0254\n8\f8\168\u0257")
        buf.write("\138\39\39\39\39\39\59\u025e\n9\39\39\39\2\b8:<BDn:\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\13\3\2\n\13\3\2<=")
        buf.write("\3\2\26\31\3\2\32\36\3\2./\4\2\'\')-\3\2%&\3\2\37 \3\2")
        buf.write("!#\2\u0274\2s\3\2\2\2\4y\3\2\2\2\6\u0083\3\2\2\2\b\u008b")
        buf.write("\3\2\2\2\n\u008e\3\2\2\2\f\u00a0\3\2\2\2\16\u00a2\3\2")
        buf.write("\2\2\20\u00b1\3\2\2\2\22\u00b9\3\2\2\2\24\u00c1\3\2\2")
        buf.write("\2\26\u00c6\3\2\2\2\30\u00ce\3\2\2\2\32\u00dc\3\2\2\2")
        buf.write("\34\u00de\3\2\2\2\36\u00e0\3\2\2\2 \u00ea\3\2\2\2\"\u00ee")
        buf.write("\3\2\2\2$\u00f0\3\2\2\2&\u00f4\3\2\2\2(\u00f6\3\2\2\2")
        buf.write("*\u0101\3\2\2\2,\u010d\3\2\2\2.\u011e\3\2\2\2\60\u012f")
        buf.write("\3\2\2\2\62\u0137\3\2\2\2\64\u013e\3\2\2\2\66\u0145\3")
        buf.write("\2\2\28\u0147\3\2\2\2:\u0152\3\2\2\2<\u015d\3\2\2\2>\u016b")
        buf.write("\3\2\2\2@\u0170\3\2\2\2B\u0172\3\2\2\2D\u0182\3\2\2\2")
        buf.write("F\u01a0\3\2\2\2H\u01a2\3\2\2\2J\u01b1\3\2\2\2L\u01bc\3")
        buf.write("\2\2\2N\u01be\3\2\2\2P\u01cf\3\2\2\2R\u01d1\3\2\2\2T\u01e3")
        buf.write("\3\2\2\2V\u01e5\3\2\2\2X\u01f4\3\2\2\2Z\u01fe\3\2\2\2")
        buf.write("\\\u0200\3\2\2\2^\u020e\3\2\2\2`\u0214\3\2\2\2b\u0217")
        buf.write("\3\2\2\2d\u0225\3\2\2\2f\u0228\3\2\2\2h\u0231\3\2\2\2")
        buf.write("j\u0235\3\2\2\2l\u0239\3\2\2\2n\u0246\3\2\2\2p\u0258\3")
        buf.write("\2\2\2rt\5\4\3\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2\2")
        buf.write("\2vw\3\2\2\2wx\7\2\2\3x\3\3\2\2\2yz\7\24\2\2z}\5\6\4\2")
        buf.write("{|\78\2\2|~\5\6\4\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0080\7:\2\2\u0080\u0081\5\b\5\2\u0081\u0082\7;\2\2\u0082")
        buf.write("\5\3\2\2\2\u0083\u0084\7<\2\2\u0084\7\3\2\2\2\u0085\u008a")
        buf.write("\5\n\6\2\u0086\u008a\5\20\t\2\u0087\u008a\5\22\n\2\u0088")
        buf.write("\u008a\5\24\13\2\u0089\u0085\3\2\2\2\u0089\u0086\3\2\2")
        buf.write("\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\u008d")
        buf.write("\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\t\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\t\2\2\2\u008f")
        buf.write("\u0090\t\3\2\2\u0090\u0096\b\6\1\2\u0091\u0092\7\66\2")
        buf.write("\2\u0092\u0093\t\3\2\2\u0093\u0095\b\6\1\2\u0094\u0091")
        buf.write("\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2\2")
        buf.write("\u0099\u009a\78\2\2\u009a\u009b\5\32\16\2\u009b\u009c")
        buf.write("\5\f\7\2\u009c\13\3\2\2\2\u009d\u009e\7(\2\2\u009e\u00a1")
        buf.write("\5\16\b\2\u009f\u00a1\7\67\2\2\u00a0\u009d\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\r\3\2\2\2\u00a2\u00a3\5\62\32\2\u00a3")
        buf.write("\u00ab\b\b\1\2\u00a4\u00a5\6\b\2\3\u00a5\u00a6\7\66\2")
        buf.write("\2\u00a6\u00a7\5\62\32\2\u00a7\u00a8\b\b\1\2\u00a8\u00aa")
        buf.write("\3\2\2\2\u00a9\u00a4\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2")
        buf.write("\u00ad\u00ab\3\2\2\2\u00ae\u00af\6\b\3\3\u00af\u00b0\7")
        buf.write("\67\2\2\u00b0\17\3\2\2\2\u00b1\u00b2\t\3\2\2\u00b2\u00b4")
        buf.write("\7\60\2\2\u00b3\u00b5\5\26\f\2\u00b4\u00b3\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\7\61\2")
        buf.write("\2\u00b7\u00b8\5N(\2\u00b8\21\3\2\2\2\u00b9\u00ba\7\21")
        buf.write("\2\2\u00ba\u00bc\7\60\2\2\u00bb\u00bd\5\26\f\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\7\61\2\2\u00bf\u00c0\5N(\2\u00c0\23\3\2\2\2\u00c1")
        buf.write("\u00c2\7\22\2\2\u00c2\u00c3\7\60\2\2\u00c3\u00c4\7\61")
        buf.write("\2\2\u00c4\u00c5\5N(\2\u00c5\25\3\2\2\2\u00c6\u00cb\5")
        buf.write("\30\r\2\u00c7\u00c8\7\67\2\2\u00c8\u00ca\5\30\r\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\27\3\2\2\2\u00cd\u00cb\3\2")
        buf.write("\2\2\u00ce\u00d3\7<\2\2\u00cf\u00d0\7\66\2\2\u00d0\u00d2")
        buf.write("\7<\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d6\u00d7\78\2\2\u00d7\u00d8\5")
        buf.write("\32\16\2\u00d8\31\3\2\2\2\u00d9\u00dd\5\34\17\2\u00da")
        buf.write("\u00dd\5\36\20\2\u00db\u00dd\5 \21\2\u00dc\u00d9\3\2\2")
        buf.write("\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\33\3")
        buf.write("\2\2\2\u00de\u00df\t\4\2\2\u00df\35\3\2\2\2\u00e0\u00e1")
        buf.write("\7\25\2\2\u00e1\u00e4\7\62\2\2\u00e2\u00e5\5\34\17\2\u00e3")
        buf.write("\u00e5\5\36\20\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2")
        buf.write("\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\7\66\2\2\u00e7\u00e8")
        buf.write("\7\33\2\2\u00e8\u00e9\7\63\2\2\u00e9\37\3\2\2\2\u00ea")
        buf.write("\u00eb\7<\2\2\u00eb!\3\2\2\2\u00ec\u00ef\5&\24\2\u00ed")
        buf.write("\u00ef\5$\23\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2")
        buf.write("\u00ef#\3\2\2\2\u00f0\u00f1\t\5\2\2\u00f1%\3\2\2\2\u00f2")
        buf.write("\u00f5\5(\25\2\u00f3\u00f5\5,\27\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5\'\3\2\2\2\u00f6\u00f7\7\25")
        buf.write("\2\2\u00f7\u00fb\7\60\2\2\u00f8\u00f9\5*\26\2\u00f9\u00fa")
        buf.write("\b\25\1\2\u00fa\u00fc\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\6\25\4")
        buf.write("\3\u00fe\u00ff\7\61\2\2\u00ff\u0100\b\25\1\2\u0100)\3")
        buf.write("\2\2\2\u0101\u0102\5\62\32\2\u0102\u010a\b\26\1\2\u0103")
        buf.write("\u0104\6\26\5\3\u0104\u0105\7\66\2\2\u0105\u0106\5\62")
        buf.write("\32\2\u0106\u0107\b\26\1\2\u0107\u0109\3\2\2\2\u0108\u0103")
        buf.write("\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b+\3\2\2\2\u010c\u010a\3\2\2\2\u010d")
        buf.write("\u010e\7\25\2\2\u010e\u0112\7\60\2\2\u010f\u0110\5.\30")
        buf.write("\2\u0110\u0111\b\27\1\2\u0111\u0113\3\2\2\2\u0112\u010f")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0115\6\27\6\3\u0115\u0116\7\61\2\2\u0116\u0117\b\27")
        buf.write("\1\2\u0117-\3\2\2\2\u0118\u0119\5(\25\2\u0119\u011a\b")
        buf.write("\30\1\2\u011a\u011f\3\2\2\2\u011b\u011c\5,\27\2\u011c")
        buf.write("\u011d\b\30\1\2\u011d\u011f\3\2\2\2\u011e\u0118\3\2\2")
        buf.write("\2\u011e\u011b\3\2\2\2\u011f\u012c\3\2\2\2\u0120\u0121")
        buf.write("\6\30\7\3\u0121\u0128\7\66\2\2\u0122\u0123\5(\25\2\u0123")
        buf.write("\u0124\b\30\1\2\u0124\u0129\3\2\2\2\u0125\u0126\5,\27")
        buf.write("\2\u0126\u0127\b\30\1\2\u0127\u0129\3\2\2\2\u0128\u0122")
        buf.write("\3\2\2\2\u0128\u0125\3\2\2\2\u0129\u012b\3\2\2\2\u012a")
        buf.write("\u0120\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d/\3\2\2\2\u012e\u012c\3\2\2")
        buf.write("\2\u012f\u0134\5\62\32\2\u0130\u0131\7\66\2\2\u0131\u0133")
        buf.write("\5\62\32\2\u0132\u0130\3\2\2\2\u0133\u0136\3\2\2\2\u0134")
        buf.write("\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\61\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\u0137\u0138\5\64\33\2\u0138\63\3\2\2\2")
        buf.write("\u0139\u013a\5\66\34\2\u013a\u013b\t\6\2\2\u013b\u013c")
        buf.write("\5\66\34\2\u013c\u013f\3\2\2\2\u013d\u013f\5\66\34\2\u013e")
        buf.write("\u0139\3\2\2\2\u013e\u013d\3\2\2\2\u013f\65\3\2\2\2\u0140")
        buf.write("\u0141\58\35\2\u0141\u0142\t\7\2\2\u0142\u0143\58\35\2")
        buf.write("\u0143\u0146\3\2\2\2\u0144\u0146\58\35\2\u0145\u0140\3")
        buf.write("\2\2\2\u0145\u0144\3\2\2\2\u0146\67\3\2\2\2\u0147\u0148")
        buf.write("\b\35\1\2\u0148\u0149\5:\36\2\u0149\u014f\3\2\2\2\u014a")
        buf.write("\u014b\f\4\2\2\u014b\u014c\t\b\2\2\u014c\u014e\5:\36\2")
        buf.write("\u014d\u014a\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3")
        buf.write("\2\2\2\u014f\u0150\3\2\2\2\u01509\3\2\2\2\u0151\u014f")
        buf.write("\3\2\2\2\u0152\u0153\b\36\1\2\u0153\u0154\5<\37\2\u0154")
        buf.write("\u015a\3\2\2\2\u0155\u0156\f\4\2\2\u0156\u0157\t\t\2\2")
        buf.write("\u0157\u0159\5<\37\2\u0158\u0155\3\2\2\2\u0159\u015c\3")
        buf.write("\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b;")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\b\37\1\2\u015e")
        buf.write("\u015f\5> \2\u015f\u0165\3\2\2\2\u0160\u0161\f\4\2\2\u0161")
        buf.write("\u0162\t\n\2\2\u0162\u0164\5> \2\u0163\u0160\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166=\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\7$\2\2")
        buf.write("\u0169\u016c\5> \2\u016a\u016c\5@!\2\u016b\u0168\3\2\2")
        buf.write("\2\u016b\u016a\3\2\2\2\u016c?\3\2\2\2\u016d\u016e\7 \2")
        buf.write("\2\u016e\u0171\5@!\2\u016f\u0171\5B\"\2\u0170\u016d\3")
        buf.write("\2\2\2\u0170\u016f\3\2\2\2\u0171A\3\2\2\2\u0172\u0173")
        buf.write("\b\"\1\2\u0173\u0174\5D#\2\u0174\u017c\3\2\2\2\u0175\u0176")
        buf.write("\f\4\2\2\u0176\u0177\7\62\2\2\u0177\u0178\5\62\32\2\u0178")
        buf.write("\u0179\7\63\2\2\u0179\u017b\3\2\2\2\u017a\u0175\3\2\2")
        buf.write("\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017dC\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0180")
        buf.write("\b#\1\2\u0180\u0183\5H%\2\u0181\u0183\5F$\2\u0182\u017f")
        buf.write("\3\2\2\2\u0182\u0181\3\2\2\2\u0183\u0191\3\2\2\2\u0184")
        buf.write("\u0185\f\6\2\2\u0185\u0186\7\64\2\2\u0186\u0190\7<\2\2")
        buf.write("\u0187\u0188\f\5\2\2\u0188\u0189\7\64\2\2\u0189\u018a")
        buf.write("\7<\2\2\u018a\u018c\7\60\2\2\u018b\u018d\5\60\31\2\u018c")
        buf.write("\u018b\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018e\u0190\7\61\2\2\u018f\u0184\3\2\2\2\u018f\u0187")
        buf.write("\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192E\3\2\2\2\u0193\u0191\3\2\2\2\u0194")
        buf.write("\u0195\7<\2\2\u0195\u0196\79\2\2\u0196\u01a1\7=\2\2\u0197")
        buf.write("\u0198\7<\2\2\u0198\u0199\79\2\2\u0199\u019a\7=\2\2\u019a")
        buf.write("\u019c\7\60\2\2\u019b\u019d\5\60\31\2\u019c\u019b\3\2")
        buf.write("\2\2\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a1")
        buf.write("\7\61\2\2\u019f\u01a1\5J&\2\u01a0\u0194\3\2\2\2\u01a0")
        buf.write("\u0197\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1G\3\2\2\2\u01a2")
        buf.write("\u01a3\t\3\2\2\u01a3\u01a5\7\60\2\2\u01a4\u01a6\5\60\31")
        buf.write("\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7")
        buf.write("\3\2\2\2\u01a7\u01a8\7\61\2\2\u01a8I\3\2\2\2\u01a9\u01aa")
        buf.write("\7\20\2\2\u01aa\u01ab\7<\2\2\u01ab\u01ad\7\60\2\2\u01ac")
        buf.write("\u01ae\5\60\31\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2")
        buf.write("\2\u01ae\u01af\3\2\2\2\u01af\u01b2\7\61\2\2\u01b0\u01b2")
        buf.write("\5L\'\2\u01b1\u01a9\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("K\3\2\2\2\u01b3\u01bd\7=\2\2\u01b4\u01bd\7<\2\2\u01b5")
        buf.write("\u01bd\7\f\2\2\u01b6\u01bd\5\"\22\2\u01b7\u01bd\7\23\2")
        buf.write("\2\u01b8\u01b9\7\60\2\2\u01b9\u01ba\5\62\32\2\u01ba\u01bb")
        buf.write("\7\61\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01b3\3\2\2\2\u01bc")
        buf.write("\u01b4\3\2\2\2\u01bc\u01b5\3\2\2\2\u01bc\u01b6\3\2\2\2")
        buf.write("\u01bc\u01b7\3\2\2\2\u01bc\u01b8\3\2\2\2\u01bdM\3\2\2")
        buf.write("\2\u01be\u01c2\7:\2\2\u01bf\u01c1\5P)\2\u01c0\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3")
        buf.write("\3\2\2\2\u01c3\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5")
        buf.write("\u01c6\7;\2\2\u01c6O\3\2\2\2\u01c7\u01d0\5R*\2\u01c8\u01d0")
        buf.write("\5X-\2\u01c9\u01d0\5\\/\2\u01ca\u01d0\5b\62\2\u01cb\u01d0")
        buf.write("\5d\63\2\u01cc\u01d0\5f\64\2\u01cd\u01d0\5h\65\2\u01ce")
        buf.write("\u01d0\5j\66\2\u01cf\u01c7\3\2\2\2\u01cf\u01c8\3\2\2\2")
        buf.write("\u01cf\u01c9\3\2\2\2\u01cf\u01ca\3\2\2\2\u01cf\u01cb\3")
        buf.write("\2\2\2\u01cf\u01cc\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce")
        buf.write("\3\2\2\2\u01d0Q\3\2\2\2\u01d1\u01d2\t\2\2\2\u01d2\u01d3")
        buf.write("\7<\2\2\u01d3\u01d9\b*\1\2\u01d4\u01d5\7\66\2\2\u01d5")
        buf.write("\u01d6\7<\2\2\u01d6\u01d8\b*\1\2\u01d7\u01d4\3\2\2\2\u01d8")
        buf.write("\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2")
        buf.write("\u01da\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01dd\7")
        buf.write("8\2\2\u01dd\u01de\5\32\16\2\u01de\u01df\5T+\2\u01dfS\3")
        buf.write("\2\2\2\u01e0\u01e1\7(\2\2\u01e1\u01e4\5V,\2\u01e2\u01e4")
        buf.write("\7\67\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4")
        buf.write("U\3\2\2\2\u01e5\u01e6\5\62\32\2\u01e6\u01ee\b,\1\2\u01e7")
        buf.write("\u01e8\6,\16\3\u01e8\u01e9\7\66\2\2\u01e9\u01ea\5\62\32")
        buf.write("\2\u01ea\u01eb\b,\1\2\u01eb\u01ed\3\2\2\2\u01ec\u01e7")
        buf.write("\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01ee\3\2\2\2")
        buf.write("\u01f1\u01f2\6,\17\3\u01f2\u01f3\7\67\2\2\u01f3W\3\2\2")
        buf.write("\2\u01f4\u01f5\5Z.\2\u01f5\u01f6\7(\2\2\u01f6\u01f7\5")
        buf.write("\62\32\2\u01f7\u01f8\7\67\2\2\u01f8Y\3\2\2\2\u01f9\u01ff")
        buf.write("\7<\2\2\u01fa\u01ff\7=\2\2\u01fb\u01ff\5B\"\2\u01fc\u01ff")
        buf.write("\5D#\2\u01fd\u01ff\5F$\2\u01fe\u01f9\3\2\2\2\u01fe\u01fa")
        buf.write("\3\2\2\2\u01fe\u01fb\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe")
        buf.write("\u01fd\3\2\2\2\u01ff[\3\2\2\2\u0200\u0201\7\6\2\2\u0201")
        buf.write("\u0202\7\60\2\2\u0202\u0203\5\62\32\2\u0203\u0204\7\61")
        buf.write("\2\2\u0204\u0208\5N(\2\u0205\u0207\5^\60\2\u0206\u0205")
        buf.write("\3\2\2\2\u0207\u020a\3\2\2\2\u0208\u0206\3\2\2\2\u0208")
        buf.write("\u0209\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020b\u020d\5`\61\2\u020c\u020b\3\2\2\2\u020c\u020d\3")
        buf.write("\2\2\2\u020d]\3\2\2\2\u020e\u020f\7\7\2\2\u020f\u0210")
        buf.write("\7\60\2\2\u0210\u0211\5\62\32\2\u0211\u0212\7\61\2\2\u0212")
        buf.write("\u0213\5N(\2\u0213_\3\2\2\2\u0214\u0215\7\b\2\2\u0215")
        buf.write("\u0216\5N(\2\u0216a\3\2\2\2\u0217\u0218\7\t\2\2\u0218")
        buf.write("\u0219\7\60\2\2\u0219\u021a\t\3\2\2\u021a\u021b\7\16\2")
        buf.write("\2\u021b\u021c\5\62\32\2\u021c\u021d\7\65\2\2\u021d\u0220")
        buf.write("\5\62\32\2\u021e\u021f\7\17\2\2\u021f\u0221\5\62\32\2")
        buf.write("\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222\3")
        buf.write("\2\2\2\u0222\u0223\7\61\2\2\u0223\u0224\5N(\2\u0224c\3")
        buf.write("\2\2\2\u0225\u0226\7\4\2\2\u0226\u0227\7\67\2\2\u0227")
        buf.write("e\3\2\2\2\u0228\u0229\7\5\2\2\u0229\u022a\7\67\2\2\u022a")
        buf.write("g\3\2\2\2\u022b\u022c\7\r\2\2\u022c\u022d\5\62\32\2\u022d")
        buf.write("\u022e\7\67\2\2\u022e\u0232\3\2\2\2\u022f\u0230\7\r\2")
        buf.write("\2\u0230\u0232\7\67\2\2\u0231\u022b\3\2\2\2\u0231\u022f")
        buf.write("\3\2\2\2\u0232i\3\2\2\2\u0233\u0236\5D#\2\u0234\u0236")
        buf.write("\5F$\2\u0235\u0233\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u0238\7\67\2\2\u0238k\3\2\2\2\u0239\u023a")
        buf.write("\5n8\2\u023a\u023b\7\64\2\2\u023b\u023c\7<\2\2\u023c\u023e")
        buf.write("\7\60\2\2\u023d\u023f\5\60\31\2\u023e\u023d\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0241\7\61\2")
        buf.write("\2\u0241m\3\2\2\2\u0242\u0243\b8\1\2\u0243\u0247\7<\2")
        buf.write("\2\u0244\u0247\7=\2\2\u0245\u0247\7\f\2\2\u0246\u0242")
        buf.write("\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0245\3\2\2\2\u0247")
        buf.write("\u0255\3\2\2\2\u0248\u0249\f\7\2\2\u0249\u024a\7\64\2")
        buf.write("\2\u024a\u0254\7<\2\2\u024b\u024c\f\6\2\2\u024c\u024d")
        buf.write("\7\64\2\2\u024d\u024e\7<\2\2\u024e\u0250\7\60\2\2\u024f")
        buf.write("\u0251\5\60\31\2\u0250\u024f\3\2\2\2\u0250\u0251\3\2\2")
        buf.write("\2\u0251\u0252\3\2\2\2\u0252\u0254\7\61\2\2\u0253\u0248")
        buf.write("\3\2\2\2\u0253\u024b\3\2\2\2\u0254\u0257\3\2\2\2\u0255")
        buf.write("\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256o\3\2\2\2\u0257")
        buf.write("\u0255\3\2\2\2\u0258\u0259\5\6\4\2\u0259\u025a\79\2\2")
        buf.write("\u025a\u025b\7=\2\2\u025b\u025d\7\60\2\2\u025c\u025e\5")
        buf.write("\60\31\2\u025d\u025c\3\2\2\2\u025d\u025e\3\2\2\2\u025e")
        buf.write("\u025f\3\2\2\2\u025f\u0260\7\61\2\2\u0260q\3\2\2\2;u}")
        buf.write("\u0089\u008b\u0096\u00a0\u00ab\u00b4\u00bc\u00cb\u00d3")
        buf.write("\u00dc\u00e4\u00ee\u00f4\u00fb\u010a\u0112\u011e\u0128")
        buf.write("\u012c\u0134\u013e\u0145\u014f\u015a\u0165\u016b\u0170")
        buf.write("\u017c\u0182\u018c\u018f\u0191\u019c\u01a0\u01a5\u01ad")
        buf.write("\u01b1\u01bc\u01c2\u01cf\u01d9\u01e3\u01ee\u01fe\u0208")
        buf.write("\u020c\u0220\u0231\u0235\u023e\u0246\u0250\u0253\u0255")
        buf.write("\u025d")
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
    RULE_indexed_array = 19
    RULE_array_list_of_expressions = 20
    RULE_multi_demensional_array = 21
    RULE_array_literal_list = 22
    RULE_list_of_expressions = 23
    RULE_expression = 24
    RULE_string_expression = 25
    RULE_relation_expression = 26
    RULE_logical_expression = 27
    RULE_adding_expression = 28
    RULE_multiplying_expression = 29
    RULE_negative_expression = 30
    RULE_sign_expression = 31
    RULE_index_expression = 32
    RULE_instance_access_expression = 33
    RULE_static_access_expression = 34
    RULE_self_method_call = 35
    RULE_object_creation_expression = 36
    RULE_operand = 37
    RULE_block_statement = 38
    RULE_statement = 39
    RULE_variable_and_const_declaration = 40
    RULE_variable_initialization = 41
    RULE_variable_initialization_list = 42
    RULE_assign_statement = 43
    RULE_left_hand_side = 44
    RULE_if_statement = 45
    RULE_elseif_statement = 46
    RULE_else_statement = 47
    RULE_foreach_statement = 48
    RULE_break_statement = 49
    RULE_continue_statement = 50
    RULE_return_statement = 51
    RULE_method_invocation_statement = 52
    RULE_instance_method_invocation = 53
    RULE_pre_instance_method_invocation = 54
    RULE_static_method_invocation = 55

    ruleNames =  [ "program", "class_declaration", "class_name", "class_body", 
                   "attribute_declaration", "attribute_initialization", 
                   "attribute_initialization_list", "method_declaration", 
                   "constructor_declaration", "destructor_declaration", 
                   "list_of_parameters", "parameter_declaration", "type_name", 
                   "primitive_type", "array_type", "class_type", "literal", 
                   "primitive_literal", "array_literal", "indexed_array", 
                   "array_list_of_expressions", "multi_demensional_array", 
                   "array_literal_list", "list_of_expressions", "expression", 
                   "string_expression", "relation_expression", "logical_expression", 
                   "adding_expression", "multiplying_expression", "negative_expression", 
                   "sign_expression", "index_expression", "instance_access_expression", 
                   "static_access_expression", "self_method_call", "object_creation_expression", 
                   "operand", "block_statement", "statement", "variable_and_const_declaration", 
                   "variable_initialization", "variable_initialization_list", 
                   "assign_statement", "left_hand_side", "if_statement", 
                   "elseif_statement", "else_statement", "foreach_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "method_invocation_statement", "instance_method_invocation", 
                   "pre_instance_method_invocation", "static_method_invocation" ]

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
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.class_declaration()
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 117
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
            self.state = 119
            self.match(D96Parser.CLASS)
            self.state = 120
            self.class_name()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 121
                self.match(D96Parser.COLON)
                self.state = 122
                self.class_name()


            self.state = 125
            self.match(D96Parser.LCB)
            self.state = 126
            self.class_body()
            self.state = 127
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
            self.state = 129
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
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 135
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAR, D96Parser.VAL]:
                    self.state = 131
                    self.attribute_declaration()
                    pass
                elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 132
                    self.method_declaration()
                    pass
                elif token in [D96Parser.CONSTRUCTOR]:
                    self.state = 133
                    self.constructor_declaration()
                    pass
                elif token in [D96Parser.DESTRUCTOR]:
                    self.state = 134
                    self.destructor_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 139
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
            self.state = 140
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 141
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.getInvokingContext(4).number_attribute+=1
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 143
                self.match(D96Parser.COMMA)
                self.state = 144
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.getInvokingContext(4).number_attribute+=1
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(D96Parser.COLON)
            self.state = 152
            self.type_name()
            self.state = 153
            self.attribute_initialization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_initialization" ):
                return visitor.visitAttribute_initialization(self)
            else:
                return visitor.visitChildren(self)




    def attribute_initialization(self):

        localctx = D96Parser.Attribute_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute_initialization)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(D96Parser.ASSIGN)
                self.state = 156
                self.attribute_initialization_list()
                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
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
        __slots__ = 'parser'

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
            return D96Parser.RULE_attribute_initialization_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_initialization_list" ):
                return visitor.visitAttribute_initialization_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_initialization_list(self):

        localctx = D96Parser.Attribute_initialization_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_initialization_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.expression()
            self.getInvokingContext(4).number_attribute -= 1
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 162
                    if not self.getInvokingContext(4).number_attribute > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$attribute_declaration::number_attribute > 0")
                    self.state = 163
                    self.match(D96Parser.COMMA)
                    self.state = 164
                    self.expression()
                    self.getInvokingContext(4).number_attribute -= 1 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 172
            if not self.getInvokingContext(4).number_attribute == 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$attribute_declaration::number_attribute == 0")
            self.state = 173
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
        self.enterRule(localctx, 14, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 176
            self.match(D96Parser.LP)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 177
                self.list_of_parameters()


            self.state = 180
            self.match(D96Parser.RP)
            self.state = 181
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
            self.state = 183
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 184
            self.match(D96Parser.LP)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 185
                self.list_of_parameters()


            self.state = 188
            self.match(D96Parser.RP)
            self.state = 189
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
            self.state = 191
            self.match(D96Parser.DESTRUCTOR)
            self.state = 192
            self.match(D96Parser.LP)
            self.state = 193
            self.match(D96Parser.RP)
            self.state = 194
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
            self.state = 196
            self.parameter_declaration()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 197
                self.match(D96Parser.SEMI)
                self.state = 198
                self.parameter_declaration()
                self.state = 203
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
            self.state = 204
            self.match(D96Parser.ID)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 205
                self.match(D96Parser.COMMA)
                self.state = 206
                self.match(D96Parser.ID)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(D96Parser.COLON)
            self.state = 213
            self.type_name()
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
        self.enterRule(localctx, 24, self.RULE_type_name)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
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
        self.enterRule(localctx, 26, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
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
        self.enterRule(localctx, 28, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(D96Parser.ARRAY)
            self.state = 223
            self.match(D96Parser.LSB)
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 224
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 225
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 228
            self.match(D96Parser.COMMA)
            self.state = 229
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 230
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
        self.enterRule(localctx, 30, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(D96Parser.ID)
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
        self.enterRule(localctx, 32, self.RULE_literal)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.array_literal()
                pass
            elif token in [D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_literal" ):
                return visitor.visitPrimitive_literal(self)
            else:
                return visitor.visitChildren(self)




    def primitive_literal(self):

        localctx = D96Parser.Primitive_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primitive_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
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
        self.enterRule(localctx, 36, self.RULE_array_literal)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.indexed_array(-1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.multi_demensional_array(-1)
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, parent_first_array_size=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.parent_first_array_size = -1
            self.size = 0
            self.list_size = 0
            self._array_list_of_expressions = None # Array_list_of_expressionsContext
            self.parent_first_array_size = parent_first_array_size

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def array_list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.Array_list_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self, parent_first_array_size):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state, parent_first_array_size)
        self.enterRule(localctx, 38, self.RULE_indexed_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(D96Parser.ARRAY)
            self.state = 245
            self.match(D96Parser.LP)
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 246
                localctx._array_list_of_expressions = self.array_list_of_expressions(localctx.parent_first_array_size)
                localctx.list_size = localctx._array_list_of_expressions.size


            self.state = 251
            if not (localctx.parent_first_array_size == -1) | (localctx.list_size == localctx.parent_first_array_size):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "($parent_first_array_size == -1) | ($list_size == $parent_first_array_size)")
            self.state = 252
            self.match(D96Parser.RP)
            localctx.size = localctx.list_size
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_list_of_expressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, parent_first_array_size=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.parent_first_array_size = -1
            self.size = 0
            self.parent_first_array_size = parent_first_array_size

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
            return D96Parser.RULE_array_list_of_expressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list_of_expressions" ):
                return visitor.visitArray_list_of_expressions(self)
            else:
                return visitor.visitChildren(self)




    def array_list_of_expressions(self, parent_first_array_size):

        localctx = D96Parser.Array_list_of_expressionsContext(self, self._ctx, self.state, parent_first_array_size)
        self.enterRule(localctx, 40, self.RULE_array_list_of_expressions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.expression()
            localctx.size += 1
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 257
                    if not (localctx.parent_first_array_size == -1) | (localctx.size < localctx.parent_first_array_size):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "($parent_first_array_size == -1) | ($size < $parent_first_array_size)")
                    self.state = 258
                    self.match(D96Parser.COMMA)
                    self.state = 259
                    self.expression()
                    localctx.size += 1 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_demensional_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, parent_first_array_size=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.parent_first_array_size = -1
            self.size = 0
            self.list_size = 0
            self._array_literal_list = None # Array_literal_listContext
            self.parent_first_array_size = parent_first_array_size

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




    def multi_demensional_array(self, parent_first_array_size):

        localctx = D96Parser.Multi_demensional_arrayContext(self, self._ctx, self.state, parent_first_array_size)
        self.enterRule(localctx, 42, self.RULE_multi_demensional_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(D96Parser.ARRAY)
            self.state = 268
            self.match(D96Parser.LP)
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 269
                localctx._array_literal_list = self.array_literal_list(localctx.parent_first_array_size)
                localctx.list_size = localctx._array_literal_list.size


            self.state = 274
            if not (localctx.parent_first_array_size == -1) | (localctx.list_size == localctx.parent_first_array_size):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "($parent_first_array_size == -1) | ($list_size == $parent_first_array_size)")
            self.state = 275
            self.match(D96Parser.RP)
            localctx.size = localctx.list_size
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, parent_first_array_size=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.parent_first_array_size = -1
            self.size = 0
            self.first_array_size = None
            self._indexed_array = None # Indexed_arrayContext
            self._multi_demensional_array = None # Multi_demensional_arrayContext
            self.parent_first_array_size = parent_first_array_size

        def indexed_array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Indexed_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,i)


        def multi_demensional_array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Multi_demensional_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Multi_demensional_arrayContext,i)


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




    def array_literal_list(self, parent_first_array_size):

        localctx = D96Parser.Array_literal_listContext(self, self._ctx, self.state, parent_first_array_size)
        self.enterRule(localctx, 44, self.RULE_array_literal_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 278
                localctx._indexed_array = self.indexed_array(-1)

                localctx.first_array_size = localctx._indexed_array.size
                localctx.size += 1

                pass

            elif la_ == 2:
                self.state = 281
                localctx._multi_demensional_array = self.multi_demensional_array(-1)

                localctx.first_array_size = localctx._multi_demensional_array.size
                localctx.size += 1

                pass


            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 286
                    if not (localctx.parent_first_array_size == -1) | (localctx.size < localctx.parent_first_array_size):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "($parent_first_array_size == -1) | ($size < $parent_first_array_size)")
                    self.state = 287
                    self.match(D96Parser.COMMA)
                    self.state = 294
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        self.state = 288
                        localctx._indexed_array = self.indexed_array(localctx.first_array_size)
                        localctx.size += 1
                        pass

                    elif la_ == 2:
                        self.state = 291
                        localctx._multi_demensional_array = self.multi_demensional_array(localctx.first_array_size)
                        localctx.size += 1
                        pass

             
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_list_of_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.expression()
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 302
                self.match(D96Parser.COMMA)
                self.state = 303
                self.expression()
                self.state = 308
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
        self.enterRule(localctx, 48, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
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
        self.enterRule(localctx, 50, self.RULE_string_expression)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.relation_expression()
                self.state = 312
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRING_EQUAL or _la==D96Parser.STRING_ADD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 313
                self.relation_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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
        self.enterRule(localctx, 52, self.RULE_relation_expression)
        self._la = 0 # Token type
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.logical_expression(0)
                self.state = 319
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LT) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 320
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 328
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 329
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 330
                    self.adding_expression(0) 
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_adding_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 339
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 340
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 341
                    self.multiplying_expression(0) 
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_multiplying_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.negative_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 350
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 351
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 352
                    self.negative_expression() 
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_negative_expression)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(D96Parser.NOT)
                self.state = 359
                self.negative_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.SUB, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
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


        def getRuleIndex(self):
            return D96Parser.RULE_sign_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expression" ):
                return visitor.visitSign_expression(self)
            else:
                return visitor.visitChildren(self)




    def sign_expression(self):

        localctx = D96Parser.Sign_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_sign_expression)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(D96Parser.SUB)
                self.state = 364
                self.sign_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
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
        __slots__ = 'parser'

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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_index_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.instance_access_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 378
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    self.match(D96Parser.LSB)
                    self.state = 373
                    self.expression()
                    self.state = 374
                    self.match(D96Parser.RSB) 
                self.state = 380
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Instance_access_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def self_method_call(self):
            return self.getTypedRuleContext(D96Parser.Self_method_callContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_access_expression" ):
                return visitor.visitInstance_access_expression(self)
            else:
                return visitor.visitChildren(self)



    def instance_access_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Instance_access_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_instance_access_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 382
                self.self_method_call()
                pass

            elif la_ == 2:
                self.state = 383
                self.static_access_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 397
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Instance_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access_expression)
                        self.state = 386
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 387
                        self.match(D96Parser.DOT)
                        self.state = 388
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Instance_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access_expression)
                        self.state = 389
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 390
                        self.match(D96Parser.DOT)
                        self.state = 391
                        self.match(D96Parser.ID)
                        self.state = 392
                        self.match(D96Parser.LP)
                        self.state = 394
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                            self.state = 393
                            self.list_of_expressions()


                        self.state = 396
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_access_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_access_expression" ):
                return visitor.visitStatic_access_expression(self)
            else:
                return visitor.visitChildren(self)




    def static_access_expression(self):

        localctx = D96Parser.Static_access_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_static_access_expression)
        self._la = 0 # Token type
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(D96Parser.ID)
                self.state = 403
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 404
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(D96Parser.ID)
                self.state = 406
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 407
                self.match(D96Parser.DOLLAR_ID)
                self.state = 408
                self.match(D96Parser.LP)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                    self.state = 409
                    self.list_of_expressions()


                self.state = 412
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
                self.object_creation_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 70, self.RULE_self_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 417
            self.match(D96Parser.LP)
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 418
                self.list_of_expressions()


            self.state = 421
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


        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_creation_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_creation_expression" ):
                return visitor.visitObject_creation_expression(self)
            else:
                return visitor.visitChildren(self)




    def object_creation_expression(self):

        localctx = D96Parser.Object_creation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_object_creation_expression)
        self._la = 0 # Token type
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(D96Parser.NEW)
                self.state = 424
                self.match(D96Parser.ID)
                self.state = 425
                self.match(D96Parser.LP)
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                    self.state = 426
                    self.list_of_expressions()


                self.state = 429
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.SELF, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operand)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 435
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                self.literal()
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 437
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 438
                self.match(D96Parser.LP)
                self.state = 439
                self.expression()
                self.state = 440
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
        self.enterRule(localctx, 76, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(D96Parser.LCB)
            self.state = 448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.SELF) | (1 << D96Parser.RETURN) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 445
                self.statement()
                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 451
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
        self.enterRule(localctx, 78, self.RULE_statement)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.variable_and_const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 455
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 456
                self.foreach_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 457
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 458
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 459
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 460
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_and_const_declaration" ):
                return visitor.visitVariable_and_const_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_and_const_declaration(self):

        localctx = D96Parser.Variable_and_const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_variable_and_const_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 464
            self.match(D96Parser.ID)
            self.getInvokingContext(40).number_variable+=1
            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 466
                self.match(D96Parser.COMMA)

                self.state = 467
                self.match(D96Parser.ID)
                self.getInvokingContext(40).number_variable+=1
                self.state = 473
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 474
            self.match(D96Parser.COLON)
            self.state = 475
            self.type_name()
            self.state = 476
            self.variable_initialization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_initialization" ):
                return visitor.visitVariable_initialization(self)
            else:
                return visitor.visitChildren(self)




    def variable_initialization(self):

        localctx = D96Parser.Variable_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_variable_initialization)
        try:
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(D96Parser.ASSIGN)
                self.state = 479
                self.variable_initialization_list()
                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_initialization_list" ):
                return visitor.visitVariable_initialization_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_initialization_list(self):

        localctx = D96Parser.Variable_initialization_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_variable_initialization_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.expression()
            self.getInvokingContext(40).number_variable -= 1
            self.state = 492
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 485
                    if not self.getInvokingContext(40).number_variable > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$variable_and_const_declaration::number_variable > 0")
                    self.state = 486
                    self.match(D96Parser.COMMA)
                    self.state = 487
                    self.expression()
                    self.getInvokingContext(40).number_variable -= 1 
                self.state = 494
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 495
            if not self.getInvokingContext(40).number_variable == 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$variable_and_const_declaration::number_variable == 0")
            self.state = 496
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
        self.enterRule(localctx, 86, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.left_hand_side()
            self.state = 499
            self.match(D96Parser.ASSIGN)
            self.state = 500
            self.expression()
            self.state = 501
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


        def instance_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Instance_access_expressionContext,0)


        def static_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Static_access_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_left_hand_side

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_hand_side" ):
                return visitor.visitLeft_hand_side(self)
            else:
                return visitor.visitChildren(self)




    def left_hand_side(self):

        localctx = D96Parser.Left_hand_sideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_left_hand_side)
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 505
                self.index_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 506
                self.instance_access_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 507
                self.static_access_expression()
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


        def elseif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elseif_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elseif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(D96Parser.IF)
            self.state = 511
            self.match(D96Parser.LP)
            self.state = 512
            self.expression()
            self.state = 513
            self.match(D96Parser.RP)
            self.state = 514
            self.block_statement()
            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 515
                self.elseif_statement()
                self.state = 520
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 521
                self.else_statement()


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
        self.enterRule(localctx, 92, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(D96Parser.ELSEIF)
            self.state = 525
            self.match(D96Parser.LP)
            self.state = 526
            self.expression()
            self.state = 527
            self.match(D96Parser.RP)
            self.state = 528
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
        self.enterRule(localctx, 94, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(D96Parser.ELSE)
            self.state = 531
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
        self.enterRule(localctx, 96, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(D96Parser.FOREACH)
            self.state = 534
            self.match(D96Parser.LP)
            self.state = 535
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 536
            self.match(D96Parser.IN)
            self.state = 537
            self.expression()
            self.state = 538
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 539
            self.expression()
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 540
                self.match(D96Parser.BY)
                self.state = 541
                self.expression()


            self.state = 544
            self.match(D96Parser.RP)
            self.state = 545
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
        self.enterRule(localctx, 98, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(D96Parser.BREAK)
            self.state = 548
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
        self.enterRule(localctx, 100, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(D96Parser.CONTINUE)
            self.state = 551
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
        self.enterRule(localctx, 102, self.RULE_return_statement)
        try:
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.match(D96Parser.RETURN)
                self.state = 554
                self.expression()
                self.state = 555
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.match(D96Parser.RETURN)
                self.state = 558
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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def instance_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Instance_access_expressionContext,0)


        def static_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Static_access_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 561
                self.instance_access_expression(0)
                pass

            elif la_ == 2:
                self.state = 562
                self.static_access_expression()
                pass


            self.state = 565
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pre_instance_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Pre_instance_method_invocationContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invocation" ):
                return visitor.visitInstance_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invocation(self):

        localctx = D96Parser.Instance_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_instance_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.pre_instance_method_invocation(0)
            self.state = 568
            self.match(D96Parser.DOT)
            self.state = 569
            self.match(D96Parser.ID)
            self.state = 570
            self.match(D96Parser.LP)
            self.state = 572
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 571
                self.list_of_expressions()


            self.state = 574
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pre_instance_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def pre_instance_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Pre_instance_method_invocationContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_pre_instance_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPre_instance_method_invocation" ):
                return visitor.visitPre_instance_method_invocation(self)
            else:
                return visitor.visitChildren(self)



    def pre_instance_method_invocation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Pre_instance_method_invocationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_pre_instance_method_invocation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.state = 577
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.state = 578
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.state = 579
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 595
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 593
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Pre_instance_method_invocationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pre_instance_method_invocation)
                        self.state = 582
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 583
                        self.match(D96Parser.DOT)
                        self.state = 584
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Pre_instance_method_invocationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pre_instance_method_invocation)
                        self.state = 585
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 586
                        self.match(D96Parser.DOT)
                        self.state = 587
                        self.match(D96Parser.ID)
                        self.state = 588
                        self.match(D96Parser.LP)
                        self.state = 590
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                            self.state = 589
                            self.list_of_expressions()


                        self.state = 592
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 597
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocation" ):
                return visitor.visitStatic_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocation(self):

        localctx = D96Parser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.class_name()
            self.state = 599
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 600
            self.match(D96Parser.DOLLAR_ID)
            self.state = 601
            self.match(D96Parser.LP)
            self.state = 603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 602
                self.list_of_expressions()


            self.state = 605
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
        self._predicates[6] = self.attribute_initialization_list_sempred
        self._predicates[19] = self.indexed_array_sempred
        self._predicates[20] = self.array_list_of_expressions_sempred
        self._predicates[21] = self.multi_demensional_array_sempred
        self._predicates[22] = self.array_literal_list_sempred
        self._predicates[27] = self.logical_expression_sempred
        self._predicates[28] = self.adding_expression_sempred
        self._predicates[29] = self.multiplying_expression_sempred
        self._predicates[32] = self.index_expression_sempred
        self._predicates[33] = self.instance_access_expression_sempred
        self._predicates[42] = self.variable_initialization_list_sempred
        self._predicates[54] = self.pre_instance_method_invocation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def attribute_initialization_list_sempred(self, localctx:Attribute_initialization_listContext, predIndex:int):
            if predIndex == 0:
                return self.getInvokingContext(4).number_attribute > 0
         

            if predIndex == 1:
                return self.getInvokingContext(4).number_attribute == 0
         

    def indexed_array_sempred(self, localctx:Indexed_arrayContext, predIndex:int):
            if predIndex == 2:
                return (localctx.parent_first_array_size == -1) | (localctx.list_size == localctx.parent_first_array_size)
         

    def array_list_of_expressions_sempred(self, localctx:Array_list_of_expressionsContext, predIndex:int):
            if predIndex == 3:
                return (localctx.parent_first_array_size == -1) | (localctx.size < localctx.parent_first_array_size)
         

    def multi_demensional_array_sempred(self, localctx:Multi_demensional_arrayContext, predIndex:int):
            if predIndex == 4:
                return (localctx.parent_first_array_size == -1) | (localctx.list_size == localctx.parent_first_array_size)
         

    def array_literal_list_sempred(self, localctx:Array_literal_listContext, predIndex:int):
            if predIndex == 5:
                return (localctx.parent_first_array_size == -1) | (localctx.size < localctx.parent_first_array_size)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def index_expression_sempred(self, localctx:Index_expressionContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def instance_access_expression_sempred(self, localctx:Instance_access_expressionContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

    def variable_initialization_list_sempred(self, localctx:Variable_initialization_listContext, predIndex:int):
            if predIndex == 12:
                return self.getInvokingContext(40).number_variable > 0
         

            if predIndex == 13:
                return self.getInvokingContext(40).number_variable == 0
         

    def pre_instance_method_invocation_sempred(self, localctx:Pre_instance_method_invocationContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 4)
         




