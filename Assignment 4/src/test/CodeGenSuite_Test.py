import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class D96Class {
                main() {    
                    io.printStr("abc");
                }
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 999))
    
