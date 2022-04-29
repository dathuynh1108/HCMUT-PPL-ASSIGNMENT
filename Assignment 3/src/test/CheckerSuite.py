import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Object {
                Var object: Object = New Object();
                method(x: Int; y: Float) {}
            }
            Class Program {
                main() {}
                Val object: Object = New Object();
                Var x: Int = Self.object.object.object.object;
            }
        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 999))

