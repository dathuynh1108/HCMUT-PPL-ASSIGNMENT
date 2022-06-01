import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class D96Class {
                Var a: Int = 0;
                Var $a: Int = 1;
                $method() {
                    Var a: Int = 2;
                    Var d: D96Class = New D96Class();
                    io.putInt(d.a);
                    io.putInt(D96Class::$a);
                    io.putInt(a);
                    Return 3;
                }
                main() {
                    io.putInt(D96Class::$method()); 
                }
            }
        """
        expect = """0123"""
        self.assertTrue(TestCodeGen.test(input, expect, 999)) 