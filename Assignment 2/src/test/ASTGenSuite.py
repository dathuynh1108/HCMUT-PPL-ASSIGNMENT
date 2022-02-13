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

    def test_003_attribute_declaration(self):
        input = """
            Class Program {
                Var a,$b,c: Int = 1,2,3;
                method() {}
            }
        """
        expect = str(Program([ClassDecl(Id("Program"), [])]))
        num = 303
        self.assertTrue(TestAST.test(input, expect, num))
