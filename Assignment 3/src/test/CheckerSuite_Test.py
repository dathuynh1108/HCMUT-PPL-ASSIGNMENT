import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Object {
                Constructor(a,b : Int) {}
            }
            Class Program {

                main() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    Var o : Object = New Object(a,b);
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 999))

