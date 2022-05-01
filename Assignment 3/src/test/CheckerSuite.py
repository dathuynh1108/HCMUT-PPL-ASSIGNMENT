import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a: String = "abc";
                    Var b: String = "abc";
                    Var c: Boolean = "abc" ==. "abc";
                    Var d: Boolean = a ==. "abc";
                    Var e: Boolean = a ==. b;

                    Var f: Boolean = a ==. 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 999))

