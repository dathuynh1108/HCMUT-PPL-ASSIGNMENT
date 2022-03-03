import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_100_lowercase_identifier(self):
        self.assertTrue(TestLexer.test("abcd","abcd,<EOF>",100))
    def test_101_lowercase_identifier(self):
        self.assertTrue(TestLexer.test("abcd ab2","abcd,ab2,<EOF>",101))
    def test_102_uppercase_identifier(self):
        self.assertTrue(TestLexer.test("abcd Ab2","abcd,Ab2,<EOF>",102))
    def test_103_lower_id_error(self):
        self.assertTrue(TestLexer.test("a?bcdab2","a,Error Token ?",103))
    def test_104_lower_id_and_int(self):
        self.assertTrue(TestLexer.test("0a12","0,a12,<EOF>",104))
    def test_105_lower_upper_id(self):
        self.assertTrue(TestLexer.test("$aCBbdc","$aCBbdc,<EOF>",105))
    def test_106_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",106))
    def test_107_mixed_id(self):
        self.assertTrue(TestLexer.test("_aAvN3","_aAvN3,<EOF>",107))
    def test_108_id_error(self):
        self.assertTrue(TestLexer.test("a^sVN3","a,Error Token ^",108))
    def test_109_mixed_id_error(self):
        self.assertTrue(TestLexer.test("__ba s@","__ba,s,Error Token @",109))
    def test_110_integer(self):
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",110))
    def test_111_oct_int(self):
        self.assertTrue(TestLexer.test("01234","01234,<EOF>",111))
    def test_112_oct_integer(self):
        self.assertTrue(TestLexer.test("08123","0,8123,<EOF>",112))
    def test_113_oct_integer(self):
        self.assertTrue(TestLexer.test("008123","00,8123,<EOF>",113))
    def test_114_integer_and_dash(self):
        self.assertTrue(TestLexer.test("123_12_3","123123,<EOF>",114))
    def test_115_integer(self):
        self.assertTrue(TestLexer.test("123_123a","123123,a,<EOF>",115))
    def test_116_hex_int_id(self):
        self.assertTrue(TestLexer.test("0x123_123","0x123123,<EOF>",116))
    def test_117_int_and_id(self):
        self.assertTrue(TestLexer.test("1230b_123","1230,b_123,<EOF>",117))
    def test_118_bin_dec(self):
        self.assertTrue(TestLexer.test("0b123_123","0b1,23123,<EOF>",118))
    def test_119_integer_error(self):
        self.assertTrue(TestLexer.test("123_?123","123,_,Error Token ?",119))
    def test_120_zero_id(self):
        self.assertTrue(TestLexer.test("0XXXX","0,XXXX,<EOF>",120))
    def test_121_oct_int(self):
        self.assertTrue(TestLexer.test("01234","01234,<EOF>",121))
    def test_122_oct_integer(self):
        self.assertTrue(TestLexer.test("08123","0,8123,<EOF>",122))
    def test_123_oct_integer(self):
        self.assertTrue(TestLexer.test("008123","00,8123,<EOF>",123))
    def test_124_integer_and_dash(self):
        self.assertTrue(TestLexer.test("123_12_3","123123,<EOF>",124))
    def test_125_integer(self):
        self.assertTrue(TestLexer.test("123_123a","123123,a,<EOF>",125))
    def test_126_hex_int_id(self):
        self.assertTrue(TestLexer.test("0x123_123","0x123123,<EOF>",126))
    def test_127_int_and_id(self):
        self.assertTrue(TestLexer.test("1230b_123","1230,b_123,<EOF>",127))
    def test_128_bin_dec(self):
        self.assertTrue(TestLexer.test("0b123_123","0b1,23123,<EOF>",128))
    def test_129_integer_error(self):
        self.assertTrue(TestLexer.test("123_?123","123,_,Error Token ?",129))
    def test_130_cmt_between(self):
        self.assertTrue(TestLexer.test("ba##cmt##ba","ba,ba,<EOF>",130))
    
    def test_131_cmt_no_end(self):
        self.assertTrue(TestLexer.test("##01234","Error Token #",131))
    def test_132_block_cmt(self):
        test_in = """
## block comment
block comment
block comment 
##
ab
"""     
        expect = """ab,<EOF>"""
        self.assertTrue(TestLexer.test(test_in,expect,132))
    def test_133_another_block_cmt(self):
        test_in = """
## block comment
# block comment
# block comment
# this is another type of block comment 
##
ab
"""     
        expect = """ab,<EOF>"""
        self.assertTrue(TestLexer.test(test_in,expect,133))
    def test_134_also_block_cmt(self):
        test_in = """
## block comment #
# block comment  #
# block comment  #
# block comment ##
ab
"""     
        expect = """ab,<EOF>"""
        self.assertTrue(TestLexer.test(test_in,expect,134))
    def test_135_mix_cmt_1(self):
        test_in = """
    ## This is a line comment ##
    ## Comment with many lines
        foo comment
    ##
    ##
        Comment with many lines
    ##
    ## nest comments
        ## "this will be out side" ##
    # inline comment
    ##
ab
"""     
        expect = """this will be out side,ab,<EOF>"""
        self.assertTrue(TestLexer.test(test_in,expect,135))
    def test_136_mix_cmt_2(self):
        test_in = """
## This is the style comment of D96
# The writer of this comment is very handsome
    ##
    ## This is inline comment ##
    ##
    \b\t\c\n\r this is some shit
    # This is comment ##
"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(test_in,expect,136))
    def test_137_mix_cmt_3(self):
        test_in = """
/* /* ## // /b/r/n */ */
    UwU/// # has no meaning here \_0_/
    # This is comment  ##      
        """
        expect = """/,*,/,*,<EOF>"""
        self.assertTrue(TestLexer.test(test_in,expect,137))
    def test_138_error_cmt_2(self):
        test_in = """
##!/usr/bin/env 
CC=gcc
CFLAGS=-I.
DEPS = hellomake.h
OBJ = hellomake.o hellofunc.o 
/## -*- coding UTF-8 -*-       
        """
        expect = """-,*,-,coding,UTF,-,8,-,*,-,<EOF>"""
        self.assertTrue(TestLexer.test(test_in,expect,138))
    def test_139_error_cmt_3(self):
        test_in = """
######
"""
        expect = """Error Token #"""
        self.assertTrue(TestLexer.test(test_in,expect,139))
    def test_140_string_lit(self):
        in_str = """
"abcd"
        """
        out_str = """abcd,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,140))
    
    def test_141_string_lit_mix(self):
        in_str = """
"String"
""
" "
"?"
"-"
"//"
"Multi Chars"
        """
        out_str = """String,, ,?,-,//,Multi Chars,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,141))
    def test_142_string_error_1(self):
        in_str = """
""
"abc"
'abc'
"abc'
'abc" 
        """
        out_str = """,abc,Error Token '"""
        self.assertTrue(TestLexer.test(in_str,out_str,142))
    
    def test_143_string_lit_mix(self):
        in_str = """
""
12 23.34 45.E56 6e-7 true "false" false "078" 1.32 1.
"abc"
        """
        out_str = """,12,23.34,45.E56,6e-7,true,false,false,078,1.32,1.,abc,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,143))
    
    def test_144_unclosed_string(self):
        in_str = """
"Bruh
"""
        out_str = """Unclosed String: Bruh"""
        self.assertTrue(TestLexer.test(in_str,out_str,144))
    def test_145_unclosed_string_multi_line(self):
        in_str = """
"bruh
Bruh x2"
"""
        out_str = """Unclosed String: bruh"""
        self.assertTrue(TestLexer.test(in_str,out_str,145))
    
    def test_146_unclosed_esc(self):
        in_str = """
"\"abc 
        """
        out_str = """,abc,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,146))
    
    def test_147_illegal_close_str(self):
        in_str = """
abc = "string     '
"a = "bruh"
g = "bruh x2"
        """
        out_str = """abc,=,Unclosed String: string     '"""
        self.assertTrue(TestLexer.test(in_str,out_str,147))
    def test_148_string_esc_in_line(self):
        in_str = """
"abc \n def "
"abc \\n def "
        """
        out_str = """Unclosed String: abc """
        self.assertTrue(TestLexer.test(in_str,out_str,148))
    def test_149_string_esc_in_line_2(self):
        in_str = """
"this is a foo string with escape \b \t \r \""
        """
        out_str = """Unclosed String: this is a foo string with escape """
        self.assertTrue(TestLexer.test(in_str,out_str,149))
    
    def test_150_string_esc_2(self):
        in_str = r"""
    "backspace  \b"
    "formfeed   \f"
    "return     \r"
    "newline    \n"
    "tab        \t"
    "quote       \'"
    "backslash  \\"
    "double     '""
    """
        out_str = r"""backspace  \b,formfeed   \f,return     \r,newline    \n,tab        \t,quote       \',backslash  \\,double     '",<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,150))

    def test_151_illegal_esc(self):
        in_str = """
aBC"\a"    
    """
        out_str = """aBC,\a,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,151))
    
    def test_152_string_legal_illegal_mix(self):
        in_str = """
"This'"s legal string"
" Hi Hi \z \d "    
        """
        out_str = """This'"s legal string,Illegal Escape In String:  Hi Hi \z"""
        self.assertTrue(TestLexer.test(in_str,out_str,152))
    
    def test_153_illegal_esc(self):
        in_str = """
"abc -+ def"
"abc \ def"
    """
        out_str = """abc -+ def,Illegal Escape In String: abc \ """
        self.assertTrue(TestLexer.test(in_str,out_str,153))
    def test_154_illegal_esc_2(self):
        in_str = """
"abc -+ def"
"abc \def"
    """
        out_str = """abc -+ def,Illegal Escape In String: abc \d"""
        self.assertTrue(TestLexer.test(in_str,out_str,154))
    def test_155_illegal_esc_3(self):
        in_str = """
"abc\def"
    """
        out_str = """Illegal Escape In String: abc\d"""
        self.assertTrue(TestLexer.test(in_str,out_str,155))
    def test_156_illegal_esc_4(self):
        in_str = """
"\z"    
    """
        out_str = """Illegal Escape In String: \z"""
        self.assertTrue(TestLexer.test(in_str,out_str,156))
    def test_157_illegal_esc_5(self):
        in_str = """
"ashjkdashjdgjhasghjsdgajhdagdjagdgas78213681dg\d"    
    """
        out_str = """Illegal Escape In String: ashjkdashjdgjhasghjsdgajhdagdjagdgas78213681dg\d"""
        self.assertTrue(TestLexer.test(in_str,out_str,157))
    def test_158_illegal_esc_6(self):
        in_str = """
"!1@2#3$4%5^6&7*8(9)0\*))))23"    
    """
        out_str = """Illegal Escape In String: !1@2#3$4%5^6&7*8(9)0\*"""
        self.assertTrue(TestLexer.test(in_str,out_str,158))

    def test_159_illegal_esc_7(self):
        in_str = """
"ABC:\\h"
        """
        out_str = """Illegal Escape In String: ABC:\\h"""
        self.assertTrue(TestLexer.test(in_str,out_str,159))

    def test_160_unclosed_string(self):
        in_str = """
"abc \r  def "
        """
        out_str = """Unclosed String: abc """
        self.assertTrue(TestLexer.test(in_str,out_str,160))
    
    def test_161_unclosed_string_2(self):
        in_str = """
"abc \fde"
        """
        out_str = """Unclosed String: abc """
        self.assertTrue(TestLexer.test(in_str,out_str,161))
    
    def test_162_unclosed_string_3(self):
        in_str = """
"abc \n def"
        """
        out_str = """Unclosed String: abc """
        self.assertTrue(TestLexer.test(in_str,out_str,162))
    
    def test_163_unclosed_string_4(self):
        in_str = """
"abc \t def"
        """
        out_str = """Unclosed String: abc """
        self.assertTrue(TestLexer.test(in_str,out_str,163))
    
    def test_164_error_token(self):
        in_str = """
!= !== ^ % $ # & ... 
        """
        out_str = """!=,!=,=,Error Token ^"""
        self.assertTrue(TestLexer.test(in_str,out_str,164))
    
    def test_165_error_token_2(self):
        in_str = """
cc=cc~~1
        """
        out_str = """cc,=,cc,Error Token ~"""
        self.assertTrue(TestLexer.test(in_str,out_str,165))
    
    def test_166_error_token_3(self):
        in_str = """
'cc!=ca
        """
        out_str = """Error Token '"""
        self.assertTrue(TestLexer.test(in_str,out_str,166))
    
    def test_167_error_token_4(self):
        in_str = """
abc`
        """
        out_str = """abc,Error Token `"""
        self.assertTrue(TestLexer.test(in_str,out_str,167))
    
    def test_168_error_token_5(self):
        in_str = """
hkkbacr59acr61acr67/*/%/^
        """
        out_str = """hkkbacr59acr61acr67,/,*,/,%,/,Error Token ^"""
        self.assertTrue(TestLexer.test(in_str,out_str,168))
    
    def test_169_error_token_6(self):
        in_str = """
0=()/_(+_+)_/(()$)
        """
        out_str = """0,=,(,),/,_,(,+,_,+,),_,/,(,(,),Error Token $"""
        self.assertTrue(TestLexer.test(in_str,out_str,169))
    
    def test_170_error_token_7(self):
        in_str = """
*()*/%!-+{+}|*()
        """
        out_str = """*,(,),*,/,%,!,-,+,{,+,},Error Token |"""
        self.assertTrue(TestLexer.test(in_str,out_str,170))
    
    def test_171_error_token_8(self):
        in_str = """
 ;,[](){}%+-*/====@akkojellyblack*
        """
        out_str = """;,,,[,],(,),{,},%,+,-,*,/,==,==,Error Token @"""
        self.assertTrue(TestLexer.test(in_str,out_str,171))
    
    def test_172_keyword(self):
        in_str = """
Break Continue If Elseif Else
Foreach True False Array In
Int Float Boolean String Return
Null Class Val Var Self
Constructor Destructor New By
        """
        out_str = """Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Self,Constructor,Destructor,New,By,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,172))
    
    def test_173_wrong_keyword(self):
        in_str = """
breAk12 Continue ifElseif elSe
        """
        out_str = """breAk12,Continue,ifElseif,elSe,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,173))
    
    def test_174_wrong_keyword_2(self):
        in_str = """
ForEach tRue 1.3falsE 1.4aRRay in23
        """
        out_str = """ForEach,tRue,1.3,falsE,1.4,aRRay,in23,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,174))
    
    def test_175_operator(self):
        in_str = """
+ - * / %
! && || == =
!= < <= > >=
==. +. . :: New
        """
        out_str = """+,-,*,/,%,!,&&,||,==,=,!=,<,<=,>,>=,==.,+.,.,::,New,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,175))
    
    def test_176_operator_2(self):
        in_str = """
*= /= -= +=
        """
        out_str = """*,=,/,=,-,=,+,=,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,176))
    
    def test_177_operator_3(self):
        in_str = """
++ -- & ^ |
        """
        out_str = """+,+,-,-,Error Token &"""
        self.assertTrue(TestLexer.test(in_str,out_str,177))
    
    def test_178_operator_4(self):
        in_str = """
hk(kb)+acr**59-acr=-61*acr<>67/!
        """
        out_str = """hk,(,kb,),+,acr,*,*,59,-,acr,=,-,61,*,acr,<,>,67,/,!,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,178))
    
    def test_179_operator_5(self):
        in_str = """
   i+=s.12*12+m/10.
        """
        out_str = """i,+,=,s,.,12,*,12,+,m,/,10.,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,179))
    
    def test_180_operator_6(self):
        in_str = """
ax^2+bx+c=0
        """
        out_str = """ax,Error Token ^"""
        self.assertTrue(TestLexer.test(in_str,out_str,180))
    
    def test_181_case_sensitive(self):
        in_str = """
false False faLSe
        """
        out_str = """false,False,faLSe,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,181))
    
    def test_182_case_sensitve_2(self):
        in_str = """
Null Class Val Var Self NuLl ClaSS VAl VAR SeLf null cLAss Val Var SElf
        """
        out_str = """Null,Class,Val,Var,Self,NuLl,ClaSS,VAl,VAR,SeLf,null,cLAss,Val,Var,SElf,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,182))
    
    def test_183_float_lit(self):
        in_str = """
1.1
        """
        out_str = """1.1,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,183))
    
    def test_184_float_lit_2(self):
        in_str = """
1.1a
        """
        out_str = """1.1,a,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,184))
    
    def test_185_float_lit_3(self):
        in_str = """
0.1101010101000
0e-432
1e-542400
313121.e00031321132
        """
        out_str = """0.1101010101000,0e-432,1e-542400,313121.e00031321132,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,185))
    
    def test_186_float_lit_4(self):
        in_str = """
1e 123e e123 e-123 -e123 123e4 1.e2 .e12
        """
        out_str = """1,e,123,e,e123,e,-,123,-,e123,123e4,1.e2,.e12,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,186))
    
    def test_187_float_lit_5(self):
        in_str = """
1.3e10
        """
        out_str = """1.3e10,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,187))
    
    def test_188_float_lit_6(self):
        in_str = """
-1.3e12
        """
        out_str = """-,1.3e12,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,188))
    
    def test_189_float_lit_7(self):
        in_str = """
-1.3e+12
        """
        out_str = """-,1.3e+12,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,189))
    
    def test_190_float_lit_8(self):
        in_str = """
-1.3e+-12
        """
        out_str = """-,1.3,e,+,-,12,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,190))
    
    def test_191_random_1(self):
        in_str = """
a = b;
a = b + c;
c = 9;
d = 10;
        """
        out_str = """a,=,b,;,a,=,b,+,c,;,c,=,9,;,d,=,10,;,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,191))
    
    def test_192_random_2(self):
        in_str = """
Foreach (x In 5 .. 2) {
    Out.printInt(arr[x]);
}
        """
        out_str = """Foreach,(,x,In,5,..,2,),{,Out,.,printInt,(,arr,[,x,],),;,},<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,192))
    
    def test_193_random_3(self):
        in_str = """
int a,b       ,c ,x                   y;
float a = b (def).12;
str arr[] = {1,2,3};
        """
        out_str = """int,a,,,b,,,c,,,x,y,;,float,a,=,b,(,def,),.,12,;,str,arr,[,],=,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,193))
    
    def test_194_random_4(self):
        in_str = """
# ],],* ae0bc not mod,return,,
    {} < + Qbef and ; of 6969 false else < > and for Mod007 & <> return = for if ..
        """
        out_str = """Error Token #"""
        self.assertTrue(TestLexer.test(in_str,out_str,194))
    
    def test_195_random_5(self):
        in_str = """
cc=cc~~1
        """
        out_str = """cc,=,cc,Error Token ~"""
        self.assertTrue(TestLexer.test(in_str,out_str,195))
    
    def test_196_random_6(self):
        in_str = """
New <identifier>(<list of expressions>)
        """
        out_str = """New,<,identifier,>,(,<,list,of,expressions,>,),<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,196))
    
    def test_197_random_7(self):
        in_str = """
ab::ab(ab,bc,1e5)
        """
        out_str = """ab,::,ab,(,ab,,,bc,,,1e5,),<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,197))
    
    def test_198_random_8(self):
        in_str = """
Val a: String = "String"
Val b: Float = 1e-1
        """
        out_str = """Val,a,:,String,=,String,Val,b,:,Float,=,1e-1,<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,198))
    
    def test_199_random_9(self):
        in_str = """
Class Circle {
    float getArea(){
        return this.radius*this.radius*pi;
    }
}
        """
        out_str = """Class,Circle,{,float,getArea,(,),{,return,this,.,radius,*,this,.,radius,*,pi,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(in_str,out_str,199))
