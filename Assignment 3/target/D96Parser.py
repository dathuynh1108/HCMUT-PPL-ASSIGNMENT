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
        buf.write("\u0235\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\6\2x\n\2\r\2\16\2y\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0082")
        buf.write("\n\3\3\3\3\3\3\3\3\3\3\4\7\4\u0089\n\4\f\4\16\4\u008c")
        buf.write("\13\4\3\5\3\5\3\5\3\5\5\5\u0092\n\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\7\6\u009b\n\6\f\6\16\6\u009e\13\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\b\5\b\u00a9\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\7\t\u00b2\n\t\f\t\16\t\u00b5\13\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\5\n\u00bd\n\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\5\13\u00c5\n\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\7\r\u00d2\n\r\f\r\16\r\u00d5\13\r\3\16")
        buf.write("\3\16\3\16\7\16\u00da\n\16\f\16\16\16\u00dd\13\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\5\17\u00e5\n\17\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00ed\n\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\5\23\u00f7\n\23\3\24\3\24\3\25\3")
        buf.write("\25\5\25\u00fd\n\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\7\27\u0107\n\27\f\27\16\27\u010a\13\27\3\30\3\30")
        buf.write("\3\30\5\30\u010f\n\30\3\30\3\30\3\31\3\31\3\31\7\31\u0116")
        buf.write("\n\31\f\31\16\31\u0119\13\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u0122\n\33\3\34\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u0129\n\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0131")
        buf.write("\n\35\f\35\16\35\u0134\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\7\36\u013c\n\36\f\36\16\36\u013f\13\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\7\37\u0147\n\37\f\37\16\37\u014a")
        buf.write("\13\37\3 \3 \3 \5 \u014f\n \3!\3!\3!\5!\u0154\n!\3\"\3")
        buf.write("\"\3\"\3\"\5\"\u015a\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\5")
        buf.write("#\u0165\n#\3$\3$\3$\3$\3$\3$\3$\3$\5$\u016f\n$\3$\3$\3")
        buf.write("$\3$\7$\u0175\n$\f$\16$\u0178\13$\3%\3%\3%\3%\3%\5%\u017f")
        buf.write("\n%\3%\3%\3%\3%\3%\5%\u0186\n%\3&\3&\3&\3&\5&\u018c\n")
        buf.write("&\3&\3&\5&\u0190\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5")
        buf.write("\'\u019a\n\'\3(\3(\3(\3(\5(\u01a0\n(\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3,\3,\7,\u01af\n,\f,\16,\u01b2\13,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01bf\n-\3.\3.\3.\3")
        buf.write(".\3.\3.\7.\u01c7\n.\f.\16.\u01ca\13.\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u01dd\n\61\f\61\16\61\u01e0\13\61\3\61\5\61\u01e3\n\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01f7\n\64\3")
        buf.write("\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u0208\n\67\38\38\58\u020c\n")
        buf.write("8\38\38\39\39\39\39\39\59\u0215\n9\39\39\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\5:\u0221\n:\3:\3:\3:\3:\7:\u0227\n:\f:\16:")
        buf.write("\u022a\13:\3;\3;\3;\3;\3;\5;\u0231\n;\3;\3;\3;\2\78:<")
        buf.write("Fr<\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt\2\13\3\2\n\13")
        buf.write("\3\2<=\3\2\26\31\3\2\32\36\3\2./\4\2\'\')-\3\2%&\3\2\37")
        buf.write(" \3\2!#\2\u023b\2w\3\2\2\2\4}\3\2\2\2\6\u008a\3\2\2\2")
        buf.write("\b\u0091\3\2\2\2\n\u0093\3\2\2\2\f\u00a3\3\2\2\2\16\u00a8")
        buf.write("\3\2\2\2\20\u00aa\3\2\2\2\22\u00b9\3\2\2\2\24\u00c1\3")
        buf.write("\2\2\2\26\u00c9\3\2\2\2\30\u00ce\3\2\2\2\32\u00d6\3\2")
        buf.write("\2\2\34\u00e4\3\2\2\2\36\u00e6\3\2\2\2 \u00e8\3\2\2\2")
        buf.write("\"\u00f2\3\2\2\2$\u00f6\3\2\2\2&\u00f8\3\2\2\2(\u00fc")
        buf.write("\3\2\2\2*\u00fe\3\2\2\2,\u0103\3\2\2\2.\u010b\3\2\2\2")
        buf.write("\60\u0112\3\2\2\2\62\u011a\3\2\2\2\64\u0121\3\2\2\2\66")
        buf.write("\u0128\3\2\2\28\u012a\3\2\2\2:\u0135\3\2\2\2<\u0140\3")
        buf.write("\2\2\2>\u014e\3\2\2\2@\u0153\3\2\2\2B\u0159\3\2\2\2D\u0164")
        buf.write("\3\2\2\2F\u0166\3\2\2\2H\u0185\3\2\2\2J\u018f\3\2\2\2")
        buf.write("L\u0199\3\2\2\2N\u019f\3\2\2\2P\u01a1\3\2\2\2R\u01a5\3")
        buf.write("\2\2\2T\u01a9\3\2\2\2V\u01ac\3\2\2\2X\u01be\3\2\2\2Z\u01c0")
        buf.write("\3\2\2\2\\\u01cf\3\2\2\2^\u01d4\3\2\2\2`\u01d6\3\2\2\2")
        buf.write("b\u01e4\3\2\2\2d\u01ea\3\2\2\2f\u01ed\3\2\2\2h\u01fb\3")
        buf.write("\2\2\2j\u01fe\3\2\2\2l\u0207\3\2\2\2n\u020b\3\2\2\2p\u020f")
        buf.write("\3\2\2\2r\u0218\3\2\2\2t\u022b\3\2\2\2vx\5\4\3\2wv\3\2")
        buf.write("\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z{\3\2\2\2{|\7\2\2\3")
        buf.write("|\3\3\2\2\2}~\7\24\2\2~\u0081\7<\2\2\177\u0080\78\2\2")
        buf.write("\u0080\u0082\7<\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2")
        buf.write("\2\2\u0082\u0083\3\2\2\2\u0083\u0084\7:\2\2\u0084\u0085")
        buf.write("\5\6\4\2\u0085\u0086\7;\2\2\u0086\5\3\2\2\2\u0087\u0089")
        buf.write("\5\b\5\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\7\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008d\u0092\5\n\6\2\u008e\u0092\5\22\n")
        buf.write("\2\u008f\u0092\5\24\13\2\u0090\u0092\5\26\f\2\u0091\u008d")
        buf.write("\3\2\2\2\u0091\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\t\3\2\2\2\u0093\u0094\t\2\2\2\u0094")
        buf.write("\u0095\5\f\7\2\u0095\u009c\b\6\1\2\u0096\u0097\7\66\2")
        buf.write("\2\u0097\u0098\5\f\7\2\u0098\u0099\b\6\1\2\u0099\u009b")
        buf.write("\3\2\2\2\u009a\u0096\3\2\2\2\u009b\u009e\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3\2\2\2")
        buf.write("\u009e\u009c\3\2\2\2\u009f\u00a0\78\2\2\u00a0\u00a1\5")
        buf.write("\34\17\2\u00a1\u00a2\5\16\b\2\u00a2\13\3\2\2\2\u00a3\u00a4")
        buf.write("\t\3\2\2\u00a4\r\3\2\2\2\u00a5\u00a6\7(\2\2\u00a6\u00a9")
        buf.write("\5\20\t\2\u00a7\u00a9\7\67\2\2\u00a8\u00a5\3\2\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9\17\3\2\2\2\u00aa\u00ab\5\62\32\2")
        buf.write("\u00ab\u00b3\b\t\1\2\u00ac\u00ad\6\t\2\3\u00ad\u00ae\7")
        buf.write("\66\2\2\u00ae\u00af\5\62\32\2\u00af\u00b0\b\t\1\2\u00b0")
        buf.write("\u00b2\3\2\2\2\u00b1\u00ac\3\2\2\2\u00b2\u00b5\3\2\2\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3")
        buf.write("\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\6\t\3\3\u00b7\u00b8")
        buf.write("\7\67\2\2\u00b8\21\3\2\2\2\u00b9\u00ba\t\3\2\2\u00ba\u00bc")
        buf.write("\7\60\2\2\u00bb\u00bd\5\30\r\2\u00bc\u00bb\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\7\61\2")
        buf.write("\2\u00bf\u00c0\5V,\2\u00c0\23\3\2\2\2\u00c1\u00c2\7\21")
        buf.write("\2\2\u00c2\u00c4\7\60\2\2\u00c3\u00c5\5\30\r\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\7\61\2\2\u00c7\u00c8\5V,\2\u00c8\25\3\2\2\2\u00c9")
        buf.write("\u00ca\7\22\2\2\u00ca\u00cb\7\60\2\2\u00cb\u00cc\7\61")
        buf.write("\2\2\u00cc\u00cd\5V,\2\u00cd\27\3\2\2\2\u00ce\u00d3\5")
        buf.write("\32\16\2\u00cf\u00d0\7\67\2\2\u00d0\u00d2\5\32\16\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\31\3\2\2\2\u00d5\u00d3\3\2")
        buf.write("\2\2\u00d6\u00db\7<\2\2\u00d7\u00d8\7\66\2\2\u00d8\u00da")
        buf.write("\7<\2\2\u00d9\u00d7\3\2\2\2\u00da\u00dd\3\2\2\2\u00db")
        buf.write("\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de\3\2\2\2")
        buf.write("\u00dd\u00db\3\2\2\2\u00de\u00df\78\2\2\u00df\u00e0\5")
        buf.write("\34\17\2\u00e0\33\3\2\2\2\u00e1\u00e5\5\36\20\2\u00e2")
        buf.write("\u00e5\5 \21\2\u00e3\u00e5\5\"\22\2\u00e4\u00e1\3\2\2")
        buf.write("\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\35\3")
        buf.write("\2\2\2\u00e6\u00e7\t\4\2\2\u00e7\37\3\2\2\2\u00e8\u00e9")
        buf.write("\7\25\2\2\u00e9\u00ec\7\62\2\2\u00ea\u00ed\5\36\20\2\u00eb")
        buf.write("\u00ed\5 \21\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00ef\7\66\2\2\u00ef\u00f0")
        buf.write("\7\33\2\2\u00f0\u00f1\7\63\2\2\u00f1!\3\2\2\2\u00f2\u00f3")
        buf.write("\7<\2\2\u00f3#\3\2\2\2\u00f4\u00f7\5(\25\2\u00f5\u00f7")
        buf.write("\5&\24\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("%\3\2\2\2\u00f8\u00f9\t\5\2\2\u00f9\'\3\2\2\2\u00fa\u00fd")
        buf.write("\5*\26\2\u00fb\u00fd\5.\30\2\u00fc\u00fa\3\2\2\2\u00fc")
        buf.write("\u00fb\3\2\2\2\u00fd)\3\2\2\2\u00fe\u00ff\7\25\2\2\u00ff")
        buf.write("\u0100\7\60\2\2\u0100\u0101\5,\27\2\u0101\u0102\7\61\2")
        buf.write("\2\u0102+\3\2\2\2\u0103\u0108\5(\25\2\u0104\u0105\7\66")
        buf.write("\2\2\u0105\u0107\5(\25\2\u0106\u0104\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("-\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\7\25\2\2\u010c")
        buf.write("\u010e\7\60\2\2\u010d\u010f\5\60\31\2\u010e\u010d\3\2")
        buf.write("\2\2\u010e\u010f\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111")
        buf.write("\7\61\2\2\u0111/\3\2\2\2\u0112\u0117\5\62\32\2\u0113\u0114")
        buf.write("\7\66\2\2\u0114\u0116\5\62\32\2\u0115\u0113\3\2\2\2\u0116")
        buf.write("\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2")
        buf.write("\u0118\61\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\5\64")
        buf.write("\33\2\u011b\63\3\2\2\2\u011c\u011d\5\66\34\2\u011d\u011e")
        buf.write("\t\6\2\2\u011e\u011f\5\66\34\2\u011f\u0122\3\2\2\2\u0120")
        buf.write("\u0122\5\66\34\2\u0121\u011c\3\2\2\2\u0121\u0120\3\2\2")
        buf.write("\2\u0122\65\3\2\2\2\u0123\u0124\58\35\2\u0124\u0125\t")
        buf.write("\7\2\2\u0125\u0126\58\35\2\u0126\u0129\3\2\2\2\u0127\u0129")
        buf.write("\58\35\2\u0128\u0123\3\2\2\2\u0128\u0127\3\2\2\2\u0129")
        buf.write("\67\3\2\2\2\u012a\u012b\b\35\1\2\u012b\u012c\5:\36\2\u012c")
        buf.write("\u0132\3\2\2\2\u012d\u012e\f\4\2\2\u012e\u012f\t\b\2\2")
        buf.write("\u012f\u0131\5:\36\2\u0130\u012d\3\2\2\2\u0131\u0134\3")
        buf.write("\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u01339")
        buf.write("\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136\b\36\1\2\u0136")
        buf.write("\u0137\5<\37\2\u0137\u013d\3\2\2\2\u0138\u0139\f\4\2\2")
        buf.write("\u0139\u013a\t\t\2\2\u013a\u013c\5<\37\2\u013b\u0138\3")
        buf.write("\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013e;\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141")
        buf.write("\b\37\1\2\u0141\u0142\5> \2\u0142\u0148\3\2\2\2\u0143")
        buf.write("\u0144\f\4\2\2\u0144\u0145\t\n\2\2\u0145\u0147\5> \2\u0146")
        buf.write("\u0143\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149=\3\2\2\2\u014a\u0148\3\2\2")
        buf.write("\2\u014b\u014c\7$\2\2\u014c\u014f\5> \2\u014d\u014f\5")
        buf.write("@!\2\u014e\u014b\3\2\2\2\u014e\u014d\3\2\2\2\u014f?\3")
        buf.write("\2\2\2\u0150\u0151\7 \2\2\u0151\u0154\5@!\2\u0152\u0154")
        buf.write("\5B\"\2\u0153\u0150\3\2\2\2\u0153\u0152\3\2\2\2\u0154")
        buf.write("A\3\2\2\2\u0155\u0156\5F$\2\u0156\u0157\5D#\2\u0157\u015a")
        buf.write("\3\2\2\2\u0158\u015a\5F$\2\u0159\u0155\3\2\2\2\u0159\u0158")
        buf.write("\3\2\2\2\u015aC\3\2\2\2\u015b\u015c\7\62\2\2\u015c\u015d")
        buf.write("\5\62\32\2\u015d\u015e\7\63\2\2\u015e\u0165\3\2\2\2\u015f")
        buf.write("\u0160\7\62\2\2\u0160\u0161\5\62\32\2\u0161\u0162\7\63")
        buf.write("\2\2\u0162\u0163\5D#\2\u0163\u0165\3\2\2\2\u0164\u015b")
        buf.write("\3\2\2\2\u0164\u015f\3\2\2\2\u0165E\3\2\2\2\u0166\u0167")
        buf.write("\b$\1\2\u0167\u0168\5H%\2\u0168\u0176\3\2\2\2\u0169\u016a")
        buf.write("\f\5\2\2\u016a\u016b\7\64\2\2\u016b\u016c\7<\2\2\u016c")
        buf.write("\u016e\7\60\2\2\u016d\u016f\5\60\31\2\u016e\u016d\3\2")
        buf.write("\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0175")
        buf.write("\7\61\2\2\u0171\u0172\f\4\2\2\u0172\u0173\7\64\2\2\u0173")
        buf.write("\u0175\7<\2\2\u0174\u0169\3\2\2\2\u0174\u0171\3\2\2\2")
        buf.write("\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177G\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a")
        buf.write("\7<\2\2\u017a\u017b\79\2\2\u017b\u017c\7=\2\2\u017c\u017e")
        buf.write("\7\60\2\2\u017d\u017f\5\60\31\2\u017e\u017d\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0186\7\61\2")
        buf.write("\2\u0181\u0182\7<\2\2\u0182\u0183\79\2\2\u0183\u0186\7")
        buf.write("=\2\2\u0184\u0186\5J&\2\u0185\u0179\3\2\2\2\u0185\u0181")
        buf.write("\3\2\2\2\u0185\u0184\3\2\2\2\u0186I\3\2\2\2\u0187\u0188")
        buf.write("\7\20\2\2\u0188\u0189\7<\2\2\u0189\u018b\7\60\2\2\u018a")
        buf.write("\u018c\5\60\31\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2")
        buf.write("\2\u018c\u018d\3\2\2\2\u018d\u0190\7\61\2\2\u018e\u0190")
        buf.write("\5L\'\2\u018f\u0187\3\2\2\2\u018f\u018e\3\2\2\2\u0190")
        buf.write("K\3\2\2\2\u0191\u019a\7<\2\2\u0192\u019a\7\f\2\2\u0193")
        buf.write("\u019a\7\23\2\2\u0194\u019a\5$\23\2\u0195\u0196\7\60\2")
        buf.write("\2\u0196\u0197\5\62\32\2\u0197\u0198\7\61\2\2\u0198\u019a")
        buf.write("\3\2\2\2\u0199\u0191\3\2\2\2\u0199\u0192\3\2\2\2\u0199")
        buf.write("\u0193\3\2\2\2\u0199\u0194\3\2\2\2\u0199\u0195\3\2\2\2")
        buf.write("\u019aM\3\2\2\2\u019b\u01a0\5P)\2\u019c\u01a0\5R*\2\u019d")
        buf.write("\u01a0\5T+\2\u019e\u01a0\7<\2\2\u019f\u019b\3\2\2\2\u019f")
        buf.write("\u019c\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0O\3\2\2\2\u01a1\u01a2\5F$\2\u01a2\u01a3\7\64\2\2")
        buf.write("\u01a3\u01a4\7<\2\2\u01a4Q\3\2\2\2\u01a5\u01a6\7<\2\2")
        buf.write("\u01a6\u01a7\79\2\2\u01a7\u01a8\7=\2\2\u01a8S\3\2\2\2")
        buf.write("\u01a9\u01aa\5F$\2\u01aa\u01ab\5D#\2\u01abU\3\2\2\2\u01ac")
        buf.write("\u01b0\7:\2\2\u01ad\u01af\5X-\2\u01ae\u01ad\3\2\2\2\u01af")
        buf.write("\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2")
        buf.write("\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\7")
        buf.write(";\2\2\u01b4W\3\2\2\2\u01b5\u01bf\5Z.\2\u01b6\u01bf\5\\")
        buf.write("/\2\u01b7\u01bf\5`\61\2\u01b8\u01bf\5f\64\2\u01b9\u01bf")
        buf.write("\5h\65\2\u01ba\u01bf\5j\66\2\u01bb\u01bf\5l\67\2\u01bc")
        buf.write("\u01bf\5n8\2\u01bd\u01bf\5V,\2\u01be\u01b5\3\2\2\2\u01be")
        buf.write("\u01b6\3\2\2\2\u01be\u01b7\3\2\2\2\u01be\u01b8\3\2\2\2")
        buf.write("\u01be\u01b9\3\2\2\2\u01be\u01ba\3\2\2\2\u01be\u01bb\3")
        buf.write("\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfY")
        buf.write("\3\2\2\2\u01c0\u01c1\t\2\2\2\u01c1\u01c2\7<\2\2\u01c2")
        buf.write("\u01c8\b.\1\2\u01c3\u01c4\7\66\2\2\u01c4\u01c5\7<\2\2")
        buf.write("\u01c5\u01c7\b.\1\2\u01c6\u01c3\3\2\2\2\u01c7\u01ca\3")
        buf.write("\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb")
        buf.write("\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\78\2\2\u01cc")
        buf.write("\u01cd\5\34\17\2\u01cd\u01ce\5\16\b\2\u01ce[\3\2\2\2\u01cf")
        buf.write("\u01d0\5^\60\2\u01d0\u01d1\7(\2\2\u01d1\u01d2\5\62\32")
        buf.write("\2\u01d2\u01d3\7\67\2\2\u01d3]\3\2\2\2\u01d4\u01d5\5N")
        buf.write("(\2\u01d5_\3\2\2\2\u01d6\u01d7\7\6\2\2\u01d7\u01d8\7\60")
        buf.write("\2\2\u01d8\u01d9\5\62\32\2\u01d9\u01da\7\61\2\2\u01da")
        buf.write("\u01de\5V,\2\u01db\u01dd\5b\62\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e3\5")
        buf.write("d\63\2\u01e2\u01e1\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3a")
        buf.write("\3\2\2\2\u01e4\u01e5\7\7\2\2\u01e5\u01e6\7\60\2\2\u01e6")
        buf.write("\u01e7\5\62\32\2\u01e7\u01e8\7\61\2\2\u01e8\u01e9\5V,")
        buf.write("\2\u01e9c\3\2\2\2\u01ea\u01eb\7\b\2\2\u01eb\u01ec\5V,")
        buf.write("\2\u01ece\3\2\2\2\u01ed\u01ee\7\t\2\2\u01ee\u01ef\7\60")
        buf.write("\2\2\u01ef\u01f0\7<\2\2\u01f0\u01f1\7\16\2\2\u01f1\u01f2")
        buf.write("\5\62\32\2\u01f2\u01f3\7\65\2\2\u01f3\u01f6\5\62\32\2")
        buf.write("\u01f4\u01f5\7\17\2\2\u01f5\u01f7\5\62\32\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8")
        buf.write("\u01f9\7\61\2\2\u01f9\u01fa\5V,\2\u01fag\3\2\2\2\u01fb")
        buf.write("\u01fc\7\4\2\2\u01fc\u01fd\7\67\2\2\u01fdi\3\2\2\2\u01fe")
        buf.write("\u01ff\7\5\2\2\u01ff\u0200\7\67\2\2\u0200k\3\2\2\2\u0201")
        buf.write("\u0202\7\r\2\2\u0202\u0203\5\62\32\2\u0203\u0204\7\67")
        buf.write("\2\2\u0204\u0208\3\2\2\2\u0205\u0206\7\r\2\2\u0206\u0208")
        buf.write("\7\67\2\2\u0207\u0201\3\2\2\2\u0207\u0205\3\2\2\2\u0208")
        buf.write("m\3\2\2\2\u0209\u020c\5p9\2\u020a\u020c\5t;\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d")
        buf.write("\u020e\7\67\2\2\u020eo\3\2\2\2\u020f\u0210\5r:\2\u0210")
        buf.write("\u0211\7\64\2\2\u0211\u0212\7<\2\2\u0212\u0214\7\60\2")
        buf.write("\2\u0213\u0215\5\60\31\2\u0214\u0213\3\2\2\2\u0214\u0215")
        buf.write("\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\7\61\2\2\u0217")
        buf.write("q\3\2\2\2\u0218\u0219\b:\1\2\u0219\u021a\5H%\2\u021a\u0228")
        buf.write("\3\2\2\2\u021b\u021c\f\5\2\2\u021c\u021d\7\64\2\2\u021d")
        buf.write("\u021e\7<\2\2\u021e\u0220\7\60\2\2\u021f\u0221\5\60\31")
        buf.write("\2\u0220\u021f\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0227\7\61\2\2\u0223\u0224\f\4\2\2\u0224")
        buf.write("\u0225\7\64\2\2\u0225\u0227\7<\2\2\u0226\u021b\3\2\2\2")
        buf.write("\u0226\u0223\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3")
        buf.write("\2\2\2\u0228\u0229\3\2\2\2\u0229s\3\2\2\2\u022a\u0228")
        buf.write("\3\2\2\2\u022b\u022c\7<\2\2\u022c\u022d\79\2\2\u022d\u022e")
        buf.write("\7=\2\2\u022e\u0230\7\60\2\2\u022f\u0231\5\60\31\2\u0230")
        buf.write("\u022f\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232\3\2\2\2")
        buf.write("\u0232\u0233\7\61\2\2\u0233u\3\2\2\2\63y\u0081\u008a\u0091")
        buf.write("\u009c\u00a8\u00b3\u00bc\u00c4\u00d3\u00db\u00e4\u00ec")
        buf.write("\u00f6\u00fc\u0108\u010e\u0117\u0121\u0128\u0132\u013d")
        buf.write("\u0148\u014e\u0153\u0159\u0164\u016e\u0174\u0176\u017e")
        buf.write("\u0185\u018b\u018f\u0199\u019f\u01b0\u01be\u01c8\u01de")
        buf.write("\u01e2\u01f6\u0207\u020b\u0214\u0220\u0226\u0228\u0230")
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
    RULE_class_body = 2
    RULE_class_member_declaration = 3
    RULE_attribute_declaration = 4
    RULE_attribute_name = 5
    RULE_initialization = 6
    RULE_initialization_list = 7
    RULE_method_declaration = 8
    RULE_constructor_declaration = 9
    RULE_destructor_declaration = 10
    RULE_list_of_parameters = 11
    RULE_parameter_declaration = 12
    RULE_type_name = 13
    RULE_primitive_type = 14
    RULE_array_type = 15
    RULE_class_type = 16
    RULE_literal = 17
    RULE_primitive_literal = 18
    RULE_array_literal = 19
    RULE_multi_demensional_array = 20
    RULE_array_literal_list = 21
    RULE_indexed_array = 22
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
    RULE_index_operator = 33
    RULE_instance_access_expression = 34
    RULE_static_access_expression = 35
    RULE_object_creation_expression = 36
    RULE_operand = 37
    RULE_scalar_variable = 38
    RULE_scalar_instance_access = 39
    RULE_scalar_static_access = 40
    RULE_scalar_index = 41
    RULE_block_statement = 42
    RULE_statement = 43
    RULE_variable_and_const_declaration = 44
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

    ruleNames =  [ "program", "class_declaration", "class_body", "class_member_declaration", 
                   "attribute_declaration", "attribute_name", "initialization", 
                   "initialization_list", "method_declaration", "constructor_declaration", 
                   "destructor_declaration", "list_of_parameters", "parameter_declaration", 
                   "type_name", "primitive_type", "array_type", "class_type", 
                   "literal", "primitive_literal", "array_literal", "multi_demensional_array", 
                   "array_literal_list", "indexed_array", "list_of_expressions", 
                   "expression", "string_expression", "relation_expression", 
                   "logical_expression", "adding_expression", "multiplying_expression", 
                   "negative_expression", "sign_expression", "index_expression", 
                   "index_operator", "instance_access_expression", "static_access_expression", 
                   "object_creation_expression", "operand", "scalar_variable", 
                   "scalar_instance_access", "scalar_static_access", "scalar_index", 
                   "block_statement", "statement", "variable_and_const_declaration", 
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

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
            self.state = 123
            self.match(D96Parser.CLASS)
            self.state = 124
            self.match(D96Parser.ID)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 125
                self.match(D96Parser.COLON)
                self.state = 126
                self.match(D96Parser.ID)


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


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_member_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_member_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 133
                self.class_member_declaration()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_member_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Method_declarationContext,0)


        def constructor_declaration(self):
            return self.getTypedRuleContext(D96Parser.Constructor_declarationContext,0)


        def destructor_declaration(self):
            return self.getTypedRuleContext(D96Parser.Destructor_declarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_member_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_member_declaration" ):
                return visitor.visitClass_member_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_member_declaration(self):

        localctx = D96Parser.Class_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_member_declaration)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR, D96Parser.VAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.attribute_declaration()
                pass
            elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.method_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.constructor_declaration()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.destructor_declaration()
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


    class Attribute_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number_attribute = 0

        def attribute_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Attribute_nameContext)
            else:
                return self.getTypedRuleContext(D96Parser.Attribute_nameContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def initialization(self):
            return self.getTypedRuleContext(D96Parser.InitializationContext,0)


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
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 146
            self.attribute_name()
            localctx.number_attribute+=1
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 148
                self.match(D96Parser.COMMA)
                self.state = 149
                self.attribute_name()
                localctx.number_attribute+=1
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(D96Parser.COLON)
            self.state = 158
            self.type_name()
            self.state = 159
            self.initialization(localctx.number_attribute)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = D96Parser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
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


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, number_variable=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number_variable = None
            self.number_variable = number_variable

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def initialization_list(self):
            return self.getTypedRuleContext(D96Parser.Initialization_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self, number_variable):

        localctx = D96Parser.InitializationContext(self, self._ctx, self.state, number_variable)
        self.enterRule(localctx, 12, self.RULE_initialization)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(D96Parser.ASSIGN)
                self.state = 164
                self.initialization_list(localctx.number_variable)
                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
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


    class Initialization_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, number_variable=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number_variable = None
            self.number_variable = number_variable

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
            return D96Parser.RULE_initialization_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization_list" ):
                return visitor.visitInitialization_list(self)
            else:
                return visitor.visitChildren(self)




    def initialization_list(self, number_variable):

        localctx = D96Parser.Initialization_listContext(self, self._ctx, self.state, number_variable)
        self.enterRule(localctx, 14, self.RULE_initialization_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.expression()
            localctx.number_variable -= 1
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 170
                    if not localctx.number_variable > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$number_variable > 0")
                    self.state = 171
                    self.match(D96Parser.COMMA)
                    self.state = 172
                    self.expression()
                    localctx.number_variable -= 1 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 180
            if not localctx.number_variable == 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$number_variable == 0")
            self.state = 181
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
        self.enterRule(localctx, 16, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 18, self.RULE_constructor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 192
            self.match(D96Parser.LP)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 193
                self.list_of_parameters()


            self.state = 196
            self.match(D96Parser.RP)
            self.state = 197
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
        self.enterRule(localctx, 20, self.RULE_destructor_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(D96Parser.DESTRUCTOR)
            self.state = 200
            self.match(D96Parser.LP)
            self.state = 201
            self.match(D96Parser.RP)
            self.state = 202
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
        self.enterRule(localctx, 22, self.RULE_list_of_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.parameter_declaration()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 205
                self.match(D96Parser.SEMI)
                self.state = 206
                self.parameter_declaration()
                self.state = 211
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
        self.enterRule(localctx, 24, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(D96Parser.ID)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 213
                self.match(D96Parser.COMMA)
                self.state = 214
                self.match(D96Parser.ID)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(D96Parser.COLON)
            self.state = 221
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
        self.enterRule(localctx, 26, self.RULE_type_name)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
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
        self.enterRule(localctx, 28, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
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
        self.enterRule(localctx, 30, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(D96Parser.ARRAY)
            self.state = 231
            self.match(D96Parser.LSB)
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 232
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 233
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 236
            self.match(D96Parser.COMMA)
            self.state = 237
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 238
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
        self.enterRule(localctx, 32, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
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
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.array_literal()
                pass
            elif token in [D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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
        self.enterRule(localctx, 36, self.RULE_primitive_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
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

        def multi_demensional_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_demensional_arrayContext,0)


        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_literal)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.multi_demensional_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.indexed_array()
                pass


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

        def array_literal_list(self):
            return self.getTypedRuleContext(D96Parser.Array_literal_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_demensional_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_demensional_array" ):
                return visitor.visitMulti_demensional_array(self)
            else:
                return visitor.visitChildren(self)




    def multi_demensional_array(self):

        localctx = D96Parser.Multi_demensional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_multi_demensional_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(D96Parser.ARRAY)
            self.state = 253
            self.match(D96Parser.LP)
            self.state = 254
            self.array_literal_list()
            self.state = 255
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
        self.enterRule(localctx, 42, self.RULE_array_literal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.array_literal()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 258
                self.match(D96Parser.COMMA)
                self.state = 259
                self.array_literal()
                self.state = 264
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
        self.enterRule(localctx, 44, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(D96Parser.ARRAY)
            self.state = 266
            self.match(D96Parser.LP)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                self.state = 267
                self.list_of_expressions()


            self.state = 270
            self.match(D96Parser.RP)
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
            self.state = 272
            self.expression()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 273
                self.match(D96Parser.COMMA)
                self.state = 274
                self.expression()
                self.state = 279
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
            self.state = 280
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
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.relation_expression()
                self.state = 283
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRING_EQUAL or _la==D96Parser.STRING_ADD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 284
                self.relation_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
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
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.logical_expression(0)
                self.state = 290
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LT) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 291
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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
            self.state = 297
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 301
                    self.adding_expression(0) 
                self.state = 306
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
            self.state = 308
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.multiplying_expression(0) 
                self.state = 317
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
            self.state = 319
            self.negative_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 323
                    self.negative_expression() 
                self.state = 328
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
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(D96Parser.NOT)
                self.state = 330
                self.negative_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.SUB, D96Parser.LP, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(D96Parser.SUB)
                self.state = 335
                self.sign_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.LP, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.index_expression()
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


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)




    def index_expression(self):

        localctx = D96Parser.Index_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_index_expression)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.instance_access_expression(0)
                self.state = 340
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.instance_access_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_index_operator)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(D96Parser.LSB)
                self.state = 346
                self.expression()
                self.state = 347
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(D96Parser.LSB)
                self.state = 350
                self.expression()
                self.state = 351
                self.match(D96Parser.RSB)
                self.state = 352
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_access_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_instance_access_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.static_access_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 370
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Instance_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access_expression)
                        self.state = 359
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 360
                        self.match(D96Parser.DOT)
                        self.state = 361
                        self.match(D96Parser.ID)
                        self.state = 362
                        self.match(D96Parser.LP)
                        self.state = 364
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                            self.state = 363
                            self.list_of_expressions()


                        self.state = 366
                        self.match(D96Parser.RP)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Instance_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access_expression)
                        self.state = 367
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 368
                        self.match(D96Parser.DOT)
                        self.state = 369
                        self.match(D96Parser.ID)
                        pass

             
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_static_access_expression)
        self._la = 0 # Token type
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(D96Parser.ID)
                self.state = 376
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 377
                self.match(D96Parser.DOLLAR_ID)
                self.state = 378
                self.match(D96Parser.LP)
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                    self.state = 379
                    self.list_of_expressions()


                self.state = 382
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(D96Parser.ID)
                self.state = 384
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 385
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
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
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(D96Parser.NEW)
                self.state = 390
                self.match(D96Parser.ID)
                self.state = 391
                self.match(D96Parser.LP)
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                    self.state = 392
                    self.list_of_expressions()


                self.state = 395
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.SELF, D96Parser.NULL, D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.LP, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


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
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.ZERO_INTEGER, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 402
                self.literal()
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 403
                self.match(D96Parser.LP)
                self.state = 404
                self.expression()
                self.state = 405
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def scalar_variable(self):

        localctx = D96Parser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_scalar_variable)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.scalar_instance_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.scalar_static_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.scalar_index()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_instance_access" ):
                return visitor.visitScalar_instance_access(self)
            else:
                return visitor.visitChildren(self)




    def scalar_instance_access(self):

        localctx = D96Parser.Scalar_instance_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_scalar_instance_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.instance_access_expression(0)
            self.state = 416
            self.match(D96Parser.DOT)
            self.state = 417
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_static_accessContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return D96Parser.RULE_scalar_static_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_static_access" ):
                return visitor.visitScalar_static_access(self)
            else:
                return visitor.visitChildren(self)




    def scalar_static_access(self):

        localctx = D96Parser.Scalar_static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_scalar_static_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(D96Parser.ID)
            self.state = 420
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 421
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Instance_access_expressionContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_scalar_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_index" ):
                return visitor.visitScalar_index(self)
            else:
                return visitor.visitChildren(self)




    def scalar_index(self):

        localctx = D96Parser.Scalar_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_scalar_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.instance_access_expression(0)
            self.state = 424
            self.index_operator()
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
        self.enterRule(localctx, 84, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(D96Parser.LCB)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.SELF) | (1 << D96Parser.RETURN) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.LP) | (1 << D96Parser.LCB) | (1 << D96Parser.ID))) != 0):
                self.state = 427
                self.statement()
                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 433
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


        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_statement)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.variable_and_const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 438
                self.foreach_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 440
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 441
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 442
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 443
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


        def initialization(self):
            return self.getTypedRuleContext(D96Parser.InitializationContext,0)


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
        self.enterRule(localctx, 88, self.RULE_variable_and_const_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 447
            self.match(D96Parser.ID)
            self.getInvokingContext(44).number_variable+=1
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 449
                self.match(D96Parser.COMMA)

                self.state = 450
                self.match(D96Parser.ID)
                self.getInvokingContext(44).number_variable+=1
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
            self.match(D96Parser.COLON)
            self.state = 458
            self.type_name()
            self.state = 459
            self.initialization(localctx.number_variable)
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
        self.enterRule(localctx, 90, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.left_hand_side()
            self.state = 462
            self.match(D96Parser.ASSIGN)
            self.state = 463
            self.expression()
            self.state = 464
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

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_left_hand_side

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_hand_side" ):
                return visitor.visitLeft_hand_side(self)
            else:
                return visitor.visitChildren(self)




    def left_hand_side(self):

        localctx = D96Parser.Left_hand_sideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_left_hand_side)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.scalar_variable()
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
        self.enterRule(localctx, 94, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(D96Parser.IF)
            self.state = 469
            self.match(D96Parser.LP)
            self.state = 470
            self.expression()
            self.state = 471
            self.match(D96Parser.RP)
            self.state = 472
            self.block_statement()
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 473
                self.elseif_statement()
                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 479
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
        self.enterRule(localctx, 96, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(D96Parser.ELSEIF)
            self.state = 483
            self.match(D96Parser.LP)
            self.state = 484
            self.expression()
            self.state = 485
            self.match(D96Parser.RP)
            self.state = 486
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
        self.enterRule(localctx, 98, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(D96Parser.ELSE)
            self.state = 489
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach_statement" ):
                return visitor.visitForeach_statement(self)
            else:
                return visitor.visitChildren(self)




    def foreach_statement(self):

        localctx = D96Parser.Foreach_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(D96Parser.FOREACH)
            self.state = 492
            self.match(D96Parser.LP)
            self.state = 493
            self.match(D96Parser.ID)
            self.state = 494
            self.match(D96Parser.IN)
            self.state = 495
            self.expression()
            self.state = 496
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 497
            self.expression()
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 498
                self.match(D96Parser.BY)
                self.state = 499
                self.expression()


            self.state = 502
            self.match(D96Parser.RP)
            self.state = 503
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
        self.enterRule(localctx, 102, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(D96Parser.BREAK)
            self.state = 506
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
        self.enterRule(localctx, 104, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(D96Parser.CONTINUE)
            self.state = 509
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
        self.enterRule(localctx, 106, self.RULE_return_statement)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(D96Parser.RETURN)
                self.state = 512
                self.expression()
                self.state = 513
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(D96Parser.RETURN)
                self.state = 516
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

        def instance_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invocationContext,0)


        def static_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 519
                self.instance_method_invocation()
                pass

            elif la_ == 2:
                self.state = 520
                self.static_method_invocation()
                pass


            self.state = 523
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invocation" ):
                return visitor.visitInstance_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invocation(self):

        localctx = D96Parser.Instance_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_instance_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.prefix_instance_method_invocation(0)
            self.state = 526
            self.match(D96Parser.DOT)
            self.state = 527
            self.match(D96Parser.ID)
            self.state = 528
            self.match(D96Parser.LP)
            self.state = 530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                self.state = 529
                self.list_of_expressions()


            self.state = 532
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_instance_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix_instance_method_invocation" ):
                return visitor.visitPrefix_instance_method_invocation(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 535
            self.static_access_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 550
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 548
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Prefix_instance_method_invocationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_instance_method_invocation)
                        self.state = 537
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 538
                        self.match(D96Parser.DOT)
                        self.state = 539
                        self.match(D96Parser.ID)
                        self.state = 540
                        self.match(D96Parser.LP)
                        self.state = 542
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                            self.state = 541
                            self.list_of_expressions()


                        self.state = 544
                        self.match(D96Parser.RP)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Prefix_instance_method_invocationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_instance_method_invocation)
                        self.state = 545
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 546
                        self.match(D96Parser.DOT)
                        self.state = 547
                        self.match(D96Parser.ID)
                        pass

             
                self.state = 552
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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


        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocation" ):
                return visitor.visitStatic_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocation(self):

        localctx = D96Parser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(D96Parser.ID)
            self.state = 554
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 555
            self.match(D96Parser.DOLLAR_ID)
            self.state = 556
            self.match(D96Parser.LP)
            self.state = 558
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_INTEGER) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                self.state = 557
                self.list_of_expressions()


            self.state = 560
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
        self._predicates[7] = self.initialization_list_sempred
        self._predicates[27] = self.logical_expression_sempred
        self._predicates[28] = self.adding_expression_sempred
        self._predicates[29] = self.multiplying_expression_sempred
        self._predicates[34] = self.instance_access_expression_sempred
        self._predicates[56] = self.prefix_instance_method_invocation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def initialization_list_sempred(self, localctx:Initialization_listContext, predIndex:int):
            if predIndex == 0:
                return localctx.number_variable > 0
         

            if predIndex == 1:
                return localctx.number_variable == 0
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def instance_access_expression_sempred(self, localctx:Instance_access_expressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def prefix_instance_method_invocation_sempred(self, localctx:Prefix_instance_method_invocationContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




