import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Program {
                Var a: Int = 1;
                Var x: Int = Self.a;
                Val y: Int = Self.a;
                Constructor() {}
                main() {
                    Var x: Int = Self.a;
                } 
            }
            

        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 999))

