import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class E {
                Var a: Int;
                Var $b: Int;
                method() {}
            }
            Class Program {
                main() {
                    Var e: E = New E();
                    Var x: Int = E.a;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 999))

