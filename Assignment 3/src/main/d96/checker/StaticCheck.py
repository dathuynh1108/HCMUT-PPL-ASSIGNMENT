
"""
 * @author Huynh Thanh Dat
"""
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
"""


def print_scope(scope):
    print("Global: [")
    for class_name in scope["global"]:
        for att in scope["global"][class_name]:
            print("   ", att, scope["global"][class_name][att])
    print("]")
    print("Current class:", scope["current"])
    print("Local: [")
    if "local" in scope:
        for local_scope in scope["local"]:
            print("[")
            for var in local_scope:
                print("   ", var, local_scope[var])
            print("]")
    print("]")

from main.d96.utils.AST import *
from main.d96.utils.Utils import Utils
from main.d96.utils.Visitor import *
from StaticError import *

class D96_utils:
    @staticmethod
    def compare(type_1, type_2): # Compare 2 type
        # Two array equal if size and element type is same
        if type(type_1) == ArrayType and type_2 == ArrayType: 
            return type_1.size == type_2.size and D96_utils.compare(type_1.eleType, type_2.eleType)
        # Same class type
        if type(type_1) ==  ClassType and type(type_2) == ClassType:
            return type_1.classname.name == type_2.classname.name
        return type(type_1) == type(type_2)
    
    @staticmethod
    def coercion(type_1, type_2, inheritance): # Check a type can coercion to another type
        print(inheritance)
        if type(type_2) == FloatType and type(type_1) == IntType: return True
        # Check type_2 is parent type_1
        # print(type_1, type_2)
        if type(type_2) == ClassType and type(type_1) == ClassType:
            parent_name = inheritance[type_1.classname.name]
            while parent_name: 
                if type_2.classname.name == parent_name: return True
                parent_name = inheritance[parent_name]
        return False
    
    @staticmethod # Find a attribute in class scope: current class --> parent class --> parent parent class
    def find_attribute(class_name, attribute_name, global_scope, inheritance):
        current_class = class_name
        while current_class:
            if attribute_name in global_scope[current_class]: return global_scope[current_class][attribute_name]
            current_class = inheritance[current_class]
        return None

class D96_type:
    # Type use for LHS Symbol: ID, Field Access, ArrayCell
    def __init__(self, kind, si_kind, type, param_type = None):
        self.kind = kind
        self.si_kind = si_kind
        self.type = type
        self.param_type = param_type
    
    def __str__(self):
        return "["+ str(self.kind) + " " + str(self.si_kind) + " " +str(self.type)  + (" " + str(self.param_type) if self.param_type else "") + "]"


class StaticChecker(BaseVisitor,Utils):    
    def __init__(self,ast):
        self.ast = ast
        self.inheritance = {}  # inheritance list, parent of each class
    
    def check(self):
        return self.visit(self.ast, None)

    def visitProgram(self,ast, scope): 
        #self.global_scope, self.inheritance = Get_global_scope().get_all_class_scope(ast)
        scope = {}
        scope["global"] = {}
        for decl in ast.decl: self.visit(decl, scope)
        return []
    
    def visitClassDecl(self, ast, scope):
        if ast.classname.name in scope["global"]: raise Redeclared(Class(), ast.classname.name)
        scope["global"][ast.classname.name] = {} # init scope for this class
        scope["current"] = ast.classname.name # save current class 
        #print_scope(scope)
        if ast.parentname:
            if ast.parentname.name not in scope["global"]: raise Undeclared(Class(), ast.parentname.name)
            self.inheritance[ast.classname.name] = ast.parentname.name
        else: self.inheritance[ast.classname.name] = None
        #print_scope(scope)
        for mem in ast.memlist: self.visit(mem, scope)

    def visitAttributeDecl(self, ast, scope):
        self.visit(ast.decl, (ast.kind, scope))
    
    def visitVarDecl(self, ast, scope):
        # kind in scope is: Instance | Static | Parameter | Variable
        # Check redeclare:   
        kind, scope = scope  # param or variable
        decl_type = self.visit(ast.varType, scope)
        init_type = self.visit(ast.varInit, scope) if ast.varInit else None
        if "local" not in scope: # Attribute
            kind = "instance" if isinstance(kind, Instance) else "static"
            if ast.variable.name in scope["global"][scope["current"]]: raise Redeclared(Attribute(), ast.variable.name)
            scope["global"][scope["current"]][ast.variable.name] = D96_type("mutable", kind, decl_type)
        # if not in class scope (in local)
        # --> push to local and check redeclare (Class scope has been checked)
        else: # Local scope --> Variable
            if ast.variable.name in scope["local"][0]: raise Redeclared(kind, ast.variable.name)
            scope["local"][0][ast.variable.name] = D96_type("variable", None, decl_type)
        
        #print(ast.variable.name, "Declare type:", decl_type, "Init type:", init_type)
        # Check type


    def visitConstDecl(self, ast, scope):
        # kind in scope is: Instance | Static | Constant
        kind, scope = scope
        if ast.value == None: raise IllegalConstantExpression(ast.value)
        decl_type = self.visit(ast.constType, scope)
        init_type = self.visit(ast.value, (True, scope)) if ast.value else None
        if "local" not in scope:  # attribute
            kind = "instance" if isinstance(kind, Instance) else "static"
            if ast.constant.name in scope["global"][scope["current"]]: raise Redeclared(Attribute(), ast.constant.name)
            scope["global"][scope["current"]][ast.constant.name] = D96_type("imutable", kind, decl_type)


        if "local" in scope: # if not in class context because class context has been check
            if ast.constant.name in scope["local"][0]: raise Redeclared(kind, ast.constant.name)
            scope["local"][0][ast.constant.name] = D96_type("constant", None, decl_type)

        # Check type
        # if isinstance(init_type, D96_type): 
        #     if init_type.kind == "mutable" or init_type == ""


    def visitMethodDecl(self, ast, scope): 
        # Check redeclare
        if ast.name.name in scope["global"][scope["current"]]: raise Redeclared(Method(), ast.name.name)
        si_kind = "instance" if isinstance(ast.kind, Instance) else "static"
        param_type = [self.visit(param.varType, scope) for param in ast.param]
        scope["global"][scope["current"]][ast.name.name] = D96_type("method", si_kind, None, param_type)

        new_scope = {} # create new --> reference global and current --> add local
        new_scope["global"] = scope["global"]
        new_scope["current"] = scope["current"]
        new_scope["local"] = [{}] 
        in_loop = False
        # Check param redeclare
        for param in ast.param: self.visit(param, (Parameter(), new_scope))
        # Check body
        for stmt in ast.body.inst: 
            if isinstance(stmt, VarDecl): self.visit(stmt, (Variable(), new_scope)) 
            elif isinstance(stmt, ConstDecl): self.visit(stmt, (Constant(), new_scope))
            else: self.visit(stmt, (in_loop, new_scope))   

    # Expression: 
    def visitUnaryOp(self, ast, scope): 
        body_type = self.visit(ast.body, scope)
        if isinstance(scope, tuple):
            in_const_expression, scope = scope
            if isinstance(body_type, D96_type): # body is an ID, FieldAccess or ArrayCell
                # Check is in const expression
                if in_const_expression and (body_type.kind == "mutable" or body_type.kind == "variable"): raise IllegalConstantExpression(ast)
        # take the type
        if isinstance(body_type, D96_type): 
            if body_type.kind == "method": raise TypeMismatchInExpression(ast)
            body_type = body_type.type
        if ast.op == "-":
            if type(body_type) == IntType or type(body_type) == FloatType: return body_type
            raise TypeMismatchInExpression(ast)
        if ast.op == "!" and type(body_type) == BoolType: return body_type
        raise TypeMismatchInExpression(ast)
    
    def visitBinaryOp(self, ast, scope): 
        left_type = self.visit(ast.left, scope)
        right_type = self.visit(ast.right, scope)
        if isinstance(scope, tuple):
            in_const_expression, scope = scope
            if isinstance(left_type, D96_type):
                if in_const_expression and (left_type.kind == "mutable" or left_type.kind == "variable"): raise IllegalConstantExpression(ast)
            if isinstance(right_type, D96_type):
                if in_const_expression and (right_type.kind == "mutable" or right_type.kind == "variable"): raise IllegalConstantExpression(ast)
        
        if isinstance(left_type, D96_type): 
            if left_type.kind == "method": raise TypeMismatchInExpression(ast)
            left_type = left_type.type
        if isinstance(right_type, D96_type):
            if right_type.kind == "method": raise TypeMismatchInExpression(ast)
            right_type = right_type.type

        if ast.op in ["+", "-", "*", "/"]:
            if not (
                (type(left_type) == IntType or type(left_type) == FloatType) 
                and 
                (type(right_type) == IntType or type(right_type) == FloatType)
            ): raise TypeMismatchInExpression(ast)
            if type(left_type) == FloatType or type(right_type) == FloatType: return FloatType
            return FloatType if ast.op != "/" else IntType
        
        if ast.op == "%":
            if type(left_type) == IntType and type(right_type) == IntType: return left_type
            raise TypeMismatchInExpression(ast)

        if ast.op in ["&&, ||"]:
            if type(left_type) == BoolType and type(right_type) == BoolType: return left_type
            raise TypeMismatchInExpression(ast)

        if ast.op == "==.":
            if type(left_type) == StringType and type(right_type) == StringType: return BoolType()

        if ast.op == "+.":
            if type(left_type) == StringType and type(right_type) == StringType: return left_type
            raise TypeMismatchInExpression(ast)
    
        if ast.op in ["==", "!="]:
            if D96_utils.compare(left_type, right_type):
                if type(left_type) == BoolType or type(left_type) == IntType: return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["<", ">", "<=", ">="]:
            if not (
                (type(left_type) == IntType or type(left_type) == FloatType) 
                and 
                (type(right_type) == IntType or type(right_type) == FloatType)
            ): raise TypeMismatchInExpression(ast)
            return BoolType()
    
    def visitNewExpr(self, ast, scope):
        if isinstance(scope, tuple): in_const_expresion, scope = scope
        if ast.classname.name in scope["global"]:
            return_type = ClassType(ast.classname)
        else: raise Undeclared(Class(), ast.classname.name)
        if len(ast.param) != 0: 
            if "Constructor" in scope["global"][ast.classname.name]:
                class_constructor = scope["global"][ast.classname.name]["Constructor"]
                argument_type = [self.visit(param, scope) for param in ast.param]
                print(argument_type)
                print(class_constructor.param_type)
                if len(argument_type) != len(class_constructor.param_type): raise TypeMismatchInExpression(ast)
                for i in range(len(argument_type)): 
                    if not D96_utils.compare(argument_type[i], class_constructor.param_type[i]) and not D96_utils.coercion(argument_type[i], class_constructor.param_type[i], self.inheritance): raise TypeMismatchInExpression(ast)
            else: raise Undeclared(Method(), "Constructor")
        return return_type

    def visitArrayCell(self, ast, scope): 
        if isinstance(scope, tuple): in_const_expresion, scope = scope
        array_type = self.visit(ast.arr, scope)
        if isinstance(array_type, D96_type): array_type = array_type.type
        index_type_list = [self.visit(idx, scope) for idx in ast.idx]
        # Go into each layer of index
        for index_type in index_type_list: 
            if type(array_type) != ArrayType: raise TypeMismatchInExpression(ast)
            if type(index_type) != IntType: raise TypeMismatchInExpression(ast)
            array_type = array_type.eleType
        return array_type
        
    def visitFieldAccess(self, ast,scope):
        if isinstance(scope, tuple):
            in_const_expresion, scope = scope
        if type(ast.obj) == SelfLiteral:
            # Self --> find in current class, and need to be static
            field_name_type = D96_utils.find_attribute(scope["current"], ast.fieldname.name, scope["global"], self.inheritance)
            if field_name_type == None: raise Undeclared(Attribute(), ast.fieldname.name)
            if field_name_type.si_kind == "static": raise IllegalMemberAccess(ast)
            return field_name_type
        
        if isinstance(ast.obj, Id): # A class name or a attribute
            # obj is static marked
            if "$" in ast.fieldname.name: 
                if ast.obj.name not in scope["global"]: 
                    try: 
                        self.visit(ast.obj, (in_const_expresion, scope))
                    except: 
                        # Exception when ast.obj.fieldname is not an Variable / Attribute --> Classname
                        raise Undeclared(Class(), ast.obj.name)
                    # An variable / attribute --> Not access to static    
                    raise IllegalMemberAccess(ast)
                field_name_type = D96_utils.find_attribute(ast.obj.name, ast.fieldname.name, scope["global"], self.inheritance)
                if field_name_type == None: raise Undeclared(Attribute(), ast.fieldname.name)
                if field_name_type.kind == "method": raise TypeMismatchInExpression(ast)
                return field_name_type
            
            if ast.obj.name in scope["global"]: # a class name --> obj is static
                field_name_type = D96_utils.find_attribute(ast.obj.name, ast.fieldname.name, scope["global"], self.inheritance)
                if field_name_type == None: raise Undeclared(Attribute(), ast.fieldname.name)
                if field_name_type.si_kind == "instance": raise IllegalMemberAccess(ast)
                if field_name_type.kind == "method": raise TypeMismatchInExpression(ast)
                return field_name_type
        
        # A ID of attr/var or Expression ---> obj is instance    
        obj_type = self.visit(ast.obj, (in_const_expresion, scope)) # instance
        if type(obj_type) == D96_type: obj_type = obj_type.type
        if type(obj_type) != ClassType: raise TypeMismatchInExpression(ast)
        class_name = obj_type.classname.name
        field_name_type = D96_utils.find_attribute(class_name, ast.fieldname.name, scope["global"], self.inheritance)
        if field_name_type == None: raise Undeclared(Attribute(), ast.fieldname.name)
        if field_name_type.si_kind == "static": raise IllegalMemberAccess(ast)
        if field_name_type.kind == "method": raise TypeMismatchInExpression(ast)
        return field_name_type
            
    def visitId(self, ast, scope):
        # check is in const declare
        if isinstance(scope, tuple):
            in_const_expression, scope = scope
        # check local scope
        if "local" in scope: 
            for local_scope in scope["local"]: 
                if ast.name in local_scope: return local_scope[ast.name]
        
        # check class scope        
        found_id = D96_utils.find_attribute(scope["current"], ast.name, scope["global"], self.inheritance)
        #print(ast.name, found_id)
        if found_id: return found_id
        raise Undeclared(Identifier(), ast.name)

    def visitIntType(self, ast, scope):
        return ast

    def visitFloatType(self, ast, scope):
        return ast

    def visitBoolType(self, ast, scope):
        return ast

    def visitStringType(self, ast, scope):
        return ast

    def visitArrayType(self, ast, scope):
        return ast

    def visitClassType(self, ast, scope):
        if ast.classname.name in scope["global"]:
            return ast
        raise Undeclared(Class(), ast.classname.name)
    
    def visitIntLiteral(self, ast, scope):
        return IntType()

    def visitFloatLiteral(self, ast, scope):
        return FloatType()

    def visitBooleanLiteral(self, ast, scope):
        return BoolType()

    def visitStringLiteral(self, ast, scope):
        return StringType()

    def visitNullLiteral(self, ast, scope):
        return ast

    def visitSelfLiteral(self, ast, scope):
        return ast

    def visitArrayLiteral(self, ast, scope):
        type_of_element_list = [self.visit(value, scope) for value in ast.value]
        for type_of_element in type_of_element_list: 
            if not D96_utils.compare(type_of_element, type_of_element_list[0]): 
                raise IllegalArrayLiteral(ast)
        return ArrayType(len(type_of_element_list), type_of_element_list[0])
