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
        Val b1, b2 : Int = 1, 2 ;
    }
    If ( boolean_expr ){
        Val c1, c2 : Int = 1, 2 ;
        If ( boolean_expr ){
            Val d1, d2 : Int = 1, 2 ;
        }
    }
    Return Self.length * Self.width ;
}
            }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(length),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(width),IntType,IntLit(2))),MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(a1),IntType,IntLit(1)),ConstDecl(Id(a2),IntType,IntLit(2)),If(Id(boolean_expr),Block([ConstDecl(Id(b1),IntType,IntLit(1)),ConstDecl(Id(b2),IntType,IntLit(2))])),If(Id(boolean_expr),Block([ConstDecl(Id(c1),IntType,IntLit(1)),ConstDecl(Id(c2),IntType,IntLit(2)),If(Id(boolean_expr),Block([ConstDecl(Id(d1),IntType,IntLit(1)),ConstDecl(Id(d2),IntType,IntLit(2))]))])),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),[[IntLit(1)],StringLit(String)]),VarDecl(Id(y),ClassType(Id(HelloClass)),ArrayCell(CallExpr(Id(IdVar),Id(funcCall),[]),[StringLit(Index on a function return value)]))])),MethodDecl(Id(main),Instance,[],Block([]))])])"""
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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),IntLit(0)),VarDecl(Id(y),ClassType(Id(HelloClass)),FieldAccess(CallExpr(CallExpr(NewExpr(Id(ClassObj),[FloatLit(4.5),BinaryOp(/,Id(x),FloatLit(4.5)),ArrayCell(Id(t),[IntLit(0)])]),Id(funcCall),[]),Id(funcCall2),[]),Id(attrAccess)))])),MethodDecl(Id(main),Instance,[],Block([]))])])"
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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[param(Id(x),IntType),param(Id(y),StringType)],Block([VarDecl(Id(x),ClassType(Id(HelloClass)),IntLit(0)),VarDecl(Id(y),ClassType(Id(HelloClass)),ArrayCell(NewExpr(Id(ClassObj),[FloatLit(4.5),BinaryOp(/,Id(x),Id(z)),ArrayCell(Id(t),[IntLit(0)])]),[FieldAccess(CallExpr(CallExpr(Id(Classname),Id($funcCall),[]),Id(funcCall2),[]),Id(attrAccess))]))])),MethodDecl(Id(main),Instance,[],Block([]))])])"
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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),ArrayType(5,IntType),BooleanLit(True)),VarDecl(Id(b),ArrayType(5,IntType),[BooleanLit(True),[BooleanLit(False)]]),AssignStmt(Id(x),BinaryOp(+,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1))))),IntLit(2))),AssignStmt(Id(x),BinaryOp(==,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1)))))),IntLit(2))),AssignStmt(Id(x),BinaryOp(!=,IntLit(1),BinaryOp(+,IntLit(2),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(2))))))))),AssignStmt(Id(x),BinaryOp(+,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(2))))),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(2)))))))),AssignStmt(Id(x),BinaryOp(>,IntLit(1),UnaryOp(-,IntLit(2)))),AssignStmt(Id(x),BinaryOp(<,IntLit(1),BinaryOp(+,UnaryOp(-,IntLit(2)),IntLit(2)))),AssignStmt(Id(x),BinaryOp(>=,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)))),AssignStmt(Id(x),BinaryOp(<=,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2))))]))])])"
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
                    a = a.b.c.d(3,4+5,Array(Array(0))).e(3,4+5,Array(Array(0)));
                    a = a.d(3,4+5,Array(Array(0))).e(3,4+5,Array(Array(0))).b.c;

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),FieldAccess(Id(a),Id(b))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(a),Id(b)),Id(c))),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[FieldAccess(Id(e),Id(f))])),AssignStmt(Id(a),FieldAccess(Id(a),Id($b))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(a),Id($b)),Id(c))),AssignStmt(Id(a),CallExpr(FieldAccess(Id(a),Id($b)),Id(d),[FieldAccess(Id(e),Id(f))])),AssignStmt(Id(a),CallExpr(Id(a),Id(b),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(Id(a),Id(b),[Id(a),Id(b),Id(c)]),Id(c),[Id(a),Id(b),Id(c)]),Id(d)),Id(c))),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(CallExpr(Id(a),Id(b),[Id(a),Id(b),Id(c)]),Id(d)),Id(c),[Id(a),Id(b),Id(c)]),Id(d),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[IntLit(3),BinaryOp(+,IntLit(4),IntLit(5)),[[IntLit(0)]]]),Id(e),[IntLit(3),BinaryOp(+,IntLit(4),IntLit(5)),[[IntLit(0)]]])),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(Id(a),Id(d),[IntLit(3),BinaryOp(+,IntLit(4),IntLit(5)),[[IntLit(0)]]]),Id(e),[IntLit(3),BinaryOp(+,IntLit(4),IntLit(5)),[[IntLit(0)]]]),Id(b)),Id(c))),AssignStmt(Id(a),CallExpr(CallExpr(Id(A),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(Id(B),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(CallExpr(CallExpr(CallExpr(Id(C),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute))),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(CallExpr(Id(D),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute))),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(CallExpr(CallExpr(CallExpr(Id(C),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(CallExpr(Id(D),Id($method),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)]),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute)),Id(method),[Id(a),Id(b),Id(c)]),Id(attribute)),Id(attribute))),AssignStmt(Id(a),BinaryOp(+,IntLit(30),CallExpr(FieldAccess(FieldAccess(FieldAccess(FloatLit(1230.0),Id(a)),Id(a)),Id(a)),Id(a),[]))),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(CallExpr(FloatLit(123.12),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Id(a),[IntLit(123)]),Id(a),[IntLit(123)])),AssignStmt(Id(a),FieldAccess(NewExpr(Id(X),[]),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b))),AssignStmt(Id(a),FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i))),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i)),Id(k),[]),Id(l),[]),Id(m),[])),AssignStmt(Id(a),BinaryOp(+,FieldAccess(NewExpr(Id(X),[]),Id(a)),CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i)),Id(k),[]),Id(l),[]),Id(m),[]))),AssignStmt(Id(a),BinaryOp(+,IntLit(5),ArrayCell(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),[ArrayCell(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i)),[CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b)),Id(c),[]),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(i)),Id(k),[]),Id(l),[]),Id(m),[])])])))]))])])"
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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(x),ArrayType(3,ArrayType(3,IntType)),IntLit(1)),VarDecl(Id(y),ArrayType(3,ArrayType(3,IntType)),IntLit(2)),VarDecl(Id(z),ArrayType(3,ArrayType(3,IntType)),IntLit(3))]))])])"
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
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),ArrayType(1,IntType),[]),VarDecl(Id(b),ArrayType(1,IntType),BinaryOp(==,Id(a),FloatLit(5.4))),AssignStmt(Id(b),[])]))])])"
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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(FieldAccess(Id(X),Id($a)),IntLit(1)),AssignStmt(FieldAccess(Id(Y),Id($a)),BinaryOp(-,BinaryOp(+,IntLit(65535),IntLit(9)),BinaryOp(*,IntLit(5349),IntLit(1)))),AssignStmt(ArrayCell(Id(arr),[IntLit(1),IntLit(2)]),ArrayCell(Id(arr),[ArrayCell(Id(arr),[BinaryOp(+,ArrayCell(Id(arr),[IntLit(1)]),IntLit(3))]),IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(ArrayCell(FieldAccess(Id(Z),Id($arr)),[IntLit(1),IntLit(2),IntLit(3)]),BinaryOp(+,ArrayCell(FieldAccess(NewExpr(Id(A),[]),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(CallExpr(NewExpr(Id(B),[]),Id(a),[]),[IntLit(1),IntLit(2),IntLit(3)]))),AssignStmt(ArrayCell(CallExpr(Id(T),Id($arr),[]),[IntLit(1),IntLit(2),IntLit(3)]),Id(x)),AssignStmt(ArrayCell(CallExpr(Id(M),Id($arr),[]),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[IntLit(1)])])])]),FieldAccess(Id(a),Id(b))),AssignStmt(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),IntLit(1)),AssignStmt(FieldAccess(Id(a),Id($b)),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])]),IntLit(1)),AssignStmt(ArrayCell(FieldAccess(Id(C),Id($a)),[ArrayCell(FieldAccess(Id(C),Id($a)),[IntLit(1)]),ArrayCell(FieldAccess(Id(C),Id($a)),[ArrayCell(FieldAccess(Id(C),Id($a)),[IntLit(1)])]),ArrayCell(FieldAccess(NewExpr(Id(C),[Id(a),Id(b),Id(c),ArrayCell(Id(A),[ArrayCell(Id(B),[IntLit(1)])])]),Id(a)),[ArrayCell(FieldAccess(Id(C),Id($a)),[IntLit(1)])])]),IntLit(1)),AssignStmt(FieldAccess(NewExpr(Id(X),[Id(a),Id(b),Id(c),ArrayCell(Id(A),[ArrayCell(Id(B),[IntLit(1)])])]),Id(a)),FieldAccess(Id(a),Id(b))),AssignStmt(ArrayCell(CallExpr(Self(),Id(a),[]),[IntLit(1),IntLit(2)]),IntLit(1)),AssignStmt(FieldAccess(Id(A),Id($a)),IntLit(1)),AssignStmt(FieldAccess(NewExpr(Id(B),[]),Id(a)),IntLit(1)),AssignStmt(ArrayCell(CallExpr(NewExpr(Id(X),[Id(a),Id(b),Id(c),ArrayCell(Id(A),[ArrayCell(Id(B),[IntLit(1)])])]),Id(a),[]),[IntLit(0)]),IntLit(1)),Return(StringLit(Goodbye))]))])])"
        num = 333
        self.assertTrue(TestAST.test(input, expect, num))

    def test334_loop_statement_scalar_is_method_call(self):
        input = """
            Class Some_class {
                Constructor(int: Int; string: String) {}
                Constructor() {}
                Destructor() {
                }
            }
            Class Program {
                main() {
                    Foreach(h::$a().b[1] In 0 .. 100){
                        Continue;
                    }
                    Foreach(h In 0 .. 100 By 2.2e2){
                        Continue;
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([For(ArrayCell(FieldAccess(CallExpr(Id(h),Id($a),[]),Id(b)),[IntLit(1)]),IntLit(0),IntLit(100),Block([Continue])]),For(Id(h),IntLit(0),IntLit(100),FloatLit(220.0),Block([Continue])])]))])])"
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
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([])),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([VarDecl(Id(a),BoolType,BooleanLit(True)),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([]),Block([VarDecl(Id(a),BoolType,BooleanLit(True))]))])),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([])),If(ArrayCell(FieldAccess(CallExpr(StringLit(string),Id(a),[]),Id(b)),[ArrayCell(Id(Arr),[UnaryOp(-,IntLit(1))])]),Block([]))]),Block([VarDecl(Id(a),BoolType,BooleanLit(True))]))]))])])"
        num = 335
        self.assertTrue(TestAST.test(input, expect, num))

    def test36_if_statement_incorrect_order(self):
        input = r"""
            Class Some_class {
                    Constructor(int: Int; string: String) {}
                    Destructor() {
                        If (a>b){}
                        Elseif(b>c){}
                        Else{}
                    }
            }
            Class Program {
                main() {
                }
            }
        """
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([])),If(BinaryOp(>,Id(b),Id(c)),Block([]),Block([]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        num = 336
        self.assertTrue(TestAST.test(input, expect, num))

    def test37_foreach_statement_continue_outside_loop(self):
        input = """
            Class Some_class {
                    Constructor(int: Int; string: String) {
                        Foreach(A::$b().d In 1 .. 100 By 1) {
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
        expect = "Program([ClassDecl(Id(Some_class),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([For(FieldAccess(CallExpr(Id(A),Id($b),[]),Id(d)),IntLit(1),IntLit(100),IntLit(1),Block([If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([Continue])),If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([Break])),Return(BooleanLit(False))])])])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(x),IntType,IntLit(1)),For(Id(i),IntLit(1),IntLit(100),FloatLit(1.01e-07),Block([Continue,Break,For(Id(k),FloatLit(1.01e-07),IntLit(100),Block([AssignStmt(Id(x),BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(x),Id(i)),Id(j)),Id(k))),Continue])]),If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([Break])),Continue,Break])]),If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([]))]))])])"
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
                        Foreach(j.foo().i In New B() .. IdVar) {
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
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(100),IntLit(1),IntLit(1),Block([If(BinaryOp(||,BooleanLit(True),BooleanLit(False)),Block([Continue])),If(BinaryOp(&&,BooleanLit(True),BooleanLit(False)),Block([Break]))])]),For(Id(i),IntLit(0),NewExpr(Id(A),[]),BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),Block([For(FieldAccess(CallExpr(Id(j),Id(foo),[]),Id(i)),NewExpr(Id(B),[]),Id(IdVar),Block([For(Id(k),UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(100)),BinaryOp(+,FieldAccess(Id(A),Id($i)),BinaryOp(/,Id(j),BinaryOp(%,Id(i),Id(j)))),Block([])])])]),If(NewExpr(Id(A),[BinaryOp(+,StringLit(stringA),StringLit(stringB))]),Block([Continue]))])])]))])])"
        num = 338
        self.assertTrue(TestAST.test(input, expect, num))

    def test39_foreach_statement_static_expr(self):
        input = r"""
            Class Program {
                Constructor(int: Int; string: String) {}
                Constructor() {}
                Destructor() {}
                main() {
                    Foreach(A::$i In A::$i .. A::$i By A::$i) {}
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([For(FieldAccess(Id(A),Id($i)),FieldAccess(Id(A),Id($i)),FieldAccess(Id(A),Id($i)),FieldAccess(Id(A),Id($i)),Block([])])]))])])"
        num = 248
        self.assertTrue(TestAST.test(input, expect, num))

    # def test49_foreach_scalar_is_static_method_error(self):
    #     input = """
    #         Class Program {
    #             main() {
    #                 Foreach (hekki::$i() In yes .. no By why ) {
    #                     hello.comeon();
    #                     Break;
    #                 }
    #                 Return;
    #             }
    #         }
    #     """
    #     expect = "Error on line 4 col 41: In"
    #     num = 249
    #     self.assertTrue(TestAST.test(input, expect, num))

    # def test50_continue_invalid(self):
    #     input = r"""
    #         Class Some_class {
    #                 Constructor(int: Int; string: String) {}
    #                 Constructor() {}
    #                 Destructor() {}
    #         }
    #         Class Program {
    #             main() {
    #                 Foreach (hekki::$i().a In yes .. no By why ) {
    #                     If (hekki::$i()) {
    #                         Continue "string";
    #                     }
    #                 }
    #                 Return;
    #             }
    #         }
    #     """
    #     expect = "Error on line 11 col 37: string"
    #     num = 250
    #     self.assertTrue(TestAST.test(input, expect, num))
