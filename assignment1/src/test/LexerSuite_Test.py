import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_temp(self): 
      input = """
                    Foreach(i in 1..10)
              """
      expect = "Illegal Escape In String: ABC: \ "
      self.assertTrue(TestLexer.test(input, expect, 999))