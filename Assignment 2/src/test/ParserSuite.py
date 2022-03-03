import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    def test_200_nothing(self):
        test_in = """
Class {}
"""
        expect = "Error on line 2 col 6: {"
        self.assertTrue(TestParser.test(test_in,expect,200))
    def test_201_simple_program(self):
        test_in = """
Class Program {}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,201))

    def test_202_simple_program_2(self):
        test_in = """
Class Program {
    main () {}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,202))
    
    def test_203_simple_program_3(self):
        test_in = """
Class Program {
    main () {
        a.putIntLn(4);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,203))
    
    def test_204_multi_class(self):
        
        test_in = """
Class Program {}
Class Bullshit{}
Class RapGod{}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,204))
    
    def test_205_extended_class(self):
        test_in = """
Class Program {}
Class Bullshit : someShit{}
Class RapGod{}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,205))

    def test_206_simple_program_4(self):
        test_in = """
Class Program {
    getProcInfo(){}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,206))
    
    def test_207_simple_program(self):
        test_in = """
Class Program {
    getProcInfo(){}
    $showProcInfo(){}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,207))
    
    def test_208_simple_program_2(self):
        test_in = """
Class Program {
    Val temp: Float = 2.3;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,208))
    
    def test_209_simple_program(self):
        test_in = """
Class Program{
    Var bruh, bruh2, bruh3: Boolean = a,b,c;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,209))

    def test_210_no_closing(self):
        test_in = """
Class Program{
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(test_in,expect,210))
    
    def test_211_semi_end(self):
        test_in = """
Class Program{};
"""
        expect = "Error on line 2 col 15: ;"
        self.assertTrue(TestParser.test(test_in,expect,211))

    def test_212_method_no_block(self):  
        test_in = """
Class Program {
    main () ;
}
"""
        expect = "Error on line 3 col 12: ;"
        self.assertTrue(TestParser.test(test_in,expect,212))
    
    def test_213_var_missing_expr(self):
        test_in = """
Class Program{
    Var bruh, bruh2, bruh3: Boolean = a,b;
}
"""
        expect = "Error on line 3 col 41: ;"
        self.assertTrue(TestParser.test(test_in,expect,213))

    def test_214_missing_var_id(self):
        test_in = """
Class Program {
    Var bruh, bruh2: Boolean = a,b,c,e,f;
}
"""
        expect = "Error on line 3 col 34: ,"
        self.assertTrue(TestParser.test(test_in,expect,214))
    
    def test_215_missing_var_id_2(self):
        test_in = """
Class Program{
    Val $susan, agent: Int = 0, 175;
    Var bruh, bruh2, a, b, c, d: Float = 1,2,3,4,5,6,7,8,9;
}
"""
        expect = "Error on line 4 col 52: ,"
        self.assertTrue(TestParser.test(test_in,expect,215))

    def test_216__var_missing_expr_2(self):
        test_in = """
Class Program{
    Val $susan, agent, $ashe, the, decoy: Int = 0, 175;
    Var bruh, bruh2, a, b, c, d: Float = 1,2,3,4,5,6;
}
"""
        expect = "Error on line 3 col 54: ;"
        self.assertTrue(TestParser.test(test_in,expect,216))
    
    def test_217_no_class_found(self):
        test_in = """
## Empty program??? Class Program{} ##
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(test_in,expect,217))

    def test_218_method_decl(self):
        
        test_in = """
Class Program {
    method_full(x, y: Int; z: String) {}
    main () {}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,218))
    
    def test_219_method_decl_2(self):
        test_in = """
Class Program {
    $method_full(x, y: Int; z: String) {}
    $foo_method(){}
    main () {}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,219))

    def test_220_static_var_decl(self):
        test_in = """
Class Program {
    Var $k98, $k99: Int = 98, 99;
    main () {
        Var $k100: Boolean = True;
    }
}
"""
        expect = "Error on line 5 col 12: $k100"
        self.assertTrue(TestParser.test(test_in,expect,220))
    
    def test_221_semi_missing(self):
        test_in = """
Class Program{
    Var $k98, $k99: Int = 98, 99
    main () {
        Var k100: Boolean = True;
    }
}
"""
        expect = "Error on line 4 col 4: main"
        self.assertTrue(TestParser.test(test_in,expect,221))

    def test_222_semi_missing_2(self):
        test_in = """
Class Program{
    Var $k98, $k99: Int = 98, 99;
    main () {
        Var k100: Boolean = True
    }
}
"""
        expect = "Error on line 6 col 4: }"
        self.assertTrue(TestParser.test(test_in,expect,222))
    
    def test_223_array_decl_test(self):
        test_in = """
Class Program{
    Var a: Array[Int, 5];
    Val b: Array[Float, 0xABEF];
    Val _c: Array[String, 0b1011];
    Var $d: Array[Int, 07654];
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,223))

    def test_224_array_lit(self):
        test_in = """
Class Program {
    Var list: Array[Int, 3] = Array(1, 1.1e-3, someClass.method(), Self.x, "foo", class::$y);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,224))
    
    def test_225_multi_dimension_array_decl(self):
        test_in = """
Class Program{
    Val list_String: Array[Array[String, 3], 3] 
    = Array(
        Array("a","b","c"),
        Array("a","b","c"),
        Array("a","b","c")
    );  
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,225))

    def test_226_multi_dimension_array_decl_2(self):
        test_in = """
Class Program {
    Val list_String: Array[Array[String, 3], 3] 
    = Array(
        Array("a","b","c"),
        Array("a","b","c"),
        Array("a","b","c")
    ),Array(
        Array("a","b","c"),
        Array("a","b","c"),
        Array("a","b","c")
    );  
}
"""
        expect = "Error on line 8 col 5: ,"
        self.assertTrue(TestParser.test(test_in,expect,226))
    
    def test_227_array_lit_2(self):
        test_in = """
Class Program{
    Val $k: Array[Int, 3] = Array(0/17%5, !-230, 1+2-3/4, a.method()[3]);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,227))

    def test_228_array_lit_3(self):
        test_in = """
Class Program {
    Val $k: Array[Int, 3] = Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,228))
    
    def test_229_multi_dimension_array_lit(self):
        test_in = """
Class Program {
    Val $k: Array[Int, 3] 
    = Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    );
    Val $k: Array[Int, 3] 
    = Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11))
    );
}
"""
        expect = "Error on line 14 col 4: )"
        self.assertTrue(TestParser.test(test_in,expect,229))

    def test_230_super_complex_array_lit(self):
        test_in = """
Class Program {
    Val $k, l, m, n, j, k, _: Array[Int, 3] 
    = Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    ),
    Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    ),
    Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    ),
    Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    );
}
"""
        expect = "Error on line 23 col 5: ;"
        self.assertTrue(TestParser.test(test_in,expect,230))
    
    def test_231_4_dimension_array(self):
        test_in = """
Class Program{
    Var b: Array[Array[Array[Array[Int, 3], 3], 3], 3]
    = Array(
        Array(
            Array(
                Array("nothing here")
            )
        )
    );
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,231))

    def test_232_super_complex_array_2(self):
        test_in = """
Class Program {
    Var list: Array[Array[Array[Array[Int,1],1],1],0];
    list = Array (
        Array (
            Array (
                "bruh"
            ),
            Array (
                "bruh"
            )
        ),
        Array (
            Array (
                "bruh"
            ),
            Array (
                "bruh"
            )
        )
    );
    Var array: Array[Array[Array[Array[Int,1],1],1],1];
}
"""
        expect = "Error on line 3 col 51: 0"
        self.assertTrue(TestParser.test(test_in,expect,232))
   
    def test_233_constructor_destructor_test(self):
        test_in = """
Class Program{
    Constructor(){}
    Destructor(){}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,233))

    def test_234_constructor_destructor_2(self):

        test_in = """
Class Program {
    Constructor(x, y: Int; z, q: Float){
        x = x;
        y = y;
    }
    Destructor(){
        z = z;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,234))
    
    def test_235_array_0(self):
        test_in = """
Class Program{
    main() {
        Var a: Array[Int, 0];
    }
}
"""
        expect = "Error on line 4 col 26: 0"
        self.assertTrue(TestParser.test(test_in,expect,235))

    def test_236_array_no_element(self):
        test_in = """
Class Program {
    main () {
        Var a: Array[Int, 2] = Array();
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,236))
    
    def test_237_var_const_statement(self):
        test_in = """
Class Program{
    main () {
        Var a,b: Int = 1, 1+2;
        Val a,b,c,d: Int = 1, 1+2,3,4;
        Var a,b,e,f,g,h,i,k,l,m: Int = 1, 1+2, 3,4,5,6,7,8,9,0;
        Val $c: Float;
    }   
}
"""
        expect = "Error on line 7 col 12: $c"
        self.assertTrue(TestParser.test(test_in,expect,237))

    def test_238_assign_statement(self):
        test_in = """
Class Program {
    main() {
        Var a: Int = Array(1,2,3);
        a = Array(1,2,3);
        a = 1234;
        a = 0X123F;
        a = 0b1111;
        a = 07654;
        a = 0XAAAA + 0b1000 - 0357 * 9999 / 3.1e27;
        class::$a = Array(1,2,3);
        class::$a = 1234;
        class::$a = 0X123F;
        class::$a = 0b1111;
        class::$a = 07654;
        class::$a = 0XAAAA + 0b1000 - 0357 * 9999 / 3.1e27; 
        class.a = Array(1,2,3);
        class.a = 1234;
        class.a = 0X123F;
        class.a = 0b1111;
        Self.a = 07654;
        class.a = 0XAAAA + 0b1000 - 0357 * 9999 / 3.1e27;

        foo_var = 1 - 2 && 3 * 4 || 4 + 5;
        foo_var = True + False && False - True && (True && False - True && 0B1111111);
        foo_var = True + False || False - True && (True || False - True || 0B1111111);

        class.foo_var = 1 - 2 && 3 * 4 || 4 + 5;
        class.foo_var = True + False && False - True && (True && False - True && 0B1111111);
        class::$foo_var = True + False || False - True || (True || False - True || 0B1111111);

        foo_arr[125] = a[b[c[3]]];
        foo_arr[125][123][123] = a[b[c[3]]][6][6][6][9];
        foo_arr[125][123][123] = a[b[c[3]]][6][6][6][9] + foo.class().bc(bc)[5][6][7];

        class.foo_arr[125] = a[b[c[3]]];
        class.foo_arr[125][123][123] = a[b[c[3]]][6][6][6][9];
        class::$foo_arr[125][123][123] = a[b[c[3]]][6][6][6][9] + foo.class().bc(bc)[5][6][7];

        a.a.a = 1;
        a::$a = 1;
        a[a] = 1;
        a[a[a[a[a[1]]]]][a[a[1]]] = 1;

        class::$a.a.a[class::$a[1]][class.a[1]] = 1;
        Self.a = 1;
        Self.a.a.a = 1;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,238))
    
    def test_239_if_statement(self):
        test_in = """
Class Program{
    main () {
        If (2>1) {
            Var a,b,c: Int;
            If (a-b-c == 100) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {}
            Elseif (a+b+c >= 200) {}
            Else {
                a = b - c;
            }
        }
        Elseif (a+b+c >= 200) {
            Var a,b,c: Int;
            If (a-b-c == 100) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {}
            Elseif (a+b+c >= 200) {}
            Else {
                a = b - c;
            }
        }
        Elseif (a+b+c >= 200) {
            Var a,b,c: Int;
            If (a-b-c == 100) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {}
            Elseif (a+b+c >= 200) {}
            Else {
                a = b - c;
            }
        }
        Else {
            c = 3;
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,239))

    def test_240_if_statement_error(self):
        test_in = """
Class Program {
    main () {
        If (a-b-c == 100) {
            a = b;
            b = c;
            c = a;
        }
        Elseif (a+b+c >= 200) {
            a = b;
            b = c;
            c = a;
        }
        Elseif (a+b+c >= 200) {}
        Elseif (a+b+c >= 200)
        Else {
            a = b - c;
        }
    }
"""
        expect = "Error on line 16 col 8: Else"
        self.assertTrue(TestParser.test(test_in,expect,240))
    
    def test_241_if_statement_with_lp_rp_1(self):
        test_in = """
Class Program {
    main() {
        If (a-b-c == 100) {
            a = b;
            b = c;
            c = d;
        }
        Elseif() (a+b+c >= 200) {
            a = b;
            b = c;
            c = a;
        }
        Elseif (a+b+c >= 200) {}
        Elseif (a+b+c >= 200)
        Else {
            a = b - c;
        }
    }
}
"""
        expect = """Error on line 9 col 15: )"""
        self.assertTrue(TestParser.test(test_in,expect,241))

    def test_242_if_statement_with_lp_rp_2(self):
        test_in = """
Class Program {
    main() {
        If (a-b-c == 100) {
            a = b;
            b = c;
            c = d;
        }
        Else() {
            a = b - c;
        }
    }
}
"""
        expect = "Error on line 9 col 12: ("
        self.assertTrue(TestParser.test(test_in,expect,242))
    
    
    def test_243_if_statement_missing_part(self):
        test_in = """
Class Program {
    main() {
        If (a-b-c == 100) {
            If (a-b-c == 100) {
                a = b;
                c = d;
            }
            If (a-b-c == 100) {
                a = b;
                c = d;
            }
        }
        Else {
            If (a-b-c == 100) {
                a = b;
                c = d;
            }
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,243))
    

    def test_244_if_wrong_order(self):
        
        test_in = """
Class Program {
    main () {
        If (a-b-c == 100) {}
        Else {}
        Elseif (a+b+c >= 200) {}
        Elseif (a+b+c >= 200) {}
    }
}
"""
        expect = "Error on line 6 col 8: Elseif"
        self.assertTrue(TestParser.test(test_in,expect,244))
    
    def test_245_foreach_statement(self):
        test_in = """
Class Program {
    main () {
        Foreach(i In 1 .. 100 By z) {
            If (True || True) {
                x = y;
            }
            Elseif (True && True) {
                y = z;
            }
        }
        Foreach(i In 1 .. 100 By z) {
            Foreach(j In 1 .. 100 By z) {
                Foreach(k In 1 .. 100 By z) {
                    a = b + c;
                }
            }
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,245))

    def test_246_foreach_statement_2(self):
        test_in = """
Class Program {
    main () {
        Foreach(i/i*i+i-i In 1 .. 100) {
            If (True || True) {
                x = y;
            }
            Elseif (True && True) {
                y = z;
            }
        }
        Foreach(i In x+yield .. 100 By z) {
            Foreach(j In a+b-c*d .. 25 &&y) {
                Foreach(k In 1 .. 100) {
                    a = b + c;
                }
            }
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,246))
    
    def test_247_foreach_stmt_with_static(self):
        test_in = """
Class Program {
    main() {
        Foreach(i/i*i+i-i In class::$var .. 100) {}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,247))
    
    def test_248_break_return_cont_stmt(self):
        test_in = """
Class Program {
    main() {
        Break;
        Continue;
        Return a.foo();
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,248))
    
    def test_249_return_nothing(self):
        test_in = """
Class Program{
    main () {
        Return;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,249))

    def test_250_cont_something(self):
        test_in = """
Class Program{
    main () {
        If (a-b-c == 100) {
            If (a-b-c == 100) {
                a = b;
                c = d;
            }
            If (a-b-c == 100) {
                Continue a = b;
                c = d;
            }
        }
    }
}
"""
        expect = "Error on line 10 col 25: a"
        self.assertTrue(TestParser.test(test_in,expect,250))
    
    def test_251_method_statement(self):
        test_in = """
Class Program{
    method_a (a: Float) {
        If (a-b-c == 100) {
            a = b;
            c = d;
        }
    }
    $method_b (a: Float) {
        If (a-b-c == 100) {
            a = b;
            c = d;
        }
    }
    Constructor(a: Float) {}
    Destructor(){}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,251))

    def test_252_method_statement_2(self):  
        test_in = """
Class Program {
    main () {
        class.method(a,b,c);
        class.method(1+2+3+4+5);
        class::$assertTrue(NotImplemented);
        class.a.b.c.d.e.f.g.h.i.k.l.m();
        class::$assertTrue.assertTrue.abc.d.e();
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,252))
    
    def test_253_self_method(self):
        test_in = """
Class Program{
    main () {
        Self.a = 3;
        Self.b.c.d.e.f.g.h.i.k.l.m();
        Self.Method(a,b,c,d,e,f,g);
    }
    
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,253))

    def test_254_self_error(self):
        test_in = """
Class Program {
    main () {
        Self::$a = 3;
    }
}
"""
        expect = "Error on line 4 col 12: ::"
        self.assertTrue(TestParser.test(test_in,expect,254))
    
    def test_255_self_in_many_methods(self):
        test_in = """
Class Program{
    Val $susan, agent: Int = 0, 175;
    $Method() {
        a.Method(Self.b.Method(Self.a.Method()));
    }
    main () {
        Foreach (Self.a() In 1 .. Self.a().Value.c.d.e.foo_method) {
            Self.a().Method();
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,255))

    def test_256__statement_mashup(self):
        test_in = """
## Say hi to papa USA ##
Class NorthKorea {
    Var $num_of_nuclear_nuke: Int = 999;
    Val $leader: String = "kim jong un";
    $Scare_little_dick_Southern_chicks(solders, cannons: Int) {
        Self.show_off_at_borders(solders, cannons);
    } 
}

Class SouthKorea{
    main () {
        Foreach (year In 1953 .. now By 1) {
            If (NorthKorea.test_nuke() == True) {
                Self.call_papa_USA();
                Break;
            }
            Elseif (NorthKorea.prepare_to_test_nuke == True) {
                Self.call_papa_USA();
            }
            Else {
                Self.pay_money_for_papa_USA();
                Continue;
            }
            USA.good_kiz = SouthKorea;
            Return USA.good_kiz;
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,256))
    
    def test_257_return_lower_case(self):
        test_in = """
Class Test {
    Test_1(input:String) {
        return Self::$result;
    }
    Test_2(input:String) {
        Return Self.error_1;
    }
    Test_3(input:String) {
        Return Self.error_2;
    }
    Test_4(input:String) {
        Return Self.error_3;
    }
}
"""
        expect = "Error on line 4 col 15: Self"
        self.assertTrue(TestParser.test(test_in,expect,257))

    def test_258_block_in_block(self):
        test_in = """
Class Program {
    main () {
        System.out.println();
        System::$out.println();
        {
            # block 
        }
    }
}
"""
        expect = "Error on line 6 col 8: {"
        self.assertTrue(TestParser.test(test_in,expect,258))
    
    def test_259_method_no_lp_rp(self):
        test_in = """
Class Program {
    foo () {
        System.out.println();
        System::$out.println();
    }
    foo1 {
        System.out.println();
        System::$out.println();
    }
}
"""
        expect = "Error on line 7 col 9: {"
        self.assertTrue(TestParser.test(test_in,expect,259))

    def test_260_self_static(self):
        test_in = """
Class Program {
    main () {
        Self.var = 3;
        Self::$out.println();
    }
}
"""
        expect = "Error on line 5 col 12: ::"
        self.assertTrue(TestParser.test(test_in,expect,260))
    
    def test_261_self_and_null(self):
        test_in = """
Class Program {
    main() {
        Self.a = Null;
        Self.method();
        class::$id = Null;
        class::$method();
        a = Null;
        Self.Self.Self.a = Null;
    }
}
"""
        expect = "Error on line 9 col 13: Self"
        self.assertTrue(TestParser.test(test_in,expect,261))

    def test_262_complex_program_with_all_statement(self): 
        test_in = """
Class Foo : Foo_2 {
    Var a, $a: Array[Array[Array[String, 3],3],3];
    Val a: Array[Array[Array[String, 3],3],3] = Array(Array(Array(Array(Array(Array(Array(Array(Array(Array(Array(3,4,5)))))))))));

    foo_method(a,b,c: String; d,e,f: Float; g,h,i: Array[Array[Array[Boolean, 2], 2], 2]) {
        Var a, b: Array[Array[Array[String, 3],3],3];
        Val a: Array[Array[Array[String, 3],3],3] = Array(Array(Array(Array(Array(Array(Array(Array(Array(Array(Array(3,4,5)))))))))));

        If (a >= Nulll) {
            foo.do_something();
        }
        Elseif (Self.objects) {
            Continue;
        }
        Else {
            Foreach (class.i In class::$a .. class::$b() By class.d()) {
                If (a >= Nulll) {
                    foo.do_something();
                }
                Elseif (Self.objects) {
                    Continue;
                }
                Else {
                    Break;
                }
            }
        }
        Return Self.objects;
    }
    Constructor(a,b,c: String){
        a.do_something();
    }
    Destructor(){}
}
Class Program { 
    main () {}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,262))
    
    def test_263_start_up_test_for_class(self):
        test_in = """
Class Keyboard {
    Var pcb: PCB;
    Var case: Material;
    Typing() {
        Self.send_signal_when_press_a_button();
    }
}

Class Mechanical_keyboard : Keyboard {
    Var switches: String;
    Var led_rgb: Boolean;
    Sound(buttons, case, switches, pcb: Part_of_keyboard) {
        Return Self.sound;
    }
}

Class Program {
    main () {
        Self.sound_test(Mechanical_keyboard);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,263))
    
    def test_264_basic_expression(self):
        test_in = """
Class Program {
    main () {
        a = (1+2-3) * 4 / 5 && False || True;
        a = 1 != 2;
        a = 2 == 2;
        a = 3 <= 4;
        a = 3 < 4;
        a = 4 > 3;
        a = 4 >= 3; 
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,264))
    
    def test_265_new_expression(self):
        test_in = """
Class Program {
    main () {
        a = New foo(index);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,265))

    def test_266_mem_access_expression(self):
        test_in = """
Class Program {
    main () {
        a = class.a;
        a = class.a.a;
        a = class.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a;

        a = class::$a;
        a = class::$a.a;
        a = class::$a.a.a.a.a;

        a = class.method();
        a = class.method().method();
        a = class.method().method().method().method().method();

        a = class.method().a;
        a = class.method().a.method();
        a = class.method().method().a.a.a.method().method();

        a = class::$a;
        a = class::$a.a();
        a = class::$a().a.a.a().a;

        a = (12345).a;
        a = (0).a();
        a = ("foo").a();
        
        a = New foo().a.c.d;
        a = New bar().a.c().d();
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,266))
    
    def test_267_wrong_access_1(self):
        test_in = """
Class Program {
    main () {
        a = b::c;
    }
}
"""
        expect = "Error on line 4 col 15: c"
        self.assertTrue(TestParser.test(test_in,expect,267))
    
    def test_268_wrong_access_2(self):
        test_in = """
Class Program {
    main () {
        a = b::c();
    }
}
"""
        expect = "Error on line 4 col 15: c"
        self.assertTrue(TestParser.test(test_in,expect,268))
    
    def test_269_string_expression(self): # begin here
        test_in = """
Class Program{
    main () {
        Var a : String = "empty string";
        a = "a-c+d" + "abcde";
        a = "a-c+d" - "abcde";
        a = "a-c+d" * "abcde" / "a-c+d" % "abcde";
        a = "a-c+d" +. "abcde";
        a = "a-c+d" != "abcde";
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,269))

    def test_270_triple_string_at_same_time(self):
        test_in = """
Class Program{
    main () {
        a = "a" +. "abcde" +. "defgh";
    }
}
"""
        expect = "Error on line 4 col 27: +."
        self.assertTrue(TestParser.test(test_in,expect,270))
    
    def test_271_triple_string_at_the_same_time_2(self):
        test_in = """
Class Program{
    main () {
        a = "a" ==. "abcde" ==. "defgh";
    }
}
"""
        expect = "Error on line 4 col 28: ==."
        self.assertTrue(TestParser.test(test_in,expect,271))

    def test_272_alot_operator(self):  
        test_in = """
Class Program {
    main () {
        a = 1||2||3||4||5||6;
        a = 1&&2&&3&&4&&5&&6; 
        a = 1+2+3+4+5+6;
        a = 1-2-3-4-5-6;
        a = 1*2*3*4*5*6;
        a = 1/ 2/3/4/5/6;
        a = 1% 2 % 3 %  4 % 5 % 6;
        a = !!!!!!!!1;
        a = --------1;
        a = b[1][1][1][1+2+3][variable];
        a = b[b[b[b[1]]]];
        a = a.b.c.d.e.f;
        a = a.b.c.method().method().a.b.method().method();
        a = a::$b().method().a.method().a.method();
        a = New a(New a(New a()));
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,272))
    
    def test_273_alot_operator_2(self):
        test_in = """
Class Program{
    main () {
        a= New a(New a(New a((a[a[a[a[a[1]]]]][a]).method()+ !!!!----1/2*3%4+5)));
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,273))

    def test_274_missing_var_id(self):
        test_in = """
Class Program {
    main () {
        a = a.a[a];
        a = a[a].a;
    }
}
"""
        expect = "Error on line 5 col 16: ."
        self.assertTrue(TestParser.test(test_in,expect,274))
    
    def test_275_relation_expression(self):
        test_in = """
Class Program{
    main () {
        a = a == 1;
        a = 1 < 2;
        a = 1 <= 2;
        a = a > 3;
        a = a >= 3;
        a = a != 4;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,275))

    def test_276__relation_expression_2(self):
        test_in = """
Class Program{
    main () {
        a = a == 1;
        a = 1 < 2;
        a = 1 <= 2;
        a = a > 3;
        a = a >= 3;
        a = a != 4 == 5;
    }
}
"""
        expect = "Error on line 9 col 19: =="
        self.assertTrue(TestParser.test(test_in,expect,276))
    
    def test_277_logical_expression(self):
        test_in = """
Class Program{
    main () {
        a = a && b;
        a = c || d;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,277))

    def test_278_logical_expression_2(self):
        test_in = """
Class Program {
    method_full(x, y: Int; z: String) {}
    main () {
        a = a && b && b && b;
        a = c || d || d || d;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,278))
    
    def test_279_adding_expression(self):
        test_in = """
Class Program {
    $method_full(x, y: Int; z: String) {}
    main () {
        a = a + b;
        a = a - b;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,279))

    def test_280_adding_expression_2(self):
        test_in = """
Class Program {
    Var $k98, $k99: Int = 98, 99;
    main () {
        a = 1 + 2 - 3 + 4 - 5 + 6 - 7;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,280))
    
    def test_281_multiplying_expression(self):
        test_in = """
Class Program {
    main () {
        a = 2 / 1;
        a = 2 * 1;
        a = 3 % 2;
    }   
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,281))

    def test_multipying_expression_2(self):
        test_in = """
Class Program {
    main () {
        a = 2 / 3 * 4 % 5 % 5 * (4 - 3 / 2);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,282))
    
    
    def test_283_sign_expression(self):
        test_in = """
Class Program {
    main () {
        a = -10;
        a = !10;
        a = -10 - 10;
        a = !10 + 10;
        a = -10 - 10 + 10 --1;
        a = -10 - !10;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,283))
    

    def test_284_sign_expression_hard_core(self):
        test_in = """
Class Program {
    main () {
        a = !!!!!!!!!!!!1;
        a = ------------1;
        a = ------------1 - !!!!!!!!!!!1 + 1;
        a = ------------1 || !!!!!!!!!!!1 && 1;
        a = ------------(2*3+4);
        a = !!!!!!!!!!!!(2*3+4);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,284))
    
    def test_285_index_expression_hard_core(self):
        test_in = """
Class Program {
    main() {
        a = a[1];
        a = a[1][1][1][1][1];
        a = a[a[a[1]]][a[a[a[1]]]];
        a = class::$method(a, b, c)[1][1][1];
        a = class.class.class[1][1][1][a[a[1]]];
        a = a[a.a[1]][a.a.a.a.a[1]];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,285))

    def test_286_super_hard_core_index_expression(self):
        test_in = """
Class the_class {
    Val $int1: Array[Int, 1] = a[1];
    Val $int2: Array[Array[Int, 1], 1] = a[1][2];
    Val $a: Array[Array[Array[Int, 1],1], 1] = a[1][2][3];
    Var $b: Int =  a[1][2][3][4];
    Var $c: Int =  a[a[a[1]]];
                    
    Constructor(a: Int; b: Float) {
        str1 = a[1];
        Val str2: Array[Array[Int, 1], 1] = a[1][2];
        Val a: Array[Array[Array[Int, 1],1], 1] = a[1][2][3];
        c =  a[1][2][3][4];
        d =  a[a[a[1]]];
    }
    Destructor() {}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,286))
    
    def test_287_new_expression_complex(self):
        test_in = """
Class Program {
    main () {
        a = New class();
        a = New class(1,2);
        a = New class().b;
        a = New class()[a][b][c];
        a = (New class()).a.a.a;
        a = (New class())[a][b][c];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,287))
    
    def test_288_new_expression_complex_2(self):
        test_in = """
Class Program {
    main () {
        a = New class(1+2-3*4/5%6&&7||8, a[9][10][11], a.a.a, a.method(), a::$a, a::$method());
        a = New class(New class(New class(1,2,(3).a)));
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,288))
    
    def test_289_left_hand_side(self):
        test_in = """
Class Program{
    main () {
        a::$a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a::$a.a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a[1][1][1] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
        a[a[a[a[1]]]][a[a[a]]] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
        a.a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a - a.a() - class::$a());
        a.a.a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a - a.a() - class::$a());
        a[1] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,289))

    def test_290_no_closing(self):
        test_in = """
Program{
    main () {
        a::$a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a::$a.a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a[1][1][1] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
        a[a[a[a[1]]]][a[a[a]]] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
    }
}
"""
        expect = "Error on line 2 col 0: Program"
        self.assertTrue(TestParser.test(test_in,expect,290))
    
    def test_291_alot_operators(self):
        test_in = """
Class Program{
    main () {
        foo = New foo();
        foo = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo[a] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo[a[a]] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo[a][a][a][a] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo.foo = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo.foo.foo.z = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo::$foo = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo::$foo().foo.z = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(test_in,expect,291))

    def test_292_destructor_not_destructor(self):  
        test_in = """
Class Program {
    Constructor(a,b,c: String){}
    Destructor(){}
    Destructor(a,b,c: String){}
}
"""
        expect = "Error on line 5 col 15: a"
        self.assertTrue(TestParser.test(test_in,expect,292))
    
    def test_293_missing_rp(self):
        test_in = """
Class Program {
    main () {
        class::$a().b.c.d();
    }

"""
        expect = "Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(test_in,expect,293))

    def test_294_contructor_in_destructor(self):
        test_in = """
Class Program {
    Constructor() {
        Return a;
    }
    Constructor(x: Int; y: String; a: Array[Array[Int,1],1]) {
        Break;
    }
    Destructor() {Constructor(a,x:Int){}}
    Destructor() {
        Continue;
    }
}
"""
        expect = "Error on line 9 col 18: Constructor"
        self.assertTrue(TestParser.test(test_in,expect,294))
    
    def test_295_declare_error(self):
        test_in = """
Class Program{
    Val $susan, agent: Int = 0, 175;
    Var bruh, bruh2, a, b, c, d: Float : 1,2,3,4,5,6;
}
"""
        expect = "Error on line 4 col 39: :"
        self.assertTrue(TestParser.test(test_in,expect,295))

    def test_296__member_acess_error(self):
        test_in = """
Class Program{
    main () {
        a = a.a.a;
        a = a.a.a();
        a = a::$a;
        a = a::$a();
        a = Self.a;
        a = Self.Null;
    }
}
"""
        expect = "Error on line 9 col 17: Null"
        self.assertTrue(TestParser.test(test_in,expect,296))
    
    def test_297_missing_operator(self):
        test_in = """
Class Program{
    main () {
        foo = New foo();
        foo = a && a || b * c + d / e - f (z + z.z / c::$z - c::$z());
        foo[a] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo[a[a]] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo[a][a][a][a] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo.foo = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo.foo.foo.z = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo::$foo = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo::$foo().foo.z = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
    }
}
"""
        expect = "Error on line 5 col 42: ("
        self.assertTrue(TestParser.test(test_in,expect,297))

    def test_298_statement_error_1(self):
        test_in = """
Class Program {
    method_full(x, y: Int; z: String) {}
    main () {
        7 = 1;
    }
}
"""
        expect = "Error on line 5 col 10: ="
        self.assertTrue(TestParser.test(test_in,expect,298))
    
    def test_299_assign_statement_error_2(self):
        test_in = """
Class Program {
    main () {
        Self.method_full() = True;
    }
}
"""
        expect = "Error on line 4 col 27: ="
        self.assertTrue(TestParser.test(test_in,expect,299))