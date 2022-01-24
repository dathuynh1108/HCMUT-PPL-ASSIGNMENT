import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_something(self):
        input = """ 
                    Class Program {
                        main() {
                            a.a().a.a();
                        }
                    
                """
        expect = ""
        self.assertTrue(TestParser.test(input,expect,999)) 
    


