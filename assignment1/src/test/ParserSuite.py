import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = r"""
        Class Program {
            Var x: Int = 1,2,3,4;
        }"""
        expect = r"successful"
        num = 201;
        self.assertTrue(TestParser.test(input,expect,num))
