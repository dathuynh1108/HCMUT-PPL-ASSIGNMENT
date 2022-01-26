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
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_002_id(self):
        input = "aBcDeF"
        expect = "aBcDeF,<EOF>"
        num = 102
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_003_id(self):
        input = "aBcDeF123_abcd;_123aBc; xyz abc 123abc"
        expect = "aBcDeF123_abcd,;,_123aBc,;,xyz,abc,123,abc,<EOF>"
        num = 103
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_004_id(self):
        input = "id1 id&&1 id||1 -id1 _ __ _id1 _id_1 1_id"
        expect = "id1,id,&&,1,id,||,1,-,id1,_,__,_id1,_id_1,1,_id,<EOF>"
        num = 104
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_005_id(self):
        input = """
            normal_Variable_123 
            $static_Variable_123 
            $_ 
            $123_Static_start_with_digit
            $123
            $
        """
        expect = "normal_Variable_123,$static_Variable_123,$_,$123_Static_start_with_digit,$123,Error Token $"
        num = 105
        self.assertTrue(TestLexer.test(input, expect, num))

    # test comment
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
        self.assertTrue(TestLexer.test(input, expect, num))

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
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_008_comment(self):
        input = """
            ## This comment ok ##
            ## 
            # Line 1
            # Line 2
            Line 3
            ##
            ###"""
        expect = "Error Token #"
        num = 108
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_009_comment(self):
        # Reference on """ of python, it is not Valid for nested """
        input = """
            ## Not support comment in comment ##
            #### Comment in comment ####
            ## #Unterminated Comment
        """
        expect = "Comment,in,comment,Error Token #"
        num = 109
        self.assertTrue(TestLexer.test(input, expect, num))

    # test integers
    def test_010_integer(self):

        input = "1234, 123 ; 123 456 0123 0x1234FFFF 0X1234AAAA"
        expect = "1234,,,123,;,123,456,0123,0x1234FFFF,0X1234AAAA,<EOF>"
        num = 110
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_011_integer(self):

        input = "12345 12_3_45 0x0_0_1_2_3 012_345 0b00_111_00_11"
        expect = "12345,12345,0x0,_0_1_2_3,012345,0b0,0,_111_00_11,<EOF>"
        num = 111
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_012_integer(self):
        # _INT is Variable
        input = "1_2_3_4_5 1_2 _1 1_"
        expect = "12345,12,_1,1,_,<EOF>"
        num = 112
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_013_integer(self):
        # _INT is Variable
        # Note question 0_x123: 0_ x123 or 0 _x123 --> can _ is the last char in INT
        input = "012345 0_12345 01_2345 0x12345 0x_12345 0_x12345 0b010101 0b_010101 0_b010101"
        expect = "012345,0,_12345,012345,0x12345,0,x_12345,0,_x12345,0b0,10101,0,b_010101,0,_b010101,<EOF>"
        num = 113
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_014_integer(self):
        # _INT is Variable
        input = "0xFFFF 0XFFFF 0xffff 0XFFFF 0XZZZZ 0xzzzz 0B1111 0b1111 0B2222 0b2222 09999 0 0xFFFF 0XF_F_F_F 0xf_f_f_f 0XF_F_F_F 0XZZZZ 0xzzzz 0B1_1_1_1 0b1_1_1_1 0B2222 0b2222 09999 0"
        expect = "0xFFFF,0XFFFF,0,xffff,0XFFFF,0,XZZZZ,0,xzzzz,0B1111,0b1111,0,B2222,0,b2222,0,9999,0,0xFFFF,0XFFFF,0,xf_f_f_f,0XFFFF,0,XZZZZ,0,xzzzz,0B1111,0b1111,0,B2222,0,b2222,0,9999,0,<EOF>"
        num = 114
        self.assertTrue(TestLexer.test(input, expect, num))

    # test string
    def test_015_string(self):
        input = r"""
            "Test escape sequence\b\f\r\n\t\'\\'""    
            ""     
        """
        expect = r"""Test escape sequence\b\f\r\n\t\'\\'",,<EOF>"""
        num = 115
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_016_string(self):
        input = r"""
            "String" "string" "string     " "string\nstring"
        """
        expect = r"""String,string,string     ,string\nstring,<EOF>"""
        num = 116
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_017_string(self):
        input = r"""
            "" "__STRING__STRING" "'"String in string'"" "String'"String in string'"String in string in string'"String in String'"String"
        """
        expect = r""",__STRING__STRING,'"String in string'",String'"String in string'"String in string in string'"String in String'"String,<EOF>"""
        num = 117
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_018_string(self):
        input = r"""
            This is not string
            "This is string\n\r\\"
            "ILLEGAL_ESCAPE\z"
        """
        expect = r"""This,is,not,string,This is string\n\r\\,Illegal Escape In String: ILLEGAL_ESCAPE\z"""
        num = 118
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_019_string(self):
        input = r"""
            "OK\'"
            "OK'""
            "ILLEGAL_ESCAPE\""
        """
        expect = r"""OK\',OK'",Illegal Escape In String: ILLEGAL_ESCAPE\""""
        num = 119
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_020_string(self):
        input = r"""
            "abc"
            "abc\'"
            "abc'"
            "Hello \' there"
            "Huynh Thanh Dat\"
        """
        expect = (
            r"abc,abc\',abc',Hello \' there,Illegal Escape In String: Huynh Thanh Dat\""
        )
        num = 120
        self.assertTrue(TestLexer.test(input, expect, num))

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
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_022_string(self):
        input = r"""
            "Int" "Float"
            "a'"b'"c"
            "!@#$%^&*()_-+=[]{}|/?><"
        """
        expect = r"""Int,Float,a'"b'"c,!@#$%^&*()_-+=[]{}|/?><,<EOF>"""
        num = 122
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_023_string(self):
        input = r"""
            "Huynh Thanh Dat \t 1910110 \n 11 08 2001"
            "abc\""
        """
        expect = r"""Huynh Thanh Dat \t 1910110 \n 11 08 2001,Illegal Escape In String: abc\""""
        num = 123
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_024_string(self):
        input = r"""
            "a\bb\fc\rd\ne\tf\\"
            "a\'b"
            "a'b"
        """
        expect = r"""a\bb\fc\rd\ne\tf\\,a\'b,a'b,<EOF>"""
        num = 124
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_025_string(self):
        input = r"""
            "{string}" 
            "'"{string}'""
            "(string)"
            "[string]"
            "`string`"
            "" not_string ""
        """
        expect = (
            r"""{string},'"{string}'",(string),[string],`string`,,not_string,,<EOF>"""
        )
        num = 125
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_026_string(self):
        input = r"""
            "Unclose string
        """
        expect = r"""Unclosed String: Unclose string"""
        num = 126
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_027_string(self):
        input = r"""
            "Unclose string with escape sequence\n\t\r\f\b
        """
        expect = r"""Unclosed String: Unclose string with escape sequence\n\t\r\f\b"""
        num = 127
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_028_string(self):
        input = r"""
            "String end with double quote'""
            "Unclose string end with double quote'"
            "String'"
            "String'" 
        """
        expect = """String end with double quote'",Unclose string end with double quote',String',Unclosed String: String'" """
        num = 128
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_029_string(self):
        input = r"""
            String s = "string"
            String s2 = "string"
            String s3 = "unclose string
            next_line
        """
        expect = r"""String,s,=,string,String,s2,=,string,String,s3,=,Unclosed String: unclose string"""
        num = 129
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_030_string(self):
        input = r"""
            "\\a"
            "String"
            " "
            "?" "-" "#" "!" "@" "#" "$" "%" "^" "&" "*" "(" ")" "-" "_" "+" ";" ":" ";" "<" ">" "?"
            "Mulitiple Characters with expression: (1+2*3)*(3-1)"
        """
        expect = r"""\\a,String, ,?,-,#,!,@,#,$,%,^,&,*,(,),-,_,+,;,:,;,<,>,?,Mulitiple Characters with expression: (1+2*3)*(3-1),<EOF>"""
        num = 130
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_031_string(self):
        input = r"""
            "Valid string"
            'Invalid string'
        """
        expect = r"""Valid string,Error Token '"""
        num = 131
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_032_string(self):
        input = r"""
            "Valid string"
            "'"Valid string'" Cristiano Ronaldo"
            "String end with double quote'"
            "String end with double quote and space '" 
        """
        expect = """Valid string,'"Valid string'" Cristiano Ronaldo,String end with double quote',Unclosed String: String end with double quote and space '" """
        num = 132
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_033_string(self):
        input = r"""
            "Valid string"
            "Huynh Thanh Dat \'\t\n\f\b\r\f\\'" 11082001"
            "String''
        """
        expect = r"""Valid string,Huynh Thanh Dat \'\t\n\f\b\r\f\\'" 11082001,Unclosed String: String''"""
        num = 133
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_034_string(self):
        input = r"""
            "String with expression: 1+1*1/1%1*(1+1)"
            Expression: 1+1*1/1%1*(1+1)
        """
        expect = r"""String with expression: 1+1*1/1%1*(1+1),Expression,:,1,+,1,*,1,/,1,%,1,*,(,1,+,1,),<EOF>"""
        num = 134
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_035_string(self):
        input = r"""
            ## Test Comment ##
            "String with expression: 1+1*1/1%1*(1+1)"
            "Class Program : Object {Var $x: Int = 1;Method(n:Int){Return n;}}"
            ##"String with expression: 1+1*1/1%1*(1+1)"##
            ## Test Comment ##
        """
        expect = r"""String with expression: 1+1*1/1%1*(1+1),Class Program : Object {Var $x: Int = 1;Method(n:Int){Return n;}},<EOF>"""
        num = 135
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_036_string(self):
        input = r"""
            "String"
            "'" String in string '""
            "String'"String in string '"String in string in string'"'""
            ##"String in comment"##
            "## Comment in string ##"
            "{braces in string}"
            {"string in braces"}
            "[square brackets in string]"
            ["string in square brackets"]
            "(parentheses in string)"
            ("string in parentheses")
            "/* C comment in string */"
            /* "string in C comment" */
            "<<abc>>"
            <<"abc">>
        """
        expect = r"""String,'" String in string '",String'"String in string '"String in string in string'"'",## Comment in string ##,{braces in string},{,string in braces,},[square brackets in string],[,string in square brackets,],(parentheses in string),(,string in parentheses,),/* C comment in string */,/,*,string in C comment,*,/,<<abc>>,<,<,abc,>,>,<EOF>"""
        num = 136
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_037_string(self):
        input = r"""
            ## test with syntax ##        
            Var $string_1: String = "this is a string";
            Var $string_2: String = "this is a string";
        """
        expect = r"""Var,$string_1,:,String,=,this is a string,;,Var,$string_2,:,String,=,this is a string,;,<EOF>"""
        num = 137
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_038_string(self):
        input = r"""
            Var $string_1: String = "abc"; ## Comment ##
            string_1 = string_1 +. "def" +. "xyz";
            Var $string_2: String = "abcdefxyz";
            "Some code in string"
            "Var i: Int; Foreach (i In 1 .. 100 By 1) {If (i==i) {Break;} Elseif(i==i+1) {Continue;} Else {Return;}}"
        """
        expect = r"""Var,$string_1,:,String,=,abc,;,string_1,=,string_1,+.,def,+.,xyz,;,Var,$string_2,:,String,=,abcdefxyz,;,Some code in string,Var i: Int; Foreach (i In 1 .. 100 By 1) {If (i==i) {Break;} Elseif(i==i+1) {Continue;} Else {Return;}},<EOF>"""
        num = 138
        self.assertTrue(TestLexer.test(input, expect, num))

    # Test boolean
    def test_039_boolean(self):
        input = r"""
            True TRUE False FALSE True_with_other_chars False_with_other_chars
        """
        expect = r"""True,TRUE,False,FALSE,True_with_other_chars,False_with_other_chars,<EOF>"""
        num = 139
        self.assertTrue(TestLexer.test(input, expect, num))

    # Test float
    def test_040_float(self):
        # 3 component
        input = r"""
            1.234 1.234e10 1.234e-10 1_234.567e10 1_234.567e-10 1_123.1_123e1_123 1.e1_123
        """
        expect = r"""1.234,1.234e10,1.234e-10,1234.567e10,1234.567e-10,1123.1,_123e1_123,1.e1,_123,<EOF>"""
        num = 140
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_041_float(self):
        # Miss Exponent
        input = r"""
            1.1234 00001.1234 1.  000001. 1.1234 1_123.1_123 1_1_2_3.1123 1_123.
        """
        expect = r"""1.1234,00,00,1.1234,1.,00,00,01,.,1.1234,1123.1,_123,1123.1123,1123.,<EOF>"""
        num = 141
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_042_float(self):
        # Miss Decimal
        input = r"""
            123e123 123E123 123e-123 123E-123 00123e00123 00123E00123
        """
        expect = (
            r"""123e123,123E123,123e-123,123E-123,00,123e00123,00,123E00123,<EOF>"""
        )
        num = 142
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_043_float(self):
        # Miss Decimal
        input = r"""
            1_123e1123 1_123E1123 1_123e1_123 1_____123e1_______123 1____123E1______123
        """
        expect = r"""1123e1123,1123E1123,1123e1,_123,1,_____123e1_______123,1,____123E1______123,<EOF>"""
        num = 143
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_044_float(self):
        # Miss Integer
        input = r"""
            .123 .1_123 .123e123 .123E123 .123e-123 .123e+123 .1_123e1_123 .1___123e1___123 .1_123E1_123 .1___123E1___123 .e123 .e1_123
        """
        expect = r""".,123,.,1123,.123e123,.123E123,.123e-123,.123e+123,.,1123e1,_123,.,1,___123e1___123,.,1123E1,_123,.,1,___123E1___123,.e123,.e1,_123,<EOF>"""
        num = 144
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_045_float(self):
        input = r"""
            123 123. 9.9999 0.9999 0. .0 0.0e10 
        """
        expect = r"""123,123.,9.9999,0.9999,0.,.,0,0.0e10,<EOF>"""
        num = 145
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_046_float(self):
        input = r"""
            .123e1.123 .123e1.123e1
        """
        expect = r""".123e1,.,123,.123e1,.123e1,<EOF>"""
        num = 146
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_047_float(self):
        input = r"""
            0x123.123 0x123.123e10 abc.123 abc.123e10
        """
        expect = r"""0x123,.,123,0x123,.123e10,abc,.,123,abc,.123e10,<EOF>"""
        num = 147
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_048_float(self):
        input = r"""
            0x123.123 0x123.123e10 0b1111.111 0b11112.123
        """
        expect = r"""0x123,.,123,0x123,.123e10,0b1111,.,111,0b1111,2.123,<EOF>"""
        num = 148
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_049_float(self):
        input = r"""
            Var $float_1: Float = 1.123;
            Var $float_2: Float = 1.123e10;
        """
        expect = r"""Var,$float_1,:,Float,=,1.123,;,Var,$float_2,:,Float,=,1.123e10,;,<EOF>"""
        num = 149
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_050_float(self):
        input = r"""
            00000000000.000000000 1_2_3_4.1234e1234 1_2_3_4.1234e-1234 1_2_3_4.1_234e1_234
        """
        expect = r"""00,00,00,00,00,0.000000000,1234.1234e1234,1234.1234e-1234,1234.1,_234e1_234,<EOF>"""
        num = 150
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_051_float(self):
        input = r"""
            1e1 1e-1 1e+1 123.123e+123 123.123e-123
        """
        expect = r"""1e1,1e-1,1e+1,123.123e+123,123.123e-123,<EOF>"""
        num = 151
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_052_float(self):
        input = r"""
            1_2_3.123e123
            1_____2______3.123e123
            1_____2______3.1_____2_____3e+1____23
            1_____2______3.1_____2_____3e-1____23
            1___2__3.1____2____3
            1___2___3e1____2____3
            1___2___3e+1____2____3
            1___2___3e-1____2____3
        """
        expect = r"""123.123e123,1,_____2______3,.123e123,1,_____2______3,.,1,_____2_____3e,+,1,____23,1,_____2______3,.,1,_____2_____3e,-,1,____23,1,___2__3,.,1,____2____3,1,___2___3e1____2____3,1,___2___3e,+,1,____2____3,1,___2___3e,-,1,____2____3,<EOF>"""
        num = 152
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_053_float(self):
        input = r"""
            123e+123 + 123e+123 - 123e-123
        """
        expect = r"""123e+123,+,123e+123,-,123e-123,<EOF>"""
        num = 153
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_054_float(self):
        input = r"""
            +.123e1
            + .123e1
            ==.123e1
            == .123e1
        """
        expect = r"""+.,123e1,+,.123e1,==.,123e1,==,.123e1,<EOF>"""
        num = 154
        self.assertTrue(TestLexer.test(input, expect, num))

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
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_056_float(self):
        input = r"""
            Var $float_1: Float = 1_2_3_4.1234e1234;
            Var $float_2: Float = 123_123.1234e-1234;
            Var $float_3: Float = 1_2_3_4.1234;
            Var $float_4: Float = 1.e10000;
            Var $float_5: Float = 1e10000;
            Var $float_6: Float = 123.;
        """
        expect = r"""Var,$float_1,:,Float,=,1234.1234e1234,;,Var,$float_2,:,Float,=,123123.1234e-1234,;,Var,$float_3,:,Float,=,1234.1234,;,Var,$float_4,:,Float,=,1.e10000,;,Var,$float_5,:,Float,=,1e10000,;,Var,$float_6,:,Float,=,123.,;,<EOF>"""
        num = 156
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_057_float(self):
        input = r"""
            1.123
            .1123e1
            .1_123e1
            .123e123
            .1_123e1_123
            .e123
            .e1_123
            .e_1123
            abc.e1123
            "".e1123
            ''.e1123
        """
        expect = r"""1.123,.1123e1,.,1123e1,.123e123,.,1123e1,_123,.e123,.e1,_123,.,e_1123,abc,.e1123,,.e1123,Error Token '"""
        num = 157
        self.assertTrue(TestLexer.test(input, expect, num))

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
        self.assertTrue(TestLexer.test(input, expect, num))

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
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_060_operator(self):
        input = r"""
            + - * / % ! && || == = != < <= > >= ==. +.
        """
        expect = r"""+,-,*,/,%,!,&&,||,==,=,!=,<,<=,>,>=,==.,+.,<EOF>"""
        num = 160
        self.assertTrue(TestLexer.test(input, expect, num))

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
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_062_operator_float(self):
        input = r"""
            1e+1+1e+1
            1e-1-1e-1
            .e-1-.e-1
            .e+1+.e+1
        """
        expect = r"""1e+1,+,1e+1,1e-1,-,1e-1,.e-1,-,.e-1,.e+1,+.,e,+,1,<EOF>"""
        num = 162
        self.assertTrue(TestLexer.test(input, expect, num))

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
        self.assertTrue(TestLexer.test(input, expect, num))

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
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_065_seperator(self):
        input = r"""
            ()[]{}.,;:::
            @staticmethod
        """
        expect = r"""(,),[,],{,},.,,,;,::,:,Error Token @"""
        num = 165
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_066_seperator(self):
        input = r"""
            [](x,y) {
                Var a,b:Int;
                x[0] == a == y[0] == b;
                a.b + Self.b;
                Some_class::$a;
                Some_class::$method();
                
            }
        """
        expect = r"""[,],(,x,,,y,),{,Var,a,,,b,:,Int,;,x,[,0,],==,a,==,y,[,0,],==,b,;,a,.,b,+,Self,.,b,;,Some_class,::,$a,;,Some_class,::,$method,(,),;,},<EOF>"""
        num = 166
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_067_seperator(self):
        input = r"""
            class JSON {
                static int variable = 0;
                public:
                    unordered_map<type_1, type_2> data;
                    Pointer method(x) {
                        Return Null;
                    }
            };
            int main() {
                int a,b,c = 0;
                cin >> a >> b >> c;
                cout << "Huynh Thanh Dat";
                int a[100];
                {
                    a[1] = a[1] + a[2];
                    a[1] == a[3];
                }
                ++JSON::variable;
                JSON::method();
            }
        """
        expect = r"""class,JSON,{,static,int,variable,=,0,;,public,:,unordered_map,<,type_1,,,type_2,>,data,;,Pointer,method,(,x,),{,Return,Null,;,},},;,int,main,(,),{,int,a,,,b,,,c,=,0,;,cin,>,>,a,>,>,b,>,>,c,;,cout,<,<,Huynh Thanh Dat,;,int,a,[,100,],;,{,a,[,1,],=,a,[,1,],+,a,[,2,],;,a,[,1,],==,a,[,3,],;,},+,+,JSON,::,variable,;,JSON,::,method,(,),;,},<EOF>"""
        num = 167
        self.assertTrue(TestLexer.test(input, expect, num))

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
                    a::b
                    x=a==1?b:c;
                }
        """
        expect = r"""x,=,array,[,(,a,+,b,),-,c,*,d,],>=,1,>,0,<=,10,<,100,;,{,a,*,*,b,a,%,b,a,$b,a,::,b,x,=,a,==,1,Error Token ?"""
        num = 168
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_069_seperator(self):
        input = r"""
            ()=>{
                console.log("abc");
                a[1];
                Var a,b,c;
                *this.a;
                this->a;    
                int* a = new int;
                Class_name::a;
                Var a:Int;
            }
            
        """
        expect = r"""(,),=,>,{,console,.,log,(,abc,),;,a,[,1,],;,Var,a,,,b,,,c,;,*,this,.,a,;,this,-,>,a,;,int,*,a,=,new,int,;,Class_name,::,a,;,Var,a,:,Int,;,},<EOF>"""
        num = 169
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_070_type(self):
        input = r"""
            Int int Int_ 
            Float float Float_ 
            Boolean boolean Boolean_ 
            String string String_
            Array array Array_
            Class Class Class_
            Null null Null_
        """
        expect = r"""Int,int,Int_,Float,float,Float_,Boolean,boolean,Boolean_,String,string,String_,Array,array,Array_,Class,Class,Class_,Null,null,Null_,<EOF>"""
        num = 170
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_071_keyword(self):
        input = r"""
            Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New
        """
        expect = r"""Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,<EOF>"""
        num = 171
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_072_keyword(self):
        input = r"""
            Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New
            "Break" "Continue" "If" "Elseif" "Else" "Foreach" "True" "False" "Array" "In" "Int" "Float" "Boolean" "String" "Return" "Null" "Class" "Val" "Var" "Constructor" "Destructor" "New"
            "Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New"
            ## Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New ##
            (Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New)
        """
        expect = r"""Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New,(,Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,),<EOF>"""
        num = 172
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_073_keyword_complex(self):
        input = r"""
            ## Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New ##
            Constructor() {
                If (1==1) {
                    Var a: Array[Int,100];
                    Val b: Array[Int,100];
                    Foreach (i In 1..101 By 1)
                        If (a[i] == 1) Return Self.text;
                        Elseif (a[i] == 2) Continue;
                        Else (a[i] == 3) Break;
                }
            }
            Destructor() {
                Return;
            }
        """
        expect = r"""Constructor,(,),{,If,(,1,==,1,),{,Var,a,:,Array,[,Int,,,100,],;,Val,b,:,Array,[,Int,,,100,],;,Foreach,(,i,In,1.,.,101,By,1,),If,(,a,[,i,],==,1,),Return,Self,.,text,;,Elseif,(,a,[,i,],==,2,),Continue,;,Else,(,a,[,i,],==,3,),Break,;,},},Destructor,(,),{,Return,;,},<EOF>"""
        num = 173
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_074_integer(self):
        input = r"""
            1_234 1_2_3_4_5  1_234_
            0123 0_123 01_23 01_2_3 0123_
            0x123 0_x123 0x_123 0x1_23 0x1_2_3 0x123_
            0b111 0_b111 0b_111 0b1_11 0b1_1_1 0b111_
        """
        expect = r"""1234,12345,1234,_,0123,0,_123,0123,0123,0123,_,0x123,0,_x123,0,x_123,0x123,0x123,0x123,_,0b111,0,_b111,0,b_111,0b111,0b111,0b111,_,<EOF>"""
        num = 174
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_075_integer(self):
        input = r"""
            _1234
            1_234
            1234_

            0xABCDEF
            0XABCDEF
            0XaBcDeF
            0b111111
            0B111111
            0x0
            0X0
            0b0
            0B0

            0xZXCVBN
            0b222222
            09999999
        """
        expect = r"""_1234,1234,1234,_,0xABCDEF,0XABCDEF,0,XaBcDeF,0b111111,0B111111,0x0,0X0,0b0,0B0,0,xZXCVBN,0,b222222,0,9999999,<EOF>"""
        num = 175
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_076_general(self):
        input = r"""
            ## Multi line comment 
            # Line 1
            # Line 2
            # Line 3
            End comment ##
            Class Program : Object {
                Var x, $y: Int;
                $static_method(a: Int) {
                    If ($a > 1) {
                        Return $a;
                    } Elseif ($a < 1) {
                        Return $a + 1;
                    }
                }
            }
        """
        expect = r"""Class,Program,:,Object,{,Var,x,,,$y,:,Int,;,$static_method,(,a,:,Int,),{,If,(,$a,>,1,),{,Return,$a,;,},Elseif,(,$a,<,1,),{,Return,$a,+,1,;,},},},<EOF>"""
        num = 176
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_077_general(self):
        input = r"""
            ## Multi line comment 
            # Line 1
            # Line 2
            # Line 3
            End comment ##
            Class Program : Object {
                Var $string: String = "This is a string";
                print_console(n: Int) {
                    Var i: Int;
                    Foreach (i In 1 .. 100 By 1) {
                        print($string);
                    }
                }
            }
        """
        expect = r"""Class,Program,:,Object,{,Var,$string,:,String,=,This is a string,;,print_console,(,n,:,Int,),{,Var,i,:,Int,;,Foreach,(,i,In,1,..,100,By,1,),{,print,(,$string,),;,},},},<EOF>"""
        num = 177
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_078_range(self):
        input = r"""
            1..100      ## 1. is float ##
            1 .. 100
            a..b
            (1)..100
            1...100
            1...100.
        """
        expect = r"""1.,.,100,1,..,100,a,..,b,(,1,),..,100,1.,..,100,1.,..,100.,<EOF>"""
        num = 178
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_079_special_case(self):
        input = r"""
            ## Unclose or Illegal ??, need do print \n? ##
            "abcde\
            ""
        """
        expect = """Illegal Escape In String: abcde\\\n"""
        num = 179
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_080_special_case(self):
        input = r"""
            ## Unclose or Illegal ?? ##
            "abcde'"
        """
        expect = """abcde',<EOF>"""
        num = 180
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_081_special_case(self):
        input = r"""
            ## Illegal at \ or \" 
            # Most language take \" but it is an escape sequence
            ##

            "abcde\"
        """
        expect = """Illegal Escape In String: abcde\\\""""
        num = 181
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_082_float_seperator(self):
        input = r"""
            1_234.
            1234.
            .1234
            .1_234e1234
            .1e+1+1
            .1e-1-1
            *()*)%!++(+)&&||*();,[](){}%+-=====*/
            &
        """
        expect = """1234.,1234.,.,1234,.,1234e1234,.1e+1,+,1,.1e-1,-,1,*,(,),*,),%,!,+,+,(,+,),&&,||,*,(,),;,,,[,],(,),{,},%,+,-,==,==,=,*,/,Error Token &"""
        num = 182
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_083_seperator(self):
        input = r"""
            ++--**//%%||||&&&&
            ++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>. 
            {{{{{{(([[[[[[[[]]]]]]]])()()())()()()()}}}}}}
            ,,,,;;;...
            ======
            =====
            !===!==
            >===<=>=<===....+..
            :::::::::::::::::::
            ...................
        """
        expect = """+,+,-,-,*,*,/,/,%,%,||,||,&&,&&,+,+.,>,+.,+,+,+,+,+,+,+.,.,+,+,+.,>,+,+.,<,<,+,+,+,+,+,+,+,+,+,+,+,+,+,+,+.,>,.,+,+,+.,-,-,-,-,-,-,.,-,-,-,-,-,-,-,-,.,>,+.,>,.,{,{,{,{,{,{,(,(,[,[,[,[,[,[,[,[,],],],],],],],],),(,),(,),(,),),(,),(,),(,),(,),},},},},},},,,,,,,,,;,;,;,..,.,==,==,==,==,==,=,!=,==,!=,=,>=,==,<=,>=,<=,==.,..,.,+.,.,::,::,::,::,::,::,::,::,::,:,..,..,..,..,..,..,..,..,..,.,<EOF>"""
        num = 183
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_084_integer_decimal(self):
        input = r"""
            ## 
                =================================
                |                               |
                |         COMMENT HERE          |  
                |                               |
                =================================
            ##
            0 _0 0_ __0 0__ 
            123456 123_456 123_456 123456_ 123456_ _123456 _123456
            123456 123__456 123__456 123456__ 123456__ __123456 __123456
            -123456 -123_456 -123__456 -_123456 -_123456 -123456_ -123456_
            +123456 +123_456 +123_456 +_123456 +_123456 +123456_ +123456_
            123ffff
            1230xfff
            1230b111
            1230123
        """
        expect = """0,_0,0,_,__0,0,__,123456,123456,123456,123456,_,123456,_,_123456,_123456,123456,123,__456,123,__456,123456,__,123456,__,__123456,__123456,-,123456,-,123456,-,123,__456,-,_123456,-,_123456,-,123456,_,-,123456,_,+,123456,+,123456,+,123456,+,_123456,+,_123456,+,123456,_,+,123456,_,123,ffff,1230,xfff,1230,b111,1230123,<EOF>"""
        num = 184
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_085_integer_decimal(self):
        input = r"""
            +123456+123456 +123_456+123_456
            -123456-123456 -123_456-123_456
            123456*123456 123_456*123_456
            123456/123456 123_456/123_456
            123456%123456 123_456%123_456
            123456!=123456 123_456!=123_456
            123456==123456 123_456==123_456
            123456>123456 123_456>=123_456
            123456<123456 123_456<=123_456
            123456<123456 123_456<=123__456
        """
        expect = """+,123456,+,123456,+,123456,+,123456,-,123456,-,123456,-,123456,-,123456,123456,*,123456,123456,*,123456,123456,/,123456,123456,/,123456,123456,%,123456,123456,%,123456,123456,!=,123456,123456,!=,123456,123456,==,123456,123456,==,123456,123456,>,123456,123456,>=,123456,123456,<,123456,123456,<=,123456,123456,<,123456,123456,<=,123,__456,<EOF>"""
        num = 185
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_086_integer_oct(self):
        input = r"""
            00 01234 01_234 01___234 _01234 01234_
            07777
            08888
            0ffff
            00xffff
            00b1111
        """
        expect = """00,01234,01,_234,01,___234,_01234,01234,_,07777,0,8888,0,ffff,00,xffff,00,b1111,<EOF>"""
        num = 186
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_086_integer_oct(self):
        input = r"""
            -01234-01234
            +01234+01234
            01234*01234
            01234/01234
            01234%01234
            01234!=01234
            01234==01234
            01234>01234
            01234>=01234
            01234<01234
            01234<=01234
        """
        expect = """-,01234,-,01234,+,01234,+,01234,01234,*,01234,01234,/,01234,01234,%,01234,01234,!=,01234,01234,==,01234,01234,>,01234,01234,>=,01234,01234,<,01234,01234,<=,01234,<EOF>"""
        num = 186
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_087_integer_bin(self):
        input = r"""
            0b00000 0b11111 0b01010101
            -0b00000 -0b11111 -0b01010101
            +0b00000 +0b11111 +0b01010101
            0B00000 0B11111 -0B1010101
            0b
            0B
            0b123456789
            0b011111111
            0b_11111111 0b1_1_1_1_1_1_1_1 0b_11111111_ 
            0b111111112
            0b111111110000002
            0b0xFFFF
            0b11110xFFFF
            0b101020xFFF 
            12340b11111
            12340b11112
            0xFFFF0b1111
            0xffff0b1111
            0xFFFF0ABCDEF
            0xffff0ABCDEF
        """
        expect = """0b0,00,00,0b11111,0b0,1010101,-,0b0,00,00,-,0b11111,-,0b0,1010101,+,0b0,00,00,+,0b11111,+,0b0,1010101,0B0,00,00,0B11111,-,0B1010101,0,b,0,B,0b1,23456789,0b0,11111111,0,b_11111111,0b11111111,0,b_11111111_,0b11111111,2,0b11111111000000,2,0b0,xFFFF,0b11110,xFFFF,0b1010,20,xFFF,12340,b11111,12340,b11112,0xFFFF0,b1111,0,xffff0b1111,0xFFFF0ABCDEF,0,xffff0ABCDEF,<EOF>"""
        num = 187
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_088_integer_bin(self):
        input = r"""
            +0b10101010+0b10101010
            -0b10101010-0b10101010
            +0b10101010*0b10101010
            -0b10101010/0b10101010
            +0b10101010%0b10101010
            -0b10101010!=0b10101010
            +0b10101010==0b10101010
            -0b10101010>0b10101010
            +0b10101010>=0b10101010
            -0b10101010<0b10101010
            +0b10101010<=0b10101010
        """
        expect = """+,0b10101010,+,0b10101010,-,0b10101010,-,0b10101010,+,0b10101010,*,0b10101010,-,0b10101010,/,0b10101010,+,0b10101010,%,0b10101010,-,0b10101010,!=,0b10101010,+,0b10101010,==,0b10101010,-,0b10101010,>,0b10101010,+,0b10101010,>=,0b10101010,-,0b10101010,<,0b10101010,+,0b10101010,<=,0b10101010,<EOF>"""
        num = 188
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_089_integer_hex(self):
        input = r"""
            0x00000
            0x123456789abcdef -0x123456789abcdef +0x123456789abcdef
            0X123456789ABCDEF -0X123456789ABCDEF +0X123456789ABCDEF
            0x123456789ABCDEF -0x123456789ABCDEF +0x123456789ABCDEF
            0X123456789aBcDeF -0X123456789aBcDeF +0X123456789aBcDeF
            0x9999FFFFF
            0x_9999FFFFF 0x9_9_9_9_F_F_F_F_F 0x9999FFFFF_ 
            0x09999FFFF
            0x0b1111111
            0x0B1111111
            0x0b2222222
            0x0B2222222
            0x11110b111
            0x11110B111
            0x11110b222
            0x11110B222
            0x
            0X
            0b0xFFFF
            0b0x0000   
            0b10100xFFFF
            0b101020xFFFF         
        """
        expect = """0x0,00,00,0x123456789,abcdef,-,0x123456789,abcdef,+,0x123456789,abcdef,0X123456789ABCDEF,-,0X123456789ABCDEF,+,0X123456789ABCDEF,0x123456789ABCDEF,-,0x123456789ABCDEF,+,0x123456789ABCDEF,0X123456789,aBcDeF,-,0X123456789,aBcDeF,+,0X123456789,aBcDeF,0x9999FFFFF,0,x_9999FFFFF,0x9999FFFFF,0x9999FFFFF,_,0x0,9999,FFFF,0x0,b1111111,0x0,B1111111,0x0,b2222222,0x0,B2222222,0x11110,b111,0x11110B111,0x11110,b222,0x11110B222,0,x,0,X,0b0,xFFFF,0b0,x0000,0b10100,xFFFF,0b1010,20,xFFFF,<EOF>"""
        num = 189
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_090_integer_hex(self):
        input = r"""
            +0X123456789ABCDEF+0X123456789ABCDEF
            -0X123456789ABCDEF-0X123456789ABCDEF
            +0X123456789ABCDEF*0X123456789ABCDEF
            -0X123456789ABCDEF/0X123456789ABCDEF
            +0X123456789ABCDEF%0X123456789ABCDEF
            -0X123456789ABCDEF!=0X123456789ABCDEF
            +0X123456789ABCDEF==0X123456789ABCDEF
            -0X123456789ABCDEF>0X123456789ABCDEF
            +0X123456789ABCDEF>=0X123456789ABCDEF
            -0X123456789ABCDEF<0X123456789ABCDEF
            +0X123456789ABCDEF<=0X123456789ABCDEF
            
            0X123456789ABCDEF+123456789  
            0X123456789ABCDEF+123_456_789
            0X123456789ABCDEF+123__456__789   
            0X123456789ABCDEF+0123456789ABCDEF 
            0X123456789ABCDEF+0B1111111  

            +0x123456789ABCDEF+0x123456789ABCDEF
            -0x123456789ABCDEF-0x123456789ABCDEF
            +0x123456789ABCDEF*0x123456789ABCDEF
            -0x123456789ABCDEF/0x123456789ABCDEF
            +0x123456789ABCDEF%0x123456789ABCDEF
            -0x123456789ABCDEF!=0x123456789ABCDEF
            +0x123456789ABCDEF==0x123456789ABCDEF
            -0x123456789ABCDEF>0x123456789ABCDEF
            +0x123456789ABCDEF>=0x123456789ABCDEF
            -0x123456789ABCDEF<0x123456789ABCDEF
            +0x123456789ABCDEF<=0x123456789ABCDEF
            
            0x123456789ABCDEF+123456789  
            0x123456789ABCDEF+123_456_789
            0x123456789ABCDEF+123__456__789   
            0x123456789ABCDEF+0123456789ABCDEF 
            0x123456789ABCDEF+0B1111111  



            +0x123456789abcdef+0x123456789abcdef
            -0x123456789abcdef-0x123456789abcdef
            +0x123456789abcdef*0x123456789abcdef
            -0x123456789abcdef/0x123456789abcdef
            +0x123456789abcdef%0x123456789abcdef
            -0x123456789abcdef!=0x123456789abcdef
            +0x123456789abcdef==0x123456789abcdef
            -0x123456789abcdef>0x123456789abcdef
            +0x123456789abcdef>=0x123456789abcdef
            -0x123456789abcdef<0x123456789abcdef
            +0x123456789abcdef<=0x123456789abcdef
            
            0x123456789abcdef+123456789  
            0x123456789abcdef+123_456_789
            0x123456789abcdef+123__456__789   
            0x123456789abcdef+0123456789abcdef 
            0x123456789abcdef+0b1111111              
        """
        expect = """+,0X123456789ABCDEF,+,0X123456789ABCDEF,-,0X123456789ABCDEF,-,0X123456789ABCDEF,+,0X123456789ABCDEF,*,0X123456789ABCDEF,-,0X123456789ABCDEF,/,0X123456789ABCDEF,+,0X123456789ABCDEF,%,0X123456789ABCDEF,-,0X123456789ABCDEF,!=,0X123456789ABCDEF,+,0X123456789ABCDEF,==,0X123456789ABCDEF,-,0X123456789ABCDEF,>,0X123456789ABCDEF,+,0X123456789ABCDEF,>=,0X123456789ABCDEF,-,0X123456789ABCDEF,<,0X123456789ABCDEF,+,0X123456789ABCDEF,<=,0X123456789ABCDEF,0X123456789ABCDEF,+,123456789,0X123456789ABCDEF,+,123456789,0X123456789ABCDEF,+,123,__456__789,0X123456789ABCDEF,+,01234567,89,ABCDEF,0X123456789ABCDEF,+,0B1111111,+,0x123456789ABCDEF,+,0x123456789ABCDEF,-,0x123456789ABCDEF,-,0x123456789ABCDEF,+,0x123456789ABCDEF,*,0x123456789ABCDEF,-,0x123456789ABCDEF,/,0x123456789ABCDEF,+,0x123456789ABCDEF,%,0x123456789ABCDEF,-,0x123456789ABCDEF,!=,0x123456789ABCDEF,+,0x123456789ABCDEF,==,0x123456789ABCDEF,-,0x123456789ABCDEF,>,0x123456789ABCDEF,+,0x123456789ABCDEF,>=,0x123456789ABCDEF,-,0x123456789ABCDEF,<,0x123456789ABCDEF,+,0x123456789ABCDEF,<=,0x123456789ABCDEF,0x123456789ABCDEF,+,123456789,0x123456789ABCDEF,+,123456789,0x123456789ABCDEF,+,123,__456__789,0x123456789ABCDEF,+,01234567,89,ABCDEF,0x123456789ABCDEF,+,0B1111111,+,0x123456789,abcdef,+,0x123456789,abcdef,-,0x123456789,abcdef,-,0x123456789,abcdef,+,0x123456789,abcdef,*,0x123456789,abcdef,-,0x123456789,abcdef,/,0x123456789,abcdef,+,0x123456789,abcdef,%,0x123456789,abcdef,-,0x123456789,abcdef,!=,0x123456789,abcdef,+,0x123456789,abcdef,==,0x123456789,abcdef,-,0x123456789,abcdef,>,0x123456789,abcdef,+,0x123456789,abcdef,>=,0x123456789,abcdef,-,0x123456789,abcdef,<,0x123456789,abcdef,+,0x123456789,abcdef,<=,0x123456789,abcdef,0x123456789,abcdef,+,123456789,0x123456789,abcdef,+,123456789,0x123456789,abcdef,+,123,__456__789,0x123456789,abcdef,+,01234567,89,abcdef,0x123456789,abcdef,+,0b1111111,<EOF>"""
        num = 190
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_091_complex(self):
        input = r"""
            Class Shape {
                Var color: String;
                area() {};
                to_string() {};
                Constructor(color: String)
                {
                    Console.log("Shape constructor called");
                    Self.color = color;
                }
                Destructor() {
                    Console.log("Destroy shape");
                }
                get_color() { return color; }
            }
            Class Circle : Shape {
                Var radius: Float;
                Constructor(color: String, radius: Float)
                {
                    Shape::constructor(color);
                    Console.log("Circle constructor called");
                    Self.radius = radius;
                }
  
                area()
                {
                    Return Math.PI * Math.pow(radius, 2);
                }
  
                to_string()
                {
                    Return "Circle color is " + Shape::getColor() +. "and area is : " + area();
                }
            }
            Class Program {
            main(args: Array[String, 100])
            {
                Var circle: Circle;
                Var string: String;
                circle = New Circle("Red", 2.2);
                string = circle.to_string();
                console.log(circle.get_color());
                Var i: Int;
                Foreach(i In 1 .. 100 by 1) {
                    Var circle: Circle;
                    If (i % 3 == 0) {
                        circle = New Circle("Blue", 10.10);
                        console.log(circle.area());
                    }
                    Elseif (i % 3 == 1) {
                        Break;
                    }
                    Else {
                        Continue;
                    }
                }
                i= +123456+123456 
                i= +123_456+123_456;
                i= -123456-123456 
                i= -123_456-123_456;
                i= 123456*123456 
                i= 123_456*123_456;
                i= 123456/123456 
                i= 123_456/123_456;
                i= 123456%123456 
                i= 123_456%123_456;
                i= 123456!=123456 
                i= 123_456!=123_456;
                i= 123456==123456 
                i= 123_456==123_456;
                i= 123456>123456 
                i= 123_456>=123_456;
                i= 123456<123456 
                i= 123_456<=123_456;
            }
        }            
        """
        expect = """Class,Shape,{,Var,color,:,String,;,area,(,),{,},;,to_string,(,),{,},;,Constructor,(,color,:,String,),{,Console,.,log,(,Shape constructor called,),;,Self,.,color,=,color,;,},Destructor,(,),{,Console,.,log,(,Destroy shape,),;,},get_color,(,),{,return,color,;,},},Class,Circle,:,Shape,{,Var,radius,:,Float,;,Constructor,(,color,:,String,,,radius,:,Float,),{,Shape,::,constructor,(,color,),;,Console,.,log,(,Circle constructor called,),;,Self,.,radius,=,radius,;,},area,(,),{,Return,Math,.,PI,*,Math,.,pow,(,radius,,,2,),;,},to_string,(,),{,Return,Circle color is ,+,Shape,::,getColor,(,),+.,and area is : ,+,area,(,),;,},},Class,Program,{,main,(,args,:,Array,[,String,,,100,],),{,Var,circle,:,Circle,;,Var,string,:,String,;,circle,=,New,Circle,(,Red,,,2.2,),;,string,=,circle,.,to_string,(,),;,console,.,log,(,circle,.,get_color,(,),),;,Var,i,:,Int,;,Foreach,(,i,In,1,..,100,by,1,),{,Var,circle,:,Circle,;,If,(,i,%,3,==,0,),{,circle,=,New,Circle,(,Blue,,,10.10,),;,console,.,log,(,circle,.,area,(,),),;,},Elseif,(,i,%,3,==,1,),{,Break,;,},Else,{,Continue,;,},},i,=,+,123456,+,123456,i,=,+,123456,+,123456,;,i,=,-,123456,-,123456,i,=,-,123456,-,123456,;,i,=,123456,*,123456,i,=,123456,*,123456,;,i,=,123456,/,123456,i,=,123456,/,123456,;,i,=,123456,%,123456,i,=,123456,%,123456,;,i,=,123456,!=,123456,i,=,123456,!=,123456,;,i,=,123456,==,123456,i,=,123456,==,123456,;,i,=,123456,>,123456,i,=,123456,>=,123456,;,i,=,123456,<,123456,i,=,123456,<=,123456,;,},},<EOF>"""
        num = 191
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_092_string(self):
        input = (
            """ "This is a complex string with '"quote'" and has comment ##abcd##" """
        )
        expect = (
            """This is a complex string with '"quote'" and has comment ##abcd##,<EOF>"""
        )
        num = 192
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_093_float_int(self):
        input = r"""
            123 310_596_32424 34234_3243243 3_4_5_5546_565465_1407_43423
            123 310__596__32424 34234__3243243 3__4__5__5546__565465__1407__43423
            0b111101 0B000000000011111111 0b111111111111111110000000000000000
            0123 002344 0003432434234 00000000000000003123123213 02313123200000000000000
            0x0000000000000000001ABCDF 0XABCDEF99999999999900000000000
            0x0000000000000000001abcdf 0Xabcdef99999999999900000000000
            123_
            1_2_3_4_5.012345e-012345
            0_1_2_3_4_5.012345e-012345
            0_1_2_3_4_5.012345e-0_1_2_3_4_5
            0_1_2_3_4_5.0_1_2_3_4_5e-012345
            0_1_2_3_4_5.0_1_2_3_4_5e-0_1_2_3_4_5
            0_1_2_3_4_5.012345e-012345_
            0_1_2_3_4_5.0_1_2_3_4_5e-0_1_2_3_4_5_
            0x123_456
            0b1111_1111
            01_234
        """
        expect = "123,31059632424,342343243243,3455546565465140743423,123,310,__596__32424,34234,__3243243,3,__4__5__5546__565465__1407__43423,0b111101,0B0,00,00,00,00,011111111,0b111111111111111110000000000000000,0123,00,2344,00,03432434234,00,00,00,00,00,00,00,00,3123123213,02313123200000000000000,0x0,00,00,00,00,00,00,00,00,01,ABCDF,0XABCDEF99999999999900000000000,0x0,00,00,00,00,00,00,00,00,01,abcdf,0,Xabcdef99999999999900000000000,123,_,12345.012345e-012345,0,_1_2_3_4_5,.012345e-012345,0,_1_2_3_4_5,.012345e-0,_1_2_3_4_5,0,_1_2_3_4_5,.,0,_1_2_3_4_5e,-,012345,0,_1_2_3_4_5,.,0,_1_2_3_4_5e,-,0,_1_2_3_4_5,0,_1_2_3_4_5,.012345e-012345,_,0,_1_2_3_4_5,.,0,_1_2_3_4_5e,-,0,_1_2_3_4_5_,0x123456,0b11111111,01234,<EOF>"
        num = 193
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_094_string_escape_sequence(self):
        input = r"""
            "First string is valid"
            "Second string is valid' "
            "Third string is valid '" "
            "This string is an unclosed string'" 
        """
        expect = r"""First string is valid,Second string is valid' ,Third string is valid '" ,Unclosed String: This string is an unclosed string'" """
        num = 194
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_095_string_illegal_escape(self):
        input = r""" "abcd\" """
        expect = r"""Illegal Escape In String: abcd\""""
        num = 195
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_096_string_illegal_escape(self):
        input = """"String \\"""
        expect = """Illegal Escape In String: String \\"""
        num = 196
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_097_array(self):
        input = r"""
            Array (1,2,3,4,5)
            Array ("string", "string", "string")
            Array (True, False, True)
            Array (
                Array("Volvo", "22", "18"),
                Array("Saab", "5", "2"),
                Array("Land Rover", "17", "15")
                Array("Huynh Thanh Dat", "11/08/2001", "1910110")
                Array("")
            )
            
        """
        num = 197
        expect = "Array,(,1,,,2,,,3,,,4,,,5,),Array,(,string,,,string,,,string,),Array,(,True,,,False,,,True,),Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),Array,(,Huynh Thanh Dat,,,11/08/2001,,,1910110,),Array,(,,),),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_098_comment_dangerous_case(self):
        # Case forget one # before EOF
        input = r"""
            ## This comment is true
                # Line 1
                # Line 2
                # Line 3
                # Array (
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
                    Array("Huynh Thanh Dat", "11/08/2001", "1910110")
                    Array("")
                )
                # Some code:
                Var circle: Circle;
                Var string: String;
                circle = New Circle("Red", 2.2);
                string = circle.to_string();
                console.log(circle.get_color());
                Var i: Int;
                # Some keyword
                Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Constructor Destructor New
            ##
            ####
        ###"""
        num = 198
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_099_float_special(self):
        # Case forget one # before EOF
        input = r"""
            1.234
            01.234
            001.234

            1.0123
            1.00123

            1.
            1.0

            1e123
            1e0123
            1e00123
            1e+123
            1e+0123
            1e+00123
            1e-123
            1e-0123
            1e-00123

            1_123.123e123
            1_1_2_3.123e123
            1_1_2_3.1_2_3e123
            1_1_2_3_1_2_3e1_2_3
            1_1_2_3_1_2_3_e1_2_3

            1_2_3.123e123
            1_2_3.000123e000123
            0_1_2_3.123e123
            0b111.123e123
            0xFFF.123e123
        """
        num = 199
        expect = "1.234,01,.,234,00,1.234,1.0123,1.00123,1.,1.0,1e123,1e0123,1e00123,1e+123,1e+0123,1e+00123,1e-123,1e-0123,1e-00123,1123.123e123,1123.123e123,1123.1,_2_3e123,1123123e1,_2_3,1123123,_e1_2_3,123.123e123,123.000123e000123,0,_1_2_3,.123e123,0b111,.123e123,0xFFF,.123e123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, num))

    def test_100_integer_start_with_zero_and_something_else(self):
        input = r"""
            12345
            01234
            001234
            00012345
            000012345

            01234
            001234

            0b111111
            0b011111
            0b001111
            0b000111

            0xFFFFFF
            0x0FFFFF
            0x00FFFF
            0x000FFF

            1_2_3_4_5
            _1_2_3_4_5
            1_2_3_4_5_

            0_1_2_3_4
            01_2_3_4
            _0_1_2_3_4
            0_1_2_3_4_

            0_0_1_2_3_4
            0_01234
            001_2_3_4

            0b_1_1_1_1
            0b1_1_1_1
            _0b1_1_1_1
            0b1_1_1_1_

            0b_0_1_1_1
            0b0_1_1_1
            0b01_1_1

            0x_FFFFF
            0xF_F_F_F
            _0xF_F_F_F
            0xF_F_F_F_

            0x_0_F_F_F
            0x0_F_F_F
            0x0F_F_F

            0xfffff
            0xFFFFF
            0Xfffff
            0xFFFFF
        """
        num = 200
        expect = r"12345,01234,00,1234,00,012345,00,00,12345,01234,00,1234,0b111111,0b0,11111,0b0,01111,0b0,00,111,0xFFFFFF,0x0,FFFFF,0x0,0,FFFF,0x0,00,FFF,12345,_1_2_3_4_5,12345,_,0,_1_2_3_4,01234,_0_1_2_3_4,0,_1_2_3_4_,0,_0_1_2_3_4,0,_01234,00,1234,0,b_1_1_1_1,0b1111,_0b1_1_1_1,0b1111,_,0,b_0_1_1_1,0b0,_1_1_1,0b0,111,0,x_FFFFF,0xFFFF,_0xF_F_F_F,0xFFFF,_,0,x_0_F_F_F,0x0,_F_F_F,0x0,F_F_F,0,xfffff,0xFFFFF,0,Xfffff,0xFFFFF,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, num))
