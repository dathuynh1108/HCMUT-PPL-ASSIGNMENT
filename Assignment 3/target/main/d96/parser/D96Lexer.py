# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u0252\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#")
        buf.write("\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3/\3/\3/\7/\u0172")
        buf.write("\n/\f/\16/\u0175\13/\3/\3/\7/\u0179\n/\f/\16/\u017c\13")
        buf.write("/\3/\3/\3/\3\60\3\60\7\60\u0183\n\60\f\60\16\60\u0186")
        buf.write("\13\60\3\60\3\60\7\60\u018a\n\60\f\60\16\60\u018d\13\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\7\63\u019a\n\63\f\63\16\63\u019d\13\63\3\64\3\64\5\64")
        buf.write("\u01a1\n\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u01ab\n\64\3\64\3\64\3\65\3\65\7\65\u01b1\n\65\f\65")
        buf.write("\16\65\u01b4\13\65\3\66\3\66\5\66\u01b8\n\66\3\66\6\66")
        buf.write("\u01bb\n\66\r\66\16\66\u01bc\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\5\67\u01c5\n\67\38\38\38\68\u01ca\n8\r8\168\u01cb")
        buf.write("\38\58\u01cf\n8\39\39\39\39\69\u01d5\n9\r9\169\u01d6\3")
        buf.write("9\59\u01da\n9\3:\3:\3:\3:\6:\u01e0\n:\r:\16:\u01e1\3:")
        buf.write("\5:\u01e5\n:\3;\3;\7;\u01e9\n;\f;\16;\u01ec\13;\3;\3;")
        buf.write("\6;\u01f0\n;\r;\16;\u01f1\7;\u01f4\n;\f;\16;\u01f7\13")
        buf.write(";\3;\5;\u01fa\n;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3C\3D\3D\3D\5D\u0210\nD\3E\3E\3F\3F\3G\3G\3")
        buf.write("H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3N\3O\6O\u0228")
        buf.write("\nO\rO\16O\u0229\3O\3O\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\7Q\u0237")
        buf.write("\nQ\fQ\16Q\u023a\13Q\3Q\3Q\7Q\u023e\nQ\fQ\16Q\u0241\13")
        buf.write("Q\3Q\3Q\3R\3R\7R\u0247\nR\fR\16R\u024a\13R\3R\3R\3R\5")
        buf.write("R\u024f\nR\3R\3R\3\u018b\2S\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\2g\64i\2k\2m\65o\2q\2s\2u\2w\66y\67{8}9\177:\u0081;")
        buf.write("\u0083<\u0085\2\u0087\2\u0089=\u008b>\u008d?\u008f@\u0091")
        buf.write("A\u0093B\u0095C\u0097D\u0099E\u009b\2\u009dF\u009fG\u00a1")
        buf.write("H\u00a3I\3\2\24\3\2%%\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\3\2\639\3\2\629\4\2ZZzz\5\2\63;CHch")
        buf.write("\5\2\62;CHch\4\2DDdd\3\2\62\63\3\2\63;\t\2))^^ddhhppt")
        buf.write("tvv\6\2\n\f\16\17$$^^\5\2\13\f\17\17\"\"\b\2^^ddhhppt")
        buf.write("tvv\2\u0269\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2g")
        buf.write("\3\2\2\2\2m\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\3\u00a5\3\2\2")
        buf.write("\2\5\u00a8\3\2\2\2\7\u00ae\3\2\2\2\t\u00b7\3\2\2\2\13")
        buf.write("\u00ba\3\2\2\2\r\u00c1\3\2\2\2\17\u00c6\3\2\2\2\21\u00ce")
        buf.write("\3\2\2\2\23\u00d3\3\2\2\2\25\u00d9\3\2\2\2\27\u00df\3")
        buf.write("\2\2\2\31\u00e2\3\2\2\2\33\u00e6\3\2\2\2\35\u00ec\3\2")
        buf.write("\2\2\37\u00f4\3\2\2\2!\u00fb\3\2\2\2#\u0102\3\2\2\2%\u0107")
        buf.write("\3\2\2\2\'\u010d\3\2\2\2)\u0111\3\2\2\2+\u0115\3\2\2\2")
        buf.write("-\u0121\3\2\2\2/\u012c\3\2\2\2\61\u0130\3\2\2\2\63\u0133")
        buf.write("\3\2\2\2\65\u0138\3\2\2\2\67\u013b\3\2\2\29\u013e\3\2")
        buf.write("\2\2;\u0141\3\2\2\2=\u0143\3\2\2\2?\u0145\3\2\2\2A\u0149")
        buf.write("\3\2\2\2C\u014c\3\2\2\2E\u014e\3\2\2\2G\u0151\3\2\2\2")
        buf.write("I\u0154\3\2\2\2K\u0156\3\2\2\2M\u0158\3\2\2\2O\u015a\3")
        buf.write("\2\2\2Q\u015c\3\2\2\2S\u015e\3\2\2\2U\u0160\3\2\2\2W\u0163")
        buf.write("\3\2\2\2Y\u0166\3\2\2\2[\u0169\3\2\2\2]\u016b\3\2\2\2")
        buf.write("_\u0180\3\2\2\2a\u0192\3\2\2\2c\u0195\3\2\2\2e\u0197\3")
        buf.write("\2\2\2g\u01aa\3\2\2\2i\u01ae\3\2\2\2k\u01b5\3\2\2\2m\u01c4")
        buf.write("\3\2\2\2o\u01c6\3\2\2\2q\u01d0\3\2\2\2s\u01db\3\2\2\2")
        buf.write("u\u01f9\3\2\2\2w\u01fb\3\2\2\2y\u01fd\3\2\2\2{\u01ff\3")
        buf.write("\2\2\2}\u0201\3\2\2\2\177\u0203\3\2\2\2\u0081\u0205\3")
        buf.write("\2\2\2\u0083\u0207\3\2\2\2\u0085\u0209\3\2\2\2\u0087\u020f")
        buf.write("\3\2\2\2\u0089\u0211\3\2\2\2\u008b\u0213\3\2\2\2\u008d")
        buf.write("\u0215\3\2\2\2\u008f\u0217\3\2\2\2\u0091\u0219\3\2\2\2")
        buf.write("\u0093\u021b\3\2\2\2\u0095\u021d\3\2\2\2\u0097\u021f\3")
        buf.write("\2\2\2\u0099\u0221\3\2\2\2\u009b\u0223\3\2\2\2\u009d\u0227")
        buf.write("\3\2\2\2\u009f\u022d\3\2\2\2\u00a1\u0230\3\2\2\2\u00a3")
        buf.write("\u0244\3\2\2\2\u00a5\u00a6\7\60\2\2\u00a6\u00a7\7\60\2")
        buf.write("\2\u00a7\4\3\2\2\2\u00a8\u00a9\7D\2\2\u00a9\u00aa\7t\2")
        buf.write("\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7")
        buf.write("m\2\2\u00ad\6\3\2\2\2\u00ae\u00af\7E\2\2\u00af\u00b0\7")
        buf.write("q\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\b\3\2\2\2\u00b7\u00b8\7K\2\2\u00b8\u00b9")
        buf.write("\7h\2\2\u00b9\n\3\2\2\2\u00ba\u00bb\7G\2\2\u00bb\u00bc")
        buf.write("\7n\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7h\2\2\u00c0\f\3\2\2\2\u00c1\u00c2")
        buf.write("\7G\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\16\3\2\2\2\u00c6\u00c7\7H\2\2\u00c7\u00c8")
        buf.write("\7q\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb")
        buf.write("\7c\2\2\u00cb\u00cc\7e\2\2\u00cc\u00cd\7j\2\2\u00cd\20")
        buf.write("\3\2\2\2\u00ce\u00cf\7V\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7w\2\2\u00d1\u00d2\7g\2\2\u00d2\22\3\2\2\2\u00d3\u00d4")
        buf.write("\7H\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7u\2\2\u00d7\u00d8\7g\2\2\u00d8\24\3\2\2\2\u00d9\u00da")
        buf.write("\7C\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd")
        buf.write("\7c\2\2\u00dd\u00de\7{\2\2\u00de\26\3\2\2\2\u00df\u00e0")
        buf.write("\7K\2\2\u00e0\u00e1\7p\2\2\u00e1\30\3\2\2\2\u00e2\u00e3")
        buf.write("\7K\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7v\2\2\u00e5\32")
        buf.write("\3\2\2\2\u00e6\u00e7\7H\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7v\2\2\u00eb\34")
        buf.write("\3\2\2\2\u00ec\u00ed\7D\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7p\2\2\u00f3\36\3\2\2\2\u00f4\u00f5")
        buf.write("\7U\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7i\2\2\u00fa \3")
        buf.write("\2\2\2\u00fb\u00fc\7T\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\"\3\2\2\2\u0102\u0103\7P\2\2\u0103\u0104")
        buf.write("\7w\2\2\u0104\u0105\7n\2\2\u0105\u0106\7n\2\2\u0106$\3")
        buf.write("\2\2\2\u0107\u0108\7E\2\2\u0108\u0109\7n\2\2\u0109\u010a")
        buf.write("\7c\2\2\u010a\u010b\7u\2\2\u010b\u010c\7u\2\2\u010c&\3")
        buf.write("\2\2\2\u010d\u010e\7X\2\2\u010e\u010f\7c\2\2\u010f\u0110")
        buf.write("\7n\2\2\u0110(\3\2\2\2\u0111\u0112\7X\2\2\u0112\u0113")
        buf.write("\7c\2\2\u0113\u0114\7t\2\2\u0114*\3\2\2\2\u0115\u0116")
        buf.write("\7E\2\2\u0116\u0117\7q\2\2\u0117\u0118\7p\2\2\u0118\u0119")
        buf.write("\7u\2\2\u0119\u011a\7v\2\2\u011a\u011b\7t\2\2\u011b\u011c")
        buf.write("\7w\2\2\u011c\u011d\7e\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7t\2\2\u0120,\3\2\2\2\u0121\u0122")
        buf.write("\7F\2\2\u0122\u0123\7g\2\2\u0123\u0124\7u\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7t\2\2\u0126\u0127\7w\2\2\u0127\u0128")
        buf.write("\7e\2\2\u0128\u0129\7v\2\2\u0129\u012a\7q\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b.\3\2\2\2\u012c\u012d\7P\2\2\u012d\u012e")
        buf.write("\7g\2\2\u012e\u012f\7y\2\2\u012f\60\3\2\2\2\u0130\u0131")
        buf.write("\7D\2\2\u0131\u0132\7{\2\2\u0132\62\3\2\2\2\u0133\u0134")
        buf.write("\7U\2\2\u0134\u0135\7g\2\2\u0135\u0136\7n\2\2\u0136\u0137")
        buf.write("\7h\2\2\u0137\64\3\2\2\2\u0138\u0139\7#\2\2\u0139\u013a")
        buf.write("\7?\2\2\u013a\66\3\2\2\2\u013b\u013c\7>\2\2\u013c\u013d")
        buf.write("\7?\2\2\u013d8\3\2\2\2\u013e\u013f\7@\2\2\u013f\u0140")
        buf.write("\7?\2\2\u0140:\3\2\2\2\u0141\u0142\7@\2\2\u0142<\3\2\2")
        buf.write("\2\u0143\u0144\7>\2\2\u0144>\3\2\2\2\u0145\u0146\7?\2")
        buf.write("\2\u0146\u0147\7?\2\2\u0147\u0148\7\60\2\2\u0148@\3\2")
        buf.write("\2\2\u0149\u014a\7-\2\2\u014a\u014b\7\60\2\2\u014bB\3")
        buf.write("\2\2\2\u014c\u014d\7\60\2\2\u014dD\3\2\2\2\u014e\u014f")
        buf.write("\7<\2\2\u014f\u0150\7<\2\2\u0150F\3\2\2\2\u0151\u0152")
        buf.write("\7/\2\2\u0152\u0153\7@\2\2\u0153H\3\2\2\2\u0154\u0155")
        buf.write("\7-\2\2\u0155J\3\2\2\2\u0156\u0157\7/\2\2\u0157L\3\2\2")
        buf.write("\2\u0158\u0159\7,\2\2\u0159N\3\2\2\2\u015a\u015b\7\61")
        buf.write("\2\2\u015bP\3\2\2\2\u015c\u015d\7\'\2\2\u015dR\3\2\2\2")
        buf.write("\u015e\u015f\7#\2\2\u015fT\3\2\2\2\u0160\u0161\7(\2\2")
        buf.write("\u0161\u0162\7(\2\2\u0162V\3\2\2\2\u0163\u0164\7~\2\2")
        buf.write("\u0164\u0165\7~\2\2\u0165X\3\2\2\2\u0166\u0167\7?\2\2")
        buf.write("\u0167\u0168\7?\2\2\u0168Z\3\2\2\2\u0169\u016a\7?\2\2")
        buf.write("\u016a\\\3\2\2\2\u016b\u017a\7$\2\2\u016c\u0179\5\u0087")
        buf.write("D\2\u016d\u016e\7)\2\2\u016e\u016f\7$\2\2\u016f\u0173")
        buf.write("\3\2\2\2\u0170\u0172\5\u0087D\2\u0171\u0170\3\2\2\2\u0172")
        buf.write("\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0176\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\7")
        buf.write(")\2\2\u0177\u0179\7$\2\2\u0178\u016c\3\2\2\2\u0178\u016d")
        buf.write("\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017d\u017e\7$\2\2\u017e\u017f\b/\2\2\u017f^\3\2\2\2")
        buf.write("\u0180\u0184\5\u009bN\2\u0181\u0183\n\2\2\2\u0182\u0181")
        buf.write("\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u018b\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0187\u018a\7%\2\2\u0188\u018a\n\2\2\2\u0189\u0187\3")
        buf.write("\2\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018e\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u018f\5\u009bN\2\u018f\u0190\3\2")
        buf.write("\2\2\u0190\u0191\b\60\3\2\u0191`\3\2\2\2\u0192\u0193\7")
        buf.write("&\2\2\u0193\u0194\5e\63\2\u0194b\3\2\2\2\u0195\u0196\5")
        buf.write("e\63\2\u0196d\3\2\2\2\u0197\u019b\t\3\2\2\u0198\u019a")
        buf.write("\t\4\2\2\u0199\u0198\3\2\2\2\u019a\u019d\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019cf\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019e\u01a0\5u;\2\u019f\u01a1\5i\65\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a3\5k\66\2\u01a3\u01ab\3\2\2\2\u01a4\u01a5\5")
        buf.write("u;\2\u01a5\u01a6\5i\65\2\u01a6\u01ab\3\2\2\2\u01a7\u01a8")
        buf.write("\5i\65\2\u01a8\u01a9\5k\66\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u019e\3\2\2\2\u01aa\u01a4\3\2\2\2\u01aa\u01a7\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01ac\u01ad\b\64\4\2\u01adh\3\2\2")
        buf.write("\2\u01ae\u01b2\7\60\2\2\u01af\u01b1\t\5\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3j\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b7\t\6\2\2\u01b6\u01b8\t\7\2\2\u01b7\u01b6\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01bb\t")
        buf.write("\5\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bdl\3\2\2\2\u01be\u01c5")
        buf.write("\5o8\2\u01bf\u01c5\5q9\2\u01c0\u01c5\5s:\2\u01c1\u01c2")
        buf.write("\5u;\2\u01c2\u01c3\b\67\5\2\u01c3\u01c5\3\2\2\2\u01c4")
        buf.write("\u01be\3\2\2\2\u01c4\u01bf\3\2\2\2\u01c4\u01c0\3\2\2\2")
        buf.write("\u01c4\u01c1\3\2\2\2\u01c5n\3\2\2\2\u01c6\u01ce\7\62\2")
        buf.write("\2\u01c7\u01c9\t\b\2\2\u01c8\u01ca\t\t\2\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cf\7\62\2")
        buf.write("\2\u01ce\u01c7\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cfp\3\2")
        buf.write("\2\2\u01d0\u01d1\7\62\2\2\u01d1\u01d9\t\n\2\2\u01d2\u01d4")
        buf.write("\t\13\2\2\u01d3\u01d5\t\f\2\2\u01d4\u01d3\3\2\2\2\u01d5")
        buf.write("\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7\u01da\3\2\2\2\u01d8\u01da\7\62\2\2\u01d9\u01d2")
        buf.write("\3\2\2\2\u01d9\u01d8\3\2\2\2\u01dar\3\2\2\2\u01db\u01dc")
        buf.write("\7\62\2\2\u01dc\u01e4\t\r\2\2\u01dd\u01df\7\63\2\2\u01de")
        buf.write("\u01e0\t\16\2\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2")
        buf.write("\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e5")
        buf.write("\3\2\2\2\u01e3\u01e5\7\62\2\2\u01e4\u01dd\3\2\2\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e5t\3\2\2\2\u01e6\u01ea\t\17\2\2\u01e7")
        buf.write("\u01e9\t\5\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3\2\2\2")
        buf.write("\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01f5\3")
        buf.write("\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ef\7a\2\2\u01ee\u01f0")
        buf.write("\t\5\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f4\3\2\2\2")
        buf.write("\u01f3\u01ed\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3")
        buf.write("\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01fa\3\2\2\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f8\u01fa\7\62\2\2\u01f9\u01e6\3\2\2\2\u01f9")
        buf.write("\u01f8\3\2\2\2\u01fav\3\2\2\2\u01fb\u01fc\7\n\2\2\u01fc")
        buf.write("x\3\2\2\2\u01fd\u01fe\7\16\2\2\u01fez\3\2\2\2\u01ff\u0200")
        buf.write("\7\17\2\2\u0200|\3\2\2\2\u0201\u0202\7\f\2\2\u0202~\3")
        buf.write("\2\2\2\u0203\u0204\7\13\2\2\u0204\u0080\3\2\2\2\u0205")
        buf.write("\u0206\7)\2\2\u0206\u0082\3\2\2\2\u0207\u0208\7^\2\2\u0208")
        buf.write("\u0084\3\2\2\2\u0209\u020a\7^\2\2\u020a\u020b\t\20\2\2")
        buf.write("\u020b\u0086\3\2\2\2\u020c\u0210\5\u0085C\2\u020d\u0210")
        buf.write("\n\21\2\2\u020e\u0210\7)\2\2\u020f\u020c\3\2\2\2\u020f")
        buf.write("\u020d\3\2\2\2\u020f\u020e\3\2\2\2\u0210\u0088\3\2\2\2")
        buf.write("\u0211\u0212\7]\2\2\u0212\u008a\3\2\2\2\u0213\u0214\7")
        buf.write("_\2\2\u0214\u008c\3\2\2\2\u0215\u0216\7*\2\2\u0216\u008e")
        buf.write("\3\2\2\2\u0217\u0218\7+\2\2\u0218\u0090\3\2\2\2\u0219")
        buf.write("\u021a\7}\2\2\u021a\u0092\3\2\2\2\u021b\u021c\7\177\2")
        buf.write("\2\u021c\u0094\3\2\2\2\u021d\u021e\7=\2\2\u021e\u0096")
        buf.write("\3\2\2\2\u021f\u0220\7.\2\2\u0220\u0098\3\2\2\2\u0221")
        buf.write("\u0222\7<\2\2\u0222\u009a\3\2\2\2\u0223\u0224\7%\2\2\u0224")
        buf.write("\u0225\7%\2\2\u0225\u009c\3\2\2\2\u0226\u0228\t\22\2\2")
        buf.write("\u0227\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u0227\3")
        buf.write("\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c")
        buf.write("\bO\3\2\u022c\u009e\3\2\2\2\u022d\u022e\13\2\2\2\u022e")
        buf.write("\u022f\bP\6\2\u022f\u00a0\3\2\2\2\u0230\u023f\7$\2\2\u0231")
        buf.write("\u023e\5\u0087D\2\u0232\u0233\7)\2\2\u0233\u0234\7$\2")
        buf.write("\2\u0234\u0238\3\2\2\2\u0235\u0237\5\u0087D\2\u0236\u0235")
        buf.write("\3\2\2\2\u0237\u023a\3\2\2\2\u0238\u0236\3\2\2\2\u0238")
        buf.write("\u0239\3\2\2\2\u0239\u023b\3\2\2\2\u023a\u0238\3\2\2\2")
        buf.write("\u023b\u023c\7)\2\2\u023c\u023e\7$\2\2\u023d\u0231\3\2")
        buf.write("\2\2\u023d\u0232\3\2\2\2\u023e\u0241\3\2\2\2\u023f\u023d")
        buf.write("\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0242\3\2\2\2\u0241")
        buf.write("\u023f\3\2\2\2\u0242\u0243\bQ\7\2\u0243\u00a2\3\2\2\2")
        buf.write("\u0244\u0248\7$\2\2\u0245\u0247\5\u0087D\2\u0246\u0245")
        buf.write("\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248")
        buf.write("\u0249\3\2\2\2\u0249\u024e\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024b\u024f\n\21\2\2\u024c\u024d\7^\2\2\u024d\u024f\n")
        buf.write("\23\2\2\u024e\u024b\3\2\2\2\u024e\u024c\3\2\2\2\u024f")
        buf.write("\u0250\3\2\2\2\u0250\u0251\bR\b\2\u0251\u00a4\3\2\2\2")
        buf.write("!\2\u0173\u0178\u017a\u0184\u0189\u018b\u019b\u01a0\u01aa")
        buf.write("\u01b2\u01b7\u01bc\u01c4\u01cb\u01ce\u01d6\u01d9\u01e1")
        buf.write("\u01e4\u01ea\u01f1\u01f5\u01f9\u020f\u0229\u0238\u023d")
        buf.write("\u023f\u0248\u024e\t\3/\2\b\2\2\3\64\3\3\67\4\3P\5\3Q")
        buf.write("\6\3R\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSEIF = 5
    ELSE = 6
    FOREACH = 7
    TRUE = 8
    FALSE = 9
    ARRAY = 10
    IN = 11
    INTTYPE = 12
    FLOATTYPE = 13
    BOOLEAN = 14
    STRING = 15
    RETURN = 16
    NULL = 17
    CLASS = 18
    VAL = 19
    VAR = 20
    CONSTRUCTOR = 21
    DESTRUCTOR = 22
    NEW = 23
    BY = 24
    SELF = 25
    NOTEQUAL = 26
    NOTLARGER = 27
    NOTSMALLER = 28
    LARGER = 29
    SMALLER = 30
    COMPARSTR = 31
    CONCAT = 32
    INSTANT = 33
    STATICATTR = 34
    INDEXOPR = 35
    ADD = 36
    MINUS = 37
    MULTI = 38
    DIV = 39
    PERCENT = 40
    NOT = 41
    AND = 42
    OR = 43
    COMPAR = 44
    EQUAL = 45
    STR = 46
    BLOCKCOMMENT = 47
    STATIC = 48
    ID = 49
    FLOAT = 50
    INT = 51
    BACKSPACE = 52
    FORMFEED = 53
    CARRETURN = 54
    NEWLINE = 55
    HORTAB = 56
    SINGQ = 57
    BACKSLASH = 58
    LS = 59
    RS = 60
    LB = 61
    RB = 62
    LP = 63
    RP = 64
    SEMI = 65
    COMMA = 66
    COLON = 67
    WS = 68
    ERROR_CHAR = 69
    UNCLOSE_STRING = 70
    ILLEGAL_ESCAPE = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'..'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'Self'", "'!='", "'<='", "'>='", "'>'", "'<'", "'==.'", 
            "'+.'", "'.'", "'::'", "'->'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'='", "'\b'", "'\f'", "'\r'", 
            "'\n'", "'\t'", "'''", "'\\'", "'['", "']'", "'('", "')'", "'{'", 
            "'}'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INTTYPE", "FLOATTYPE", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "NOTEQUAL", "NOTLARGER", "NOTSMALLER", 
            "LARGER", "SMALLER", "COMPARSTR", "CONCAT", "INSTANT", "STATICATTR", 
            "INDEXOPR", "ADD", "MINUS", "MULTI", "DIV", "PERCENT", "NOT", 
            "AND", "OR", "COMPAR", "EQUAL", "STR", "BLOCKCOMMENT", "STATIC", 
            "ID", "FLOAT", "INT", "BACKSPACE", "FORMFEED", "CARRETURN", 
            "NEWLINE", "HORTAB", "SINGQ", "BACKSLASH", "LS", "RS", "LB", 
            "RB", "LP", "RP", "SEMI", "COMMA", "COLON", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INTTYPE", "FLOATTYPE", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                  "NOTEQUAL", "NOTLARGER", "NOTSMALLER", "LARGER", "SMALLER", 
                  "COMPARSTR", "CONCAT", "INSTANT", "STATICATTR", "INDEXOPR", 
                  "ADD", "MINUS", "MULTI", "DIV", "PERCENT", "NOT", "AND", 
                  "OR", "COMPAR", "EQUAL", "STR", "BLOCKCOMMENT", "STATIC", 
                  "ID", "IDENTIFY", "FLOAT", "DECIMAL", "EXPONENT", "INT", 
                  "OCT", "HEX", "BIN", "DEC", "BACKSPACE", "FORMFEED", "CARRETURN", 
                  "NEWLINE", "HORTAB", "SINGQ", "BACKSLASH", "ESC", "CHAR", 
                  "LS", "RS", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "COLON", 
                  "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[45] = self.STR_action 
            actions[50] = self.FLOAT_action 
            actions[53] = self.INT_action 
            actions[78] = self.ERROR_CHAR_action 
            actions[79] = self.UNCLOSE_STRING_action 
            actions[80] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('"', "")
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text.replace('"', ""))
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text.replace('"', ""))
     


