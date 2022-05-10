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
        expect = "No Entry Point"
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
        expect = "No Entry Point"
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
        expect = "Undeclared Attribute: a"
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
        expect = "Undeclared Attribute: a"
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
            Class Program {
                main(x: Int) {}
                main() {}
            }
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
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[FloatLit(1.2),NewExpr(Id(Sub),[])])"
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
                    a = a - o.e;
                    a = a + o.a;
                    b = b + o.b;
                    c = c == o.c;
                    d = d +. o.d;
                }
            }
        """
        expect = "Undeclared Attribute: a"
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
                    a = o.method().method().a; 
                    a = o.method().method().b;
                }
            }
        """
        expect = "Undeclared Attribute: b"
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
                    a = Object::$method().method().method().method().a; 
                    a = Object::$method().method().method().method().b; 
                }
            }
        """
        expect = "Undeclared Attribute: b"
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

                    ##
                    o = Object_1::$o;
                    o = Object_1::$o.o.o.o.method().method();
                    o = Object_1::$o.o.o.o.method().method().o.o.o;
                    o = Object_1::$o.o.o.o.method().method().o.o.o.method();
                    o = Object_1::$method();

                    o = Program::$o;
                    o = Program::$o.o.o.o.method().method();
                    o = Program::$o.o.o.o.method().method().o.o.o;
                    o = Program::$o.o.o.o.method().method().o.o.o.method();
                    o = Program::$method();
                    ##
                    ## Program : Object_1 : Object --> It can see attribute of itself, Object_1, and Object ##

                    ## Attribute of Object ##
                    o = Object::$o;
                    o = Object::$o.o.o;
                    o = Object::$o.method();
                    o = Object::$o.o.o.method().method();
                    o = Object::$method();
                    o = Object::$method().o.o.o;
                    o = Object::$method().o.o.o.method();

                    ## Attribute of Object_1 ##
                    ##
                    o = Object_1::$o_1;
                    o = Object_1::$o_1.o_1.o_1;
                    o = Object_1::$o_1.method_1();
                    o = Object_1::$o_1.o_1.o_1.method_1().method_1();
                    o = Object_1::$method_1();
                    o = Object_1::$method_1().o_1.o_1.o_1;
                    o = Object_1::$method_1().o_1.o_1.o_1.method_1().method_1();
                    ##
                    ## Attribute of Program ##
                    ##
                    o = Program::$o;
                    o = Program::$o.o.o;
                    o = Program::$o.method();
                    o = Program::$o.o.o.method().method();
                    o = Program::$method();
                    o = Program::$method().o.o.o;
                    o = Program::$method().o.o.o.method();
                    o = Program::$o_1;
                    o = Program::$o_1.o_1.o_1;
                    o = Program::$o_1.method_1();
                    o = Program::$o_1.o_1.o_1.method_1().method_1();
                    o = Program::$method_1();
                    o = Program::$method_1().o_1.o_1.o_1;
                    o = Program::$method_1().o_1.o_1.o_1.method_1().method_1();
                    ##
                    
                    
                    
                    ## Mix ##
                    ## OK, Program see Object_1, Object attribute ##
                    ##
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
                    o = Program::$o_1.o;
                    o = Program::$o_1.o_1.o;
                    o = Program::$o_1.o_1.method_1().method_1().method();
                    o = Program::$o_1.o_1.method_1().method_1().o.o.method().method();
                    o = Program::$o_1.o_1.method_1().method_1().o_1.o_1.method_1().method_1().method();
                    ##
                    Var o_o: Other_object = New Other_object();
                    ## OK, Program can see Other_object's method and Object's attribute##
                    o = o_o.method().method();      
                    o = o_o.method().method().o.o.o;
                    o = o_o.method().method().o.o.o.method().method();

                    o = o_o.o.method();      
                    ## Test inheritance ##
                    Var o_1: Object_1 = New Object_1();
                    o = o_1.o.o.o.o.o.method();                   
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
                Var x: Int = 1;
                main() {
                    Var a: Int = 1;
                    a = Self.x;
                }
                $method() {
                    Var a: Int = 1;
                    a = Self.x;
                }
            }
        """
        expect = "Illegal Member Access: FieldAccess(Self(),Id(x))"
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
                Var a: Int;
                method_int() {
                    Return Self.a;
                }
                method_void() {
                    Return;
                }
                main() {
                    Var a: Int = 1;
                    a = Self.method_int();
                    a = Self.method_void();
                }
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
            Class Program {
                main() {
                    Var o : Object = New Object();
                    Var a: Int = 1;
                    a = o.method_int();
                    a = o.method_void();
                }
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

    def test_079_assign_statement(self):
        input = r"""
            Class Object {}
            Class Program : Object {
                main() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    b = a;

                    Var c: Float = 1.2;
                    Var d: Float = 1.2;
                    d = c;

                    Var e: Boolean = True;
                    Var f: Boolean = False;
                    f = e;

                    Var g: String = "abc";
                    Var h: String = "abc";
                    h = g;

                    d = a;
                    a = e;
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_080_assign_statement_with_coercion(self):
        input = r"""
            Class Object {}
            Class Object_1 : Object {}
            Class Program  {
                main() {
                    Var i : Int = 1;
                    Var j: Float = 1;
                    Var f: Float = 1.2;
                    f = i; 
                    
                    Var o : Object = New Object();
                    Var o_1: Object_1 = New Object_1();
                    o = Null;
                    o_1 = Null;
                    o = o_1;

                    o_1 = o;
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(o),Id(o_1))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_081_assign_statement_with_coercion_for_array(self):
        input = r"""
            Class Object {}
            Class Object_1 : Object {}
            Class Program  {
                main() {
                    Var a_i: Array[Int, 5];
                    Var a_f: Array[Float, 5];
                    a_f = a_i;
                    a_i = Array(1,2,3,4,5);
                    a_f = Array(1,2,3,4,5);

                    a_i = Array(1,2,3);
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a_i),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_082_assign_statement_with_coercion_for_array(self):
        input = r"""
            Class Object {}
            Class Object_1 : Object {}
            Class Program  {
                main() {
                    Var a_i: Array[Int, 5];
                    Var a_f: Array[Float, 5];
                    a_f = a_i;

                    Var a_i_i : Array[Array[Int, 5], 5];
                    Var a_f_f : Array[Array[Float, 5], 5];
                    a_f_f = a_i_i;

                    a_i = Array(1, 2, 3, 4, 5);
                    a_f = Array(1.1, 2.2, 3.3, 4.4, 5.5);
                    a_f = Array(1, 2, 3, 4, 5);

                    a_i_i = Array(
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5)
                    );
                    a_f_f = Array(
                        Array(1.1,2.2,3.3,4.4,5.5),
                        Array(1.1,2.2,3.3,4.4,5.5),
                        Array(1.1,2.2,3.3,4.4,5.5),
                        Array(1.1,2.2,3.3,4.4,5.5),
                        Array(1.1,2.2,3.3,4.4,5.5)
                    );
                    a_f_f = Array(
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5),
                        Array(1,2,3,4,5)
                    );
                    
                    a_i_i = a_f_f;
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a_i_i),Id(a_f_f))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_083_block(self):
        input = r"""
            Class Program  {
                main() {
                    Var a: Int = 1;
                    {
                        Var a: Int = 1;
                        {
                            Var a: Int = 1;
                        }
                    }
                    Var x: Int = 1;
                    Val x: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input, expect, 483)) 
    
    def test_084_if_statement(self):
        input = r"""
            Class Program  {
                main() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    Var c: Float = 1.2;
                    Var d: Float = 1.2;
                    Var x: Boolean = True;
                    Var y: Boolean = False;
                    
                    If (True) {}
                    If (x) {} Else {}
                    If (x == y) {}
                    If (x != y) {}
                    If (x && y) {}
                    If (x || y) {}
                    
                    If (a == b) {}   
                    If (a != b) {}   
                    If (a > b) {}   
                    If (a >= b) {}  
                    If (a < b) {}   
                    If (a <= b) {}  
                    
                    If (c > d) {}   
                    If (c >= d) {}  
                    If (c < d) {}   
                    If (c <= d) {}    

                    Var n: Int = 1;
                    If (True) {
                        Var n: Int = 1; 
                        If (True) {
                            Var n: Int = 1;
                        }
                        Else {
                            Var n: Int = 1;
                        }
                    }
                    Else {
                        Var n: Int = 1;
                    }

                    If (a) {}
                }
            }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_085_if_statement(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                Var $a: Int = 1;
                method() {Return 1;}
                main() {
                    Var a: Int = 1;
                    Foreach (a In Self.a .. Self.method() By Object::$a) {}
                }
            }
            Class Program  {
                Var $a: Int = 1;
                $method() {Return 1;}
                main() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    Var c: Int = 1;
                    Var d: Int = 1;
                    
                    Foreach(a In 1 .. 100) {}
                    Foreach(a In 1 .. 100 By 2) {}
                    Foreach(a In b .. c) {}
                    Foreach(a In b .. c By d) {}
                    Foreach(a In b + c + d .. b * c * d By b - c - d) {}
                    Foreach(a In b % c % d .. Program::$method() By Program::$a) {}

                    Foreach(a In 1 .. 100) {
                        Var a: Int = 1;
                        Foreach(a In 1 .. 100) {
                            Var a: Int = 1;
                        }
                    }

                    Foreach (a In 1.2 .. 1.3 By 1.4) {}
                }
            }
        """
        expect = "Type Mismatch In Statement: For(Id(a),FloatLit(1.2),FloatLit(1.3),FloatLit(1.4),Block([])])"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_086_for_statement_with_constant(self):
        input = r"""
            Class Program {
                main() {
                    Val a: Int = 1;
                    Foreach(a In 1 .. 100) {}
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_087_break_statement(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    Foreach(a In 1 .. 100) {
                        Break;
                        {Break;}
                        If (True) {Break;}
                        Foreach(a In 1 .. 100) {
                            Break;
                            {Break;}
                            If (True) {Break;}
                        }
                        Break;
                    }
                    Break;
                }
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test_088_continue_statement(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    Foreach(a In 1 .. 100) {
                        Continue;
                        {Continue;}
                        If (True) {Continue;}
                        Foreach(a In 1 .. 100) {
                            Continue;
                            {Continue;}
                            If (True) {Continue;}
                        }
                        Continue;
                    }
                    Continue;
                }
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 488))
    
    def test_089_return_statement(self):
        input = r"""
            Class Program {
                Var a: Int = 1;
                Var $a: Int = 1;
                $method() {Return 1;}
                method() {
                    Var a: Int = 1;
                    Return 1;
                    Return a;
                    Return Self.a;
                    Return a + 1 * Self.a;
                    Return a + 1 * Self.a % Program::$a;
                    Return a + 1 * Self.a % Program::$a - Program::$method();
                    Return a + 1 * Self.a % Program::$a - Program::$method() + 1.2;
                }
                main() {}
            }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,BinaryOp(-,BinaryOp(+,Id(a),BinaryOp(%,BinaryOp(*,IntLit(1),FieldAccess(Self(),Id(a))),FieldAccess(Id(Program),Id($a)))),CallExpr(Id(Program),Id($method),[])),FloatLit(1.2)))"
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test_090_check_param_type(self):
        input = r"""
            Class Object {
                Var a: Int = 1;
                Var b: Int = 1;
                Constructor(a,b : Int) {}
                method(a,b: Int) {
                    Var o : Object = New Object(Self.a, Self.b);
                    o = New Object(1, 1);
                    o = New Object(1 + 1 - 1 *  1, 1 % 1);
                    o = New Object(Self.a + Self.b - a - b, Self.a * Self.b % a % b);
                    Return o;
                }
                method_float(a,b: Float) {
                    Return a + b;
                }
            }
            Class Animal : Object {}
            Class Dog : Animal {}
            Class Program : Object {
                Var a: Int = 1;
                Var b: Int = 1;
                Constructor(a,b : Int) {}
                method(a,b: Int) {
                    Var o : Object = New Object(Self.a, Self.b);
                    o = New Object(1, 1);
                    o = New Object(1 + 1 - 1 *  1, 1 % 1);
                    o = New Object(Self.a + Self.b - a - b, Self.a * Self.b % a % b);
                    Return o;
                }
                method_float(a,b: Float) {
                    Return a + b;
                }
                some_method() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    Var o : Object = New Object(a,b);
                    o = Self.method(a,b);
                    o = Self.method(1,1);
                    o = Self.method(a + b, a - b);
                    o = Self.method(a + 1, b - 1);
                    o = Self.method(1 + 1, 1 - 1);
                    Var x: Float = Self.method_float(a, b);
                    x = Self.method_float(a + b, a - b);
                    Return Self.method_float(1, 1.2);
                }
                object_method(d_1, d_2: Object) {
                    Return 1;
                }
                test_method () {
                    Var a: Float = Self.some_method();
                    Var b: Int = 1;
                    b = Self.object_method(New Object(1,1), New Object());
                    b = Self.object_method(New Animal(), New Animal());
                    b = Self.object_method(New Dog(), New Dog());
                    Var d_1, d_2 : Animal = New Dog(), New Animal();
                    b = Self.object_method(d_1, d_2);
    
                    b = Self.some_method(); ## Fail ##
                }
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(object_method),[NewExpr(Id(Animal),[]),NewExpr(Id(Animal),[])])"
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test_091_check_default_constructor(self):
        input = r"""
            Class Object {
                Constructor(x: Int) {}
            }
            Class Program {
                main() {
                    Var x: Object;
                    x = New Object();
                    x = New Object(1);
                    x = New Object(1,2);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test_092_call_statement(self):
        input = r"""
            Class Object {
                Var o : Object;
                Var $o : Object;
                method() {
                    Return;
                }
                $method() {
                    Return;
                }
                method_o() {
                    Return New Object();
                }
                $method_o() {
                    Return New Object();
                }
            }
            Class Object_1 : Object {
                Var o_1 : Object_1;
                Var $o_1 : Object_1;
                method_1() {
                    Return;
                }
                $method_1() {
                    Return;
                }

                method_o_1() {
                    Return New Object_1();
                }
                $method_o_1() {
                    Return New Object_1();
                }
            }
            Class Program : Object_1 {
                main() {
                    Self.method_1();
                    Self.method();
                    Program::$method();
                    Program::$method_1();
                    Self.method_o().method();
                    Self.method_o_1().method();
                    Self.method_o_1().o_1.method();
                    Self.method_o_1().o.method_o().o.method();
                    Self.method_o_1().o_1.method_o_1().method_o().method();
                    Program::$method_o().method();
                    Program::$method_o().method_o().method_o().method();
                    Program::$method_o_1().o_1.method_o_1().o_1.method_o_1().method();
                    Program::$method_o_1().o_1.method_o_1().o_1.method_o_1().method_1();
                    Program::$method_o_1().o_1.method_o_1().o_1.method_o_1().o.method_o().o.method_o().method();

                    Program::$method_o_1().o_1.method_o_1().o_1.method_o_1().o.method_o().o.method_o().method_1(); ## Fail ##
                }
            }
        """
        expect = "Undeclared Method: method_1"
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test_093_use_attribute_as_call_statement(self):
        input = r"""
            Class Object {
                Var o : Object;
                Var $o : Object;
                method() {
                    Return;
                }
                $method() {
                    Return;
                }
                method_o() {
                    Return New Object();
                }
                $method_o() {
                    Return New Object();
                }
            }
            Class Program : Object {
                main() {
                    Self.o();
                }
            }
        """
        expect = "Undeclared Method: o"
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test_094_call_statement_non_void_type(self):
        input = r"""
            Class Object {
                Var o : Object;
                Var $o : Object;
                method() {
                    Return 1;
                }
            }

            Class Program : Object {
                Var o : Object;
                Var $o : Object;
                method() {
                    Return 1;
                }
                main() {
                    Self.method();
                }
            }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(method),[])"
        self.assertTrue(TestChecker.test(input, expect, 494))
    
    def test_095_null_as_parameter(self):
        input = r"""

            Class Object {
                Constructor(x: Object) {}
            }
            Class Object_1 : Object {}
            Class Program {
                method(x,y: Object) {
                    Return 1;
                }

                main() {
                    Var x: Int = Self.method(New Object(), New Object());
                    x = Self.method(Null, Null);
                    x = Self.method(New Object(New Object()), New Object(Null));
                    x = Self.method(New Object(New Object(New Object())), New Object(New Object(Null)));
                    x = Self.method(New Object_1(), Null);
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(method),[NewExpr(Id(Object_1),[]),NullLiteral()])"
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test_096_illegal_constant_expression(self):
        input = r"""
            Class Program {
                main() {
                    Val x: Int = 1;
                    Var y: Int = 1;
                    Var z: Int = x + y;
                    Val const: Int = x + y + z;
                }
            }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,BinaryOp(+,Id(x),Id(y)),Id(z))"
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test_097_illegal_constant_expression_for_call_expression(self):
        input = r"""
            Class Program {
                method_val() {
                    Return 1;
                }
                method_var() {
                    Var a: Int = 1;
                    Return a + 1;
                }
                main() {
                    Val x: Int = Self.method_val();
                    Val y: Int = Self.method_var();

                }
            }
        """
        expect = "Illegal Constant Expression: CallExpr(Self(),Id(method_var),[])"
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test_098_special_case_const_array(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int = 1;
                    Val x: Array[Int, 5] = Array(1, 2, 3, 4, 5);
                    Val y: Array[Int, 5] = Array(a, a, a, a, a);
                    Val z: Array[Int, 5] = Array(x[0], y[0], x[0], y[0], x[0]);
                    Val t: Array[Array[Int ,3], 2] = Array(Array(1,2,1.2), Array(1,2,3)); ## Throw which array??? ##
                }
            }
        """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(1.2)]"
        self.assertTrue(TestChecker.test(input, expect, 498))
    
    def test_099_elseif_statement_fail(self):
        input = r"""
            Class Program {
                main() {
                    If (True) {}
                    Elseif (True) {
                        If (True) {}
                        Elseif (1) {}
                        Else {}
                    }
                    Else {}  
                }
            }
        """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(1.2)]"
        self.assertTrue(TestChecker.test(input, expect, 499))


    


    
    
    
    
