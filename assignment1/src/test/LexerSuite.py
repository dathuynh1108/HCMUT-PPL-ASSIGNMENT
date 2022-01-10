import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    ### Test method is sorted by alphabet before run 
    # --> Name it with alphabet order to show right order of Text Test Runner
    # test identifiers 
    def test_001_id(self):
        input = "abc xyz,    abc xyz"
        expect = "abc,xyz,,,abc,xyz,<EOF>"
        num = 101
        self.assertTrue(TestLexer.test(input,expect,num))
    
    def test_002_id(self):
        input = "aBcDeF"
        expect = "aBcDeF,<EOF>"
        num = 102
        self.assertTrue(TestLexer.test(input,expect,num))
    
    def test_003_id(self):
        input = "aBcDeF123_abcd;_123aBc; xyz abc 123abc"
        expect = "aBcDeF123_abcd,;,_123aBc,;,xyz,abc,123,abc,<EOF>"
        num = 103
        self.assertTrue(TestLexer.test(input,expect,num))
    
    def test_004_id(self):
        input = "id1 id&&1 -id1 _ __ _id1 _id_1"
        expect = "id1,id,&&,1,-,id1,_,__,_id1,_id_1,<EOF>"
        num = 104
        self.assertTrue(TestLexer.test(input,expect,num))
    
    def test_005_id(self):
        input = "$static_variable_123 normal_variable_123 $_ $"
        expect = "$static_variable_123,normal_variable_123,$_,Error Token $"
        num = 105
        self.assertTrue(TestLexer.test(input,expect,num))
    
    #test comment
    def test_006_comment(self):
        input = """ 
            ##Comment line 1
            Comment line 2##
            \r\n\t\f
            ## Hi ##
            abc, 123
        """
        expect = "abc,,,123,<EOF>"
        num = 106
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_007_comment(self):
        input = """
            ## This is inline comment \t\r\n\f\\';><?##
            ## 
                This is block comment
                This is block comment
                This is block comment
                Huynh Thanh Dat
                11082001
                _____________________
                \t\r\n\f\\';><?
            ##
            Huynh Thanh Dat
        """
        expect = "Huynh,Thanh,Dat,<EOF>"
        num = 107
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_008_comment(self):
        input = """
            ## This comment ok ##
            ## 
            # Line 1
            # Line 2
            Line 3
            ##
            ###"""
        expect = "Unterminated Comment"
        num = 108
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_009_comment(self):
        # Reference on """ of python, it is not valid for nested """
        input = """
            #### Comment in comment ####
            ## #Unterminated Comment
        """
        expect = "Comment,in,comment,Unterminated Comment"
        num = 109
        self.assertTrue(TestLexer.test(input,expect,num))
    
    #test integers
    def test_010_integer(self):

        input = "1234, 123 ; 123 456 0123 0x1234ffff 0X1234AAAA"
        expect = "1234,,,123,;,123,456,0123,0x1234ffff,0X1234AAAA,<EOF>"
        num = 110
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_011_integer(self):
    
        input = "12345 12____3_45 0x0___0_1___2___3 012___3__45 0b00___111__00__11"
        expect = "12345,12345,0x0,___0_1___2___3,012,___3__45,0b00,___111__00__11,<EOF>"
        num = 111
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_012_integer(self):
        # _INT is variable
        input = "1_2_3_4_5 1_____2 ______1 1_______"
        expect = "12345,12,______1,1,_______,<EOF>"
        num = 112
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_013_integer(self):
        # _INT is variable
        # Note question 0_x123: 0_ x123 or 0 _x123 --> can _ is the last char in INT
        input = "012345 0_12345 01_2345 0x12345 0x_12345 0_x12345 0b010101 0b_010101 0_b010101"
        expect = "012345,0,_12345,01,_2345,0x12345,0,x_12345,0,_x12345,0b010101,0,b_010101,0,_b010101,<EOF>"
        num = 113
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_014_integer(self):
        # _INT is variable
        input = "0XFFFF 0xffff 0XZZZZ 0xzzzz 0B1111 0b1111 0B2222 0b2222 09999 0"
        expect = "0XFFFF,0xffff,0,XZZZZ,0,xzzzz,0B1111,0b1111,0,B2222,0,b2222,0,9999,0,<EOF>"
        num = 114
        self.assertTrue(TestLexer.test(input,expect,num))    
    
    # test string
    def test_015_string(self):
        input = r"""
            "Test escape sequence\b\f\r\n\t\'\\'""    
            ""     
        """
        expect = r"""Test escape sequence\b\f\r\n\t\'\\'",,<EOF>"""
        num = 115
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_016_string(self):
        input = r"""
            "String" "string" "string     " "string\nstring"
        """
        expect = r"""String,string,string     ,string\nstring,<EOF>"""
        num = 116
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_017_string(self):
        input = r"""
            "" "__STRING__STRING" "'"String in string'"" "String'"String in string'"String in string in string'"String in String'"String"
        """
        expect = r""",__STRING__STRING,'"String in string'",String'"String in string'"String in string in string'"String in String'"String,<EOF>"""
        num = 117
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_018_string(self):
        input = r"""
            This is not string
            "This is string\n\r\\"
            "ILLEGAL_ESCAPE\z"
        """
        expect = r"""This,is,not,string,This is string\n\r\\,Illegal Escape In String: ILLEGAL_ESCAPE\z"""
        num = 118
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_019_string(self):
        input = r"""
            "OK\'"
            "OK'""
            "ILLEGAL_ESCAPE\""
        """
        expect = r"""OK\',OK'",Illegal Escape In String: ILLEGAL_ESCAPE\""""
        num = 119
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_020_string(self):        
        input = r"""
            "abc"
            "abc\'"
            "abc'"
        """
        expect = "abc,abc\\',Unclosed String: abc'\""
        num = 120
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_021_string(self):
        input = r"""
            "Normal string"
            ## "String in comment" ##
            "## Comment in string ##"
            "String""String"
            "'"String in string'""
            ""This is not a string in string""
        """
        expect = r"""Normal string,## Comment in string ##,String,String,'"String in string'",,This,is,not,a,string,in,string,,<EOF>"""
        num = 121
        self.assertTrue(TestLexer.test(input,expect,num))        
    def test_022_string(self):        
        input = r"""
            "Int" "Float"
            "a'"b'"c"
            "!@#$%^&*()_-+=[]{}|/?><"
        """
        expect = r"""Int,Float,a'"b'"c,!@#$%^&*()_-+=[]{}|/?><,<EOF>"""
        num = 122
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_023_string(self):
        input = r"""
            "Huynh Thanh Dat \t 1910110 \n 11 08 2001"
            "abc\""
        """
        expect = r"""Huynh Thanh Dat \t 1910110 \n 11 08 2001,Illegal Escape In String: abc\""""
        num = 123
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_024_string(self):
        input = r"""
            "a\bb\fc\rd\ne\tf\\"
            "a\'b"
            "a'b"
        """
        expect = r"""a\bb\fc\rd\ne\tf\\,a\'b,Illegal Escape In String: a'b"""
        num = 124
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_025_string(self):
        input = r"""
            "{string}" 
            "'"{string}'""
            "(string)"
            "[string]"
            "`string`"
            "" not_string ""
        """
        expect = r"""{string},'"{string}'",(string),[string],`string`,,not_string,,<EOF>"""
        num = 125
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_026_string(self):
        input = r"""
            "Unclose string
        """
        expect = r"""Unclosed String: Unclose string"""
        num = 126
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_027_string(self):
        input = r"""
            "Unclose string with escape sequence\n\t\r\f\b
        """
        expect = r"""Unclosed String: Unclose string with escape sequence\n\t\r\f\b"""
        num = 127
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_028_string(self):
        input = r"""
            "String end with double quote'""
            "Unclose string end with double quote'"
        """
        expect = """String end with double quote'",Unclosed String: Unclose string end with double quote'\""""
        num = 128
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_029_string(self):
        input = r"""
            String s = "string"
            String s2 = "string"
            String s3 = "unclose string
            next_line
        """
        expect = r"""String,s,=,string,String,s2,=,string,String,s3,=,Unclosed String: unclose string"""
        num = 129
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_030_string(self):
        input = r"""
            "\\a"
            "String"
            " "
            "?" "-" "#" "!" "@" "#" "$" "%" "^" "&" "*" "(" ")" "-" "_" "+" ";" ":" ";" "<" ">" "?"
            "Mulitiple Characters"
        """
        expect = r"""\\a,String, ,?,-,#,!,@,#,$,%,^,&,*,(,),-,_,+,;,:,;,<,>,?,Mulitiple Characters,<EOF>"""
        num = 130
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_031_string(self):
        input = r"""
            "Valid string"
            'Invalid string'
        """
        expect = r"""Valid string,Error Token '"""
        num = 131
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_032_string(self):
        input = r"""
            "Valid string"
            "Invalid string'"
        """
        expect = """Valid string,Unclosed String: Invalid string'\""""
        num = 132
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_033_string(self):
        input = r"""
            "Valid string"
            'Invalid string'
        """
        expect = r"""Valid string,Error Token '"""
        num = 133
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_034_string(self):
        input = r"""
            "String with expression: 1+1*1/1%1*(1+1)"
        """
        expect = r"""String with expression: 1+1*1/1%1*(1+1),<EOF>"""
        num = 134
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_035_string(self):
        input = r"""
            ## Test Comment ##
            "String with expression: 1+1*1/1%1*(1+1)"
            ## Test Comment ##
        """
        expect = r"""String with expression: 1+1*1/1%1*(1+1),<EOF>"""
        num = 135
        self.assertTrue(TestLexer.test(input,expect,num))     
    def test_036_string(self):
        input = r"""
            "String in comment"
            "## Comment in string ##"
            "parentheses in string"
            ("string in parentheses")
        """
        expect = r"""String in comment,## Comment in string ##,parentheses in string,(,string in parentheses,),<EOF>"""
        num = 136
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_037_string(self):
        input = r"""
            ## test with syntax ##        
            var $string_1: String = "this is a string";
            var $string_2: String = "this is a string";
        """
        expect = r"""var,$string_1,:,String,=,this is a string,;,var,$string_2,:,String,=,this is a string,;,<EOF>"""
        num = 137
        self.assertTrue(TestLexer.test(input,expect,num))  
    def test_038_string(self):
        input = r"""
            var $string_1: String = "abc"; ## Comment ##
            string_1 = string_1 +. "def" +. "xyz";
            var $string_2: String = "abcdefxyz";
        """
        expect = r"""var,$string_1,:,String,=,abc,;,string_1,=,string_1,+.,def,+.,xyz,;,var,$string_2,:,String,=,abcdefxyz,;,<EOF>"""
        num = 138
        self.assertTrue(TestLexer.test(input,expect,num)) 
    # Test boolean
    def test_039_boolean(self):
        input = r"""
            True TRUE False FALSE True_with_other_chars False_with_other_chars
        """
        expect = r"""True,TRUE,False,FALSE,True_with_other_chars,False_with_other_chars,<EOF>"""
        num = 139
        self.assertTrue(TestLexer.test(input,expect,num))   
    # Test float
    def test_040_float(self):
        # 3 component
        input = r"""
            1.234 1.234e10 1.234e-10 1_234.567e10 1_234.567e-10 1_123.1_123e1_123 1.e1_123
        """
        expect = r"""1.234,1.234e10,1.234e-10,1234.567e10,1234.567e-10,1123.1123e1123,1.e1123,<EOF>"""
        num = 140
        self.assertTrue(TestLexer.test(input,expect,num))   
    
    def test_041_float(self):
        # Miss Exponent
        input = r"""
            1.1234 00001.1234 1.  000001. 1.1234 1_123.1_123 1___1___2___3.1___1___2___3 1_123.
        """
        expect = r"""1.1234,00001.1234,1.,000001.,1.1234,1123.1123,1123.1123,1123.,<EOF>"""
        num = 141
        self.assertTrue(TestLexer.test(input,expect,num))  
    def test_042_float(self):
        # Miss Decimal
        input = r"""
            123e123 123E123 123e-123 123E-123 00123e00123 00123E00123
        """
        expect = r"""123e123,123E123,123e-123,123E-123,00123e00123,00123E00123,<EOF>"""
        num = 142
        self.assertTrue(TestLexer.test(input,expect,num))  
    def test_043_float(self):
        # Miss Decimal
        input = r"""
            1_123e1_123 1_123E1_123 1_____123e1_______123 1____123E1______123
        """
        expect = r"""1123e1123,1123E1123,1123e1123,1123E1123,<EOF>"""
        num = 143
        self.assertTrue(TestLexer.test(input,expect,num))  
    def test_044_float(self):
        # Miss Integer
        input = r"""
            .123 .1_123 .123e123 .123E123 .1_123e1_123 .1___123e1___123 .1_123E1_123 .1___123E1___123 .e123 .e1_123
        """
        expect = r""".,123,.,1123,.123e123,.123E123,.1123e1123,.1123e1123,.1123E1123,.1123E1123,.e123,.e1123,<EOF>"""
        num = 144
        self.assertTrue(TestLexer.test(input,expect,num))  
    def test_045_float(self):
        input = r"""
            123 123. 9.9999 0.9999 0. .0 0.0e10 
        """
        expect = r"""123,123.,9.9999,0.9999,0.,.,0,0.0e10,<EOF>"""
        num = 145
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_046_float(self):
        input = r"""
            .123e1.123 .123e1.123e1
        """
        expect = r""".123e1,.,123,.123e1,.123e1,<EOF>"""
        num = 146
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_047_float(self):
        input = r"""
            0x123.123 0x123.123e10 abc.123 abc.123e10
        """
        expect = r"""0x123,.,123,0x123,.123e10,abc,.,123,abc,.123e10,<EOF>"""
        num = 147
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_048_float(self):
        input = r"""
            0x123.123 0x123.123e10 0b1111.111 0b11112.123
        """
        expect = r"""0x123,.,123,0x123,.123e10,0b1111,.,111,0b1111,2.123,<EOF>"""
        num = 148
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_049_float(self):
        input = r"""
            var $float_1: Float = 1.123;
            var $float_2: Float = 1.123e10;
        """
        expect = r"""var,$float_1,:,Float,=,1.123,;,var,$float_2,:,Float,=,1.123e10,;,<EOF>"""
        num = 149
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_050_float(self):
        input = r"""
            0000000000.000000000 1_2_3_4.1_2_3_4e1_2_3_4 1_2_3_4.1_2_3_4e-1_2_3_4 
        """
        expect = r"""0000000000.000000000,1234.1234e1234,1234.1234e-1234,<EOF>"""
        num = 150
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_051_float(self):
        input = r"""
            1e1 1e-1 1e+1 123.123e+123 123.123e-123
        """
        expect = r"""1e1,1e-1,1e+1,123.123e+123,123.123e-123,<EOF>"""
        num = 151
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_052_float(self):
        input = r"""
            1_____2______3.1_____2_____3e1____23
            1_____2______3.1_____2_____3e+1____23
            1_____2______3.1_____2_____3e-1____23
            1___2__3.1____2____3
            1___2___3e1____2____3
            1___2___3e+1____2____3
            1___2___3e-1____2____3
        """
        expect = r"""123.123e123,123.123e+123,123.123e-123,123.123,123e123,123e+123,123e-123,<EOF>"""
        num = 152
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_053_float(self):
        input = r"""
            123e+123 + 123e+123 - 123e-123
        """
        expect = r"""123e+123,+,123e+123,-,123e-123,<EOF>"""
        num = 153
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_054_float(self):
        input = r"""
            +.123e1
            + .123e1
            ==.123e1
            == .123e1
        """
        expect = r"""+.,123e1,+,.123e1,==.,123e1,==,.123e1,<EOF>"""
        num = 154
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_055_float_with_others(self):
        input = r"""
            "1.1e+1+1+1e+1"
            1.1 + 2.2 + 3.3
            1.1e+1+1+1e+1
            1.+1.1e+1+ .1e+1+ .0e-1 -.1
            1.-123
            +1.123e+1+1
        """
        expect = r"""1.1e+1+1+1e+1,1.1,+,2.2,+,3.3,1.1e+1,+,1,+,1e+1,1.,+,1.1e+1,+,.1e+1,+,.0e-1,-,.,1,1.,-,123,+,1.123e+1,+,1,<EOF>"""
        num = 155
        self.assertTrue(TestLexer.test(input,expect,num))    
    def test_056_float(self):
        input = r"""
            var $float_1: Float = 1.1_234e1_234;
            var $float_2: Float = .1_234e1_234;
            var $float_3: Float = 1.1_234;
            var $float_4: Float = 1.e10_000;
            var $float_5: Float = 1e10_000;
        """
        expect = r"""var,$float_1,:,Float,=,1.1234e1234,;,var,$float_2,:,Float,=,.1234e1234,;,var,$float_3,:,Float,=,1.1234,;,var,$float_4,:,Float,=,1.e10000,;,var,$float_5,:,Float,=,1e10000,;,<EOF>"""
        num = 156
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_057_float(self):
        input = r"""
            1.123
            .1_123e1
            .1_123e1_123
            .e1_123
            .e_1123
            abc.e1_123
            "".e1_123
            ''.e1_123
        """
        expect = r"""1.123,.1123e1,.1123e1123,.e1123,.,e_1123,abc,.e1123,,.e1123,Error Token '"""
        num = 157
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_058_float(self):
        input = r"""
            1.123e10 + 1.123e10
            .123e10 + .123e10
            1.123e+10 + 1.123e+10
            1.123e-10 - 1.123e-10
            1.123e+10 * 1.123e-10
            1.123e+10 / 1.123e-10
            1.123e+10 % 1.123e-10
        """
        expect = r"""1.123e10,+,1.123e10,.123e10,+,.123e10,1.123e+10,+,1.123e+10,1.123e-10,-,1.123e-10,1.123e+10,*,1.123e-10,1.123e+10,/,1.123e-10,1.123e+10,%,1.123e-10,<EOF>"""
        num = 158
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_059_float(self):
        input = r"""
            1.1e+1+1
            .e+1+1
            1.1e++1+1
            .e++1+1
            1.1e-1-1
            .e-1-1
            1.1e-1--1
            .e--1-1
            1.1e*1
            1.1e/1
            1.1e+.1
            .1e1.1e1
            1.123.123
            1.123.123e10
        """
        expect = r"""1.1e+1,+,1,.e+1,+,1,1.1,e,+,+,1,+,1,.,e,+,+,1,+,1,1.1e-1,-,1,.e-1,-,1,1.1e-1,-,-,1,.,e,-,-,1,-,1,1.1,e,*,1,1.1,e,/,1,1.1,e,+.,1,.1e1,.1e1,1.123,.,123,1.123,.123e10,<EOF>"""
        num = 159
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_060_operator(self):
        input = r"""
            + - * / % ! && || == = != < <= > >= ==. +.
        """
        expect = r"""+,-,*,/,%,!,&&,||,==,=,!=,<,<=,>,>=,==.,+.,<EOF>"""
        num = 160
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_061_operator_string(self):
        input = r"""
            ==.
            +.
            == .
            + .
            "string"+."string"
            "string"==."string"
        """
        expect = r"""==.,+.,==,.,+,.,string,+.,string,string,==.,string,<EOF>"""
        num = 161
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_062_operator_float(self):
        input = r"""
            1e+1+1e+1
            1e-1-1e-1
            .e-1-.e-1
            .e+1+.e+1
        """
        expect = r"""1e+1,+,1e+1,1e-1,-,1e-1,.e-1,-,.e-1,.e+1,+.,e,+,1,<EOF>"""
        num = 162
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_063_operator(self):
        input = r"""
            x = (a+b)*c-d||(a-b)/c &&(a-b)%d==!1
            x!=y
            x>y+1
            x>=y+100
            x<y*2/3+1
            x<=y
            x**y
            ++x
            --x
            x^y
        """
        expect = r"""x,=,(,a,+,b,),*,c,-,d,||,(,a,-,b,),/,c,&&,(,a,-,b,),%,d,==,!,1,x,!=,y,x,>,y,+,1,x,>=,y,+,100,x,<,y,*,2,/,3,+,1,x,<=,y,x,*,*,y,+,+,x,-,-,x,x,Error Token ^"""
        num = 163
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_064_operator_with_others(self):
        input = r"""
            "!a+b-c*d/x%y&&z||1!=1==1"
            ##!a+b-c*d/x%y&&z||1!=1==1##
            !a+b-c*d/x%y&&z||1!=1==1
            "a>100>=1<=10<100"
            ##a>100>=1<=10<100##
            a>100>=1<=10<100
        """
        expect = r"""!a+b-c*d/x%y&&z||1!=1==1,!,a,+,b,-,c,*,d,/,x,%,y,&&,z,||,1,!=,1,==,1,a>100>=1<=10<100,a,>,100,>=,1,<=,10,<,100,<EOF>"""
        num = 164
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_065_seperator(self):
        input = r"""
            ()[]{}.,;:
        """
        expect = r"""(,),[,],{,},.,,,;,:,<EOF>"""
        num = 165
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_066_seperator(self):
        input = r"""
            [](x,y) {
                var a,b;
                x[0] == a == y[0] == b;
            }
        """
        expect = r"""[,],(,x,,,y,),{,var,a,,,b,;,x,[,0,],==,a,==,y,[,0,],==,b,;,},<EOF>"""
        num = 166
        self.assertTrue(TestLexer.test(input,expect,num)) 
    def test_067_seperator(self):
        input = r"""
            int main() {
                int a,b,c = 0;
                cin >> a >> b >> c;
                cout << "Huynh Thanh Dat";
                int a[100];
                {
                    a[1] = a[1] + a[2];
                    a[1] == a[3];
                }
            }
        """
        expect = r"""int,main,(,),{,int,a,,,b,,,c,=,0,;,cin,>,>,a,>,>,b,>,>,c,;,cout,<,<,Huynh Thanh Dat,;,int,a,[,100,],;,{,a,[,1,],=,a,[,1,],+,a,[,2,],;,a,[,1,],==,a,[,3,],;,},},<EOF>"""
        num = 167
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_068_seperator_operator(self):
        input = r"""
                ##  
                x=array[(a+b)-c*d] >=1>0<=10<100;
                {
                    a**b
                    a%b
                    a$b
                    x=a==1?b:c;
                }
                ##

                x=array[(a+b)-c*d] >=1>0<=10<100;
                {
                    a**b
                    a%b
                    a$b
                    x=a==1?b:c;
                }
        """
        expect = r"""x,=,array,[,(,a,+,b,),-,c,*,d,],>=,1,>,0,<=,10,<,100,;,{,a,*,*,b,a,%,b,a,$b,x,=,a,==,1,Error Token ?""" 
        num = 168
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_069_seperator(self):
        input = r"""
            ()=>{
                console.log("abc");
                a[1];
                var a,b,c;
                *this.a;
                this->a;    
                int* a = new int;
                class_name::a;
                var a:Int;
            }
            
        """
        expect = r"""(,),=,>,{,console,.,log,(,abc,),;,a,[,1,],;,var,a,,,b,,,c,;,*,this,.,a,;,this,-,>,a,;,int,*,a,=,new,int,;,class_name,::,a,;,var,a,:,Int,;,},<EOF>""" 
        num = 169
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_070_type(self):
        input = r"""
            Int int Int_ 
            Float float Float_ 
            Boolean boolean Boolean_ 
            String string String_
            Array array Array_
            class Class class_
            Null null Null_
        """
        expect = r"""Int,int,Int_,Float,float,Float_,Boolean,boolean,Boolean_,String,string,String_,Array,array,Array_,class,Class,class_,Null,null,Null_,<EOF>""" 
        num = 170
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_071_keyword(self):
        input = r"""
            Break Continue If Elseif Else For var val self return In By constructor destructor
        """
        expect = r"""Break,Continue,If,Elseif,Else,For,var,val,self,return,In,By,constructor,destructor,<EOF>""" 
        num = 171
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_072_keyword(self):
        input = r"""
            Break Continue If Elseif Else For var val self return In By constructor destructor
            "Break" "Continue" "If" "Elseif" "Else" "For" "var" "val" "self" "return" "In" "By" "constructor" "destructor"
        """
        expect = r"""Break,Continue,If,Elseif,Else,For,var,val,self,return,In,By,constructor,destructor,Break,Continue,If,Elseif,Else,For,var,val,self,return,In,By,constructor,destructor,<EOF>""" 
        num = 172
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_073_keyword_complex(self):
        input = r"""
            ## Break Continue If Elseif Else For var val self return In By constructor destructor ##
            constructor() {
                If (1==1) {
                    var a: Array[Int,100];
                    val b: Array[Int,100];
                    For (i In 1..101 By 1)
                        If (a[i] == 1) return self.text;
                        Elseif (a[i] == 2) continue;
                        Else (a[i] == 3) break;
                }
            }
            destructor() {
                return;
            }
        """
        expect = r"""constructor,(,),{,If,(,1,==,1,),{,var,a,:,Array,[,Int,,,100,],;,val,b,:,Array,[,Int,,,100,],;,For,(,i,In,1.,.,101,By,1,),If,(,a,[,i,],==,1,),return,self,.,text,;,Elseif,(,a,[,i,],==,2,),continue,;,Else,(,a,[,i,],==,3,),break,;,},},destructor,(,),{,return,;,},<EOF>""" 
        num = 173
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_074_integer(self):
        input = r"""
            1_234 1_____2_____3_____4_____5  1__234_
            0123 0_123 01_23
            0x123 0_x123 0x_123 0x1_23
            0b111 0_b111 0b_111 0b1_11
        """
        expect = r"""1234,12345,1234,_,0123,0,_123,01,_23,0x123,0,_x123,0,x_123,0x1,_23,0b111,0,_b111,0,b_111,0b1,_11,<EOF>""" 
        num = 174
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_075_integer(self):
        input = r"""
            ____1234
            1____234
            1234____

            0xabcdef
            0XaBcDeF
            0b111111
            0B111111
            0x0
            0X0
            0b0
            0B0

            0xzxcvbb
            0b222222
            09999999
        """
        expect = r"""____1234,1234,1234,____,0xabcdef,0XaBcDeF,0b111111,0B111111,0x0,0X0,0b0,0B0,0,xzxcvbb,0,b222222,0,9999999,<EOF>""" 
        num = 175
        self.assertTrue(TestLexer.test(input,expect,num))
    
    