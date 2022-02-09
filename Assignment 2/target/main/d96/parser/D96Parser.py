# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u0203\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3v\n\3\3\4\3\4\3\4\3\4\5\4|\n\4\3\4\3\4\3\4\5\4")
        buf.write("\u0081\n\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u008c")
        buf.write("\n\6\3\7\3\7\5\7\u0090\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u0099\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00a3")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00ab\n\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00b2\n\f\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00b9\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00c0\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\7\17\u00c8\n\17\f\17\16\17")
        buf.write("\u00cb\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00d3")
        buf.write("\n\20\f\20\16\20\u00d6\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00de\n\21\f\21\16\21\u00e1\13\21\3\22\3\22")
        buf.write("\3\22\5\22\u00e6\n\22\3\23\3\23\3\23\5\23\u00eb\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\7\24\u00f2\n\24\f\24\16\24\u00f5")
        buf.write("\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00fd\n\25\f")
        buf.write("\25\16\25\u0100\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u0108\n\26\f\26\16\26\u010b\13\26\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u0111\n\27\3\30\3\30\3\30\5\30\u0116\n\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u012b\n\30\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0131\n\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u0139\n\32\3\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0143\n\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\5\35\u014c\n\35\3\35\3\35\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u0154\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u015e\n\37\3 \3 \3 \3 \3 \5 \u0165\n \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3!\3!\5!\u0172\n!\3!\3!\3!\5!\u0177")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0181\n\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u018d\n#\3#\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\5\'\u019e\n\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3)\5)\u01ac\n)\3*\3*\3+\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\5,\u01ba\n,\3-\3-\5-\u01be\n-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\5/\u01cc\n/\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u01dc\n\62\3\63\3\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01ec")
        buf.write("\n\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01f6")
        buf.write("\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u01ff\n")
        buf.write("\67\3\67\3\67\3\67\2\b\34\36 &(*8\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjl\2\f\3\2\25\26\3\2\62\63\3\2!\"\4\2\34 ")
        buf.write("..\3\2,-\3\2&\'\3\2(*\3\2=>\4\2\27\30\62\63\5\2\n\13\60")
        buf.write("\60\64\65\2\u0217\2n\3\2\2\2\4u\3\2\2\2\6w\3\2\2\2\b\u0084")
        buf.write("\3\2\2\2\n\u008b\3\2\2\2\f\u008f\3\2\2\2\16\u0091\3\2")
        buf.write("\2\2\20\u009c\3\2\2\2\22\u00a2\3\2\2\2\24\u00aa\3\2\2")
        buf.write("\2\26\u00b1\3\2\2\2\30\u00b8\3\2\2\2\32\u00bf\3\2\2\2")
        buf.write("\34\u00c1\3\2\2\2\36\u00cc\3\2\2\2 \u00d7\3\2\2\2\"\u00e5")
        buf.write("\3\2\2\2$\u00ea\3\2\2\2&\u00ec\3\2\2\2(\u00f6\3\2\2\2")
        buf.write("*\u0101\3\2\2\2,\u0110\3\2\2\2.\u012a\3\2\2\2\60\u012c")
        buf.write("\3\2\2\2\62\u0134\3\2\2\2\64\u0142\3\2\2\2\66\u0144\3")
        buf.write("\2\2\28\u0148\3\2\2\2:\u0153\3\2\2\2<\u015d\3\2\2\2>\u0164")
        buf.write("\3\2\2\2@\u016a\3\2\2\2B\u0180\3\2\2\2D\u0182\3\2\2\2")
        buf.write("F\u0191\3\2\2\2H\u0194\3\2\2\2J\u0197\3\2\2\2L\u019d\3")
        buf.write("\2\2\2N\u01a1\3\2\2\2P\u01ab\3\2\2\2R\u01ad\3\2\2\2T\u01af")
        buf.write("\3\2\2\2V\u01b9\3\2\2\2X\u01bd\3\2\2\2Z\u01bf\3\2\2\2")
        buf.write("\\\u01cb\3\2\2\2^\u01cd\3\2\2\2`\u01cf\3\2\2\2b\u01db")
        buf.write("\3\2\2\2d\u01dd\3\2\2\2f\u01e1\3\2\2\2h\u01e5\3\2\2\2")
        buf.write("j\u01ef\3\2\2\2l\u01f9\3\2\2\2no\5\4\3\2op\7\2\2\3p\3")
        buf.write("\3\2\2\2qr\5\6\4\2rs\5\4\3\2sv\3\2\2\2tv\5\6\4\2uq\3\2")
        buf.write("\2\2ut\3\2\2\2v\5\3\2\2\2wx\7\24\2\2x{\7\63\2\2y|\5\b")
        buf.write("\5\2z|\3\2\2\2{y\3\2\2\2{z\3\2\2\2|}\3\2\2\2}\u0080\7")
        buf.write("A\2\2~\u0081\5\n\6\2\177\u0081\3\2\2\2\u0080~\3\2\2\2")
        buf.write("\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\7B")
        buf.write("\2\2\u0083\7\3\2\2\2\u0084\u0085\7E\2\2\u0085\u0086\7")
        buf.write("\63\2\2\u0086\t\3\2\2\2\u0087\u0088\5\f\7\2\u0088\u0089")
        buf.write("\5\n\6\2\u0089\u008c\3\2\2\2\u008a\u008c\5\f\7\2\u008b")
        buf.write("\u0087\3\2\2\2\u008b\u008a\3\2\2\2\u008c\13\3\2\2\2\u008d")
        buf.write("\u0090\5\16\b\2\u008e\u0090\5\62\32\2\u008f\u008d\3\2")
        buf.write("\2\2\u008f\u008e\3\2\2\2\u0090\r\3\2\2\2\u0091\u0092\5")
        buf.write("\20\t\2\u0092\u0093\5\22\n\2\u0093\u0094\7E\2\2\u0094")
        buf.write("\u0098\5\24\13\2\u0095\u0096\7/\2\2\u0096\u0099\5\26\f")
        buf.write("\2\u0097\u0099\3\2\2\2\u0098\u0095\3\2\2\2\u0098\u0097")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\7C\2\2\u009b")
        buf.write("\17\3\2\2\2\u009c\u009d\t\2\2\2\u009d\21\3\2\2\2\u009e")
        buf.write("\u009f\t\3\2\2\u009f\u00a0\7D\2\2\u00a0\u00a3\5\22\n\2")
        buf.write("\u00a1\u00a3\t\3\2\2\u00a2\u009e\3\2\2\2\u00a2\u00a1\3")
        buf.write("\2\2\2\u00a3\23\3\2\2\2\u00a4\u00ab\7\20\2\2\u00a5\u00ab")
        buf.write("\7\16\2\2\u00a6\u00ab\7\17\2\2\u00a7\u00ab\7\21\2\2\u00a8")
        buf.write("\u00ab\5Z.\2\u00a9\u00ab\7\63\2\2\u00aa\u00a4\3\2\2\2")
        buf.write("\u00aa\u00a5\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00a7\3")
        buf.write("\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\25")
        buf.write("\3\2\2\2\u00ac\u00ad\5\30\r\2\u00ad\u00ae\7D\2\2\u00ae")
        buf.write("\u00af\5\26\f\2\u00af\u00b2\3\2\2\2\u00b0\u00b2\5\30\r")
        buf.write("\2\u00b1\u00ac\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\27\3")
        buf.write("\2\2\2\u00b3\u00b4\5\32\16\2\u00b4\u00b5\t\4\2\2\u00b5")
        buf.write("\u00b6\5\32\16\2\u00b6\u00b9\3\2\2\2\u00b7\u00b9\5\32")
        buf.write("\16\2\u00b8\u00b3\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\31")
        buf.write("\3\2\2\2\u00ba\u00bb\5\34\17\2\u00bb\u00bc\t\5\2\2\u00bc")
        buf.write("\u00bd\5\34\17\2\u00bd\u00c0\3\2\2\2\u00be\u00c0\5\34")
        buf.write("\17\2\u00bf\u00ba\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\33")
        buf.write("\3\2\2\2\u00c1\u00c2\b\17\1\2\u00c2\u00c3\5\36\20\2\u00c3")
        buf.write("\u00c9\3\2\2\2\u00c4\u00c5\f\4\2\2\u00c5\u00c6\t\6\2\2")
        buf.write("\u00c6\u00c8\5\36\20\2\u00c7\u00c4\3\2\2\2\u00c8\u00cb")
        buf.write("\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\35\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\b\20\1\2\u00cd")
        buf.write("\u00ce\5 \21\2\u00ce\u00d4\3\2\2\2\u00cf\u00d0\f\4\2\2")
        buf.write("\u00d0\u00d1\t\7\2\2\u00d1\u00d3\5 \21\2\u00d2\u00cf\3")
        buf.write("\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\37\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8")
        buf.write("\b\21\1\2\u00d8\u00d9\5\"\22\2\u00d9\u00df\3\2\2\2\u00da")
        buf.write("\u00db\f\4\2\2\u00db\u00dc\t\b\2\2\u00dc\u00de\5\"\22")
        buf.write("\2\u00dd\u00da\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0!\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e2\u00e3\7+\2\2\u00e3\u00e6\5\"\22\2\u00e4")
        buf.write("\u00e6\5$\23\2\u00e5\u00e2\3\2\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6#\3\2\2\2\u00e7\u00e8\7\'\2\2\u00e8\u00eb\5$\23")
        buf.write("\2\u00e9\u00eb\5&\24\2\u00ea\u00e7\3\2\2\2\u00ea\u00e9")
        buf.write("\3\2\2\2\u00eb%\3\2\2\2\u00ec\u00ed\b\24\1\2\u00ed\u00ee")
        buf.write("\5(\25\2\u00ee\u00f3\3\2\2\2\u00ef\u00f0\f\4\2\2\u00f0")
        buf.write("\u00f2\t\t\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f5\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\'\3\2\2")
        buf.write("\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\b\25\1\2\u00f7\u00f8")
        buf.write("\5*\26\2\u00f8\u00fe\3\2\2\2\u00f9\u00fa\f\4\2\2\u00fa")
        buf.write("\u00fb\7#\2\2\u00fb\u00fd\5*\26\2\u00fc\u00f9\3\2\2\2")
        buf.write("\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3")
        buf.write("\2\2\2\u00ff)\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102")
        buf.write("\b\26\1\2\u0102\u0103\5,\27\2\u0103\u0109\3\2\2\2\u0104")
        buf.write("\u0105\f\4\2\2\u0105\u0106\7$\2\2\u0106\u0108\5*\26\5")
        buf.write("\u0107\u0104\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u0109\u010a\3\2\2\2\u010a+\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010c\u010d\7\31\2\2\u010d\u010e\7\63\2\2\u010e")
        buf.write("\u0111\5,\27\2\u010f\u0111\5.\30\2\u0110\u010c\3\2\2\2")
        buf.write("\u0110\u010f\3\2\2\2\u0111-\3\2\2\2\u0112\u0115\7?\2\2")
        buf.write("\u0113\u0116\5\30\r\2\u0114\u0116\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u012b\7@\2\2\u0118\u012b\7\23\2\2\u0119\u012b\7\65\2")
        buf.write("\2\u011a\u012b\7\64\2\2\u011b\u012b\7\n\2\2\u011c\u012b")
        buf.write("\7\13\2\2\u011d\u012b\7\60\2\2\u011e\u012b\7\63\2\2\u011f")
        buf.write("\u012b\7\62\2\2\u0120\u012b\5T+\2\u0121\u012b\5N(\2\u0122")
        buf.write("\u012b\5\60\31\2\u0123\u012b\5l\67\2\u0124\u012b\7\33")
        buf.write("\2\2\u0125\u012b\5h\65\2\u0126\u012b\5j\66\2\u0127\u012b")
        buf.write("\5d\63\2\u0128\u012b\5f\64\2\u0129\u012b\5`\61\2\u012a")
        buf.write("\u0112\3\2\2\2\u012a\u0118\3\2\2\2\u012a\u0119\3\2\2\2")
        buf.write("\u012a\u011a\3\2\2\2\u012a\u011b\3\2\2\2\u012a\u011c\3")
        buf.write("\2\2\2\u012a\u011d\3\2\2\2\u012a\u011e\3\2\2\2\u012a\u011f")
        buf.write("\3\2\2\2\u012a\u0120\3\2\2\2\u012a\u0121\3\2\2\2\u012a")
        buf.write("\u0122\3\2\2\2\u012a\u0123\3\2\2\2\u012a\u0124\3\2\2\2")
        buf.write("\u012a\u0125\3\2\2\2\u012a\u0126\3\2\2\2\u012a\u0127\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b/")
        buf.write("\3\2\2\2\u012c\u012d\7\63\2\2\u012d\u0130\7?\2\2\u012e")
        buf.write("\u0131\5\26\f\2\u012f\u0131\3\2\2\2\u0130\u012e\3\2\2")
        buf.write("\2\u0130\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133")
        buf.write("\7@\2\2\u0133\61\3\2\2\2\u0134\u0135\t\n\2\2\u0135\u0138")
        buf.write("\7?\2\2\u0136\u0139\5\64\33\2\u0137\u0139\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0138\u0137\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a\u013b\7@\2\2\u013b\u013c\58\35\2\u013c\63\3\2\2")
        buf.write("\2\u013d\u013e\5\66\34\2\u013e\u013f\7C\2\2\u013f\u0140")
        buf.write("\5\64\33\2\u0140\u0143\3\2\2\2\u0141\u0143\5\66\34\2\u0142")
        buf.write("\u013d\3\2\2\2\u0142\u0141\3\2\2\2\u0143\65\3\2\2\2\u0144")
        buf.write("\u0145\5\22\n\2\u0145\u0146\7E\2\2\u0146\u0147\5\24\13")
        buf.write("\2\u0147\67\3\2\2\2\u0148\u014b\7A\2\2\u0149\u014c\5:")
        buf.write("\36\2\u014a\u014c\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\7B\2\2\u014e")
        buf.write("9\3\2\2\2\u014f\u0150\5<\37\2\u0150\u0151\5:\36\2\u0151")
        buf.write("\u0154\3\2\2\2\u0152\u0154\5<\37\2\u0153\u014f\3\2\2\2")
        buf.write("\u0153\u0152\3\2\2\2\u0154;\3\2\2\2\u0155\u015e\5\16\b")
        buf.write("\2\u0156\u015e\5> \2\u0157\u015e\5@!\2\u0158\u015e\5D")
        buf.write("#\2\u0159\u015e\5F$\2\u015a\u015e\5H%\2\u015b\u015e\5")
        buf.write("J&\2\u015c\u015e\5L\'\2\u015d\u0155\3\2\2\2\u015d\u0156")
        buf.write("\3\2\2\2\u015d\u0157\3\2\2\2\u015d\u0158\3\2\2\2\u015d")
        buf.write("\u0159\3\2\2\2\u015d\u015a\3\2\2\2\u015d\u015b\3\2\2\2")
        buf.write("\u015d\u015c\3\2\2\2\u015e=\3\2\2\2\u015f\u0165\5`\61")
        buf.write("\2\u0160\u0165\5d\63\2\u0161\u0165\5f\64\2\u0162\u0165")
        buf.write("\7\63\2\2\u0163\u0165\7\62\2\2\u0164\u015f\3\2\2\2\u0164")
        buf.write("\u0160\3\2\2\2\u0164\u0161\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\7")
        buf.write("/\2\2\u0167\u0168\5\30\r\2\u0168\u0169\7C\2\2\u0169?\3")
        buf.write("\2\2\2\u016a\u016b\7\6\2\2\u016b\u016c\7?\2\2\u016c\u016d")
        buf.write("\5\30\r\2\u016d\u016e\7@\2\2\u016e\u0171\58\35\2\u016f")
        buf.write("\u0172\5B\"\2\u0170\u0172\3\2\2\2\u0171\u016f\3\2\2\2")
        buf.write("\u0171\u0170\3\2\2\2\u0172\u0176\3\2\2\2\u0173\u0174\7")
        buf.write("\b\2\2\u0174\u0177\58\35\2\u0175\u0177\3\2\2\2\u0176\u0173")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177A\3\2\2\2\u0178\u0179")
        buf.write("\7\7\2\2\u0179\u017a\7?\2\2\u017a\u017b\5\30\r\2\u017b")
        buf.write("\u017c\7@\2\2\u017c\u017d\58\35\2\u017d\u017e\5B\"\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u0178\3\2\2\2")
        buf.write("\u0180\u017f\3\2\2\2\u0181C\3\2\2\2\u0182\u0183\7\t\2")
        buf.write("\2\u0183\u0184\7?\2\2\u0184\u0185\t\3\2\2\u0185\u0186")
        buf.write("\7\r\2\2\u0186\u0187\7\65\2\2\u0187\u0188\7\3\2\2\u0188")
        buf.write("\u018c\7\65\2\2\u0189\u018a\7\32\2\2\u018a\u018d\7\65")
        buf.write("\2\2\u018b\u018d\3\2\2\2\u018c\u0189\3\2\2\2\u018c\u018b")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\7@\2\2\u018f")
        buf.write("\u0190\58\35\2\u0190E\3\2\2\2\u0191\u0192\7\4\2\2\u0192")
        buf.write("\u0193\7C\2\2\u0193G\3\2\2\2\u0194\u0195\7\5\2\2\u0195")
        buf.write("\u0196\7C\2\2\u0196I\3\2\2\2\u0197\u0198\7\22\2\2\u0198")
        buf.write("\u0199\5\30\r\2\u0199\u019a\7C\2\2\u019aK\3\2\2\2\u019b")
        buf.write("\u019e\5j\66\2\u019c\u019e\5h\65\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\7")
        buf.write("C\2\2\u01a0M\3\2\2\2\u01a1\u01a2\7\f\2\2\u01a2\u01a3\7")
        buf.write("?\2\2\u01a3\u01a4\5P)\2\u01a4\u01a5\7@\2\2\u01a5O\3\2")
        buf.write("\2\2\u01a6\u01a7\5R*\2\u01a7\u01a8\7D\2\2\u01a8\u01a9")
        buf.write("\5P)\2\u01a9\u01ac\3\2\2\2\u01aa\u01ac\5R*\2\u01ab\u01a6")
        buf.write("\3\2\2\2\u01ab\u01aa\3\2\2\2\u01acQ\3\2\2\2\u01ad\u01ae")
        buf.write("\t\13\2\2\u01aeS\3\2\2\2\u01af\u01b0\7\f\2\2\u01b0\u01b1")
        buf.write("\7?\2\2\u01b1\u01b2\5V,\2\u01b2\u01b3\7@\2\2\u01b3U\3")
        buf.write("\2\2\2\u01b4\u01b5\5X-\2\u01b5\u01b6\7D\2\2\u01b6\u01b7")
        buf.write("\5V,\2\u01b7\u01ba\3\2\2\2\u01b8\u01ba\5X-\2\u01b9\u01b4")
        buf.write("\3\2\2\2\u01b9\u01b8\3\2\2\2\u01baW\3\2\2\2\u01bb\u01be")
        buf.write("\5T+\2\u01bc\u01be\5N(\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc")
        buf.write("\3\2\2\2\u01beY\3\2\2\2\u01bf\u01c0\7\f\2\2\u01c0\u01c1")
        buf.write("\7=\2\2\u01c1\u01c2\5\\/\2\u01c2\u01c3\7D\2\2\u01c3\u01c4")
        buf.write("\5^\60\2\u01c4\u01c5\7>\2\2\u01c5[\3\2\2\2\u01c6\u01cc")
        buf.write("\7\16\2\2\u01c7\u01cc\7\17\2\2\u01c8\u01cc\7\20\2\2\u01c9")
        buf.write("\u01cc\5Z.\2\u01ca\u01cc\7\21\2\2\u01cb\u01c6\3\2\2\2")
        buf.write("\u01cb\u01c7\3\2\2\2\u01cb\u01c8\3\2\2\2\u01cb\u01c9\3")
        buf.write("\2\2\2\u01cb\u01ca\3\2\2\2\u01cc]\3\2\2\2\u01cd\u01ce")
        buf.write("\7\65\2\2\u01ce_\3\2\2\2\u01cf\u01d0\7\63\2\2\u01d0\u01d1")
        buf.write("\5b\62\2\u01d1a\3\2\2\2\u01d2\u01d3\7=\2\2\u01d3\u01d4")
        buf.write("\5\30\r\2\u01d4\u01d5\7>\2\2\u01d5\u01dc\3\2\2\2\u01d6")
        buf.write("\u01d7\7=\2\2\u01d7\u01d8\5\30\r\2\u01d8\u01d9\7>\2\2")
        buf.write("\u01d9\u01da\5b\62\2\u01da\u01dc\3\2\2\2\u01db\u01d2\3")
        buf.write("\2\2\2\u01db\u01d6\3\2\2\2\u01dcc\3\2\2\2\u01dd\u01de")
        buf.write("\7\63\2\2\u01de\u01df\7#\2\2\u01df\u01e0\7\63\2\2\u01e0")
        buf.write("e\3\2\2\2\u01e1\u01e2\7\63\2\2\u01e2\u01e3\7$\2\2\u01e3")
        buf.write("\u01e4\7\62\2\2\u01e4g\3\2\2\2\u01e5\u01e6\7\63\2\2\u01e6")
        buf.write("\u01e7\7#\2\2\u01e7\u01e8\7\63\2\2\u01e8\u01eb\7?\2\2")
        buf.write("\u01e9\u01ec\5\26\f\2\u01ea\u01ec\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01ee\7@\2\2\u01eei\3\2\2\2\u01ef\u01f0\7\63\2\2\u01f0")
        buf.write("\u01f1\7$\2\2\u01f1\u01f2\7\62\2\2\u01f2\u01f5\7?\2\2")
        buf.write("\u01f3\u01f6\5\26\f\2\u01f4\u01f6\3\2\2\2\u01f5\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f8\7@\2\2\u01f8k\3\2\2\2\u01f9\u01fa\7\31\2\2\u01fa")
        buf.write("\u01fb\7\63\2\2\u01fb\u01fe\7?\2\2\u01fc\u01ff\5\26\f")
        buf.write("\2\u01fd\u01ff\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201\7@\2\2\u0201")
        buf.write("m\3\2\2\2,u{\u0080\u008b\u008f\u0098\u00a2\u00aa\u00b1")
        buf.write("\u00b8\u00bf\u00c9\u00d4\u00df\u00e5\u00ea\u00f3\u00fe")
        buf.write("\u0109\u0110\u0115\u012a\u0130\u0138\u0142\u014b\u0153")
        buf.write("\u015d\u0164\u0171\u0176\u0180\u018c\u019d\u01ab\u01b9")
        buf.write("\u01bd\u01cb\u01db\u01eb\u01f5\u01fe")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'..'", "'Break'", "'Continue'", "'If'", 
                     "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
                     "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'!='", "'<='", "'>='", "'>'", "'<'", 
                     "'==.'", "'+.'", "'.'", "'::'", "'->'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\b'", "'\f'", "'\r'", "'\n'", 
                     "'\t'", "'''", "'\\'", "'['", "']'", "'('", "')'", 
                     "'{'", "'}'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INTTYPE", "FLOATTYPE", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "NOTEQUAL", "NOTLARGER", 
                      "NOTSMALLER", "LARGER", "SMALLER", "COMPARSTR", "CONCAT", 
                      "INSTANT", "STATICATTR", "INDEXOPR", "ADD", "MINUS", 
                      "MULTI", "DIV", "PERCENT", "NOT", "AND", "OR", "COMPAR", 
                      "EQUAL", "STR", "BLOCKCOMMENT", "STATIC", "ID", "FLOAT", 
                      "INT", "BACKSPACE", "FORMFEED", "CARRETURN", "NEWLINE", 
                      "HORTAB", "SINGQ", "BACKSLASH", "LS", "RS", "LB", 
                      "RB", "LP", "RP", "SEMI", "COMMA", "COLON", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecls = 1
    RULE_classdecl = 2
    RULE_superclass = 3
    RULE_memberlist = 4
    RULE_member = 5
    RULE_attr = 6
    RULE_attrtype = 7
    RULE_idlist = 8
    RULE_typ = 9
    RULE_exprlist = 10
    RULE_expr = 11
    RULE_exp1 = 12
    RULE_exp2 = 13
    RULE_exp3 = 14
    RULE_exp4 = 15
    RULE_exp5 = 16
    RULE_exp6 = 17
    RULE_exp7 = 18
    RULE_exp8 = 19
    RULE_exp9 = 20
    RULE_exp10 = 21
    RULE_exp11 = 22
    RULE_call = 23
    RULE_method = 24
    RULE_paramlist = 25
    RULE_param = 26
    RULE_blockstate = 27
    RULE_statements = 28
    RULE_sta = 29
    RULE_lhs = 30
    RULE_ifsta = 31
    RULE_eliflist = 32
    RULE_forsta = 33
    RULE_breaksta = 34
    RULE_continuesta = 35
    RULE_returnsta = 36
    RULE_methodsta = 37
    RULE_indexedarr = 38
    RULE_literals = 39
    RULE_lit = 40
    RULE_multiarr = 41
    RULE_arrlist = 42
    RULE_arr = 43
    RULE_arrdecl = 44
    RULE_element = 45
    RULE_size = 46
    RULE_eleexp = 47
    RULE_indexop = 48
    RULE_instance = 49
    RULE_staatr = 50
    RULE_imethodi = 51
    RULE_smethodi = 52
    RULE_objcreate = 53

    ruleNames =  [ "program", "classdecls", "classdecl", "superclass", "memberlist", 
                   "member", "attr", "attrtype", "idlist", "typ", "exprlist", 
                   "expr", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "call", "method", 
                   "paramlist", "param", "blockstate", "statements", "sta", 
                   "lhs", "ifsta", "eliflist", "forsta", "breaksta", "continuesta", 
                   "returnsta", "methodsta", "indexedarr", "literals", "lit", 
                   "multiarr", "arrlist", "arr", "arrdecl", "element", "size", 
                   "eleexp", "indexop", "instance", "staatr", "imethodi", 
                   "smethodi", "objcreate" ]

    EOF = Token.EOF
    T__0=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    TRUE=8
    FALSE=9
    ARRAY=10
    IN=11
    INTTYPE=12
    FLOATTYPE=13
    BOOLEAN=14
    STRING=15
    RETURN=16
    NULL=17
    CLASS=18
    VAL=19
    VAR=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    NEW=23
    BY=24
    SELF=25
    NOTEQUAL=26
    NOTLARGER=27
    NOTSMALLER=28
    LARGER=29
    SMALLER=30
    COMPARSTR=31
    CONCAT=32
    INSTANT=33
    STATICATTR=34
    INDEXOPR=35
    ADD=36
    MINUS=37
    MULTI=38
    DIV=39
    PERCENT=40
    NOT=41
    AND=42
    OR=43
    COMPAR=44
    EQUAL=45
    STR=46
    BLOCKCOMMENT=47
    STATIC=48
    ID=49
    FLOAT=50
    INT=51
    BACKSPACE=52
    FORMFEED=53
    CARRETURN=54
    NEWLINE=55
    HORTAB=56
    SINGQ=57
    BACKSLASH=58
    LS=59
    RS=60
    LB=61
    RB=62
    LP=63
    RP=64
    SEMI=65
    COMMA=66
    COLON=67
    WS=68
    ERROR_CHAR=69
    UNCLOSE_STRING=70
    ILLEGAL_ESCAPE=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.classdecls()
            self.state = 109
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclContext,0)


        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecls" ):
                return visitor.visitClassdecls(self)
            else:
                return visitor.visitChildren(self)




    def classdecls(self):

        localctx = D96Parser.ClassdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecls)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.classdecl()
                self.state = 112
                self.classdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.classdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def superclass(self):
            return self.getTypedRuleContext(D96Parser.SuperclassContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(D96Parser.MemberlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(D96Parser.CLASS)
            self.state = 118
            self.match(D96Parser.ID)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.state = 119
                self.superclass()
                pass
            elif token in [D96Parser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 123
            self.match(D96Parser.LP)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.STATIC, D96Parser.ID]:
                self.state = 124
                self.memberlist()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 128
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_superclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclass" ):
                return visitor.visitSuperclass(self)
            else:
                return visitor.visitChildren(self)




    def superclass(self):

        localctx = D96Parser.SuperclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_superclass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(D96Parser.COLON)
            self.state = 131
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(D96Parser.MemberlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memberlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = D96Parser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memberlist)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.member()
                self.state = 134
                self.memberlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(D96Parser.AttrContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.attr()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.STATIC, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.method()
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


    class AttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrtype(self):
            return self.getTypedRuleContext(D96Parser.AttrtypeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)




    def attr(self):

        localctx = D96Parser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.attrtype()
            self.state = 144
            self.idlist()
            self.state = 145
            self.match(D96Parser.COLON)
            self.state = 146
            self.typ()
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EQUAL]:
                self.state = 147
                self.match(D96Parser.EQUAL)
                self.state = 148
                self.exprlist()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 152
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attrtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrtype" ):
                return visitor.visitAttrtype(self)
            else:
                return visitor.visitChildren(self)




    def attrtype(self):

        localctx = D96Parser.AttrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
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


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 157
                self.match(D96Parser.COMMA)
                self.state = 158
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def arrdecl(self):
            return self.getTypedRuleContext(D96Parser.ArrdeclContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typ)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.arrdecl()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.match(D96Parser.ID)
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


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = D96Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exprlist)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.expr()
                self.state = 171
                self.match(D96Parser.COMMA)
                self.state = 172
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def CONCAT(self):
            return self.getToken(D96Parser.CONCAT, 0)

        def COMPARSTR(self):
            return self.getToken(D96Parser.COMPARSTR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.exp1()
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==D96Parser.COMPARSTR or _la==D96Parser.CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp2Context,i)


        def COMPAR(self):
            return self.getToken(D96Parser.COMPAR, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def NOTSMALLER(self):
            return self.getToken(D96Parser.NOTSMALLER, 0)

        def NOTLARGER(self):
            return self.getToken(D96Parser.NOTLARGER, 0)

        def LARGER(self):
            return self.getToken(D96Parser.LARGER, 0)

        def SMALLER(self):
            return self.getToken(D96Parser.SMALLER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = D96Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.exp2(0)
                self.state = 185
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NOTEQUAL) | (1 << D96Parser.NOTLARGER) | (1 << D96Parser.NOTSMALLER) | (1 << D96Parser.LARGER) | (1 << D96Parser.SMALLER) | (1 << D96Parser.COMPAR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 194
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 195
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 196
                    self.exp3(0) 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 205
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 206
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 207
                    self.exp4(0) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def MULTI(self):
            return self.getToken(D96Parser.MULTI, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def PERCENT(self):
            return self.getToken(D96Parser.PERCENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTI) | (1 << D96Parser.DIV) | (1 << D96Parser.PERCENT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.exp5() 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp5)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(D96Parser.NOT)
                self.state = 225
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.exp6()
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


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp6)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(D96Parser.MINUS)
                self.state = 230
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.exp7(0)
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


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_exp7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 238
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.LS or _la==D96Parser.RS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def INSTANT(self):
            return self.getToken(D96Parser.INSTANT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    self.match(D96Parser.INSTANT)
                    self.state = 249
                    self.exp9(0) 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def exp9(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp9Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp9Context,i)


        def STATICATTR(self):
            return self.getToken(D96Parser.STATICATTR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    self.match(D96Parser.STATICATTR)
                    self.state = 260
                    self.exp9(3) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def exp11(self):
            return self.getTypedRuleContext(D96Parser.Exp11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp10)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.NEW)
                self.state = 267
                self.match(D96Parser.ID)
                self.state = 268
                self.exp10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.exp11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def STR(self):
            return self.getToken(D96Parser.STR, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def multiarr(self):
            return self.getTypedRuleContext(D96Parser.MultiarrContext,0)


        def indexedarr(self):
            return self.getTypedRuleContext(D96Parser.IndexedarrContext,0)


        def call(self):
            return self.getTypedRuleContext(D96Parser.CallContext,0)


        def objcreate(self):
            return self.getTypedRuleContext(D96Parser.ObjcreateContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def imethodi(self):
            return self.getTypedRuleContext(D96Parser.ImethodiContext,0)


        def smethodi(self):
            return self.getTypedRuleContext(D96Parser.SmethodiContext,0)


        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def staatr(self):
            return self.getTypedRuleContext(D96Parser.StaatrContext,0)


        def eleexp(self):
            return self.getTypedRuleContext(D96Parser.EleexpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp11)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(D96Parser.LB)
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                    self.state = 273
                    self.expr()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 277
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(D96Parser.NULL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.match(D96Parser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.match(D96Parser.FLOAT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.match(D96Parser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.match(D96Parser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 283
                self.match(D96Parser.STR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 284
                self.match(D96Parser.ID)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 285
                self.match(D96Parser.STATIC)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 286
                self.multiarr()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 287
                self.indexedarr()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 288
                self.call()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 289
                self.objcreate()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 290
                self.match(D96Parser.SELF)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 291
                self.imethodi()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 292
                self.smethodi()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 293
                self.instance()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 294
                self.staatr()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 295
                self.eleexp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = D96Parser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(D96Parser.ID)
            self.state = 299
            self.match(D96Parser.LB)
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.state = 300
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 304
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.STATIC) | (1 << D96Parser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 307
            self.match(D96Parser.LB)
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.STATIC, D96Parser.ID]:
                self.state = 308
                self.paramlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 312
            self.match(D96Parser.RB)
            self.state = 313
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = D96Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_paramlist)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.param()
                self.state = 316
                self.match(D96Parser.SEMI)
                self.state = 317
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.idlist()
            self.state = 323
            self.match(D96Parser.COLON)
            self.state = 324
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_blockstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstate" ):
                return visitor.visitBlockstate(self)
            else:
                return visitor.visitChildren(self)




    def blockstate(self):

        localctx = D96Parser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(D96Parser.LP)
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.STATIC, D96Parser.ID]:
                self.state = 327
                self.statements()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 331
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sta(self):
            return self.getTypedRuleContext(D96Parser.StaContext,0)


        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statements)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.sta()
                self.state = 334
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.sta()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(D96Parser.AttrContext,0)


        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ifsta(self):
            return self.getTypedRuleContext(D96Parser.IfstaContext,0)


        def forsta(self):
            return self.getTypedRuleContext(D96Parser.ForstaContext,0)


        def breaksta(self):
            return self.getTypedRuleContext(D96Parser.BreakstaContext,0)


        def continuesta(self):
            return self.getTypedRuleContext(D96Parser.ContinuestaContext,0)


        def returnsta(self):
            return self.getTypedRuleContext(D96Parser.ReturnstaContext,0)


        def methodsta(self):
            return self.getTypedRuleContext(D96Parser.MethodstaContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSta" ):
                return visitor.visitSta(self)
            else:
                return visitor.visitChildren(self)




    def sta(self):

        localctx = D96Parser.StaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_sta)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.lhs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self.ifsta()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self.forsta()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 343
                self.breaksta()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 344
                self.continuesta()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 345
                self.returnsta()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 346
                self.methodsta()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def eleexp(self):
            return self.getTypedRuleContext(D96Parser.EleexpContext,0)


        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def staatr(self):
            return self.getTypedRuleContext(D96Parser.StaatrContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 349
                self.eleexp()
                pass

            elif la_ == 2:
                self.state = 350
                self.instance()
                pass

            elif la_ == 3:
                self.state = 351
                self.staatr()
                pass

            elif la_ == 4:
                self.state = 352
                self.match(D96Parser.ID)
                pass

            elif la_ == 5:
                self.state = 353
                self.match(D96Parser.STATIC)
                pass


            self.state = 356
            self.match(D96Parser.EQUAL)
            self.state = 357
            self.expr()
            self.state = 358
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.BlockstateContext)
            else:
                return self.getTypedRuleContext(D96Parser.BlockstateContext,i)


        def eliflist(self):
            return self.getTypedRuleContext(D96Parser.EliflistContext,0)


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ifsta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfsta" ):
                return visitor.visitIfsta(self)
            else:
                return visitor.visitChildren(self)




    def ifsta(self):

        localctx = D96Parser.IfstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ifsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(D96Parser.IF)
            self.state = 361
            self.match(D96Parser.LB)
            self.state = 362
            self.expr()
            self.state = 363
            self.match(D96Parser.RB)
            self.state = 364
            self.blockstate()
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 365
                self.eliflist()
                pass

            elif la_ == 2:
                pass


            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.state = 369
                self.match(D96Parser.ELSE)
                self.state = 370
                self.blockstate()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.STATIC, D96Parser.ID, D96Parser.RP]:
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


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(D96Parser.EliflistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = D96Parser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_eliflist)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(D96Parser.ELSEIF)
                self.state = 375
                self.match(D96Parser.LB)
                self.state = 376
                self.expr()
                self.state = 377
                self.match(D96Parser.RB)
                self.state = 378
                self.blockstate()
                self.state = 379
                self.eliflist()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.STATIC, D96Parser.ID, D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class ForstaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INT)
            else:
                return self.getToken(D96Parser.INT, i)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forsta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForsta" ):
                return visitor.visitForsta(self)
            else:
                return visitor.visitChildren(self)




    def forsta(self):

        localctx = D96Parser.ForstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forsta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(D96Parser.FOREACH)
            self.state = 385
            self.match(D96Parser.LB)
            self.state = 386
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 387
            self.match(D96Parser.IN)
            self.state = 388
            self.match(D96Parser.INT)
            self.state = 389
            self.match(D96Parser.T__0)
            self.state = 390
            self.match(D96Parser.INT)
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.state = 391
                self.match(D96Parser.BY)
                self.state = 392
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 396
            self.match(D96Parser.RB)
            self.state = 397
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breaksta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreaksta" ):
                return visitor.visitBreaksta(self)
            else:
                return visitor.visitChildren(self)




    def breaksta(self):

        localctx = D96Parser.BreakstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_breaksta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(D96Parser.BREAK)
            self.state = 400
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continuesta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuesta" ):
                return visitor.visitContinuesta(self)
            else:
                return visitor.visitChildren(self)




    def continuesta(self):

        localctx = D96Parser.ContinuestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continuesta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(D96Parser.CONTINUE)
            self.state = 403
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_returnsta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnsta" ):
                return visitor.visitReturnsta(self)
            else:
                return visitor.visitChildren(self)




    def returnsta(self):

        localctx = D96Parser.ReturnstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_returnsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(D96Parser.RETURN)
            self.state = 406
            self.expr()
            self.state = 407
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodstaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def smethodi(self):
            return self.getTypedRuleContext(D96Parser.SmethodiContext,0)


        def imethodi(self):
            return self.getTypedRuleContext(D96Parser.ImethodiContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodsta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodsta" ):
                return visitor.visitMethodsta(self)
            else:
                return visitor.visitChildren(self)




    def methodsta(self):

        localctx = D96Parser.MethodstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_methodsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 409
                self.smethodi()
                pass

            elif la_ == 2:
                self.state = 410
                self.imethodi()
                pass


            self.state = 413
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexedarrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexedarr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexedarr" ):
                return visitor.visitIndexedarr(self)
            else:
                return visitor.visitChildren(self)




    def indexedarr(self):

        localctx = D96Parser.IndexedarrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_indexedarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(D96Parser.ARRAY)
            self.state = 416
            self.match(D96Parser.LB)
            self.state = 417
            self.literals()
            self.state = 418
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(D96Parser.LitContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literals)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.lit()
                self.state = 421
                self.match(D96Parser.COMMA)
                self.state = 422
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def STR(self):
            return self.getToken(D96Parser.STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = D96Parser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.STR) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT))) != 0)):
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


    class MultiarrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def arrlist(self):
            return self.getTypedRuleContext(D96Parser.ArrlistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multiarr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiarr" ):
                return visitor.visitMultiarr(self)
            else:
                return visitor.visitChildren(self)




    def multiarr(self):

        localctx = D96Parser.MultiarrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_multiarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(D96Parser.ARRAY)
            self.state = 430
            self.match(D96Parser.LB)
            self.state = 431
            self.arrlist()
            self.state = 432
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr(self):
            return self.getTypedRuleContext(D96Parser.ArrContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def arrlist(self):
            return self.getTypedRuleContext(D96Parser.ArrlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlist" ):
                return visitor.visitArrlist(self)
            else:
                return visitor.visitChildren(self)




    def arrlist(self):

        localctx = D96Parser.ArrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arrlist)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.arr()
                self.state = 435
                self.match(D96Parser.COMMA)
                self.state = 436
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiarr(self):
            return self.getTypedRuleContext(D96Parser.MultiarrContext,0)


        def indexedarr(self):
            return self.getTypedRuleContext(D96Parser.IndexedarrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr" ):
                return visitor.visitArr(self)
            else:
                return visitor.visitChildren(self)




    def arr(self):

        localctx = D96Parser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arr)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.multiarr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.indexedarr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def element(self):
            return self.getTypedRuleContext(D96Parser.ElementContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def size(self):
            return self.getTypedRuleContext(D96Parser.SizeContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrdecl" ):
                return visitor.visitArrdecl(self)
            else:
                return visitor.visitChildren(self)




    def arrdecl(self):

        localctx = D96Parser.ArrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arrdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(D96Parser.ARRAY)
            self.state = 446
            self.match(D96Parser.LS)
            self.state = 447
            self.element()
            self.state = 448
            self.match(D96Parser.COMMA)
            self.state = 449
            self.size()
            self.state = 450
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def arrdecl(self):
            return self.getTypedRuleContext(D96Parser.ArrdeclContext,0)


        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = D96Parser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_element)
        try:
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 455
                self.arrdecl()
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 456
                self.match(D96Parser.STRING)
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


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(D96Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EleexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def indexop(self):
            return self.getTypedRuleContext(D96Parser.IndexopContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_eleexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEleexp" ):
                return visitor.visitEleexp(self)
            else:
                return visitor.visitChildren(self)




    def eleexp(self):

        localctx = D96Parser.EleexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_eleexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(D96Parser.ID)
            self.state = 462
            self.indexop()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def indexop(self):
            return self.getTypedRuleContext(D96Parser.IndexopContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)




    def indexop(self):

        localctx = D96Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_indexop)
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(D96Parser.LS)
                self.state = 465
                self.expr()
                self.state = 466
                self.match(D96Parser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(D96Parser.LS)
                self.state = 469
                self.expr()
                self.state = 470
                self.match(D96Parser.RS)
                self.state = 471
                self.indexop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def INSTANT(self):
            return self.getToken(D96Parser.INSTANT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance" ):
                return visitor.visitInstance(self)
            else:
                return visitor.visitChildren(self)




    def instance(self):

        localctx = D96Parser.InstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(D96Parser.ID)
            self.state = 476
            self.match(D96Parser.INSTANT)
            self.state = 477
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaatrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATICATTR(self):
            return self.getToken(D96Parser.STATICATTR, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_staatr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaatr" ):
                return visitor.visitStaatr(self)
            else:
                return visitor.visitChildren(self)




    def staatr(self):

        localctx = D96Parser.StaatrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_staatr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(D96Parser.ID)
            self.state = 480
            self.match(D96Parser.STATICATTR)
            self.state = 481
            self.match(D96Parser.STATIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImethodiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def INSTANT(self):
            return self.getToken(D96Parser.INSTANT, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_imethodi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImethodi" ):
                return visitor.visitImethodi(self)
            else:
                return visitor.visitChildren(self)




    def imethodi(self):

        localctx = D96Parser.ImethodiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_imethodi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(D96Parser.ID)
            self.state = 484
            self.match(D96Parser.INSTANT)
            self.state = 485
            self.match(D96Parser.ID)
            self.state = 486
            self.match(D96Parser.LB)
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.state = 487
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 491
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SmethodiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATICATTR(self):
            return self.getToken(D96Parser.STATICATTR, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_smethodi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmethodi" ):
                return visitor.visitSmethodi(self)
            else:
                return visitor.visitChildren(self)




    def smethodi(self):

        localctx = D96Parser.SmethodiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_smethodi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(D96Parser.ID)
            self.state = 494
            self.match(D96Parser.STATICATTR)
            self.state = 495
            self.match(D96Parser.STATIC)
            self.state = 496
            self.match(D96Parser.LB)
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.state = 497
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 501
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjcreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_objcreate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjcreate" ):
                return visitor.visitObjcreate(self)
            else:
                return visitor.visitChildren(self)




    def objcreate(self):

        localctx = D96Parser.ObjcreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_objcreate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(D96Parser.NEW)
            self.state = 504
            self.match(D96Parser.ID)
            self.state = 505
            self.match(D96Parser.LB)
            self.state = 508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.state = 506
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 510
            self.match(D96Parser.RB)
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
        self._predicates[13] = self.exp2_sempred
        self._predicates[14] = self.exp3_sempred
        self._predicates[15] = self.exp4_sempred
        self._predicates[18] = self.exp7_sempred
        self._predicates[19] = self.exp8_sempred
        self._predicates[20] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




