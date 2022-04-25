import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                Var x: Int = a;
                method() {
                    Return 1;
                    Return 2.1;
                }
                
            }
            

        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 999))

