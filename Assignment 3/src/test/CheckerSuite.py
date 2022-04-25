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
                    Var a: Array[Int, 1] = 1;
                    a = Array(1, 2);
                }
                
            }
            

        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 999))

