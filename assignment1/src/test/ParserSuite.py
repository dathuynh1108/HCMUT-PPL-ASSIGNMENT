import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_033_incorrect_access_instance(self): 
        input = r"""
            Class Program {
                main() {
                    a = b.$attribute;
                }
            }
        """
        expect = r"successful"
        num = 233
        self.assertTrue(TestParser.test(input,expect,num))    

