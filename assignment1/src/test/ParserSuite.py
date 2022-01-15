import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_001_simple_class(self):
        input = r"""
            Class Program {}
        """
        expect = r"successful"
        num = 201;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_002_multi_simple_class(self):
        input = r"""
            Class Person {}
            Class Student : Person {}
            Class Teacher : Person {}
            Class Program {}
        """
        expect = r"successful"
        num = 202;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_003_simple_program(self):
        input = r"""
            Class Program {
                Val $author: String = "Huynh Thanh Dat";
                main() {}
            }
        """
        expect = r"successful"
        num = 203;
        self.assertTrue(TestParser.test(input,expect,num))
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
        num = 204;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_005_class_keyword_lowercase(self):
        input = r"""
            class Program {}
        """
        expect = r"Error on line 2 col 12: class"
        num = 205;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_006_class_with_semi(self):
        input = r"""
            Class Program {};
        """
        expect = r"Error on line 2 col 28: ;"
        num = 206;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_007_class_attribute_declaration(self):
        input = r"""
            Class Program {
                Var num_1, num_2, num_3: Int;
                Var x, y, z: Int = 1,2,3;
                Val $a, $b, $c: String = "string 1", "string 2", "string 3";
            }
        """
        expect = r"successful"
        num = 207;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_008_class_attribute_declaration(self):
        input = r"""
            Class Program {
                Var x, y, z: Int;
                Var a, b, c, d: Int = 1,2,3; ## Not equal initialization ##
            }
        """
        expect = r"Error on line 4 col 43: ;"
        num = 208;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_009_class_attribute_declaration(self):
        input = r"""
            Class Program {
                Var x, y, z: Int;
                Var a, b, c, d: Int = 1,2,3,4,5,6,7,8,9,10; ## Not equal initialization ##
            }
        """
        expect = r"Error on line 4 col 45: ,"
        num = 209;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_010_error_token(self):
        input = r"""
            ## Error Token catch in Lexer ##
            ?^
        """
        expect = r"?"
        num = 210;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_011_empty_program(self):
        input = r"""
            ## Can program be empty ? ##
        """
        expect = r"successful"
        num = 211;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_012_method_declaration(self):
        input = r"""
            Class Program {
                Var $x: Int = 1;
                method_1(x: Int; y: String) {}
                main() {}
            }
        """
        expect = r"successful"
        num = 212;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_013_static_method_declaration(self):
        input = r"""
            Class Program {
                $method_1() {}
                $method_2(x: Int; y: String) {}
                main() {}
            }
        """
        expect = r"successful"
        num = 213;
        self.assertTrue(TestParser.test(input,expect,num))
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
        num = 214;
        self.assertTrue(TestParser.test(input,expect,num))
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
        num = 215;
        self.assertTrue(TestParser.test(input,expect,num))
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
        num = 216;
        self.assertTrue(TestParser.test(input,expect,num))
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
        num = 216;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_017_miss_semi_in_declaration(self):
        input = r"""
            Class Program {
                Var $x: Int = 1
                main() {}
            }
        """
        expect = r"Error on line 4 col 16: main"
        num = 217;
        self.assertTrue(TestParser.test(input,expect,num))
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
        num = 218;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_019_array_declaration(self):
        input = r"""
            Class Program {
                Var array: Array[Int, 5];
            }
        """
        expect = r"successful"
        num = 219;
        self.assertTrue(TestParser.test(input,expect,num))
    def test_020_array_literal(self):
        input = r"""
            Class Program {
                Var array: Array[Int, 5] = Array(1,2,3,4,5);
            }
        """
        expect = r"successful"
        num = 220;
        self.assertTrue(TestParser.test(input,expect,num))
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
        num = 221;
        self.assertTrue(TestParser.test(input,expect,num))
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
        self.assertTrue(TestParser.test(input,expect,num))
    def test_023_array_complex_initialization(self):
        input = r"""
            Class Program {
                Var array: Array[Int, 6] = Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x));        
            }
        """
        expect = r"successful"
        num = 223
        self.assertTrue(TestParser.test(input,expect,num))    
    
    def test_024_array_complex_initialization(self):
        input = r"""
            Class Program {
                Var array: Array[Int, 6] = Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x));        
            }
        """
        expect = r"successful"
        num = 224
        self.assertTrue(TestParser.test(input,expect,num))    
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
        self.assertTrue(TestParser.test(input,expect,num))
    def test_026_three_dimensional_array(self):
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
        num = 226
        self.assertTrue(TestParser.test(input,expect,num))
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
        self.assertTrue(TestParser.test(input,expect,num))
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
        self.assertTrue(TestParser.test(input,expect,num))
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
        self.assertTrue(TestParser.test(input,expect,num))
    def test_030_member_accesss_expression(self): 
        input = r"""
            Class Program {
                main() {
                    Var a: Int;
                    a = class_variable.attribute;
                    a = class_variable.attribute.attrubute;
                    a = class_name::$attribute;
                    a = class_name::$attribute.attribute;
                    a = class_variable.method(a,b,c);
                    a = class_variable.attribute.method(a,b,c);
                    a = class_name::$method(abc);
                }
            }
        """
        expect = r"successful"
        num = 230
        self.assertTrue(TestParser.test(input,expect,num))
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
        self.assertTrue(TestParser.test(input,expect,num))    
    def test_032_incorrect_access_static(self): 
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
        self.assertTrue(TestParser.test(input,expect,num))   
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
        self.assertTrue(TestParser.test(input,expect,num))    
    def test_034_incorrect_access_instance(self): 
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
        self.assertTrue(TestParser.test(input,expect,num))    
    def test_035_string_expression(self): 
        input = r"""
            Class Program {
                main() {
                    Var s: String;
                    s = "abc" +. "abc";
                    s = "abc" ==. "abc";
                }
            }
        """
        expect = r"successful"
        num = 235
        self.assertTrue(TestParser.test(input,expect,num))    
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
        self.assertTrue(TestParser.test(input,expect,num))    
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
        self.assertTrue(TestParser.test(input,expect,num))  
          
