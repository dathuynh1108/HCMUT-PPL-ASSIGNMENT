import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = r"""
        class Program {
            var x: Int;
            var $y: Float;
            main(fuck: Int) {
                var x: Int;
            }
        }"""
        expect = r"successful"
        num = 201;
        self.assertTrue(TestParser.test(input,expect,num))
