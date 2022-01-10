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
        expect = "12345,12,______1,1,<EOF>"
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
    
    
