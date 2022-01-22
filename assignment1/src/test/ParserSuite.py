import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_081_multi_demensional_array(self):
        input = r"""
            Class Program {
                main() {
                    a = Array(
                            Array(1,2,3),
                            Array(1,2)
                        );
                }
            }
        """
        expect = r"""successful"""
        num = 281
        self.assertTrue(TestParser.test(input,expect,num))  


