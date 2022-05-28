import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = """ 
            Class A {
                func() {
                    Return;
                }
            }
            Class B {
                Var obj_a : A;
                func() {
                    Return New A();
                }
            }
            Class C {
                Var obj_b : B;
            }
            Class Program {
                
                main() {
                    Var c : C;
                    c.obj_b.func().func();      ## ok, return void ##
                    c.obj_b.func();             ## error, return non-void ##
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 999))

