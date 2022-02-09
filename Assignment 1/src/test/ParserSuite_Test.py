import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_33(self):
        input = """
                Class myclass{
                   Var a,b,c: Int;
                   Var d : Array[Int, 5] = Array(1,2,3,4,5);
                   func(e:Int;f:Array){
                       Var g : Array[Array[Int,1],3];
                       If(a){
                           Foreach ( i In 1 .. 100 By 1){
                               a = a+i;
                           }
                       }Else{
                           Return a+1;
                       }
                   }
               }
                """
        expect="""successful"""
        self.assertTrue(TestParser.test(input,expect,999))
    


