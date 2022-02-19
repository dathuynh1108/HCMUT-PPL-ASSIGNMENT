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
