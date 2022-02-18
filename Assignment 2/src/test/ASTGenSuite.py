import unittest
from TestUtils import TestAST
from AST import *

from main.d96.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    def test_000_simple_class(self):
        input = """Class Program {}"""
        expect = str(Program([ClassDecl(Id("Program"), [])]))
        #expect = "Program([ClassDecl(Id(Program), [])])"
        num = 300
        self.assertTrue(TestAST.test(input, expect, num))
    def test_001_simple_class_with_parent(self):
        input = """Class Program : Object {}"""
        expect = str(Program([ClassDecl(Id("Program"), [], Id("Object"))]))
        num = 301
        self.assertTrue(TestAST.test(input, expect, num))
    def test_002_many_class(self):
        input = """
            Class Object {}
            Class Some_class : Object {}
            Class Program : Object {}

        """
        expect = str(Program([ClassDecl(Id("Object"), []), ClassDecl(
            Id("Some_class"), [], Id("Object")), ClassDecl(Id("Program"), [], Id("Object"))]))
        num = 302
        self.assertTrue(TestAST.test(input, expect, num))

    def test_003_attribute_declaration_simple_instance(self):
        input = """
            Class Program {
                Var a: Int;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"),[AttributeDecl(Instance(),VarDecl("a",IntType()))])]))
        num = 303
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_004_attribute_declaration_simple_static(self):
        input = """
            Class Program {
                Var $a: Int;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"),[AttributeDecl(Static(),VarDecl("$a",IntType()))])]))
        num = 304
        self.assertTrue(TestAST.test(input, expect, num))

    def test_005_attribute_declaration_simple_instance_const(self):
        input = """
            Class Program {
                Val a: Int;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"),[AttributeDecl(Instance(),ConstDecl("a",IntType(),None))])]))
        num = 305
        self.assertTrue(TestAST.test(input, expect, num))

    def test_006_attribute_declaration_simple_static_const(self):
        input = """
            Class Program {
                Val $a: Int;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Static(), ConstDecl("$a", IntType(), None))])]))
        num = 306
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_007_attribute_declaration_instance_with_init(self):
        input = """
            Class Program {
                Var a, b, c : Int = 1, 2, 3;
                Val x, y, z : Float = 1.1, 1.2, 1.3;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Instance(), VarDecl("a", IntType(), IntLiteral(1))), AttributeDecl(Instance(), VarDecl("b", IntType(), IntLiteral(2))), AttributeDecl(Instance(), VarDecl("c", IntType(), IntLiteral(
            3))), AttributeDecl(Instance(), ConstDecl("x", FloatType(), FloatLiteral(1.1))), AttributeDecl(Instance(), ConstDecl("y", FloatType(), FloatLiteral(1.2))), AttributeDecl(Instance(), ConstDecl("z", FloatType(), FloatLiteral(1.3)))])]))
        num = 307
        self.assertTrue(TestAST.test(input, expect, num))

    def test_008_attribute_declaration_instance_with_init(self):
        input = """
            Class Program {
                Var $a, $b, $c : Int = 1, 2, 3;
                Val $x, $y, $z : Float = 1.1, 1.2, 1.3;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Static(), VarDecl("$a", IntType(), IntLiteral(1))), AttributeDecl(Static(), VarDecl("$b", IntType(), IntLiteral(2))), AttributeDecl(Static(), VarDecl("$c", IntType(), IntLiteral(
            3))), AttributeDecl(Static(), ConstDecl("$x", FloatType(), FloatLiteral(1.1))), AttributeDecl(Static(), ConstDecl("$y", FloatType(), FloatLiteral(1.2))), AttributeDecl(Static(), ConstDecl("$z", FloatType(), FloatLiteral(1.3)))])]))
        num = 308
        self.assertTrue(TestAST.test(input, expect, num))

    def test_009_attribute_declaration_and_method_declaration(self):
        input = """
            Class Program {
                Var a, b, c : Int = 1, 2, 3;
                Val x, y, z : Float = 1.1, 1.2, 1.3;
                Var $a, $b, $c : Int = 1, 2, 3;
                Val $x, $y, $z : Float = 1.1, 1.2, 1.3;
                method() {}
                $method() {}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(a,IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(b,IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(c,IntType,IntLit(3))),AttributeDecl(Instance,ConstDecl(x,FloatType,FloatLit(1.1))),AttributeDecl(Instance,ConstDecl(y,FloatType,FloatLit(1.2))),AttributeDecl(Instance,ConstDecl(z,FloatType,FloatLit(1.3))),AttributeDecl(Static,VarDecl($a,IntType,IntLit(1))),AttributeDecl(Static,VarDecl($b,IntType,IntLit(2))),AttributeDecl(Static,VarDecl($c,IntType,IntLit(3))),AttributeDecl(Static,ConstDecl($x,FloatType,FloatLit(1.1))),AttributeDecl(Static,ConstDecl($y,FloatType,FloatLit(1.2))),AttributeDecl(Static,ConstDecl($z,FloatType,FloatLit(1.3))),MethodDecl(Id(method),Instance,[],Block([])),MethodDecl(Id($method),Static,[],Block([]))])])"""
        num = 309
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_010_method_with_parameter(self):
        input = """
            Class Program {
                method() {}
                $method() {}
                method(a,b: Int; x,y: String) {}
                $method(a,b: Int; x,y: String) {}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([])),MethodDecl(Id($method),Static,[],Block([])),MethodDecl(Id(method),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(x),StringType),param(Id(y),StringType)],Block([])),MethodDecl(Id($method),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(x),StringType),param(Id(y),StringType)],Block([]))])])"""
        num = 310
        self.assertTrue(TestAST.test(input, expect, num))

    def test_011_main_method_in_class_program(self):
        input = """
            Class Program {
                main() {}
                main(a: Int) {}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([]))])])"""
        num = 311
        self.assertTrue(TestAST.test(input, expect, num))

    def test_012_string_expression(self):
        input = """
            Class Program {
                Var a, b: String = "abc" +. "xyz", "abc" ==. "xyz";
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(a,StringType,BinaryOp(+.,StringLit(abc),StringLit(xyz)))),AttributeDecl(Instance,VarDecl(b,StringType,BinaryOp(==.,StringLit(abc),StringLit(xyz))))])])"""
        num = 312
        self.assertTrue(TestAST.test(input, expect, num))
