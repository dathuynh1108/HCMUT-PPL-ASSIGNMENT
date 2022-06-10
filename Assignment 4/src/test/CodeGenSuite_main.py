import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_000(self):
        input = r"""
            Class Program {
                main() {
                    io.writeStr("Huynh Thanh Dat\n");
                    io.writeStr("1910110\n");
                }
            }
        """
        expect = """Huynh Thanh Dat\n1910110\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_001(self):
        input = r"""
            Class Program {
                main() {
                    io.writeInt(1);
                    io.writeInt(1);
                    io.writeInt(1 + 1);
                    io.writeInt(1 - 1);
                    io.writeInt(1 * 1);
                }
            }
        """
        expect = """11201"""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    def test_002(self):
        input = r"""
            Class Program {
                main() {
                    io.writeFloat(1.1);
                    io.writeFloat(1.1);
                    io.writeFloat(1.1 + 1.1);
                    io.writeFloat(1.1 - 1.1);
                    io.writeFloat(1.1 * 1.1);
                    io.writeFloat(1.1 / 1.1);
                    
                    io.writeFloat(1);
                    io.writeFloat(1);
                    io.writeFloat(1 + 1);
                    io.writeFloat(1 - 1);
                    io.writeFloat(1 * 1);
                    io.writeFloat(1 / 1);

                    io.writeFloat(1.1 + 1);
                    io.writeFloat(1.1 - 1);
                    io.writeFloat(1.1 * 1);
                    io.writeFloat(1.1 / 1);
                }
            }
        """
        expect = """1.11.12.20.01.211.01.01.02.00.01.01.02.10.1000000241.11.1"""
        self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test_003(self):
        input = r"""
            Class Program {
                main() {
                    io.writeBool(True);
                    io.writeBool(False);
                    io.writeBool(True);
                    io.writeBool(False);

                    io.writeBool(True && True);
                    io.writeBool(True && False);
                    io.writeBool(False && True);
                    io.writeBool(False && False);
                    io.writeBool(True || True);
                    io.writeBool(True || False);
                    io.writeBool(False || True);
                    io.writeBool(False || False);
        
                    io.writeBool(1 > 2);
                    io.writeBool(1 >= 2);
                    io.writeBool(1 < 2);
                    io.writeBool(1 <= 2);
                    io.writeBool(1 == 2);
                    io.writeBool(1 != 2);

                    io.writeBool(1.1 > 2);
                    io.writeBool(1.1 >= 2);
                    io.writeBool(1.1 < 2);
                    io.writeBool(1.1 <= 2);
                    io.writeBool(1.1 == 2);
                    io.writeBool(1.1 != 2);    

                    io.writeBool(1.1 > 2.1);
                    io.writeBool(1.1 >= 2.1);
                    io.writeBool(1.1 < 2.1);
                    io.writeBool(1.1 <= 2.1);
                    io.writeBool(1.1 == 2.1);
                    io.writeBool(1.1 != 2.1);    
                }
            }
        """
        expect = """truefalsetruefalsetruefalsefalsefalsetruetruetruefalsefalsefalsetruetruefalsetruefalsefalsetruetruefalsetruefalsefalsetruetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_004(self):
        input = r"""
            Class Program {
                main() {
                    io.writeStr("Dat" +. "Huynh\n");
                    io.writeBool("Dat" ==. "Dat");
                    io.writeBool("Dat" ==. "Huynh");
                }
            }
        """
        expect = """DatHuynh\ntruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_005(self):
        input = r"""
            Class Program {
                Var a: String = "Huynh Thanh Dat";
                main() {
                    Var a: String = "Huynh Thanh Dat";
                    io.writeStr(a);
                    Var d: Program = New Program();
                    io.writeStr(d.a);
                }
            }
        """
        expect = """Huynh Thanh DatHuynh Thanh Dat"""
        self.assertTrue(TestCodeGen.test(input, expect, 505))   

    def test_006(self):
        input = r"""
            Class Program {
                Var a: Int = 0;
                Var $a: Int = 1;
                $method() {
                    Var a: Int = 2;
                    Var d: Program = New Program();
                    io.writeInt(d.a);
                    io.writeInt(Program::$a);
                    io.writeInt(a);
                    Return 3;
                }
                main() {
                    io.writeInt(Program::$method()); 
                }
            }
        """
        expect = """0123"""
        self.assertTrue(TestCodeGen.test(input, expect, 506)) 
    
    def test_007(self):
        input = r"""
            Class Program {
                Var a: Int = 0;
                Var $a: Int = 1;
                Constructor(x: Int) {
                    io.writeStr("<init>");
                } 
                main() {
                    Var x: Program = New Program();
                    Var y: Program = New Program(1);
                }
            }
        """
        expect = """<init>"""
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_008(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5);
                    io.writeInt(a[0]);
                    io.writeInt(a[1]);
                    io.writeInt(a[2]);
                    io.writeInt(a[3]);
                    io.writeInt(a[4]);
                }
            }
        """
        expect = """12345"""
        self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    def test_009(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5); 
                    a[0] = 5;
                    a[1] = 4;
                    a[2] = 3;
                    a[3] = 2;
                    a[4] = 1;
                    io.writeInt(a[0]);
                    io.writeInt(a[1]);
                    io.writeInt(a[2]);
                    io.writeInt(a[3]);
                    io.writeInt(a[4]);
                }
            }
        """
        expect = """54321"""
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_010(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Array[Int, 3], 3] = Array(
                        Array(1, 2, 3),
                        Array(4, 5, 6),
                        Array(7, 8, 9)
                    );
                    io.writeInt(a[0][0]);
                    io.writeInt(a[0][1]);
                    io.writeInt(a[0][2]);

                    io.writeInt(a[1][0]);
                    io.writeInt(a[1][1]);
                    io.writeInt(a[1][2]);

                    io.writeInt(a[2][0]);
                    io.writeInt(a[2][1]);
                    io.writeInt(a[2][2]);
                }
            }
        """
        expect = """123456789"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    def test_011(self):
        input = r"""
            Class Program {
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
                    
                    
                    io.writeInt(a[0][0]);
                    io.writeInt(a[0][1]);
                    io.writeInt(a[0][2]);

                    io.writeInt(a[1][0]);
                    io.writeInt(a[1][1]);
                    io.writeInt(a[1][2]);

                    io.writeInt(a[2][0]);
                    io.writeInt(a[2][1]);
                    io.writeInt(a[2][2]);
                }
            }
        """
        expect = """987654321"""
        self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    
    def test_012(self):
        input = r"""
            Class Program {
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
                    io.writeInt(a[0][0][0]);
                    a[0][0][0] = 1000;
                    io.writeInt(a[0][0][0]);
                }
            }
        """
        expect = """11000"""
        self.assertTrue(TestCodeGen.test(input, expect, 512))
    
    def test_013(self):
        input = r"""
            Class Program {
                main() {
                    If (1 > 2) {
                        io.writeStr("False");
                    }
                    Else {
                        io.writeStr("True");
                    }
                }
            }
        """
        expect = """True"""
        self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    def test_014(self):
        input = r"""
            Class Program {
                main() {
                    If (1 > 2) {
                        io.writeStr("False");
                    }
                    Elseif (1 < 3) {
                        io.writeStr("True");
                    }
                    Else {
                        io.writeStr("False");
                    }
                }
            }
        """
        expect = """True"""
        self.assertTrue(TestCodeGen.test(input, expect, 514))
    
    def test_015(self):
        input = r"""
            Class Program {
                main() {
                    If (1 > 2) {
                        io.writeStr("False");
                    }
                    Elseif (1 > 3) {
                        io.writeStr("False");
                    }
                    Elseif (1 > 4) {
                        io.writeStr("False");
                    }
                    Elseif (1 == 1) {
                        io.writeStr("True");
                    }
                }
            }
        """
        expect = """True"""
        self.assertTrue(TestCodeGen.test(input, expect, 515))
    
    def test_016(self):
        input = r"""
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Foreach (i In 1 .. 10) {
                        io.writeInt(i);
                    }
                }
            }
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test_017(self):
        input = r"""
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Foreach (i In 10 .. 1) {
                        io.writeInt(i);
                    }
                }
            }
        """
        expect = """10987654321"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    def test_017(self):
        input = r"""
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Foreach (i In 1 .. 10 By 2) {
                        io.writeInt(i);
                    }
                }
            }
        """
        expect = """13579"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    def test_018(self):
        input = r"""
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Foreach (i In 10 .. 1 By 2) {
                        io.writeInt(i);
                    }
                }
            }
        """
        expect = """108642"""
        self.assertTrue(TestCodeGen.test(input, expect, 518))
    
    def test_019(self):
        input = r"""
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Foreach (i In a .. b) {
                        io.writeInt(i);
                        a = a - 1;
                        b = b - 1;
                    }
                }
            }
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 519))
    
    def test_020(self):
        input = r"""
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Var temp: Int;
                    Foreach (i In a .. b) {
                        io.writeInt(i);
                        temp = a;
                        a = b;
                        b = temp;
                    }
                }
            }
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 520))
    
    def test_021(self):
        input = r"""
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Foreach (i In a .. b) {
                        io.writeInt(i);
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
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Foreach (i In a .. b) {
                        io.writeInt(i);
                        If (i > 5) {
                            Continue;
                        }
                        io.writeInt(i);
                    }
                }
            }
        """
        expect = """1122334455678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 522))
    
    def test_023(self):
        input = r"""
            Class Program {
                main() {
                    Var i : Int = 1000;
                    Var a: Int = 1;
                    Var b: Int = 10;
                    Foreach (i In a .. b) {
                        io.writeInt(i);
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
            Class Program {
                main() {
                    Var a: Int = 2;
                    Var b: Int = 10;
                    io.writeFloat(a-b+b/a * b + 0.1);
                    io.writeInt(a + b * a % b);
                }
            }
        """
        expect = """42.12"""
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    def test_025(self):
        input = r"""
            Class Program {
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
                    
                    io.writeInt(a + b);
                    io.writeInt(a + a);
                    io.writeInt(b + b);
                    io.writeInt(a + Self.a);
                    io.writeInt(a + Self.b);

                    io.writeFloat(a + b);
                    io.writeFloat(a + a);
                    io.writeFloat(b + b);
                    io.writeFloat(a + Self.a);
                    io.writeFloat(a + Self.b);
                    io.writeFloat(Self. a + Self.b);
                    io.writeFloat(x + y);
                    io.writeFloat(a + x);
                    io.writeFloat(a + y);
                    io.writeFloat(a + Self.x);
                    io.writeFloat(a + Self.y);
                }
                main() {
                    Var d: Program = New Program();
                    d.method();
                }
            }
        """
        expect = """222222.02.02.02.02.02.03.02.03.02.03.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 525))
    
    def test_026(self):
        input = r"""
            Class Program {
                Var $a: Int = 1;
                Val $b: Int = 1;

                Var $x: Float = 1;
                Var $y: Float = 1.0;
                method() {
                    Var a: Int = 1;
                    Val b: Int = 1;

                    Var x: Float = 1;
                    Val y: Float = 1.0;

                    io.writeInt(Program::$a + b);
                    io.writeInt(Program::$a  + a);
                    io.writeInt(Program::$b  + b);
                    io.writeInt(Program::$a  + b);
                    io.writeInt(Program::$a  + Program::$b);

                    io.writeFloat(Program::$a + x);
                    io.writeFloat(Program::$a  + y);
                    io.writeFloat(Program::$x  + a);
                    io.writeFloat(Program::$x  + b);
                    io.writeFloat(Program::$x  + Program::$y);
                }
                main() {
                    Var d: Program = New Program();
                    d.method();
                }
            }
        """
        expect = """222222.02.02.02.02.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    def test_027(self):
        input = r"""
            Class Program {
                Var $name: String = "Huynh Thanh Dat";
                Var $escapeSequence: String = "\n1910110";
            
                main() {
                    io.writeStr(Program::$name +. Program::$escapeSequence);
                }
            }
        """
        expect = """Huynh Thanh Dat\n1910110"""
        self.assertTrue(TestCodeGen.test(input, expect, 527))
    
    
    def test_028(self):
        input = r"""
            Class Program {
                main() {
                    Var true: Boolean = True;
                    Var false: Boolean = False;

                    io.writeBool(true && false);
                    io.writeBool(true && True);
                    io.writeBool(!true);
                    io.writeBool(!false);
                    io.writeBool(!True);
                    io.writeBool(!False);
                }
            }
        """
        expect = """falsetruefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    def test_029(self):
        input = r"""
            Class Program {
                Var $true: Boolean = True;
                Var $false: Boolean = False;
                main() {
                    io.writeBool(Program::$true && Program::$false);
                    io.writeBool(Program::$true && True);
                    io.writeBool(!Program::$true && Program::$false);
                    io.writeBool(!Program::$true && True);
                    io.writeBool(!Program::$true);
                    io.writeBool(!Program::$false);
                    io.writeBool(!Program::$true);
                    io.writeBool(!Program::$false);
                }
            }
        """
        expect = """falsetruefalsefalsefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    def test_030(self):
        input = r"""
            Class Program {
                Var x: Int = 1;
                Var y: Float = 1;
                Var $x: Int = 1;
                Var $y: Float = 1;
                Constructor(x: Int) {}
                main() {
                    Var x, y: Program = New Program(), New Program(1);
                    io.writeStr("OK");
                }
            }
        """
        expect = """OK"""
        self.assertTrue(TestCodeGen.test(input, expect, 530))
    
    def test_031(self):
        input = r"""
            Class Program {
                Var x: Int = 1;
                Var y: Float = 1;
                Var $x: Int = 1;
                Var $y: Float = 1;
                Constructor(x: Int) {
                    Self.x = 100;
                }
                main() {
                    Var x, y: Program = New Program(), New Program(1);
                    io.writeInt(x.x);
                    io.writeInt(y.x);
                }
            }
        """
        expect = """1100"""
        self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    def test_032(self):
        input = r"""
            Class Program {
                Var x: Int = 123;
                Var y: Float = 1;
                Var $x: Int = 1;
                Var $y: Float = 1;
                method_1() {
                    Return Self.x;
                }
                method_2() {
                    Return Self.method_1();
                }
                method_3() {
                    Return Self.method_2();
                }
                main() {
                    Var x: Program = New Program();
                    io.writeInt(x.method_3());
                }
            }
        """
        expect = """123"""
        self.assertTrue(TestCodeGen.test(input, expect, 532))
    
    def test_033(self):
        input = r"""
            Class Program {
                Var x: Int = 123;
                Var y: Float = 1;
                Var $x: Int = 1;
                Var $y: Float = 1;
                method_1() {
                    Return Self;
                }
                main() {
                    Var x: Program = New Program();
                    io.writeInt(x.method_1().x);
                    io.writeFloat(x.method_1().method_1().method_1().y);
                }
            }
        """
        expect = """1231.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    def test_034(self):
        input = r"""
            Class Program {
                method_1() {
                    Return Self;
                }
                main() {
                    Var i: Int = 1;
                    Foreach (i In 1 .. 10) {
                        If (i % 2 == 0) {
                            io.writeStr("even ");
                        }
                        Else {
                            io.writeStr("odd ");
                        }
                    }
                }
            }
        """
        expect = """odd even odd even odd even odd even odd even """
        self.assertTrue(TestCodeGen.test(input, expect, 534))
    
    def test_035(self):
        input = r"""
            Class Program {
                method_1() {
                    Return Self;
                }
                main() {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5);
                    a = Array(-1,-2,-3,-4,-5);
                    Var i: Int;
                    Foreach (i In 0 .. 4) {
                        io.writeInt(a[i]);
                    }
                }
            }
        """
        expect = """-1-2-3-4-5"""
        self.assertTrue(TestCodeGen.test(input, expect, 535))
    
    def test_036(self):
        input = r"""
            Class Program {
                method_1() {
                    Return Self;
                }
                main() {
                    Var a: Array[Array[Int, 5], 2] = Array(
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5)
                    );
                    a[1] = Array(6,7,8,9,10);
                    Var i: Int;
                    Var j: Int;
                    Foreach (i In 0 .. 1) {
                        Foreach(j In 0 .. 4) {
                            io.writeInt(a[i][j]);
                        }
                    }
                }
            }
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 536))
    
    def test_037(self):
        input = r"""
            Class Program {
                method_1() {
                    Return Self;
                }
                main() {
                    Var a: Array[Array[Int, 5], 2] = Array(
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5)
                    );
                    a[1] = Array(6,7,8,9,10);
                    Var i: Int;
                    Var j: Int;
                    Foreach (i In 1 + 1 - 1 - 1 .. 1 + 1 - 1 - 1 + 1) {
                        Foreach(j In 1 * 1 * 1 * 1 .. 1 * 2 + 1 * 2) {
                            io.writeInt(a[i][j]);
                        }
                    }
                }
            }
        """
        expect = """234578910"""
        self.assertTrue(TestCodeGen.test(input, expect, 537))
    
    def test_038(self):
        input = r"""
            Class Program {
                method_1() {
                    Return Self;
                }
                main() {
                    Var a: Array[Array[Int, 5], 2] = Array(
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5)
                    );
                    a[1] = Array(6,7,8,9,10);
                    Var i: Int;
                    Var j: Int;
                    Foreach (i In 0 .. 1) {
                        Foreach(j In 0 .. 4) {
                            If (j % 2 == 0) {
                                io.writeInt(a[i][j]);
                            }
                        }
                    }
                }
            }
        """
        expect = """1356810"""
        self.assertTrue(TestCodeGen.test(input, expect, 538))
    
    def test_039(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Float, 4] = Array(1,2,3,4);
                    io.writeFloat(a[0]);
                }
            }
        """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 539))
    
    def test_040(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Float, 4] = Array(1, 2.0, 3, 4.0); ## Different type ##
                    io.writeFloat(a[0]);
                }
            }
        """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_041(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Float, 4] = Array(1, 2.0, 3, 4.0); ## Different type ##
                    a[0] = 10; 
                    io.writeFloat(a[0]);
                }
            }
        """
        expect = """10.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_042(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Array[Float, 4], 2] = Array(
                        Array(1,2,3,4),
                        Array(5,6,7,8)
                    );
                    io.writeFloat(a[0][0]);
                }
            }
        """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 542)) 
    
    def test_043(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Array[Float, 4], 2] = Array(
                        Array(1,2,3,4),
                        Array(5,6,7,8)
                    );
                    a[0][0] = 10;
                    io.writeFloat(a[0][0]);
                }
            }
        """
        expect = """10.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 543)) 
    
    def test_044(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Array[Float, 4], 2] = Array(
                        Array(1,2.0,3.0,4),
                        Array(5.0,6,7,8.0)
                    );
                    a[0][0] = 10;
                    io.writeFloat(a[0][0]);
                }
            }
        """
        expect = """10.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 544)) 
    
    def test_045(self):
        input = r"""
            Class Program {
                Var $a: Float = 1;
                main() {
                    Program::$a = 2;
                    io.writeFloat(Program::$a);
                }
            }
        """
        expect = """2.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 545)) 

    def test_046(self):
        input = r"""
            Class Program {
                Var $a: Float = 1;
                Var a: Float = 1;
                main() {
                    Var d: Program = New Program();
                    d.a = 2;
                    io.writeFloat(d.a);
                }
            }
        """
        expect = """2.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 546)) 
    
    def test_047(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                Var $a: Int = 1;
                method() {
                    Return Self.a;
                }
                $method() {
                    Return Object::$a;
                }
            }
            Class Program {
                main() {
                    Var o: Object = New Object();
                    io.writeInt(o.a);
                    io.writeInt(Object::$a);
                    io.writeInt(o.method());
                    io.writeInt(Object::$method());
                }
            }
        """
        expect = """1111"""
        self.assertTrue(TestCodeGen.test(input, expect, 547)) 
    
    def test_048(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                Var $a: Int = 1;
                method() {
                    Return Self.a;
                }
                $method() {
                    Return Object::$a;
                }
            }
            Class Program : Object {
                main() {
                    Var d: Program = New Program();
                    io.writeInt(d.a);
                    io.writeInt(Program::$a);
                    io.writeInt(d.method());
                    io.writeInt(Program::$method());
                }
            }
        """
        expect = """1111"""
        self.assertTrue(TestCodeGen.test(input, expect, 548))
    
    def test_049(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                Var $a: Int = 1;
                method() {
                    Return Self.a;
                }
                $method() {
                    Return Object::$a;
                }
            }
            Class Program : Object {
                Var a: Int = 2;
                Var $a: Int = 2;
                method() {
                    Return 2;
                }
                $method() {
                    Return 2;
                }
                main() {
                    Var o: Program = New Program();
                    io.writeInt(o.a);
                    io.writeInt(Program::$a);
                    io.writeInt(o.method());
                    io.writeInt(Program::$method());
                }
            }
        """
        expect = """2222"""
        self.assertTrue(TestCodeGen.test(input, expect, 549)) 
    
    def test_050(self):
        input = r"""
            Class Object {
                method() {
                    Return 1;
                }
                $method() {
                    Return 1;
                }
            }
            Class Object_1 : Object {}
            Class Object_2 : Object_1 {}
            
            Class Program : Object_2 {
                main() {
                    Var o: Program = New Program();
                    io.writeFloat(o.method());
                    io.writeFloat(Program::$method());
                }
            }
        """
        expect = """1.01.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 550)) 
    
    def test_051(self):
        input = r"""
            Class Object {
                method() {
                    Return "Parent";
                }
                $method() {
                    Return "Parent";
                }
            }
            
            Class Program : Object {
                method() {
                    Return "Child";
                }
                $method() {
                    Return "Child";
                }
                main() {
                    Var o: Object = New Program();
                    io.writeStr(o.method());
                    io.writeStr(Program::$method());
                }
            }
        """
        expect = """ChildChild"""
        self.assertTrue(TestCodeGen.test(input, expect, 551)) 
    
    def test_052(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                method(o: Object) {
                    Return Self.a;
                }
            }
            
            Class Program : Object {
                Var a: Int = 2;
                method(o: Object) {
                    Return Self.a;
                }
                main() {
                    Var o: Object = New Program();
                    io.writeInt(o.method(o));
                }
            }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 552)) 
    
    def test_053(self):
        input = r"""
            Class Object {
                method() {
                    Return 1;
                }
                some_method() {}
            }

            Class Object_2 : Object {
                method() {
                    Return 2;
                }
            }
            Class Object_3 : Object {
                method() {
                    Return 3;
                }
            }
            Class Program : Object {
                Var a: Object = New Object();
                some_method() {
                    Var a: Object = New Object();
                    io.writeInt(a.method());
                    a = New Object_2();
                    io.writeInt(a.method());
                    a = New Object_3();
                    io.writeInt(a.method());
                }
                main() {
                    Var o: Object = New Program();
                    o.some_method();
                }
            }
        """
        expect = """123"""
        self.assertTrue(TestCodeGen.test(input, expect, 553)) 
    
    def test_054(self):
        input = r"""
            Class Animal {}
            Class Dog : Animal {}

            Class Program {
                $method(a: Animal) {
                    io.writeStr("OK");
                }
                main() {
                    Var a: Animal   = New Animal();
                    Var b: Animal   = New Dog();
                    Var c: Dog      = New Dog();
                    Program::$method(a);
                    Program::$method(b);
                    Program::$method(c);
                    Program::$method(New Animal());
                    Program::$method(New Dog());
                }
            }
        """
        expect = """OKOKOKOKOK"""
        self.assertTrue(TestCodeGen.test(input, expect, 554)) 
    
    def test_055(self):
        input = r"""
            Class Animal {}
            Class Dog : Animal {}

            Class Program {
                $method(a: Array[Int, 5]) {
                    Return a[0];
                }
                main() {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5);
                    io.writeInt(Program::$method(a));
                    io.writeInt(Program::$method(Array(1,2,3,4,5)));
                }
            }
        """
        expect = """11"""
        self.assertTrue(TestCodeGen.test(input, expect, 555)) 
    
    def test_056(self):
        input = r"""
            Class Animal {}
            Class Dog : Animal {}

            Class Program {
                $method(a: Array[Array[Int, 5], 2]) {
                    Return a[0][0];
                }
                main() {
                    Var a: Array[Array[Int, 5], 2] = Array(
                        Array(1,2,3,4,5), 
                        Array(6,7,8,9,10)
                    );
                    io.writeInt(Program::$method(a));
                    io.writeInt(Program::$method(Array(
                        Array(1,2,3,4,5), 
                        Array(6,7,8,9,10)
                    )));
                }
            }
        """
        expect = """11"""
        self.assertTrue(TestCodeGen.test(input, expect, 556)) 
    
    def test_057(self):
        input = r"""
            Class Program {
                Var a: Array[Int, 5] = Array(9,9,9,9,9);
                Var $a: Array[Int, 5] = Array(9,9,9,9,9);
                
                method(x: Array[Int, 5]) {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5);
                    Val b: Array[Int, 5] = Array(1,2,3,4,5);
                    Self.a = Array(1,2,3,4,5);
                    Program::$a = Array(1,2,3,4,5);
                    io.writeInt(x[0]);
                    io.writeInt(a[0]);
                    io.writeInt(b[0]);
                    io.writeInt(Self.a[0]);
                    io.writeInt(Program::$a[0]);
                }
                main() {    
                    Var d: Program = New Program();
                    d.method(Array(1,2,3,4,5));
                }
            }
        """
        expect = """11111"""
        self.assertTrue(TestCodeGen.test(input, expect, 557)) 
    
    def test_058(self):
        input = r"""
            Class Program {
                Var a: Array[Float, 5] = Array(9,9,9,9,9);
                Var $a: Array[Float, 5] = Array(9,9,9,9,9);
                
                method(x: Array[Float, 5]) {
                    Var a: Array[Float, 5] = Array(1,2,3,4,5);
                    Val b: Array[Float, 5] = Array(1,2,3,4,5);
                    Self.a = Array(1,2,3,4,5);
                    Program::$a = Array(1,2,3,4,5);
                    io.writeFloat(x[0]);
                    io.writeFloat(a[0]);
                    io.writeFloat(b[0]);
                    io.writeFloat(Self.a[0]);
                    io.writeFloat(Program::$a[0]);
                }
                main() {    
                    Var d: Program = New Program();
                    d.method(Array(1,2,3,4,5));
                }
            }
        """
        expect = """1.01.01.01.01.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 558)) 
    
    def test_059(self):
        input = r"""
            Class Program {
                Var a: Array[Array[Int,5], 2] = Array(
                    Array(9,9,9,9,9),
                    Array(9,9,9,9,9)
                );
                Var $a: Array[Array[Int,5], 2] = Array(
                    Array(9,9,9,9,9),
                    Array(9,9,9,9,9)
                );
                method(x: Array[Array[Int,5], 2]) {
                    Var a: Array[Array[Int,5], 2] = Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    );
                    Val b: Array[Array[Int,5], 2] = Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    );
                    Self.a = Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    );
                    Program::$a = Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    );
                    io.writeInt(x[0][0]);
                    io.writeInt(a[0][0]);
                    io.writeInt(b[0][0]);
                    io.writeInt(Self.a[0][0]);
                    io.writeInt(Program::$a[0][0]);
                }
                main() {    
                    Var d: Program = New Program();
                    d.method(Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    ));
                }
            }
        """
        expect = """11111"""
        self.assertTrue(TestCodeGen.test(input, expect, 559)) 
    def test_060(self):
        input = r"""
            Class Program {
                Var a: Array[Array[Float,5], 2] = Array(
                    Array(9,9,9,9,9),
                    Array(9,9,9,9,9)
                );
                Var $a: Array[Array[Float,5], 2] = Array(
                    Array(9,9,9,9,9),
                    Array(9,9,9,9,9)
                );
                method(x: Array[Array[Float,5], 2]) {
                    Var a: Array[Array[Float,5], 2] = Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    );
                    Val b: Array[Array[Float,5], 2] = Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    );
                    Self.a = Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    );
                    Program::$a = Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    );
                    io.writeFloat(x[0][0]);
                    io.writeFloat(a[0][0]);
                    io.writeFloat(b[0][0]);
                    io.writeFloat(Self.a[0][0]);
                    io.writeFloat(Program::$a[0][0]);
                }
                main() {    
                    Var d: Program = New Program();
                    d.method(Array(
                        Array(1,2,3,4,5),
                        Array(6,7,8,9,10)
                    ));
                }
            }
        """
        expect = """1.01.01.01.01.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    def test_061(self):
        input = r"""
            Class Program {
                Var a: Array[Array[Float,5], 2] = Array(
                    Array(9,9,9,9,9),
                    Array(9,9,9,9,9)
                );
                Var $a: Array[Array[Float,5], 2] = Array(
                    Array(9,9,9,9,9),
                    Array(9,9,9,9,9)
                );
                method(x: Array[Array[Float,5], 2]) {
                    Var a: Array[Array[Float,5], 2] = Array(
                        Array(11.1,2,3,4,5),
                        Array(6.0,7.5,8.1,9,10.2)
                    );
                    Val b: Array[Array[Float,5], 2] = Array(
                        Array(11.1,2,3,4,5),
                        Array(6.0,7.5,8.1,9,10.2)
                    );
                    Self.a = Array(
                        Array(11.1,2,3,4,5),
                        Array(6.0,7.5,8.1,9,10.2)
                    );
                    Program::$a = Array(
                        Array(11.1,2,3,4,5),
                        Array(6.0,7.5,8.1,9,10.2)
                    );
                    io.writeFloat(x[0][0]);
                    io.writeFloat(a[0][0]);
                    io.writeFloat(b[0][0]);
                    io.writeFloat(Self.a[0][0]);
                    io.writeFloat(Program::$a[0][0]);
                }
                main() {    
                    Var d: Program = New Program();
                    d.method(Array(
                        Array(11.1,2,3,4,5),
                        Array(6.0,7.5,8.1,9,10.2)
                    ));
                }
            }
        """
        expect = """11.111.111.111.111.1"""
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_062(self):
        input = r"""
            Class Program {
                main() {    
                    io.writeInt(Array(1,2,3,4)[0]);
                    io.writeFloat(Array(1,2,3,4)[0]);
                }
            }
        """
        expect = """11.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 562))
    
    def test_063(self):
        input = r"""
            Class Program {
                main() {    
                    io.writeInt(
                        Array(
                            Array(9,8,7,6,5),
                            Array(4,3,2,1,0)
                        )[0][0]
                    );
                    io.writeFloat(
                        Array(
                            Array(9,8,7,6,5),
                            Array(4,3,2,1,0)
                        )[0][0]
                    );
                }
            }
        """
        expect = """99.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 563))
    
    def test_064(self):
        input = r"""
            Class Program {
                method() {
                    Return Array(1,2,3,4,5);
                }
                main() {    
                    Var d: Program = New Program();
                    io.writeInt(d.method()[0]);
                    io.writeFloat(d.method()[0]);
                    Var a: Array[Int, 5] = d.method();
                    io.writeInt(a[0]);
                }
            }
        """
        expect = """11.01"""
        self.assertTrue(TestCodeGen.test(input, expect, 564))
    
    def test_065(self):
        input = r"""
            Class Program {
                method() {
                    Return Array(
                        Array(9,8,7,6,5),
                        Array(4,3,2,1,0)
                    );
                }
                main() {    
                    Var d: Program = New Program();
                    io.writeInt(d.method()[0][0]);
                    io.writeFloat(d.method()[0][0]);
                    Var a: Array[Int, 5] = d.method()[0];
                    io.writeInt(a[0]);
                    Var b: Array[Int, 5] = d.method()[1];
                    io.writeInt(b[0]);
                }
            }
        """
        expect = """99.094"""
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test_066(self):
        input = r"""
            Class Program {
                method(a: Array[Int, 5]) {
                    Return a;
                }
                main() {    
                    Var d: Program = New Program();
                    io.writeInt(d.method(d.method(Array(1,2,3,4,5)))[0]);
                    
                }
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    def test_067(self):
        input = r"""
            Class Program {
                main() {    
                    io.writeInt(
                        Array(
                            Array(
                                Array(1,2,3),
                                Array(1,2,3),
                                Array(1,2,3)
                            ),
                            Array(
                                Array(1,2,3),
                                Array(1,2,3),
                                Array(1,2,3)
                            )
                        )[0][0][0]
                    );
                }
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 567))
    
    def test_068(self):
        input = r"""
            Class Program {
                main() {    
                    Var a: Array[Int, 3] = Array(
                            Array(
                                Array(1,2,3),
                                Array(1,2,3),
                                Array(1,2,3)
                            ),
                            Array(
                                Array(1,2,3),
                                Array(1,2,3),
                                Array(1,2,3)
                            )
                        )[0][0];
                    io.writeInt(a[0]);
                }
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 568))
    
    def test_069(self):
        input = r"""
            Class Program {
                main() {    
                    Var a: Array[Array[Int, 3], 3] = Array(
                            Array(
                                Array(1,2,3),
                                Array(1,2,3),
                                Array(1,2,3)
                            ),
                            Array(
                                Array(1,2,3),
                                Array(1,2,3),
                                Array(1,2,3)
                            )
                        )[0];
                    io.writeInt(a[0][0]);
                }
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 569))
    
    
    def test_070(self):
        input = r"""
            Class Program {
                Var a: Array[Int, 5] = Array(1,2,3,4,5);
                Var $a: Array[Int, 5] = Array(1,2,3,4,5);
                method() {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5);
                    Var i: Int;
                    Foreach (i In 0 .. 4) {
                        a[i] = a[i] + Self.a[i] + Program::$a[i];
                        io.writeInt(a[i]);
                    }
                }
                main() {    
                    Var o: Program = New Program();
                    o.method();
                }
            }
        """
        expect = """3691215"""
        self.assertTrue(TestCodeGen.test(input, expect, 570))
    
    def test_071(self):
        input = r"""
            Class Program {
                Var a: Array[Int, 5] = Array(1,2,3,4,5);
                Var $a: Array[Int, 5] = Array(1,2,3,4,5);
                method() {
                    Var a: Array[Int, 5] = Array(1,2,3,4,5);
                    Var i: Int;
                    Foreach (i In 0 .. 4) {
                        a[i] = a[i] * Self.a[i] + Program::$a[i];
                        Self.a[i] = Self.a[i] * 2;
                        Program::$a[i] = Program::$a[i] % 2;
                        io.writeInt(a[i]);
                        io.writeInt(Self.a[i]);
                        io.writeInt(Program::$a[i]);
                    }
                }
                main() {    
                    Var o: Program = New Program();
                    o.method();
                }
            }
        """
        expect = """2216401261208030101"""
        self.assertTrue(TestCodeGen.test(input, expect, 571))
    
    def test_072(self):
        input = r"""
            Class Node {
                Var next: Node = Null;
                Var data: Int = 0;
                Constructor(next: Node; data: Int) {
                    Self.next = next;
                    Self.data = data;
                }
            }
            Class Linked_list {
                Var head: Node = Null;
                Var tail: Node = Null;
                Var size: Int = 0;
                insert(node: Node) {
                    If (Self.size == 0) {
                        Self.head = node;
                        Self.tail = node;
                        Self.size = Self.size + 1;
                    }
                    Else {
                        Self.tail.next = node;
                        Self.tail = node;
                        Self.size = Self.size + 1;
                    }
                }
                traverse() {
                    Var i: Int;
                    Var current: Node = Self.head;
                    Foreach (i In 1 .. Self.size) {
                        io.writeInt(current.data);
                        current = current.next;
                    }
                }
            }
            Class Program {
                main() {    
                    Var linked_list : Linked_list = New Linked_list();
                    Var i: Int;
                    Foreach (i In  1 .. 20) {
                        linked_list.insert(New Node(Null, i));
                    }
                    linked_list.traverse();
                }
            }
        """
        expect = """1234567891011121314151617181920"""
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    
    