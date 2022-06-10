import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class D96Class {
                method(a: Array[Int, 5]) {
                    Return a;
                }
                main() {    
                    Var d: D96Class = New D96Class();
                    io.writeInt(d.method(d.method(Array(1,2,3,4,5)))[0]);
                    
                }
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 999))
    
