import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_con_cac(self):
        input = """
            Class  Object {
                Var a: Int;
                method() {}
            }
        """
        expect = ""
        num = 999
        self.assertTrue(TestAST.test(input, expect, num))
