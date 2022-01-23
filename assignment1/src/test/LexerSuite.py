import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_temp(self): 
      input = """"string\\"""
      expect = "Illegal Escape In String: ABC: \ "
      self.assertTrue(TestLexer.test(input, expect, 999))