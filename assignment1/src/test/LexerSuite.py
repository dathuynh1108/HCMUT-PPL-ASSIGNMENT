import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    ### Test method is sorted --> Remember to name it with alphabet order to show right order of Text Test Runner
    
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
            ## Comment line 1
            Comment line 2 ##
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
            ## Comment is close ##
            ## 
            # Comment is closed
            ## 
            ##Comment is not closed
        """
        expect = "Unterminated Comment"
        num = 108
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_009_comment(self):
        # Reference on """ of python, it is not valid for nested """
        input = """
            #### Comment in comment ####
        """
        expect = "Comment,in,comment,<EOF>"
        num = 109
        self.assertTrue(TestLexer.test(input,expect,num))
    #test integers
    def test_010_simple_integer(self):

        input = "1234, 123 ; 123 456"
        expect = "1234,,,123,;,123,456,<EOF>"
        num = 110
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_011_simple_integer(self):
    
        input = "12345 12____3_45 0x0___0_1___2___3 012___3__45 0b00___111__00__11"
        expect = "12345,12345,0x00123,012345,0b001110011,<EOF>"
        num = 111
        self.assertTrue(TestLexer.test(input,expect,num))
    def test_015_string(self):
        input = r"""
            "Test escape sequence\b\f\r\n\t\'\\'""    
            ""     
        """
        expect = """Test escape sequence\\b\\f\\r\\n\\t\\'\\\\'",,<EOF>"""

        num = 115
        self.assertTrue(TestLexer.test(input,expect,num))
