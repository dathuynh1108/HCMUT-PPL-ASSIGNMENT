import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_000(self):
        input = """
            Class D96Class{
                Var $a: Int = 1;
                Var a: Int = 1;
                method(x: Int; y: String) {
                    Var a: Int = -1;
                    Val b: Int = 1;
                }
                main() {}
            }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,500))
