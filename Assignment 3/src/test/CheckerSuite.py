import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Object {
                Var x: Int = 1;
                method(a: Int) {
                    Var x: Int = 1;
                    {
                        Var x: Int = 1;
                        {Var x: Int = 2;}
                    }
                }
                Var a: Int = method;
            }
            

        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 999))

