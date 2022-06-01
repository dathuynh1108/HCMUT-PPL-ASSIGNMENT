import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class D96Class {
                Var $true: Boolean = True;
                Var $false: Boolean = False;
                main() {
                    io.putBool(D96Class::$true && D96Class::$false);
                    io.putBool(D96Class::$true && True);
                    io.putBool(!D96Class::$true && D96Class::$false);
                    io.putBool(!D96Class::$true && True);
                    io.putBool(!D96Class::$true);
                    io.putBool(!D96Class::$false);
                    io.putBool(!D96Class::$true);
                    io.putBool(!D96Class::$false);
                    
                }
            }
        """
        expect = """falsetruefalsefalsefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 999)) 
