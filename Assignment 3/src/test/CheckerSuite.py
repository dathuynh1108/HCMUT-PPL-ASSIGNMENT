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
                    Var x: Float = 1 / 2;
                    Var y: Float = 1 / 1.2;
                    Var m: Float = x / 3;
                    Var n: Float = y / 1.2;
                    Var z: Float = x / y;
                    Var t: Float = m / x;
       
                    Var a: Float = 1 / True;
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
                    Var x: Boolean = True && False;
                    Var y: Boolean = True && a;
                    Var z: Boolean = a && b;

                    Var m: Boolean = 1 && True;
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
                    Var x: Boolean = True || False;
                    Var y: Boolean = True || a;
                    Var z: Boolean = a || b;

                    Var m: Boolean = 1 || True;
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

    def test_038_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var c: Boolean = True == False;
                    Var d: Boolean = a == True;
                    Var e: Boolean = a == b;

                    Var f: Boolean = a == 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_039_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a_1: Boolean = True;
                    Var b_1: Boolean = False;
                    Var c_1: Boolean = True == False;
                    Var d_1: Boolean = a_1 == True;
                    Var e_1: Boolean = a_1 == b_1;

                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 == 1;
                    Var d_2: Boolean = a_2 == 1;
                    Var e_2: Boolean = a_2 == b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 == 1.2;
                    Var d_3: Boolean = a_3 == 1.2;
                    Var e_3: Boolean = a_3 == b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 == 1.2;
                    Var d_4: Boolean = a_4 == 1.2;
                    Var e_4: Boolean = a_4 == b_4;

                    Var f: Boolean = True == 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.2),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_040_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a_1: Boolean = True;
                    Var b_1: Boolean = False;
                    Var c_1: Boolean = True != False;
                    Var d_1: Boolean = a_1 != True;
                    Var e_1: Boolean = a_1 != b_1;

                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 != 1;
                    Var d_2: Boolean = a_2 != 1;
                    Var e_2: Boolean = a_2 != b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 != 1.2;
                    Var d_3: Boolean = a_3 != 1.2;
                    Var e_3: Boolean = a_3 != b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 != 1.2;
                    Var d_4: Boolean = a_4 != 1.2;
                    Var e_4: Boolean = a_4 != b_4;

                    Var f: Boolean = True != 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLit(1.2),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_041_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 > 1;
                    Var d_2: Boolean = a_2 > 1;
                    Var e_2: Boolean = a_2 > b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 > 1.2;
                    Var d_3: Boolean = a_3 > 1.2;
                    Var e_3: Boolean = a_3 > b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 > 1.2;
                    Var d_4: Boolean = a_4 > 1.2;
                    Var e_4: Boolean = a_4 > b_4;

                    Var f: Boolean = 1 > True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_042_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 >= 1;
                    Var d_2: Boolean = a_2 >= 1;
                    Var e_2: Boolean = a_2 >= b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 >= 1.2;
                    Var d_3: Boolean = a_3 >= 1.2;
                    Var e_3: Boolean = a_3 >= b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 >= 1.2;
                    Var d_4: Boolean = a_4 >= 1.2;
                    Var e_4: Boolean = a_4 >= b_4;

                    Var f: Boolean = 1 >= True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_043_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 < 1;
                    Var d_2: Boolean = a_2 < 1;
                    Var e_2: Boolean = a_2 < b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 < 1.2;
                    Var d_3: Boolean = a_3 < 1.2;
                    Var e_3: Boolean = a_3 < b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 < 1.2;
                    Var d_4: Boolean = a_4 < 1.2;
                    Var e_4: Boolean = a_4 < b_4;

                    Var f: Boolean = 1 < True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_044_binary_op(self):
        input = r"""
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 <= 1;
                    Var d_2: Boolean = a_2 <= 1;
                    Var e_2: Boolean = a_2 <= b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 <= 1.2;
                    Var d_3: Boolean = a_3 <= 1.2;
                    Var e_3: Boolean = a_3 <= b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 <= 1.2;
                    Var d_4: Boolean = a_4 <= 1.2;
                    Var e_4: Boolean = a_4 <= b_4;

                    Var f: Boolean = 1 <= True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_045_new_expression(self):
        input = r"""
            Class Object {}
            Class Program {
                main() {
                    Var o: Object = New Object();
                    Var e: Object = New E();
                }
            }
        """
        expect = "Undeclared Class: E"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_046_new_expression_with_constructor(self):
        input = r"""
            Class Object {
                Constructor() {}
            }
            Class Program {
                main() {
                    Var o: Object = New Object();
                    Var e: Object = New Object(1);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_047_new_expression_with_constructor_and_coercion(self):
        input = r"""
            Class Base {}
            Class Sub: Base {}
            Class Object {
                Constructor(x: Float; y: Base) {}
            }
            Class Program {
                main() {
                    Var o_1: Object = New Object(1.2, New Base());
                    Var o_2: Object = New Object(1.2, New Sub());
                    Var o_3: Object = New Object(1, New Base());
                    Var o_4: Object = New Object(1, New Sub());

                    Var o : Object = New Object(1, 1);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_048_new_expression_without_constructor(self):
        input = r"""
            Class Object {}
            Class Program {
                main() {
                    Var o_1: Object = New Object();
                    Var o_2: Object = New Object(1);
                }
            }
        """
        expect = "Undeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_049_default_constructor_and_user_define_constructor(self):
        input = r"""
            Class Object {
                Constructor(x: Int) {}
            }
            Class Program {
                main() {
                    Var a: Object = Null;
                    Var b: Object = New Object();
                    Var c: Object = New Object(1);
                    Var d: Object = New Object(1, 2);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_050_array_cell_simple(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Int, 3] = Array(1,2,3);
                    a[0] = 1;
                    a[1] = 2;
                    a[a[a[0]]] = 1;
                    a[0][0] = 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(0),IntLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_051_array_cell_complex(self):
        input = r"""
            Class Program {
                main() {
                    Var a_1: Array[Int, 3] = Array(1,2,3);
                    Var a_2: Array[Array[Int, 3], 3] = Array(
                                                                Array(1,2,3), 
                                                                Array(1,2,3), 
                                                                Array(1,2,3)
                                                            );
                    a_1 = Array(1,2,3);
                    a_1[0] = 1;
                    a_2 = Array(Array(1,2,3), Array(1,2,3), Array(1,2,3));
                    a_2[0] = Array(1,2,3);
                    a_2[0] = a_1;
                    a_2[0][0] = 1;
                    a_2[a_1[0]][a_1[0]] = 1;
                    a_2[a_2[0][0]][a_2[0][0]] = 1;
                    a_2[0][0][0] = 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a_2),[IntLit(0),IntLit(0),IntLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_052_array_cell_index_is_not_int(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Int, 3] = Array(1,2,3);
                    a[0] = 1;
                    a[1.2] = 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_053_array_cell_index_is_not_int_expression(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Array[Int, 3] = Array(1,2,3);
                    Var x: Int = 1;
                    Var y: Float = 1.2;
                    a[x] = 1;
                    a[x + y] = 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[BinaryOp(+,Id(x),Id(y))])"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_054_instance_field_access_with_self(self):
        input = r"""
            Class Program {
                Var a: Int = 1;
                Var b: Float = 1.2;
                method() {
                    Var a: Int = 1;
                    Var b: Float = 1.2;
                    a = a + Self.a;
                    b = b + Self.b;
                    Var c: String = Self.c;
                }
                main() {}
            }
        """
        expect = "Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_055_instance_field_access_with_id(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                Var b: Float = 1.2;
                Var c: Boolean = True;
                Var d: String = "abc";
            }
            Class Program : Object {
                main() {
                    Var o: Object = New Object();
                    Var a: Int = 1;
                    Var b: Float = 1.2;
                    Var c: Boolean = True;
                    Var d: String = "abc";
                    a = a + o.a;
                    b = b + o.b;
                    c = c == o.c;
                    d = d +. o.d;
                    a = a - o.e;
                }
            }
        """
        expect = "Undeclared Attribute: e"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_056_static_field_access_with_id(self):
        input = r"""
            Class Object {
                Var $a: Int = 1;
                Var $b: Float = 1.2;
                Var $c: Boolean = True;
                Var $d: String = "abc";
            }
            Class Program {
                main() {
                    Var o: Object = New Object();
                    Var a: Int = 1;
                    Var b: Float = 1.2;
                    Var c: Boolean = True;
                    Var d: String = "abc";
                    a = a + Object::$a;
                    b = b + Object::$b;
                    c = c == Object::$c;
                    d = d +. Object::$d;
                    a = a - Object::$e;
                }
            }
        """
        expect = "Undeclared Attribute: $e"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_057_inheritance_instance_field_access_with_id(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                Var b: Float = 1.2;
                Var c: Boolean = True;
                Var d: String = "abc";
            }

            Class Dog : Object {
                Var e: Int = 1;
            }

            Class Program : Dog {
                main() {
                    Var o: Dog = New Dog();
                    Var a: Int = 1;
                    Var b: Float = 1.2;
                    Var c: Boolean = True;
                    Var d: String = "abc";
                    a = a + o.a;
                    b = b + o.b;
                    c = c == o.c;
                    d = d +. o.d;
                    a = a - o.e;
                    a = a - o.f;
                }
            }
        """
        expect = "Undeclared Attribute: f"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_058_static_field_access_with_id(self):
        input = r"""
            Class Object {
                Var $a: Int = 1;
                Var $b: Float = 1.2;
                Var $c: Boolean = True;
                Var $d: String = "abc";
            }
            Class Dog : Object {
                Var $e: Int = 1;
            }
            Class Program {
                main() {
                    Var o: Dog = New Dog();
                    Var a: Int = 1;
                    Var b: Float = 1.2;
                    Var c: Boolean = True;
                    Var d: String = "abc";
                    a = a + Object::$a;
                    b = b + Object::$b;
                    c = c == Object::$c;
                    d = d +. Object::$d;
                    a = a - Dog::$e;
                    a = a - Dog::$f;
                }
            }
        """
        expect = "Undeclared Attribute: $f"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_059_long_instance_field_access_with_id(self):
        input = r"""
            Class Object_1 {
                Var a: Int = 1;
            }
            Class Object_2 : Object_1 {
                Var o_1: Object_1;
                Var o_2: Object_2;
            }

            Class Program : Object_2 {
                main() {
                    Var o_2 : Object_2 = New Object_2();
                    Var o_1 : Object_1;
                    o_2 = o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_2;
                    o_1 = o_2.o_1;
                    o_1 = o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_1;
                    
                    Var a: Int = 1;
                    a = o_2.o_1.a;
                    a = o_2.o_2.o_1.a;
                    a = o_2.o_2.o_2.o_1.a;
                    a = o_1.a;
                    a = o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_1.a;
                    a = o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_2.o_1.b;
                }
            }
        """
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_060_long_static_instance_field_access_with_id(self):
        input = r"""
            Class Object_1 {
                Var a: Int = 1;
            }
            Class Object_2 : Object_1 {
                Var o_1: Object_1;
                Var o_2: Object_2;
                Var $o_1: Object_1;
                Var $o_2: Object_2;
            }

            Class Program : Object_2 {
                main() {
                    Var o_1 : Object_1;
                    Var o_2 : Object_2;
                    o_1 = Object_2::$o_1;
                    o_2 = Object_2::$o_2;
                    o_1 = Object_2::$o_2.o_1;
                    o_1 = Object_2::$o_2.o_2.o_1;
                    o_1 = Object_2::$o_2.o_2.o_2.o_2.o_2.o_2.o_1;

                    Var a: Int = 1;
                    a = Object_2::$o_1.a;
                    a = Object_2::$o_2.o_2.o_2.o_2.o_2.o_2.o_1.a;
                    a = Object_2::$o_2.o_2.o_2.o_2.o_2.o_2.o_1.b;
                }
            }
        """
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_061_special_instance_field_access_object_same_as_a_classname_1(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
            }
            Class Object_2 {
                Var a: Int = 1;
            }
            Class Program : Object {
                main() {
                    Var Object: Object = New Object();
                    Var a: Int = 1;
                    
                    a = Object.a;       ## OK because of having a local variable "Object" ##
                    a = Object_2.a;     ## Fail because of NOT having a local variable "Object_2" and Object_2 is a classname ##
                }
            }
        """
        expect = "Illegal Member Access: FieldAccess(Id(Object_2),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_062_special_instance_field_access_object_same_as_a_classname_2(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
            }
            Class Program : Object {
                main() {
                    Var Object: Object = New Object();
                    Var a: Int = 1;
                    
                    a = Object.a;       ## OK because of having a local variable "Object" ##
                    a = Object_2.a;     ## Fail because of NOT having a local variable "Object_2" and Object_2 is NOT a classname ##
                }
            }
        """
        expect = "Undeclared Identifier: Object_2"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_063_special_staic_field_access_object_same_as_a_classname_1(self):
        input = r"""
            Class Object {
                Var $a: Int = 1;
            }
            Class Program : Object {
                main() {
                    Var Object: Object = New Object();
                    Var Object_2: Object = New Object();
                    Var a: Int = 1;
                    
                    a = Object::$a;       ## OK because of having a class "Object" ##
                    a = Object_2::$a;     ## Fail because of NOT having a class "Object_2" and Object_2 is a local variable ##
                }
            }
        """
        expect = "Illegal Member Access: FieldAccess(Id(Object_2),Id($a))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_064_special_staic_field_access_object_same_as_a_classname_1(self):
        input = r"""
            Class Object {
                Var $a: Int = 1;
            }
            Class Program : Object {
                main() {
                    Var Object: Object = New Object();
                    Var a: Int = 1;
                    
                    a = Object::$a;       ## OK because of having a class "Object" ##
                    a = Object_2::$a;     ## Fail because of NOT having a class "Object_2" and Object_2 is NOT a local variable ##
                }
            }
        """
        expect = "Undeclared Class: Object_2"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_065_self_call_expression(self):
        input = r"""
            Class Program {
                method() {
                    Return 1;
                }
                sub_main() {
                    Var a: Int = 1;
                    a = Self.method();
                    a = Self.method_1();
                }
                main() {}
            }
        """
        expect = "Undeclared Method: method_1"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_066_instance_method_call_expression_another_class(self):
        input = r"""
            Class Object {
                method() {
                    Return 1;
                }
            }
            Class Program {
                main() {
                    Var o: Object = New Object();
                    Var a: Int = 1;
                    a = o.method();
                    a = o.method_1();
                }
            }
        """
        expect = "Undeclared Method: method_1"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_067_instance_method_call_expression_another_class(self):
        input = r"""
            Class Object {
                $method() {
                    Return 1;
                }
            }
            Class Program {
                main() {
                    Var a: Int = 1;
                    a = Object::$method();
                    a = Object::$method_1();
                }
            }
        """
        expect = "Undeclared Method: $method_1"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_068_chain_of_instance_method_call_expression_another_class(self):
        input = r"""
            Class Object {
                Var a: Int;
                method() {
                    Return New Object();
                }
            }
            Class Inheritance_object : Object {
                main() {
                    Var o: Object = New Object();
                    o = o.method().method().method().method().method();
                    Var a: Int = 1;
                    a = o.method().method().a; ## OK because sub class can see "a" attribute of Object ##
                }
            }
            Class Program {
                main() {
                    Var o: Object = New Object();
                    o = o.method().method().method().method().method();
                    Var a: Int = 1;
                    a = o.method().method().a; ## Fail because Program class only see Object class's method ##
                }
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_069_chain_of_static_method_and_instance_method_call_expression_another_class(self):
        input = r"""
            Class Object {
                Var a: Int;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Inheritance_object : Object {
                main() {
                    Var a: Int;
                    Var o: Object = New Object();
                    o = Object::$o;
                    o = Object::$method();
                    o = Object::$method().method().method().method();
                    a = Object::$method().method().method().method().a; ## OK because sub class can see "a" attribute of Object ##
                }
            }
            Class Program {
                main() {
                    Var a: Int;
                    Var o: Object = New Object();
                    o = Object::$o;
                    o = Object::$method();
                    o = Object::$method().method().method().method();
                    a = Object::$method().method().method().method().a; ## Fail because Program class only see Object class's method ##
                }
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test_070_call_instance_method_as_attribute(self):
        input = r"""
            Class Object {
                Var a: Int;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Program : Object {
                main() {
                    Var o: Object = New Object();
                    o = o.method;
                }
            }
        """
        expect = "Undeclared Attribute: method"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test_071_call_staic_method_as_attribute(self):
        input = r"""
            Class Object {
                Var a: Int;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Program : Object {
                main() {
                    Var o: Object = New Object();
                    o = Object::$method;
                }
            }
        """
        expect = "Undeclared Attribute: $method"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_072_call_instance_attribute_as_method(self):
        input = r"""
            Class Object {
                Var a: Int;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Program : Object {
                main() {
                    Var o: Object = New Object();
                    o = o.a();
                }
            }
        """
        expect = "Undeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test_073_call_static_attribute_as_method(self):
        input = r"""
            Class Object {
                Var a: Int;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Program : Object {
                main() {
                    Var o: Object = New Object();
                    o = Object::$a();
                }
            }
        """
        expect = "Undeclared Method: $a"
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test_074_call_chain_of_field_access_and_call_expression_complex(self):
        input = r"""
            Class Object {
                Var a: Int;
                Var o: Object;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Object_1 : Object {
                Var a: Int;
                Var o_1: Object_1;
                Var $o_1: Object_1;
                method_1() {
                    Return New Object_1();
                }
                $method_1() {
                    Return New Object_1();
                }
            }
            Class Other_object {
                Var a: Int;
                Var o: Object;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Program : Object_1 {
                main() {
                    ## Program and Object can see attribute of Object ## 
                    Var o: Object = New Object();
                    o = o.o.o.o.o.method();
                    o = o.o.o.method().o.o.o;
                    o = o.o.o.method().o.o.o.method();
                    o = o.o.o.method().o.o.o.method().method().method();

                    o = Object::$o;
                    o = Object::$o.o.o.o.method().method();
                    o = Object::$o.o.o.o.method().method().o.o.o;
                    o = Object::$o.o.o.o.method().method().o.o.o.method();
                    o = Object::$method();
                    
                    ## Program : Object_1 : Object --> It can see attribute of itself, Object_1, and Object ##

                    ## Attribute of Object ##
                    o = Object_1::$o;
                    o = Object_1::$o.o.o;
                    o = Object_1::$o.method();
                    o = Object_1::$o.o.o.method().method();
                    o = Object_1::$method();
                    o = Object_1::$method().o.o.o;
                    o = Object_1::$method().o.o.o.method();

                    ## Attribute of Object_1 ##
                    o = Object_1::$o_1;
                    o = Object_1::$o_1.o_1.o_1;
                    o = Object_1::$o_1.method_1();
                    o = Object_1::$o_1.o_1.o_1.method_1().method_1();
                    o = Object_1::$method_1();
                    o = Object_1::$method_1().o_1.o_1.o_1;
                    o = Object_1::$method_1().o_1.o_1.o_1.method_1().method_1();
                    
                    ## Mix ##
                    ## OK, Program see Object_1, Object attribute ##
                    Var o_1: Object_1 = New Object_1();
                    o = o_1.o.o.o.o.o.method();     
                    o = o_1.o_1.o.o.o.o.method();   
                    o = o_1.o.o.o.o.o.method().o.o.o;
                    o = o_1.o.o.o.o.o.method().o.o.o.method();
                    o = o_1.o.o.o.o.o.method().o.o.o.method().method().method();

                    o = o_1.o_1.o_1.o_1.o.o.o.method();
                    o = o_1.o_1.o_1.method_1().method_1();
                    o = o_1.o_1.o_1.method_1().o.o.method();                                        
                                    
                    o = Object_1::$o_1.o;
                    o = Object_1::$o_1.o_1.o;
                    o = Object_1::$o_1.o_1.method_1().method_1().method();
                    o = Object_1::$o_1.o_1.method_1().method_1().o.o.method().method();
                    o = Object_1::$o_1.o_1.method_1().method_1().o_1.o_1.method_1().method_1().method();
                    
                    Var o_o: Other_object = New Other_object();
                    ## OK, Program can see Other_object's method and Object's attribute##
                    o = o_o.method().method();      
                    o = o_o.method().method().o.o.o;
                    o = o_o.method().method().o.o.o.method().method();

                    o = o_o.o.method();             ## Fail, Program can's see Other_object's attribute ##                 
                }
            }
        """
        expect = "Undeclared Attribute: o"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_075_use_self_in_static_method(self):
        input = r"""
            Class Object {
                Var a: Int;
            }
            Class Program : Object {
                main() {
                    Var a: Int = 1;
                    a = Self.a;
                }
            }
        """
        expect = "Illegal Member Access: FieldAccess(Self(),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_076_call_self_void_method_as_call_expression(self):
        input = r"""
            Class Object {
                Var a: Int;
                method_int() {
                    Return Self.a;
                }
                method_void() {
                    Return;
                }
            }
            Class Program : Object {
                sub_main() {
                    Var a: Int = 1;
                    a = Self.method_int();
                    a = Self.method_void();
                }
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(method_void),[])"
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test_077_call_instance_void_method_as_call_expression(self):
        input = r"""
            Class Object {
                Var a: Int;
                method_int() {
                    Return Self.a;
                }
                method_void() {
                    Return;
                }
            }
            Class Program : Object {
                sub_main() {
                    Var o : Object = New Object();
                    Var a: Int = 1;
                    a = o.method_int();
                    a = o.method_void();
                }
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(o),Id(method_void),[])"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_078_call_staiic_void_method_as_call_expression(self):
        input = r"""
            Class Object {
                Var $a: Int;
                $method_int() {
                    Return Object::$a;
                }
                $method_void() {
                    Return;
                }
            }
            Class Program : Object {
                sub_main() {
                    Var a: Int = 1;
                    a = Object::$method_int();
                    a = Object::$method_void();
                }
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(Object),Id($method_void),[])"
        self.assertTrue(TestChecker.test(input, expect, 478))



