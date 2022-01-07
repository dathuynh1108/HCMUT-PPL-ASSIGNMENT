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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u01be\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\7\2\u0087\n\2\f\2\16\2\u008a\13\2\5\2\u008c\n\2\3\3\3")
        buf.write("\3\6\3\u0090\n\3\r\3\16\3\u0091\3\4\3\4\3\4\6\4\u0097")
        buf.write("\n\4\r\4\16\4\u0098\3\5\3\5\3\5\6\5\u009e\n\5\r\5\16\5")
        buf.write("\u009f\3\6\3\6\3\6\5\6\u00a5\n\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\5\t\u00b0\n\t\3\n\3\n\3\13\6\13\u00b5\n")
        buf.write("\13\r\13\16\13\u00b6\3\f\3\f\3\f\3\r\3\r\5\r\u00be\n\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\7\16\u00c6\n\16\f\16\16\16")
        buf.write("\u00c9\13\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\58\u0169\n8\38\38\78\u016d\n8\f8\168\u0170")
        buf.write("\138\39\39\39\39\59\u0176\n9\39\39\3:\3:\7:\u017c\n:\f")
        buf.write(":\16:\u017f\13:\3:\3:\3:\3;\3;\5;\u0186\n;\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3=\6=\u0193\n=\r=\16=\u0194\3=\3=")
        buf.write("\3>\3>\3>\3>\3>\3>\5>\u019f\n>\5>\u01a1\n>\3>\3>\3>\3")
        buf.write("?\3?\7?\u01a8\n?\f?\16?\u01ab\13?\3?\5?\u01ae\n?\3?\3")
        buf.write("?\3@\3@\7@\u01b4\n@\f@\16@\u01b7\13@\3@\3@\3@\3A\3A\3")
        buf.write("A\3\u00c7\2B\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25")
        buf.write("\2\27\2\31\2\33\3\35\4\37\5!\6#\7%\b\'\t)\n+\13-\f/\r")
        buf.write("\61\16\63\17\65\20\67\219\22;\23=\24?\25A\26C\27E\30G")
        buf.write("\31I\32K\33M\34O\35Q\36S\37U W!Y\"[#]$_%a&c\'e(g)i*k+")
        buf.write("m,o-q.s/u\60w\61y\62{\63}\64\177\65\u0081\66\3\2\23\4")
        buf.write("\2\63;aa\4\2\62;aa\4\2\629aa\4\2DDdd\4\2\62\63aa\4\2Z")
        buf.write("Zzz\6\2\62;CHaach\7\2\n\f\16\17$$))^^\t\2))^^ddhhpptt")
        buf.write("vv\3\2^^\4\2--//\4\2GGgg\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\16\17\"\"\3\2%%\7\3\n\f\16\17$$))^^\2\u01c8\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\3\u008b\3\2\2\2\5\u008d\3\2\2\2\7\u0093\3\2\2\2\t\u009a")
        buf.write("\3\2\2\2\13\u00a4\3\2\2\2\r\u00a6\3\2\2\2\17\u00a9\3\2")
        buf.write("\2\2\21\u00af\3\2\2\2\23\u00b1\3\2\2\2\25\u00b4\3\2\2")
        buf.write("\2\27\u00b8\3\2\2\2\31\u00bb\3\2\2\2\33\u00c1\3\2\2\2")
        buf.write("\35\u00cf\3\2\2\2\37\u00d5\3\2\2\2!\u00de\3\2\2\2#\u00e1")
        buf.write("\3\2\2\2%\u00e8\3\2\2\2\'\u00ed\3\2\2\2)\u00f5\3\2\2\2")
        buf.write("+\u00fa\3\2\2\2-\u0100\3\2\2\2/\u0106\3\2\2\2\61\u010c")
        buf.write("\3\2\2\2\63\u0110\3\2\2\2\65\u0116\3\2\2\2\67\u011e\3")
        buf.write("\2\2\29\u0125\3\2\2\2;\u012a\3\2\2\2=\u012c\3\2\2\2?\u012e")
        buf.write("\3\2\2\2A\u0130\3\2\2\2C\u0132\3\2\2\2E\u0134\3\2\2\2")
        buf.write("G\u0136\3\2\2\2I\u0139\3\2\2\2K\u013c\3\2\2\2M\u013f\3")
        buf.write("\2\2\2O\u0141\3\2\2\2Q\u0144\3\2\2\2S\u0146\3\2\2\2U\u0149")
        buf.write("\3\2\2\2W\u014b\3\2\2\2Y\u014e\3\2\2\2[\u0152\3\2\2\2")
        buf.write("]\u0155\3\2\2\2_\u0157\3\2\2\2a\u0159\3\2\2\2c\u015b\3")
        buf.write("\2\2\2e\u015d\3\2\2\2g\u015f\3\2\2\2i\u0161\3\2\2\2k\u0163")
        buf.write("\3\2\2\2m\u0165\3\2\2\2o\u0168\3\2\2\2q\u0175\3\2\2\2")
        buf.write("s\u0179\3\2\2\2u\u0185\3\2\2\2w\u0187\3\2\2\2y\u0192\3")
        buf.write("\2\2\2{\u0198\3\2\2\2}\u01a5\3\2\2\2\177\u01b1\3\2\2\2")
        buf.write("\u0081\u01bb\3\2\2\2\u0083\u008c\7\62\2\2\u0084\u0088")
        buf.write("\t\2\2\2\u0085\u0087\t\3\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u0083\3")
        buf.write("\2\2\2\u008b\u0084\3\2\2\2\u008c\4\3\2\2\2\u008d\u008f")
        buf.write("\7\62\2\2\u008e\u0090\t\4\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\6\3\2\2\2\u0093\u0094\7\62\2\2\u0094\u0096\t\5")
        buf.write("\2\2\u0095\u0097\t\6\2\2\u0096\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\b\3\2\2\2\u009a\u009b\7\62\2\2\u009b\u009d\t\7\2\2\u009c")
        buf.write("\u009e\t\b\2\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\n\3\2\2")
        buf.write("\2\u00a1\u00a5\n\t\2\2\u00a2\u00a5\5\r\7\2\u00a3\u00a5")
        buf.write("\5\17\b\2\u00a4\u00a1\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a3\3\2\2\2\u00a5\f\3\2\2\2\u00a6\u00a7\7^\2\2\u00a7")
        buf.write("\u00a8\t\n\2\2\u00a8\16\3\2\2\2\u00a9\u00aa\7)\2\2\u00aa")
        buf.write("\u00ab\7$\2\2\u00ab\20\3\2\2\2\u00ac\u00ad\7^\2\2\u00ad")
        buf.write("\u00b0\n\n\2\2\u00ae\u00b0\n\13\2\2\u00af\u00ac\3\2\2")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00b0\22\3\2\2\2\u00b1\u00b2\t")
        buf.write("\f\2\2\u00b2\24\3\2\2\2\u00b3\u00b5\t\3\2\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\26\3\2\2\2\u00b8\u00b9\13\2\2\2\u00b9")
        buf.write("\u00ba\5\25\13\2\u00ba\30\3\2\2\2\u00bb\u00bd\t\r\2\2")
        buf.write("\u00bc\u00be\5\23\n\2\u00bd\u00bc\3\2\2\2\u00bd\u00be")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\5\25\13\2\u00c0")
        buf.write("\32\3\2\2\2\u00c1\u00c2\7%\2\2\u00c2\u00c3\7%\2\2\u00c3")
        buf.write("\u00c7\3\2\2\2\u00c4\u00c6\13\2\2\2\u00c5\u00c4\3\2\2")
        buf.write("\2\u00c6\u00c9\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00cb\7%\2\2\u00cb\u00cc\7%\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00ce\b\16\2\2\u00ce\34\3\2\2\2\u00cf\u00d0\7D\2\2\u00d0")
        buf.write("\u00d1\7t\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7c\2\2\u00d3")
        buf.write("\u00d4\7m\2\2\u00d4\36\3\2\2\2\u00d5\u00d6\7E\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7v\2\2\u00d9")
        buf.write("\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7w\2\2\u00dc")
        buf.write("\u00dd\7g\2\2\u00dd \3\2\2\2\u00de\u00df\7K\2\2\u00df")
        buf.write("\u00e0\7h\2\2\u00e0\"\3\2\2\2\u00e1\u00e2\7G\2\2\u00e2")
        buf.write("\u00e3\7n\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5\7g\2\2\u00e5")
        buf.write("\u00e6\7k\2\2\u00e6\u00e7\7h\2\2\u00e7$\3\2\2\2\u00e8")
        buf.write("\u00e9\7G\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7u\2\2\u00eb")
        buf.write("\u00ec\7g\2\2\u00ec&\3\2\2\2\u00ed\u00ee\7H\2\2\u00ee")
        buf.write("\u00ef\7q\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7g\2\2\u00f1")
        buf.write("\u00f2\7c\2\2\u00f2\u00f3\7e\2\2\u00f3\u00f4\7j\2\2\u00f4")
        buf.write("(\3\2\2\2\u00f5\u00f6\7V\2\2\u00f6\u00f7\7t\2\2\u00f7")
        buf.write("\u00f8\7w\2\2\u00f8\u00f9\7g\2\2\u00f9*\3\2\2\2\u00fa")
        buf.write("\u00fb\7H\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7n\2\2\u00fd")
        buf.write("\u00fe\7u\2\2\u00fe\u00ff\7g\2\2\u00ff,\3\2\2\2\u0100")
        buf.write("\u0101\7e\2\2\u0101\u0102\7n\2\2\u0102\u0103\7c\2\2\u0103")
        buf.write("\u0104\7u\2\2\u0104\u0105\7u\2\2\u0105.\3\2\2\2\u0106")
        buf.write("\u0107\7C\2\2\u0107\u0108\7t\2\2\u0108\u0109\7t\2\2\u0109")
        buf.write("\u010a\7c\2\2\u010a\u010b\7{\2\2\u010b\60\3\2\2\2\u010c")
        buf.write("\u010d\7K\2\2\u010d\u010e\7p\2\2\u010e\u010f\7v\2\2\u010f")
        buf.write("\62\3\2\2\2\u0110\u0111\7H\2\2\u0111\u0112\7n\2\2\u0112")
        buf.write("\u0113\7q\2\2\u0113\u0114\7c\2\2\u0114\u0115\7v\2\2\u0115")
        buf.write("\64\3\2\2\2\u0116\u0117\7D\2\2\u0117\u0118\7q\2\2\u0118")
        buf.write("\u0119\7q\2\2\u0119\u011a\7n\2\2\u011a\u011b\7g\2\2\u011b")
        buf.write("\u011c\7c\2\2\u011c\u011d\7p\2\2\u011d\66\3\2\2\2\u011e")
        buf.write("\u011f\7U\2\2\u011f\u0120\7v\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write("\u0122\7k\2\2\u0122\u0123\7p\2\2\u0123\u0124\7i\2\2\u0124")
        buf.write("8\3\2\2\2\u0125\u0126\7P\2\2\u0126\u0127\7w\2\2\u0127")
        buf.write("\u0128\7n\2\2\u0128\u0129\7n\2\2\u0129:\3\2\2\2\u012a")
        buf.write("\u012b\7-\2\2\u012b<\3\2\2\2\u012c\u012d\7/\2\2\u012d")
        buf.write(">\3\2\2\2\u012e\u012f\7,\2\2\u012f@\3\2\2\2\u0130\u0131")
        buf.write("\7\61\2\2\u0131B\3\2\2\2\u0132\u0133\7\'\2\2\u0133D\3")
        buf.write("\2\2\2\u0134\u0135\7#\2\2\u0135F\3\2\2\2\u0136\u0137\7")
        buf.write("(\2\2\u0137\u0138\7(\2\2\u0138H\3\2\2\2\u0139\u013a\7")
        buf.write("~\2\2\u013a\u013b\7~\2\2\u013bJ\3\2\2\2\u013c\u013d\7")
        buf.write("?\2\2\u013d\u013e\7?\2\2\u013eL\3\2\2\2\u013f\u0140\7")
        buf.write("?\2\2\u0140N\3\2\2\2\u0141\u0142\7#\2\2\u0142\u0143\7")
        buf.write("?\2\2\u0143P\3\2\2\2\u0144\u0145\7>\2\2\u0145R\3\2\2\2")
        buf.write("\u0146\u0147\7>\2\2\u0147\u0148\7?\2\2\u0148T\3\2\2\2")
        buf.write("\u0149\u014a\7@\2\2\u014aV\3\2\2\2\u014b\u014c\7@\2\2")
        buf.write("\u014c\u014d\7?\2\2\u014dX\3\2\2\2\u014e\u014f\7?\2\2")
        buf.write("\u014f\u0150\7?\2\2\u0150\u0151\7\60\2\2\u0151Z\3\2\2")
        buf.write("\2\u0152\u0153\7-\2\2\u0153\u0154\7\60\2\2\u0154\\\3\2")
        buf.write("\2\2\u0155\u0156\7*\2\2\u0156^\3\2\2\2\u0157\u0158\7+")
        buf.write("\2\2\u0158`\3\2\2\2\u0159\u015a\7]\2\2\u015ab\3\2\2\2")
        buf.write("\u015b\u015c\7_\2\2\u015cd\3\2\2\2\u015d\u015e\7\60\2")
        buf.write("\2\u015ef\3\2\2\2\u015f\u0160\7.\2\2\u0160h\3\2\2\2\u0161")
        buf.write("\u0162\7=\2\2\u0162j\3\2\2\2\u0163\u0164\7}\2\2\u0164")
        buf.write("l\3\2\2\2\u0165\u0166\7\177\2\2\u0166n\3\2\2\2\u0167\u0169")
        buf.write("\7&\2\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u016a\3\2\2\2\u016a\u016e\t\16\2\2\u016b\u016d\t\17\2")
        buf.write("\2\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016fp\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0171\u0176\5\3\2\2\u0172\u0176\5\5\3\2\u0173")
        buf.write("\u0176\5\t\5\2\u0174\u0176\5\7\4\2\u0175\u0171\3\2\2\2")
        buf.write("\u0175\u0172\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0174\3")
        buf.write("\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\b9\3\2\u0178r\3")
        buf.write("\2\2\2\u0179\u017d\7$\2\2\u017a\u017c\5\13\6\2\u017b\u017a")
        buf.write("\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u0180\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u0180\u0181\7$\2\2\u0181\u0182\b:\4\2\u0182t\3\2\2\2")
        buf.write("\u0183\u0186\5)\25\2\u0184\u0186\5+\26\2\u0185\u0183\3")
        buf.write("\2\2\2\u0185\u0184\3\2\2\2\u0186v\3\2\2\2\u0187\u0188")
        buf.write("\7C\2\2\u0188\u0189\7t\2\2\u0189\u018a\7t\2\2\u018a\u018b")
        buf.write("\7c\2\2\u018b\u018c\7{\2\2\u018c\u018d\3\2\2\2\u018d\u018e")
        buf.write("\7*\2\2\u018e\u018f\3\2\2\2\u018f\u0190\7+\2\2\u0190x")
        buf.write("\3\2\2\2\u0191\u0193\t\20\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\u0197\b=\2\2\u0197z\3\2\2\2")
        buf.write("\u0198\u0199\7%\2\2\u0199\u019a\7%\2\2\u019a\u01a0\3\2")
        buf.write("\2\2\u019b\u019c\n\21\2\2\u019c\u01a1\n\21\2\2\u019d\u019f")
        buf.write("\13\2\2\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("\u01a1\3\2\2\2\u01a0\u019b\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2\u01a3\7\2\2\3\u01a3\u01a4\b")
        buf.write(">\5\2\u01a4|\3\2\2\2\u01a5\u01a9\7$\2\2\u01a6\u01a8\5")
        buf.write("\13\6\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ad\3\2\2\2")
        buf.write("\u01ab\u01a9\3\2\2\2\u01ac\u01ae\t\22\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\b?\6\2\u01b0")
        buf.write("~\3\2\2\2\u01b1\u01b5\7$\2\2\u01b2\u01b4\5\13\6\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b8\u01b9\5\21\t\2\u01b9\u01ba\b@\7\2\u01ba\u0080")
        buf.write("\3\2\2\2\u01bb\u01bc\13\2\2\2\u01bc\u01bd\bA\b\2\u01bd")
        buf.write("\u0082\3\2\2\2\30\2\u0088\u008b\u0091\u0098\u009f\u00a4")
        buf.write("\u00af\u00b6\u00bd\u00c7\u0168\u016e\u0175\u017d\u0185")
        buf.write("\u0194\u019e\u01a0\u01a9\u01ad\u01b5\t\b\2\2\39\2\3:\3")
        buf.write("\3>\4\3?\5\3@\6\3A\7")
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
    TRUE = 8
    FALSE = 9
    CLASS = 10
    ARRAY = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    STRING = 15
    NULL = 16
    ADD = 17
    SUB = 18
    MUL = 19
    DIV = 20
    MOD = 21
    NOT = 22
    AND = 23
    OR = 24
    EQUAL = 25
    ASSIGN = 26
    NOT_EQUAL = 27
    LT = 28
    LTE = 29
    GT = 30
    GTE = 31
    STRING_EQUAL = 32
    STRING_ADD = 33
    LP = 34
    RP = 35
    LSB = 36
    RSB = 37
    DOT = 38
    COMMA = 39
    SEMI = 40
    LCB = 41
    RCB = 42
    ID = 43
    INTEGER_LITERAL = 44
    STRING_LITERAL = 45
    BOOLEAN_LITERAL = 46
    INDEXED_ARRAY = 47
    WS = 48
    UNTERMINATED_COMMENT = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_TOKEN = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'class'", "'Array'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Null'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'==.'", "'+.'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", 
            "STRING", "NULL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", "GT", 
            "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", "LSB", "RSB", 
            "DOT", "COMMA", "SEMI", "LCB", "RCB", "ID", "INTEGER_LITERAL", 
            "STRING_LITERAL", "BOOLEAN_LITERAL", "INDEXED_ARRAY", "WS", 
            "UNTERMINATED_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_TOKEN" ]

    ruleNames = [ "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", 
                  "HEX_INTEGER_LITERAL", "STRING_CHAR", "ESCAPE_SEQUENCE", 
                  "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", "SIGN", "FLOAT_INTEGER_PART", 
                  "FLOAT_DECIMAL_PART", "FLOAT_EXPONENT_PART", "COMMENT", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "NULL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", 
                  "GT", "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "SEMI", "LCB", "RCB", "ID", 
                  "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                  "INDEXED_ARRAY", "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", 
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
            actions[55] = self.INTEGER_LITERAL_action 
            actions[56] = self.STRING_LITERAL_action 
            actions[60] = self.UNTERMINATED_COMMENT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_TOKEN_action 
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

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise UNTERMINATED_COMMENT(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                y = str(self.text)
                possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
                if y[-1] in possible:
                    raise UNCLOSE_STRING(y[1:-1])
                else:
                    raise UNCLOSE_STRING(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise ILLEGAL_ESCAPE(self.text[1:])
                
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    raise ERROR_TOKEN(self.text)
                
     


