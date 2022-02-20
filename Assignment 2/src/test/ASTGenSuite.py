import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_con_cac(self):
        input = """
            Class Program : Object {
                method() {
                    If (1 == 1) {}
                    Elseif (2 == 2) {}
                    Elseif (3 == 3) {}
                    Else {}
                }
            }
        """
        expect = ""
        num = 999
        self.assertTrue(TestAST.test(input, expect, num))
