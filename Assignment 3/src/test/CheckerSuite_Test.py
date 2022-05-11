import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_999(self):
        input = """    
            Class Program {
                func1() {
                    Return 1;
                }
                
                func2() {
                    Return 2.3;
                }
                
                main() {
                    Var x : Float = Self.func1();
                    Val y : Float = Self.func2() + 1;
                    Val z : Float = Self.func1() + Self.func2() / Self.func1() * Self.func2();
                    Val m : Float = Self.func1() + x;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 999))

