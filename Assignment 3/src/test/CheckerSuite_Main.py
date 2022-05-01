import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_000_redeclare_variable(self):
        input = r"""
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Var x: Int = x;
                }
            }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_001_redeclare_variable_with_parameter(self):
        input = r"""
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Var a: Int = x;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_002_redeclare_variable_with_constant(self):
        input = r"""
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Val x, y : Int = 1, 2;
                    Var x: Int = a;
                }
            }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_003_redeclare_constant(self):
        input = r"""
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Val x, y : Int = 1, 1;                    
                    Val x: Int = 1;
                    
                }
            }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_004_redeclare_constant_with_param(self):
        input = r"""
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Val a: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_005_redeclare_constant_with_variable(self):
        input = r"""
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Val x: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input, expect, 405))
    


    def test_006_redeclare_attribute_same_type(self):
        input = r"""
            Class A {
                Val x, y: Int = 1, 1;
                Val x: Int = 1;
            }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_007_redeclare_attribute_different_type(self):
        input = r"""
            Class A {
                Val x, y: Int = 1, 1;
                Var x: Int = 1;
            }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_008_redeclare_attribute_with_method(self):
        input = r"""
            Class A {
                x() {}
                Val x, y: Int = 1, 1;
            }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_009_redeclare_class(self):
        input = r"""
            Class A {}
            Class A {}
        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_010_redeclare_method(self):
        input = r"""
            Class A {
                method() {}
                method() {}
            }
        """
        expect = "Redeclared Method: method"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_011_redeclare_method_with_attribute(self):
        input = r"""
            Class A {
                Var x: Int;
                x() {}
            }
        """
        expect = "Redeclared Method: x"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_012_redeclare_parameter(self):
        input = r"""
            Class A {
                method(a,a: Int) {}
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test_013_attribute_inheritance(self):
        input = r"""
            Class Object {
                Var a, b : Int = 1, 2;
            }
            Class A : Object {
                method() {
                    Var x, y : Int = Self.a, Self.b; ## OK ##
                    Var m, n : Int = m, n; 
                }
            }
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_014_multi_layer_inheritance(self):
        input = r"""
            Class A {
                Var a: Int  = 1;
            }
            Class B : A {
                Var b: Int = 1;
            }
            Class C: B {
                Var c: Int = 1;
                method() {
                    Var a_1, a_2, a_3 : Int = Self.a, Self.b, Self.c;
                    Var x_1 : Int = x;
                }
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_015_inheritance_undeclare_class(self):
        input = r"""
            Class A {
                Var x: Int = 1;
                method(x: Int) {}
            }
            Class B : A {
                Var a: A;
                method(x: A) {}
            }
            Class C: Object {}
        """
        expect = "Undeclared Class: Object"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_016_undeclare_indentifier(self):
        input = r"""
            Class A {
                Var x, y: Int = 1, 1;
                Var a, b: Int = Self.x, Self.y; 
                method(a,b: Int) {
                    Var x1 : Int = Self.x;
                    Var y1 : Int = Self.y;
                    Var a1 : Int = Self.a;
                    Var b1 : Int = Self.b;
                    Var c1 : Int = c;
                }
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_017_undeclare_attribute(self):
        input = r"""
            Class A {
                Var x, y: Int = 1, 1;
                Var a, b: Int = Self.x, Self.y;
                Var m, n: Int = p, q; 
                method(a,b: Int) {}
            }
        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_018_use_declaring_attribute_in_init(self):
        input = r"""
            Class Program {
                Var a: Int = a;
                main() {}
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_019_use_declaring_self_attribute_in_init(self):
        input = r"""
            Class Program {
                Var a: Int = Self.a;
                main() {}
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_020_access_field_directly(self):
        input = r"""
            Class Program {
                Var a : Int = 1;
                Var b : Int = Self.a; 
                Var c : Int = a;
                main() {}
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_021_no_entry_point_1(self):
        input = r"""
            Class Object {main() {}}
            Class ABC {
                main() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_022_no_entry_point_2(self):
        input = r"""
            Class Object {main(){}}
            Class Program {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_023_no_entry_point_3(self): 
        input = r"""
            Class Object {main(){}}
            Class Program {
                main(x: Int) {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_024_unary_op_1(self):
        input = r"""
            Class Program {
                Var x: Int = - True;
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_025_unary_op_2(self):
        input = r"""
            Class Program {
                Var x: Int = - "String";
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,StringLit(String))"
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_026_unary_op_3(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int = 1;
                    Var b: Int = - a;
                    Var c: Float = 1.2;
                    Var d: Float = - 1.2;
                    Var e: Float = - c;
                    Var x: Boolean = True;
                    Var y: Int = - x;
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_027_unary_op_4(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Class_type = New Class_type();
                    Var y: Int = - x;
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_028_unary_op_5(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Boolean = True;
                    Var y: Boolean = ! True;
                    Var z: Boolean = ! x;
                    Var m: Boolean = ! 1; 
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test_029_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 + 2;
                    Var y: Float = 1 + 1.2;
                    Var m: Int = x + 3;
                    Var n: Float = y + 1.2;
                    Var z: Float = x + y;
                    Var t: Int = m + x;
                    
                    Var a: String;
                    Var b: String = a +. "String";
                    Var c: String = a + "String";
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(String))"
        self.assertTrue(TestChecker.test(input, expect, 429))
    
    def test_030_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 - 2;
                    Var y: Float = 1 - 1.2;
                    Var m: Int = x - 3;
                    Var n: Float = y - 1.2;
                    Var z: Float = x - y;
                    Var t: Int = m - x;
                    
                    Var a: Int = 1 - True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_031_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 * 2;
                    Var y: Float = 1 * 1.2;
                    Var m: Int = x * 3;
                    Var n: Float = y * 1.2;
                    Var z: Float = x * y;
                    Var t: Int = m * x;
       
                    Var a: Int = 1 * True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_032_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 / 2;
                    Var y: Float = 1 / 1.2;
                    Var m: Int = x / 3;
                    Var n: Float = y / 1.2;
                    Var z: Float = x / y;
                    Var t: Int = m / x;
       
                    Var a: Int = 1 / True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_033_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    Var x: Int = 1 % 1;
                    Var y: Int = a % 1;
                    Var z: Int = a % b;

                    Var m: Int = 1 % 1.2;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(1),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_034_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var x: Int = True && False;
                    Var y: Int = True && a;
                    Var z: Int = a && b;

                    Var m: Int = 1 && True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_035_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var x: Int = True || False;
                    Var y: Int = True || a;
                    Var z: Int = a || b;

                    Var m: Int = 1 || True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_036_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a: String = "abc";
                    Var b: String = "abc";
                    Var c: String = "abc" +. "abc";
                    Var d: String = a +. "abc";
                    Var e: String = a +. b;

                    Var f: String = a +. 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_037_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a: String = "abc";
                    Var b: String = "abc";
                    Var c: Boolean = "abc" ==. "abc";
                    Var d: Boolean = a ==. "abc";
                    Var e: Boolean = a ==. b;

                    Var f: Boolean = a ==. 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 437))









