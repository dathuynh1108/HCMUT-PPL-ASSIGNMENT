import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Class_type {}
            Class Program {
                Var $a: Array[Int, 5];
                main() {
                    Val a: Array[Float, 3] = Array(1,2,3);
                    a = Array(1,2,3);
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 999))

