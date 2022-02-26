import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_001_simple_class(self):
        input = r"""
            Class Program {}
        """
        expect = r"successful"
        num = 201
        self.assertTrue(TestParser.test(input, expect, num))

    def test_002_multi_simple_class(self):
        input = r"""
            Class Person {}
            Class Student : Person {}
            Class Teacher : Person {}
            Class Program {}
        """
        expect = r"successful"
        num = 202
        self.assertTrue(TestParser.test(input, expect, num))

    def test_003_simple_program(self):
        input = r"""
            Class Program {
                Val $author: String = "Huynh Thanh Dat";
                main() {}
            }
        """
        expect = r"successful"
        num = 203
        self.assertTrue(TestParser.test(input, expect, num))

    def test_004_simple_program_with_class(self):
        input = r"""
            Class Author {
                Var user_name: String;
            }
            Class Program {
                Val author: Author;
                main() {}
            }
        """
        expect = r"successful"
        num = 204
        self.assertTrue(TestParser.test(input, expect, num))

    def test_005_class_keyword_lowercase(self):
        input = r"""
            class Program {}
        """
        expect = r"Error on line 2 col 12: class"
        num = 205
        self.assertTrue(TestParser.test(input, expect, num))

    def test_006_class_with_semi(self):
        input = r"""
            Class Program {};
        """
        expect = r"Error on line 2 col 28: ;"
        num = 206
        self.assertTrue(TestParser.test(input, expect, num))

    def test_007_class_attribute_declaration(self):
        input = r"""
            Class Program {
                Var num_1, num_2, num_3: Int;
                Var x, y, z: Int = 1,2,3;
                Val $a, $b, $c: String = "string 1", "string 2", "string 3";
            }
        """
        expect = r"successful"
        num = 207
        self.assertTrue(TestParser.test(input, expect, num))

    def test_008_class_attribute_declaration(self):
        input = r"""
            Class Program {
                Var x, y, z: Int;
                Var a, b, c, d: Int = 1,2,3; ## Not equal initialization ##
            }
        """
        expect = r"Error on line 4 col 43: ;"
        num = 208
        self.assertTrue(TestParser.test(input, expect, num))

    def test_009_class_attribute_declaration(self):
        input = r"""
            Class Program {
                Var x, y, z: Int;
                Var a, b, c, d: Int = 1,2,3,4,5,6,7,8,9,10; ## Not equal initialization ##
            }
        """
        expect = r"Error on line 4 col 45: ,"
        num = 209
        self.assertTrue(TestParser.test(input, expect, num))

    def test_010_error_token(self):
        input = r"""
            ## Error Token catch in Lexer ##
            ?^
        """
        expect = r"?"
        num = 210
        self.assertTrue(TestParser.test(input, expect, num))

    def test_011_empty_program(self):
        input = r"""
            ## Can program be empty ? ##
        """
        expect = r"Error on line 3 col 8: <EOF>"
        num = 211
        self.assertTrue(TestParser.test(input, expect, num))

    def test_012_method_declaration(self):
        input = r"""
            Class Program {
                Var $x: Int = 1;
                method_1(x: Int; y: String) {}
                main() {}
            }
        """
        expect = r"successful"
        num = 212
        self.assertTrue(TestParser.test(input, expect, num))

    def test_013_static_method_declaration(self):
        input = r"""
            Class Program {
                $method_1() {}
                $method_2(x: Int; y: String) {}
                main() {}
            }
        """
        expect = r"successful"
        num = 213
        self.assertTrue(TestParser.test(input, expect, num))

    def test_014_static_variable_in_method(self):
        input = r"""
            Class Program {
                Var $x: Int = 1;
                main() {
                    Var $a;
                }
            }
        """
        expect = r"Error on line 5 col 24: $a"
        num = 214
        self.assertTrue(TestParser.test(input, expect, num))

    def test_015_variable_declaration(self):
        input = r"""
            Class Program {
                Var $x: Int = 1;
                main() {
                    Var a, b: Int = 1, 2;
                    Var s_1, s_2: String = "string 1", "string 2";
                }
            }
        """
        expect = r"successful"
        num = 215
        self.assertTrue(TestParser.test(input, expect, num))

    def test_016_variable_declaration(self):
        input = r"""
            Class Program {
                Var $x: Int = 1;
                main() {
                    Var a, b, c: Int = 1, 2; ## Not equal initialization ##
                }
            }
        """
        expect = r"Error on line 5 col 43: ;"
        num = 216
        self.assertTrue(TestParser.test(input, expect, num))

    def test_016_variable_declaration(self):
        input = r"""
            Class Program {
                Var $x: Int = 1;
                main() {
                    Var a, b, c: Int = 1, 2, 3, 4, 5, 6, 7; ## Not equal initialization ##
                }
            }
        """
        expect = r"Error on line 5 col 46: ,"
        num = 216
        self.assertTrue(TestParser.test(input, expect, num))

    def test_017_miss_semi_in_declaration(self):
        input = r"""
            Class Program {
                Var $x: Int = 1
                main() {}
            }
        """
        expect = r"Error on line 4 col 16: main"
        num = 217
        self.assertTrue(TestParser.test(input, expect, num))

    def test_018_miss_semi_in_declaration(self):
        input = r"""
            Class Program {
                Var $x: Int = 1;
                main() {
                    Var a: Int
                }
            }
        """
        expect = r"Error on line 6 col 16: }"
        num = 218
        self.assertTrue(TestParser.test(input, expect, num))

    def test_019_array_declaration(self):
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
        expect = r"successful"
        num = 219
        self.assertTrue(TestParser.test(input, expect, num))

    def test_020_array_literal(self):
        input = r"""
            Class Program {
                Var array: Array[Int, 5] = Array(1, 1+2-3*4/5, a.b, Class_name::$a, a.b().c, a.b(), Class_name::$a.a());
            }
        """
        expect = r"successful"
        num = 220
        self.assertTrue(TestParser.test(input, expect, num))

    def test_021_multi_dimensional_array(self):
        input = r"""
            Class Program {
                Var array: Array[Array[Int, 5], 5] = Array(
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5)
                );
            }
        """
        expect = r"successful"
        num = 221
        self.assertTrue(TestParser.test(input, expect, num))

    def test_022_multi_dimensional_array(self):
        input = r"""
            Class Program {
                Var array: Array[Array[Int, 5], 5] = Array(
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5)
                ), ## Fail right here, only 1 array is declared ##
                Array(
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5),
                    Array(1,2,3,4,5)
                ),
            }
        """
        expect = r"Error on line 9 col 17: ,"
        num = 222
        self.assertTrue(TestParser.test(input, expect, num))

    def test_023_array_complex_initialization(self):
        input = r"""
            Class Program {
                Var array: Array[Int, 6] = Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x));  
                Var array: Array[Int, 6] = Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)), Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x));        
            }
        """
        expect = r"Error on line 4 col 99: ,"
        num = 223
        self.assertTrue(TestParser.test(input, expect, num))

    def test_024_array_complex_initialization(self):
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
                Var array_1, array_2, array_3, array_4: Array[Array[Int,6], 6] = Array(
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
        expect = r"Error on line 32 col 21: ;"
        num = 224
        self.assertTrue(TestParser.test(input, expect, num))

    def test_025_three_dimensional_array(self):
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
        expect = r"successful"
        num = 225
        self.assertTrue(TestParser.test(input, expect, num))

    def test_026_array_many_declare(self):
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
                Var array: Array[Array[Array[Array[Int,1],0],1],1];
            }
        """
        expect = r"Error on line 22 col 58: 0"
        num = 226
        self.assertTrue(TestParser.test(input, expect, num))

    def test_027_constructor_destructor(self):
        input = r"""
            Class Program {
                Var $a, b: Int = 1, 2;
                Var $x, y: String;
                constructor() {}
                constructor(x: Int; y: String){}
                destructor() {}
                main() {}
            }
        """
        expect = r"successful"
        num = 227
        self.assertTrue(TestParser.test(input, expect, num))

    def test_028_class_type(self):
        input = r"""
            Class Number {
                Var data: String = "1234"; 
            }
            Class Integer : Number{
                Var data: Number;
            }
            Class Program {
                main() {
                    Var x: Integer;
                }
            }
        """
        expect = r"successful"
        num = 228
        self.assertTrue(TestParser.test(input, expect, num))

    def test_029_simple_expression(self):
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
        expect = r"successful"
        num = 229
        self.assertTrue(TestParser.test(input, expect, num))

    def test_030_member_accesss_expression(self):
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
        expect = r"successful"
        num = 230
        self.assertTrue(TestParser.test(input, expect, num))

    def test_031_incorrect_access_static(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    a = b::variable;
                }
            }
        """
        expect = r"Error on line 5 col 27: variable"
        num = 231
        self.assertTrue(TestParser.test(input, expect, num))

    def test_032_incorrect_access_static_method(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    a = b::method();
                }
            }
        """
        expect = r"Error on line 5 col 27: method"
        num = 232
        self.assertTrue(TestParser.test(input, expect, num))

    def test_033_incorrect_access_instance(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    a = b.$attribute;
                }
            }
        """
        expect = r"Error on line 5 col 26: $attribute"
        num = 233
        self.assertTrue(TestParser.test(input, expect, num))

    def test_034_incorrect_access_instance_method(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    a = b.$method();
                }
            }
        """
        expect = r"Error on line 5 col 26: $method"
        num = 234
        self.assertTrue(TestParser.test(input, expect, num))

    def test_035_string_expression(self):
        input = r"""
            Class Program {
                main() {
                    Var s: String;
                    s = "abc" +. "abc";
                    s = "abc" ==. "abc";

                    ## Fail type but ok in parser ##
                    s = "abc" + "abc";
                    s = "abc" == "abc";
                }
            }
        """
        expect = r"successful"
        num = 235
        self.assertTrue(TestParser.test(input, expect, num))

    def test_036_string_expression_associativity(self):
        input = r"""
            Class Program {
                main() {
                    s = "abc" +. "abc" +. "abc";
                }
            }
        """
        expect = r"Error on line 4 col 39: +."
        num = 236
        self.assertTrue(TestParser.test(input, expect, num))

    def test_037_string_expression_associativity(self):
        input = r"""
            Class Program {
                main() {
                    s = "abc" ==. "abc" ==. "abc" ==. "abc";
                }
            }
        """
        expect = r"Error on line 4 col 40: ==."
        num = 237
        self.assertTrue(TestParser.test(input, expect, num))

    def test_038_operator_associativity(self):
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
        expect = r"successful"
        num = 238
        self.assertTrue(TestParser.test(input, expect, num))

    def test_039_operator_precedence(self):
        input = r"""
            Class Program {
                main() {
                    a = New class_name(New class_name(a[i][j][z][a.b.method().method() + !!!!----1+2-3*4/5%6||7&&8], a[1+2-3*4/5%6||7&&8], "string 1" +. "string 2", "string 1" ==. "string 2", New class(1+2-3*4/5%6||7&&8)));
                }
            }
        """
        expect = r"successful"
        num = 239
        self.assertTrue(TestParser.test(input, expect, num))

    def test_040_operator_precedence_special_case(self):
        input = r"""
            Class Program {
                main() {
                    a = a.b[1];
                    a = a[1].b;
                }
            }
        """
        expect = r"Error on line 5 col 28: ."
        num = 240
        self.assertTrue(TestParser.test(input, expect, num))

    def test_041_relation_expression(self):
        input = r"""
            Class Program {
                main() {
                    a = 1==2;
                    a = 1 != 2;
                    a = 1 > 2;
                    a = 1 >= 2;
                    a = 1 < 2;
                    a = 1 <= 2;
                }
            }
        """
        expect = r"successful"
        num = 241
        self.assertTrue(TestParser.test(input, expect, num))

    def test_042_relation_expression_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = 1==2 == 3;
                }
            }
        """
        expect = r"Error on line 4 col 29: =="
        num = 242
        self.assertTrue(TestParser.test(input, expect, num))

    def test_043_logical_expression(self):
        input = r"""
            Class Program {
                main() {
                    a = 1 && 2;
                    a = 1 || 2;
                }
            }
        """
        expect = r"successful"
        num = 243
        self.assertTrue(TestParser.test(input, expect, num))

    def test_044_logical_expression_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = 1 && 2 && 3 && 4 && 5;
                    a = 1 || 2 || 3 || 4 || 5;
                }
            }
        """
        expect = r"successful"
        num = 244
        self.assertTrue(TestParser.test(input, expect, num))

    def test_045_add_expresion(self):
        input = r"""
            Class Program {
                main() {
                    a = 1 + 2;
                    a = 1 - 2;
                }
            }
        """
        expect = r"successful"
        num = 245
        self.assertTrue(TestParser.test(input, expect, num))

    def test_046_add_expresion_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = 1 + 2 + 3 + 4 + 5 - 6 - 7 - 8;
                    a = 1 - 2 - 3 - 4 - 5 + 6 + 7 + 8;
                }
            }
        """
        expect = r"successful"
        num = 246
        self.assertTrue(TestParser.test(input, expect, num))

    def test_047_mul_expresion(self):
        input = r"""
            Class Program {
                main() {
                    a = 1 * 2;
                    a = 1 / 2;
                    a = 1 % 2;
                }
            }
        """
        expect = r"successful"
        num = 247
        self.assertTrue(TestParser.test(input, expect, num))

    def test_048_mul_expresion_associativity(self):
        input = r"""
            Class Program {
                main() {
                    a = 1 * 2 * 3 * 4 / 5 / 6 / 7 % 8 % 9 % 10;
                    a = 1 / 2 / 3 / 4 * 5 * 6 * 7 % 8 % 9 % 10;
                    a = 1 % 2 % 4 % 5 / 5 / 6 / 7 * 8 * 9 * 10;
                }
            }
        """
        expect = r"successful"
        num = 248
        self.assertTrue(TestParser.test(input, expect, num))

    def test_049_sign_not_expresion(self):
        input = r"""
            Class Program {
                main() {
                    a = -1;
                    a = !1;
                    a = -1 - 1;
                    a = !1 - 1;
                    a = -1 - 1 - 1 --1;
                    a = -1 + !1;
                }
            }
        """
        expect = r"successful"
        num = 249
        self.assertTrue(TestParser.test(input, expect, num))

    def test_050_sign_not_expresion_associativity(self):
        input = r"""
            Class Program {
                main() {
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
        expect = r"successful"
        num = 250
        self.assertTrue(TestParser.test(input, expect, num))

    def test_051_index_expresion(self):
        input = r"""
            Class Some_class {
                    Val str1: Array[Int, 1] = a[1];
                    Val str2: Array[Array[Int, 1], 1] = a[1][2];
                    Val a: Array[Array[Array[Int, 1],1], 1] = a[1][2][3];
                    Var c: Int =  a[1][2][3][4];
                    Var c: Int =  a[arr[arr[1]]];
                    Var c: Int =  a[arr[1]];
                    Val $str1: Array[Int, 1] = a[1];
                    Val $str2: Array[Array[Int, 1], 1] = a[1][2];
                    Val $a: Array[Array[Array[Int, 1],1], 1] = a[1][2][3];
                    Var $c: Int =  a[1][2][3][4];
                    Var $c: Int =  a[arr[arr[1]]];
                    Var $c: Int =  a[arr[1]];
                    
                    Constructor(int: Int; string: String) {
                        Val str1: Array[Int, 1] = a[1];
                        Val str2: Array[Array[Int, 1], 1] = a[1][2];
                        Val a: Array[Array[Array[Int, 1],1], 1] = a[1][2][3];
                        Var c: Int =  a[1][2][3][4];
                        Var c: Int =  a[arr[arr[1]]];
                        Var c: Int =  a[arr[1]];
                    }
                    Destructor() {}
            }
            Class Program {
                main() {
                    Val str1: Array[Int, 1] = a[1];
                    Val str2: Array[Array[Int, 1], 1] = a[1][2];
                    Val a: Array[Array[Array[Int, 1],1], 1] = a[1][2][3];
                    Var c: Int =  a[1][2][3][4];
                    Var c: Int =  a[arr[arr[1]]];
                    Var c: Int =  a[arr[1]];

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
        expect = r"successful"
        num = 251
        self.assertTrue(TestParser.test(input, expect, num))

    def test_052_new_expression(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    a = New Some_class();
                    a = New Some_class(1,2);
                    a = New Some_class(1+2-3*4/5%6||7&&8, a[1][1][1], a.a.a, a.method(), a::$a, a::$method());
                    a = New Some_class(New Some_class(New Some_class(1,2,3)));
                    a = New Some_class().fucking_attribute;
                    a = New Some_class()[1][2][3];
                    a = (New Some_class()).a.a.a;
                    a = (New Some_class())[1][2][3];
                }
            }
        """
        expect = r"successful"
        num = 252
        self.assertTrue(TestParser.test(input, expect, num))

    def test_053_array_size_0(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Var a: Array[Int, 0];
                }
            }
        """
        expect = r"Error on line 9 col 38: 0"
        num = 253
        self.assertTrue(TestParser.test(input, expect, num))

    def test_054_empty_array(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Var a: Array[Int, 1] = Array();
                    b = Array();
                }
            }
        """
        expect = r"successful"
        num = 254
        self.assertTrue(TestParser.test(input, expect, num))

    def test_055_assign_statement(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Var a: Array[Int, 1000] = Array(1,1,1,1,1);
                    a = Array(1,1,1,1,1);
                    a = 1;
                    a = 012345;
                    a = 0b1001;
                    a = 0xFFFF;
                    a = 0xFFFF + 0b1001 - 012345 * 1;
                    Class_name::$a = 1;
                    Class_name::$a = 012345;
                    Class_name::$a = 0b1001;
                    Class_name::$a = 0xFFFF;
                    Class_name::$a = 0xFFFF + 0b1001 - 012345 * 1;
                    
                    some_var = 1 + 2 +3 || 5 && 6;
                    some_var = True || (1 || 01 || 0b100010 || 0xFFFFF11);
                    some_var = True && (1 && 01 && 0b100010 && 0xFFFFF11);
                    
                    Class_name::$some_var = 1 + 2 +3 || 5 && 6;
                    Class_name::$some_var = True || (1 || 01 || 0b100010 || 0xFFFFF11);
                    Class_name::$some_var = True && (1 && 01 && 0b100010 && 0xFFFFF11);

                    arr[1] = arr[arr[arr[1]]];
                    arr[1][1][1] = arr[arr[arr[1]]][1][1][1];
                    arr[1][1][1] = New Some_class().a[1][2][3];
                    arr[arr[arr[arr[1]]]] = a.b + New Some_class().a()[1][2][3];    

                    Class_name::$arr[1] = arr[arr[arr[1]]];
                    Class_name::$arr[1][1][1] = arr[arr[arr[1]]][1][1][1];
                    Class_name::$arr[1][1][1] = New Some_class().a[1][2][3];
                    Class_name::$arr[arr[arr[arr[1]]]] = a.b + New Some_class().a()[1][2][3]; 

                    a.b.c = 1;
                    a::$b = 1; 
                    
                    a[1] = 1;
                    a[a[1]][a[a[1]]][a[a[1]]] = 1;
                    Class_name::$a[Class_name::$a[1]][Class_name::$a[Class_name::$a[1]]][Class_name::$a[Class_name::$a[1]]] = 1;
                    
                    Self.a = 1;
                    Class_name::$a = 1;
                    Self.a.a.a.a.a = 1;
                    Class_name::$a.a.a.a.a.a = 1;
                }
            }
        """
        expect = r"successful"
        num = 255
        self.assertTrue(TestParser.test(input, expect, num))

    def test_056_if_statement(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    If (1>2) {
                        Var a,b,c: Int = 1,2,3;
                        If (a+b+c) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                        Elseif(a+b+c == 100) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        } 
                        Elseif (1>2) {}
                        Elseif (1>2) {}
                        Else {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                    }
                    Elseif(10>2) {
                        Var x,y,z: String = "abc", "abc", "abc";
                        If ("abc" ==. x) {
                            x = "xyz";
                        }
                        Elseif (y +. "abc") {
                            y = y +. "xyz";
                        }
                        Elseif (1>2) {
                            a = 1;
                            b = a + b + c;
                            c = 1;}
                        Elseif (1||2) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                        Elseif (1&&2) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                        Elseif (!1) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                        Else {
                            z = z ==. "xyz";
                        }
                    }
                    Elseif (1>2) {}
                    Elseif (1>2) {}
                    Elseif (1>2) {}
                    Elseif (1>2) {}
                    Else {
                        a = 1;
                    }
                }
            }
        """
        expect = r"successful"
        num = 256
        self.assertTrue(TestParser.test(input, expect, num))

    def test_057_if_statement_fail(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                   If (1 > 2)
                   Elseif (1>2) {}
                   Else {}
                }
            }
        """
        expect = r"Error on line 10 col 19: Elseif"
        num = 257
        self.assertTrue(TestParser.test(input, expect, num))

    def test_058_if_statement_else_with_lp_rp(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                   If (1 > 2) {}
                   Elseif (1>2) {}
                   Elseif (1||2) {}
                   Elseif (1&&2) {}
                   Elseif (!1) {}
                   Else() {}
                }
            }
        """
        expect = r"Error on line 14 col 23: ("
        num = 258
        self.assertTrue(TestParser.test(input, expect, num))

    def test_059_if_statement_no_condition(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                   If () {}
                   Elseif () {}
                   Else {}
                }
            }
        """
        expect = r"Error on line 9 col 23: )"
        num = 259
        self.assertTrue(TestParser.test(input, expect, num))

    def test_060_if_statement_miss_part(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {
                        If (a || b || c) {
                        a = 1;
                        b = a + b + c;
                        c = 1;
                        }

                        If (a || b || c) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                        Elseif (a && b && c) {
                            If (a || b || c) {
                                a = 1;
                                b = a + b + c;
                                c = 1;
                            }
                        }

                        If (a || b || c) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                        Else {
                            If (True) {
                                a = 1;
                                b = a + b + c;
                                c = 1;
                            }
                            If (False) {
                                a = 1;
                                b = a + b + c;
                                c = 1;
                            }
                        }
                    }
            }
            Class Program {
                main() {
                    If (a || b || c) {
                        a = 1;
                        b = a + b + c;
                        c = 1;
                    }

                    If (a || b || c) {
                        a = 1;
                        b = a + b + c;
                        c = 1;
                    }
                    Elseif (a && b && c) {
                        If (a || b || c) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                    }

                    If (a || b || c) {
                        a = 1;
                        b = a + b + c;
                        c = 1;
                    }
                    Else {
                        If (True) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                        If (False) {
                            a = 1;
                            b = a + b + c;
                            c = 1;
                        }
                    }


                }
            }
        """
        expect = r"successful"
        num = 260
        self.assertTrue(TestParser.test(input, expect, num))

    def test_061_if_statement_incorrect_order(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    If (a>b){}
                    Else{}
                    Elseif(b>c){}


                }
            }
        """
        expect = r"Error on line 11 col 20: Elseif"
        num = 261
        self.assertTrue(TestParser.test(input, expect, num))

    def test_062_foreach_statement(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Foreach(i In 1 .. 100 By 1) {
                        If (True || False) {
                            Continue;
                        }
                        Elseif (True && False) {
                            Break;
                        }
                        Return False;
                    }
                    Var x: Int = 1;
                    Foreach(i In 1 .. 100 By 1) {
                        Foreach(j In 1 .. 100 By 1) {
                            Foreach(k In 1 .. 100 By 1) {
                                x = x + i + j + k;
                            }
                        }
                    }

                }
            }
        """
        expect = r"successful"
        num = 262
        self.assertTrue(TestParser.test(input, expect, num))

    def test_063_foreach_statement_reverse_and_miss_by(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Foreach(i In 100 .. 1 By 1) {
                        If (True || False) {
                            Continue;
                        }
                        Elseif (True && False) {
                            Break;
                        }
                        Return False;
                    }
                    Var x: Int = 1;
                    Foreach(i In 0 .. 10000 By 100) {
                        Foreach(j In 10000 .. -10000) {
                            Foreach(k In -1 .. -100 By -1000) {
                                x = x + i + j + k;
                            }
                        }
                    }

                    Foreach(i In 0 .. 10000 By 1+2+3+4) {
                        Foreach(j In 10000 .. i+i-i*i/i) {
                            Foreach(k In -1 .. -100 By i+j-i*j/(i||j&&i)) {
                                x = x + i + j + k;
                            }
                        }
                    }

                }
            }
        """
        expect = r"successful"
        num = 263
        self.assertTrue(TestParser.test(input, expect, num))

    def test_064_foreach_statement_scalar_is_static(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Foreach(Class_name::$i In 1 .. 100 By 1) {}

                }
            }
        """
        expect = r"successful"
        num = 264
        self.assertTrue(TestParser.test(input, expect, num))

    def test_065_break_return_continue(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Foreach (i In 100+a+b/c .. 100*a||b&&c By a[a[i]][j]) {
                        If (True || False) {
                            Return True;
                        }
                        Elseif (True > False) {
                            Return False;
                        }
                        Elseif (True == False) {
                            Break;
                        }
                        Elseif (True != False) {
                            Continue;
                        }
                        Else {
                            Return New Some_class(100+a+b/c%100*a||b&&c) + a[a[i]][j];
                        }

                    }
                    Return;
                }
            }
        """
        expect = r"successful"
        num = 265
        self.assertTrue(TestParser.test(input, expect, num))

    def test_066_break_return_continue(self):
        input = r"""
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Foreach (i In 100+a+b/c .. 100*a||b&&c By a[a[i]][j]) {
                        If (True || False) {
                            Continue a+b+c;
                        }

                    }
                    Return;
                }
            }
        """
        expect = r"Error on line 11 col 37: a"
        num = 266
        self.assertTrue(TestParser.test(input, expect, num))

    def test_067_method_invocation_statement(self):
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
                    Constructor(int: Int; string: String) {}
                    Constructor() {}
                    Destructor() {}
            }
            Class Program {
                main() {
                    Var some_class: Some_class = New Some_class(1, "abc");
                    Some_class::$Method(1+2-3*4/5%6);
                    some_class.method(1+2+3);
                    some_class.method().method().method();
                    some_class.a.a.a.a.method();
                    Some_class::$a.a.a.a.method();
                    Some_class::$method().a.a.a.method();
                    Foreach (i In Some_class::$Method(1+2-3*4/5%6) .. some_class.method(1+2+3) By 1) {
                        Self.print(i);
                        If (i > 1) {
                            Self.print(i);
                        }
                        Elseif (i < -1) {
                            Self.add_100(i);
                        }
                        Else {
                            Self.sub_100(i);
                        }
                    }
                }
            }
        """
        expect = r"successful"
        num = 267
        self.assertTrue(TestParser.test(input, expect, num))

    def test_068_self_method(self):
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
        expect = r"successful"
        num = 268
        self.assertTrue(TestParser.test(input, expect, num))

    def test_069_mix_statement(self):
        input = r"""
            Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
                $getNumOfShape() {
                    Return Shape::$numOfShape;
                }
                get_length() {
                    Return Self.legnth;
                }
                get_width() {
                    Return width;
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
        expect = r"successful"
        num = 269
        self.assertTrue(TestParser.test(input, expect, num))

    def test_070_lower_return(self):
        input = r"""
            Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
                $getNumOfShape() {
                    return $numOfShape;
                }
                get_length() {
                    Return Self.legnth;
                }
                get_width() {
                    Return width;
                }
            }
            Class Rectangle: Shape {
                getArea() {
                    Return Self.length * self.width;
                }
            }
            Class Program {
                main() {
                    Out.printInt(Shape::$numOfShape);
                    OutStream::$printInt(shape.numOfShape);

                }
            }

        """
        expect = r"Error on line 7 col 27: $numOfShape"
        num = 270
        self.assertTrue(TestParser.test(input, expect, num))

    def test_071_complex_program(self):
        input = r"""
            Class Shape {
                Var color: String;
                area() {}
                to_string() {}
                Constructor(color: String)
                {
                    Console.log("Shape constructor called");
                    Self.color = color;
                }
                $Method(color: String)
                {
                    Console.log("Shape constructor called");
                    Self.color = color;
                }
                Destructor() {
                    Console.log("Destroy shape");
                }
                get_color() { Return color; }
            }
            Class Circle : Shape {
                Var radius: Float;
                Constructor(color: String; radius: Float)
                {
                    Shape::$Method(color);
                    Console.log("Circle constructor called");
                    Self.radius = radius;
                }
  
                area()
                {
                    Return Math.PI * Math.pow(radius, 2);
                }
  
                to_string()
                {
                    Return "Circle color is " + Shape::$getColor() +. "and area is : " + Shape::$area();
                }
            }
            Class Program {
            main(args: Array[String, 100])
            {
                Var circle: Circle;
                Var string: String;
                circle = New Circle("Red", 2.2);
                string = circle.to_string();
                console.log(circle.get_color());
                Var i: Int;
                Foreach(i In 1 .. 100 By 1) {
                    Var circle: Circle;
                    If (i % 3 == 0) {
                        circle = New Circle("Blue", 10.10);
                        console.log(circle.area());
                    }
                    Elseif (i % 3 == 1) {
                        Break;
                    }
                    Else {
                        Continue;
                    }
                }
                i= -123456+123456 ;
                i= -123_456+123_456;
                i= -123456-123456 ;
                i= -123_456-123_456;
                i= 123456*123456 ;
                i= 123_456*123_456;
                i= 123456/123456 ;
                i= 123_456/123_456;
                i= 123456%123456 ;
                i= 123_456%123_456;
                i= 123456!=123456 ;
                i= 123_456!=123_456;
                i= 123456==123456 ;
                i= 123_456==123_456;
                i= 123456>123456 ;
                i= 123_456>=123_456;
                i= 123456<123456 ;
                i= 123_456<=123_456;
            }
        }            
        """
        expect = r"successful"
        num = 271
        self.assertTrue(TestParser.test(input, expect, num))

    def test_072_miss_scope(self):
        input = r"""
            Class Program {
                $Method() {
                    Console.log(1);
                    Console::$log(1);
                }
                Var x: Int = 1;

        """
        expect = r"Error on line 9 col 8: <EOF>"
        num = 272
        self.assertTrue(TestParser.test(input, expect, num))

    def test_073_program_end_at_EOF(self):
        input = r"""
            Class Program {
                $Method() {
                    Console.log(1);
                    Console::$log(1);
                }
                Var x: Int = 1;
            }
            Something write here
        """
        expect = r"Error on line 9 col 12: Something"
        num = 273
        self.assertTrue(TestParser.test(input, expect, num))

    def test_074_program_end_at_EOF(self):
        input = r"""
            Class Program {
                $Method() {
                    Console.log(1);
                    Console::$log(1);
                }
                Var x: Int = 1;
            }
            Something write here
        """
        expect = r"Error on line 9 col 12: Something"
        num = 274
        self.assertTrue(TestParser.test(input, expect, num))

    def test_075_block_statement_in_block_statement(self):
        input = """
            Class Program {
                $Method() {
                    Console.log(1);
                    Console::$log(1);
                    {
                        ## Another block in block ## 
                        {
                            ## Another block in block ## 
                        }
                    }
                }
                Var x: Int = 1;
            }
        """
        expect = r"""successful"""
        num = 275
        self.assertTrue(TestParser.test(input, expect, num))

    def test_076_method_miss_lp_rp(self):
        input = """
            Class Program {
                $Method() {
                    Console.log(1);
                    Console::$log(1);
                }
                Var x: Int = 1;
                main {
                    Console.log(1);
                }
            }
        """
        expect = r"""Error on line 8 col 21: {"""
        num = 276
        self.assertTrue(TestParser.test(input, expect, num))

    def test_077_direct_statement_in_class(self):
        input = """
            Class Some_class {         
                    Constructor(int: Int; string: String) {}
                    Constructor() {
                        Self.method(00);
                        a.method(0x0, 0X0);
                        b::$method(0b0, 0B0);
                        Return 0 + 0x0 + 0X0 + 00 + 0b0 + 0B0;
                    }
                    Destructor() {
                        Return;
                    }
            }
            Class Program {
                main() {
                    Foreach (i In 100+a+b/c .. 100*a||b&&c By a[a[i]][j]) {
                        If (True || False) {
                            Continue;
                        }
                        If (True && False) {
                            Break;
                        }
                        Foreach (Class_name::$j In 1 .. 100) {
                            Return;
                        }
                    }
                    a = 1;
                    Class_name::$a = 1;
                    a[1] = 1;
                    a[a[1]][a[a[1]]][a[a[1]]] = 1;
                    Self.a = 1;
                    Class_name::$a = 1;
                    Class_name::$a.a.a.a = 1;
                    Return;
                }
            }
            a = 1;
        """
        expect = r"""Error on line 37 col 12: a"""
        num = 277
        self.assertTrue(TestParser.test(input, expect, num))

    def test_078_self_static_access(self):
        input = """
            Class Program {
                $Method() {
                    Console.log(1);
                    Console::$log(1);
                }
                Var x: Int = 1;
                main() {
                    Self.variable = 1;
                    variable = 1;
                    Self::$variable = 1;
                }
            }
        """
        expect = r"""Error on line 11 col 24: ::"""
        num = 278
        self.assertTrue(TestParser.test(input, expect, num))

    def test_079_self_access_and_null_literal(self):
        input = """
            Class Program {
                $Method() {
                    Console.log(1);
                    Console::$log(1);
                }
                Var x: Int = 1;
                main() {
                    Self.variable = Null;
                    Self.method();
                    Program::$static = Null;
                    Program::$method();
                    variable = Null;
                    Class_name::$static = Null;
                    ## Sequence of Self is illgegal ##
                    Self.Self.Self.a = Null;
                }
            }
        """
        expect = r"""Error on line 16 col 25: Self"""
        num = 279
        self.assertTrue(TestParser.test(input, expect, num))

    def test_080_declaration_of_attribute_variable_method_array(self):
        input = """
            Class Some_class : Object {
                Val a, $a: Array[Array[Array[Int, 1], 1], 1];
                Var a: Array[Int, 1] = Array(1,2,3,4);
                Method(a,b,c: Int; x,y,z: String; m,n,t: Array[Boolean, 1]; var_1, var_2: Array[Array[Float, 1], 1]) {
                    Var a: Array[Array[Array[Int, 1], 1], 1];
                    Var a: Array[Int, 1] = Array(1,2,3,4);
                    If (a != Null) {
                        Return a;
                    }
                    Elseif (Self.a == Null) {
                        Return;
                    }
                    Else {
                        Foreach (Class_name::$i In Class_name::$a .. a By Class_name::$a) {
                            If (Class_name::$a + Class_name::$i == Null) {
                                Return Array(1,2,3,4);
                            }
                            Else {
                                Return Array(Array(Array(1,2,3,4)));
                            }
                        } 
                    }
                    Break;
                    Continue;
                    Return;
                }
                Constructor() {

                }
            }
            Class Program : Object {
                main() {
                    Some_class::$Method(a,b,Array(1,2,3,4));
                    object.Method(Array(Array(1,2,4,5)));
                    Some_class::$var = Array(Array(1,2,3,4));
                    object.var = Array(Array(1,2,3,4));
                    
                    Var a,b,c: Int = 1,2,3;
                    Var a,b,c: Int = 1,2,3,4; ## Not equal declaration ##
                    Return;    
                }
            }
        """
        expect = r"""Error on line 40 col 42: ,"""
        num = 280
        self.assertTrue(TestParser.test(input, expect, num))

    def test_081_multi_demensional_array(self):
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
        expect = r"""successful"""
        num = 281
        self.assertTrue(TestParser.test(input, expect, num))

    def test_082_method_inovation_statement(self):
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
        expect = r"successful"
        num = 282
        self.assertTrue(TestParser.test(input, expect, num))

    def test_083_method_inovation_statement_incorrect(self):
        input = r"""
            Class Program {
                main() {
                    Class_name::$a();
                    Self.a();
                    a.b;
                }
            }
        """
        expect = r"Error on line 6 col 23: ;"
        num = 283
        self.assertTrue(TestParser.test(input, expect, num))

    def test_084_method_inovation_statement_incorrect(self):
        input = r"""
            Class Program {
                main() {
                    Self.a.a.a.a.a.a();
                    Self.a().a().a().a();
                    Class_name::$a.a.a.a.a();
                    Class_name::$a().a.a.a.a();

                    Class_name::$a;
                }
            }
        """
        expect = r"Error on line 9 col 34: ;"
        num = 284
        self.assertTrue(TestParser.test(input, expect, num))

    def test_085_index_and_access_expression(self):
        input = r"""
            Class Program {
                main() {
                    a = a.b[1];
                    a = a.a.a.a.a.a[1];
                    a = Self.a[1];
                    a = Self.a.a.a.a.a[1];
                    a = Class_name::$a[1];
                    a = Class_name::$a.a.a.a[1];

                    a = a[1].b;
                }
            }
        """
        expect = r"Error on line 11 col 28: ."
        num = 285
        self.assertTrue(TestParser.test(input, expect, num))

    def test_086_no_check_type_in_expression(self):
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
        expect = r"successful"
        num = 286
        self.assertTrue(TestParser.test(input, expect, num))

    def test_087_static_is_parameter(self):
        input = r"""
            Class Program {
                main($x: Int) {}
            }
        """
        expect = r"Error on line 3 col 21: $x"
        num = 287
        self.assertTrue(TestParser.test(input, expect, num))

    def test_088_invalid_method_inovation_statement(self):
        input = r"""
            Class Program {
                main() {
                    a.a();
                    a::$a();

                    a.$a();
                }
            }
        """
        expect = r"Error on line 7 col 22: $a"
        num = 288
        self.assertTrue(TestParser.test(input, expect, num))

    def test_089_invalid_method_inovation_statement(self):
        input = r"""
            Class Program {
                main() {
                    a.a();
                    a::$a();

                    a::a();
                }
            }
        """
        expect = r"Error on line 7 col 23: a"
        num = 289
        self.assertTrue(TestParser.test(input, expect, num))

    def test_090_member_access_invalid(self):
        input = r"""
            Class Program {
                main() {
                    a = Null.a;
                    a = Null.null.a;
                    a = Null.Null.a;
                }
            }
        """
        expect = r"Error on line 6 col 29: Null"
        num = 290
        self.assertTrue(TestParser.test(input, expect, num))

    def test_091_left_hand_size_form(self):
        input = r"""
            Class Program {
                main() {
                    a = New X();
                    a = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a - a.a() - Class_name::$a());
                    a[1] = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a- a.a() - Class_name::$a());
                    a[1][1][1] = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a- a.a() - Class_name::$a());
                    a[a[a[a[1]]]][a[a[a]]] = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a- a.a() - Class_name::$a());
                    a.a = "String" || "String" && "String" * 0 / 0x0 % (a  + a.a + Class_name::$a- a.a() - Class_name::$a());
                    a.a.a = "String" || "String" && "String" * 0 / 0x0 % (a  + a.a + Class_name::$a- a.a() - Class_name::$a());
                    A::$a = "String" || "String" && "String" * 0 / 0x0 % (a  + a.a + Class_name::$a- a.a() - Class_name::$a());
                    A::$a.a = "String" || "String" && "String" * 0 / 0x0 % (a  + a.a + Class_name::$a- a.a() - Class_name::$a());
                }
            }
        """
        expect = r"successful"
        num = 291
        self.assertTrue(TestParser.test(input, expect, num))

    def test_092_destructor_with_param(self):
        input = """
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
                Destructor(x: Int) {
                    Return x;
                }
            }
        """
        expect = """Error on line 12 col 27: x"""
        num = 292
        self.assertTrue(TestParser.test(input, expect, num))

    def test_093_multi_destructor_constructor_without_return(self):
        # Not valid but ok in parser
        input = """
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
        expect = """successful"""
        num = 293
        self.assertTrue(TestParser.test(input, expect, num))

    def test_094_miss_scope_after_method_inovation(self):
        input = """
            Class Program {
                main() {
                    a.b.c();
                    a.b().c();
                    
                    Self.a();
                    Self.a.a();
                    
                    Class_name::$a();
                    Class_name::$a.a();
                    Class_name::$a().a();
                    
                    a.b();
                }
            
        """
        expect = """Error on line 17 col 8: <EOF>"""
        num = 294
        self.assertTrue(TestParser.test(input, expect, num))

    def test_095_member_access_invalid(self):
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
                    a = Self.Null;
                }
            }
        """
        expect = r"Error on line 11 col 29: Null"
        num = 295
        self.assertTrue(TestParser.test(input, expect, num))

    def test_096_declaration_invalid(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int = 1;
                    Var a: Int : 1;
                }
            }
        """
        expect = r"Error on line 5 col 31: :"
        num = 296
        self.assertTrue(TestParser.test(input, expect, num))

    def test_097_declaration_invalid(self):
        # Ít hơn số biến trả về dấu ;
        input = r"""
            Class Program {
                Var a,b,$c: Int = 1,2,3; ## Equal ##
                Val a,b,$c: Int = 1,2,3; ## Equal ##
                main() {
                    Var a,b,c: Int = 1,2,3; ## Equal ##
                    Val a,b,c: Int = 1,2,3; ## Equal ##
                    Var a,b,c,d,e,f: Int = 1,2; ## Less than variable ##
                }
            }
        """
        expect = r"Error on line 8 col 46: ;"
        num = 297
        self.assertTrue(TestParser.test(input, expect, num))

    def test_098_declaration_invalid(self):
        # Nhiều hơn số biến trả về dấu ,
        input = r"""
            Class Program {
                Var a,b,$c: Int = 1,2,3; ## Equal ##
                Val a,b,$c: Int = 1,2,3; ## Equal ##
                main() {
                    Var a,b,c: Int = 1,2,3; ## Equal ##
                    Val a,b,c: Int = 1,2,3; ## Equal ##
                    Var a,b,c: Int = 1,2,4,5,6,7,8,9; ## Greater than variable ##
                }
            }
        """
        expect = r"Error on line 8 col 42: ,"
        num = 298
        self.assertTrue(TestParser.test(input, expect, num))

    def test_099_scalar_is_funcall(self):
        input = r"""
            Class Program {
                main() {
                    Self.method() = 1;
                }
            }
        """
        expect = r"Error on line 4 col 34: ="
        num = 299
        self.assertTrue(TestParser.test(input, expect, num))

    def test_100_scalar_is_operand(self):
        input = r"""
            Class Program {
                main() {
                    1 = 1;
                }
            }
        """
        expect = r"Error on line 4 col 22: ="
        num = 200
        self.assertTrue(TestParser.test(input, expect, num))
