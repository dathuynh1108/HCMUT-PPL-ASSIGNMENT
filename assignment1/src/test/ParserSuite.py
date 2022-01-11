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

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.test(input,expect,203))