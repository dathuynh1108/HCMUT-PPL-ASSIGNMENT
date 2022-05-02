import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class D {}
            Class E : D {}
            Class Program {
                main() {
                    Val e: D = New D();
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 999))

