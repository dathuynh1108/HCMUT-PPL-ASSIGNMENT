import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = r"""
        Class Program {
            Var x,y,z,r,t: Int = 1,2,x,y,z;
            Var x,y : Int = 1,2;
        }"""
        expect = r"successful"
        num = 201;
        self.assertTrue(TestParser.test(input,expect,num))
