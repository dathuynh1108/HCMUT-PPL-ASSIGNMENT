import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Object {
                Var x: Array[Array[Int, 1], 1] = 1;
                Val y: Int = x[0][1][0];
            }
            

        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 999))

