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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0198\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\7\2}\n\2\f\2\16\2\u0080\13\2")
        buf.write("\5\2\u0082\n\2\3\3\3\3\6\3\u0086\n\3\r\3\16\3\u0087\3")
        buf.write("\4\3\4\3\4\6\4\u008d\n\4\r\4\16\4\u008e\3\5\3\5\3\5\6")
        buf.write("\5\u0094\n\5\r\5\16\5\u0095\3\6\3\6\3\6\5\6\u009b\n\6")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00a6\n\t\3\n")
        buf.write("\3\n\3\n\3\n\7\n\u00ac\n\n\f\n\16\n\u00af\13\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\5\64\u014f\n\64")
        buf.write("\3\64\3\64\7\64\u0153\n\64\f\64\16\64\u0156\13\64\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u015c\n\65\3\65\3\65\3\66\3\66\7")
        buf.write("\66\u0162\n\66\f\66\16\66\u0165\13\66\3\66\3\66\3\66\3")
        buf.write("\67\3\67\5\67\u016c\n\67\38\38\38\38\38\38\38\38\38\3")
        buf.write("8\39\69\u0179\n9\r9\169\u017a\39\39\3:\3:\3:\3:\3:\3:")
        buf.write("\5:\u0185\n:\5:\u0187\n:\3:\3:\3:\3;\3;\7;\u018e\n;\f")
        buf.write(";\16;\u0191\13;\3;\3;\3;\3<\3<\3<\3\u00ad\2=\3\2\5\2\7")
        buf.write("\2\t\2\13\2\r\2\17\2\21\2\23\3\25\4\27\5\31\6\33\7\35")
        buf.write("\b\37\t!\n#\13%\f\'\r)\16+\17-\20/\21\61\22\63\23\65\24")
        buf.write("\67\259\26;\27=\30?\31A\32C\33E\34G\35I\36K\37M O!Q\"")
        buf.write("S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65\3")
        buf.write("\2\20\4\2\63;aa\4\2\62;aa\4\2\629aa\4\2DDdd\4\2\62\63")
        buf.write("aa\4\2ZZzz\6\2\62;CHaach\7\2\n\f\16\17$$))^^\t\2))^^d")
        buf.write("dhhppttvv\3\2^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16")
        buf.write("\17\"\"\3\2%%\2\u01a3\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\3\u0081\3\2\2\2\5\u0083\3\2\2\2\7\u0089")
        buf.write("\3\2\2\2\t\u0090\3\2\2\2\13\u009a\3\2\2\2\r\u009c\3\2")
        buf.write("\2\2\17\u009f\3\2\2\2\21\u00a5\3\2\2\2\23\u00a7\3\2\2")
        buf.write("\2\25\u00b5\3\2\2\2\27\u00bb\3\2\2\2\31\u00c4\3\2\2\2")
        buf.write("\33\u00c7\3\2\2\2\35\u00ce\3\2\2\2\37\u00d3\3\2\2\2!\u00db")
        buf.write("\3\2\2\2#\u00e0\3\2\2\2%\u00e6\3\2\2\2\'\u00ec\3\2\2\2")
        buf.write(")\u00f2\3\2\2\2+\u00f6\3\2\2\2-\u00fc\3\2\2\2/\u0104\3")
        buf.write("\2\2\2\61\u010b\3\2\2\2\63\u0110\3\2\2\2\65\u0112\3\2")
        buf.write("\2\2\67\u0114\3\2\2\29\u0116\3\2\2\2;\u0118\3\2\2\2=\u011a")
        buf.write("\3\2\2\2?\u011c\3\2\2\2A\u011f\3\2\2\2C\u0122\3\2\2\2")
        buf.write("E\u0125\3\2\2\2G\u0127\3\2\2\2I\u012a\3\2\2\2K\u012c\3")
        buf.write("\2\2\2M\u012f\3\2\2\2O\u0131\3\2\2\2Q\u0134\3\2\2\2S\u0138")
        buf.write("\3\2\2\2U\u013b\3\2\2\2W\u013d\3\2\2\2Y\u013f\3\2\2\2")
        buf.write("[\u0141\3\2\2\2]\u0143\3\2\2\2_\u0145\3\2\2\2a\u0147\3")
        buf.write("\2\2\2c\u0149\3\2\2\2e\u014b\3\2\2\2g\u014e\3\2\2\2i\u015b")
        buf.write("\3\2\2\2k\u015f\3\2\2\2m\u016b\3\2\2\2o\u016d\3\2\2\2")
        buf.write("q\u0178\3\2\2\2s\u017e\3\2\2\2u\u018b\3\2\2\2w\u0195\3")
        buf.write("\2\2\2y\u0082\7\62\2\2z~\t\2\2\2{}\t\3\2\2|{\3\2\2\2}")
        buf.write("\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0082\3\2\2")
        buf.write("\2\u0080~\3\2\2\2\u0081y\3\2\2\2\u0081z\3\2\2\2\u0082")
        buf.write("\4\3\2\2\2\u0083\u0085\7\62\2\2\u0084\u0086\t\4\2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\6\3\2\2\2\u0089\u008a\7\62")
        buf.write("\2\2\u008a\u008c\t\5\2\2\u008b\u008d\t\6\2\2\u008c\u008b")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\b\3\2\2\2\u0090\u0091\7\62\2\2\u0091")
        buf.write("\u0093\t\7\2\2\u0092\u0094\t\b\2\2\u0093\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\n\3\2\2\2\u0097\u009b\n\t\2\2\u0098\u009b")
        buf.write("\5\r\7\2\u0099\u009b\5\17\b\2\u009a\u0097\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\f\3\2\2\2\u009c")
        buf.write("\u009d\7^\2\2\u009d\u009e\t\n\2\2\u009e\16\3\2\2\2\u009f")
        buf.write("\u00a0\7)\2\2\u00a0\u00a1\7$\2\2\u00a1\20\3\2\2\2\u00a2")
        buf.write("\u00a3\7^\2\2\u00a3\u00a6\n\n\2\2\u00a4\u00a6\n\13\2\2")
        buf.write("\u00a5\u00a2\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\22\3\2")
        buf.write("\2\2\u00a7\u00a8\7%\2\2\u00a8\u00a9\7%\2\2\u00a9\u00ad")
        buf.write("\3\2\2\2\u00aa\u00ac\13\2\2\2\u00ab\u00aa\3\2\2\2\u00ac")
        buf.write("\u00af\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\7")
        buf.write("%\2\2\u00b1\u00b2\7%\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4")
        buf.write("\b\n\2\2\u00b4\24\3\2\2\2\u00b5\u00b6\7D\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7m\2\2\u00ba\26\3\2\2\2\u00bb\u00bc\7E\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0")
        buf.write("\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\30\3\2\2\2\u00c4\u00c5\7K\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\32\3\2\2\2\u00c7\u00c8\7G\2\2\u00c8\u00c9")
        buf.write("\7n\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc")
        buf.write("\7k\2\2\u00cc\u00cd\7h\2\2\u00cd\34\3\2\2\2\u00ce\u00cf")
        buf.write("\7G\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2")
        buf.write("\7g\2\2\u00d2\36\3\2\2\2\u00d3\u00d4\7H\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7c\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da\7j\2\2\u00da \3")
        buf.write("\2\2\2\u00db\u00dc\7V\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7w\2\2\u00de\u00df\7g\2\2\u00df\"\3\2\2\2\u00e0\u00e1")
        buf.write("\7H\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7u\2\2\u00e4\u00e5\7g\2\2\u00e5$\3\2\2\2\u00e6\u00e7")
        buf.write("\7e\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea")
        buf.write("\7u\2\2\u00ea\u00eb\7u\2\2\u00eb&\3\2\2\2\u00ec\u00ed")
        buf.write("\7C\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f1\7{\2\2\u00f1(\3\2\2\2\u00f2\u00f3")
        buf.write("\7K\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7v\2\2\u00f5*\3")
        buf.write("\2\2\2\u00f6\u00f7\7H\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9")
        buf.write("\7q\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7v\2\2\u00fb,\3")
        buf.write("\2\2\2\u00fc\u00fd\7D\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7c\2\2\u0102\u0103\7p\2\2\u0103.\3\2\2\2\u0104\u0105")
        buf.write("\7U\2\2\u0105\u0106\7v\2\2\u0106\u0107\7t\2\2\u0107\u0108")
        buf.write("\7k\2\2\u0108\u0109\7p\2\2\u0109\u010a\7i\2\2\u010a\60")
        buf.write("\3\2\2\2\u010b\u010c\7P\2\2\u010c\u010d\7w\2\2\u010d\u010e")
        buf.write("\7n\2\2\u010e\u010f\7n\2\2\u010f\62\3\2\2\2\u0110\u0111")
        buf.write("\7-\2\2\u0111\64\3\2\2\2\u0112\u0113\7/\2\2\u0113\66\3")
        buf.write("\2\2\2\u0114\u0115\7,\2\2\u01158\3\2\2\2\u0116\u0117\7")
        buf.write("\61\2\2\u0117:\3\2\2\2\u0118\u0119\7\'\2\2\u0119<\3\2")
        buf.write("\2\2\u011a\u011b\7#\2\2\u011b>\3\2\2\2\u011c\u011d\7(")
        buf.write("\2\2\u011d\u011e\7(\2\2\u011e@\3\2\2\2\u011f\u0120\7~")
        buf.write("\2\2\u0120\u0121\7~\2\2\u0121B\3\2\2\2\u0122\u0123\7?")
        buf.write("\2\2\u0123\u0124\7?\2\2\u0124D\3\2\2\2\u0125\u0126\7?")
        buf.write("\2\2\u0126F\3\2\2\2\u0127\u0128\7#\2\2\u0128\u0129\7?")
        buf.write("\2\2\u0129H\3\2\2\2\u012a\u012b\7>\2\2\u012bJ\3\2\2\2")
        buf.write("\u012c\u012d\7>\2\2\u012d\u012e\7?\2\2\u012eL\3\2\2\2")
        buf.write("\u012f\u0130\7@\2\2\u0130N\3\2\2\2\u0131\u0132\7@\2\2")
        buf.write("\u0132\u0133\7?\2\2\u0133P\3\2\2\2\u0134\u0135\7?\2\2")
        buf.write("\u0135\u0136\7?\2\2\u0136\u0137\7\60\2\2\u0137R\3\2\2")
        buf.write("\2\u0138\u0139\7-\2\2\u0139\u013a\7\60\2\2\u013aT\3\2")
        buf.write("\2\2\u013b\u013c\7*\2\2\u013cV\3\2\2\2\u013d\u013e\7+")
        buf.write("\2\2\u013eX\3\2\2\2\u013f\u0140\7]\2\2\u0140Z\3\2\2\2")
        buf.write("\u0141\u0142\7_\2\2\u0142\\\3\2\2\2\u0143\u0144\7\60\2")
        buf.write("\2\u0144^\3\2\2\2\u0145\u0146\7.\2\2\u0146`\3\2\2\2\u0147")
        buf.write("\u0148\7=\2\2\u0148b\3\2\2\2\u0149\u014a\7}\2\2\u014a")
        buf.write("d\3\2\2\2\u014b\u014c\7\177\2\2\u014cf\3\2\2\2\u014d\u014f")
        buf.write("\7&\2\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0154\t\f\2\2\u0151\u0153\t\r\2\2")
        buf.write("\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3")
        buf.write("\2\2\2\u0154\u0155\3\2\2\2\u0155h\3\2\2\2\u0156\u0154")
        buf.write("\3\2\2\2\u0157\u015c\5\3\2\2\u0158\u015c\5\5\3\2\u0159")
        buf.write("\u015c\5\t\5\2\u015a\u015c\5\7\4\2\u015b\u0157\3\2\2\2")
        buf.write("\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a\3")
        buf.write("\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\b\65\3\2\u015e")
        buf.write("j\3\2\2\2\u015f\u0163\7$\2\2\u0160\u0162\5\13\6\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0166\u0167\7$\2\2\u0167\u0168\b\66\4\2\u0168l")
        buf.write("\3\2\2\2\u0169\u016c\5!\21\2\u016a\u016c\5#\22\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016cn\3\2\2\2\u016d")
        buf.write("\u016e\7C\2\2\u016e\u016f\7t\2\2\u016f\u0170\7t\2\2\u0170")
        buf.write("\u0171\7c\2\2\u0171\u0172\7{\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0174\7*\2\2\u0174\u0175\3\2\2\2\u0175\u0176\7+\2\2\u0176")
        buf.write("p\3\2\2\2\u0177\u0179\t\16\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017d\b9\2\2\u017dr\3\2\2\2")
        buf.write("\u017e\u017f\7%\2\2\u017f\u0180\7%\2\2\u0180\u0186\3\2")
        buf.write("\2\2\u0181\u0182\n\17\2\2\u0182\u0187\n\17\2\2\u0183\u0185")
        buf.write("\13\2\2\2\u0184\u0183\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\u0187\3\2\2\2\u0186\u0181\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u0189\7\2\2\3\u0189\u018a\b")
        buf.write(":\5\2\u018at\3\2\2\2\u018b\u018f\7$\2\2\u018c\u018e\5")
        buf.write("\13\6\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0192\u0193\5\21\t\2\u0193\u0194")
        buf.write("\b;\6\2\u0194v\3\2\2\2\u0195\u0196\13\2\2\2\u0196\u0197")
        buf.write("\b<\7\2\u0197x\3\2\2\2\24\2~\u0081\u0087\u008e\u0095\u009a")
        buf.write("\u00a5\u00ad\u014e\u0154\u015b\u0163\u016b\u017a\u0184")
        buf.write("\u0186\u018f\b\b\2\2\3\65\2\3\66\3\3:\4\3;\5\3<\6")
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
    ILLEGAL_ESCAPE = 50
    ERROR_TOKEN = 51

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
            "UNTERMINATED_COMMENT", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "DEC_INTEGER_LITERAL", "OCT_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", 
                  "HEX_INTEGER_LITERAL", "STRING_CHAR", "ESCAPE_SEQUENCE", 
                  "DOUBLE_QUOTE_CHAR", "ILLEGAL_SEQUENCE", "COMMENT", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                  "FALSE", "CLASS", "ARRAY", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "NULL", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LTE", 
                  "GT", "GTE", "STRING_EQUAL", "STRING_ADD", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "SEMI", "LCB", "RCB", "ID", 
                  "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                  "INDEXED_ARRAY", "WS", "UNTERMINATED_COMMENT", "ILLEGAL_ESCAPE", 
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
            actions[51] = self.INTEGER_LITERAL_action 
            actions[52] = self.STRING_LITERAL_action 
            actions[56] = self.UNTERMINATED_COMMENT_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_TOKEN_action 
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

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise ILLEGAL_ESCAPE(self.text[1:])
                
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise ERROR_TOKEN(self.text)
                
     


