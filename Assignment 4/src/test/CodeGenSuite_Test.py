import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_000(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i: Int;
                    Foreach (i In 100 .. 1 By 1) {
                        io.putIntLn(i);
                    }
                }
            }
        """
        expect = """"""
        self.assertTrue(TestCodeGen.test(input, expect, 500))
