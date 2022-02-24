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
        expect = str(Program([ClassDecl(Id("Program"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        num = 303
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_004_attribute_declaration_simple_static(self):
        input = """
            Class Program {
                Var $a: Int;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"),[AttributeDecl(Static(),VarDecl(Id("$a"),IntType()))])]))
        num = 304
        self.assertTrue(TestAST.test(input, expect, num))

    def test_005_attribute_declaration_simple_instance_const(self):
        input = """
            Class Program {
                Val a: Int;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),None))])]))
        num = 305
        self.assertTrue(TestAST.test(input, expect, num))

    def test_006_attribute_declaration_simple_static_const(self):
        input = """
            Class Program {
                Val $a: Int;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Static(), ConstDecl(Id("$a"), IntType(), None))])]))
        num = 306
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_007_attribute_declaration_instance_with_init(self):
        input = """
            Class Program {
                Var a, b, c : Int = 1, 2, 3;
                Val x, y, z : Float = 1.1, 1.2, 1.3;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Instance(), VarDecl(Id("a"), IntType(), IntLiteral(1))), AttributeDecl(Instance(), VarDecl(Id("b"), IntType(), IntLiteral(2))), AttributeDecl(Instance(), VarDecl(Id("c"), IntType(), IntLiteral(
            3))), AttributeDecl(Instance(), ConstDecl(Id("x"), FloatType(), FloatLiteral(1.1))), AttributeDecl(Instance(), ConstDecl(Id("y"), FloatType(), FloatLiteral(1.2))), AttributeDecl(Instance(), ConstDecl(Id("z"), FloatType(), FloatLiteral(1.3)))])]))
        num = 307
        self.assertTrue(TestAST.test(input, expect, num))

    def test_008_attribute_declaration_instance_with_init(self):
        input = """
            Class Program {
                Var $a, $b, $c : Int = 1, 2, 3;
                Val $x, $y, $z : Float = 1.1, 1.2, 1.3;
            }
        """
        expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Static(), VarDecl(Id("$a"), IntType(), IntLiteral(1))), AttributeDecl(Static(), VarDecl(Id("$b"), IntType(), IntLiteral(2))), AttributeDecl(Static(), VarDecl(Id("$c"), IntType(), IntLiteral(
            3))), AttributeDecl(Static(), ConstDecl(Id("$x"), FloatType(), FloatLiteral(1.1))), AttributeDecl(Static(), ConstDecl(Id("$y"), FloatType(), FloatLiteral(1.2))), AttributeDecl(Static(), ConstDecl(Id("$z"), FloatType(), FloatLiteral(1.3)))])]))
        num = 308
        self.assertTrue(TestAST.test(input, expect, num))

    def test_009_attribute_declaration_and_method_declaration(self):
        input = """
            Class Program {
                method() {}
                $method() {}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([])),MethodDecl(Id($method),Static,[],Block([]))])])"""
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

    def test_012_constructor_destructor(self):
        input = """
            Class Program {
                Constructor() {}
                Constructor(a,b:Int; b: String) {}
                Destructor() {}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(b),StringType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        num = 312
        self.assertTrue(TestAST.test(input, expect, num))

    def test_013_string_expression(self):
        input = """
            Class Program {
                Var a, b: String = "abc" +. "xyz", "abc" ==. "xyz";
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(+.,StringLit(abc),StringLit(xyz)))),AttributeDecl(Instance,VarDecl(Id(b),StringType,BinaryOp(==.,StringLit(abc),StringLit(xyz))))])])"""
        num = 313
        self.assertTrue(TestAST.test(input, expect, num))

    def test_014_relation_expression(self):
        input = """
            Class Program {
                Var a, b, c, d, e, f: Int = 1 == 1, 1 != 1, a > b, a >= b, a < 1, a <= 1;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(==,IntLit(1),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(!=,IntLit(1),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(>,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(d),IntType,BinaryOp(>=,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(e),IntType,BinaryOp(<,Id(a),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(f),IntType,BinaryOp(<=,Id(a),IntLit(1))))])])"""
        num = 314
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_015_logical_expression(self):
        input = """
            Class Program {
                Var a, b: Int = a && True, b || False;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(&&,Id(a),BooleanLit(True)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(||,Id(b),BooleanLit(False))))])])"""
        num = 315
        self.assertTrue(TestAST.test(input, expect, num))

    def test_016_adding_expression(self):
        input = """
            Class Program {
                Var a, b: Int = a + 1, b - 1;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,Id(a),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(-,Id(b),IntLit(1))))])])"""
        num = 316
        self.assertTrue(TestAST.test(input, expect, num))

    def test_017_multiplying_expression(self):
        input = """
            Class Program {
                Var a, b, c: Int = a * 1, b / 1, c % 1;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(*,Id(a),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(/,Id(b),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(%,Id(c),IntLit(1))))])])"""
        num = 317
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_018_negative_expression(self):
        input = """
            Class Program {
                Var a, b: Int = !1, !a;
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,UnaryOp(!,IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,UnaryOp(!,Id(a))))])])"
        num = 318
        self.assertTrue(TestAST.test(input, expect, num))

    def test_019_sign_expression(self):
        input = """
            Class Program {
                Var a, b: Int = -1, -a;
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,UnaryOp(-,IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,UnaryOp(-,Id(a))))])])"
        num = 319
        self.assertTrue(TestAST.test(input, expect, num))

    def test_020_index_expression(self):
        input = """
            Class Program {
                Var a: Int = a[1][2][3][4][a][1+2];
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),Id(a),BinaryOp(+,IntLit(1),IntLit(2))])))])])"
        num = 320
        self.assertTrue(TestAST.test(input, expect, num))

    def test_021_instance_access_expession(self):
        input = """
            Class Program {
                Var a: Int = a.b.c.d;
                Var b: Int = a.c().c.d();
                Var c: Int = a.b(1,2,3).c.d(a,b,c);
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,CallExpr(FieldAccess(CallExpr(Id(a),Id(c),[]),Id(c)),Id(d),[]))),AttributeDecl(Instance,VarDecl(Id(c),IntType,CallExpr(FieldAccess(CallExpr(Id(a),Id(b),[IntLit(1),IntLit(2),IntLit(3)]),Id(c)),Id(d),[Id(a),Id(b),Id(c)])))])])"
        num = 321
        self.assertTrue(TestAST.test(input, expect, num))

    def test_022_static_access_expession(self):
        input = """
            Class Program {
                Var a: Int = a::$a;
                Var b: Int = a::$method(1,a,1+1);
                Var c: Int = a::$method(1,a,1+1).b;
                Var d: Int = a::$method(1,a,1+1).b(1,True, a);
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FieldAccess(Id(a),Id($a)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,CallExpr(Id(a),Id($method),[IntLit(1),Id(a),BinaryOp(+,IntLit(1),IntLit(1))]))),AttributeDecl(Instance,VarDecl(Id(c),IntType,FieldAccess(CallExpr(Id(a),Id($method),[IntLit(1),Id(a),BinaryOp(+,IntLit(1),IntLit(1))]),Id(b)))),AttributeDecl(Instance,VarDecl(Id(d),IntType,CallExpr(CallExpr(Id(a),Id($method),[IntLit(1),Id(a),BinaryOp(+,IntLit(1),IntLit(1))]),Id(b),[IntLit(1),BooleanLit(True),Id(a)])))])])"
        num = 322
        self.assertTrue(TestAST.test(input, expect, num))

    def test_023_object_creation_expression(self):
        input = """
            Class Program {
                Var a: Object = New Object();
                Var a: Object = New Object(New Object(1,2,3));
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Object)),NewExpr(Id(Object),[]))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Object)),NewExpr(Id(Object),[NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3)])])))])])"
        num = 323
        self.assertTrue(TestAST.test(input, expect, num))

    def test_024_operator_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = 1||2||3||4||5||6;
                    a = 1&&2&&3&&4&&5&&6; 
                    a = 1+2+3+4+5+6;
                    a = 1-2-3-4-5-6;
                    a = 1*2*3*4*5*6;
                    a = 1/2/3/4/5/6;
                    a = 1%2%3%4%5%6;
                    a = !!!!!!!!1;
                    a = --------1;
                    a = b[1][1][1][1+2+3][variable];
                    a = b[b[b[b[1]]]];
                    a = a.b.c.d.e.f;
                    a = a::$b.c.d.e.f;
                    a = a.b.c.method().method().a.b.method().method();
                    a = a::$b().method().a.method().a.method();
                    a = New a(New a(New a()));
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(-,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(*,BinaryOp(*,BinaryOp(*,BinaryOp(*,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(/,BinaryOp(/,BinaryOp(/,BinaryOp(/,BinaryOp(/,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(%,BinaryOp(%,BinaryOp(%,BinaryOp(%,BinaryOp(%,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1)))))))))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1)))))))))),AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(1),IntLit(1),IntLit(1),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),Id(variable)])),AssignStmt(Id(a),ArrayCell(Id(b),[ArrayCell(Id(b),[ArrayCell(Id(b),[ArrayCell(Id(b),[IntLit(1)])])])])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),Id(e)),Id(f))),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id($b)),Id(c)),Id(d)),Id(e)),Id(f))),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(method),[]),Id(method),[]),Id(a)),Id(b)),Id(method),[]),Id(method),[])),AssignStmt(Id(a),CallExpr(FieldAccess(CallExpr(FieldAccess(CallExpr(CallExpr(Id(a),Id($b),[]),Id(method),[]),Id(a)),Id(method),[]),Id(a)),Id(method),[])),AssignStmt(Id(a),NewExpr(Id(a),[NewExpr(Id(a),[NewExpr(Id(a),[])])]))]))])])"
        num = 324
        self.assertTrue(TestAST.test(input, expect, num))

    def test_025_simple_mix_expression(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    a = !(-1+2)*3/4%5 && True || False;
                    a = 1 == 2;
                    a = 1 != 2;
                    a = 1 > 2;
                    a = 1 < 2;
                    a = 1 >= 2;
                    a = 1<= 2;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),BinaryOp(||,BinaryOp(&&,BinaryOp(%,BinaryOp(/,BinaryOp(*,UnaryOp(!,BinaryOp(+,UnaryOp(-,IntLit(1)),IntLit(2))),IntLit(3)),IntLit(4)),IntLit(5)),BooleanLit(True)),BooleanLit(False))),AssignStmt(Id(a),BinaryOp(==,IntLit(1),IntLit(2))),AssignStmt(Id(a),BinaryOp(!=,IntLit(1),IntLit(2))),AssignStmt(Id(a),BinaryOp(>,IntLit(1),IntLit(2))),AssignStmt(Id(a),BinaryOp(<,IntLit(1),IntLit(2))),AssignStmt(Id(a),BinaryOp(>=,IntLit(1),IntLit(2))),AssignStmt(Id(a),BinaryOp(<=,IntLit(1),IntLit(2)))]))])])"
        num = 325
        self.assertTrue(TestAST.test(input, expect, num))

    def test_026_member_accesss_expression(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    ## Multi attribute ##
                    a = class_variable.attribute;
                    a = class_variable.attribute.attrubute;
                    a = class_variable.attribute.attrubute.attribute;
                   
                    ## Multi static and instance ##
                    a = class_name::$attribute;
                    a = class_name::$attribute.attribute;
                    a = class_name::$attribute.attribute.attribute;
                    
                    ## Multi method ##
                    a = class_variable.method(a,b,c);
                    a = class_variable.method(a,b,c).method(a,b,c);
                    a = class_variable.method(a,b,c).method(a,b,c).method(a,b,c);
                    
                    ## Hybrid ##
                    a = class_variable.attribute.method(a,b,c);
                    a = class_variable.attribute.method(a,b,c).method(a,b,c);
                    
                    a = class_variable.attribute.attribute.method(a,b,c);
                    a = class_variable.attribute.attribute.method(a,b,c).method(a,b,c);

                    a = class_variable.method(a,b,c).attribute;
                    a = class_variable.method(a,b,c).method(a,b,c).attribute;
                    a = class_variable.method(a,b,c).method(a,b,c).attribute.attribute;
                    a = class_variable.method(a,b,c).method(a,b,c).attribute.attribute.method(a,b,c);

                    a = class_name::$method(abc).method(a,b,c);
                    a = class_name::$method(abc).method(a,b,c).method(a,b,c);
                    a = class_name::$method(abc).method(a,b,c).method(a,b,c).attribute;
                    a = class_name::$method(abc).method(a,b,c).method(a,b,c).attribute.attribute;

                    a = (123).a();
                    a = (0).a();
                    a = (0x0).a();
                    a = (0b0).a();
                    a = (1.234).a();

                    a = (123).a.a.a.a();
                    a = (0).a.a.a.a();
                    a = (0x0).a.a.a.a();
                    a = (0b0).a.a.a.a();
                    a = (1.234).a.a.a.a();
                    a = (123).a(123).a(123).a(123).a(123);

                    a = New X().a;
                    a = New X().a.a.a.a;
                    a = New X().a.a.a.a.a();

                    a = New X().a();
                    a = New X().a().a.a.a();
                    a = New X().a.a().a().a.a.a();
                    a = New X().a().a().a().a().a();
                    
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),FieldAccess(Id(class_variable),Id(attribute))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(class_variable),Id(attribute)),Id(attrubute))),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(Id(class_variable),Id(attribute)),Id(attrubute)),Id(attribute))),AssignStmt(Id(a),FieldAccess(Id(class_name),Id($attribute))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(class_name),Id($attribute)),Id(attribute))),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(Id(class_name),Id($attribute)),Id(attribute)),Id(attribute))),AssignStmt(Id(a),CallExpr(Id(class_variable),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(Id(class_variable),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(Id(class_variable),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(FieldAccess(Id(class_variable),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(Id(class_variable),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(Id(class_variable),Id(attribute)),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(FieldAccess(Id(class_variable),Id(attribute)),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(CallExpr(Id(class_variable),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute))),AssignStmt(Id(a),FieldAccess(CallExpr(CallExpr(Id(class_variable),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute))),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(Id(class_variable),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute))),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(Id(class_variable),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(Id(class_name),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(Id(class_name),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(CallExpr(CallExpr(CallExpr(Id(class_name),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute))),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(CallExpr(Id(class_name),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute))),AssignStmt(Id(a),CallExpr(IntLit(123),Id(a),[])),AssignStmt(Id(a),CallExpr(IntLit(0),Id(a),[])),AssignStmt(Id(a),CallExpr(IntLit(0),Id(a),[])),AssignStmt(Id(a),CallExpr(IntLit(0),Id(a),[])),AssignStmt(Id(a),CallExpr(FloatLit(1.234),Id(a),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(FieldAccess(IntLit(123),Id(a)),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(FieldAccess(IntLit(0),Id(a)),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(FieldAccess(IntLit(0),Id(a)),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(FieldAccess(IntLit(0),Id(a)),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(FieldAccess(FloatLit(1.234),Id(a)),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(CallExpr(IntLit(123),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Id(a),[IntLit(123)])),AssignStmt(Id(a),FieldAccess(NewExpr(Id(X),[]),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(a)),Id(a)),Id(a))),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(a)),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(NewExpr(Id(X),[]),Id(a),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(CallExpr(NewExpr(Id(X),[]),Id(a),[]),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(a),[]),Id(a),[]),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(NewExpr(Id(X),[]),Id(a),[]),Id(a),[]),Id(a),[]),Id(a),[]),Id(a),[]))]))])])"
        num = 326
        self.assertTrue(TestAST.test(input, expect, num))

    def test_027_operator_precedence(self):
        input = r"""
            Class Program {
                main() {
                    a = a * b + c || d / e % f + - d;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(||,BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(+,BinaryOp(%,BinaryOp(/,Id(d),Id(e)),Id(f)),UnaryOp(-,Id(d)))))]))])])"
        num = 327
        self.assertTrue(TestAST.test(input, expect, num))

    def test_028_operator_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = a || b || c && d && e;  
                    a = a + b + c - d;
                    a = a * b / c % d;
                    a = !!!a;
                    a = ---a;
                    a = a[1][2][3][4];
                    a = a.a.a.a.a;
                    a = a.a().a.a().a();
                    a = New a(New a(New a (1)));
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(&&,BinaryOp(&&,BinaryOp(||,BinaryOp(||,Id(a),Id(b)),Id(c)),Id(d)),Id(e))),AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),Id(d))),AssignStmt(Id(a),BinaryOp(%,BinaryOp(/,BinaryOp(*,Id(a),Id(b)),Id(c)),Id(d))),AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,Id(a))))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(a))))),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),Id(a)),Id(a))),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(CallExpr(Id(a),Id(a),[]),Id(a)),Id(a),[]),Id(a),[])),AssignStmt(Id(a),NewExpr(Id(a),[NewExpr(Id(a),[NewExpr(Id(a),[IntLit(1)])])]))]))])])"
        num = 328
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_029_operator_precedence(self):
        input = r"""
            Class Program {
                main() {
                    a = a.b[1];
                    a = a + b - c * d / e % f || g && h == 1 ==. "a";
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),ArrayCell(FieldAccess(Id(a),Id(b)),[IntLit(1)])),AssignStmt(Id(a),BinaryOp(==.,BinaryOp(==,BinaryOp(&&,BinaryOp(||,BinaryOp(-,BinaryOp(+,Id(a),Id(b)),BinaryOp(%,BinaryOp(/,BinaryOp(*,Id(c),Id(d)),Id(e)),Id(f))),Id(g)),Id(h)),IntLit(1)),StringLit(a)))]))])])"
        num = 329
        self.assertTrue(TestAST.test(input, expect, num))

    def test_030_operator_precedence(self):
        input = r"""
            Class Program {
                main() {
                    a = a + b - c * d / e;
                    a = a -- b;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,Id(a),Id(b)),BinaryOp(/,BinaryOp(*,Id(c),Id(d)),Id(e)))),AssignStmt(Id(a),BinaryOp(-,Id(a),UnaryOp(-,Id(b))))]))])])"
        num = 330
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_031_operator_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = 1 * 2 * 3 * 4 / 5 / 6 / 7 % 8 % 9 % 10;
                    a = 1 / 2 / 3 / 4 * 5 * 6 * 7 % 8 % 9 % 10;
                    a = 1 % 2 % 4 % 5 / 5 / 6 / 7 * 8 * 9 * 10;
                    a = 1 + 2 + 3 + 4 + 5 - 6 - 7 - 8;
                    a = 1 - 2 - 3 - 4 - 5 + 6 + 7 + 8;
                    a = ----------------------1;
                    a = !!!!!!!!!!!!!!!!!!!!!!1;
                    a = ----------------------1 - 1 - -----------------1;
                    a = !!!!!!!!!!!!!!!!!!!!!1 - 1 && !!!!!!!!!!!!!1;
                    a = -(1+2+3+4);
                    a = !(1+2+3+4);
                    a = --------------(1+2+3+4);
                    a = !!!!!!!!!!!!!!(1+2+3+4);
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(%,BinaryOp(%,BinaryOp(%,BinaryOp(/,BinaryOp(/,BinaryOp(/,BinaryOp(*,BinaryOp(*,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6)),IntLit(7)),IntLit(8)),IntLit(9)),IntLit(10))),AssignStmt(Id(a),BinaryOp(%,BinaryOp(%,BinaryOp(%,BinaryOp(*,BinaryOp(*,BinaryOp(*,BinaryOp(/,BinaryOp(/,BinaryOp(/,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6)),IntLit(7)),IntLit(8)),IntLit(9)),IntLit(10))),AssignStmt(Id(a),BinaryOp(*,BinaryOp(*,BinaryOp(*,BinaryOp(/,BinaryOp(/,BinaryOp(/,BinaryOp(%,BinaryOp(%,BinaryOp(%,IntLit(1),IntLit(2)),IntLit(4)),IntLit(5)),IntLit(5)),IntLit(6)),IntLit(7)),IntLit(8)),IntLit(9)),IntLit(10))),AssignStmt(Id(a),BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6)),IntLit(7)),IntLit(8))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(-,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6)),IntLit(7)),IntLit(8))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1)))))))))))))))))))))))),AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1)))))))))))))))))))))))),AssignStmt(Id(a),BinaryOp(-,BinaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1))))))))))))))))))))))),IntLit(1)),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1)))))))))))))))))))),AssignStmt(Id(a),BinaryOp(&&,BinaryOp(-,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1)))))))))))))))))))))),IntLit(1)),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1)))))))))))))))),AssignStmt(Id(a),UnaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)))),AssignStmt(Id(a),UnaryOp(!,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4))))))))))))))))),AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)))))))))))))))))]))])])"
        num = 331
        self.assertTrue(TestAST.test(input, expect, num))
    def test_032_index_expression_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = a[1];
                    a = a[a[1]];
                    a = a[1][1];
                    a = a[1][1][1][1][1][1];
                    a = a[a[1][1][1]][1][1][1];
                    a = a[a[a[a[a[1]]]]][1][1][a[a[a[a[1]]]]];
                    a = Some_class::$method(1,1,1)[1][1][1];
                    a = some_object.method(1,1,1)[1][1][1];
                    a = some_object.method(1,1,1).method(1,1,1)[some_object.method(1,1,1).method(1,1,1)][1][1];
                    a = a.a.a[1][1][1];
                    a = a.a.a[a.a.a[a.a.a[a.a.a[1]]]];
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1),IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1)]),IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])])]),IntLit(1),IntLit(1),ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])])])])),AssignStmt(Id(a),ArrayCell(CallExpr(Id(Some_class),Id($method),[IntLit(1),IntLit(1),IntLit(1)]),[IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(CallExpr(Id(some_object),Id(method),[IntLit(1),IntLit(1),IntLit(1)]),[IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(CallExpr(CallExpr(Id(some_object),Id(method),[IntLit(1),IntLit(1),IntLit(1)]),Id(method),[IntLit(1),IntLit(1),IntLit(1)]),[CallExpr(CallExpr(Id(some_object),Id(method),[IntLit(1),IntLit(1),IntLit(1)]),Id(method),[IntLit(1),IntLit(1),IntLit(1)]),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),[IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),[ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),[ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),[ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),[IntLit(1)])])])]))]))])])"
        num = 333
        self.assertTrue(TestAST.test(input, expect, num))

    def test_033_new_expression_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = New Some_class();
                    a = New Some_class(1,2);
                    a = New Some_class(1+2-3*4/5%6||7&&8, a[1][1][1], a.a.a, a.method(), a::$a, a::$method());
                    a = New Some_class(New Some_class(New Some_class(1,2,3)));
                    a = New Some_class().fucking_attribute;
                    a = New Some_class()[1][2][3];
                    a = (New Some_class()).a.b.c;
                    a = (New Some_class())[1][2][3];
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(Some_class),[])),AssignStmt(Id(a),NewExpr(Id(Some_class),[IntLit(1),IntLit(2)])),AssignStmt(Id(a),NewExpr(Id(Some_class),[BinaryOp(&&,BinaryOp(||,BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(%,BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5)),IntLit(6))),IntLit(7)),IntLit(8)),ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1)]),FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),CallExpr(Id(a),Id(method),[]),FieldAccess(Id(a),Id($a)),CallExpr(Id(a),Id($method),[])])),AssignStmt(Id(a),NewExpr(Id(Some_class),[NewExpr(Id(Some_class),[NewExpr(Id(Some_class),[IntLit(1),IntLit(2),IntLit(3)])])])),AssignStmt(Id(a),FieldAccess(NewExpr(Id(Some_class),[]),Id(fucking_attribute))),AssignStmt(Id(a),ArrayCell(NewExpr(Id(Some_class),[]),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(Some_class),[]),Id(a)),Id(b)),Id(c))),AssignStmt(Id(a),ArrayCell(NewExpr(Id(Some_class),[]),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        num = 333
        self.assertTrue(TestAST.test(input, expect, num))

    def test_034_zero_integer_literal(self):
        input = r"""
            Class Program {
                Var a_1: Int = 0;
                Var a_2: Int = 00;
                Var a_3: Int = 0x0;
                Var a_4: Int = 0X0;
                Var a_5: Int = 0b0;
                Var a_6: Int = 0B0;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_2),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_3),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_4),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_5),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_6),IntType,IntLit(0)))])])"
        num = 334
        self.assertTrue(TestAST.test(input, expect, num))

    def test_035_integer_literal_dec(self):
        input = r"""
            Class Program {
                Var a_1: Int = 123456;
                Var a_2: Int = 1_2_3_4_5_6;
                Var a_3: Int = 123_456;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),IntType,IntLit(123456))),AttributeDecl(Instance,VarDecl(Id(a_2),IntType,IntLit(123456))),AttributeDecl(Instance,VarDecl(Id(a_3),IntType,IntLit(123456)))])])"
        num = 335
        self.assertTrue(TestAST.test(input, expect, num))

    def test_036_integer_literal_hex(self):
        input = r"""
            Class Program {
                Var a_1: Int = 0xABCDEF12345;
                Var a_2: Int = 0XABCDEF12345;
                Var a_3: Int = 0xA_B_C_D_E_F_1_2_3_4_5;
                Var a_4: Int = 0XA_B_C_D_E_F_1_2_3_4_5;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),IntType,IntLit(11806310474565))),AttributeDecl(Instance,VarDecl(Id(a_2),IntType,IntLit(11806310474565))),AttributeDecl(Instance,VarDecl(Id(a_3),IntType,IntLit(11806310474565))),AttributeDecl(Instance,VarDecl(Id(a_4),IntType,IntLit(11806310474565)))])])"
        num = 336
        self.assertTrue(TestAST.test(input, expect, num))

    def test_037_integer_literal_oct(self):
        input = r"""
            Class Program {
                Var a_1: Int = 012345670;
                Var a_2: Int = 01_2_3_4_5_6_7_0;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),IntType,IntLit(2739128))),AttributeDecl(Instance,VarDecl(Id(a_2),IntType,IntLit(2739128)))])])"
        num = 337
        self.assertTrue(TestAST.test(input, expect, num))

    def test_038_iteger_literal_bin(self):
        input = r"""
            Class Program {
                Var a_1: Int = 0b10101010101010;
                Var a_2: Int = 0B10101010101010;
                Var a_3: Int = 0b1_0_1_0_1_0_1_0;
                Var a_4: Int = 0B1_0_1_0_1_0_1_0;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),IntType,IntLit(10922))),AttributeDecl(Instance,VarDecl(Id(a_2),IntType,IntLit(10922))),AttributeDecl(Instance,VarDecl(Id(a_3),IntType,IntLit(170))),AttributeDecl(Instance,VarDecl(Id(a_4),IntType,IntLit(170)))])])"
        num = 338
        self.assertTrue(TestAST.test(input, expect, num))

    def test_039_float_literal(self):
        input = r"""
            Class Program {
                Var a_1: Float = 1.12345;
                Var a_2: Float = 1.12345e2;
                Var a_3: Float = 1.12345e+2;
                Var a_4: Float = 1.12345e-2;
                Var a_5: Float = 1.e2;
                Var a_6: Float = 1.e-2;
                Var a_7: Float = 1.e+2;
                Var a_8: Float = 1e2;
                Var a_9: Float = 1e-2;
                Var a_10: Float = 1e+2;
                Var a_11: Float = .e2;
                Var a_12: Float = .e-2;
                Var a_13: Float = .e+2;
                Var a_14: Float = .1e2;
                Var a_15: Float = .1e-2;
                Var a_16: Float = .1e+2;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),FloatType,FloatLit(1.12345))),AttributeDecl(Instance,VarDecl(Id(a_2),FloatType,FloatLit(112.345))),AttributeDecl(Instance,VarDecl(Id(a_3),FloatType,FloatLit(112.345))),AttributeDecl(Instance,VarDecl(Id(a_4),FloatType,FloatLit(0.0112345))),AttributeDecl(Instance,VarDecl(Id(a_5),FloatType,FloatLit(100.0))),AttributeDecl(Instance,VarDecl(Id(a_6),FloatType,FloatLit(0.01))),AttributeDecl(Instance,VarDecl(Id(a_7),FloatType,FloatLit(100.0))),AttributeDecl(Instance,VarDecl(Id(a_8),FloatType,FloatLit(100.0))),AttributeDecl(Instance,VarDecl(Id(a_9),FloatType,FloatLit(0.01))),AttributeDecl(Instance,VarDecl(Id(a_10),FloatType,FloatLit(100.0))),AttributeDecl(Instance,VarDecl(Id(a_11),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(a_12),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(a_13),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(a_14),FloatType,FloatLit(10.0))),AttributeDecl(Instance,VarDecl(Id(a_15),FloatType,FloatLit(0.001))),AttributeDecl(Instance,VarDecl(Id(a_16),FloatType,FloatLit(10.0)))])])"
        num = 339
        self.assertTrue(TestAST.test(input, expect, num))

    def test_040_string_literal(self):
        input = r"""
            Class Program {
                Var a_1: String = "abcdef";
                Var a_2: String = "abc\n\t\b\f\r'""; 
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),StringType,StringLit(abcdef))),AttributeDecl(Instance,VarDecl(Id(a_2),StringType,StringLit(abc\n\t\b\f\r'")))])])"""
        num = 340
        self.assertTrue(TestAST.test(input, expect, num))

    def test_041_boolean_literal(self):
        input = r"""
            Class Program {
                Var a: Boolean = True;
                Var b: Boolean = False;
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(b),BoolType,BooleanLit(False)))])])"""
        num = 341
        self.assertTrue(TestAST.test(input, expect, num))

    def test_042_indexed_array_literal(self):
        input = r"""
            Class Program {
                Var a: Array[Int, 100] = Array();
                Var b: Array[Int, 100] = Array(1,2,3,4);
                Var c: Array[String, 100] = Array("huynh", "thanh", "dat");
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(100,IntType),[])),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(100,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(100,StringType),[StringLit(huynh),StringLit(thanh),StringLit(dat)]))])])"""
        num = 342
        self.assertTrue(TestAST.test(input, expect, num))

    def test_043_multi_demensional_array(self):
        input = r"""
            Class Program {
                Var a: Array[Array[Int, 100], 100] = Array(Array(), Array(), Array());
                Var a: Array[Array[Int, 100], 100] = Array(Array(1,2,3), Array(1,2,3), Array(1,2,3));
                Var a: Array[Array[Array[Int, 100], 100], 100] = Array(Array(Array(1,2,3), Array(1,2,3)), Array(Array(1,2,3), Array(1,2,3)));
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(100,ArrayType(100,IntType)),[[],[],[]])),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(100,ArrayType(100,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3)]])),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(100,ArrayType(100,ArrayType(100,IntType))),[[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3)]],[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3)]]]))])])"""
        num = 343
        self.assertTrue(TestAST.test(input, expect, num))

    def test_044_array_complex_initialization(self):
        input = r"""
            Class Program {
                Var array_1, array_2, array_3: Array[Array[Int,6], 6] = Array(
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
                    ),
                    Array(
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
                    ),
                    Array(
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
                    );    
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(array_1),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]])),AttributeDecl(Instance,VarDecl(Id(array_2),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]])),AttributeDecl(Instance,VarDecl(Id(array_3),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]]))])])"
        num = 344
        self.assertTrue(TestAST.test(input, expect, num))

    def test_045_three_dimensional_array(self):
        input = r"""
            Class Program {
                Var array: Array[Array[Array[Int, 5], 1], 1] = Array (
                    Array (
                        Array (
                            1, 2, 3, 4, 5
                        )
                    )
                );
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(array),ArrayType(1,ArrayType(1,ArrayType(5,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]]]))])])"
        num = 345
        self.assertTrue(TestAST.test(input, expect, num))

    def test_046_array_many_declare(self):
        input = r"""
            Class Program {
                Var array: Array[Array[Array[Array[Int,1],1],1],1];
                Var array: Array[Array[Array[Int, 5], 1], 1] = Array (
                    Array (
                        Array (
                            1, 2, 3, 4, 5
                        ),
                        Array (
                            1, 2, 3, 4, 5
                        )
                    ),
                    Array (
                        Array (
                            1, 2, 3, 4, 5
                        ),
                        Array (
                            1, 2, 3, 4, 5
                        )
                    )
                );
                Var array: Array[Array[Array[Array[Int,1],1],1],1];
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(array),ArrayType(1,ArrayType(1,ArrayType(1,ArrayType(1,IntType)))))),AttributeDecl(Instance,VarDecl(Id(array),ArrayType(1,ArrayType(1,ArrayType(5,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]]])),AttributeDecl(Instance,VarDecl(Id(array),ArrayType(1,ArrayType(1,ArrayType(1,ArrayType(1,IntType))))))])])"
        num = 346
        self.assertTrue(TestAST.test(input, expect, num))

    def test_047_class_type(self):
        input = r"""
            Class Number {
                Var data: String = "1234"; 
            }
            Class Integer : Number{
                Var data: Number;
                Constructor(x: Int) {
                    Self.data = x;
                }
            }
            Class Program {
                main() {
                    Var x: Integer = New Integer(1);
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(data),StringType,StringLit(1234)))]),ClassDecl(Id(Integer),Id(Number),[AttributeDecl(Instance,VarDecl(Id(data),ClassType(Id(Number)))),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(data)),Id(x))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),ClassType(Id(Integer)),NewExpr(Id(Integer),[IntLit(1)]))]))])])"
        num = 347
        self.assertTrue(TestAST.test(input, expect, num))

    def test_048_special_literal(self):
        input = r"""
            Class Program {
                main() {
                    Self.x = 1;
                    Self.x();
                    Self.x(1,2,3);
                    Self.x = Null;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(x)),IntLit(1)),Call(Self(),Id(x),[]),Call(Self(),Id(x),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(FieldAccess(Self(),Id(x)),NullLiteral())]))])])"
        num = 348
        self.assertTrue(TestAST.test(input, expect, num))

    def test_049_array_incorrect_type(self):
        input = r"""
            Class Program {
                main() {
                    Var x: Int = Array(1,2,3, Array(1,2,3));
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,[IntLit(1),IntLit(2),IntLit(3),[IntLit(1),IntLit(2),IntLit(3)]])]))])])"
        num = 349
        self.assertTrue(TestAST.test(input, expect, num))

    def test_050_constructor_destructor_main(self):
        input = r"""
            Class Program {
                Constructor() {}
                Constructor(x: Int) {}
                Destructor() {}
                main() {}
                main(x: Int) {}
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(x),IntType)],Block([]))])])"
        num = 350
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_051_no_check_type_in_expression(self):
        input = r"""
            Class Program {
                main() {
                    a = True && "String";
                    a = "String" + 1 +. "String";
                    a = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a);
                    a = 0 + 0x0 + 0X0 + 0b0 + 0B0;
                    a = !1e123 - -True + !True / -----"String";
                    a = .123e123 > True;
                    a = 1.234e123 == "String";
                    a = 1.e-123 ==. "String";
                    a = Array(1,2,3) + Array(Array(1,2,3), Array(1,2,3));             
                    a = (1).a.a.a.a.a;
                    a = (1).a().a().a().a();
                    a = (1).a.a.a();
                    a = 1[1];
                    a = 1[1[1[1[1[1[1[1[1[1]]]]]]]]];
                    a = 1[1[1[1]]][1[1[1]]][0x0 + 0X0 - 0XFF + 0b0 + 0B0 / 0B1111];
                    a = (1).b[1][1][1][1][1];
                    a = (a+b+c).a.a.a[1[1[1[1[1[1]]]]]][1][a.b][Class_name::$a][a][Class_name::$a];
                    a = New X()[1];
                    a = New X().a;
                    a = New X(New X(a[New X()])).a[1];
                    a = Array(1,2,3)[1];
                    a = Array(Array(1,2,3), Array(1,2,3)).a.a.a();
                    a = Array(1,2,3)[Array(1,2,3)[1]];
                    a = "String"[1];
                    a = "String"["String"[1]];
                    a = "String"[New X().a];
                    a = Null;
                    a = Null.a;
                    a = Null.a.a.a;
                    a = Null.a.a.a();
                    a = Null.a().a().a();
                    a = Null[1];
                    a = Array(Null);
                    a = Null;
                    
                    Null.a();
                    Null.a.a.a();
                    Null.a();
                    Null.a.a.a();
                    Null.a().a().a();
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(&&,BooleanLit(True),StringLit(String))),AssignStmt(Id(a),BinaryOp(+.,BinaryOp(+,StringLit(String),IntLit(1)),StringLit(String))),AssignStmt(Id(a),BinaryOp(&&,BinaryOp(||,StringLit(String),StringLit(String)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(String),IntLit(0)),IntLit(0)),BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(Class_name),Id($a)))))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,UnaryOp(!,FloatLit(1e+123)),UnaryOp(-,BooleanLit(True))),BinaryOp(/,UnaryOp(!,BooleanLit(True)),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,StringLit(String))))))))),AssignStmt(Id(a),BinaryOp(>,FloatLit(1.23e+122),BooleanLit(True))),AssignStmt(Id(a),BinaryOp(==,FloatLit(1.234e+123),StringLit(String))),AssignStmt(Id(a),BinaryOp(==.,FloatLit(1e-123),StringLit(String))),AssignStmt(Id(a),BinaryOp(+,[IntLit(1),IntLit(2),IntLit(3)],[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3)]])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(IntLit(1),Id(a)),Id(a)),Id(a)),Id(a)),Id(a))),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(CallExpr(IntLit(1),Id(a),[]),Id(a),[]),Id(a),[]),Id(a),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(IntLit(1),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),ArrayCell(IntLit(1),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[IntLit(1)])])])])])])])])])),AssignStmt(Id(a),ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[IntLit(1)])]),ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[IntLit(1)])]),BinaryOp(+,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(255)),IntLit(0)),BinaryOp(/,IntLit(0),IntLit(15)))])),AssignStmt(Id(a),ArrayCell(FieldAccess(IntLit(1),Id(b)),[IntLit(1),IntLit(1),IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(FieldAccess(FieldAccess(BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),Id(a)),Id(a)),Id(a)),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[ArrayCell(IntLit(1),[IntLit(1)])])])])]),IntLit(1),FieldAccess(Id(a),Id(b)),FieldAccess(Id(Class_name),Id($a)),Id(a),FieldAccess(Id(Class_name),Id($a))])),AssignStmt(Id(a),ArrayCell(NewExpr(Id(X),[]),[IntLit(1)])),AssignStmt(Id(a),FieldAccess(NewExpr(Id(X),[]),Id(a))),AssignStmt(Id(a),ArrayCell(FieldAccess(NewExpr(Id(X),[NewExpr(Id(X),[ArrayCell(Id(a),[NewExpr(Id(X),[])])])]),Id(a)),[IntLit(1)])),AssignStmt(Id(a),ArrayCell([IntLit(1),IntLit(2),IntLit(3)],[IntLit(1)])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess([[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3)]],Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),ArrayCell([IntLit(1),IntLit(2),IntLit(3)],[ArrayCell([IntLit(1),IntLit(2),IntLit(3)],[IntLit(1)])])),AssignStmt(Id(a),ArrayCell(StringLit(String),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(StringLit(String),[ArrayCell(StringLit(String),[IntLit(1)])])),AssignStmt(Id(a),ArrayCell(StringLit(String),[FieldAccess(NewExpr(Id(X),[]),Id(a))])),AssignStmt(Id(a),NullLiteral()),AssignStmt(Id(a),FieldAccess(NullLiteral(),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(NullLiteral(),Id(a)),Id(a)),Id(a))),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(NullLiteral(),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(NullLiteral(),Id(a),[]),Id(a),[]),Id(a),[])),AssignStmt(Id(a),ArrayCell(NullLiteral(),[IntLit(1)])),AssignStmt(Id(a),[NullLiteral()]),AssignStmt(Id(a),NullLiteral()),Call(NullLiteral(),Id(a),[]),Call(FieldAccess(FieldAccess(NullLiteral(),Id(a)),Id(a)),Id(a),[]),Call(NullLiteral(),Id(a),[]),Call(FieldAccess(FieldAccess(NullLiteral(),Id(a)),Id(a)),Id(a),[]),Call(CallExpr(CallExpr(NullLiteral(),Id(a),[]),Id(a),[]),Id(a),[])]))])])"
        num = 351
        self.assertTrue(TestAST.test(input, expect, num))

    def test_052_method_param(self):
        input = r"""
            Class Program {
                method() {}
                main() {}
                method(a,b,c: Int; x,y,z: String) {}
                main(a,b,c: Int; x,y,z: String) {}
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(method),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),StringType),param(Id(y),StringType),param(Id(z),StringType)],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),StringType),param(Id(y),StringType),param(Id(z),StringType)],Block([]))])])"
        num = 352
        self.assertTrue(TestAST.test(input, expect, num))

    def test_053_method_param(self):
        input = r"""
            Class Program {
                method() {}
                main() {}
                method(a,b,c: Int; x,y,z: String) {}
                main(a,b,c: Int; x,y,z: String) {}
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(method),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),StringType),param(Id(y),StringType),param(Id(z),StringType)],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),StringType),param(Id(y),StringType),param(Id(z),StringType)],Block([]))])])"
        num = 353
        self.assertTrue(TestAST.test(input, expect, num))

    def test_054_assign_statement_lhs_is_id(self):
        input = r"""
            Class Program {
                method() {
                    a = 1;
                    a = 1 + 1;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(a),IntLit(1)),AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(1)))]))])])"
        num = 354
        self.assertTrue(TestAST.test(input, expect, num))

    def test_055_assign_statement_lhs_is_array_cell(self):
        input = r"""
            Class Program {
                method() {
                    a[1] = 1;
                    a[1][1] = 1;
                    a[1][1][1] = 1;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1)]),IntLit(1))]))])])"
        num = 355
        self.assertTrue(TestAST.test(input, expect, num))

    def test_056_assign_statement_lhs_is_field_access(self):
        input = r"""
            Class Program {
                method() {
                    a.b = 1;
                    a.b.c = 1;
                    a.b.c.d.e = 1;
                    a.b().c().d = 1;
                    Self.a().b = 1;
                    Self.a().b().c().d = 1;
                    Self.a().b = Null;
                    Self.a().b().c().d = Null;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(FieldAccess(Id(a),Id(b)),IntLit(1)),AssignStmt(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),IntLit(1)),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),Id(e)),IntLit(1)),AssignStmt(FieldAccess(CallExpr(CallExpr(Id(a),Id(b),[]),Id(c),[]),Id(d)),IntLit(1)),AssignStmt(FieldAccess(CallExpr(Self(),Id(a),[]),Id(b)),IntLit(1)),AssignStmt(FieldAccess(CallExpr(CallExpr(CallExpr(Self(),Id(a),[]),Id(b),[]),Id(c),[]),Id(d)),IntLit(1)),AssignStmt(FieldAccess(CallExpr(Self(),Id(a),[]),Id(b)),NullLiteral()),AssignStmt(FieldAccess(CallExpr(CallExpr(CallExpr(Self(),Id(a),[]),Id(b),[]),Id(c),[]),Id(d)),NullLiteral())]))])])"
        num = 356
        self.assertTrue(TestAST.test(input, expect, num))

    def test_057_simple_foreach_statement(self):
        input = r"""
            Class Program {
                method() {
                    Foreach (i In 1 .. 100 By 1) {}
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([])])]))])])"
        num = 357
        self.assertTrue(TestAST.test(input, expect, num))

    def test_058_foreach_statement_miss_by(self):
        input = r"""
            Class Program {
                method() {
                    Foreach (i In 1 .. 100) {}
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([])])]))])])"
        num = 358
        self.assertTrue(TestAST.test(input, expect, num))

    def test_059_foreach_statement_statement_with_expression(self):
        input = r"""
            Class Program {
                method() {
                    Foreach (i In 1 + 1 + a + b .. a + b * c / d By Self.a) {}
                    Foreach (i In Self.a .. Self.b() By a::$b) {}
                    
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(1)),Id(a)),Id(b)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(*,Id(b),Id(c)),Id(d))),FieldAccess(Self(),Id(a)),Block([])]),For(Id(i),FieldAccess(Self(),Id(a)),CallExpr(Self(),Id(b),[]),FieldAccess(Id(a),Id($b)),Block([])])]))])])"
        num = 359
        self.assertTrue(TestAST.test(input, expect, num))

    def test_060_break_statement(self):
        input = r"""
            Class Program {
                method() {
                    Foreach (i In 1 .. 100) {
                        Break;
                    } 
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Break])])]))])])"
        num = 360
        self.assertTrue(TestAST.test(input, expect, num))
    def test_061_break_statement(self):
        input = r"""
            Class Program {
                method() {
                    Foreach (i In 1 .. 100) {
                        Continue;
                    } 
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Continue])])]))])])"
        num = 361
        self.assertTrue(TestAST.test(input, expect, num))

    def test_062_return_statement_without_expression(self):
        input = r"""
            Class Program {
                method() {
                    Return;
                    Foreach (i In 1 .. 100) {
                        Return;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Return(),For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Return()])])]))])])"
        num = 362
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_063_return_statement_with_expression(self):
        input = r"""
            Class Program {
                method() {
                    Return a + 1 * b;
                    Foreach (i In 1 .. 100) {
                        Return i * i + a.b;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,Id(a),BinaryOp(*,IntLit(1),Id(b)))),For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Return(BinaryOp(+,BinaryOp(*,Id(i),Id(i)),FieldAccess(Id(a),Id(b))))])])]))])])"
        num = 363
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_064_block_statement_in_block_statement(self):
        input = r"""
            Class Program {
                method() {
                    {{{{}}}}
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Block([Block([Block([Block([])])])])]))])])"
        num = 364
        self.assertTrue(TestAST.test(input, expect, num))

    def test_065_foreach_in_foreach(self):
        input = r"""
            Class Program {
                method() {
                    Foreach (i In 1 .. 100) {
                        Foreach (j In 1 .. i By i * i) {
                            {
                                Break;
                            }
                        }
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([For(Id(j),IntLit(1),Id(i),BinaryOp(*,Id(i),Id(i)),Block([Block([Break])])])])])]))])])"
        num = 365
        self.assertTrue(TestAST.test(input, expect, num))

    def test_066_method_inovation_statement_pure_instance(self):
        input = r"""
            Class Program {
                method() {
                    a.b();
                    a.b.c();
                    a.b().c();
                    a.b.c.d();
                    a.b.c().d();
                    a.b().c().d();
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(Id(a),Id(b),[]),Call(FieldAccess(Id(a),Id(b)),Id(c),[]),Call(CallExpr(Id(a),Id(b),[]),Id(c),[]),Call(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[]),Call(CallExpr(FieldAccess(Id(a),Id(b)),Id(c),[]),Id(d),[]),Call(CallExpr(CallExpr(Id(a),Id(b),[]),Id(c),[]),Id(d),[])]))])])"
        num = 366
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_067_method_inovation_statement_static_instance(self):
        input = r"""
            Class Program {
                method() {
                    a::$b();
                    a::$b.c();
                    a::$b.c.d();
                    a::$b.c().d();
                    a::$b().c().d();
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(Id(a),Id($b),[]),Call(FieldAccess(Id(a),Id($b)),Id(c),[]),Call(FieldAccess(FieldAccess(Id(a),Id($b)),Id(c)),Id(d),[]),Call(CallExpr(FieldAccess(Id(a),Id($b)),Id(c),[]),Id(d),[]),Call(CallExpr(CallExpr(Id(a),Id($b),[]),Id(c),[]),Id(d),[])]))])])"
        num = 367
        self.assertTrue(TestAST.test(input, expect, num))

    def test_068_method_inovation_statement_of_new_expression(self):
        input = r"""
            Class Program {
                method() {
                    New X().a();
                    New X().a.b();
                    New X().a().b();
                    New X(New X()).a().b();
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(NewExpr(Id(X),[]),Id(a),[]),Call(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b),[]),Call(CallExpr(NewExpr(Id(X),[]),Id(a),[]),Id(b),[]),Call(CallExpr(NewExpr(Id(X),[NewExpr(Id(X),[])]),Id(a),[]),Id(b),[])]))])])"
        num = 368
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_069_method_inovation_statement(self):
        input = r"""
            Class Program {
                main() {
                    a.b();
                    a.b.c();
                    a.b.c.d();
                    a.b().c().d();
                    
                    a.b(123).c(123);
                    a.b(123).c.d(123);
                    a.b.c(123).d(123);
                    a.b(123).c(123).d(123);
                    a.b(123).c().d(123);
                    
                    a::$b();
                    a::$b.c();
                    a::$b.c.d();

                    a::$b.c(123).d(123);
                    a::$b(123).c.d(123);
                    a::$b(123).c().d(123);            
                
                    Self.a();
                    Self.a.b();
                    Self.a.b.c();
                    Self.a().b.c();
                    Self.a().b().c();

                    (123).a();
                    (0).a();
                    (0x0).a();
                    (0b0).a();
                    (1.234).a();

                    (123).a.a.a.a();
                    (0).a.a.a.a();
                    (0x0).a.a.a.a();
                    (0b0).a.a.a.a();
                    (1.234).a.a.a.a();
                    (123).a(123).a(123).a(123).a(123);
                    
                    New X().a();
                    New X().a.a.a();
                    New X().a().a.a();
                    New X().a().a().a();
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(a),Id(b),[]),Call(FieldAccess(Id(a),Id(b)),Id(c),[]),Call(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[]),Call(CallExpr(CallExpr(Id(a),Id(b),[]),Id(c),[]),Id(d),[]),Call(CallExpr(Id(a),Id(b),[IntLit(123)]),Id(c),[IntLit(123)]),Call(FieldAccess(CallExpr(Id(a),Id(b),[IntLit(123)]),Id(c)),Id(d),[IntLit(123)]),Call(CallExpr(FieldAccess(Id(a),Id(b)),Id(c),[IntLit(123)]),Id(d),[IntLit(123)]),Call(CallExpr(CallExpr(Id(a),Id(b),[IntLit(123)]),Id(c),[IntLit(123)]),Id(d),[IntLit(123)]),Call(CallExpr(CallExpr(Id(a),Id(b),[IntLit(123)]),Id(c),[]),Id(d),[IntLit(123)]),Call(Id(a),Id($b),[]),Call(FieldAccess(Id(a),Id($b)),Id(c),[]),Call(FieldAccess(FieldAccess(Id(a),Id($b)),Id(c)),Id(d),[]),Call(CallExpr(FieldAccess(Id(a),Id($b)),Id(c),[IntLit(123)]),Id(d),[IntLit(123)]),Call(FieldAccess(CallExpr(Id(a),Id($b),[IntLit(123)]),Id(c)),Id(d),[IntLit(123)]),Call(CallExpr(CallExpr(Id(a),Id($b),[IntLit(123)]),Id(c),[]),Id(d),[IntLit(123)]),Call(Self(),Id(a),[]),Call(FieldAccess(Self(),Id(a)),Id(b),[]),Call(FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),Id(c),[]),Call(FieldAccess(CallExpr(Self(),Id(a),[]),Id(b)),Id(c),[]),Call(CallExpr(CallExpr(Self(),Id(a),[]),Id(b),[]),Id(c),[]),Call(IntLit(123),Id(a),[]),Call(IntLit(0),Id(a),[]),Call(IntLit(0),Id(a),[]),Call(IntLit(0),Id(a),[]),Call(FloatLit(1.234),Id(a),[]),Call(FieldAccess(FieldAccess(FieldAccess(IntLit(123),Id(a)),Id(a)),Id(a)),Id(a),[]),Call(FieldAccess(FieldAccess(FieldAccess(IntLit(0),Id(a)),Id(a)),Id(a)),Id(a),[]),Call(FieldAccess(FieldAccess(FieldAccess(IntLit(0),Id(a)),Id(a)),Id(a)),Id(a),[]),Call(FieldAccess(FieldAccess(FieldAccess(IntLit(0),Id(a)),Id(a)),Id(a)),Id(a),[]),Call(FieldAccess(FieldAccess(FieldAccess(FloatLit(1.234),Id(a)),Id(a)),Id(a)),Id(a),[]),Call(CallExpr(CallExpr(CallExpr(IntLit(123),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Call(NewExpr(Id(X),[]),Id(a),[]),Call(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(a)),Id(a),[]),Call(FieldAccess(CallExpr(NewExpr(Id(X),[]),Id(a),[]),Id(a)),Id(a),[]),Call(CallExpr(CallExpr(NewExpr(Id(X),[]),Id(a),[]),Id(a),[]),Id(a),[])]))])])"
        num = 369
        self.assertTrue(TestAST.test(input, expect, num))

    def test_070_index_with_access_expression(self):
        input = r"""
            Class Program {
                main() {
                    a = a.b[1];
                    a = a.a.a.a.a.a[1];
                    a = Self.a[1];
                    a = Self.a.a.a.a.a[1];
                    a = Class_name::$a[1];
                    a = Class_name::$a.a.a.a[1];
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),ArrayCell(FieldAccess(Id(a),Id(b)),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Self(),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(Id(Class_name),Id($a)),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(Class_name),Id($a)),Id(a)),Id(a)),Id(a)),[IntLit(1)]))]))])])"
        num = 370
        self.assertTrue(TestAST.test(input, expect, num))

    def test_071_index_with_method_call_expression(self):
        input = r"""
            Class Program {
                main() {
                    a = a.b()[1];
                    a = a.b(1,2,3)[1][2][3];
                    a = a.b.c(1,2,3).d[1][2][3];
                    a = a.b().c(1,2,3).d()[1][2][3];
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),ArrayCell(CallExpr(Id(a),Id(b),[]),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(CallExpr(Id(a),Id(b),[IntLit(1),IntLit(2),IntLit(3)]),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(Id(a),ArrayCell(FieldAccess(CallExpr(FieldAccess(Id(a),Id(b)),Id(c),[IntLit(1),IntLit(2),IntLit(3)]),Id(d)),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(Id(a),ArrayCell(CallExpr(CallExpr(CallExpr(Id(a),Id(b),[]),Id(c),[IntLit(1),IntLit(2),IntLit(3)]),Id(d),[]),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        num = 371
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_072_left_hand_side(self):
        input = r"""
            Class Program {
                main() {
                    a = 1;
                    a[1] = 1;
                    a[1][2][3] = 1;
                    a[1][a[a[2]]][3][4] = 1;
                    a[a[a[1][2][3]]][2][3] = 1;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(2)])]),IntLit(3),IntLit(4)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])]),IntLit(2),IntLit(3)]),IntLit(1))]))])])"
        num = 372
        self.assertTrue(TestAST.test(input, expect, num))

    def test_072_left_hand_side(self):
        input = r"""
            Class Program {
                main() {
                    a = 1;
                    a[1] = 1;
                    a[1][2][3] = 1;
                    a[1][a[a[2]]][3][4] = 1;
                    a[a[a[1][2][3]]][2][3] = 1;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(2)])]),IntLit(3),IntLit(4)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])]),IntLit(2),IntLit(3)]),IntLit(1))]))])])"
        num = 372
        self.assertTrue(TestAST.test(input, expect, num))

    def test_073_foreach_statement_reverse(self):
        input = r"""
            Class Program {
                main() {
                    Foreach (i In 1 .. 100 By -1) {}
                    Foreach (i In 100 .. 1) {}
                    Foreach (i In 100 .. 1 By 1) {}
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),UnaryOp(-,IntLit(1)),Block([])]),For(Id(i),IntLit(100),IntLit(1),IntLit(1),Block([])]),For(Id(i),IntLit(100),IntLit(1),IntLit(1),Block([])])]))])])"
        num = 373
        self.assertTrue(TestAST.test(input, expect, num))

    def test_074_self_method(self):
        input = r"""
            Class Some_class {    
                    Var $a, b: Int = 1, 2;
                    Method(n: Int) {
                        If (n == 1) {
                            Return True;
                        }
                        Else {
                            Return False;
                        }
                    }  
                    $Method(n: Int) {
                        If (n == 1) {
                            Return True;
                        }
                        Else {
                            Return False;
                        }
                    }    
                    Constructor(int: Int; string: String) {
                        Some_class::$Method(1,2,3);
                        Self.Method(1,2,3);
                        a = Some_class::$Method(1,2,3);
                        a = Self.Method(1,2,3);
                    }
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                add_100 (i:Int) {
                    i = i + 100;
                    Return i;
                }
                $sub_100(i:Int) {
                    i = i - 100;
                    Return i;
                }
                main() {
                    Var some_class: Some_class = New Some_class(1, "abc");
                    Foreach (i In Some_class::$Method(1+2-3*4/5%6) .. some_class.method(1+2+3) By 1) {
                        Self.print(i);
                        If (i > 1) {
                            Self.print(i);
                        }
                        Elseif (i < -1) {
                            Self.add_100(i);
                        }
                        Else {
                            Some_class::$sub_100(i);
                        }
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Some_class),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(Method),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(1)),Block([Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))])),MethodDecl(Id($Method),Static,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(1)),Block([Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))])),MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([Call(Id(Some_class),Id($Method),[IntLit(1),IntLit(2),IntLit(3)]),Call(Self(),Id(Method),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(Id(a),CallExpr(Id(Some_class),Id($Method),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(Id(a),CallExpr(Self(),Id(Method),[IntLit(1),IntLit(2),IntLit(3)]))])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(add_100),Instance,[param(Id(i),IntType)],Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(100))),Return(Id(i))])),MethodDecl(Id($sub_100),Static,[param(Id(i),IntType)],Block([AssignStmt(Id(i),BinaryOp(-,Id(i),IntLit(100))),Return(Id(i))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(some_class),ClassType(Id(Some_class)),NewExpr(Id(Some_class),[IntLit(1),StringLit(abc)])),For(Id(i),CallExpr(Id(Some_class),Id($Method),[BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(%,BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5)),IntLit(6)))]),CallExpr(Id(some_class),Id(method),[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))]),IntLit(1),Block([Call(Self(),Id(print),[Id(i)]),If(BinaryOp(>,Id(i),IntLit(1)),Block([Call(Self(),Id(print),[Id(i)])]),If(BinaryOp(<,Id(i),UnaryOp(-,IntLit(1))),Block([Call(Self(),Id(add_100),[Id(i)])]),Block([Call(Id(Some_class),Id($sub_100),[Id(i)])])))])])]))])])"
        num = 374
        self.assertTrue(TestAST.test(input, expect, num))

    def test_075_complex_multi_demensional_array(self):
        input = r"""
            Class Program {
                main() {
                    a = Array(
                        Array(1,2,3),
                        Array(1,2),
                        Array(Array(1,2,3), Array(1,2,3,4), Array(1,2,3,4,5)),
                        Array(a[1], New X(), New X()[1], a==b, "String" ==. "String"),
                        a[Array(1,2,3,4)],
                        New X(),
                        (1+2+3)
                    );
                }
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2)],[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]],[ArrayCell(Id(a),[IntLit(1)]),NewExpr(Id(X),[]),ArrayCell(NewExpr(Id(X),[]),[IntLit(1)]),BinaryOp(==,Id(a),Id(b)),BinaryOp(==.,StringLit(String),StringLit(String))],ArrayCell(Id(a),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]]),NewExpr(Id(X),[]),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))])]))])])"""
        num = 375
        self.assertTrue(TestAST.test(input, expect, num))

    def test_076_expression_with_lp_rp(self):
        input = r"""
            Class Program {
                main() {
                    a = 1 + (2 + 3);
                }
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))))]))])])"""
        num = 376
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_077_method_call_with_complex_expression(self):
        input = r"""
            Class Program {
                main() {
                    a.b(1, 1 + 2, True && False, "huynh" +. "dat", (1 + 2), -1);
                }
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(a),Id(b),[IntLit(1),BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(&&,BooleanLit(True),BooleanLit(False)),BinaryOp(+.,StringLit(huynh),StringLit(dat)),BinaryOp(+,IntLit(1),IntLit(2)),UnaryOp(-,IntLit(1))])]))])])"""
        num = 377
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_078_method_call_with_complex_expression(self):
        input = r"""
            Class Program {
                main() {
                    a = !-1;
                    a = -(!1);
                }
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),UnaryOp(!,UnaryOp(-,IntLit(1)))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(!,IntLit(1))))]))])])"""
        num = 378
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_079_multi_lp_rp(self):
        input = r"""
            Class Program {
                main() {
                    a = ((((((1 + 2)))))) * 3;
                }
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])"""
        num = 379
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_080_special_parameter(self):
        input = r"""
            Class Program {
                main() {
                    a = a.b(Self, Null, (((((1))))));
                }
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(a),Id(b),[Self(),NullLiteral(),IntLit(1)]))]))])])"""
        num = 380
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_081_multi_destructor_constructor_without_return(self):
        # Not valid but ok 
        input = r"""
            Class Program {
                Constructor() {
                    Return;
                }
                Constructor(x: Int; y: String; a: Array[Array[Int,1],1]) {
                    Return a + x + y;
                }
                Destructor() {
                    Console.log("End");
                }
                Destructor() {
                    Return;
                }
                Constructor() {}
                Constructor(x: Int; y: String; a: Array[Array[Int,1],1]) {}
                Destructor() {}
                Destructor() {}
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([Return()])),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),StringType),param(Id(a),ArrayType(1,ArrayType(1,IntType)))],Block([Return(BinaryOp(+,BinaryOp(+,Id(a),Id(x)),Id(y)))])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(Console),Id(log),[StringLit(End)])])),MethodDecl(Id(Destructor),Instance,[],Block([Return()])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),StringType),param(Id(a),ArrayType(1,ArrayType(1,IntType)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        num = 381
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_082_member_access_invalid_but_ok(self):
        input = r"""
            Class Program {
                main() {
                    a = a.b.c;
                    a = Class_name::$a;
                    a = Class_name::$a.a.a.a();
                    a = Null.a;
                    a = Null.null.a;
                    a = Self.a;
                    a = Self.self.a;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),FieldAccess(FieldAccess(Id(a),Id(b)),Id(c))),AssignStmt(Id(a),FieldAccess(Id(Class_name),Id($a))),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Class_name),Id($a)),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),FieldAccess(NullLiteral(),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(NullLiteral(),Id(null)),Id(a))),AssignStmt(Id(a),FieldAccess(Self(),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(Self(),Id(self)),Id(a)))]))])])"
        num = 382
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_083_new_expression_associativity(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program : Some_class {
                main() {
                    a = New a(New a(New a(1,2,3), New a(1,2,3)), New a());
                    a = New Some_class();
                    a = New Some_class(1,2);
                    a = New Some_class(1+2-3*4/5%6||7&&8, a[1][1][1], a.a.a, a.method(), a::$a, a::$method());
                    a = New Some_class(New Some_class(New Some_class(1,2,3)));
                    a = New Some_class(New Some_class(New Some_class()))[1][2][3];
                    a = (New Some_class() + Self).a.a.a;
                    a = (New Some_class() + Null)[1][2][3];
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),Id(Some_class),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(a),[NewExpr(Id(a),[NewExpr(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),NewExpr(Id(a),[IntLit(1),IntLit(2),IntLit(3)])]),NewExpr(Id(a),[])])),AssignStmt(Id(a),NewExpr(Id(Some_class),[])),AssignStmt(Id(a),NewExpr(Id(Some_class),[IntLit(1),IntLit(2)])),AssignStmt(Id(a),NewExpr(Id(Some_class),[BinaryOp(&&,BinaryOp(||,BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(%,BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5)),IntLit(6))),IntLit(7)),IntLit(8)),ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1)]),FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),CallExpr(Id(a),Id(method),[]),FieldAccess(Id(a),Id($a)),CallExpr(Id(a),Id($method),[])])),AssignStmt(Id(a),NewExpr(Id(Some_class),[NewExpr(Id(Some_class),[NewExpr(Id(Some_class),[IntLit(1),IntLit(2),IntLit(3)])])])),AssignStmt(Id(a),ArrayCell(NewExpr(Id(Some_class),[NewExpr(Id(Some_class),[NewExpr(Id(Some_class),[])])]),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(BinaryOp(+,NewExpr(Id(Some_class),[]),Self()),Id(a)),Id(a)),Id(a))),AssignStmt(Id(a),ArrayCell(BinaryOp(+,NewExpr(Id(Some_class),[]),NullLiteral()),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        num = 383
        self.assertTrue(TestAST.test(input, expect, num))

    def test_084_array_complex_initialization(self):
        input = r"""
            Class Program {
                Var array_1, array_2, array_3: Array[Array[Int,6], 6] = Array(
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
                    ),
                    Array(
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
                    ),
                    Array(
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                        Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
                    );  
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(array_1),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]])),AttributeDecl(Instance,VarDecl(Id(array_2),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]])),AttributeDecl(Instance,VarDecl(Id(array_3),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]]))])])"
        num = 384
        self.assertTrue(TestAST.test(input, expect, num))
    def test_085_array_declaration_with_many_base(self):
        input = r"""
            Class Program {
                Var a: Array[Int, 5];
                Var a: Array[Int, 0xFFFF];
                Var a: Array[Int, 0XFFFF];
                Var a: Array[Int, 0b1111];
                Var a: Array[Int, 0B1111];
                Var a: Array[Int, 01234];
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(65535,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(65535,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(15,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(15,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(668,IntType)))])])"
        num = 385
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_086_float_overflow(self):
        input = r"""
            Class Program {
                Var a: Float = 1.111111111111111111111111111111111111111111;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(1.1111111111111112)))])])"
        num = 386
        self.assertTrue(TestAST.test(input, expect, num))
    def test_087_int_over_flow(self):
        input = r"""
            Class Program {
                Var a: Float = 99999999999999999999999999999999999999999999999999999;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,IntLit(99999999999999999999999999999999999999999999999999999)))])])"
        num = 387
        self.assertTrue(TestAST.test(input, expect, num))

    def test_088_add_expression_associativity(self):
        input = r"""
            Class Program {
                Var a: Int = a + b - c - d + e;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,BinaryOp(-,BinaryOp(-,BinaryOp(+,Id(a),Id(b)),Id(c)),Id(d)),Id(e))))])])"
        num = 388
        self.assertTrue(TestAST.test(input, expect, num))

    def test_089_logical_expression_associativity(self):
        input = r"""
            Class Program {
                Var a: Int = a || b && c || d && e;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(||,Id(a),Id(b)),Id(c)),Id(d)),Id(e))))])])"
        num = 389
        self.assertTrue(TestAST.test(input, expect, num))

    def test_090_mul_expression_associativity(self):
        input = r"""
            Class Program {
                Var a: Int = a * b / c * d % e;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(%,BinaryOp(*,BinaryOp(/,BinaryOp(*,Id(a),Id(b)),Id(c)),Id(d)),Id(e))))])])"
        num = 390
        self.assertTrue(TestAST.test(input, expect, num))

    def test_091_simple_if_statement(self):
        input = r"""
            Class Program {
                method(a: Int) {
                    If (a > 1) {
                        Return 1;
                    }
                    Return 2;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(>,Id(a),IntLit(1)),Block([Return(IntLit(1))])),Return(IntLit(2))]))])])"
        num = 391
        self.assertTrue(TestAST.test(input, expect, num))


    def test_092_simple_if_else_statement(self):
        input = r"""
            Class Program {
                method(a: Int) {
                    If (a > 1) {
                        Return 1;
                    }
                    Else {
                        Return 2;
                    }
                    Return 2;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(>,Id(a),IntLit(1)),Block([Return(IntLit(1))]),Block([Return(IntLit(2))])),Return(IntLit(2))]))])])"
        num = 392
        self.assertTrue(TestAST.test(input, expect, num))

    def test_093_simple_if_elseif_statement(self):
        input = r"""
            Class Program {
                method(a: Int) {
                    If (a > 1) {
                        Return 1;
                    }
                    Elseif (a < 1) {
                        Return 2;
                    }
                    Return 2;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(>,Id(a),IntLit(1)),Block([Return(IntLit(1))]),If(BinaryOp(<,Id(a),IntLit(1)),Block([Return(IntLit(2))]))),Return(IntLit(2))]))])])"
        num = 393
        self.assertTrue(TestAST.test(input, expect, num))

    def test_094_simple_if_elseif_else_statement(self):
        input = r"""
            Class Program {
                method(a: Int) {
                    If (a > 1) {
                        Return 1;
                    }
                    Elseif (a < 1) {
                        Return 2;
                    }
                    Else {
                        Return 2;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(>,Id(a),IntLit(1)),Block([Return(IntLit(1))]),If(BinaryOp(<,Id(a),IntLit(1)),Block([Return(IntLit(2))]),Block([Return(IntLit(2))])))]))])])"
        num = 394
        self.assertTrue(TestAST.test(input, expect, num))

    def test_095_simple_if_multi_elseif_statement(self):
        input = r"""
            Class Program {
                method(a: Int) {
                    If (a > 1) {
                        Return 1;
                    }
                    Elseif (a < 1) {
                        Return 2;
                    }
                    Elseif (a == 1) {
                        Return 3;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(>,Id(a),IntLit(1)),Block([Return(IntLit(1))]),If(BinaryOp(<,Id(a),IntLit(1)),Block([Return(IntLit(2))]),If(BinaryOp(==,Id(a),IntLit(1)),Block([Return(IntLit(3))]))))]))])])"
        num = 395
        self.assertTrue(TestAST.test(input, expect, num))

    def test_096_simple_if_multi_elseif_else_statement(self):
        input = r"""
            Class Program {
                method(a: Int) {
                    If (a > 1) {
                        Return 1;
                    }
                    Elseif (a < 1) {
                        Return 2;
                    }
                    Elseif (a == 1) {
                        Return 3;
                    }
                    Elseif (b > 1) {
                        Return 4;
                    }
                    Else {
                        Return 5;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(>,Id(a),IntLit(1)),Block([Return(IntLit(1))]),If(BinaryOp(<,Id(a),IntLit(1)),Block([Return(IntLit(2))]),If(BinaryOp(==,Id(a),IntLit(1)),Block([Return(IntLit(3))]),If(BinaryOp(>,Id(b),IntLit(1)),Block([Return(IntLit(4))]),Block([Return(IntLit(5))])))))]))])])"
        num = 396
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_097_complex_if_multi_elseif_else_statement(self):
        input = r"""
            Class Program {
                method(a: Int) {
                    If (a == 1) {
                        If (b == 1) {}
                        Elseif (b == 2) {}
                        Elseif (b == 3) {}
                        Else {}
                    }
                    Elseif (a == 2) {
                        If (b == 1) {}
                        Elseif (b == 2) {}
                        Elseif (b == 3) {}
                        Else {}
                    }
                    Elseif (a == 3) {
                        If (b == 1) {}
                        Elseif (b == 2) {}
                        Elseif (b == 3) {}
                        Else {}
                    }
                    Else {
                        If (b == 1) {}
                        Elseif (b == 2) {}
                        Elseif (b == 3) {}
                        Else {}
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(==,Id(a),IntLit(1)),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([]),If(BinaryOp(==,Id(b),IntLit(2)),Block([]),If(BinaryOp(==,Id(b),IntLit(3)),Block([]),Block([]))))]),If(BinaryOp(==,Id(a),IntLit(2)),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([]),If(BinaryOp(==,Id(b),IntLit(2)),Block([]),If(BinaryOp(==,Id(b),IntLit(3)),Block([]),Block([]))))]),If(BinaryOp(==,Id(a),IntLit(3)),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([]),If(BinaryOp(==,Id(b),IntLit(2)),Block([]),If(BinaryOp(==,Id(b),IntLit(3)),Block([]),Block([]))))]),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([]),If(BinaryOp(==,Id(b),IntLit(2)),Block([]),If(BinaryOp(==,Id(b),IntLit(3)),Block([]),Block([]))))]))))]))])])"
        num = 397
        self.assertTrue(TestAST.test(input, expect, num))
    
    def test_098_complex_statement(self):
        input = r"""
            Class Program {
                Var x, y: Int;
                Val $a, $b: Float = 1.1, 1.2;
                method(a: Int) {
                    Var x, y: Int = Self.x, Self.y;
                    Val a, b: Float = Program::$a, Program::$b;
                    If (a == 1) {
                        If (b == 1) {
                            Foreach (i In 1 .. 100) {
                                If (i % Self.x == 0) {
                                    Break;
                                }
                                Else {
                                    Continue;
                                }
                            }
                            Self.x = 1;
                        }
                        Elseif (b == 2) {
                            Self.x = Self.x + b;
                        }
                        Elseif (b == 3) {
                            {{{}}}
                        }
                        Else {
                            Console.log("Huynh Thanh Dat");
                            Self.y = a.b();
                        }
                        Return 1;
                    }
                    Elseif (a == 2) {
                        If (b == 1) {
                            Program::$a = a.b;
                            Program::$b = a.b(1,2,Self.x);
                        }
                        Elseif (b == 2) {}
                        Elseif (b == 3) {}
                        Else {}
                        Foreach (i In 1 .. 100 By i % 2) {
                                If (i % Self.x == 0) {
                                    Break;
                                }
                                Else {
                                    Continue;
                                }
                        }
                    }
                    Elseif (a == 3) {
                        If (b == 1) {}
                        Elseif (b == 2) {}
                        Elseif (b == 3) {}
                        Else {}
                    }
                    Else {
                        If (b == 1) {}
                        Elseif (b == 2) {}
                        Elseif (b == 3) {}
                        Else {}
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),AttributeDecl(Static,ConstDecl(Id($a),FloatType,FloatLit(1.1))),AttributeDecl(Static,ConstDecl(Id($b),FloatType,FloatLit(1.2))),MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([VarDecl(Id(x),IntType,FieldAccess(Self(),Id(x))),VarDecl(Id(y),IntType,FieldAccess(Self(),Id(y))),ConstDecl(Id(a),FloatType,FieldAccess(Id(Program),Id($a))),ConstDecl(Id(b),FloatType,FieldAccess(Id(Program),Id($b))),If(BinaryOp(==,Id(a),IntLit(1)),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(i),FieldAccess(Self(),Id(x))),IntLit(0)),Block([Break]),Block([Continue]))])]),AssignStmt(FieldAccess(Self(),Id(x)),IntLit(1))]),If(BinaryOp(==,Id(b),IntLit(2)),Block([AssignStmt(FieldAccess(Self(),Id(x)),BinaryOp(+,FieldAccess(Self(),Id(x)),Id(b)))]),If(BinaryOp(==,Id(b),IntLit(3)),Block([Block([Block([Block([])])])]),Block([Call(Id(Console),Id(log),[StringLit(Huynh Thanh Dat)]),AssignStmt(FieldAccess(Self(),Id(y)),CallExpr(Id(a),Id(b),[]))])))),Return(IntLit(1))]),If(BinaryOp(==,Id(a),IntLit(2)),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([AssignStmt(FieldAccess(Id(Program),Id($a)),FieldAccess(Id(a),Id(b))),AssignStmt(FieldAccess(Id(Program),Id($b)),CallExpr(Id(a),Id(b),[IntLit(1),IntLit(2),FieldAccess(Self(),Id(x))]))]),If(BinaryOp(==,Id(b),IntLit(2)),Block([]),If(BinaryOp(==,Id(b),IntLit(3)),Block([]),Block([])))),For(Id(i),IntLit(1),IntLit(100),BinaryOp(%,Id(i),IntLit(2)),Block([If(BinaryOp(==,BinaryOp(%,Id(i),FieldAccess(Self(),Id(x))),IntLit(0)),Block([Break]),Block([Continue]))])])]),If(BinaryOp(==,Id(a),IntLit(3)),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([]),If(BinaryOp(==,Id(b),IntLit(2)),Block([]),If(BinaryOp(==,Id(b),IntLit(3)),Block([]),Block([]))))]),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([]),If(BinaryOp(==,Id(b),IntLit(2)),Block([]),If(BinaryOp(==,Id(b),IntLit(3)),Block([]),Block([]))))]))))]))])])"
        num = 398
        self.assertTrue(TestAST.test(input, expect, num))

    def test_099_call_exp_vs_call_statement(self):
        input = r"""
            Class Object {
                Var x: Int = Self.a();
                main() {
                    x = Self.a();
                    x = a.a();
                    Self.a();
                    a.a();
                }
            }
            Class Program : Object {
                main() {
                    Var x: Int = Object::$main();
                    Var x: Int = Object.main();
                    Object::$main();
                    object.main();
                    object.main(object.main());
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Object),[AttributeDecl(Instance,VarDecl(Id(x),IntType,CallExpr(Self(),Id(a),[]))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(x),CallExpr(Self(),Id(a),[])),AssignStmt(Id(x),CallExpr(Id(a),Id(a),[])),Call(Self(),Id(a),[]),Call(Id(a),Id(a),[])]))]),ClassDecl(Id(Program),Id(Object),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,CallExpr(Id(Object),Id($main),[])),VarDecl(Id(x),IntType,CallExpr(Id(Object),Id(main),[])),Call(Id(Object),Id($main),[]),Call(Id(object),Id(main),[]),Call(Id(object),Id(main),[CallExpr(Id(object),Id(main),[])])]))])])"
        num = 399
        self.assertTrue(TestAST.test(input, expect, num))
