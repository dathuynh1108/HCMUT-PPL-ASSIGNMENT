import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = r"""
            Class Program {
                sort(a: Array[Int, 10000]; size: Int) {
                    Var i,j: Int;
                    Foreach (i In 0 .. size - 2) {
                        Var min_index : Int = i;
                        Var min :Int = a[i];
                        Foreach (j In i + 1 .. size - 1) {
                            If (a[j] < a[min_index]) {
                                min_index = j;
                                min = a[j];
                            }
                        }
                        Var temp :Int = a[i];
                        a[i] = a[min_index];
                        a[min_index] = temp;
                    }
                    Foreach (i In 0 .. size - 1) {
                        io.writeInt(a[i]);
                    }
                }
                main() {    
                    Var o: Program = New Program();
                    o.sort(Array(10,9,8,7,6,5,4,3,2,1), 10);
                    
                }   
            }
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 999))
    
