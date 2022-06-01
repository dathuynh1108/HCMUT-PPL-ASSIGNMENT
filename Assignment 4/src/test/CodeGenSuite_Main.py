import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_000(self):
        input = r"""
            Class D96Class {
                main() {
                    io.putStringLn("Huynh Thanh Dat");
                    io.putString("1910110");
                    io.putLn();
                }
            }
        """
        expect = """Huynh Thanh Dat\n1910110\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_001(self):
        input = r"""
            Class D96Class {
                main() {
                    io.putInt(1);
                    io.putIntLn(1);
                    io.putIntLn(1 + 1);
                    io.putIntLn(1 - 1);
                    io.putIntLn(1 * 1);
                }
            }
        """
        expect = """11\n2\n0\n1\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    def test_002(self):
        input = r"""
            Class D96Class {
                main() {
                    io.putFloatLn(1.1);
                    io.putFloat(1.1);
                    io.putFloat(1.1 + 1.1);
                    io.putFloat(1.1 - 1.1);
                    io.putFloat(1.1 * 1.1);
                    io.putFloat(1.1 / 1.1);
                    
                    io.putFloatLn(1);
                    io.putFloat(1);
                    io.putFloat(1 + 1);
                    io.putFloat(1 - 1);
                    io.putFloat(1 * 1);
                    io.putFloat(1 / 1);

                    io.putFloat(1.1 + 1);
                    io.putFloat(1.1 - 1);
                    io.putFloat(1.1 * 1);
                    io.putFloat(1.1 / 1);
                }
            }
        """
        expect = """1.1\n1.12.20.01.211.01.0\n1.02.00.01.01.02.10.1000000241.11.1"""
        self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test_003(self):
        input = r"""
            Class D96Class {
                main() {
                    io.putBool(True);
                    io.putBoolLn(False);
                    io.putBool(True);
                    io.putBoolLn(False);

                    io.putBool(True && True);
                    io.putBool(True && False);
                    io.putBool(False && True);
                    io.putBool(False && False);
                    io.putBool(True || True);
                    io.putBool(True || False);
                    io.putBool(False || True);
                    io.putBool(False || False);
        
                    io.putBool(1 > 2);
                    io.putBool(1 >= 2);
                    io.putBool(1 < 2);
                    io.putBool(1 <= 2);
                    io.putBool(1 == 2);
                    io.putBool(1 != 2);

                    io.putBool(1.1 > 2);
                    io.putBool(1.1 >= 2);
                    io.putBool(1.1 < 2);
                    io.putBool(1.1 <= 2);
                    io.putBool(1.1 == 2);
                    io.putBool(1.1 != 2);    

                    io.putBool(1.1 > 2.1);
                    io.putBool(1.1 >= 2.1);
                    io.putBool(1.1 < 2.1);
                    io.putBool(1.1 <= 2.1);
                    io.putBool(1.1 == 2.1);
                    io.putBool(1.1 != 2.1);    
                }
            }
        """
        expect = """truefalse\ntruefalse\ntruefalsefalsefalsetruetruetruefalsefalsefalsetruetruefalsetruefalsefalsetruetruefalsetruefalsefalsetruetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_004(self):
        input = r"""
            Class D96Class {
                main() {
                    io.putStringLn("Dat" +. "Huynh");
                    io.putBool("Dat" ==. "Dat");
                    io.putBool("Dat" ==. "Huynh");
                }
            }
        """
        expect = """DatHuynh\ntruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_005(self):
        input = r"""
            Class D96Class {
                Var a: String = "Huynh Thanh Dat";
                main() {
                    Var a: String = "Huynh Thanh Dat";
                    io.putStringLn(a);
                    Var d: D96Class = New D96Class();
                    io.putStringLn(d.a);
                }
            }
        """
        expect = """Huynh Thanh Dat\nHuynh Thanh Dat\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 505))   

    def test_006(self):
        input = r"""
            Class D96Class {
                Var a: Int = 0;
                Var $a: Int = 1;
                $method() {
                    Var a: Int = 2;
                    Var d: D96Class = New D96Class();
                    io.putInt(d.a);
                    io.putInt(D96Class::$a);
                    io.putInt(a);
                    Return 3;
                }
                main() {
                    io.putInt(D96Class::$method()); 
                }
            }
        """
        expect = """0123"""
        self.assertTrue(TestCodeGen.test(input, expect, 506)) 
    
    def test_007(self):
        input = r"""
            Class D96Class {
                Var a: Int = 0;
                Var $a: Int = 1;
                Constructor(x: Int) {
                    io.putStringLn("<init>");
                } 
                main() {
                    Var x: D96Class = New D96Class();
                    Var y: D96Class = New D96Class(1);
                }
            }
        """
        expect = """<init>\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_008(self):
        input = r"""
            Class D96Class {
                main() {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5);
                    io.putInt(a[0]);
                    io.putInt(a[1]);
                    io.putInt(a[2]);
                    io.putInt(a[3]);
                    io.putInt(a[4]);
                }
            }
        """
        expect = """12345"""
        self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    def test_009(self):
        input = r"""
            Class D96Class {
                main() {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5); 
                    a[0] = 5;
                    a[1] = 4;
                    a[2] = 3;
                    a[3] = 2;
                    a[4] = 1;
                    io.putInt(a[0]);
                    io.putInt(a[1]);
                    io.putInt(a[2]);
                    io.putInt(a[3]);
                    io.putInt(a[4]);
                }
            }
        """
        expect = """54321"""
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_010(self):
        input = r"""
            Class D96Class {
                main() {
                    Var a: Array[Array[Int, 3], 3] = Array(
                        Array(1, 2, 3),
                        Array(4, 5, 6),
                        Array(7, 8, 9)
                    );
                    io.putInt(a[0][0]);
                    io.putInt(a[0][1]);
                    io.putInt(a[0][2]);

                    io.putInt(a[1][0]);
                    io.putInt(a[1][1]);
                    io.putInt(a[1][2]);

                    io.putInt(a[2][0]);
                    io.putInt(a[2][1]);
                    io.putInt(a[2][2]);
                }
            }
        """
        expect = """123456789"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    def test_011(self):
        input = r"""
            Class D96Class {
                main() {
                    Var a: Array[Array[Int, 3], 3] = Array(
                        Array(1, 2, 3),
                        Array(4, 5, 6),
                        Array(7, 8, 9)
                    );
                    
                    a[0][0] = 9;
                    a[0][1] = 8;
                    a[0][2] = 7;
                    a[1][0] = 6;
                    a[1][1] = 5;
                    a[1][2] = 4;
                    a[2][0] = 3;
                    a[2][1] = 2;
                    a[2][2] = 1;
                    
                    
                    io.putInt(a[0][0]);
                    io.putInt(a[0][1]);
                    io.putInt(a[0][2]);

                    io.putInt(a[1][0]);
                    io.putInt(a[1][1]);
                    io.putInt(a[1][2]);

                    io.putInt(a[2][0]);
                    io.putInt(a[2][1]);
                    io.putInt(a[2][2]);
                }
            }
        """
        expect = """987654321"""
        self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    
    def test_012(self):
        input = r"""
            Class D96Class {
                main() {
                    Var a: Array[Array[Array[Int, 2], 2], 2] = Array(
                        Array(
                            Array(1, 2),
                            Array(3, 4)
                        ),
                        Array(
                            Array(5, 6),
                            Array(7, 8)
                        )
                    );
                    io.putInt(a[0][0][0]);
                    a[0][0][0] = 1000;
                    io.putInt(a[0][0][0]);
                }
            }
        """
        expect = """11000"""
        self.assertTrue(TestCodeGen.test(input, expect, 512))
    
    def test_013(self):
        input = r"""
            Class D96Class {
                main() {
                    If (1 > 2) {
                        io.putString("False");
                    }
                    Else {
                        io.putString("True");
                    }
                }
            }
        """
        expect = """True"""
        self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    def test_014(self):
        input = r"""
            Class D96Class {
                main() {
                    If (1 > 2) {
                        io.putString("False");
                    }
                    Elseif (1 < 3) {
                        io.putString("True");
                    }
                    Else {
                        io.putString("False");
                    }
                }
            }
        """
        expect = """True"""
        self.assertTrue(TestCodeGen.test(input, expect, 514))
    
    def test_015(self):
        input = r"""
            Class D96Class {
                main() {
                    If (1 > 2) {
                        io.putString("False");
                    }
                    Elseif (1 > 3) {
                        io.putString("False");
                    }
                    Elseif (1 > 4) {
                        io.putString("False");
                    }
                    Elseif (1 == 1) {
                        io.putString("True");
                    }
                }
            }
        """
        expect = """True"""
        self.assertTrue(TestCodeGen.test(input, expect, 515))
    
    def test_016(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Foreach (i In 1 .. 10) {
                        io.putInt(i);
                    }
                }
            }
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test_017(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Foreach (i In 10 .. 1) {
                        io.putInt(i);
                    }
                }
            }
        """
        expect = """10987654321"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    def test_017(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Foreach (i In 1 .. 10 By 2) {
                        io.putInt(i);
                    }
                }
            }
        """
        expect = """13579"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    def test_018(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Foreach (i In 10 .. 1 By 2) {
                        io.putInt(i);
                    }
                }
            }
        """
        expect = """108642"""
        self.assertTrue(TestCodeGen.test(input, expect, 518))
    
    def test_019(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Foreach (i In a .. b) {
                        io.putInt(i);
                        a = a - 1;
                        b = b - 1;
                    }
                }
            }
        """
        expect = """12345"""
        self.assertTrue(TestCodeGen.test(input, expect, 519))
    
    def test_020(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Var temp: Int;
                    Foreach (i In a .. b) {
                        io.putInt(i);
                        temp = a;
                        a = b;
                        b = temp;
                    }
                }
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 520))
    
    def test_021(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Foreach (i In a .. b) {
                        io.putInt(i);
                        If (i == 5) {
                            Break;
                        }
                    }
                }
            }
        """
        expect = """12345"""
        self.assertTrue(TestCodeGen.test(input, expect, 521))
    
    def test_022(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Foreach (i In a .. b) {
                        io.putInt(i);
                        If (i > 5) {
                            Continue;
                        }
                        io.putInt(i);
                    }
                }
            }
        """
        expect = """1122334455678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 522))
    
    def test_023(self):
        input = r"""
            Class D96Class {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Foreach (i In a .. b) {
                        io.putInt(i);
                        Continue;
                        Break;
                    }
                }
            }
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 523))
    
    def test_024(self):
        input = r"""
            Class D96Class {
                main() {
                    Var a: Int = 2;
                    Var b: Int = 10;
                    io.putFloat(a-b+b/a * b + 0.1);
                    io.putInt(a + b * a % b);
                }
            }
        """
        expect = """42.12"""
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    def test_025(self):
        input = r"""
            Class D96Class {
                Var a: Int = 1;
                Val b: Int = 1;

                Var x: Float = 1;
                Var y: Float = 2;


                Var $a: Int = 1;
                
                method() {
                    Var a: Int = 1;
                    Val b: Int = 1;

                    Var x: Float = 1;
                    Var y: Float = 2;
                    
                    io.putInt(a + b);
                    io.putInt(a + a);
                    io.putInt(b + b);
                    io.putInt(a + Self.a);
                    io.putInt(a + Self.b);

                    io.putFloat(a + b);
                    io.putFloat(a + a);
                    io.putFloat(b + b);
                    io.putFloat(a + Self.a);
                    io.putFloat(a + Self.b);
                    io.putFloat(Self. a + Self.b);
                    io.putFloat(x + y);
                    io.putFloat(a + x);
                    io.putFloat(a + y);
                    io.putFloat(a + Self.x);
                    io.putFloat(a + Self.y);
                }
                main() {
                    Var d: D96Class = New D96Class();
                    d.method();
                }
            }
        """
        expect = """222222.02.02.02.02.02.03.02.03.02.03.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 525))
    
    def test_026(self):
        input = r"""
            Class D96Class {
                Var $a: Int = 1;
                Val $b: Int = 1;

                Var $x: Float = 1;
                Var $y: Float = 1.0;
                method() {
                    Var a: Int = 1;
                    Val b: Int = 1;

                    Var x: Float = 1;
                    Val y: Float = 1.0;

                    io.putInt(D96Class::$a + b);
                    io.putInt(D96Class::$a  + a);
                    io.putInt(D96Class::$b  + b);
                    io.putInt(D96Class::$a  + b);
                    io.putInt(D96Class::$a  + D96Class::$b);

                    io.putFloat(D96Class::$a + x);
                    io.putFloat(D96Class::$a  + y);
                    io.putFloat(D96Class::$x  + a);
                    io.putFloat(D96Class::$x  + b);
                    io.putFloat(D96Class::$x  + D96Class::$y);
                }
                main() {
                    Var d: D96Class = New D96Class();
                    d.method();
                }
            }
        """
        expect = """222222.02.02.02.02.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    def test_027(self):
        input = r"""
            Class D96Class {
                Var $name: String = "Huynh Thanh Dat";
                Var $escapeSequence: String = "\n1910110";
            
                main() {
                    io.putString(D96Class::$name +. D96Class::$escapeSequence);
                }
            }
        """
        expect = """Huynh Thanh Dat\n1910110"""
        self.assertTrue(TestCodeGen.test(input, expect, 527))
    
    
    def test_028(self):
        input = r"""
            Class D96Class {
                main() {
                    Var true: Boolean = True;
                    Var false: Boolean = False;

                    io.putBool(true && false);
                    io.putBool(true && True);
                    io.putBool(!true);
                    io.putBool(!false);
                    io.putBool(!True);
                    io.putBool(!False);
                }
            }
        """
        expect = """falsetruefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    def test_029(self):
        input = r"""
            Class D96Class {
                Var $true: Boolean = True;
                Var $false: Boolean = False;
                main() {
                    io.putBool(D96Class::$true && D96Class::$false);
                    io.putBool(D96Class::$true && True);
                    io.putBool(!D96Class::$true && D96Class::$false);
                    io.putBool(!D96Class::$true && True);
                    io.putBool(!D96Class::$true);
                    io.putBool(!D96Class::$false);
                    io.putBool(!D96Class::$true);
                    io.putBool(!D96Class::$false);
                }
            }
        """
        expect = """falsetruefalsefalsefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    
    