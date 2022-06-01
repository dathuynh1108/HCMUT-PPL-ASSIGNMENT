import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class D96Class {
                Var x: Int = 123;
                Var y: Float = 1;
                Var $x: Int = 1;
                Var $y: Float = 1;
                method_1() {
                    Return Self.x;
                }
                method_2() {
                    Return Self.method_1();
                }
                method_3() {
                    Return Self.method_2();
                }
                main() {
                    Var x: D96Class = New D96Class();
                    io.putInt(x.method_3());
                }
            }
        """
        expect = """123"""
        self.assertTrue(TestCodeGen.test(input, expect, 999)) 
    
