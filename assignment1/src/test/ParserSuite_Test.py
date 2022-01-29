import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_18(self):
        input = """
               Class myclass{
                   Var a,b,c: Int;
                   Var d : Array[Int, 5] = Array(1,2,3,4,5);
                   func(){
                       a = 10;
                       b = a + 5 + 10;
                       d[4] = d[2] + d[1];
                       If(a>=10){
                           a = a + 1;
                       }
                       Else {
                           a = a-1;
                       }
                   }
               }
                """
        expect = "Error on line 9 col 25: ("
        self.assertTrue(TestParser.test(input,expect,999))
    


