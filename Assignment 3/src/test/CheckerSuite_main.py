import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_000_redeclare_variable(self):
        input = r"""
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = x, y;
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
                    Var x, y : Int = x, y;
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
                    Val x, y : Int = x, y;
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
                    Val x, y : Int = x, y;
                    Val a: Int = x;
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_004_redeclare_constant_with_param(self):
        input = r"""
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Val x, y : Int = x, y;
                    Val a: Int = a;
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
                    Var x, y : Int = x, y;
                    Val x: Int = a;
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
                    Var x, y : Int = a, b; ## OK ##
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
                    Var a_1, a_2, a_3 : Int = a, b, c;
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
                Var a, b: Int = x, y; 
                method(a,b: Int) {
                    Var x1 : Int = x;
                    Var y1 : Int = y;
                    Var a1 : Int = a;
                    Var b1 : Int = b;
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
                Var a, b: Int = x, y;
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





