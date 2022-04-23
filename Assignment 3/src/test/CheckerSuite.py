import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Object {}
            Class Animal : Object {}
            Class Dog : Animal {
                Constructor(x: Object; y: Object; z: Object) {}
            }
            Class Program {
                main() {
                    Var x: Int = New Dog(New Object(), New Dog(), New Animal());
                }
            }

        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 999))

