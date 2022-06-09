import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Object {
                method() {
                    Return 1;
                }
                $method() {
                    Return 1;
                }
            }
            Class Object_1 : Object {}
            Class Object_2 : Object_1 {}
            
            Class D96Class : Object_2 {
                main() {
                    Var o: D96Class = New D96Class();
                    io.writeFloat(o.method());
                    io.writeFloat(D96Class::$method());
                }
            }
        """
        expect = """1.01.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 999)) 
    
