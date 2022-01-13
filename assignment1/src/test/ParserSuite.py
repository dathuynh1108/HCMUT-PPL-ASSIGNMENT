import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = r"""
        Class Program {
            Var x: Int;
            Var $y: Float = 1+2-3*5/6%7;
            main(fuck: Int) {
                Var x: Int;
                Self.a= New a(123, 1+2+3, 4*5);
                expression = !a || b && c + a*b/c-d%e;
                a[Self.a][1+2+3*4/5] = 1;
            }
        }"""
        expect = r"successful"
        num = 201;
        self.assertTrue(TestParser.test(input,expect,num))
