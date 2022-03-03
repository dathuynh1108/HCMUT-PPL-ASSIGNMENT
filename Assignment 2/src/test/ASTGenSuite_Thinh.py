import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1_self_instance_access_stmt_AND_class_access_exprs(self):
        input = r"""
            Class Rectangle: Shape {
                getArea() {
                    Return Self.length * Self.width;
                }
            }
        """
        # Out.printInt(Shape::$numOfShape);
        expect = """Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2_attr_decl_unequivalent_num(self):
        input = r"""
            Class Program {
Val length, width : Int = 1, 2 ;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(length),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(width),IntType,IntLit(2)))])])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3_attr_decl_unequivalent_num(self):
        input = r"""
            Class Program {
Val length, width, height : Int = 1, 2, 4 ;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(length),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(width),IntType,IntLit(2))),AttributeDecl(Instance,ConstDecl(Id(height),IntType,IntLit(4)))])])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4_if_block_stmt(self):
        input = r"""
            Class Program {
Val length, width : Int = 1, 2 ;
getArea() {
    Val t2, t1 : Int = 1, 2 ;
    If ( boolean_expr ){
        Val length, width : Int = 1, 2 ;
    }
    Return Self.length * Self.width ;
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(length),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(width),IntType,IntLit(2))),MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(t2),IntType,IntLit(1)),ConstDecl(Id(t1),IntType,IntLit(2)),If(Id(boolean_expr),Block([ConstDecl(Id(length),IntType,IntLit(1)),ConstDecl(Id(width),IntType,IntLit(2))])),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test5_for_in_block_stmt(self):
        input = r"""
            Class Program {
Val length, width : Int = 1, 2 ;
getArea() {
    Val t2, t1 : Int = 1, 2 ;
    Foreach ( i In 1 .. 100 By 2 ){
        Val length, width : Int = 1, 2 ;
    }
    Return Self.length * Self.width ;
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(length),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(width),IntType,IntLit(2))),MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(t2),IntType,IntLit(1)),ConstDecl(Id(t1),IntType,IntLit(2)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([ConstDecl(Id(length),IntType,IntLit(1)),ConstDecl(Id(width),IntType,IntLit(2))])]),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6_if_nested_block_stmt(self):
        input = r"""
            Class Program {
Val length, width : Int = 1, 2 ;
getArea() {
    Val a1, a2 : Int = 1, 2;
    If ( boolean_expr ){
        Val c1, c2 : Int = 1, 2 ;
        If ( boolean_expr ){
            Val d1, d2 : Int = 1, 2 ;
        }
    }
    Else {
    }
    Return Self.length * Self.width ;
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(length),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(width),IntType,IntLit(2))),MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(a1),IntType,IntLit(1)),ConstDecl(Id(a2),IntType,IntLit(2)),If(Id(boolean_expr),Block([ConstDecl(Id(c1),IntType,IntLit(1)),ConstDecl(Id(c2),IntType,IntLit(2)),If(Id(boolean_expr),Block([ConstDecl(Id(d1),IntType,IntLit(1)),ConstDecl(Id(d2),IntType,IntLit(2))]))]),Block([])),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7_for_in_nested_block_stmt(self):
        input = r"""
    Class Program1 {
        Val length, width : Int = 1, 2 ;
        getArea() {
            Val t2, t1 : Int = 1, 2 ;
            Foreach ( i In 1 .. 100 By 2 ){
                Val length, width : Int = 1, 2 ;
                If ( boolean_expr ){
                    Val d1, d2 : Int = 1, 2 ;
                }
            }
            Return Self.length * Self.width ;
        }
    }

    Class Program2 {
        Val length, width : Int = 1, 2 ;
        getArea() {
            Val t2, t1 : Int = 1, 2 ;
            Foreach ( i In 1 .. 100 By 2 ){
                Val length, width : Int = 1, 2 ;
            }
            Return Self.length * Self.width ;
        }
    }
            """
        expect = """Program([ClassDecl(Id(Program1),[AttributeDecl(Instance,ConstDecl(Id(length),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(width),IntType,IntLit(2))),MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(t2),IntType,IntLit(1)),ConstDecl(Id(t1),IntType,IntLit(2)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([ConstDecl(Id(length),IntType,IntLit(1)),ConstDecl(Id(width),IntType,IntLit(2)),If(Id(boolean_expr),Block([ConstDecl(Id(d1),IntType,IntLit(1)),ConstDecl(Id(d2),IntType,IntLit(2))]))])]),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program2),[AttributeDecl(Instance,ConstDecl(Id(length),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(width),IntType,IntLit(2))),MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(t2),IntType,IntLit(1)),ConstDecl(Id(t1),IntType,IntLit(2)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([ConstDecl(Id(length),IntType,IntLit(1)),ConstDecl(Id(width),IntType,IntLit(2))])]),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test8_instance_method_invoke_stmt(self):
        input = r"""
            Class Program {
getArea() {
    hello.printInt(i1, i2).getVar(3 + 4);
    Return Self.length * Self.width ;
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([Call(CallExpr(Id(hello),Id(printInt),[Id(i1),Id(i2)]),Id(getVar),[BinaryOp(+,IntLit(3),IntLit(4))]),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test09_static_attr_access_expr(self):
        input = r"""
            Class Program {
getArea() {
    Var x, y : Int = 1, 2;
    x = 1 + Hello::$stint;
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([VarDecl(Id(x),IntType,IntLit(1)),VarDecl(Id(y),IntType,IntLit(2)),AssignStmt(Id(x),BinaryOp(+,IntLit(1),FieldAccess(Id(Hello),Id($stint))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test10_instance_attr_access_expr(self):
        input = r"""
Class Program {
getArea() {
    Var x, y : Int = 1, 2;
    x = Self.x / Self.atrtr.y + Hello::$stint;
}
}
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([VarDecl(Id(x),IntType,IntLit(1)),VarDecl(Id(y),IntType,IntLit(2)),AssignStmt(Id(x),BinaryOp(+,BinaryOp(/,FieldAccess(Self(),Id(x)),FieldAccess(FieldAccess(Self(),Id(atrtr)),Id(y))),FieldAccess(Id(Hello),Id($stint))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test11_static_method_invoke_stmt(self):
        input = r"""
            Class Program {
getArea() {
    Hello::$stfunc(12, s1, 3 + 9).wrong("ok");
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([Call(CallExpr(Id(Hello),Id($stfunc),[IntLit(12),Id(s1),BinaryOp(+,IntLit(3),IntLit(9))]),Id(wrong),[StringLit(ok)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12_instance_method_invoke_stmt(self):
        input = r"""
            Class Program {
getArea() {
    Hello.stfunc(12, s1, 3 + 9).right(1 + 3, 2 + 4, x1, x2);
    Hello.stfunc(12, s1, 3 + 9).right(1 + 3, 2 + 4, x1, x2);
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([Call(CallExpr(Id(Hello),Id(stfunc),[IntLit(12),Id(s1),BinaryOp(+,IntLit(3),IntLit(9))]),Id(right),[BinaryOp(+,IntLit(1),IntLit(3)),BinaryOp(+,IntLit(2),IntLit(4)),Id(x1),Id(x2)]),Call(CallExpr(Id(Hello),Id(stfunc),[IntLit(12),Id(s1),BinaryOp(+,IntLit(3),IntLit(9))]),Id(right),[BinaryOp(+,IntLit(1),IntLit(3)),BinaryOp(+,IntLit(2),IntLit(4)),Id(x1),Id(x2)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13_mix_instance_method_attr_access_stmt(self):
        input = r"""
Class Program {
getArea() {
    x = 1 + a;
    Self.hello.func(4 + 5, a1, s2).inbetweencvar.foo(1,2,3);
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(Id(x),BinaryOp(+,IntLit(1),Id(a))),Call(FieldAccess(CallExpr(FieldAccess(Self(),Id(hello)),Id(func),[BinaryOp(+,IntLit(4),IntLit(5)),Id(a1),Id(s2)]),Id(inbetweencvar)),Id(foo),[IntLit(1),IntLit(2),IntLit(3)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14_array_type_decl(self):
        input = r"""
Class Program {
getArea() {
    Val x : Array[Int, 01001] = 6;
}
}
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(x),ArrayType(513,IntType),IntLit(6))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15_array_type_decl(self):
        input = r"""
Class Program {
Var $x,$y,$z :Array[Int,0b1010]=3,4,5;
getArea() {
    Var x,y,z :Array[Int,0xA]=1,2,3;
}
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($x),ArrayType(10,IntType),IntLit(3))),AttributeDecl(Static,VarDecl(Id($y),ArrayType(10,IntType),IntLit(4))),AttributeDecl(Static,VarDecl(Id($z),ArrayType(10,IntType),IntLit(5))),MethodDecl(Id(getArea),Instance,[],Block([VarDecl(Id(x),ArrayType(10,IntType),IntLit(1)),VarDecl(Id(y),ArrayType(10,IntType),IntLit(2)),VarDecl(Id(z),ArrayType(10,IntType),IntLit(3))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test16_assignment(self):
        input = r"""
Class Program {
Val x: Float = 5.4e12;
getArea() {
    Val x: Float = 1;
}
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(x),FloatType,FloatLit(5400000000000.0))),MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(x),FloatType,IntLit(1))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17_instance_access_from_function_return(self):
        input = """
Class Test{
    Var ins: Int;
    Var $static: Int;
    $Test(){
        Var x: Array[Array[String, 1], 1] = a::$stfunc().a.b().c[a.b()][2];
    }
}
        """
        expect = """Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(ins),IntType)),AttributeDecl(Static,VarDecl(Id($static),IntType)),MethodDecl(Id($Test),Static,[],Block([VarDecl(Id(x),ArrayType(1,ArrayType(1,StringType)),ArrayCell(FieldAccess(CallExpr(FieldAccess(CallExpr(Id(a),Id($stfunc),[]),Id(a)),Id(b),[]),Id(c)),[CallExpr(Id(a),Id(b),[]),IntLit(2)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18_ClassType(self):
        input = """
Class Test{
    Var ins: Int;
    Var $static: Int;
    $Test(){
        Var x: Classname = a::$stfunc().a.b().c[a.b()][2];
    }
}
        """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(ins),IntType)),AttributeDecl(Static,VarDecl(Id($static),IntType)),MethodDecl(Id($Test),Static,[],Block([VarDecl(Id(x),ClassType(Id(Classname)),ArrayCell(FieldAccess(CallExpr(FieldAccess(CallExpr(Id(a),Id($stfunc),[]),Id(a)),Id(b),[]),Id(c)),[CallExpr(Id(a),Id(b),[]),IntLit(2)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19_index_operator_on_function_return(self):
        input = """
            ## Program with a main function ##
            Class Program {
                func(x: Int; y: String) {
Var x,y: HelloClass = Array(Array(1),"String"), IdVar.funcCall()["Index on a function return value"];
                }
                main() {}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),[[IntLit(1)],StringLit(String)]),VarDecl(Id(y),ClassType(Id(HelloClass)),ArrayCell(CallExpr(Id(IdVar),Id(funcCall),[]),[StringLit(Index on a function return value)]))])),MethodDecl(Id(main),Static,[],Block([]))])])"""
        num = 319
        self.assertTrue(TestAST.test(input, expect, num))

    def test20_index_operator_on_function_return(self):
        input = """
            ## Program with a main function ##
            Class Program1 {
                func(x: Int; y: String) {
Var x,y: HelloClass = IdVar.funcCall()["Index"],
a.b()[12 + 5 == Hello.world][Array(Array(1),"String")];
                }
                main() {}
            }
            Class Program2 {}
        """
        expect = "Program([ClassDecl(Id(Program1),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),ArrayCell(CallExpr(Id(IdVar),Id(funcCall),[]),[StringLit(Index)])),VarDecl(Id(y),ClassType(Id(HelloClass)),ArrayCell(CallExpr(Id(a),Id(b),[]),[BinaryOp(==,BinaryOp(+,IntLit(12),IntLit(5)),FieldAccess(Id(Hello),Id(world))),[[IntLit(1)],StringLit(String)]]))])),MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program2),[])])"
        num = 320
        self.assertTrue(TestAST.test(input, expect, num))

    def test21_instance_attr_access_on_function_return(self):
        input = """
            ## Program with a main function ##
            Class Program1 {
                func(x: Int; y: String) {
Var x,y: HelloClass = IdVar.funcCall().funcCall2().attrAccess, 0;
                }
                main() {}
            }
            Class Program2 {}
        """
        expect = "Program([ClassDecl(Id(Program1),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),FieldAccess(CallExpr(CallExpr(Id(IdVar),Id(funcCall),[]),Id(funcCall2),[]),Id(attrAccess))),VarDecl(Id(y),ClassType(Id(HelloClass)),IntLit(0))])),MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program2),[])])"
        num = 321
        self.assertTrue(TestAST.test(input, expect, num))

    def test22_instance_attr_access_on_static_method_return(self):
        input = """
                ## Program with a main function ##
                Class Program1 {
                    func(x: Int; y: String) {
    Var x,y: HelloClass = IdVar::$funcCall().funcCall2().attrAccess, 0;
                    }
                    main() {}
                }
                Class Program2 {}
            """
        expect = "Program([ClassDecl(Id(Program1),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),FieldAccess(CallExpr(CallExpr(Id(IdVar),Id($funcCall),[]),Id(funcCall2),[]),Id(attrAccess))),VarDecl(Id(y),ClassType(Id(HelloClass)),IntLit(0))])),MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program2),[])])"
        num = 322
        self.assertTrue(TestAST.test(input, expect, num))

    def test23_new_operator_member_access(self):
        input = """
            ## Program with a main function ##
            Class Program {
                func(x: Int; y: String) {
Var x,y: HelloClass = 0, New ClassObj(4.5, x / 4.5, t[0]).funcCall().funcCall2().attrAccess;
                }
                main() {}
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),IntLit(0)),VarDecl(Id(y),ClassType(Id(HelloClass)),FieldAccess(CallExpr(CallExpr(NewExpr(Id(ClassObj),[FloatLit(4.5),BinaryOp(/,Id(x),FloatLit(4.5)),ArrayCell(Id(t),[IntLit(0)])]),Id(funcCall),[]),Id(funcCall2),[]),Id(attrAccess)))])),MethodDecl(Id(main),Static,[],Block([]))])])"
        num = 323
        self.assertTrue(TestAST.test(input, expect, num))

    def test24_index_element_on_new_operator(self):
        input = """
            ## Program with a main function ##
            Class Program {
                func(x: Int; y: String) {
Var x,y: HelloClass = 0, New ClassObj(4.5, x / z, t[0])[Classname::$funcCall().funcCall2().attrAccess];
                }
                main() {}
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),IntLit(0)),VarDecl(Id(y),ClassType(Id(HelloClass)),ArrayCell(NewExpr(Id(ClassObj),[FloatLit(4.5),BinaryOp(/,Id(x),Id(z)),ArrayCell(Id(t),[IntLit(0)])]),[FieldAccess(CallExpr(CallExpr(Id(Classname),Id($funcCall),[]),Id(funcCall2),[]),Id(attrAccess))]))])),MethodDecl(Id(main),Static,[],Block([]))])])"
        num = 324
        self.assertTrue(TestAST.test(input, expect, num))

    def test25_simple_expression(self):
        input = """
            Class Program {
                main() {
                    Var a, b: Array[Int, 5] = True, Array(True, Array(False));
                    x = ---- 1 + 2;
                    x = -----1 == 2;
                    x = 1 != 2 + ----- 2;
                    x = 1 ---- 2 + ----- 2;
                    x = 1 > -2;
                    x = 1 < -2 + 2;
                    x = - 1 >= - 2;
                    x = -  1 <= - 2;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(5,IntType),BooleanLit(True)),VarDecl(Id(b),ArrayType(5,IntType),[BooleanLit(True),[BooleanLit(False)]]),AssignStmt(Id(x),BinaryOp(+,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1))))),IntLit(2))),AssignStmt(Id(x),BinaryOp(==,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1)))))),IntLit(2))),AssignStmt(Id(x),BinaryOp(!=,IntLit(1),BinaryOp(+,IntLit(2),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(2))))))))),AssignStmt(Id(x),BinaryOp(+,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(2))))),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(2)))))))),AssignStmt(Id(x),BinaryOp(>,IntLit(1),UnaryOp(-,IntLit(2)))),AssignStmt(Id(x),BinaryOp(<,IntLit(1),BinaryOp(+,UnaryOp(-,IntLit(2)),IntLit(2)))),AssignStmt(Id(x),BinaryOp(>=,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)))),AssignStmt(Id(x),BinaryOp(<=,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2))))]))])])"
        num = 325
        self.assertTrue(TestAST.test(input, expect, num))

    def test26_member_accesss_expression(self):
        input = """
            Class Program {
                main() {
                    Var a: Int;
                    a = a.b;
                    a = a.b.c;
                    a = a.b.c.d(e.f);

                    a = a::$b;
                    a = a::$b.c;
                    a = a::$b.d(e.f);

                    a = a.b(a,b,c);
                    a = a.b(a,b,c).c(a,b,c).d.c;
                    a = a.b(a,b,c).d.c(a,b,c).d(a,b,c);
                    a = a.b.c.d(3,4+5,Array(Array(0))
                                ).e(3,4+5,Array(Array(0)));
                    a = a.d(3,4+5,Array(Array(0))).e(3,
                            4+5,Array(Array(0))).b.c;

                    a = A::$method(abc).method(a,b,c);
                    a = B::$method(abc).method(a,b,c).method(a,b,c);
                    a = C::$method(abc).method(a,b,c).method(a,b,c).attribute;
                    a = D::$method(abc).method(a,b,c).method(a,b,c).attribute.attribute;
                    a = C::$method(abc).method(a,b,c).method(a,b,c).attribute.method(a,b,c).method(a,b,c);
                    a = D::$method(abc).method(a,b,c).method(a,b,c).attribute.attribute.method(a,b,c).attribute.attribute;

                    a = 30+123e1.a.a.a.a();
                    a = 123.12.a(123).a(123).a(123).a(123);

                    a = New X().a;
                    a = New X().a.b;
                    a = New X().a.b.c().d.e.f().g().h.i;
                    a = New X().a.b.c().d.e.f().g().h.i.k().l().m();

                    a = New X().a + New X().a.b.c().d.e.f().g().h.i.k().l().m();
                    a = 5 + New X().a.b[New X().a.b.c().d.e.f().g().h.i[New X().a.b.c().d.e.f().g().h.i.k().l().m()]];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),FieldAccess(Id(a),Id(b))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(a),Id(b)),Id(c))),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[FieldAccess(Id(e),Id(f))])),AssignStmt(Id(a),FieldAccess(Id(a),Id($b))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(a),Id($b)),Id(c))),AssignStmt(Id(a),CallExpr(FieldAccess(Id(a),Id($b)),Id(d),[FieldAccess(Id(e),Id(f))])),AssignStmt(Id(a),CallExpr(Id(a),Id(b),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(Id(a),Id(b),[Id(a),Id(b),Id(c)]),Id(c),[Id(a),Id(b),Id(c)]),Id(d)),Id(c))),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(CallExpr(Id(a),Id(b),[Id(a),Id(b),Id(c)]),Id(d)),Id(c),[Id(a),Id(b),Id(c)]),Id(d),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[IntLit(3),BinaryOp(+,IntLit(4),IntLit(5)),[[IntLit(0)]]]),Id(e),[IntLit(3),BinaryOp(+,IntLit(4),IntLit(5)),[[IntLit(0)]]])),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(Id(a),Id(d),[IntLit(3),BinaryOp(+,IntLit(4),IntLit(5)),[[IntLit(0)]]]),Id(e),[IntLit(3),BinaryOp(+,IntLit(4),IntLit(5)),[[IntLit(0)]]]),Id(b)),Id(c))),AssignStmt(Id(a),CallExpr(CallExpr(Id(A),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(Id(B),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(CallExpr(CallExpr(CallExpr(Id(C),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute))),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(CallExpr(Id(D),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute))),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(CallExpr(CallExpr(CallExpr(Id(C),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(CallExpr(Id(D),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute))),AssignStmt(Id(a),BinaryOp(+,IntLit(30),CallExpr(FieldAccess(FieldAccess(FieldAccess(FloatLit(1230.0),Id(a)),Id(a)),Id(a)),Id(a),[]))),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(CallExpr(FloatLit(123.12),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Id(a),[IntLit(123)])),AssignStmt(Id(a),FieldAccess(NewExpr(Id(X),[]),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b))),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i))),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i)),Id(k),[]),Id(l),[]),Id(m),[])),AssignStmt(Id(a),BinaryOp(+,FieldAccess(NewExpr(Id(X),[]),Id(a)),CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i)),Id(k),[]),Id(l),[]),Id(m),[]))),AssignStmt(Id(a),BinaryOp(+,IntLit(5),ArrayCell(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),[ArrayCell(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i)),[CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i)),Id(k),[]),Id(l),[]),Id(m),[])])])))]))])])"
        num = 326
        self.assertTrue(TestAST.test(input, expect, num))

    def test27_static_method_declaration(self):
        input = """
            Class Program {
                $static_method() {}
                $static_method(x: Int; y: String) {}
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($static_method),Static,[],Block([])),MethodDecl(Id($static_method),Static,[param(Id(x),IntType),param(Id(y),StringType)],Block([]))])])"
        num = 327
        self.assertTrue(TestAST.test(input, expect, num))

    def test28_static_method_declaration(self):
        input = """
            Class Program {
                $static_method() {}
                $static_method(x: Int; y: String) {
                    Val x, y, z: Float = 1, 2, 4;
                }
                Var $x, y: Int = 1, 2;
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($static_method),Static,[],Block([])),MethodDecl(Id($static_method),Static,[param(Id(x),IntType),param(Id(y),StringType)],Block([ConstDecl(Id(x),FloatType,IntLit(1)),ConstDecl(Id(y),FloatType,IntLit(2)),ConstDecl(Id(z),FloatType,IntLit(4))])),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(y),IntType,IntLit(2)))])])"
        num = 328
        self.assertTrue(TestAST.test(input, expect, num))

    def test29_array_of_array_def_type(self):
        input = """
            Class Program {
                main() {
                    Var x, y, z: Array[Array[Int,3], 3] = 1, 2, 3;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),ArrayType(3,ArrayType(3,IntType)),IntLit(1)),VarDecl(Id(y),ArrayType(3,ArrayType(3,IntType)),IntLit(2)),VarDecl(Id(z),ArrayType(3,ArrayType(3,IntType)),IntLit(3))]))])])"
        num = 329
        self.assertTrue(TestAST.test(input, expect, num))

    def test30_array_declaration(self):
        input = """
            Class Program {
                Var a: Array[Int, 05777];
                Var a: Array[Array[Int, 0XFFFF], 0b1001] = Array(1,Array(3,Array(2,4)));
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(3071,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(9,ArrayType(65535,IntType)),[IntLit(1),[IntLit(3),[IntLit(2),IntLit(4)]]]))])])"
        num = 330
        self.assertTrue(TestAST.test(input, expect, num))

    def test31_array_literal(self):
        input = """
            Class Program {
                Val x: Array[Int, 5] = Array(Classname::$a.func().b, Array(1,2,3));
                Var a: Array[Array[Int, 0XFFFF], 0b1001] = 5.4;
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(x),ArrayType(5,IntType),[FieldAccess(CallExpr(FieldAccess(Id(Classname),Id($a)),Id(func),[]),Id(b)),[IntLit(1),IntLit(2),IntLit(3)]])),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(9,ArrayType(65535,IntType)),FloatLit(5.4)))])])"
        num = 331
        self.assertTrue(TestAST.test(input, expect, num))

    def test32_Constructor_Destructor(self):
        input = """
            Class Some_class {
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Var a, b: Array[Int, 1] = Array(), a == 5.4;
                    b = Array();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(1,IntType),[]),VarDecl(Id(b),ArrayType(1,IntType),BinaryOp(==,Id(a),FloatLit(5.4))),AssignStmt(Id(b),[])]))])])"
        num = 332
        self.assertTrue(TestAST.test(input, expect, num))

    def test33_assign_statement_scalar_variable_and_return_stmt(self):
        input = """
            Class Program {
                main() {
                    X::$a = 1;
                    Y::$a = 0xFFFF + 0b1001 - 012345 * 1;

                    arr[1][2] = arr[arr[arr[1] + 03]][1][2][3];
                    Z::$arr[1][2][3] = New A().a[1][2][3] + New B().a()[1][2][3];

                    T::$arr()[1][2][3] = x;
                    M::$arr()[arr[arr[arr[1]]]] = a.b;

                    a.b.c = 1;
                    a::$b = 1;

                    a[1] = 1;
                    a[a[1]][a[a[1]]] = 1;
                    C::$a[C::$a[1]][C::$a[C::$a[1]]][New C(a,b,c,A[B[01]]).a[C::$a[1]]] = 1;

                    New X(a,b,c,A[B[01]]).a = a.b;

                    Self.a()[1][2] = 1;
                    A::$a = 1;
                    New B().a = 1;
                    New X(a,b,c,A[B[01]]).a()[0] = 1;

                    Return "Goodbye";
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(X),Id($a)),IntLit(1)),AssignStmt(FieldAccess(Id(Y),Id($a)),BinaryOp(-,BinaryOp(+,IntLit(65535),IntLit(9)),BinaryOp(*,IntLit(5349),IntLit(1)))),AssignStmt(ArrayCell(Id(arr),[IntLit(1),IntLit(2)]),ArrayCell(Id(arr),[ArrayCell(Id(arr),[BinaryOp(+,ArrayCell(Id(arr),[IntLit(1)]),IntLit(3))]),IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(ArrayCell(FieldAccess(Id(Z),Id($arr)),[IntLit(1),IntLit(2),IntLit(3)]),BinaryOp(+,ArrayCell(FieldAccess(NewExpr(Id(A),[]),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(CallExpr(NewExpr(Id(B),[]),Id(a),[]),[IntLit(1),IntLit(2),IntLit(3)]))),AssignStmt(ArrayCell(CallExpr(Id(T),Id($arr),[]),[IntLit(1),IntLit(2),IntLit(3)]),Id(x)),AssignStmt(ArrayCell(CallExpr(Id(M),Id($arr),[]),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[IntLit(1)])])])]),FieldAccess(Id(a),Id(b))),AssignStmt(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),IntLit(1)),AssignStmt(FieldAccess(Id(a),Id($b)),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])]),IntLit(1)),AssignStmt(ArrayCell(FieldAccess(Id(C),Id($a)),[ArrayCell(FieldAccess(Id(C),Id($a)),[IntLit(1)]),ArrayCell(FieldAccess(Id(C),Id($a)),[ArrayCell(FieldAccess(Id(C),Id($a)),[IntLit(1)])]),ArrayCell(FieldAccess(NewExpr(Id(C),[Id(a),Id(b),Id(c),ArrayCell(Id(A),[ArrayCell(Id(B),[IntLit(1)])])]),Id(a)),[ArrayCell(FieldAccess(Id(C),Id($a)),[IntLit(1)])])]),IntLit(1)),AssignStmt(FieldAccess(NewExpr(Id(X),[Id(a),Id(b),Id(c),ArrayCell(Id(A),[ArrayCell(Id(B),[IntLit(1)])])]),Id(a)),FieldAccess(Id(a),Id(b))),AssignStmt(ArrayCell(CallExpr(Self(),Id(a),[]),[IntLit(1),IntLit(2)]),IntLit(1)),AssignStmt(FieldAccess(Id(A),Id($a)),IntLit(1)),AssignStmt(FieldAccess(NewExpr(Id(B),[]),Id(a)),IntLit(1)),AssignStmt(ArrayCell(CallExpr(NewExpr(Id(X),[Id(a),Id(b),Id(c),ArrayCell(Id(A),[ArrayCell(Id(B),[IntLit(1)])])]),Id(a),[]),[IntLit(0)]),IntLit(1)),Return(StringLit(Goodbye))]))])])"
        num = 333
        self.assertTrue(TestAST.test(input, expect, num))

    def test34_loop_statement_scalar_is_method_call(self):
        input = """
            Class Some_class {
                Constructor(int: Int; string: String) {}
                Constructor() {}
                Destructor() {
                }
            }
            Class Program {
                main() {
                    Foreach(a In 0 .. 100){
                        Continue;
                    }
                    Foreach(h In 0 .. 100 By 2.2e2){
                        Continue;
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(0),IntLit(100),IntLit(1),Block([Continue])]),For(Id(h),IntLit(0),IntLit(100),FloatLit(220.0),Block([Continue])])]))])])"
        num = 334
        self.assertTrue(TestAST.test(input, expect, num))

    def test35_if_statement(self):
        input = r"""
            Class Some_class {
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {
                    }
            }
            Class Program {
                main() {
                    If ("string".a().b[Arr[-1]]) {
                        Var a: Boolean = True;
                    }

                    If ("string".a().b[Arr[-1]]) {
                    }
                    Elseif ("string".a().b[Arr[-1]]) {
                        Var a: Boolean = True;
                        If ("string".a().b[Arr[-1]]) {
                        }
                        Else {
                            Var a: Boolean = True;
                        }
                    }
                    Elseif ("string".a().b[Arr[-1]]) {
                        If ("string".a().b[Arr[-1]]) {
                        }
                        Elseif ("string".a().b[Arr[-1]]) {
                        }
                    }
                    Else {
                        Var a: Boolean = True;
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([]),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([VarDecl(Id(a),BoolType,BooleanLit(True)),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([]),Block([VarDecl(Id(a),BoolType,BooleanLit(True))]))]),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([]),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([])))]),Block([VarDecl(Id(a),BoolType,BooleanLit(True))]))))]))])])"
        num = 335
        self.assertTrue(TestAST.test(input, expect, num))

    def test36_if_statement_incorrect_order(self):
        input = r"""
            Class Some_class {
                Constructor(int: Int; string: String) {}
                Destructor() {
                    If(a>b){}
                    Elseif(b>c){}
                    Else{}
                }
            }
            Class Program {
                main() {}
            }
        """
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([]),If(BinaryOp(>,Id(b),Id(c)),Block([]),Block([])))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        num = 336
        self.assertTrue(TestAST.test(input, expect, num))

    def test37_foreach_statement_continue_outside_loop(self):
        input = """
            Class Some_class {
                    Constructor(int: Int; string: String) {
                        Foreach(d In 1 .. 100 By 1) {
                            If (New A("stringA" + "stringB")) {
                                Continue;
                            }
                            Elseif (New A("stringA" + "stringB")) {
                                Break;
                            }
                            Return False;
                        }
                    }
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Var x: Int = 1;
                    Foreach(i In 1 .. 100 By 101.E-09) {
                        Continue;
                        Break;
                        Foreach(k In 101.E-09 .. 100 ) {
                            x = x + i + j + k;
                            Continue;
                        }
                        If (New A("stringA" + "stringB")) {
                            Break;
                        }
                        Continue;
                        Break;
                    }
                    If (New A("stringA" + "stringB")) {
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([For(Id(d),IntLit(1),IntLit(100),IntLit(1),Block([If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([Continue]),If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([Break]))),Return(BooleanLit(False))])])])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,IntLit(1)),For(Id(i),IntLit(1),IntLit(100),FloatLit(1.01e-07),Block([Continue,Break,For(Id(k),FloatLit(1.01e-07),IntLit(100),IntLit(1),Block([AssignStmt(Id(x),BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(x),Id(i)),Id(j)),Id(k))),Continue])]),If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([Break])),Continue,Break])]),If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([]))]))])])"
        num = 337
        self.assertTrue(TestAST.test(input, expect, num))

    def test38_foreach_statement_other_expr_type(self):
        input = r"""
            Class Program {
                main() {
                    Foreach(i In 100 .. 1 By 1) {
                        If (True || False) {
                            Continue;
                        }
                        Elseif (True && False) {
                            Break;
                        }
                    }
                    Foreach(i In 0 .. New A() By 1+2+3+4) {
                        Foreach(j In New B() .. IdVar) {
                            Foreach(k In -1 .. -100 By (A::$i)+j/(i%j)) {
                            }
                        }
                        If (New A("stringA" + "stringB")) {
                            Continue;
                        }
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(100),IntLit(1),IntLit(1),Block([If(BinaryOp(||,BooleanLit(True),BooleanLit(False)),Block([Continue]),If(BinaryOp(&&,BooleanLit(True),BooleanLit(False)),Block([Break])))])]),For(Id(i),IntLit(0),NewExpr(Id(A),[]),BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),Block([For(Id(j),NewExpr(Id(B),[]),Id(IdVar),IntLit(1),Block([For(Id(k),UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(100)),BinaryOp(+,FieldAccess(Id(A),Id($i)),BinaryOp(/,Id(j),BinaryOp(%,Id(i),Id(j)))),Block([])])])]),If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([Continue]))])])]))])])"
        num = 338
        self.assertTrue(TestAST.test(input, expect, num))

    def test39_foreach_statement_static_expr(self):
        input = r"""
            Class Program {
                Constructor(int: Int; string: String) {}
                Constructor() {}
                Destructor() {}
                main() {
                    Foreach(A In A::$i .. A::$i By A::$i) {}
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([For(Id(A),FieldAccess(Id(A),Id($i)),FieldAccess(Id(A),Id($i)),FieldAccess(Id(A),Id($i)),Block([])])]))])])"
        num = 339
        self.assertTrue(TestAST.test(input, expect, num))

    def test40_simpler_if_statement(self):
        input = r"""
            Class Program {
                main() {
                    If (a == 1) {
                        a = 1;
                    }

                    If (b == 2) {
                        b = 2;
                    }
                    Elseif (c == 3) {
                        c = 3;
                    }
                    Elseif (d == 4) {
                        d = 5;
                    }
                    Else {
                        e = 5;
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(a),IntLit(1)),Block([AssignStmt(Id(a),IntLit(1))])),If(BinaryOp(==,Id(b),IntLit(2)),Block([AssignStmt(Id(b),IntLit(2))]),If(BinaryOp(==,Id(c),IntLit(3)),Block([AssignStmt(Id(c),IntLit(3))]),If(BinaryOp(==,Id(d),IntLit(4)),Block([AssignStmt(Id(d),IntLit(5))]),Block([AssignStmt(Id(e),IntLit(5))]))))]))])])"
        num = 340
        self.assertTrue(TestAST.test(input, expect, num))

    def test41_foreach(self):
        input = """
            Class Program {
                main() {
                    Foreach (hekki In yes .. no By why ) {
                        hello.comeon();
                        Break;
                    }
                    Return;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(hekki),Id(yes),Id(no),Id(why),Block([Call(Id(hello),Id(comeon),[]),Break])]),Return()]))])])"
        num = 341
        self.assertTrue(TestAST.test(input, expect, num))

    def test42_continue(self):
        input = r"""
            Class Program {
                main() {
                    Foreach (hekki In yes .. no By why ) {
                        If (hekki::$i()) {
                            Continue;
                        }
                    }
                    Return;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(hekki),Id(yes),Id(no),Id(why),Block([If(CallExpr(Id(hekki),Id($i),[]),Block([Continue]))])]),Return()]))])])"
        num = 342
        self.assertTrue(TestAST.test(input, expect, num))

    def test43_method_invocation_statement(self):
        input = """
            Class Shape {
                Draw(x, y: Int; size: Float) {
                }
                $Manual(name: Name) {
                    Out.printInt(hekki::$i().arr[x]);
                }
            }
            Class Program {
                main() {
                    Var c: C = New T("string", "abc");
                    x = 12+3==.4/5%6;
                    y = 12+3==.4/5%6;
                    D::$stfoo(12+3==.4/5%6);
                    D::$stfoo(12==3+.4/5%6);
                    c.foo("string");
                    Foreach (a In A::$B(12==3+.4/5%6) .. B.foo(12+3==.4/5%6) By 1) {
                        Self.printInt(hekki::$i().arr[x]);
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Draw),Instance,[param(Id(x),IntType),param(Id(y),IntType),param(Id(size),FloatType)],Block([])),MethodDecl(Id($Manual),Static,[param(Id(name),ClassType(Id(Name)))],Block([Call(Id(Out),Id(printInt),[ArrayCell(FieldAccess(CallExpr(Id(hekki),Id($i),[]),Id(arr)),[Id(x)])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(c),ClassType(Id(C)),NewExpr(Id(T),[StringLit(string),StringLit(abc)])),AssignStmt(Id(x),BinaryOp(==.,BinaryOp(+,IntLit(12),IntLit(3)),BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),IntLit(6)))),AssignStmt(Id(y),BinaryOp(==.,BinaryOp(+,IntLit(12),IntLit(3)),BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),IntLit(6)))),Call(Id(D),Id($stfoo),[BinaryOp(==.,BinaryOp(+,IntLit(12),IntLit(3)),BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),IntLit(6)))]),Call(Id(D),Id($stfoo),[BinaryOp(+.,BinaryOp(==,IntLit(12),IntLit(3)),BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),IntLit(6)))]),Call(Id(c),Id(foo),[StringLit(string)]),For(Id(a),CallExpr(Id(A),Id($B),[BinaryOp(+.,BinaryOp(==,IntLit(12),IntLit(3)),BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),IntLit(6)))]),CallExpr(Id(B),Id(foo),[BinaryOp(==.,BinaryOp(+,IntLit(12),IntLit(3)),BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),IntLit(6)))]),IntLit(1),Block([Call(Self(),Id(printInt),[ArrayCell(FieldAccess(CallExpr(Id(hekki),Id($i),[]),Id(arr)),[Id(x)])])])])]))])])"
        num = 343
        self.assertTrue(TestAST.test(input, expect, num))

    def test44_member_accessing_self_error(self):
        input = """
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
                    Var a: A = New A(1, "abc");
                    Foreach (i In A::$a().c .. B.b().d By A::$a()) {
                        Self.print(i);
                        If (i > 1) {
                            A::$sub_100(i);
                        }
                        Elseif (i < -1) {
                            Self.add_100(i);
                        }
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(add_100),Instance,[param(Id(i),IntType)],Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(100))),Return(Id(i))])),MethodDecl(Id($sub_100),Static,[param(Id(i),IntType)],Block([AssignStmt(Id(i),BinaryOp(-,Id(i),IntLit(100))),Return(Id(i))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[IntLit(1),StringLit(abc)])),For(Id(i),FieldAccess(CallExpr(Id(A),Id($a),[]),Id(c)),FieldAccess(CallExpr(Id(B),Id(b),[]),Id(d)),CallExpr(Id(A),Id($a),[]),Block([Call(Self(),Id(print),[Id(i)]),If(BinaryOp(>,Id(i),IntLit(1)),Block([Call(Id(A),Id($sub_100),[Id(i)])]),If(BinaryOp(<,Id(i),UnaryOp(-,IntLit(1))),Block([Call(Self(),Id(add_100),[Id(i)])])))])])]))])])"
        num = 344
        self.assertTrue(TestAST.test(input, expect, num))

    def test45_mix_member_access_statement(self):
        input = """
            Class Shape {
                Val $numOfShape: Int = 0;
                Var length, width: Int;
                $getNumOfShape() {
                    Return Shape::$numOfShape;
                }
                getLength() {
                    Return Self.legnth;
                }
                getWidth() {
                    Return Self.width;
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
                    OutStream::$printInt(shape.numOfShape);
                }
            }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(Shape),Id($numOfShape)))])),MethodDecl(Id(getLength),Instance,[],Block([Return(FieldAccess(Self(),Id(legnth)))])),MethodDecl(Id(getWidth),Instance,[],Block([Return(FieldAccess(Self(),Id(width)))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),Call(Id(OutStream),Id($printInt),[FieldAccess(Id(shape),Id(numOfShape))])]))])])"
        num = 345
        self.assertTrue(TestAST.test(input, expect, num))

    def test46_block_statement_in_block_statement(self):
        input = """
            Class Program {
                $Method() {
                    Console.log(1);
                    Console::$log(1);
                        ## Comment in block ##
                }
                Var x, y: Int = 1, "str";
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Method),Static,[],Block([Call(Id(Console),Id(log),[IntLit(1)]),Call(Id(Console),Id($log),[IntLit(1)])])),AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(y),IntType,StringLit(str)))])])"""
        num = 246
        self.assertTrue(TestAST.test(input, expect, num))

    def test47_multiple_main_program(self):
        input = """
            Class NotProgram {
                main(a,b: Int; c,d: Pointer) {
                    System.Out.Println(1);
                }
                main() {
                    System.Out.Println(1);
                }
            }
            Class Program {
                Var x: Int = 1;
                main(a,b: Int; c,d: Pointer){
                    Var x: Int = 1;
                }
                main() {
                    Var x: Int = 1;
                }
            }
        """
        expect = "Program([ClassDecl(Id(NotProgram),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),ClassType(Id(Pointer))),param(Id(d),ClassType(Id(Pointer)))],Block([Call(FieldAccess(Id(System),Id(Out)),Id(Println),[IntLit(1)])])),MethodDecl(Id(main),Instance,[],Block([Call(FieldAccess(Id(System),Id(Out)),Id(Println),[IntLit(1)])]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(1))),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),ClassType(Id(Pointer))),param(Id(d),ClassType(Id(Pointer)))],Block([VarDecl(Id(x),IntType,IntLit(1))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,IntLit(1))]))])])"
        num = 247
        self.assertTrue(TestAST.test(input, expect, num))

    def test48_method_lack_argument_parenthese(self):
        input = """
            Class Program {
                if (xfunction_pararter: Int; b: Float){

                }
                main (){
                    Console.log(1);
                }
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(if),Instance,[param(Id(xfunction_pararter),IntType),param(Id(b),FloatType)],Block([])),MethodDecl(Id(main),Static,[],Block([Call(Id(Console),Id(log),[IntLit(1)])]))])])"""
        num = 348
        self.assertTrue(TestAST.test(input, expect, num))

    def test49_self_access_and_null_literal(self):
        input = """
            Class Program {
                main() {
                    A.a = Null;
                    Self.A(Null, Null, Null);
                    C::$static = Null;
                    D::$method(Null);
                    variable = Null;
                    Val a,b,c: Array[Int,3] = Null, Null, Null;
                    Val a,b,c: Classname = Null, Null, Null;
                }
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(A),Id(a)),NullLiteral()),Call(Self(),Id(A),[NullLiteral(),NullLiteral(),NullLiteral()]),AssignStmt(FieldAccess(Id(C),Id($static)),NullLiteral()),Call(Id(D),Id($method),[NullLiteral()]),AssignStmt(Id(variable),NullLiteral()),ConstDecl(Id(a),ArrayType(3,IntType),NullLiteral()),ConstDecl(Id(b),ArrayType(3,IntType),NullLiteral()),ConstDecl(Id(c),ArrayType(3,IntType),NullLiteral()),ConstDecl(Id(a),ClassType(Id(Classname)),NullLiteral()),ConstDecl(Id(b),ClassType(Id(Classname)),NullLiteral()),ConstDecl(Id(c),ClassType(Id(Classname)),NullLiteral())]))])])"""
        num = 349
        self.assertTrue(TestAST.test(input, expect, num))

    def test50_if_statement_inside_loop_statement(self):
        input = """
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
                    Var a: A = New A(1, "abc");
                    If (i > 1) {
                        A::$sub_100(i);
                        Foreach (i In 1 .. 100 By A::$a()) {
                            Self.print(i);
                            If (i > 1) {
                                A::$sub_100(i);
                                Continue;
                            }
                            Elseif (i < -1) {
                                Self.add_100(i);
                            }
                            Break;
                        }

                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(add_100),Instance,[param(Id(i),IntType)],Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(100))),Return(Id(i))])),MethodDecl(Id($sub_100),Static,[param(Id(i),IntType)],Block([AssignStmt(Id(i),BinaryOp(-,Id(i),IntLit(100))),Return(Id(i))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[IntLit(1),StringLit(abc)])),If(BinaryOp(>,Id(i),IntLit(1)),Block([Call(Id(A),Id($sub_100),[Id(i)]),For(Id(i),IntLit(1),IntLit(100),CallExpr(Id(A),Id($a),[]),Block([Call(Self(),Id(print),[Id(i)]),If(BinaryOp(>,Id(i),IntLit(1)),Block([Call(Id(A),Id($sub_100),[Id(i)]),Continue]),If(BinaryOp(<,Id(i),UnaryOp(-,IntLit(1))),Block([Call(Self(),Id(add_100),[Id(i)])]))),Break])])]))]))])])"
        num = 350
        self.assertTrue(TestAST.test(input, expect, num))

    def test51_multi_demensional_array(self):
        input = """
            Class Program {
                main() {
                    a = Array(
                        Array(1,2,3),
                        Array(Array(1,2,3), Array(1,2,3,4), Array(1,2,3,4,5)),
                        a[Array(1,2,3)][a[Array(1,2,3)]],
                        New X(Array("1","2","3"))
                    );
                }
            }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),[[IntLit(1),IntLit(2),IntLit(3)],[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]],ArrayCell(Id(a),[[IntLit(1),IntLit(2),IntLit(3)],ArrayCell(Id(a),[[IntLit(1),IntLit(2),IntLit(3)]])]),NewExpr(Id(X),[[StringLit(1),StringLit(2),StringLit(3)]])])]))])])"""
        num = 351
        self.assertTrue(TestAST.test(input, expect, num))

    def test52_float_literal(self):
        input = r"""
            Class Program {
                Var x1: Float = 1.123;
                Var x2: Float = 1.123e2;
                Var x3: Float = 1.123e+2;
                Var x4: Float = 1.123e-2;
                Var x5: Float = 1.e123;
                Var x6: Float = 1.e-123;
                Var x7: Float = 1.e+123;
                Var x8: Float = 1e123;
                Var x9: Float = 1e-123;
                Var x10: Float = 1e+123;
                Var x11: Float = .e123;
                Var x12: Float = .e-123;
                Var x13: Float = .e+123;
                Var x14: Float = .1e123;
                Var x15: Float = .1e-123;
                Var x16: Float = .1e+123;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x1),FloatType,FloatLit(1.123))),AttributeDecl(Instance,VarDecl(Id(x2),FloatType,FloatLit(112.3))),AttributeDecl(Instance,VarDecl(Id(x3),FloatType,FloatLit(112.3))),AttributeDecl(Instance,VarDecl(Id(x4),FloatType,FloatLit(0.01123))),AttributeDecl(Instance,VarDecl(Id(x5),FloatType,FloatLit(1e+123))),AttributeDecl(Instance,VarDecl(Id(x6),FloatType,FloatLit(1e-123))),AttributeDecl(Instance,VarDecl(Id(x7),FloatType,FloatLit(1e+123))),AttributeDecl(Instance,VarDecl(Id(x8),FloatType,FloatLit(1e+123))),AttributeDecl(Instance,VarDecl(Id(x9),FloatType,FloatLit(1e-123))),AttributeDecl(Instance,VarDecl(Id(x10),FloatType,FloatLit(1e+123))),AttributeDecl(Instance,VarDecl(Id(x11),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(x12),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(x13),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(x14),FloatType,FloatLit(1e+122))),AttributeDecl(Instance,VarDecl(Id(x15),FloatType,FloatLit(1e-124))),AttributeDecl(Instance,VarDecl(Id(x16),FloatType,FloatLit(1e+122)))])])"
        num = 352
        self.assertTrue(TestAST.test(input, expect, num))

    def test53_left_hand_size(self):
        input = r"""
            Class Program {
                main() {
                    a = New X();
                    a = "String";
                    a[1] = "String";
                    a[1][1][1] = "String";
                    a[a[a[a[1]]]][a[a[a]]] = "String";
                    a.a = "String";
                    a.a.a = "String";
                    A::$a = "String";
                    A::$a.a = "String";
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(X),[])),AssignStmt(Id(a),StringLit(String)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),StringLit(String)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1)]),StringLit(String)),AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])]),ArrayCell(Id(a),[ArrayCell(Id(a),[Id(a)])])]),StringLit(String)),AssignStmt(FieldAccess(Id(a),Id(a)),StringLit(String)),AssignStmt(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),StringLit(String)),AssignStmt(FieldAccess(Id(A),Id($a)),StringLit(String)),AssignStmt(FieldAccess(FieldAccess(Id(A),Id($a)),Id(a)),StringLit(String))]))])])"
        num = 353
        self.assertTrue(TestAST.test(input, expect, num))

    def test54_member_access(self):
        input = """
            Class Program {
                main() {
                    a = a.b.c;
                    a = Class_name::$a;
                    a = Class_name::$a.a.a.a();
                    a = Self.a;
                    a = Self.self.a;
                    a = Self;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),FieldAccess(FieldAccess(Id(a),Id(b)),Id(c))),AssignStmt(Id(a),FieldAccess(Id(Class_name),Id($a))),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Class_name),Id($a)),Id(a)),Id(a)),Id(a),[])),AssignStmt(Id(a),FieldAccess(Self(),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(Self(),Id(self)),Id(a))),AssignStmt(Id(a),Self())]))])])"
        num = 354
        self.assertTrue(TestAST.test(input, expect, num))

    def test55_var_decl_attr_decl(self):
        input = """
            Class Program {
                Var a,b,$c: Int = 1,2,3;
                main() {
                    Var a,b,c,d: Int = 1,2,3,4;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(3))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),IntType,IntLit(2)),VarDecl(Id(c),IntType,IntLit(3)),VarDecl(Id(d),IntType,IntLit(4))]))])])"
        num = 355
        self.assertTrue(TestAST.test(input, expect, num))

    def test56_scalar_is_funcall_accessing_member(self):
        input = """
            Class Program {
                main() {
                    A.c().b = 1;
                    A::$staticMethod().d = 1;
                    A::$staticMethod().d.e()[0] = 1;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(CallExpr(Id(A),Id(c),[]),Id(b)),IntLit(1)),AssignStmt(FieldAccess(CallExpr(Id(A),Id($staticMethod),[]),Id(d)),IntLit(1)),AssignStmt(ArrayCell(CallExpr(FieldAccess(CallExpr(Id(A),Id($staticMethod),[]),Id(d)),Id(e),[]),[IntLit(0)]),IntLit(1))]))])])"
        num = 356
        self.assertTrue(TestAST.test(input, expect, num))

    def test57_foreach_stmt_with_SEMI(self):
        input = """
        Class Program {
            main() {
                "1".a = a.b;
            }
        }
        Class Program {
            main() {
                "1".a = a.b;
                Foreach (A In A::$B(12==3+.4/5%6) .. B.foo(12+3==.4/5%6) By 1) {
                    Self.printInt(hekki::$i().arr[x]);
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(StringLit(1),Id(a)),FieldAccess(Id(a),Id(b)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(StringLit(1),Id(a)),FieldAccess(Id(a),Id(b))),For(Id(A),CallExpr(Id(A),Id($B),[BinaryOp(+.,BinaryOp(==,IntLit(12),IntLit(3)),BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),IntLit(6)))]),CallExpr(Id(B),Id(foo),[BinaryOp(==.,BinaryOp(+,IntLit(12),IntLit(3)),BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),IntLit(6)))]),IntLit(1),Block([Call(Self(),Id(printInt),[ArrayCell(FieldAccess(CallExpr(Id(hekki),Id($i),[]),Id(arr)),[Id(x)])])])])]))])])"
        num = 357
        self.assertTrue(TestAST.test(input, expect, num))

    def test58_if_stmt(self):
        input = """
        Class Program {
            main() {
                "1".a = a.b;
            }
        }
        Class Program {
            main() {
                "1".a = a.b;
                If (i > 1) {
                    A::$sub_100(i);
                }
                Elseif (i < -1) {
                    a.add_100(i);
                }
                Else {}
                "1".a = a.b;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(StringLit(1),Id(a)),FieldAccess(Id(a),Id(b)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(StringLit(1),Id(a)),FieldAccess(Id(a),Id(b))),If(BinaryOp(>,Id(i),IntLit(1)),Block([Call(Id(A),Id($sub_100),[Id(i)])]),If(BinaryOp(<,Id(i),UnaryOp(-,IntLit(1))),Block([Call(Id(a),Id(add_100),[Id(i)])]),Block([]))),AssignStmt(FieldAccess(StringLit(1),Id(a)),FieldAccess(Id(a),Id(b)))]))])])"
        num = 358
        self.assertTrue(TestAST.test(input, expect, num))

    def test59_static_attr_static_method_access(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    $getNumOfShape() {
        Classname::$numOfShape = $numOfShape;
        Return Hello::$numOfShape();
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
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([AssignStmt(FieldAccess(Id(Classname),Id($numOfShape)),None),Return(CallExpr(Id(Hello),Id($numOfShape),[]))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        num = 359
        self.assertTrue(TestAST.test(input, expect, num))

    def test60_static_attr_static_method_direct_access_as_an_expr(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    $getNumOfShape() {
        Classname::$numOfShape = $numOfShape;
        Return numOfShape;
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
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([AssignStmt(FieldAccess(Id(Classname),Id($numOfShape)),None),Return(Id(numOfShape))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        num = 360
        self.assertTrue(TestAST.test(input, expect, num))

    def test61_Null_accessing_member(self):
        input = r"""
            Class Program {
                main() {
                    Null.a();
                    Null.a.a.a();
                    Null.a();
                    Null.a.a.a();
                    Null.a().a().a();
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(NullLiteral(),Id(a),[]),Call(FieldAccess(FieldAccess(NullLiteral(),Id(a)),Id(a)),Id(a),[]),Call(NullLiteral(),Id(a),[]),Call(FieldAccess(FieldAccess(NullLiteral(),Id(a)),Id(a)),Id(a),[]),Call(CallExpr(CallExpr(NullLiteral(),Id(a),[]),Id(a),[]),Id(a),[])]))])])"
        num = 361
        self.assertTrue(TestAST.test(input, expect, num))

    def test62_operation_expr_with_Null(self):
        input = r"""
            Class Program {
                main() {
                    a.a()[0] = Null + Null;
                    b = arr[Null];
                    c = arr[arr[Null]][Null];
                    d = Null +. Null ;
                    e = ----Null -- Null / Null % Null * Null ==. Null + Null;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(CallExpr(Id(a),Id(a),[]),[IntLit(0)]),BinaryOp(+,NullLiteral(),NullLiteral())),AssignStmt(Id(b),ArrayCell(Id(arr),[NullLiteral()])),AssignStmt(Id(c),ArrayCell(Id(arr),[ArrayCell(Id(arr),[NullLiteral()]),NullLiteral()])),AssignStmt(Id(d),BinaryOp(+.,NullLiteral(),NullLiteral())),AssignStmt(Id(e),BinaryOp(==.,BinaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,NullLiteral())))),BinaryOp(*,BinaryOp(%,BinaryOp(/,UnaryOp(-,NullLiteral()),NullLiteral()),NullLiteral()),NullLiteral())),BinaryOp(+,NullLiteral(),NullLiteral())))]))])])"
        num = 362
        self.assertTrue(TestAST.test(input, expect, num))

    def test63_operation_expr_with_Null_with_parenth(self):
        input = r"""
            Class Program {
                main() {
                    a.a()[0] = Null + Null;
                    b = arr[Null];
                    c = arr[arr[Null]][Null];
                    d = Null +. Null ;
                    e = ----Null -- Null / Null % Null * (Null ==. Null) + (Null +. Null);
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(CallExpr(Id(a),Id(a),[]),[IntLit(0)]),BinaryOp(+,NullLiteral(),NullLiteral())),AssignStmt(Id(b),ArrayCell(Id(arr),[NullLiteral()])),AssignStmt(Id(c),ArrayCell(Id(arr),[ArrayCell(Id(arr),[NullLiteral()]),NullLiteral()])),AssignStmt(Id(d),BinaryOp(+.,NullLiteral(),NullLiteral())),AssignStmt(Id(e),BinaryOp(+,BinaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,NullLiteral())))),BinaryOp(*,BinaryOp(%,BinaryOp(/,UnaryOp(-,NullLiteral()),NullLiteral()),NullLiteral()),BinaryOp(==.,NullLiteral(),NullLiteral()))),BinaryOp(+.,NullLiteral(),NullLiteral())))]))])])"
        num = 363
        self.assertTrue(TestAST.test(input, expect, num))

    def test64_multi_class_inheritance(self):
        input = """
            Class Shape {}
            Class Circle : Shape {}
            Class Rectangle : Shape {}
            Class Program {}
        """
        expect = "Program([ClassDecl(Id(Shape),[]),ClassDecl(Id(Circle),Id(Shape),[]),ClassDecl(Id(Rectangle),Id(Shape),[]),ClassDecl(Id(Program),[])])"
        num = 364
        self.assertTrue(TestAST.test(input, expect, num))

    def test65_simple_program_with_class(self):
        input = r"""
            Class Author {
                Var user_name: String;
            }
            Class Program {
                Val author, illustrator: Author;
                main() {}
            }
        """
        expect = r"Program([ClassDecl(Id(Author),[AttributeDecl(Instance,VarDecl(Id(user_name),StringType))]),ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(author),ClassType(Id(Author)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(illustrator),ClassType(Id(Author)),NullLiteral())),MethodDecl(Id(main),Static,[],Block([]))])])"
        num = 365
        self.assertTrue(TestAST.test(input, expect, num))

    def test66_complex_program(self):
        input = r"""
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
        a.a()[0] = Null + Null;
        b = arr[Null];
        c = arr[arr[Null]][Null];
        d = Null +. Null ;
        e = ----Null -- Null / Null % Null * (Null ==. Null) + (Null +. Null);
        Var a: A = New A(1, "abc");
        Val b: C = A::$a();
        Foreach (i In 1 .. 100 By A::$a()) {
            Self.print(i);
            If (i > 1) {
                A::$sub_100(i);
            }
        }
    }
}
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(add_100),Instance,[param(Id(i),IntType)],Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(100))),Return(Id(i))])),MethodDecl(Id($sub_100),Static,[param(Id(i),IntType)],Block([AssignStmt(Id(i),BinaryOp(-,Id(i),IntLit(100))),Return(Id(i))])),MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(CallExpr(Id(a),Id(a),[]),[IntLit(0)]),BinaryOp(+,NullLiteral(),NullLiteral())),AssignStmt(Id(b),ArrayCell(Id(arr),[NullLiteral()])),AssignStmt(Id(c),ArrayCell(Id(arr),[ArrayCell(Id(arr),[NullLiteral()]),NullLiteral()])),AssignStmt(Id(d),BinaryOp(+.,NullLiteral(),NullLiteral())),AssignStmt(Id(e),BinaryOp(+,BinaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,NullLiteral())))),BinaryOp(*,BinaryOp(%,BinaryOp(/,UnaryOp(-,NullLiteral()),NullLiteral()),NullLiteral()),BinaryOp(==.,NullLiteral(),NullLiteral()))),BinaryOp(+.,NullLiteral(),NullLiteral()))),VarDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[IntLit(1),StringLit(abc)])),ConstDecl(Id(b),ClassType(Id(C)),CallExpr(Id(A),Id($a),[])),For(Id(i),IntLit(1),IntLit(100),CallExpr(Id(A),Id($a),[]),Block([Call(Self(),Id(print),[Id(i)]),If(BinaryOp(>,Id(i),IntLit(1)),Block([Call(Id(A),Id($sub_100),[Id(i)])]))])])]))])])"
        num = 366
        self.assertTrue(TestAST.test(input, expect, num))

    def test67_class_inheritance(self):
        input = """
Class Out {
    Constructor(){}
    Destructor(){}
    print(el: Element){}
    print(str: String){}
    print(x: Int){}
}

Class Cin {
    Constructor(){}
    Destructor(){}
    input(){
        Val result: Int = 0;
        Return result;
    }
}

Class System {
    Constructor(){
        Self.out = New Out();
        Self.in = New Cin();
    }
    Destructor(){}
    Var out: Out = Null;
    Var in: Cin = Null;
    len(arr: Array[Int, 10000]){
        Var length: Int;
        Return length;
    }
}

Class Element {
    Val $system: System = New System();
    Var $st1, $st2: Array[Int, 2];
    Var x1, x2: Int = 0, 1;
    Var str1, str2: String = "Hello", "Friend";
    Var f1, f2: Float;
    Var arr1, arr2: Array[Array[String, 0XABCDE12], 0B100101] = Array(), Array(Array(0,1), Array(0,2));
    Var c1, c2: Element = Null, New Element();
    Constructor(){
        Element::$st1 = Array(0,1);
        Element::$st2 = Array("x","y");
        Self.f1 = 0.0e1;
        Self.f2 = 1.234e-1;
    }
    Constructor(x1, x2: Int; str1, str2: String; f1,f2: Float; arr1, arr2: Array[Array[String, 0XABCDE12], 01237]; c1, c2: Element){
        Var var1, var2: Int = 0, 1;
        Self.x1 = x1; Self.x2 = x2;
        Self.str1 = str1; Self.str2 = str2;
        Self.f1 = f1; Self.f2 = f2;
        Self.arr1 = arr1; Self.arr2 = arr2;
        Self.c1 = c1; Self.c2 = c2;
    }
    Destructor(){}
    $staticFunction1(p1, p2: Int; p3, p4: String; c1, c2: Element) {
        Element::$system.out.print("Element::$StaticFunction1(...)");
    }

    $quickSort(arr: Array[Float, 10000]; size: Int){
        Element::$recursiveQuickSort(arr, 0, size - 1);
    }

    $recursiveQuickSort(arr: Array[Float, 10000]; low: Int; high: Int){
        If(low == high){
            Return arr;
        }
        Elseif(low < hight){
            Var pi: Int;
            pi = Element::$partition(arr, low, high);

            Element::$quickSort(arr, low, pi - 1);
            Element::$quickSort(arr, pi + 1, high);
        }
    }

    $partition(arr: Array[Int, 10000]; low: Int; high: Int){
        Var i, j: Int = low - 1, 0;
        Var pivot: Int = arr[high];
        Foreach (j In low .. high By 1){
            If (arr[j] <= pivot) {
                i = i + 1;
                Var temp: Int;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            Else {
                Continue;
            }
        }
        Var temp: Int;
        temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        Return i + 1;
    }
}
Class SortElement : Element {
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
        Self.str1 = el.str1; Self.str2 = el.str2;
        Self.f1 = el.f1; Self.f2 = el.f2;
        Self.arr1 = el.arr1; Self.arr2 = el.arr2;
        Self.c1 = el.c1; Self.c2 = el.c2;
    }
    printArray1or2(number: Int) {
        If (number == 1) {
            Var x: Int;
            Foreach(x In 0 .. Element::$system.len(Self.arr1)) {
                Element::$system.out.print(x);
                Element::$system.out.print(" ");
            }
        }
        Elseif (number == 2) {
            Foreach(x In 0 .. Element::$system.len(Self.arr2)) {
                Element::$system.out.print(x);
                Element::$system.out.print(" ");
            }
        }
        Else {
            Element::$system.out.print("Invalid array number");
        }
    }
}
Class MonthElement : Element {
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
        Self.str1 = el.str1; Self.str2 = el.str2;
        Self.f1 = el.f1; Self.f2 = el.f2;
        Self.arr1 = el.arr1; Self.arr2 = el.arr2;
        Self.c1 = el.c1; Self.c2 = el.c2;
    }
    daysInMonth() {
        Var month: Int = Element::$system.in.input();
        If(month == 2) {
            Element::$system.out.print(28);
            Return 28;
        }
        Elseif ((month == 4) || (month == 6) || (month == 9) || (month == 11)) {
            Element::$system.out.print(30);
            Return 30;
        }
        Elseif ((month == 1) || (month == 3) || (month == 5) || (month == 7) || (month == 8) || (month == 10) || (month == 12)) {
            Element::$system.out.print(31);
            Return 31;
        }
        Else {
            Element::$system.out.print("Invalid month number");
            Return -1;
        }
    }
}
Class Program {
    main(){
        Var element1, element2, element3: Element = New Element(), New Element(), New Element(10,20,"str1","str2",1.2e1,-1.2e2, Array(), Array(Array(1,2), Array(3,4)), element1, element2);
        Var element3, element4: Element;
    }
}
        """
        expect = "Program([ClassDecl(Id(Out),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(print),Instance,[param(Id(el),ClassType(Id(Element)))],Block([])),MethodDecl(Id(print),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([]))]),ClassDecl(Id(Cin),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(input),Instance,[],Block([ConstDecl(Id(result),IntType,IntLit(0)),Return(Id(result))]))]),ClassDecl(Id(System),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(out)),NewExpr(Id(Out),[])),AssignStmt(FieldAccess(Self(),Id(in)),NewExpr(Id(Cin),[]))])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(out),ClassType(Id(Out)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(in),ClassType(Id(Cin)),NullLiteral())),MethodDecl(Id(len),Instance,[param(Id(arr),ArrayType(10000,IntType))],Block([VarDecl(Id(length),IntType),Return(Id(length))]))]),ClassDecl(Id(Element),[AttributeDecl(Static,ConstDecl(Id($system),ClassType(Id(System)),NewExpr(Id(System),[]))),AttributeDecl(Static,VarDecl(Id($st1),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($st2),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(x1),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(x2),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(str1),StringType,StringLit(Hello))),AttributeDecl(Instance,VarDecl(Id(str2),StringType,StringLit(Friend))),AttributeDecl(Instance,VarDecl(Id(f1),FloatType)),AttributeDecl(Instance,VarDecl(Id(f2),FloatType)),AttributeDecl(Instance,VarDecl(Id(arr1),ArrayType(37,ArrayType(180149778,StringType)),[])),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(37,ArrayType(180149778,StringType)),[[IntLit(0),IntLit(1)],[IntLit(0),IntLit(2)]])),AttributeDecl(Instance,VarDecl(Id(c1),ClassType(Id(Element)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c2),ClassType(Id(Element)),NewExpr(Id(Element),[]))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Element),Id($st1)),[IntLit(0),IntLit(1)]),AssignStmt(FieldAccess(Id(Element),Id($st2)),[StringLit(x),StringLit(y)]),AssignStmt(FieldAccess(Self(),Id(f1)),FloatLit(0.0)),AssignStmt(FieldAccess(Self(),Id(f2)),FloatLit(0.1234))])),MethodDecl(Id(Constructor),Instance,[param(Id(x1),IntType),param(Id(x2),IntType),param(Id(str1),StringType),param(Id(str2),StringType),param(Id(f1),FloatType),param(Id(f2),FloatType),param(Id(arr1),ArrayType(671,ArrayType(180149778,StringType))),param(Id(arr2),ArrayType(671,ArrayType(180149778,StringType))),param(Id(c1),ClassType(Id(Element))),param(Id(c2),ClassType(Id(Element)))],Block([VarDecl(Id(var1),IntType,IntLit(0)),VarDecl(Id(var2),IntType,IntLit(1)),AssignStmt(FieldAccess(Self(),Id(x1)),Id(x1)),AssignStmt(FieldAccess(Self(),Id(x2)),Id(x2)),AssignStmt(FieldAccess(Self(),Id(str1)),Id(str1)),AssignStmt(FieldAccess(Self(),Id(str2)),Id(str2)),AssignStmt(FieldAccess(Self(),Id(f1)),Id(f1)),AssignStmt(FieldAccess(Self(),Id(f2)),Id(f2)),AssignStmt(FieldAccess(Self(),Id(arr1)),Id(arr1)),AssignStmt(FieldAccess(Self(),Id(arr2)),Id(arr2)),AssignStmt(FieldAccess(Self(),Id(c1)),Id(c1)),AssignStmt(FieldAccess(Self(),Id(c2)),Id(c2))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id($staticFunction1),Static,[param(Id(p1),IntType),param(Id(p2),IntType),param(Id(p3),StringType),param(Id(p4),StringType),param(Id(c1),ClassType(Id(Element))),param(Id(c2),ClassType(Id(Element)))],Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Element::$StaticFunction1(...))])])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Id(Element),Id($recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])])),MethodDecl(Id($recursiveQuickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(low),IntType),param(Id(high),IntType)],Block([If(BinaryOp(==,Id(low),Id(high)),Block([Return(Id(arr))]),If(BinaryOp(<,Id(low),Id(hight)),Block([VarDecl(Id(pi),IntType),AssignStmt(Id(pi),CallExpr(Id(Element),Id($partition),[Id(arr),Id(low),Id(high)])),Call(Id(Element),Id($quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),IntLit(1))]),Call(Id(Element),Id($quickSort),[Id(arr),BinaryOp(+,Id(pi),IntLit(1)),Id(high)])])))])),MethodDecl(Id($partition),Static,[param(Id(arr),ArrayType(10000,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([VarDecl(Id(i),IntType,BinaryOp(-,Id(low),IntLit(1))),VarDecl(Id(j),IntType,IntLit(0)),VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(high)])),For(Id(j),Id(low),Id(high),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))]),Block([Continue]))])]),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))]),ArrayCell(Id(arr),[Id(high)])),AssignStmt(ArrayCell(Id(arr),[Id(high)]),Id(temp)),Return(BinaryOp(+,Id(i),IntLit(1)))]))]),ClassDecl(Id(SortElement),Id(Element),[MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2))),AssignStmt(FieldAccess(Self(),Id(str1)),FieldAccess(Id(el),Id(str1))),AssignStmt(FieldAccess(Self(),Id(str2)),FieldAccess(Id(el),Id(str2))),AssignStmt(FieldAccess(Self(),Id(f1)),FieldAccess(Id(el),Id(f1))),AssignStmt(FieldAccess(Self(),Id(f2)),FieldAccess(Id(el),Id(f2))),AssignStmt(FieldAccess(Self(),Id(arr1)),FieldAccess(Id(el),Id(arr1))),AssignStmt(FieldAccess(Self(),Id(arr2)),FieldAccess(Id(el),Id(arr2))),AssignStmt(FieldAccess(Self(),Id(c1)),FieldAccess(Id(el),Id(c1))),AssignStmt(FieldAccess(Self(),Id(c2)),FieldAccess(Id(el),Id(c2)))])),MethodDecl(Id(printArray1or2),Instance,[param(Id(number),IntType)],Block([If(BinaryOp(==,Id(number),IntLit(1)),Block([VarDecl(Id(x),IntType),For(Id(x),IntLit(0),CallExpr(FieldAccess(Id(Element),Id($system)),Id(len),[FieldAccess(Self(),Id(arr1))]),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[Id(x)]),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit( )])])])]),If(BinaryOp(==,Id(number),IntLit(2)),Block([For(Id(x),IntLit(0),CallExpr(FieldAccess(Id(Element),Id($system)),Id(len),[FieldAccess(Self(),Id(arr2))]),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[Id(x)]),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit( )])])])]),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Invalid array number)])])))]))]),ClassDecl(Id(MonthElement),Id(Element),[MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2))),AssignStmt(FieldAccess(Self(),Id(str1)),FieldAccess(Id(el),Id(str1))),AssignStmt(FieldAccess(Self(),Id(str2)),FieldAccess(Id(el),Id(str2))),AssignStmt(FieldAccess(Self(),Id(f1)),FieldAccess(Id(el),Id(f1))),AssignStmt(FieldAccess(Self(),Id(f2)),FieldAccess(Id(el),Id(f2))),AssignStmt(FieldAccess(Self(),Id(arr1)),FieldAccess(Id(el),Id(arr1))),AssignStmt(FieldAccess(Self(),Id(arr2)),FieldAccess(Id(el),Id(arr2))),AssignStmt(FieldAccess(Self(),Id(c1)),FieldAccess(Id(el),Id(c1))),AssignStmt(FieldAccess(Self(),Id(c2)),FieldAccess(Id(el),Id(c2)))])),MethodDecl(Id(daysInMonth),Instance,[],Block([VarDecl(Id(month),IntType,CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),If(BinaryOp(==,Id(month),IntLit(2)),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(28)]),Return(IntLit(28))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(month),IntLit(4)),BinaryOp(==,Id(month),IntLit(6))),BinaryOp(==,Id(month),IntLit(9))),BinaryOp(==,Id(month),IntLit(11))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(30)]),Return(IntLit(30))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(month),IntLit(1)),BinaryOp(==,Id(month),IntLit(3))),BinaryOp(==,Id(month),IntLit(5))),BinaryOp(==,Id(month),IntLit(7))),BinaryOp(==,Id(month),IntLit(8))),BinaryOp(==,Id(month),IntLit(10))),BinaryOp(==,Id(month),IntLit(12))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(31)]),Return(IntLit(31))]),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Invalid month number)]),Return(UnaryOp(-,IntLit(1)))]))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(element1),ClassType(Id(Element)),NewExpr(Id(Element),[])),VarDecl(Id(element2),ClassType(Id(Element)),NewExpr(Id(Element),[])),VarDecl(Id(element3),ClassType(Id(Element)),NewExpr(Id(Element),[IntLit(10),IntLit(20),StringLit(str1),StringLit(str2),FloatLit(12.0),UnaryOp(-,FloatLit(120.0)),[],[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)]],Id(element1),Id(element2)])),VarDecl(Id(element3),ClassType(Id(Element)),NullLiteral()),VarDecl(Id(element4),ClassType(Id(Element)),NullLiteral())]))])])"
        num = 367
        self.assertTrue(TestAST.test(input, expect, num))

    def test68_class_type_not_initialize(self):
        input = """
            Class Program {
                Var c1: A = New A();
                Var c1: A;

                Var $c2: A = New A();
                Var $c2: A;

                Var c3: A = New A();
                Val c3: A;

                Var $c3: A = New A();
                Val $c3: A;
                method() {
                    Var x: A;
                    Var x: A = New A();

                    Val y: A;
                    Var y: A = New A();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(c1),ClassType(Id(A)),NewExpr(Id(A),[]))),AttributeDecl(Instance,VarDecl(Id(c1),ClassType(Id(A)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($c2),ClassType(Id(A)),NewExpr(Id(A),[]))),AttributeDecl(Static,VarDecl(Id($c2),ClassType(Id(A)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c3),ClassType(Id(A)),NewExpr(Id(A),[]))),AttributeDecl(Instance,ConstDecl(Id(c3),ClassType(Id(A)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($c3),ClassType(Id(A)),NewExpr(Id(A),[]))),AttributeDecl(Static,ConstDecl(Id($c3),ClassType(Id(A)),NullLiteral())),MethodDecl(Id(method),Instance,[],Block([VarDecl(Id(x),ClassType(Id(A)),NullLiteral()),VarDecl(Id(x),ClassType(Id(A)),NewExpr(Id(A),[])),ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()),VarDecl(Id(y),ClassType(Id(A)),NewExpr(Id(A),[]))]))])])"
        num = 368
        self.assertTrue(TestAST.test(input, expect, num))

    def test69(self):
        input = """
Class Out {
    Constructor(){}
    Destructor(){}
    print(el: Element){}
    print(str: String){}
    print(x: Int){}
}

Class Cin {
    Constructor(){}
    Destructor(){}
    input(){
        Val result: Int = 0;
        Return result;
    }
}

Class System {
    Constructor(){
        Self.out = New Out();
        Self.in = New Cin();
    }
    Destructor(){}
    Var out: Out = Null;
    Var in: Cin = Null;
    len(arr: Array[Int, 10000]){
        Var length: Int;
        Return length;
    }
    $staticFunction1(p1, p2: Int; p3, p4: String; c1, c2: Element) {
        Element::$system.out.print("Element::$StaticFunction1(...)");
    }
}

Class Element {
    Val $system: System = New System();
    Var $st1, $st2: Array[Int, 2];
    Var x1, x2: Int;
    Constructor(){
        Element::$st1 = Array(0,1);
        Element::$st2 = Array("x","y");
    }
    Constructor(x1, x2: Int; st1, st2: Array[Int, 2]){
        Self.x1 = x1; Self.x2 = x2;
        Element::$st1 = st1;
        Element::$st2 = st2;
    }
    Destructor(){}
}
Class SortElement : Element {
    Var arr1, arr2: Array[Int, 10000];
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    printArray1or2(number: Int) {
        If (number == 1) {
            Var x: Int;
            Foreach(x In 0 .. Element::$system.len(Self.arr1)) {
                Element::$system.out.print(x);
                Element::$system.out.print(" ");
            }
        }
        Elseif (number == 2) {
            Foreach(x In 0 .. Element::$system.len(Self.arr2)) {
                Element::$system.out.print(x);
                Element::$system.out.print(" ");
            }
        }
        Else {
            Element::$system.out.print("Invalid array number");
        }
    }
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Element::$recursiveQuickSort(arr, 0, size - 1);
    }
    $recursiveQuickSort(arr: Array[Float, 10000]; low: Int; high: Int){
        If(low == high){
            Return arr;
        }
        Elseif(low < hight){
            Var pi: Int;
            pi = Element::$partition(arr, low, high);

            Element::$quickSort(arr, low, pi - 1);
            Element::$quickSort(arr, pi + 1, high);
        }
    }
    $partition(arr: Array[Int, 10000]; low: Int; high: Int){
        Var i, j: Int = low - 1, 0;
        Var pivot: Int = arr[high];
        Foreach (j In low .. high By 1){
            If (arr[j] <= pivot) {
                i = i + 1;
                Var temp: Int;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            Else {
                Continue;
            }
        }
        Var temp: Int;
        temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        Return i + 1;
    }
}
Class MonthElement : Element {
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    daysInMonth() {
        Var month: Int = Element::$system.in.input();
        If(month == 2) {
            Element::$system.out.print(28);
            Return 28;
        }
        Elseif ((month == 4) || (month == 6) || (month == 9) || (month == 11)) {
            Element::$system.out.print(30);
            Return 30;
        }
        Elseif ((month == 1) || (month == 3) || (month == 5) || (month == 7) || (month == 8) || (month == 10) || (month == 12)) {
            Element::$system.out.print(31);
            Return 31;
        }
        Else {
            Element::$system.out.print("Invalid month number");
            Return -1;
        }
    }
}
            Class Program {
                method() {
                    Var arr: Array[String, 3];
                    arr[0] = New Element();
                    arr[1] = New SortElement();
                    arr[2] = New MonthElement();
                    Return arr;
                }
                main() {
                    Var arr: Array[String, 3] = Self.method();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Out),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(print),Instance,[param(Id(el),ClassType(Id(Element)))],Block([])),MethodDecl(Id(print),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([]))]),ClassDecl(Id(Cin),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(input),Instance,[],Block([ConstDecl(Id(result),IntType,IntLit(0)),Return(Id(result))]))]),ClassDecl(Id(System),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(out)),NewExpr(Id(Out),[])),AssignStmt(FieldAccess(Self(),Id(in)),NewExpr(Id(Cin),[]))])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(out),ClassType(Id(Out)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(in),ClassType(Id(Cin)),NullLiteral())),MethodDecl(Id(len),Instance,[param(Id(arr),ArrayType(10000,IntType))],Block([VarDecl(Id(length),IntType),Return(Id(length))])),MethodDecl(Id($staticFunction1),Static,[param(Id(p1),IntType),param(Id(p2),IntType),param(Id(p3),StringType),param(Id(p4),StringType),param(Id(c1),ClassType(Id(Element))),param(Id(c2),ClassType(Id(Element)))],Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Element::$StaticFunction1(...))])]))]),ClassDecl(Id(Element),[AttributeDecl(Static,ConstDecl(Id($system),ClassType(Id(System)),NewExpr(Id(System),[]))),AttributeDecl(Static,VarDecl(Id($st1),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($st2),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(x1),IntType)),AttributeDecl(Instance,VarDecl(Id(x2),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Element),Id($st1)),[IntLit(0),IntLit(1)]),AssignStmt(FieldAccess(Id(Element),Id($st2)),[StringLit(x),StringLit(y)])])),MethodDecl(Id(Constructor),Instance,[param(Id(x1),IntType),param(Id(x2),IntType),param(Id(st1),ArrayType(2,IntType)),param(Id(st2),ArrayType(2,IntType))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),Id(x1)),AssignStmt(FieldAccess(Self(),Id(x2)),Id(x2)),AssignStmt(FieldAccess(Id(Element),Id($st1)),Id(st1)),AssignStmt(FieldAccess(Id(Element),Id($st2)),Id(st2))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[AttributeDecl(Instance,VarDecl(Id(arr1),ArrayType(10000,IntType))),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(10000,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(printArray1or2),Instance,[param(Id(number),IntType)],Block([If(BinaryOp(==,Id(number),IntLit(1)),Block([VarDecl(Id(x),IntType),For(Id(x),IntLit(0),CallExpr(FieldAccess(Id(Element),Id($system)),Id(len),[FieldAccess(Self(),Id(arr1))]),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[Id(x)]),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit( )])])])]),If(BinaryOp(==,Id(number),IntLit(2)),Block([For(Id(x),IntLit(0),CallExpr(FieldAccess(Id(Element),Id($system)),Id(len),[FieldAccess(Self(),Id(arr2))]),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[Id(x)]),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit( )])])])]),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Invalid array number)])])))])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Id(Element),Id($recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])])),MethodDecl(Id($recursiveQuickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(low),IntType),param(Id(high),IntType)],Block([If(BinaryOp(==,Id(low),Id(high)),Block([Return(Id(arr))]),If(BinaryOp(<,Id(low),Id(hight)),Block([VarDecl(Id(pi),IntType),AssignStmt(Id(pi),CallExpr(Id(Element),Id($partition),[Id(arr),Id(low),Id(high)])),Call(Id(Element),Id($quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),IntLit(1))]),Call(Id(Element),Id($quickSort),[Id(arr),BinaryOp(+,Id(pi),IntLit(1)),Id(high)])])))])),MethodDecl(Id($partition),Static,[param(Id(arr),ArrayType(10000,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([VarDecl(Id(i),IntType,BinaryOp(-,Id(low),IntLit(1))),VarDecl(Id(j),IntType,IntLit(0)),VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(high)])),For(Id(j),Id(low),Id(high),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))]),Block([Continue]))])]),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))]),ArrayCell(Id(arr),[Id(high)])),AssignStmt(ArrayCell(Id(arr),[Id(high)]),Id(temp)),Return(BinaryOp(+,Id(i),IntLit(1)))]))]),ClassDecl(Id(MonthElement),Id(Element),[MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(daysInMonth),Instance,[],Block([VarDecl(Id(month),IntType,CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),If(BinaryOp(==,Id(month),IntLit(2)),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(28)]),Return(IntLit(28))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(month),IntLit(4)),BinaryOp(==,Id(month),IntLit(6))),BinaryOp(==,Id(month),IntLit(9))),BinaryOp(==,Id(month),IntLit(11))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(30)]),Return(IntLit(30))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(month),IntLit(1)),BinaryOp(==,Id(month),IntLit(3))),BinaryOp(==,Id(month),IntLit(5))),BinaryOp(==,Id(month),IntLit(7))),BinaryOp(==,Id(month),IntLit(8))),BinaryOp(==,Id(month),IntLit(10))),BinaryOp(==,Id(month),IntLit(12))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(31)]),Return(IntLit(31))]),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Invalid month number)]),Return(UnaryOp(-,IntLit(1)))]))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([VarDecl(Id(arr),ArrayType(3,StringType)),AssignStmt(ArrayCell(Id(arr),[IntLit(0)]),NewExpr(Id(Element),[])),AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),NewExpr(Id(SortElement),[])),AssignStmt(ArrayCell(Id(arr),[IntLit(2)]),NewExpr(Id(MonthElement),[])),Return(Id(arr))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(arr),ArrayType(3,StringType),CallExpr(Self(),Id(method),[]))]))])])"
        num = 369
        self.assertTrue(TestAST.test(input, expect, num))

    def test70_block_statement_in_block_statement(self):
        input = r"""
            Class Program {
                method() {
                    {{{{}}}}
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Block([Block([Block([Block([])])])])]))])])"
        num = 370
        self.assertTrue(TestAST.test(input, expect, num))

    def test71_foreach_in_foreach(self):
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
        num = 371
        self.assertTrue(TestAST.test(input, expect, num))

    def test72(self):
        input = """
Class Out {
    Constructor(){}
    Destructor(){}
    print(el: Element){}
    print(str: String){}
    print(x: Int){}
}

Class Cin {
    Constructor(){}
    Destructor(){}
    input(){
        Val result: Int = 0;
        Return result;
    }
}

Class System {
    Constructor(){
        Self.out = New Out();
        Self.in = New Cin();
    }
    Destructor(){}
    Var out: Out = Null;
    Var in: Cin = Null;
    len(arr: Array[Int, 10000]){
        Var length: Int;
        Return length;
    }
    $staticFunction1(p1, p2: Int; p3, p4: String; c1, c2: Element) {
        Element::$system.out.print("Element::$StaticFunction1(...)");
    }
}

Class Element {
    Val $system: System = New System();
    Var $st1, $st2: Array[Int, 2];
    Var x1, x2: Int;
    Constructor(){
        Element::$st1 = Array(0,1);
        Element::$st2 = Array("x","y");
    }
    Constructor(x1, x2: Int; st1, st2: Array[Int, 2]){
        Self.x1 = x1; Self.x2 = x2;
        Element::$st1 = st1;
        Element::$st2 = st2;
    }
    Destructor(){}
}
Class SortElement : Element {
    Var arr1, arr2: Array[Int, 10000];
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    printArray1or2(number: Int) {
        If (number == 1) {
            Var x: Int;
            Foreach(x In 0 .. Element::$system.len(Self.arr1)) {
                Element::$system.out.print(x);
                Element::$system.out.print(" ");
            }
        }
        Elseif (number == 2) {
            Foreach(x In 0 .. Element::$system.len(Self.arr2)) {
                Element::$system.out.print(x);
                Element::$system.out.print(" ");
            }
        }
        Else {
            Element::$system.out.print("Invalid array number");
        }
    }
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Element::$recursiveQuickSort(arr, 0, size - 1);
    }
    $recursiveQuickSort(arr: Array[Float, 10000]; low: Int; high: Int){
        If(low == high){
            Return arr;
        }
        Elseif(low < hight){
            Var pi: Int;
            pi = Element::$partition(arr, low, high);

            Element::$quickSort(arr, low, pi - 1);
            Element::$quickSort(arr, pi + 1, high);
        }
    }
    $partition(arr: Array[Int, 10000]; low: Int; high: Int){
        Var i, j: Int = low - 1, 0;
        Var pivot: Int = arr[high];
        Foreach (j In low .. high By 1){
            If (arr[j] <= pivot) {
                i = i + 1;
                Var temp: Int;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            Else {
                Continue;
            }
        }
        Var temp: Int;
        temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        Return i + 1;
    }
}
Class MonthElement : Element {
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    daysInMonth() {
        Var month: Int = Element::$system.in.input();
        If(month == 2) {
            Element::$system.out.print(28);
            Return 28;
        }
        Elseif ((month == 4) || (month == 6) || (month == 9) || (month == 11)) {
            Element::$system.out.print(30);
            Return 30;
        }
        Elseif ((month == 1) || (month == 3) || (month == 5) || (month == 7) || (month == 8) || (month == 10) || (month == 12)) {
            Element::$system.out.print(31);
            Return 31;
        }
        Else {
            Element::$system.out.print("Invalid month number");
            Return -1;
        }
    }
}
            Class Program {
                createDefaultElement() {
                    Var el: Element = New Element();
                    Return el;
                }
                main() {
                    Var el: Element = Self.method();
                    Var sort: SortElement = New SortElement(el);
                    Var month: MonthElement = New MonthElement(el);
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Out),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(print),Instance,[param(Id(el),ClassType(Id(Element)))],Block([])),MethodDecl(Id(print),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([]))]),ClassDecl(Id(Cin),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(input),Instance,[],Block([ConstDecl(Id(result),IntType,IntLit(0)),Return(Id(result))]))]),ClassDecl(Id(System),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(out)),NewExpr(Id(Out),[])),AssignStmt(FieldAccess(Self(),Id(in)),NewExpr(Id(Cin),[]))])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(out),ClassType(Id(Out)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(in),ClassType(Id(Cin)),NullLiteral())),MethodDecl(Id(len),Instance,[param(Id(arr),ArrayType(10000,IntType))],Block([VarDecl(Id(length),IntType),Return(Id(length))])),MethodDecl(Id($staticFunction1),Static,[param(Id(p1),IntType),param(Id(p2),IntType),param(Id(p3),StringType),param(Id(p4),StringType),param(Id(c1),ClassType(Id(Element))),param(Id(c2),ClassType(Id(Element)))],Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Element::$StaticFunction1(...))])]))]),ClassDecl(Id(Element),[AttributeDecl(Static,ConstDecl(Id($system),ClassType(Id(System)),NewExpr(Id(System),[]))),AttributeDecl(Static,VarDecl(Id($st1),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($st2),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(x1),IntType)),AttributeDecl(Instance,VarDecl(Id(x2),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Element),Id($st1)),[IntLit(0),IntLit(1)]),AssignStmt(FieldAccess(Id(Element),Id($st2)),[StringLit(x),StringLit(y)])])),MethodDecl(Id(Constructor),Instance,[param(Id(x1),IntType),param(Id(x2),IntType),param(Id(st1),ArrayType(2,IntType)),param(Id(st2),ArrayType(2,IntType))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),Id(x1)),AssignStmt(FieldAccess(Self(),Id(x2)),Id(x2)),AssignStmt(FieldAccess(Id(Element),Id($st1)),Id(st1)),AssignStmt(FieldAccess(Id(Element),Id($st2)),Id(st2))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[AttributeDecl(Instance,VarDecl(Id(arr1),ArrayType(10000,IntType))),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(10000,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(printArray1or2),Instance,[param(Id(number),IntType)],Block([If(BinaryOp(==,Id(number),IntLit(1)),Block([VarDecl(Id(x),IntType),For(Id(x),IntLit(0),CallExpr(FieldAccess(Id(Element),Id($system)),Id(len),[FieldAccess(Self(),Id(arr1))]),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[Id(x)]),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit( )])])])]),If(BinaryOp(==,Id(number),IntLit(2)),Block([For(Id(x),IntLit(0),CallExpr(FieldAccess(Id(Element),Id($system)),Id(len),[FieldAccess(Self(),Id(arr2))]),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[Id(x)]),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit( )])])])]),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Invalid array number)])])))])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Id(Element),Id($recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])])),MethodDecl(Id($recursiveQuickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(low),IntType),param(Id(high),IntType)],Block([If(BinaryOp(==,Id(low),Id(high)),Block([Return(Id(arr))]),If(BinaryOp(<,Id(low),Id(hight)),Block([VarDecl(Id(pi),IntType),AssignStmt(Id(pi),CallExpr(Id(Element),Id($partition),[Id(arr),Id(low),Id(high)])),Call(Id(Element),Id($quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),IntLit(1))]),Call(Id(Element),Id($quickSort),[Id(arr),BinaryOp(+,Id(pi),IntLit(1)),Id(high)])])))])),MethodDecl(Id($partition),Static,[param(Id(arr),ArrayType(10000,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([VarDecl(Id(i),IntType,BinaryOp(-,Id(low),IntLit(1))),VarDecl(Id(j),IntType,IntLit(0)),VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(high)])),For(Id(j),Id(low),Id(high),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))]),Block([Continue]))])]),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))]),ArrayCell(Id(arr),[Id(high)])),AssignStmt(ArrayCell(Id(arr),[Id(high)]),Id(temp)),Return(BinaryOp(+,Id(i),IntLit(1)))]))]),ClassDecl(Id(MonthElement),Id(Element),[MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(daysInMonth),Instance,[],Block([VarDecl(Id(month),IntType,CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),If(BinaryOp(==,Id(month),IntLit(2)),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(28)]),Return(IntLit(28))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(month),IntLit(4)),BinaryOp(==,Id(month),IntLit(6))),BinaryOp(==,Id(month),IntLit(9))),BinaryOp(==,Id(month),IntLit(11))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(30)]),Return(IntLit(30))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(month),IntLit(1)),BinaryOp(==,Id(month),IntLit(3))),BinaryOp(==,Id(month),IntLit(5))),BinaryOp(==,Id(month),IntLit(7))),BinaryOp(==,Id(month),IntLit(8))),BinaryOp(==,Id(month),IntLit(10))),BinaryOp(==,Id(month),IntLit(12))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[IntLit(31)]),Return(IntLit(31))]),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Invalid month number)]),Return(UnaryOp(-,IntLit(1)))]))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(createDefaultElement),Instance,[],Block([VarDecl(Id(el),ClassType(Id(Element)),NewExpr(Id(Element),[])),Return(Id(el))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(el),ClassType(Id(Element)),CallExpr(Self(),Id(method),[])),VarDecl(Id(sort),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(el)])),VarDecl(Id(month),ClassType(Id(MonthElement)),NewExpr(Id(MonthElement),[Id(el)]))]))])])"
        num = 372
        self.assertTrue(TestAST.test(input, expect, num))

    def test73(self):
        input = """
Class Out {
    Constructor(){}
    Destructor(){}
    print(el: Element){}
    print(str: String){}
    print(x: Int){}
}

Class Cin {
    Constructor(){}
    Destructor(){}
    input(){
        Val result: Int = 0;
        Return result;
    }
}

Class System {
    Constructor(){
        Self.out = New Out();
        Self.in = New Cin();
    }
    Destructor(){}
    Var out: Out = Null;
    Var in: Cin = Null;
    len(arr: Array[Int, 10000]){
        Var length: Int;
        Return length;
    }
    $staticFunction1(p1, p2: Int; p3, p4: String; c1, c2: Element) {
        Element::$system.out.print("Element::$StaticFunction1(...)");
    }
}

Class Element {
    Val $system: System = New System();
    Var $st1, $st2: Array[Int, 2];
    Var x1, x2: Int;
    Constructor(){
        Element::$st1 = Array(0,1);
        Element::$st2 = Array("x","y");
    }
    Constructor(x1, x2: Int; st1, st2: Array[Int, 2]){
        Self.x1 = x1; Self.x2 = x2;
        Element::$st1 = st1;
        Element::$st2 = st2;
    }
    Destructor(){}
}
Class SortElement : Element {
    Var arr1, arr2: Array[Int, 10000];
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    printArray1or2(number: Int) {
    }
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Element::$recursiveQuickSort(arr, 0, size - 1);
    }
    $recursiveQuickSort(arr: Array[Float, 10000]; low: Int; high: Int){
    }
    $partition(arr: Array[Int, 10000]; low: Int; high: Int){
    }
}
Class MonthElement : Element {
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    daysInMonth() {
    }
}
Class Program {
    createDefaultElement() {
        Var el: Element = New Element();
        Return el;
    }
    main() {
        Var el: Element = Self.method();
        Var sort: SortElement = New SortElement(el);
        Var month: MonthElement = New MonthElement(el);
        Var size: Int;
        size = Element::$system.in.input();
        Var arr: Array[Float, 10000];
        Var i: Int = 0;
        Foreach(i In 0 .. (size - 1)) {
            Val str: String = Element::$system.in.input();
            If (Self.isDigit(str)) {

            }
            Else {

            }
        }
        sort::$quickSort(arr, size);
        Foreach(i In 0 .. (size - 1)) {
            Element::$system.out.print(arr[i]);
        }
    }
}
        """
        expect = r"Program([ClassDecl(Id(Out),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(print),Instance,[param(Id(el),ClassType(Id(Element)))],Block([])),MethodDecl(Id(print),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([]))]),ClassDecl(Id(Cin),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(input),Instance,[],Block([ConstDecl(Id(result),IntType,IntLit(0)),Return(Id(result))]))]),ClassDecl(Id(System),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(out)),NewExpr(Id(Out),[])),AssignStmt(FieldAccess(Self(),Id(in)),NewExpr(Id(Cin),[]))])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(out),ClassType(Id(Out)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(in),ClassType(Id(Cin)),NullLiteral())),MethodDecl(Id(len),Instance,[param(Id(arr),ArrayType(10000,IntType))],Block([VarDecl(Id(length),IntType),Return(Id(length))])),MethodDecl(Id($staticFunction1),Static,[param(Id(p1),IntType),param(Id(p2),IntType),param(Id(p3),StringType),param(Id(p4),StringType),param(Id(c1),ClassType(Id(Element))),param(Id(c2),ClassType(Id(Element)))],Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Element::$StaticFunction1(...))])]))]),ClassDecl(Id(Element),[AttributeDecl(Static,ConstDecl(Id($system),ClassType(Id(System)),NewExpr(Id(System),[]))),AttributeDecl(Static,VarDecl(Id($st1),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($st2),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(x1),IntType)),AttributeDecl(Instance,VarDecl(Id(x2),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Element),Id($st1)),[IntLit(0),IntLit(1)]),AssignStmt(FieldAccess(Id(Element),Id($st2)),[StringLit(x),StringLit(y)])])),MethodDecl(Id(Constructor),Instance,[param(Id(x1),IntType),param(Id(x2),IntType),param(Id(st1),ArrayType(2,IntType)),param(Id(st2),ArrayType(2,IntType))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),Id(x1)),AssignStmt(FieldAccess(Self(),Id(x2)),Id(x2)),AssignStmt(FieldAccess(Id(Element),Id($st1)),Id(st1)),AssignStmt(FieldAccess(Id(Element),Id($st2)),Id(st2))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[AttributeDecl(Instance,VarDecl(Id(arr1),ArrayType(10000,IntType))),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(10000,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(printArray1or2),Instance,[param(Id(number),IntType)],Block([])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Id(Element),Id($recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])])),MethodDecl(Id($recursiveQuickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(low),IntType),param(Id(high),IntType)],Block([])),MethodDecl(Id($partition),Static,[param(Id(arr),ArrayType(10000,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([]))]),ClassDecl(Id(MonthElement),Id(Element),[MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(daysInMonth),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(createDefaultElement),Instance,[],Block([VarDecl(Id(el),ClassType(Id(Element)),NewExpr(Id(Element),[])),Return(Id(el))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(el),ClassType(Id(Element)),CallExpr(Self(),Id(method),[])),VarDecl(Id(sort),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(el)])),VarDecl(Id(month),ClassType(Id(MonthElement)),NewExpr(Id(MonthElement),[Id(el)])),VarDecl(Id(size),IntType),AssignStmt(Id(size),CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),VarDecl(Id(arr),ArrayType(10000,FloatType)),VarDecl(Id(i),IntType,IntLit(0)),For(Id(i),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([ConstDecl(Id(str),StringType,CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),If(CallExpr(Self(),Id(isDigit),[Id(str)]),Block([]),Block([]))])]),Call(Id(sort),Id($quickSort),[Id(arr),Id(size)]),For(Id(i),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[ArrayCell(Id(arr),[Id(i)])])])])]))])])"
        num = 373
        self.assertTrue(TestAST.test(input, expect, num))

    def test74(self):
        input = """
Class Out {
    print(el: Element){}
    print(str: String){}
    print(x: Int){}
}

Class Cin {
    input(){
        Val result: Int = 0;
        Return result;
    }
}

Class System {
    Constructor(){
        Self.out = New Out();
        Self.in = New Cin();
    }
    Destructor(){}
    Var out: Out = Null;
    Var in: Cin = Null;
}

Class Element {
    Val $system: System = New System();
    Var $st1, $st2: Array[Int, 2];
    Var x1, x2: Int;
    Constructor(){
        Element::$st1 = Array(0,1);
        Element::$st2 = Array("x","y");
    }
    Constructor(x1, x2: Int; st1, st2: Array[Int, 2]){
        Self.x1 = x1; Self.x2 = x2;
        Element::$st1 = st1;
        Element::$st2 = st2;
    }
    Destructor(){}
}
Class SortElement : Element {
    Var arr1, arr2: Array[Int, 10000];
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    printArray1or2(number: Int) {
    }
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Element::$recursiveQuickSort(arr, 0, size - 1);
    }
}
Class MonthElement : Element {
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    daysInMonth() {
    }
}
Class Program {
    createDefaultElement() {
        Var el: Element = New Element();
        Return el;
    }
    main() {
        Var el: Element = Self.method();
        Var sort: SortElement = New SortElement(el);
        Var month: MonthElement = New MonthElement(el);
        Var size: Int;
        size = Element::$system.in.input();
        Var arr: Array[Float, 10000];
        Var i: Int = 0;
        Foreach(i In 0 .. (size - 1)) {
            Val str: String = Element::$system.in.input();
            If (Self.isDigit(str)) {
                arr[i] = Self.toInt(str);
            }
            Else {
                Element::$system.out.print("Error not digit string");
            }
        }
        sort::$quickSort(arr, size);
        Foreach(i In 0 .. (size - 1)) {
            Element::$system.out.print(arr[i]);
        }
    }
}
        """
        expect = r"Program([ClassDecl(Id(Out),[MethodDecl(Id(print),Instance,[param(Id(el),ClassType(Id(Element)))],Block([])),MethodDecl(Id(print),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([]))]),ClassDecl(Id(Cin),[MethodDecl(Id(input),Instance,[],Block([ConstDecl(Id(result),IntType,IntLit(0)),Return(Id(result))]))]),ClassDecl(Id(System),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(out)),NewExpr(Id(Out),[])),AssignStmt(FieldAccess(Self(),Id(in)),NewExpr(Id(Cin),[]))])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(out),ClassType(Id(Out)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(in),ClassType(Id(Cin)),NullLiteral()))]),ClassDecl(Id(Element),[AttributeDecl(Static,ConstDecl(Id($system),ClassType(Id(System)),NewExpr(Id(System),[]))),AttributeDecl(Static,VarDecl(Id($st1),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($st2),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(x1),IntType)),AttributeDecl(Instance,VarDecl(Id(x2),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Element),Id($st1)),[IntLit(0),IntLit(1)]),AssignStmt(FieldAccess(Id(Element),Id($st2)),[StringLit(x),StringLit(y)])])),MethodDecl(Id(Constructor),Instance,[param(Id(x1),IntType),param(Id(x2),IntType),param(Id(st1),ArrayType(2,IntType)),param(Id(st2),ArrayType(2,IntType))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),Id(x1)),AssignStmt(FieldAccess(Self(),Id(x2)),Id(x2)),AssignStmt(FieldAccess(Id(Element),Id($st1)),Id(st1)),AssignStmt(FieldAccess(Id(Element),Id($st2)),Id(st2))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[AttributeDecl(Instance,VarDecl(Id(arr1),ArrayType(10000,IntType))),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(10000,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(printArray1or2),Instance,[param(Id(number),IntType)],Block([])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Id(Element),Id($recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])]))]),ClassDecl(Id(MonthElement),Id(Element),[MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(daysInMonth),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(createDefaultElement),Instance,[],Block([VarDecl(Id(el),ClassType(Id(Element)),NewExpr(Id(Element),[])),Return(Id(el))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(el),ClassType(Id(Element)),CallExpr(Self(),Id(method),[])),VarDecl(Id(sort),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(el)])),VarDecl(Id(month),ClassType(Id(MonthElement)),NewExpr(Id(MonthElement),[Id(el)])),VarDecl(Id(size),IntType),AssignStmt(Id(size),CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),VarDecl(Id(arr),ArrayType(10000,FloatType)),VarDecl(Id(i),IntType,IntLit(0)),For(Id(i),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([ConstDecl(Id(str),StringType,CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),If(CallExpr(Self(),Id(isDigit),[Id(str)]),Block([AssignStmt(ArrayCell(Id(arr),[Id(i)]),CallExpr(Self(),Id(toInt),[Id(str)]))]),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Error not digit string)])]))])]),Call(Id(sort),Id($quickSort),[Id(arr),Id(size)]),For(Id(i),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[ArrayCell(Id(arr),[Id(i)])])])])]))])])"
        num = 374
        self.assertTrue(TestAST.test(input, expect, num))

    def test75(self):
        input = """
Class Out {
    print(el: Element){}
    print(str: String){}
    print(x: Int){}
}

Class Cin {
    input(){
        Val result: Int = 0;
        Return result;
    }
}

Class System {
    Constructor(){
        Self.out = New Out();
        Self.in = New Cin();
    }
    Destructor(){}
    Var out: Out = Null;
    Var in: Cin = Null;
}

Class Element {
    Val $system: System = New System();
    Var $st1, $st2: Array[Int, 2];
    Var x1, x2: Int;
    Constructor(){
        Element::$st1 = Array(0,1);
        Element::$st2 = Array("x","y");
    }
    Constructor(x1, x2: Int; st1, st2: Array[Int, 2]){
        Self.x1 = x1; Self.x2 = x2;
        Element::$st1 = st1;
        Element::$st2 = st2;
    }
    Destructor(){}
}
Class SortElement : Element {
    Var arr1, arr2: Array[Int, 10000];
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    printArray1or2(number: Int) {
    }
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Element::$recursiveQuickSort(arr, 0, size - 1);
    }
}
Class MonthElement : Element {
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    daysInMonth() {
    }
}
Class Program {
    createDefaultElement() {
        Var el: Element = New Element();
        Return el;
    }
    main() {
        Var el: Element = Self.method();
        Var sort: SortElement = New SortElement(el);
        Var month: MonthElement = New MonthElement(el);
        Var number: Int;
        Val str: String = Element::$system.in.input();
        If (Self.isDigit(str)) {
            number = Self.toInt(str);
        }
        Else {
            Element::$system.out.print("Error not digit string");
        }
        Var day: Int = month.daysInMonth(number);
        Element::$system.out.print(day);
    }
}
        """
        expect = r"Program([ClassDecl(Id(Out),[MethodDecl(Id(print),Instance,[param(Id(el),ClassType(Id(Element)))],Block([])),MethodDecl(Id(print),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([]))]),ClassDecl(Id(Cin),[MethodDecl(Id(input),Instance,[],Block([ConstDecl(Id(result),IntType,IntLit(0)),Return(Id(result))]))]),ClassDecl(Id(System),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(out)),NewExpr(Id(Out),[])),AssignStmt(FieldAccess(Self(),Id(in)),NewExpr(Id(Cin),[]))])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(out),ClassType(Id(Out)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(in),ClassType(Id(Cin)),NullLiteral()))]),ClassDecl(Id(Element),[AttributeDecl(Static,ConstDecl(Id($system),ClassType(Id(System)),NewExpr(Id(System),[]))),AttributeDecl(Static,VarDecl(Id($st1),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($st2),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(x1),IntType)),AttributeDecl(Instance,VarDecl(Id(x2),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Element),Id($st1)),[IntLit(0),IntLit(1)]),AssignStmt(FieldAccess(Id(Element),Id($st2)),[StringLit(x),StringLit(y)])])),MethodDecl(Id(Constructor),Instance,[param(Id(x1),IntType),param(Id(x2),IntType),param(Id(st1),ArrayType(2,IntType)),param(Id(st2),ArrayType(2,IntType))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),Id(x1)),AssignStmt(FieldAccess(Self(),Id(x2)),Id(x2)),AssignStmt(FieldAccess(Id(Element),Id($st1)),Id(st1)),AssignStmt(FieldAccess(Id(Element),Id($st2)),Id(st2))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[AttributeDecl(Instance,VarDecl(Id(arr1),ArrayType(10000,IntType))),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(10000,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(printArray1or2),Instance,[param(Id(number),IntType)],Block([])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Id(Element),Id($recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])]))]),ClassDecl(Id(MonthElement),Id(Element),[MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(daysInMonth),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(createDefaultElement),Instance,[],Block([VarDecl(Id(el),ClassType(Id(Element)),NewExpr(Id(Element),[])),Return(Id(el))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(el),ClassType(Id(Element)),CallExpr(Self(),Id(method),[])),VarDecl(Id(sort),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(el)])),VarDecl(Id(month),ClassType(Id(MonthElement)),NewExpr(Id(MonthElement),[Id(el)])),VarDecl(Id(number),IntType),ConstDecl(Id(str),StringType,CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),If(CallExpr(Self(),Id(isDigit),[Id(str)]),Block([AssignStmt(Id(number),CallExpr(Self(),Id(toInt),[Id(str)]))]),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[StringLit(Error not digit string)])])),VarDecl(Id(day),IntType,CallExpr(Id(month),Id(daysInMonth),[Id(number)])),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[Id(day)])]))])])"
        num = 375
        self.assertTrue(TestAST.test(input, expect, num))

    def test76(self):
        input = """
Class Out {
    print(el: Element){}
    print(str: String){}
    print(x: Int){}
}

Class Cin {
    input(){
        Val result: Int = 0;
        Return result;
    }
}

Class System {
    Constructor(){
        Self.out = New Out();
        Self.in = New Cin();
    }
    Destructor(){}
    Var out: Out = Null;
    Var in: Cin = Null;
}

Class Element {
    Val $system: System = New System();
    Var $st1, $st2: Array[Int, 2];
    Var x1, x2: Int;
    Constructor(){
        Element::$st1 = Array(0,1);
        Element::$st2 = Array("x","y");
    }
    Constructor(x1, x2: Int; st1, st2: Array[Int, 2]){
        Self.x1 = x1; Self.x2 = x2;
        Element::$st1 = st1;
        Element::$st2 = st2;
    }
    Destructor(){}
}
Class SortElement : Element {
    Var arr1, arr2: Array[Int, 10000];
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    printArray1or2(number: Int) {
    }
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Element::$recursiveQuickSort(arr, 0, size - 1);
    }
}
Class MonthElement : Element {
    Constructor(el: Element) {
        Self.x1 = el.x1; Self.x2 = el.x2;
    }
    daysInMonth() {
    }
}
Class Program {
    createDefaultElement() {
        Var el: Element = New Element();
        Return el;
    }
    main() {
        {
            Var x1, x2, x3: Int = 1,2,3;
            Var c1, c2, c3: Element = New Element(), New SortElement(c2), New MonthElement(c3);
        }

        Var c4: Element = New SortElement(c1);
        Var c5: SortElement = New SortElement(c4);

        {
            If ((c4.x1 == 0) && (c4::$st1[0] == -5)) {
                Element::$system.out.print(Self.toInt("123" + "12"));
            }
            Elseif ((c4.x1 != 0) || (c4::$st1[0] == 5)) {
                Var arr: Array[String, 1] = Array("Hi Mom");
                Element::$system.out.print(arr[0]);
            }
            Elseif ((c5.x1 != 0) || (c5::$st1[0] == 5)) {
                Var i: Int = 0;
                Var arr: Array[Int, 5];
                Foreach (i In 0 .. 9 By 2) {
                    arr[i / 2] = i;
                    Element::$system.out.print(arr[i]);
                }
            }
            Else {
                Return "Case 4";
            }
        }

        Return -1;
    }
}
        """
        expect = r"Program([ClassDecl(Id(Out),[MethodDecl(Id(print),Instance,[param(Id(el),ClassType(Id(Element)))],Block([])),MethodDecl(Id(print),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([]))]),ClassDecl(Id(Cin),[MethodDecl(Id(input),Instance,[],Block([ConstDecl(Id(result),IntType,IntLit(0)),Return(Id(result))]))]),ClassDecl(Id(System),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(out)),NewExpr(Id(Out),[])),AssignStmt(FieldAccess(Self(),Id(in)),NewExpr(Id(Cin),[]))])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(out),ClassType(Id(Out)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(in),ClassType(Id(Cin)),NullLiteral()))]),ClassDecl(Id(Element),[AttributeDecl(Static,ConstDecl(Id($system),ClassType(Id(System)),NewExpr(Id(System),[]))),AttributeDecl(Static,VarDecl(Id($st1),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($st2),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(x1),IntType)),AttributeDecl(Instance,VarDecl(Id(x2),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Element),Id($st1)),[IntLit(0),IntLit(1)]),AssignStmt(FieldAccess(Id(Element),Id($st2)),[StringLit(x),StringLit(y)])])),MethodDecl(Id(Constructor),Instance,[param(Id(x1),IntType),param(Id(x2),IntType),param(Id(st1),ArrayType(2,IntType)),param(Id(st2),ArrayType(2,IntType))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),Id(x1)),AssignStmt(FieldAccess(Self(),Id(x2)),Id(x2)),AssignStmt(FieldAccess(Id(Element),Id($st1)),Id(st1)),AssignStmt(FieldAccess(Id(Element),Id($st2)),Id(st2))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[AttributeDecl(Instance,VarDecl(Id(arr1),ArrayType(10000,IntType))),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(10000,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(printArray1or2),Instance,[param(Id(number),IntType)],Block([])),MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Id(Element),Id($recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])]))]),ClassDecl(Id(MonthElement),Id(Element),[MethodDecl(Id(Constructor),Instance,[param(Id(el),ClassType(Id(Element)))],Block([AssignStmt(FieldAccess(Self(),Id(x1)),FieldAccess(Id(el),Id(x1))),AssignStmt(FieldAccess(Self(),Id(x2)),FieldAccess(Id(el),Id(x2)))])),MethodDecl(Id(daysInMonth),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(createDefaultElement),Instance,[],Block([VarDecl(Id(el),ClassType(Id(Element)),NewExpr(Id(Element),[])),Return(Id(el))])),MethodDecl(Id(main),Static,[],Block([Block([VarDecl(Id(x1),IntType,IntLit(1)),VarDecl(Id(x2),IntType,IntLit(2)),VarDecl(Id(x3),IntType,IntLit(3)),VarDecl(Id(c1),ClassType(Id(Element)),NewExpr(Id(Element),[])),VarDecl(Id(c2),ClassType(Id(Element)),NewExpr(Id(SortElement),[Id(c2)])),VarDecl(Id(c3),ClassType(Id(Element)),NewExpr(Id(MonthElement),[Id(c3)]))]),VarDecl(Id(c4),ClassType(Id(Element)),NewExpr(Id(SortElement),[Id(c1)])),VarDecl(Id(c5),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(c4)])),Block([If(BinaryOp(&&,BinaryOp(==,FieldAccess(Id(c4),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c4),Id($st1)),[IntLit(0)]),UnaryOp(-,IntLit(5)))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[CallExpr(Self(),Id(toInt),[BinaryOp(+,StringLit(123),StringLit(12))])])]),If(BinaryOp(||,BinaryOp(!=,FieldAccess(Id(c4),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c4),Id($st1)),[IntLit(0)]),IntLit(5))),Block([VarDecl(Id(arr),ArrayType(1,StringType),[StringLit(Hi Mom)]),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[ArrayCell(Id(arr),[IntLit(0)])])]),If(BinaryOp(||,BinaryOp(!=,FieldAccess(Id(c5),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c5),Id($st1)),[IntLit(0)]),IntLit(5))),Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(arr),ArrayType(5,IntType)),For(Id(i),IntLit(0),IntLit(9),IntLit(2),Block([AssignStmt(ArrayCell(Id(arr),[BinaryOp(/,Id(i),IntLit(2))]),Id(i)),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[ArrayCell(Id(arr),[Id(i)])])])])]),Block([Return(StringLit(Case 4))]))))]),Return(UnaryOp(-,IntLit(1)))]))])])"
        num = 376
        self.assertTrue(TestAST.test(input, expect, num))

    def test77(self):
        input = """
Class Out {
    print(el: Element){}
    print(str: String){}
    print(x: Int){}
}

Class Cin {
    input(){
        Val result: Int = 0;
        Return result;
    }
}

Class System {
    Constructor(){
        Self.out = New Out();
        Self.in = New Cin();
    }
    Destructor(){}
    Var out: Out = Null;
    Var in: Cin = Null;
}

Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Self.recursiveQuickSort(arr, 0, size - 1);
    }
    recursiveQuickSort(arr: Array[Float, 10000]; low: Int; high: Int){
        If(low == high){
            Return arr;
        }
        Elseif(low < hight){
            Var pi: Int;
            pi = Element::$partition(arr, low, high);

            Element::$quickSort(arr, low, pi - 1);
            Element::$quickSort(arr, pi + 1, high);
        }
    }
    partition(arr: Array[Int, 10000]; low: Int; high: Int){
        Var i, j: Int = low - 1, 0;
        Var pivot: Int = arr[high];
        Foreach (j In low .. high By 1){
            If (arr[j] <= pivot) {
                i = i + 1;
                Var temp: Int;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            Else {
                Continue;
            }
        }
        Var temp: Int;
        temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        Return i + 1;
    }
}
Class Program {
    createDefaultElement() {
        Var el: Element = New Element();
        Return el;
    }
    main() {
        {
            Var x1, x2, x3: Int = 1,2,3;
            Var c1, c2, c3: Element = New Element(), New SortElement(c2), New MonthElement(c3);
        }

        Var c4: Element = New SortElement(c1);
        Var c5: SortElement = New SortElement(c4);

        {
            If ((c4.x1 == 0) && (c4::$st1[0] == -5)) {
                Element::$system.out.print(Self.toInt("123" + "12"));
            }
            Elseif ((c4.x1 != 0) || (c4::$st1[0] == 5)) {
                Var arr: Array[String, 1] = Array("Hi Mom");
                Element::$system.out.print(arr[0]);
            }
            Elseif ((c5.x1 != 0) || (c5::$st1[0] == 5)) {
                Var i: Int = 0;
                Var arr: Array[Int, 10000];
                Foreach (i In 9 .. 0 By (-2)) {
                    arr[i / 2] = i;
                }
                c5.recursiveQuickSort(arr, 0, 5);
                Foreach (i In 0 .. 4 By (1)) {
                    Element::$system.out.print(arr[i]);
                }
            }
            Else {
                Return "Case 4";
            }
        }

        Return -1;
    }
}
        """
        expect = r"Program([ClassDecl(Id(Out),[MethodDecl(Id(print),Instance,[param(Id(el),ClassType(Id(Element)))],Block([])),MethodDecl(Id(print),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([]))]),ClassDecl(Id(Cin),[MethodDecl(Id(input),Instance,[],Block([ConstDecl(Id(result),IntType,IntLit(0)),Return(Id(result))]))]),ClassDecl(Id(System),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(out)),NewExpr(Id(Out),[])),AssignStmt(FieldAccess(Self(),Id(in)),NewExpr(Id(Cin),[]))])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(out),ClassType(Id(Out)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(in),ClassType(Id(Cin)),NullLiteral()))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Self(),Id(recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])])),MethodDecl(Id(recursiveQuickSort),Instance,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(low),IntType),param(Id(high),IntType)],Block([If(BinaryOp(==,Id(low),Id(high)),Block([Return(Id(arr))]),If(BinaryOp(<,Id(low),Id(hight)),Block([VarDecl(Id(pi),IntType),AssignStmt(Id(pi),CallExpr(Id(Element),Id($partition),[Id(arr),Id(low),Id(high)])),Call(Id(Element),Id($quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),IntLit(1))]),Call(Id(Element),Id($quickSort),[Id(arr),BinaryOp(+,Id(pi),IntLit(1)),Id(high)])])))])),MethodDecl(Id(partition),Instance,[param(Id(arr),ArrayType(10000,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([VarDecl(Id(i),IntType,BinaryOp(-,Id(low),IntLit(1))),VarDecl(Id(j),IntType,IntLit(0)),VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(high)])),For(Id(j),Id(low),Id(high),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))]),Block([Continue]))])]),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))]),ArrayCell(Id(arr),[Id(high)])),AssignStmt(ArrayCell(Id(arr),[Id(high)]),Id(temp)),Return(BinaryOp(+,Id(i),IntLit(1)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(createDefaultElement),Instance,[],Block([VarDecl(Id(el),ClassType(Id(Element)),NewExpr(Id(Element),[])),Return(Id(el))])),MethodDecl(Id(main),Static,[],Block([Block([VarDecl(Id(x1),IntType,IntLit(1)),VarDecl(Id(x2),IntType,IntLit(2)),VarDecl(Id(x3),IntType,IntLit(3)),VarDecl(Id(c1),ClassType(Id(Element)),NewExpr(Id(Element),[])),VarDecl(Id(c2),ClassType(Id(Element)),NewExpr(Id(SortElement),[Id(c2)])),VarDecl(Id(c3),ClassType(Id(Element)),NewExpr(Id(MonthElement),[Id(c3)]))]),VarDecl(Id(c4),ClassType(Id(Element)),NewExpr(Id(SortElement),[Id(c1)])),VarDecl(Id(c5),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(c4)])),Block([If(BinaryOp(&&,BinaryOp(==,FieldAccess(Id(c4),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c4),Id($st1)),[IntLit(0)]),UnaryOp(-,IntLit(5)))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[CallExpr(Self(),Id(toInt),[BinaryOp(+,StringLit(123),StringLit(12))])])]),If(BinaryOp(||,BinaryOp(!=,FieldAccess(Id(c4),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c4),Id($st1)),[IntLit(0)]),IntLit(5))),Block([VarDecl(Id(arr),ArrayType(1,StringType),[StringLit(Hi Mom)]),Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[ArrayCell(Id(arr),[IntLit(0)])])]),If(BinaryOp(||,BinaryOp(!=,FieldAccess(Id(c5),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c5),Id($st1)),[IntLit(0)]),IntLit(5))),Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(arr),ArrayType(10000,IntType)),For(Id(i),IntLit(9),IntLit(0),UnaryOp(-,IntLit(2)),Block([AssignStmt(ArrayCell(Id(arr),[BinaryOp(/,Id(i),IntLit(2))]),Id(i))])]),Call(Id(c5),Id(recursiveQuickSort),[Id(arr),IntLit(0),IntLit(5)]),For(Id(i),IntLit(0),IntLit(4),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[ArrayCell(Id(arr),[Id(i)])])])])]),Block([Return(StringLit(Case 4))]))))]),Return(UnaryOp(-,IntLit(1)))]))])])"
        num = 377
        self.assertTrue(TestAST.test(input, expect, num))

    def test78(self):
        input = """
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Self.recursiveQuickSort(arr, 0, size - 1);
    }
    recursiveQuickSort(arr: Array[Float, 10000]; low: Int; high: Int){
        If(low == high){
            Return arr;
        }
        Elseif(low < hight){
            Var pi: Int;
            pi = Element::$partition(arr, low, high);

            Element::$quickSort(arr, low, pi - 1);
            Element::$quickSort(arr, pi + 1, high);
        }
    }
    partition(arr: Array[Int, 10000]; low: Int; high: Int){
        Var i, j: Int = low - 1, 0;
        Var pivot: Int = arr[high];
        Foreach (j In low .. high By 1){
            If (arr[j] <= pivot) {
                i = i + 1;
                Var temp: Int;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            Else {
                Continue;
            }
        }
        Var temp: Int;
        temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        Return i + 1;
    }
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    $isNum(str: String; length: Int) {
        Var i, j: Int = 0, 0;
        Foreach(i In 0 .. length By 1) {
            If(UltilityElement::$isDigit(System::$toInt(str[i]))){
                Continue;
            }
            Else{
                Return False;
            }
        }
        Return True;
    }
    $isDigit(ch: Int) {
        Return (ch >= 48) && (ch <= 57);
    }
}
Class Program {
    main() {
        {
            Var x1, x2, x3: Int = 1,2,3;
            Var c1, c2, c3: Element = New Element(), New SortElement(c2), New MonthElement(c3);
        }

        Var c4: Element = Self.createDefaultElement();
        Var c5: SortElement = New SortElement(c4);

        {
            If ((c4.x1 == 0) && (c4::$st1[0] == -5)) {
                Element::$system.out.print(Self.toInt("123" + "12"));
            }
            Elseif ((c5.x1 != 0) || (c5::$st1[0] == 5)) {
                Var i: Int = 0;
                Var arr: Array[Int, 10000];
                Foreach (i In 9 .. 0 By (-2)) {
                    arr[i / 2] = i;
                }
                c5.recursiveQuickSort(arr, 0, 5);
                Foreach (i In 0 .. 4 By (1)) {
                    Element::$system.out.print(arr[i]);
                }
            }
        }

        Return -1;
    }
}
        """
        expect = r"Program([ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Self(),Id(recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])])),MethodDecl(Id(recursiveQuickSort),Instance,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(low),IntType),param(Id(high),IntType)],Block([If(BinaryOp(==,Id(low),Id(high)),Block([Return(Id(arr))]),If(BinaryOp(<,Id(low),Id(hight)),Block([VarDecl(Id(pi),IntType),AssignStmt(Id(pi),CallExpr(Id(Element),Id($partition),[Id(arr),Id(low),Id(high)])),Call(Id(Element),Id($quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),IntLit(1))]),Call(Id(Element),Id($quickSort),[Id(arr),BinaryOp(+,Id(pi),IntLit(1)),Id(high)])])))])),MethodDecl(Id(partition),Instance,[param(Id(arr),ArrayType(10000,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([VarDecl(Id(i),IntType,BinaryOp(-,Id(low),IntLit(1))),VarDecl(Id(j),IntType,IntLit(0)),VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(high)])),For(Id(j),Id(low),Id(high),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))]),Block([Continue]))])]),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))]),ArrayCell(Id(arr),[Id(high)])),AssignStmt(ArrayCell(Id(arr),[Id(high)]),Id(temp)),Return(BinaryOp(+,Id(i),IntLit(1)))]))]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id($isNum),Static,[param(Id(str),StringType),param(Id(length),IntType)],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(j),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(length),IntLit(1),Block([If(CallExpr(Id(UltilityElement),Id($isDigit),[CallExpr(Id(System),Id($toInt),[ArrayCell(Id(str),[Id(i)])])]),Block([Continue]),Block([Return(BooleanLit(False))]))])]),Return(BooleanLit(True))])),MethodDecl(Id($isDigit),Static,[param(Id(ch),IntType)],Block([Return(BinaryOp(&&,BinaryOp(>=,Id(ch),IntLit(48)),BinaryOp(<=,Id(ch),IntLit(57))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([VarDecl(Id(x1),IntType,IntLit(1)),VarDecl(Id(x2),IntType,IntLit(2)),VarDecl(Id(x3),IntType,IntLit(3)),VarDecl(Id(c1),ClassType(Id(Element)),NewExpr(Id(Element),[])),VarDecl(Id(c2),ClassType(Id(Element)),NewExpr(Id(SortElement),[Id(c2)])),VarDecl(Id(c3),ClassType(Id(Element)),NewExpr(Id(MonthElement),[Id(c3)]))]),VarDecl(Id(c4),ClassType(Id(Element)),CallExpr(Self(),Id(createDefaultElement),[])),VarDecl(Id(c5),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(c4)])),Block([If(BinaryOp(&&,BinaryOp(==,FieldAccess(Id(c4),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c4),Id($st1)),[IntLit(0)]),UnaryOp(-,IntLit(5)))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[CallExpr(Self(),Id(toInt),[BinaryOp(+,StringLit(123),StringLit(12))])])]),If(BinaryOp(||,BinaryOp(!=,FieldAccess(Id(c5),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c5),Id($st1)),[IntLit(0)]),IntLit(5))),Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(arr),ArrayType(10000,IntType)),For(Id(i),IntLit(9),IntLit(0),UnaryOp(-,IntLit(2)),Block([AssignStmt(ArrayCell(Id(arr),[BinaryOp(/,Id(i),IntLit(2))]),Id(i))])]),Call(Id(c5),Id(recursiveQuickSort),[Id(arr),IntLit(0),IntLit(5)]),For(Id(i),IntLit(0),IntLit(4),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[ArrayCell(Id(arr),[Id(i)])])])])])))]),Return(UnaryOp(-,IntLit(1)))]))])])"
        num = 378
        self.assertTrue(TestAST.test(input, expect, num))

    def test79(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
    $quickSort(arr: Array[Float, 10000]; size: Int){
        Self.recursiveQuickSort(arr, 0, size - 1);
    }
    recursiveQuickSort(arr: Array[Float, 10000]; low: Int; high: Int){
        If(low == high){
            Return arr;
        }
        Elseif(low < hight){
            Var pi: Int;
            pi = Element::$partition(arr, low, high);

            Element::$quickSort(arr, low, pi - 1);
            Element::$quickSort(arr, pi + 1, high);
        }
    }
    partition(arr: Array[Int, 10000]; low: Int; high: Int){
        Var i, j: Int = low - 1, 0;
        Var pivot: Int = arr[high];
        Foreach (j In low .. high By 1){
            If (arr[j] <= pivot) {
                i = i + 1;
                Var temp: Int;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            Else {
                Continue;
            }
        }
        Var temp: Int;
        temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        Return i + 1;
    }
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    $isNum(str: String; length: Int) {
        Var i, j: Int = 0, 0;
        Foreach(i In 0 .. length By 1) {
            If(UltilityElement::$isDigit(System::$toInt(str[i]))){
                Continue;
            }
            Else{
                Return False;
            }
        }
        Return True;
    }
    $isDigit(ch: Int) {
        Return (ch >= 48) && (ch <= 57);
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Var c1: Element = New Element();
        {
            Var c1, c2, c3: Element = New Element(), New SortElement(c2), New MonthElement(c3);
        }
        Var c4: Element;
        Var c5: SortElement = New SortElement(c4);
        {
            If ((c4.x1 == 0) && (c4::$st1[0] == 0)) {
                Element::$system.out.print(Self.toInt("123" + "12"));
            }
            Elseif ((c5.x1 == 0) || (c5::$st1[0] == 0)) {
                Var i, size: Int = 0, 0;
                Var str1, str2: String = "", "Temp String";
                str1 = System::$input();
                If (UltilityElement::$isNumber(str1)) {
                    size = Self.toInt(str1);
                }
                Var arr: Array[Int, 10000];
                Foreach (i In 0 .. Size By 1) {
                    arr[i] = Self.toInt(System::$input());
                }
                c5.recursiveQuickSort(arr, 0, Size);
                Foreach (i In 0 .. 4 By (1)) {
                    System::$output(Self.toStr(arr[i]));
                }
            }
        }
        Return -1;
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[MethodDecl(Id($quickSort),Static,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(size),IntType)],Block([Call(Self(),Id(recursiveQuickSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))])])),MethodDecl(Id(recursiveQuickSort),Instance,[param(Id(arr),ArrayType(10000,FloatType)),param(Id(low),IntType),param(Id(high),IntType)],Block([If(BinaryOp(==,Id(low),Id(high)),Block([Return(Id(arr))]),If(BinaryOp(<,Id(low),Id(hight)),Block([VarDecl(Id(pi),IntType),AssignStmt(Id(pi),CallExpr(Id(Element),Id($partition),[Id(arr),Id(low),Id(high)])),Call(Id(Element),Id($quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),IntLit(1))]),Call(Id(Element),Id($quickSort),[Id(arr),BinaryOp(+,Id(pi),IntLit(1)),Id(high)])])))])),MethodDecl(Id(partition),Instance,[param(Id(arr),ArrayType(10000,IntType)),param(Id(low),IntType),param(Id(high),IntType)],Block([VarDecl(Id(i),IntType,BinaryOp(-,Id(low),IntLit(1))),VarDecl(Id(j),IntType,IntLit(0)),VarDecl(Id(pivot),IntType,ArrayCell(Id(arr),[Id(high)])),For(Id(j),Id(low),Id(high),IntLit(1),Block([If(BinaryOp(<=,ArrayCell(Id(arr),[Id(j)]),Id(pivot)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[Id(i)])),AssignStmt(ArrayCell(Id(arr),[Id(i)]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(ArrayCell(Id(arr),[Id(j)]),Id(temp))]),Block([Continue]))])]),VarDecl(Id(temp),IntType),AssignStmt(Id(temp),ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(i),IntLit(1))]),ArrayCell(Id(arr),[Id(high)])),AssignStmt(ArrayCell(Id(arr),[Id(high)]),Id(temp)),Return(BinaryOp(+,Id(i),IntLit(1)))]))]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id($isNum),Static,[param(Id(str),StringType),param(Id(length),IntType)],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(j),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(length),IntLit(1),Block([If(CallExpr(Id(UltilityElement),Id($isDigit),[CallExpr(Id(System),Id($toInt),[ArrayCell(Id(str),[Id(i)])])]),Block([Continue]),Block([Return(BooleanLit(False))]))])]),Return(BooleanLit(True))])),MethodDecl(Id($isDigit),Static,[param(Id(ch),IntType)],Block([Return(BinaryOp(&&,BinaryOp(>=,Id(ch),IntLit(48)),BinaryOp(<=,Id(ch),IntLit(57))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(c1),ClassType(Id(Element)),NewExpr(Id(Element),[])),Block([VarDecl(Id(c1),ClassType(Id(Element)),NewExpr(Id(Element),[])),VarDecl(Id(c2),ClassType(Id(Element)),NewExpr(Id(SortElement),[Id(c2)])),VarDecl(Id(c3),ClassType(Id(Element)),NewExpr(Id(MonthElement),[Id(c3)]))]),VarDecl(Id(c4),ClassType(Id(Element)),NullLiteral()),VarDecl(Id(c5),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(c4)])),Block([If(BinaryOp(&&,BinaryOp(==,FieldAccess(Id(c4),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c4),Id($st1)),[IntLit(0)]),IntLit(0))),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[CallExpr(Self(),Id(toInt),[BinaryOp(+,StringLit(123),StringLit(12))])])]),If(BinaryOp(||,BinaryOp(==,FieldAccess(Id(c5),Id(x1)),IntLit(0)),BinaryOp(==,ArrayCell(FieldAccess(Id(c5),Id($st1)),[IntLit(0)]),IntLit(0))),Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(size),IntType,IntLit(0)),VarDecl(Id(str1),StringType,StringLit()),VarDecl(Id(str2),StringType,StringLit(Temp String)),AssignStmt(Id(str1),CallExpr(Id(System),Id($input),[])),If(CallExpr(Id(UltilityElement),Id($isNumber),[Id(str1)]),Block([AssignStmt(Id(size),CallExpr(Self(),Id(toInt),[Id(str1)]))])),VarDecl(Id(arr),ArrayType(10000,IntType)),For(Id(i),IntLit(0),Id(Size),IntLit(1),Block([AssignStmt(ArrayCell(Id(arr),[Id(i)]),CallExpr(Self(),Id(toInt),[CallExpr(Id(System),Id($input),[])]))])]),Call(Id(c5),Id(recursiveQuickSort),[Id(arr),IntLit(0),Id(Size)]),For(Id(i),IntLit(0),IntLit(4),IntLit(1),Block([Call(Id(System),Id($output),[CallExpr(Self(),Id(toStr),[ArrayCell(Id(arr),[Id(i)])])])])])])))]),Return(UnaryOp(-,IntLit(1)))]))])])"
        num = 379
        self.assertTrue(TestAST.test(input, expect, num))

    def test80(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    $isNum(str: String; length: Int) {
        Var i, j: Int = 0, 0;
        Foreach(i In 0 .. length By 1) {
            If(UltilityElement::$isDigit(System::$toInt(str[i]))){
                Continue;
            }
            Else{
                Return False;
            }
        }
        Return True;
    }
    $isDigit(ch: Int) {
        Return (ch >= 48) && (ch <= 57);
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Var floor, roof: Int = Self.toInt(System::$input()), Self.toInt(System::$input());
        Var chances: Int = (roof - floor) / 5;
        Var answer, guess: Int = System::$random(floor, roof), 0;
        Var str1: String = "Range from " + Self.toStr(floor) + "to " + Self.toStr(roof) + " " + Self.toStr(chances) + " chances to guess: \\n";
        System::$output("Range from " + Self.toStr(floor) + "to " + Self.toStr(roof) + " " + Self.toStr(chances) + " chances to guess: \\n");
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id($isNum),Static,[param(Id(str),StringType),param(Id(length),IntType)],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(j),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(length),IntLit(1),Block([If(CallExpr(Id(UltilityElement),Id($isDigit),[CallExpr(Id(System),Id($toInt),[ArrayCell(Id(str),[Id(i)])])]),Block([Continue]),Block([Return(BooleanLit(False))]))])]),Return(BooleanLit(True))])),MethodDecl(Id($isDigit),Static,[param(Id(ch),IntType)],Block([Return(BinaryOp(&&,BinaryOp(>=,Id(ch),IntLit(48)),BinaryOp(<=,Id(ch),IntLit(57))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(floor),IntType,CallExpr(Self(),Id(toInt),[CallExpr(Id(System),Id($input),[])])),VarDecl(Id(roof),IntType,CallExpr(Self(),Id(toInt),[CallExpr(Id(System),Id($input),[])])),VarDecl(Id(chances),IntType,BinaryOp(/,BinaryOp(-,Id(roof),Id(floor)),IntLit(5))),VarDecl(Id(answer),IntType,CallExpr(Id(System),Id($random),[Id(floor),Id(roof)])),VarDecl(Id(guess),IntType,IntLit(0)),VarDecl(Id(str1),StringType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(Range from ),CallExpr(Self(),Id(toStr),[Id(floor)])),StringLit(to )),CallExpr(Self(),Id(toStr),[Id(roof)])),StringLit( )),CallExpr(Self(),Id(toStr),[Id(chances)])),StringLit( chances to guess: \n))),Call(Id(System),Id($output),[BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(Range from ),CallExpr(Self(),Id(toStr),[Id(floor)])),StringLit(to )),CallExpr(Self(),Id(toStr),[Id(roof)])),StringLit( )),CallExpr(Self(),Id(toStr),[Id(chances)])),StringLit( chances to guess: \n))])]))])])"
        num = 380
        self.assertTrue(TestAST.test(input, expect, num))

    def test81(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    $isNum(str: String; length: Int) {
        Var i, j: Int = 0, 0;
        Foreach(i In 0 .. length By 1) {
            If(UltilityElement::$isDigit(System::$toInt(str[i]))){
                Continue;
            }
            Else{
                Return False;
            }
        }
        Return True;
    }
    $isDigit(ch: Int) {
        Return (ch >= 48) && (ch <= 57);
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Var floor, roof: Int = Self.toInt(System::$input()), Self.toInt(System::$input());
        Var chances: Int = (roof - floor) / 5;
        Var answer, guess: Int = System::$random(floor, roof), 0;
        Var str1: String = "Range from " + Self.toStr(floor) + "to " + Self.toStr(roof) + " " + Self.toStr(chances) + " chances to guess: \\n";
        System::$output("Range from " + Self.toStr(floor) + "to " + Self.toStr(roof) + " " + Self.toStr(chances) + " chances to guess: \\n");
        Var times: Int = chances;
        Foreach(times In chances .. 0 By -1) {
            System::$output(times + " chances left, guess: ");
            guess = Self.toInt(System::$input());
            If(guess < answer) {
                System::$output("Wrong, the answer is bigger than " + Self.toStr(guess) + "\\n");
            }
            Elseif(guess > answer) {
                System::$output("Wrong, the answer is smaller than " + Self.toStr(guess) + "\\n");
            }
            Elseif(guess == answer) {
                System::$output("Congrat, the answet is " + Self.toStr(guess) + "\\n");
                Break;
            }
        }
        System::$output("Better luck next time, the answet is " + Self.toStr(guess) + "\\n");
        Return;
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id($isNum),Static,[param(Id(str),StringType),param(Id(length),IntType)],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(j),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(length),IntLit(1),Block([If(CallExpr(Id(UltilityElement),Id($isDigit),[CallExpr(Id(System),Id($toInt),[ArrayCell(Id(str),[Id(i)])])]),Block([Continue]),Block([Return(BooleanLit(False))]))])]),Return(BooleanLit(True))])),MethodDecl(Id($isDigit),Static,[param(Id(ch),IntType)],Block([Return(BinaryOp(&&,BinaryOp(>=,Id(ch),IntLit(48)),BinaryOp(<=,Id(ch),IntLit(57))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(floor),IntType,CallExpr(Self(),Id(toInt),[CallExpr(Id(System),Id($input),[])])),VarDecl(Id(roof),IntType,CallExpr(Self(),Id(toInt),[CallExpr(Id(System),Id($input),[])])),VarDecl(Id(chances),IntType,BinaryOp(/,BinaryOp(-,Id(roof),Id(floor)),IntLit(5))),VarDecl(Id(answer),IntType,CallExpr(Id(System),Id($random),[Id(floor),Id(roof)])),VarDecl(Id(guess),IntType,IntLit(0)),VarDecl(Id(str1),StringType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(Range from ),CallExpr(Self(),Id(toStr),[Id(floor)])),StringLit(to )),CallExpr(Self(),Id(toStr),[Id(roof)])),StringLit( )),CallExpr(Self(),Id(toStr),[Id(chances)])),StringLit( chances to guess: \n))),Call(Id(System),Id($output),[BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(Range from ),CallExpr(Self(),Id(toStr),[Id(floor)])),StringLit(to )),CallExpr(Self(),Id(toStr),[Id(roof)])),StringLit( )),CallExpr(Self(),Id(toStr),[Id(chances)])),StringLit( chances to guess: \n))]),VarDecl(Id(times),IntType,Id(chances)),For(Id(times),Id(chances),IntLit(0),UnaryOp(-,IntLit(1)),Block([Call(Id(System),Id($output),[BinaryOp(+,Id(times),StringLit( chances left, guess: ))]),AssignStmt(Id(guess),CallExpr(Self(),Id(toInt),[CallExpr(Id(System),Id($input),[])])),If(BinaryOp(<,Id(guess),Id(answer)),Block([Call(Id(System),Id($output),[BinaryOp(+,BinaryOp(+,StringLit(Wrong, the answer is bigger than ),CallExpr(Self(),Id(toStr),[Id(guess)])),StringLit(\n))])]),If(BinaryOp(>,Id(guess),Id(answer)),Block([Call(Id(System),Id($output),[BinaryOp(+,BinaryOp(+,StringLit(Wrong, the answer is smaller than ),CallExpr(Self(),Id(toStr),[Id(guess)])),StringLit(\n))])]),If(BinaryOp(==,Id(guess),Id(answer)),Block([Call(Id(System),Id($output),[BinaryOp(+,BinaryOp(+,StringLit(Congrat, the answet is ),CallExpr(Self(),Id(toStr),[Id(guess)])),StringLit(\n))]),Break]))))])]),Call(Id(System),Id($output),[BinaryOp(+,BinaryOp(+,StringLit(Better luck next time, the answet is ),CallExpr(Self(),Id(toStr),[Id(guess)])),StringLit(\n))]),Return()]))])])"
        num = 381
        self.assertTrue(TestAST.test(input, expect, num))

    def test82(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    $isNum(str: String; length: Int) {
        Var i, j: Int = 0, 0;
        Foreach(i In 0 .. length By 1) {
            If(UltilityElement::$isDigit(System::$toInt(str[i]))){
                Continue;
            }
            Else{
                Return False;
            }
        }
        Return True;
    }
    $isDigit(ch: Int) {
        Return (ch >= 48) && (ch <= 57);
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        result = Self.main();
        Return;
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id($isNum),Static,[param(Id(str),StringType),param(Id(length),IntType)],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(j),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(length),IntLit(1),Block([If(CallExpr(Id(UltilityElement),Id($isDigit),[CallExpr(Id(System),Id($toInt),[ArrayCell(Id(str),[Id(i)])])]),Block([Continue]),Block([Return(BooleanLit(False))]))])]),Return(BooleanLit(True))])),MethodDecl(Id($isDigit),Static,[param(Id(ch),IntType)],Block([Return(BinaryOp(&&,BinaryOp(>=,Id(ch),IntLit(48)),BinaryOp(<=,Id(ch),IntLit(57))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(result),CallExpr(Self(),Id(main),[])),Return()]))])])"
        num = 382
        self.assertTrue(TestAST.test(input, expect, num))

    def test83(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    squareRootNewtonMethod(num, loop: Int; delta: Float) {
        Var i, x: Int = 0,1;
        Foreach(i In 0 .. loop By 1) {
            Var fx, dfx: Float = x * x - num, 2 * x;
            x = x - fx / dfx;
            If (x * x - num < delta) {
                Break;
            }
            Else {
                Continue;
            }
        }
        Return x;
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Var x1, x2: Float = (New UltilityElement()).squareRootNewtonMethod(2), (New UltilityElement()).squareRootNewtonMethod(3);
        Return;
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id(squareRootNewtonMethod),Instance,[param(Id(num),IntType),param(Id(loop),IntType),param(Id(delta),FloatType)],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(x),IntType,IntLit(1)),For(Id(i),IntLit(0),Id(loop),IntLit(1),Block([VarDecl(Id(fx),FloatType,BinaryOp(-,BinaryOp(*,Id(x),Id(x)),Id(num))),VarDecl(Id(dfx),FloatType,BinaryOp(*,IntLit(2),Id(x))),AssignStmt(Id(x),BinaryOp(-,Id(x),BinaryOp(/,Id(fx),Id(dfx)))),If(BinaryOp(<,BinaryOp(-,BinaryOp(*,Id(x),Id(x)),Id(num)),Id(delta)),Block([Break]),Block([Continue]))])]),Return(Id(x))]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x1),FloatType,CallExpr(NewExpr(Id(UltilityElement),[]),Id(squareRootNewtonMethod),[IntLit(2)])),VarDecl(Id(x2),FloatType,CallExpr(NewExpr(Id(UltilityElement),[]),Id(squareRootNewtonMethod),[IntLit(3)])),Return()]))])])"
        num = 383
        self.assertTrue(TestAST.test(input, expect, num))

    def test84(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    squareRootNewtonMethod(num, loop: Int; delta: Float) {
        Var i, x: Int = 0,1;
        Foreach(i In 0 .. loop By 1) {
            Var fx, dfx: Float = x * x - num, 2 * x;
            x = x - fx / dfx;
            If (x * x - num < delta) {
                Break;
            }
            Else {
                Continue;
            }
        }
        Return x;
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Var x1, x2: Float = (New UltilityElement()).squareRootNewtonMethod(2), (New UltilityElement()).squareRootNewtonMethod(3);
        Return;
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id(squareRootNewtonMethod),Instance,[param(Id(num),IntType),param(Id(loop),IntType),param(Id(delta),FloatType)],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(x),IntType,IntLit(1)),For(Id(i),IntLit(0),Id(loop),IntLit(1),Block([VarDecl(Id(fx),FloatType,BinaryOp(-,BinaryOp(*,Id(x),Id(x)),Id(num))),VarDecl(Id(dfx),FloatType,BinaryOp(*,IntLit(2),Id(x))),AssignStmt(Id(x),BinaryOp(-,Id(x),BinaryOp(/,Id(fx),Id(dfx)))),If(BinaryOp(<,BinaryOp(-,BinaryOp(*,Id(x),Id(x)),Id(num)),Id(delta)),Block([Break]),Block([Continue]))])]),Return(Id(x))]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x1),FloatType,CallExpr(NewExpr(Id(UltilityElement),[]),Id(squareRootNewtonMethod),[IntLit(2)])),VarDecl(Id(x2),FloatType,CallExpr(NewExpr(Id(UltilityElement),[]),Id(squareRootNewtonMethod),[IntLit(3)])),Return()]))])])"
        num = 384
        self.assertTrue(TestAST.test(input, expect, num))

    def test85(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    splitString(str: String; size: Int; strlist: Array[String, 10000]; delimiter: String) {
        Var word: String = "";
        Var idx, num: Int = 0, 0;
        Foreach(idx In 0 .. size - 1 By 1) {
            If (!(str[i] ==. delimiter)) {
                word = word +. str[i];
            }
            Elseif (!(word ==. "")) {
                strlist[num] = word;
                num = num + 1;
                word = "";
            }
        }
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Val myStr, delimiter: String = System::$input(), System::$input();
        Var myStrList: Array[String, 10000];
        UltilityElement.splitString(
            myStr, Self.length(myStr), myStrList, delimiter);
        Return;
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id(splitString),Instance,[param(Id(str),StringType),param(Id(size),IntType),param(Id(strlist),ArrayType(10000,StringType)),param(Id(delimiter),StringType)],Block([VarDecl(Id(word),StringType,StringLit()),VarDecl(Id(idx),IntType,IntLit(0)),VarDecl(Id(num),IntType,IntLit(0)),For(Id(idx),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([If(UnaryOp(!,BinaryOp(==.,ArrayCell(Id(str),[Id(i)]),Id(delimiter))),Block([AssignStmt(Id(word),BinaryOp(+.,Id(word),ArrayCell(Id(str),[Id(i)])))]),If(UnaryOp(!,BinaryOp(==.,Id(word),StringLit())),Block([AssignStmt(ArrayCell(Id(strlist),[Id(num)]),Id(word)),AssignStmt(Id(num),BinaryOp(+,Id(num),IntLit(1))),AssignStmt(Id(word),StringLit())])))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(myStr),StringType,CallExpr(Id(System),Id($input),[])),ConstDecl(Id(delimiter),StringType,CallExpr(Id(System),Id($input),[])),VarDecl(Id(myStrList),ArrayType(10000,StringType)),Call(Id(UltilityElement),Id(splitString),[Id(myStr),CallExpr(Self(),Id(length),[Id(myStr)]),Id(myStrList),Id(delimiter)]),Return()]))])])"
        num = 385
        self.assertTrue(TestAST.test(input, expect, num))

    def test86(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    euclidGreatestCommonDivisor(a,b: Int) {
        If (b == 0) {
            Return a;
        }
        Else {
            Return Self.euclidGreatestCommonDivisor(b, a % b);
        }
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Val str1, str2: String = System::$input(), System::$input();
        Var a, b: Int = Self.toInt(str1), Self.toInt(str2);
        Val util: UltilityElement = New UltilityElement();
        Var gcd: Int = util.euclidGreatestCommonDivisor(a,b);
        Return;
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id(euclidGreatestCommonDivisor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([If(BinaryOp(==,Id(b),IntLit(0)),Block([Return(Id(a))]),Block([Return(CallExpr(Self(),Id(euclidGreatestCommonDivisor),[Id(b),BinaryOp(%,Id(a),Id(b))]))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(str1),StringType,CallExpr(Id(System),Id($input),[])),ConstDecl(Id(str2),StringType,CallExpr(Id(System),Id($input),[])),VarDecl(Id(a),IntType,CallExpr(Self(),Id(toInt),[Id(str1)])),VarDecl(Id(b),IntType,CallExpr(Self(),Id(toInt),[Id(str2)])),ConstDecl(Id(util),ClassType(Id(UltilityElement)),NewExpr(Id(UltilityElement),[])),VarDecl(Id(gcd),IntType,CallExpr(Id(util),Id(euclidGreatestCommonDivisor),[Id(a),Id(b)])),Return()]))])])"
        num = 386
        self.assertTrue(TestAST.test(input, expect, num))

    def test87(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
    towerOfHanoiSolution(degree: Int; from: String; aux: String; to: String) {
        If (degree == 0){ Return; }
        Self.towerOfHanoiSolution(degree - 1, from, aux, to);
        System::$output("Move disk " + n + " from rod " + from + " to rod " + to);
        Self.towerOfHanoiSolution(degree - 1, aux, to, from);
    }
}
Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Val str1: String = System::$input();
        Var n: Int = Self.toInt(str1);
        Val util: UltilityElement = New UltilityElement();
        Var from, aux, to: String = System::$input(), System::$input(), System::$input();
        util.towerOfHanoiSolution(n, from, aux, to);
        Return;
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([])),MethodDecl(Id(towerOfHanoiSolution),Instance,[param(Id(degree),IntType),param(Id(from),StringType),param(Id(aux),StringType),param(Id(to),StringType)],Block([If(BinaryOp(==,Id(degree),IntLit(0)),Block([Return()])),Call(Self(),Id(towerOfHanoiSolution),[BinaryOp(-,Id(degree),IntLit(1)),Id(from),Id(aux),Id(to)]),Call(Id(System),Id($output),[BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(Move disk ),Id(n)),StringLit( from rod )),Id(from)),StringLit( to rod )),Id(to))]),Call(Self(),Id(towerOfHanoiSolution),[BinaryOp(-,Id(degree),IntLit(1)),Id(aux),Id(to),Id(from)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(str1),StringType,CallExpr(Id(System),Id($input),[])),VarDecl(Id(n),IntType,CallExpr(Self(),Id(toInt),[Id(str1)])),ConstDecl(Id(util),ClassType(Id(UltilityElement)),NewExpr(Id(UltilityElement),[])),VarDecl(Id(from),StringType,CallExpr(Id(System),Id($input),[])),VarDecl(Id(aux),StringType,CallExpr(Id(System),Id($input),[])),VarDecl(Id(to),StringType,CallExpr(Id(System),Id($input),[])),Call(Id(util),Id(towerOfHanoiSolution),[Id(n),Id(from),Id(aux),Id(to)]),Return()]))])])"
        num = 387
        self.assertTrue(TestAST.test(input, expect, num))

    def test88(self):
        input = """
Class System {
    $input() {
        Return "";
    }
    $output(str: String) {
    }
}
Class Element {
    Constructor(){}
    Destructor(){}
    spamFunction(x1, x2, x3: Array[String, 4]; y1, y2: Float) {}
}
Class SortElement : Element {
}
Class UtilityElement : Element{
    mergeSort(arr: Array[Int, 10000]; left, right: Int) {
        If (left > right) {
            Var mid: Int = left + (right - left) / 2;
            Self.mergeSort(arr, left, mid);
            Self.mergeSort(arr, mid, right);
            Self.merge(arr, left, mid, right);
        }
    }

    merge(arr: Array[Int, 10000]; left, mid, right: Int) {
        Var lIdx, rIdx, mIdx: Int = 0, 0, 0;
        Var lSize, rSize: Int = mid - left + 1, right - mid;
        Var lArray, rArray: Array[Int, 10000];
        ## Copy data to temp arrays L[] and R[] ##
        Foreach(lIdx In 0 .. lSize By 1) {
            lArray[lIdx] = arr[left + lIdx];
        }
        Foreach(rIdx In 0 .. rSize By 1) {
            lArray[rIdx] = arr[mid + 1 + rIdx];
        }

        ## Merge the temp arrays back into arr[left..right] ##
        lIdx = 0; ## Initial index of first subarray ##
        rIdx = 0; ## Initial index of second subarray ##
        mIdx = left; ## Initial index of merged subarray ##
        Var infCounter: Int = 0;
        Foreach(infCounter In 0 .. 1 By -1){
            If((lIdx < leftSize) && (rIdx < rightSize)) {
                If (lArray[lIdx] <= rArray[rIdx]) {
                    arr[mIdx] = lArray[lIdx];
                    lIdx = lIdx + 1;
                }
                Else {
                    arr[mIdx] = rArray[rIdx];
                    rIdx = rIdx + 1;
                }
                mIdx = mIdx + 1;
            }
            Else {
                Break;
            }
        }

    ## Copy the remaining elements of L[], if there are any ##
        Foreach(infCounter In 0 .. 1 By -1){
            If (lIdx < lSize) {
                arr[mIdx] = lArray[lIdx];
                lIdx = lIdx + 1;
                mIdx = mIdx + 1;
            }
            Else {
                Break;
            }
        }

    ## Copy the remaining elements of R[], if there are any ##
        Foreach(infCounter In 0 .. 1 By -1){
            If (rIdx < rSize) {
                arr[mIdx] = lArray[lIdx];
                rIdx = rIdx + 1;
                mIdx = mIdx + 1;
            }
            Else {
                Break;
            }
        }
    }
}

Class Program {
    toInt(str: String) {
        Return 123;
    }
    toStr(i: Int) {
        Return "123";
    }
    main() {
        Var el: Element = Self.method();
        Var util: UtilityElement = New UtilityElement(el);
        Var sort: SortElement = New SortElement(el);
        Var size: Int;
        size = Element::$system.in.input();
        Var arr: Array[Float, 10000];
        Var i: Int = 0;
        Foreach(i In 0 .. (size - 1)) {
            Val str: String = Element::$system.in.input();
            If (Self.isDigit(str)) {
                arr[i] = Self.toInt(str);
            }
        }
        util.mergeSort(arr, 0, size - 1);
        Foreach(i In 0 .. (size - 1)) {
            Element::$system.out.print(arr[i]);
        }
    }
}
        """
        expect = r"Program([ClassDecl(Id(System),[MethodDecl(Id($input),Static,[],Block([Return(StringLit())])),MethodDecl(Id($output),Static,[param(Id(str),StringType)],Block([]))]),ClassDecl(Id(Element),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(spamFunction),Instance,[param(Id(x1),ArrayType(4,StringType)),param(Id(x2),ArrayType(4,StringType)),param(Id(x3),ArrayType(4,StringType)),param(Id(y1),FloatType),param(Id(y2),FloatType)],Block([]))]),ClassDecl(Id(SortElement),Id(Element),[]),ClassDecl(Id(UtilityElement),Id(Element),[MethodDecl(Id(mergeSort),Instance,[param(Id(arr),ArrayType(10000,IntType)),param(Id(left),IntType),param(Id(right),IntType)],Block([If(BinaryOp(>,Id(left),Id(right)),Block([VarDecl(Id(mid),IntType,BinaryOp(+,Id(left),BinaryOp(/,BinaryOp(-,Id(right),Id(left)),IntLit(2)))),Call(Self(),Id(mergeSort),[Id(arr),Id(left),Id(mid)]),Call(Self(),Id(mergeSort),[Id(arr),Id(mid),Id(right)]),Call(Self(),Id(merge),[Id(arr),Id(left),Id(mid),Id(right)])]))])),MethodDecl(Id(merge),Instance,[param(Id(arr),ArrayType(10000,IntType)),param(Id(left),IntType),param(Id(mid),IntType),param(Id(right),IntType)],Block([VarDecl(Id(lIdx),IntType,IntLit(0)),VarDecl(Id(rIdx),IntType,IntLit(0)),VarDecl(Id(mIdx),IntType,IntLit(0)),VarDecl(Id(lSize),IntType,BinaryOp(+,BinaryOp(-,Id(mid),Id(left)),IntLit(1))),VarDecl(Id(rSize),IntType,BinaryOp(-,Id(right),Id(mid))),VarDecl(Id(lArray),ArrayType(10000,IntType)),VarDecl(Id(rArray),ArrayType(10000,IntType)),For(Id(lIdx),IntLit(0),Id(lSize),IntLit(1),Block([AssignStmt(ArrayCell(Id(lArray),[Id(lIdx)]),ArrayCell(Id(arr),[BinaryOp(+,Id(left),Id(lIdx))]))])]),For(Id(rIdx),IntLit(0),Id(rSize),IntLit(1),Block([AssignStmt(ArrayCell(Id(lArray),[Id(rIdx)]),ArrayCell(Id(arr),[BinaryOp(+,BinaryOp(+,Id(mid),IntLit(1)),Id(rIdx))]))])]),AssignStmt(Id(lIdx),IntLit(0)),AssignStmt(Id(rIdx),IntLit(0)),AssignStmt(Id(mIdx),Id(left)),VarDecl(Id(infCounter),IntType,IntLit(0)),For(Id(infCounter),IntLit(0),IntLit(1),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(&&,BinaryOp(<,Id(lIdx),Id(leftSize)),BinaryOp(<,Id(rIdx),Id(rightSize))),Block([If(BinaryOp(<=,ArrayCell(Id(lArray),[Id(lIdx)]),ArrayCell(Id(rArray),[Id(rIdx)])),Block([AssignStmt(ArrayCell(Id(arr),[Id(mIdx)]),ArrayCell(Id(lArray),[Id(lIdx)])),AssignStmt(Id(lIdx),BinaryOp(+,Id(lIdx),IntLit(1)))]),Block([AssignStmt(ArrayCell(Id(arr),[Id(mIdx)]),ArrayCell(Id(rArray),[Id(rIdx)])),AssignStmt(Id(rIdx),BinaryOp(+,Id(rIdx),IntLit(1)))])),AssignStmt(Id(mIdx),BinaryOp(+,Id(mIdx),IntLit(1)))]),Block([Break]))])]),For(Id(infCounter),IntLit(0),IntLit(1),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(<,Id(lIdx),Id(lSize)),Block([AssignStmt(ArrayCell(Id(arr),[Id(mIdx)]),ArrayCell(Id(lArray),[Id(lIdx)])),AssignStmt(Id(lIdx),BinaryOp(+,Id(lIdx),IntLit(1))),AssignStmt(Id(mIdx),BinaryOp(+,Id(mIdx),IntLit(1)))]),Block([Break]))])]),For(Id(infCounter),IntLit(0),IntLit(1),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(<,Id(rIdx),Id(rSize)),Block([AssignStmt(ArrayCell(Id(arr),[Id(mIdx)]),ArrayCell(Id(lArray),[Id(lIdx)])),AssignStmt(Id(rIdx),BinaryOp(+,Id(rIdx),IntLit(1))),AssignStmt(Id(mIdx),BinaryOp(+,Id(mIdx),IntLit(1)))]),Block([Break]))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(toInt),Instance,[param(Id(str),StringType)],Block([Return(IntLit(123))])),MethodDecl(Id(toStr),Instance,[param(Id(i),IntType)],Block([Return(StringLit(123))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(el),ClassType(Id(Element)),CallExpr(Self(),Id(method),[])),VarDecl(Id(util),ClassType(Id(UtilityElement)),NewExpr(Id(UtilityElement),[Id(el)])),VarDecl(Id(sort),ClassType(Id(SortElement)),NewExpr(Id(SortElement),[Id(el)])),VarDecl(Id(size),IntType),AssignStmt(Id(size),CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),VarDecl(Id(arr),ArrayType(10000,FloatType)),VarDecl(Id(i),IntType,IntLit(0)),For(Id(i),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([ConstDecl(Id(str),StringType,CallExpr(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(in)),Id(input),[])),If(CallExpr(Self(),Id(isDigit),[Id(str)]),Block([AssignStmt(ArrayCell(Id(arr),[Id(i)]),CallExpr(Self(),Id(toInt),[Id(str)]))]))])]),Call(Id(util),Id(mergeSort),[Id(arr),IntLit(0),BinaryOp(-,Id(size),IntLit(1))]),For(Id(i),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([Call(FieldAccess(FieldAccess(Id(Element),Id($system)),Id(out)),Id(print),[ArrayCell(Id(arr),[Id(i)])])])])]))])])"
        num = 388
        self.assertTrue(TestAST.test(input, expect, num))

    def test89_if_statement(self):
        input = r"""
            Class Program {
                main() {
                    If(True){}
                    Elseif(False){}
                    Else{}
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BooleanLit(True),Block([]),If(BooleanLit(False),Block([]),Block([])))]))])])"
        num = 389
        self.assertTrue(TestAST.test(input, expect, num))

    def test90_break_statement(self):
        input = r"""
            Class Program {
                main() {
                    Foreach (i In 1 .. 100) {
                        Break;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Break])])]))])])"
        num = 390
        self.assertTrue(TestAST.test(input, expect, num))

    def test91_continue_statement(self):
        input = r"""
            Class Program {
                main() {
                    Foreach (i In 1 .. 100) {
                        Continue;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Continue])])]))])])"
        num = 391
        self.assertTrue(TestAST.test(input, expect, num))

    def test92_array_cell_access(self):
        input = r"""
            Class Program {
                method() {
                    Var a: Array[Array[Array[Int, 4], 3], 2];
                    a[1] = 1;
                    a[1][2] = 1;
                    a[1][2][3] = 1;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(3,ArrayType(4,IntType)))),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(1))]))])])"
        num = 392
        self.assertTrue(TestAST.test(input, expect, num))

    def test93_method_access(self):
        input = r"""
            Class Program {
                method() {
                    a.b();
                    a.b.c();
                    a.b().c();
                    a.b.c.d();
                    a.b.c().d();
                    a.b().c().d();
                    a::$b();
                    a::$b().c();
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(Id(a),Id(b),[]),Call(FieldAccess(Id(a),Id(b)),Id(c),[]),Call(CallExpr(Id(a),Id(b),[]),Id(c),[]),Call(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[]),Call(CallExpr(FieldAccess(Id(a),Id(b)),Id(c),[]),Id(d),[]),Call(CallExpr(CallExpr(Id(a),Id(b),[]),Id(c),[]),Id(d),[]),Call(Id(a),Id($b),[]),Call(CallExpr(Id(a),Id($b),[]),Id(c),[])]))])])"
        num = 393
        self.assertTrue(TestAST.test(input, expect, num))

    def test94_object_creation(self):
        input = """
            Class Object {

            }
            Class Program {
                Var a: Object = New Object();
                Var a: Object = New Object(New Object(1,2,3));
                Var a: Object = New Object(1,2,3);
            }
        """
        expect = "Program([ClassDecl(Id(Object),[]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Object)),NewExpr(Id(Object),[]))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Object)),NewExpr(Id(Object),[NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3)])]))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Object)),NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3)])))])])"
        num = 394
        self.assertTrue(TestAST.test(input, expect, num))

    def test95_string_expression(self):
        input = """
            Class Program {
                Var str1, str2: String = "abc" +. "xyz", "abc" ==. "xyz";
                Var str1, str2: String;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(str1),StringType,BinaryOp(+.,StringLit(abc),StringLit(xyz)))),AttributeDecl(Instance,VarDecl(Id(str2),StringType,BinaryOp(==.,StringLit(abc),StringLit(xyz)))),AttributeDecl(Instance,VarDecl(Id(str1),StringType)),AttributeDecl(Instance,VarDecl(Id(str2),StringType))])])"""
        num = 395
        self.assertTrue(TestAST.test(input, expect, num))

    def test96_logical_expression(self):
        input = """
            Class Program {
                Var a, b: Boolean = a && True, b || False;
                Var a, b: Boolean;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),BoolType,BinaryOp(&&,Id(a),BooleanLit(True)))),AttributeDecl(Instance,VarDecl(Id(b),BoolType,BinaryOp(||,Id(b),BooleanLit(False)))),AttributeDecl(Instance,VarDecl(Id(a),BoolType)),AttributeDecl(Instance,VarDecl(Id(b),BoolType))])])"""
        num = 396
        self.assertTrue(TestAST.test(input, expect, num))

    def test97_adding_expression(self):
        input = """
            Class Program {
                Var a, b: Int = a + 1, b - 1;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,Id(a),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(-,Id(b),IntLit(1))))])])"""
        num = 397
        self.assertTrue(TestAST.test(input, expect, num))

    def test98_multiplying_expression(self):
        input = """
            Class Program {
                Var a, b, c: Int = a * 1, b / 1, c % 1;
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(*,Id(a),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(/,Id(b),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(%,Id(c),IntLit(1))))])])"""
        num = 398
        self.assertTrue(TestAST.test(input, expect, num))

    def test99_negative_expression(self):
        input = """
            Class Program {
                Var a, b: Int = !True, !False;
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,UnaryOp(!,BooleanLit(True)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,UnaryOp(!,BooleanLit(False))))])])"
        num = 399
        self.assertTrue(TestAST.test(input, expect, num))

    def test100_sign_expression(self):
        input = """
            Class Program {
                Var a, b: Int = -123, -a;
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,UnaryOp(-,IntLit(123)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,UnaryOp(-,Id(a))))])])"
        num = 400
        self.assertTrue(TestAST.test(input, expect, num))
