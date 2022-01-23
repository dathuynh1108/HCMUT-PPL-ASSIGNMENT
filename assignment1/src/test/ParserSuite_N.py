import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_some_relational_expressions(self):
        input = """
                Class Program {
                    
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var $x, $y, z : Int = 0, 0, 0;
                    
                    Constructor(a: Int; B: Float) {
                        $x = 10;
                        $y = 1000;
                        My1stCons = 5 + 2;
                        My2ndCons = (0b1101010 && 0b1101110);
                    }
                    
                    Destructor() {
                        $x = 0;
                        $y = 0;
                        My1stCons = 0;
                        My2ndCons = 0;
                    }
                    
                    test() {
                        If (-5 == 5) {##nothing##}
                        If (5 != 4) {##nothing##}
                        If (5 > 4) {##nothing##}
                        If (3 < 4) {##nothing##}
                        If (5 >= 4) {##nothing##}
                        If (3 <= 4) {##nothing##}
                        If (a == 5) {##nothing##}
                        If (a < 5) {##nothing##}
                        If (a > 5) {##nothing##}
                        If (a <= 5) {##nothing##}
                        If (a >= 5) {##nothing##}
                        If (a == xyz) {##nothing##}
                        If (a != $xyz) {##nothing##}
                        If (a > nhanvo) {##nothing##}
                        If (a < ldpv) {##nothing##}
                        If (a >= abc) {##nothing##}
                        If (a <= abc) {##nothing##}
                    }
                    
                    main() {
                        
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_some_arithmetic_expressions(self):
        input = """
                Class Program {
                    
                    Val a: Int = 130703100310 + -255255255255;
                    Val b: Int = -130703100310 - 255255255255;
                    Var m: Int =-130703100310 / 255255255255;
                    Var c: Int = 130703100310 % 255255255255;
                    Var d: Float = -130703100310.213e-10 + -255255255255.3e+10;
                    Var e: Float = 0.0000001e10 - -0.00000000000000008e-10;
                    Var f: Float = 99999.10e30 / -123456789.10e-20;
        
                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        
    def test_some_boolean_expressions(self):
        input = """
                Class Program {
                    
                    Val a: Int = 0b1111111111 && 0B1101010101;
                    Val b: Int = 0b1111111111 || 0B1101010101;
                    Var m: String = "First string compare with" ==. "Second string";
                    Var c: Int = 130703100310 % 255255255255;
                    Var d: Float = -130703100310.213e-10 + -255255255255.3e+10;
                    Var e: Float = 0.0000001e10 - -0.00000000000000008e-10;
                    Var f: Float = 99999.10e30 / -123456789.10e-20;
        
                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        If (!True) {
                            ##nothing##
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
        
    def test_string_expression(self):
        input = """
                Class Program {
                    
                    Val str1: String = "xyz";
                    Val str2: String = "double xyz";
                    Val a: String = str1 +. str2;
                    Var c: String =  "Nhan Vo Nguyen Thien" +. str2;
                    Var c: String =  str1 +. "Nhan Vo Nguyen Thien";
                    Var c: String =  "Nhan Vo Nguyen Thien" +. "LDPV";

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        
    def test_index_operator_expression(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];
                    Val str2: String = x[1][2];
                    Val a: String = x[1][2][3];
                    Var c: String =  x[1][2][3][4];
                    Var c: String =  arr[arr[arr[1]]];
                    Var c: String =  arr[arr[1]];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
        
    def test_statement_assignment(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];
                    Val str2: String = x[1][2];
                    Val a: String = x[1][2][3];
                    Var c: String =  x[1][2][3][4];
                    Var c: String =  arr[arr[arr[1]]];
                    Var c: String =  arr[arr[1]];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        a = 2;
                        abc = 2+5;
                        abc = (0b110101 && 0b1100100);
                        abc = (0b010101 || 0b1100100);
                        abc = "first string" + "second string";
                        abc = arr[1][2];
                        $abc = arr[arr[arr[1]]];
                        arr[2] = arr[arr[arr[1]]];
                        arr[arr[arr[arr[100]]]] = a.b;
                    }
                }
                """
        expect = "Error on line 19 col 34: 10101"
        self.assertTrue(TestParser.test(input,expect,206))
        
    def test_statement_if(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        If (a == 5) {##nothing##}
                        If (2+5 == 5) {##nothing##}
                        If (arr[arr[arr[arr[100]]]] == (0b110101 && 0B1100100)) {##nothing##}
                        If (True) {##nothing##}
                        If (!True && False && ( (a == 5) || (b == 6) ) ) {##nothing##}
                        
                        If (!True && False) { ##nothing## } Else {##nothing##}
                        
                        If (!True && False) { ##nothing## } 
                        Elseif (a == 5) {##nothing##}
                        Elseif (b == 6) {  }
                        Elseif (!False) {##nothing##}
                        Elseif (a < b) {##nothing##}
                        Elseif ($xyz >= 3) {##nothing##}
                        Elseif (ar[2] > 3) {##nothing##}
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
        
    def test_statement_if_2(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        If (!True && False) { ##nothing## } 
                        Else {
                            If (!True && False && ( (a == 5) || (b == 6) ) ) {##nothing##}
                        }
                        
                        If (!True && False) { ##nothing## } 
                        Elseif (a == 5) {
                            If (!True && False) { ##nothing## } 
                            Elseif (a == 5) {##nothing##}
                            Elseif (b == 6) {  }
                            Elseif (!False) {##nothing##}
                            Elseif (a < b) {##nothing##}
                            Elseif ($xyz >= 3) {##nothing##}
                            Elseif (ar[2] > 3) {##nothing##}    
                        }
                        Elseif (b == 6) {
                            If (!True && False) { ##nothing## } 
                            Elseif (a == 5) {##nothing##}
                            Elseif (b == 6) {  }
                            Elseif (!False) {##nothing##}
                            Elseif (a < b) {##nothing##}
                            Elseif ($xyz >= 3) {##nothing##}
                            Elseif (ar[2] > 3) {##nothing##}    
                        }
                        Else {
                            If (!True && False) { ##nothing## } 
                            Elseif (a == 5) {##nothing##}
                            Elseif (b == 6) { 
                                If (!True && False) { ##nothing## } 
                                Elseif (a == 5) {##nothing##}
                                Elseif (b == 6) {  }
                                Elseif (!False) {##nothing##}
                                Elseif (a < b) {##nothing##}
                                Elseif ($xyz >= 3) {##nothing##}
                                Elseif (ar[2] > 3) {##nothing##}
                            }
                            Elseif (!False) {##nothing##}
                            Elseif (a < b) {##nothing##}
                            Elseif ($xyz >= 3) {##nothing##}
                            Elseif (ar[2] > 3) {##nothing##}
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
        
    def test_statement_for_in(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        Foreach (i In 1 .. 100 By 2) {
                            If (!True && False) { ##nothing## } 
                            Elseif (a == 5) {##nothing##}
                            Elseif (b == 6) {  }
                            Elseif (!False) {##nothing##}
                            Elseif (a < b) {##nothing##}
                            Elseif ($xyz >= 3) {##nothing##}
                            Elseif (ar[2] > 3) {##nothing##}
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            a = a + 1;
                            b = b - 1;
                            arr[arr[arr[arr[100]]]] = a.b;
                        }
                        
                        Foreach (abc In (-123456 + -34231) .. 2) {
                            If ($abc == 4) {
                                Continue;
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test_statement_break(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        Foreach (i In 1 .. 100 By 2) {
                            If (!True && False) { Break; } 
                            Elseif (a == 5) { Break; }
                            Elseif (b == 6) {  }
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            Break;
                        }
                        
                        Foreach ($bc In (-123456 + -34231) .. 2) {
                            If ($abc == 4) {
                                Break;
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
        
    def test_statement_continue(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        Foreach (i In 1 .. 100 By 2) {
                            If (!True && False) { Continue; } 
                            Elseif (a == 5) { Break; }
                            Elseif (b == 6) {  }
                            Elseif (!False) {Continue;}
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            Continue;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
        
    def test_statement_return(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        Foreach (i In 1 .. 100 By 2) {
                            If (!True && False) { Continue; } 
                            Elseif (a == 5) { Break; }
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            If (x == (3*2--3)) {
                                Return "Nhan Vo";   
                            }
                        }
                        
                        Foreach (abc In (-123456 + -34231) .. 2) {
                            If ($abc == 4) {
                                Return;
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
        
    def test_some_class_declare(self):
        input = """Class Program {

                }
                \n"""
        input += """
                    Class NhanVo {
                        Constructor() {
                            Foreach (x In 5+2 .. 100*3) {
                                If (x == (3*2--3)) {
                                    Return "Nhan Vo";   
                                }
                            }
                        }
                        
                        Constructor(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            Foreach (i In 1 .. 100 By 2) {
                                If (!True && False) { Continue; } 
                                Elseif (a == 5) { Break; }
                                Elseif (b == 6) {  }
                                Elseif (!False) {Continue;}
                                Elseif (a < b) {##nothing##}
                                Elseif ($xyz >= 3) {##nothing##}
                                Elseif (ar[2] > 3) {##nothing##}
                            }      
                        }
                        
                        Destructor() {
                            If (a == b) {
                                If (c == d) {
                                    ##nothing##
                                }
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
        
    def test_some_class_declare_2(self):
        input = """
                    Class NhanVo {
                        
                        Constructor(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            Foreach (i In 1 .. 100 By 2) {
                                If (!True && False) { Continue; } 
                                Elseif (a == 5) { Break; }
                                Elseif (b == 6) {  }
                                Elseif (!False) {Continue;}
                                Elseif (a < b) {##nothing##}
                                Elseif ($xyz >= 3) {##nothing##}
                                Elseif (ar[2] > 3) {##nothing##}
                            }      
                        }
                        
                        Destructor(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            If (a == b) {
                                If (c == d) {
                                    ##nothing##
                                }
                            }
                        }
                    }
                """
        expect = "Error on line 16 col 35: a"
        self.assertTrue(TestParser.test(input,expect,214))
        
    def test_some_class_declare_3(self):
        input = """
                    Class NhanVo {
                        
                        Constructor(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            Foreach (i In 1 .. 100 By 2) {
                                If (!True && False) { Continue; } 
                                Elseif (a == 5) { Break; }
                                Elseif (b == 6) {  }
                                Elseif (!False) {Continue;}
                                Elseif (a < b) {##nothing##}
                                Elseif ($xyz >= 3) {##nothing##}
                                Elseif (ar[2] > 3) {##nothing##}
                            }      
                        }
                        
                        Destructor() {
                            If (a == b) {
                                If (c == d) {
                                    ##nothing##
                                }
                            }
                        }
                        
                        getElement(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            ##nothing##
                        }
                        
                        getIndex(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            If (a == b) {
                                If (c == d) {
                                    ##nothing##
                                }
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        
    def test_some_class_declare_4(self):
        input = """
                    Class Shape {
                        $getNumofShape( {
                            Return self.length;
                        }
                    }
                """
        expect = "Error on line 3 col 40: {"
        self.assertTrue(TestParser.test(input,expect,216))
        
    def test_some_array(self):
        input = """
                    Class Shape {
                        Var a: Float = 45;
                        Var b: Float = 45.67;
                        Var c: Array[Int, 5] = Array(1, 2, 3, 4, 5);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
        
    def test_some_multidimensional_array(self):
        input = """
                    Class Shape {
                        main() {
                            a = Array();
                            $b = Array (
                                    Array("Volvo", "22", "18"),
                                    Array("Saab", "5", "2"),
                                    Array("Land Rover", "17", "15")
                                );
                            arr[arr[arr[3+4]]] = Array (
                                    Array("Volvo", "22", "18"),
                                    Array("Saab", "5", "2"),
                                    Array("Land Rover", "17", "15")
                                );
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
        
    def test_some_member_access(self):
        input = """
                    Class Shape {
                        main() {
                            a = object.length;
                            c = Shape::$width;
                            d = obj.getLength("abcd", 12);
                            f = Shape::$getWidth();
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
        
    def test_simple_progeam(self):
        input = """
                    Class Shape {
                        Var a: Int;
                        Notmain() {
                            x = 4;
                        }
                    }
                    
                    Class _program {
                        main() {
                            Val x: Float;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
        
    def test_error_simple_program(self):
        input = """
                    Class Shape {
                        Var a: Int;
                        Notmain() {
                            x = 4;
                        }
                    }
                    
                    class _program {
                        main() {
                            Val x: Float;
                        }
                    }
                """
        expect = "Error on line 9 col 20: class"
        self.assertTrue(TestParser.test(input,expect,221))
        
    def test_some_define_method(self):
        input = """
                    Class Shape {
                        method1() {}
                        method2(a, b: Int; c: Array[Int, 5]) {}
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
        
    def test_some_error_declare_var(self):
        input = """
                    Class Shape {
                        method2() {
                            Var a: Int;
                        }
                        
                        method1() {
                            Var $a: Int;
                        }
                    }
                """
        expect = "Error on line 8 col 32: $a"
        self.assertTrue(TestParser.test(input,expect,223))
        
    def test_some_method_invoke(self):
        input = """
                    Class Shape {
                        method2() {
                            obj.method1();
                        }
                        
                        method1() {
                            obj.method2();
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
        
    def test_multidimensional_array_declare(self):
        input = """
                    Class Shape {
                        Var arr: Array[Array[Int, 3], 3] = Array (
                                                            Array (3,4,5),
                                                            Array (6,7,8),
                                                            Array (9,10,11)
                                                                );
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
        
    def test_error_keyword_Val(self):
        input = """
                    Class Shape {
                        main() {
                            val x: String = "Nhan vo";
                        }
                    }
                """
        expect = "Error on line 4 col 32: x"
        self.assertTrue(TestParser.test(input,expect,226))
        
    def test_unequal_vars_and_values(self):
        input = """
                    Class Shape {
                        Val x, y: Int = 4;
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 3 col 41: ;"
        self.assertTrue(TestParser.test(input,expect,227))
        
    def test_unequal_vars_and_values_2(self):
        input = """
                    Class Shape {
                        Val x, y, $a: Int = 4, 6, 7, 9;
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 3 col 51: ,"
        self.assertTrue(TestParser.test(input,expect,228))
        
    def test_unequal_vars_and_values_3(self):
        input = """
                    Class Shape {
                        Var a, b: Float = 10;
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 3 col 44: ;"
        self.assertTrue(TestParser.test(input,expect,229))
        
    def test_unequal_vars_and_values_4(self):
        input = """
                    Class Shape {
                        Var a, b: Float = 10.e10, 3.23;
                        Val $x, $y: String = "nhanvo", "nguyenthien", "blabla";
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 4 col 68: ,"
        self.assertTrue(TestParser.test(input,expect,230))
        
    def test_unequal_vars_and_values_5(self):
        input = """
                    Class Shape {
                        Var a, b: Float = 10.e10, 3.23;
                        Val $x, $y: String = "nhanvo", "nguyenthien", "blabla","xyz", "str1" + "str2";
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 4 col 68: ,"
        self.assertTrue(TestParser.test(input,expect,231))
    
    def test_valid_attribute_declare(self):
        input = """
                    Class Shape {
                        Var a, b: Float = 10.e10, 3.23;
                        Val $x, $y, $z: String = "nhanvo", "xyz", "str1" + "str2";
                        main() {
                            a = b;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
        
    def test_valid_attribute_declare_2(self):
        input = """
                    Class Shape {
                        Var x, $y, z: Boolean;
                        Var m, $n, p: Boolean = True, False, False;
                        main() {
                            a = b;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
        
    def test_valid_attribute_declare_3(self):
        input = """
                    Class Shape {
                        Var m: Array[Int, 5] = Array(1, 2, 3, 4, 5);
                        main() {
                            
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
        
    def test_valid_attribute_declare_4(self):
        input = """
                Class Shape {
                    Var m: Array[Array[Int, 3], 3] = Array (Array(1,2,3), Array(4,5,6), Array(8,9,10));
                    main() {
                        
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
        
    def test_class_inhertance(self):
        input = """
                    Class Shape {}
                    Class Triangle : Shape {}
                    Class Circle : Triangle {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
        
    def test_method_declare(self):
        input = """
                    Class Shape {
                        getLength() {
                            Return length;
                        }
                        
                        getShape(a, b, c, d: Int; str1, str2: String) {
                            Return str1 + str2;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
        
    def test_static_method_declare(self):
        input = """
                    Class Shape {
                        $getLength() {
                            Return $length;
                        }
                        
                        $getShape(a, b, c, d: Int; str1, str2: String) {
                            Return str1 + str2;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
        
    def test_wrong_declare_class(self):
        input = """
                    Class Shape {
                        main() {
                            a = "nhan" + "vo";
                        }
                        
                        Constructor() {}
                        Destructor() {}
                    };
                """
        expect = "Error on line 9 col 21: ;"
        self.assertTrue(TestParser.test(input,expect,239))
        
    def test_some_object_creation(self):
        input = """
                    Class Shape {
                        
                    }
                    
                    Class Program {
                        main() {
                            a = New Shape();
                            a = New Shape(a, "nhanvo", 12+5-12*23, 8/2);
                            a = New Shape(New Shape(12, 3));
                            a = New Shape(New Shape(New Shape(New Shape(New Shape(New Shape(12, 3))))));
                            a = New Shape(arr[arr[arr[1]]][2]);
                            a = New Shape(Shape.length, Shape.arr[arr[arr[2]]], obj.getLength(12, 3));
                            a = (New Shape())[arr[1]];
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
        
    def test_unary_operator(self):
        input = """
                    Class Program {
                        main() {
                            a = -4;
                            a = --4;
                            a = ---4;
                            a = !True;
                            a = !!True;
                            a = !!!True;
                            a = !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!True;
                            a = !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(True && False);
                            a = ------------ (12 + 5 * 3 - 6 + 3 / 14 - 7);
                            a =  !(12 + 5 * 3 - 6 + 3 / 14 - 7);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
        
    def test_variable_and_constant_declare(self):
        input = """
                    Class Program {
                        main() {
                            Var x: Int;
                            Var x: Int = 5;
                            Var x, y: Int = 5, 6;
                            Var x, y, z: Int = -5, ------------6, "nhanvo" + "vo" + "nguyen" + "thien";
                            Var x, y, z: Int = 5, 6, New Shape(New Shape(New Shape(New Shape(New Shape(New Shape(12, 3))))));
                            Var x: Array[Array[Int, 3], 3] = Array (Array(1,2,3), Array(4,5,6), Array(8,9,10));
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
        
    def test_invalid_variable_and_constant_declare(self):
        input = """
                    Class Program {
                        main() {
                            Var x: Float = 3.4, 5.6;
                        }
                    }
                """
        expect = "Error on line 4 col 46: ,"
        self.assertTrue(TestParser.test(input,expect,243))
        
    def test_invalid_variable_and_constant_declare_1(self):
        input = """
                    Class Program {
                        main() {
                            Var x, y, z, m, n, p: Float = 3.4, 5.6;
                        }
                    }
                """
        expect = "Error on line 4 col 66: ;"
        self.assertTrue(TestParser.test(input,expect,244))
        
    def test_invalid_variable_and_constant_declare_2(self):
        input = """
                    Class Program {
                        Var $x: Int = 5;
                        Var $y, $z: Float;
                        
                        main() {
                            Var $a: Int;
                        }
                    }
                """
        expect = "Error on line 7 col 32: $a"
        self.assertTrue(TestParser.test(input,expect,245))
        
    def test_invalid_variable_and_constant_declare_3(self):
        input = """
                    Class Program {
                        Var $x: Int = 5;
                        Var $y, $z: Float;
                        
                        main() {
                            Var a Int = 5;
                        }
                    }
                """
        expect = "Error on line 7 col 34: Int"
        self.assertTrue(TestParser.test(input,expect,246))
        
    def test_array_type_declare(self):
        input = """
                    Class Program {
                        Var x: Array[Int, 1000];
                        Var x: Array[Int, 0];
                        
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 4 col 42: 0"
        self.assertTrue(TestParser.test(input,expect,247))
        
    def test_some_method_declaration(self):
        input = """
                    Class Program {
                        
                        method(arr1, arr2: Array[Int, 5]; arr3: Array[Array[Int, 3], 3]) {
                            ## nothing ##
                        }
                        
                        main() {
                            ## nothing ##
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
        
    def test_array_type_declare_2(self):
        input = """
                    Class Program {
                        
                        method(arr1, arr2: Array[Int, 5]; arr3: Array[Array[Int, 3], 3]) {
                            Var newArr: Array[Float, 3] = Array (1.2, 4.3, 5.600);
                        }
                        
                        main() {
                            Var arr: Array[String, 0] = Array();
                        }
                    }
                """
        expect = "Error on line 9 col 51: 0"
        self.assertTrue(TestParser.test(input,expect,249))
        
    def test_program_no_class(self):
        input = """
                
                """
        expect = "Error on line 3 col 16: <EOF>"
        self.assertTrue(TestParser.test(input,expect,250))
        
    def test_multidimensional_array(self):
        input = """
                    Class Program {
                        Var a: Array[Int, 1] = Array(Array(Array(1,2,3)));
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
        
    def test_multiple_inheritance(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                    }
                    
                    Class Shape {
                        Constructor() {
                            Var x: String = "nhanvo" + "nguyenthien";
                        }
                    }
                    
                    Class Child : Program : Shape {
                        
                    }
                """
        expect = "Error on line 14 col 42: :"
        self.assertTrue(TestParser.test(input,expect,252))
        
    def test_instance_attribute_access(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            x = a.b;
                            x = New X().b;
                            x = (arr[1]).b;
                            x = Shape::$obj.b;
                            x = Shape::$obj.b;
                            x = a.func(a, b, "xyz").b;
                            x = a.func(a, b, "xyz").func2(a, b, "xyz").b;
                            x = a.func(a, b, "xyz").func2(a, b, "xyz").func3(a, b, "xyz").b;
                            x = Shape::$func(a, b, c).b;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
        
    def test_static_attribute_access(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            x = Shape::$attr;
                            x = Circle::$area;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
        
    def test_static_attribute_access_2(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            ## no chaining calling ##
                            x = Shape::$attr::$attr2;
                        }
                    }
                """
        expect = "Error on line 9 col 44: ::"
        self.assertTrue(TestParser.test(input,expect,255))
        
    def test_instance_method_invocation(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            x.func();
                            x.func(a, b, c, d, "nhanvo", 1+2, "str1" + "str2");
                            x.func(a, "nhanvo", 1+2, "str1" + "str2").func2(a, "nhanvo", 1+2, "str1" + "str2");
                            x.func(a, "nhanvo", 1+2, "str1" + "str2").func2(a, "nhanvo", 1+2, "str1" + "str2").func3(a, "nhanvo", 1+2, "str1" + "str2");
                            New X().func();
                            New X().func().func2();
                            (New X().func().objInClass).func2();
                            (Shape::$obj).func();
                            New X().c.func();
                            (arr[1]).c.func();
                            Shape::$obj.obj2.func();
                            obj.obj2.func();
                            ("str" + "str").func();     ## ???? ##
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
        
    def test_static_method_invocation(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            Shape::$getLength();
                            Shape::$getLength(a, b, "nhan", 1+2-3*4/5, arr[1]);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
        
    def test_invalid_static_method_invocation(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            Shape::getLength();
                            Shape::$getLength(a, b, "nhan", 1+2-3*4/5, arr[1]);
                        }
                    }
                """
        expect = "Error on line 8 col 35: getLength"
        self.assertTrue(TestParser.test(input,expect,258))
        
    def test_keyword_self(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            Return Self.length * Self.width;
                        }
                        
                        getArea() {
                            r = Self.getR();
                            area = pi * r * r;
                            Return area;
                        }
                        
                        getR() {
                            Return Self.r;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
        
    def test_keyword_self_2(self):
        ## Self not used with static attribute and static method ???
        input = """
                    Class Program {
                        Var $abc: Float = 12.0000;
                        
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        $getWidth(a, b: Int; c: Float) {
                            Return (a-b)*c;
                        }
                        
                        main() {
                            Self.garbage = Self.$abc;
                            Self.w = Self.$getWidth();
                            Return Self.$length * Self.$width;
                        }
                    }
                """
        expect = "Error on line 14 col 48: $abc"
        self.assertTrue(TestParser.test(input,expect,260))
    
    def test_method_invocation_statement(self):
        ## Self not used with static attribute and static method ???
        input = """
                    Class Program {
                        Var $abc: Float = 12.0000;
                        Var arr: Array[Int, 5] = Array (1, 2, 3, 4, 5);
                        Var length: Int = 0;
                        Val $width : Int = 0;
                        
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                            Return;
                        }
                        
                        getLength() {
                            Self.length = 12 - 5 + 5 / 7 * 6 - arr[1];
                            Return Self.length;
                        }
                        
                        $getWidth(a, b: Int; str: String) {
                            $width = 12 - 5 + 5 / 7 * 6 - arr[4];
                            Return $width;
                        }
                        
                        main() {
                            Var a: Int = getLength();   ## calling method inside class ##
                            Var b: Int = $getWidth(a, b, "nhan");   ## calling method inside class ##
                            Return a-b;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
        
    def test_method_invocation_statement_2(self):
        input = """
                    Class Program {
                        Var $abc: Float = 12.0000;
                        Var arr: Array[Int, 5] = Array (1, 2, 3, 4, 5);
                        Var length: Int = 0;
                        Val $width : Int = 0;
                        
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                            Return;
                        }
                        
                        getLength() {
                            Self.length = 12 - 5 + 5 / 7 * 6 - arr[1];
                            Return Self.length;
                        }
                        
                        $getWidth(a, b: Int; str: String) {
                            $width = 12 - 5 + 5 / 7 * 6 - arr[4];
                            Return $width;
                        }
                        
                        main() {
                            Var a: Int = getLength();   ## calling method inside class ##
                            Var b: Int = $getWidth(a, b, "nhan");   ## calling method inside class ##
                            Return a-b;
                        }
                    }
                    
                    Class Shape {
                        Var a: Int = 5;
                        
                        method1(a, b: Int) {
                            Var a: Program = New Program();
                            Var b: Int = a.getLength();
                            Var c: Int = Program::$getWidth(12, 3, some_string);
                            a.getLength();
                            Program::$getWidth(12, 3, some_string);
                            Return;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
        
    def test_sample_program(self):
        input = """
                    Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        
                        $getNumOfShape() {
                            Return $numOfShape;
                        }
                    }
                    
                    Class Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    
                    Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
        
    def test_invalid_multidimensional_array(self):
        input = """ 
                    Class Program {
                        Var arr: Array[Array[Int, 5], 5] = Array (
                                                            Array(1,2,3,4,54),
                                                            Array(1,2,3,4,55),
                                                            Array(1,2,3,4,56),
                                                            Array(1,2,3,4,57),
                                                            Array(1,2,3,4,58)
                                                                );
                        main() {
                            Var arr: Array[Array[Int, 5], 5] 
                                = Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                ),
                                Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                ),
                                Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                ),
                                Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                ),
                                Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                );
                        }
                    }
                """
        expect = "Error on line 18 col 33: ,"
        self.assertTrue(TestParser.test(input,expect,264))
        
    def test_multidimensional_array_more_than_two(self):
        input = """ 
                    Class Program {
                        Var arr: Array[Array[Int, 5], 5] = Array (
                                                            Array(1,2,3,4,54),
                                                            Array(1,2,3,4,55),
                                                            Array(1,2,3,4,56),
                                                            Array(1,2,3,4,57),
                                                            Array(1,2,3,4,58)
                                                                );
                        main() {
                            Var arr: Array[Array[Array[Int, 2], 1], 2] 
                                = Array (
                                    Array(
                                        Array(1,2)
                                    ),
                                    Array (
                                        Array(3,4)
                                    )
                                );
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
        
    def test_size_of_array_type(self):
        input = """ 
                    Class Program {
                        main() {
                            Var arr: Array[Int, 0b111];
                            Var arr: Array[Int, 0x123];
                            Var arr: Array[Int, 0xABCD];
                            Var arr: Array[Int, 0XEF099];
                            Var arr: Array[Int, 0123];
                            Var arr: Array[Int, 0456];
                            Var arr: Array[Int, 100];
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
        
    def test_invalid_size_of_array_type(self):
        input = """ 
                    Class Program {
                        main() {
                            Var arr: Array[Int, 0b0];
                        }
                    }
                """
        expect = "Error on line 4 col 48: 0b0"
        self.assertTrue(TestParser.test(input,expect,267))
        
    def test_invalid_size_of_array_type_2(self):
        input = """ 
                    Class Program {
                        main() {
                            Var arr: Array[Int, 0x0];
                        }
                    }
                """
        expect = "Error on line 4 col 48: 0x0"
        self.assertTrue(TestParser.test(input,expect,268))
        
    def test_invalid_size_of_array_type_3(self):
        input = """ 
                    Class Program {
                        main() {
                            Var arr: Array[Int, 00];
                        }
                    }
                """
        expect = "Error on line 4 col 48: 00"
        self.assertTrue(TestParser.test(input,expect,269))
        
    def test_combo_member_access_expression(self):
        input = """ 
                    Class Program {
                        Var x: Int;
                        
                        main() {
                            x = obj.attr;
                            x = obj.attr.attr;
                            x = obj.attr.attr.attr;
                            x = obj.attr.attr.attr.attr.attr.attr.attr.attr;
                            x = Shape::$attr;
                            x = Shape::$attr.attr;
                            x = Shape::$attr.attr.attr;
                            x = Shape::$attr.attr.attr.attr;
                            x = Shape::$attr.attr.attr.attr.attr;
                            x = Shape.func();
                            x = Shape.func().func2(m,n,p);
                            x = Shape.func().func2(m,n,p).func3(m,n,p,x,y,z,"string");
                            x = Shape.attr.func();
                            x = Shape.attr.func(x,y,z).func2(m,n,p);
                            x = Shape.attr.attr.func(m,n,p);
                            x = Shape.attr.attr.func(m,n,p).func(m,n,p);
                            x = Shape.func(m,n,p).attr;
                            x = Shape.func(m,n,p).attr.attr.attr.attr.attr;
                            x = Shape.func(m,n,p).func(m,n,p).attr;
                            x = Shape.func(m,n,p).func(m,n,p).attr.attr;
                            x = Shape.func(m,n,p).func(m,n,p).attr.attr.func(m,n,p);
                            x = Shape::$func().func(m,n,p);
                            x = Shape::$func().func(m,n,p).func(m,n,p);
                            x = Shape::$func().func(m,n,p).func(m,n,p).attr;
                            x = Shape::$func().func(m,n,p).func(m,n,p).attr.attr;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
        
    