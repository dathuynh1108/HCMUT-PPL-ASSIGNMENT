import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Object {
                Var a, b : Int = 1, 2;
            }
            Class A : Object {
                method() {
                    Var x, y : Int = Self.a, Self.b; ## OK ##
                    Var m, n : Int = m, n; 
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 999))

