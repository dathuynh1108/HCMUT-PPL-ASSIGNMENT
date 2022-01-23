import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_081_multi_demensional_array(self):
        input = r"""
            Class Program {
                main() {
                    a();
                    a.b();
                    a.b.c();
                    a.b.c.d();
                    
                    a.b().c();
                    a.b.c().d();
                    a.b().c().d();
                    a().b().c().d();
                    
                    a::$b();
                    a::$b.c();
                    a::$b.c.d();

                    a::$b.c().d();
                    a::$b().c.d();
                    a::$b().c().d();            
                }
            }
        """
        expect = r"successful"
        num = 999
        self.assertTrue(TestParser.test(input,expect,num))  


