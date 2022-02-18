import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_con_cac(self):
        input = """
            Class Program : Object {
                method() {
                    a.b(1,2,3);
                }
            }
        """
        expect = ""
        num = 999
        self.assertTrue(TestAST.test(input, expect, num))
