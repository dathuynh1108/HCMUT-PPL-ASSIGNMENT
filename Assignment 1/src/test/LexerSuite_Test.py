import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_temp(self): 
      input = "\"String with single quote \'this is good\'\""
      expect = "Illegal Escape In String: ABC: \ "
      self.assertTrue(TestLexer.test(input, expect, 999))