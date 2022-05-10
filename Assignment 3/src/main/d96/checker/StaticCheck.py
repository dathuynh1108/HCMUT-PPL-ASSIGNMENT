
"""
 * @author Huynh Thanh Dat
"""

# from AST import *
# from Visitor import *
# from StaticError import *

from main.d96.utils.AST import *
from main.d96.utils.Visitor import *
from StaticError import *

class D96_type:
    # Type use for LHS Symbol: ID, Field Access, ArrayCell
    def __init__(self, kind, si_kind, type, param_type=None):
        self.kind = kind
        self.si_kind = si_kind
        self.type = type
        self.param_type = param_type

    def __str__(self):
        return "[" + str(self.kind) + " " + str(self.si_kind) + " " + str(self.type) + (" " + str(self.param_type) if self.param_type is not None else "") + "]"

class Class_scope:
    def __init__(self):
        self.attribute = {}
        self.method = {}   
    def insert_attribute(self, attribute_name, attribute_type):
        self.attribute[attribute_name] = attribute_type
    
    def insert_method(self, method_name, method_type):
        self.method[method_name] = method_type
    
    def find_attribute(self, attribute_name):
        if attribute_name in self.attribute: return self.attribute[attribute_name]
        return None
    
    def find_method(self, method_name):
        if method_name in self.method: return self.method[method_name]
        return None
    

class D96_utils:
    @staticmethod
    def compare(type_1, type_2): # Compare 2 type
        # Two array equal if size and element type is same
        if isinstance(type_1, D96_type): type_1 = type_1.type
        if isinstance(type_2, D96_type): type_2 = type_2.type
        if type(type_1) == ArrayType and type(type_2) == ArrayType: 
            return type_1.size == type_2.size and D96_utils.compare(type_1.eleType, type_2.eleType)
        # Same class type
        if type(type_1) ==  ClassType and type(type_2) == ClassType:
            return type_1.classname.name == type_2.classname.name
        return type(type_1) == type(type_2)
    
    @staticmethod
    def coercion(type_1, type_2, inheritance): # Check a type can coercion to another type
        if isinstance(type_1, D96_type): type_1 = type_1.type
        if isinstance(type_2, D96_type): type_2 = type_2.type
        if type(type_2) == FloatType and type(type_1) == IntType: return True
        # Check type_2 is parent type_1
        # print(type_1, type_2)
        if type(type_2) == ClassType and type(type_1) == NullLiteral: return True
        # if type(type_2) == ClassType and type(type_1) == ClassType:
        #     parent_name = inheritance[type_1.classname.name]
        #     while parent_name: 
        #         if type_2.classname.name == parent_name: return True
        #         parent_name = inheritance[parent_name]
        if type(type_2) == ArrayType and type(type_1) == ArrayType:
            return type_2.size == type_1.size and D96_utils.coercion(type_1.eleType, type_2.eleType, inheritance)
        return False
    
    @staticmethod # Find a attribute in class scope: current class --> parent class --> parent parent class
    def find_attribute(class_name, attribute_name, global_scope, inheritance):
        # current_class = class_name
        # while current_class is not None:
        #     if attribute_name in global_scope[current_class]: return global_scope[current_class][attribute_name]
        #     current_class = inheritance[current_class]     
        # if attribute_name in global_scope[class_name]: return global_scope[class_name][attribute_name]
        # return None
        return global_scope[class_name].find_attribute(attribute_name)
    
    @staticmethod
    def find_method(class_name, method_name, global_scope, inheritance):
        return global_scope[class_name].find_method(method_name)

    
    @staticmethod
    def find_local(id, local_scope_stack):
        for local_scope in local_scope_stack:
              if id in local_scope:
                    return local_scope[id]
        return None    

    @staticmethod
    def check_param_type(method, argument_type, inheritance):
        if len(method.param_type) != len(argument_type): return False
        for i in range(len(argument_type)): 
            if isinstance(argument_type[i], D96_type): argument_type[i] = argument_type[i].type
            if not D96_utils.compare(argument_type[i], method.param_type[i]) and not D96_utils.coercion(argument_type[i], method.param_type[i], inheritance):
                return False
        return True

    @staticmethod
    def check_class_scope(sub_class, parent_class, inheritance): 
        current_class = sub_class
        while current_class is not None:
            if current_class == parent_class: return True
            current_class = inheritance[current_class]
        return False



class StaticChecker(BaseVisitor):    
    def __init__(self,ast):
        self.ast = ast
        self.inheritance = {}  # inheritance list, parent of each class
        self.current_method = None
        self.current_class = None
        self.top_level_if_statement = None
    
    def check(self):
        return self.visit(self.ast, None)

    def visitProgram(self,ast, scope): 
        #self.global_scope, self.inheritance = Get_global_scope().get_all_class_scope(ast)
        scope = {}
        scope["global"] = {}
        has_program_class = False
        for decl in ast.decl: 
            self.visit(decl, scope)
            if decl.classname.name == "Program": has_program_class = True
        if not has_program_class: raise NoEntryPoint()
        return []
    
    def visitClassDecl(self, ast, scope):
        if ast.classname.name in scope["global"]: raise Redeclared(Class(), ast.classname.name)
        # scope["global"][ast.classname.name] = {} # init scope for this class
        scope["global"][ast.classname.name] = Class_scope()
        #scope["current"] = ast.classname.name # save current class 
        self.current_class = ast.classname.name
        #print_scope(scope)
        if ast.parentname:
            if ast.parentname.name not in scope["global"]: raise Undeclared(Class(), ast.parentname.name)
            self.inheritance[ast.classname.name] = ast.parentname.name
        else: self.inheritance[ast.classname.name] = None
        for mem in ast.memlist: 
            if ast.classname.name == "Program" and isinstance(mem, MethodDecl) and mem.name.name == "main" and mem.param != []: raise NoEntryPoint()
            self.visit(mem, scope) 

        self.current_class = None
        

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
            if scope["global"][self.current_class].find_attribute(ast.variable.name): raise Redeclared(Attribute(), ast.variable.name)
            scope["global"][self.current_class].insert_attribute(ast.variable.name, D96_type("mutable", kind, decl_type))
        # if not in class scope (in local)
        # --> push to local and check redeclare (Class scope has been checked)
        else: # Local scope --> Variable
            if ast.variable.name in scope["local"][0]: raise Redeclared(kind, ast.variable.name)
            scope["local"][0][ast.variable.name] = D96_type("variable", None, decl_type)
        
        # Check type
        if ast.varInit: 
            if isinstance(init_type, D96_type): init_type = init_type.type
            if not D96_utils.compare(init_type, decl_type) and not D96_utils.coercion(init_type, decl_type, self.inheritance): raise TypeMismatchInStatement(ast)



    def visitConstDecl(self, ast, scope):
        # kind in scope is: Instance | Static | Constant
        kind, scope = scope
        if ast.value is None: raise IllegalConstantExpression(ast.value)
        decl_type = self.visit(ast.constType, scope)
        init_type = self.visit(ast.value, scope) if ast.value else None
        if "local" not in scope:  # attribute
            kind = "instance" if isinstance(kind, Instance) else "static"
            if scope["global"][self.current_class].find_attribute(ast.constant.name): raise Redeclared(Attribute(), ast.constant.name)
            scope["global"][self.current_class].insert_attribute(ast.constant.name, D96_type("imutable", kind, decl_type))

        if "local" in scope: # if not in class context because class context has been check
            if ast.constant.name in scope["local"][0]: raise Redeclared(kind, ast.constant.name)
            scope["local"][0][ast.constant.name] = D96_type("constant", None, decl_type)
        
        # Check type
        if ast.value:
            if isinstance(init_type, D96_type): 
                if init_type.kind != "imutable" and init_type.kind != "constant": raise IllegalConstantExpression(ast.value)
                init_type = init_type.type
            if not D96_utils.compare(init_type, decl_type) and not D96_utils.coercion(init_type, decl_type, self.inheritance): raise TypeMismatchInConstant(ast)



    def visitMethodDecl(self, ast, scope): 
        # Check redeclare
        if scope["global"][self.current_class].find_method(ast.name.name): raise Redeclared(Method(), ast.name.name)
        si_kind = "instance" if isinstance(ast.kind, Instance) else "static"
        param_type = [self.visit(param.varType, scope) for param in ast.param]
        scope["global"][self.current_class].insert_method(ast.name.name, D96_type("method", si_kind, None, param_type))

        self.current_method = ast.name.name

        new_scope = scope.copy() # create new --> reference global and current --> add local
        new_scope["local"] = [{}] 
        in_loop = False
        # Check param redeclare
        for param in ast.param: self.visit(param, (Parameter(), new_scope))
        # Check body
        for stmt in ast.body.inst: 
            if isinstance(stmt, VarDecl): self.visit(stmt, (Variable(), new_scope)) 
            elif isinstance(stmt, ConstDecl): self.visit(stmt, (Constant(), new_scope))
            else: self.visit(stmt, (in_loop, new_scope))   
        # Check and for no return type:
        if scope["global"][self.current_class].find_method(ast.name.name).type is None: scope["global"][self.current_class].find_method(ast.name.name).type = VoidType()
        self.current_method = None
    
    # Expression: 
    def visitUnaryOp(self, ast, scope): 
        expression_kind = "imutable"
        body_type = self.visit(ast.body, scope)
        # take the type
        if isinstance(body_type, D96_type): 
            if body_type.kind != "mutable" and body_type.kind != "constant": expression_kind = "mutable"
            body_type = body_type.type
        if ast.op == "-":
            if type(body_type) == IntType or type(body_type) == FloatType: return D96_type(expression_kind, None, body_type)
            raise TypeMismatchInExpression(ast)
        if ast.op == "!" and type(body_type) == BoolType: return D96_type(expression_kind, None, body_type)
        raise TypeMismatchInExpression(ast)
    
    def visitBinaryOp(self, ast, scope): 
        expression_kind = "imutable"
        left_type = self.visit(ast.left, scope)
        right_type = self.visit(ast.right, scope)
        #print(left_type, right_type)
        if isinstance(left_type, D96_type): 
            if left_type.kind != "mutable" and left_type.kind != "constant": expression_kind = "mutable"
            left_type = left_type.type
        if isinstance(right_type, D96_type): 
            if right_type.kind != "mutable" and right_type.kind != "constant": expression_kind = "mutable"
            right_type = right_type.type
        
        if ast.op in ["+", "-", "*", "/"]:
            if not (
                (type(left_type) == IntType or type(left_type) == FloatType) 
                and 
                (type(right_type) == IntType or type(right_type) == FloatType)
            ): raise TypeMismatchInExpression(ast)
            if type(left_type) == FloatType or type(right_type) == FloatType: return FloatType()
            return D96_type(expression_kind, None, FloatType()) if ast.op == "/" else D96_type(expression_kind, None,IntType())
        
        if ast.op == "%":
            if type(left_type) == IntType and type(right_type) == IntType: return D96_type(expression_kind, None, left_type)
            raise TypeMismatchInExpression(ast)

        if ast.op in ["&&", "||"]:
            if type(left_type) == BoolType and type(right_type) == BoolType: return D96_type(expression_kind, None, left_type)
            raise TypeMismatchInExpression(ast)

        if ast.op == "==.":
            if type(left_type) == StringType and type(right_type) == StringType: return D96_type(expression_kind, None, BoolType())
            raise TypeMismatchInExpression(ast)

        if ast.op == "+.":
            if type(left_type) == StringType and type(right_type) == StringType: return D96_type(expression_kind, None, left_type)
            raise TypeMismatchInExpression(ast)
    
        if ast.op in ["==", "!="]:
            if D96_utils.compare(left_type, right_type):
                if type(left_type) == BoolType or type(left_type) == IntType: return D96_type(expression_kind, None, BoolType())
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["<", ">", "<=", ">="]:
            if not (
                (type(left_type) == IntType or type(left_type) == FloatType) 
                and 
                (type(right_type) == IntType or type(right_type) == FloatType)
            ): raise TypeMismatchInExpression(ast)
            return D96_type(expression_kind, None, BoolType())
    
    def visitNewExpr(self, ast, scope):
        if ast.classname.name in scope["global"]:
            return_type = ClassType(ast.classname)
        else: raise Undeclared(Class(), ast.classname.name)
        if len(ast.param) != 0: 
            class_constructor = scope["global"][ast.classname.name].find_method("Constructor")
            if class_constructor:
                argument_type = [self.visit(param, scope) for param in ast.param]
                if not D96_utils.check_param_type(class_constructor, argument_type, self.inheritance): raise TypeMismatchInExpression(ast)
            else: raise Undeclared(Method(), "Constructor")
        return D96_type("mutable", None, return_type)

    def visitArrayCell(self, ast, scope): 
        array_type = self.visit(ast.arr, scope)
        kind = None
        if isinstance(array_type, D96_type): 
            kind = array_type.kind
            array_type = array_type.type
        index_type_list = [self.visit(idx, scope) for idx in ast.idx]
        # Go into each layer of index
        for index_type in index_type_list: 
            if type(index_type) == D96_type: index_type = index_type.type
            if type(array_type) != ArrayType: raise TypeMismatchInExpression(ast)
            if type(index_type) != IntType: raise TypeMismatchInExpression(ast)
            array_type = array_type.eleType
        return D96_type(kind, None, array_type)
        
    def visitFieldAccess(self, ast, scope):
        if type(ast.obj) == SelfLiteral:
            # Self not use in static method
            if self.current_method and self.current_method != "main" and scope["global"][self.current_class].find_method(self.current_method).si_kind == "static": raise IllegalMemberAccess(ast)
            # Self --> find in current class, and need to be instance
            field_name_type = D96_utils.find_attribute(self.current_class, ast.fieldname.name, scope["global"], self.inheritance)
            if field_name_type is None: raise Undeclared(Attribute(), ast.fieldname.name)
            if field_name_type.kind == "method": raise Undeclared(Attribute(), ast.fieldname.name)
            if field_name_type.si_kind == "static": raise IllegalMemberAccess(ast)
            # if const_expresion and field_name_type.kind == "mutable": raise IllegalConstantExpression(const_expresion)
            return field_name_type
        

        if isinstance(ast.obj, Id):
            # Static ID
            # E::$a. E is a class or E is a local
            # E is a class ---> True
            # E is a var ---> False
            # --> Prio E is a class
            if "$" in ast.fieldname.name: # A class name or a attribute
                # obj is static marked --> need a class
                # if not class
                if ast.obj.name not in scope["global"]: 
                    # If a variable --> Cannot access to static
                    if D96_utils.find_local(ast.obj.name, scope["local"]): raise IllegalMemberAccess(ast)
                    # If not a variable --> Undeclare class
                    raise Undeclared(Class(), ast.obj.name)
                # If a class --> find attribute
                field_name_type = D96_utils.find_attribute(ast.obj.name, ast.fieldname.name, scope["global"], self.inheritance)
                if field_name_type is None: raise Undeclared(Attribute(), ast.fieldname.name)
                if field_name_type.kind == "method": raise Undeclared(Attribute(), ast.fieldname.name)
                if field_name_type.si_kind == "instance": raise IllegalMemberAccess(ast)
                # if const_expresion and field_name_type.kind == "mutable": raise IllegalConstantExpression(const_expresion)
                return field_name_type
            
            # Normal ID:
            # E.a: E is a class or E is a local
            # E is local --> true
            # E is class --> false
            # --> Prio E is local
            obj_type  = D96_utils.find_local(ast.obj.name, scope["local"])
            if obj_type: # is a local
                if isinstance(obj_type, D96_type): obj_type = obj_type.type
                if type(obj_type) != ClassType: raise TypeMismatchInExpression(ast)
                
                # Class Scope: Current class can see instance attribute of it or it's parent
                # if not D96_utils.check_class_scope(self.current_class, obj_type.classname.name, self.inheritance): raise Undeclared(Attribute(), ast.fieldname.name)
                
                field_name_type = D96_utils.find_attribute(obj_type.classname.name, ast.fieldname.name, scope["global"], self.inheritance)
                if field_name_type is None: raise Undeclared(Attribute(), ast.fieldname.name)
                if field_name_type.kind == "method": raise Undeclared(Attribute(), ast.fieldname.name)
                if field_name_type.si_kind == "static": raise IllegalMemberAccess(ast)
                # if const_expresion and field_name_type.kind == "mutable": raise IllegalConstantExpression(const_expresion)
                return field_name_type
            # Not a local --> A class or Undeclare
            if ast.obj.name in scope["global"]: raise IllegalMemberAccess(ast)
            raise Undeclared(Identifier(), ast.obj.name)
        
        expression_kind = "imutable"
        obj_type = self.visit(ast.obj, scope)
        if isinstance(obj_type, D96_type): 
            if obj_type.kind != "imutable": expression_kind = "mutable"
            obj_type = obj_type.type
        if type(obj_type) != ClassType: raise TypeMismatchInExpression(ast)
        # Class Scope: Current class can see instance attribute of it or it's parent
        # if not D96_utils.check_class_scope(self.current_class, obj_type.classname.name, self.inheritance): raise Undeclared(Attribute(), ast.fieldname.name)
                
        field_name_type = D96_utils.find_attribute(obj_type.classname.name, ast.fieldname.name, scope["global"], self.inheritance)
        if field_name_type is None: raise Undeclared(Attribute(), ast.fieldname.name)
        if field_name_type.kind == "method": raise Undeclared(Attribute(), ast.fieldname.name)
        if field_name_type.si_kind == "static": raise IllegalMemberAccess(ast)
        # if const_expresion and field_name_type.kind == "mutable": raise IllegalConstantExpression(const_expresion)
        if field_name_type.kind != "imutable": expression_kind = "mutable"
        return D96_type(expression_kind, None, field_name_type.type)

    def visitCallExpr(self, ast, scope):
        # Method có tính vào không khởi tạo cho const không ????
        # if const_expresion: raise IllegalConstantExpression(const_expresion)
        
        if type(ast.obj) == SelfLiteral:
            if self.current_method and self.current_method != "main" and scope["global"][self.current_class].find_method(self.current_method).si_kind == "static": raise IllegalMemberAccess(ast)
            call_method  = D96_utils.find_method(self.current_class, ast.method.name, scope["global"], self.inheritance)
            if call_method is None: raise Undeclared(Method(), ast.method.name)
            if call_method.kind != "method": raise Undeclared(Method(), ast.method.name)
            if call_method.si_kind == "static": raise IllegalMemberAccess(ast)
            if type(call_method.type) == VoidType: raise TypeMismatchInExpression(ast) 
            # Check type param
            argument_type = [self.visit(param, scope) for param in ast.param]
            if not D96_utils.check_param_type(call_method, argument_type, self.inheritance): raise TypeMismatchInExpression(ast)
            return call_method.type
        
        # Static method
        if isinstance(ast.obj, Id):
            if "$" in ast.method.name:
                if ast.obj.name not in scope["global"]: 
                    # If a variable --> Cannot access to static
                    if D96_utils.find_local(ast.obj.name, scope["local"]): raise IllegalMemberAccess(ast)
                    # If not a variable --> Undeclare class
                    raise Undeclared(Class(), ast.obj.name)
                
                call_method = D96_utils.find_method(ast.obj.name, ast.method.name, scope["global"], self.inheritance)
                if call_method is None: raise Undeclared(Method(), ast.method.name)
                if call_method.kind != "method": raise Undeclared(Method(), ast.method.name)
                if call_method.si_kind == "instance": raise IllegalMemberAccess(ast)
                if type(call_method.type) == VoidType: raise TypeMismatchInExpression(ast) 
                # Check type param
                argument_type = [self.visit(param, scope) for param in ast.param]
                if not D96_utils.check_param_type(call_method, argument_type, self.inheritance): raise TypeMismatchInExpression(ast)
                return call_method.type
            
            obj_type = D96_utils.find_local(ast.obj.name, scope["local"])
            if obj_type:
                if isinstance(obj_type, D96_type): obj_type = obj_type.type
                call_method = D96_utils.find_method(obj_type.classname.name, ast.method.name, scope["global"], self.inheritance)
                if call_method is None: raise Undeclared(Method(), ast.method.name)
                if call_method.kind != "method": raise Undeclared(Method(), ast.method.name)
                if call_method.si_kind == "static": raise IllegalMemberAccess(ast)
                if type(call_method.type) == VoidType: raise TypeMismatchInExpression(ast) 
                # Check type param
                argument_type = [self.visit(param, scope) for param in ast.param]
                if not D96_utils.check_param_type(call_method, argument_type, self.inheritance): raise TypeMismatchInExpression(ast)
                return call_method.type
            # Not a local --> A class or Undeclare
            if ast.obj.name in scope["global"]: raise IllegalMemberAccess(ast)
            raise Undeclared(Identifier(), ast.obj.name)
        
        # Normal ID or Expr --> Instance
        obj_type = self.visit(ast.obj, scope)
        if isinstance(obj_type, D96_type): obj_type = obj_type.type
        if type(obj_type) != ClassType: raise TypeMismatchInExpression(ast)
        call_method = D96_utils.find_method(obj_type.classname.name, ast.method.name, scope["global"], self.inheritance)
        if call_method is None: raise Undeclared(Method(), ast.method.name)
        if call_method.kind != "method": raise Undeclared(Method(), ast.method.name)
        if call_method.si_kind == "static": raise IllegalMemberAccess(ast)
        if type(call_method.type) == VoidType: raise TypeMismatchInExpression(ast) 
        # Check type param
        argument_type = [self.visit(param, scope) for param in ast.param]
        if not D96_utils.check_param_type(call_method, argument_type, self.inheritance): raise TypeMismatchInExpression(ast)
        return call_method.type

    def visitId(self, ast, scope): # Only use to find local variable
        # check is in const declare
        # check local scope
        if "local" in scope: 
            local_id = D96_utils.find_local(ast.name, scope["local"])
            if local_id: 
                # if const_expression and (local_id.kind == "mutable" or local_id.kind == "variable"): raise IllegalConstantExpression(const_expression)
                return local_id
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
        return D96_type("constant", None, IntType())

    def visitFloatLiteral(self, ast, scope):
        return D96_type("constant", None, FloatType())

    def visitBooleanLiteral(self, ast, scope):
        return D96_type("constant", None, BoolType())

    def visitStringLiteral(self, ast, scope):
        return D96_type("constant", None, StringType())

    def visitNullLiteral(self, ast, scope):
        return D96_type("constant", None, ast)

    def visitSelfLiteral(self, ast, scope):
        return ast

    def visitArrayLiteral(self, ast, scope):
        try:
            type_of_element_list = [self.visit(value, scope) for value in ast.value]
        except IllegalArrayLiteral:
            raise IllegalArrayLiteral(ast)
        for type_of_element in type_of_element_list: 
            if not D96_utils.compare(type_of_element, type_of_element_list[0]): raise IllegalArrayLiteral(ast)
        return ArrayType(len(type_of_element_list), type_of_element_list[0])
    
    # Statement:
    def visitAssign(self, ast, scope): 
        in_loop, scope = scope
        rhs_type = self.visit(ast.exp, scope)
        lhs_type = self.visit(ast.lhs, scope)
        #print(lhs_type, rhs_type)
        if isinstance(lhs_type, D96_type): 
            if lhs_type.kind == "imutable" or lhs_type.kind == "constant": raise CannotAssignToConstant(ast)
            lhs_type = lhs_type.type
        if isinstance(rhs_type, D96_type): rhs_type = rhs_type.type
        if not D96_utils.compare(lhs_type, rhs_type) and not D96_utils.coercion(rhs_type, lhs_type, self.inheritance): raise TypeMismatchInStatement(ast)


    def visitBlock(self, ast, scope): 
        param = scope
        #in_loop, scope = scope
        scope = scope[1]
        new_scope = scope.copy()
        new_scope["local"] = [{}] + scope["local"]
        for stmt in ast.inst: 
            if isinstance(stmt, VarDecl): self.visit(stmt, (Variable(), new_scope)) 
            elif isinstance(stmt, ConstDecl): self.visit(stmt, (Constant(), new_scope))
            else: self.visit(stmt, param)   


    def visitIf(self, ast, scope): 
        param = scope
        # ------------------------------------------------
        # scope = scope[1]
        # condition_type = self.visit(ast.expr, scope)
        # if isinstance(condition_type, D96_type): condition_type = condition_type.type
        # if type(condition_type) != BoolType: raise TypeMismatchInStatement(ast)
        # self.visit(ast.thenStmt, param)
        # if ast.elseStmt: self.visit(ast.elseStmt, param) 
        # -------------------------------------------------
        scope = scope[1]
        condition_type = self.visit(ast.expr, scope)
        if isinstance(condition_type, D96_type): condition_type = condition_type.type
        if type(condition_type) != BoolType: 
            if self.top_level_if_statement: raise TypeMismatchInStatement(self.top_level_if_statement)
            raise TypeMismatchInStatement(ast)
        
        # Reset when get in then statement, there is no top_if, after that restore value of top_if
        save_top_level_if_statement = self.top_level_if_statement
        self.top_level_if_statement = None
        self.visit(ast.thenStmt, param)
        self.top_level_if_statement = save_top_level_if_statement

        # save_top_level_if_statement = self.top_level_if_statement
        if isinstance(ast.elseStmt, If):
            # If Elsestmt is If --> Elseif branch --> If top_if is set, not change (This is not first elseif stmt)
            # Else --> Get in new scope --> top_if = None
            if self.top_level_if_statement is None: self.top_level_if_statement = ast
        else: self.top_level_if_statement = None
        if ast.elseStmt: self.visit(ast.elseStmt, param) 
        self.top_level_if_statement = save_top_level_if_statement

    def visitFor(self, ast, scope): 
        in_loop, scope = scope
        in_loop = True
        id_type = self.visit(ast.id, scope)
        expr1_type = self.visit(ast.expr1, scope)
        expr2_type = self.visit(ast.expr2, scope)
        # "In the case of a for statement, just the assignment part in this statement is printed out in the error message."
        if id_type.kind == "constant" or id_type.kind == "imutable": raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        id_type = id_type.type
        if isinstance(expr1_type, D96_type): expr1_type = expr1_type.type
        if isinstance(expr2_type, D96_type): expr2_type = expr2_type.type
        if type(expr1_type) != IntType or type(expr2_type) != IntType: raise TypeMismatchInStatement(ast)
        if type(id_type) != IntType and type(id_type) != FloatType: raise TypeMismatchInStatement(ast)
        if ast.expr3:
            expr3_type = self.visit(ast.expr3, scope) 
            if isinstance(expr3_type, D96_type): expr3_type = expr3_type.type
            if type(expr3_type) != IntType: raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, (in_loop, scope))

    def visitBreak(self, ast, scope): 
        in_loop, scope = scope
        if not in_loop: raise MustInLoop(ast)
    
    def visitContinue(self, ast, scope): 
        in_loop, scope = scope
        if not in_loop: raise MustInLoop(ast)
    
    def visitReturn(self, ast, scope): 
        in_loop, scope = scope
        if self.current_method == "main" and self.current_class == "Program" and ast.expr is not None: raise TypeMismatchInStatement(ast)
        if self.current_method == "Constructor" and ast.expr is not None: raise TypeMismatchInStatement(ast)
        if self.current_method == "Destructor": raise TypeMismatchInStatement(ast)
        currnet_return_type = self.visit(ast.expr, scope) if ast.expr else VoidType()

        # if isinstance(currnet_return_type, D96_type): currnet_return_type = currnet_return_type.type
        # Suy diễn kiểu
        current_method = scope["global"][self.current_class].find_method(self.current_method)
        if current_method.type is None:
            current_method.type = currnet_return_type
        else:
            # Chỗ này so cứng hay cho ép kiểu ??
            if not D96_utils.compare(currnet_return_type, current_method.type) and not D96_utils.coercion(currnet_return_type, current_method.type, self.inheritance):
                raise TypeMismatchInStatement(ast)
            

    def visitCallStmt(self, ast, scope): 
        in_loop, scope = scope
        if type(ast.obj) == SelfLiteral:
            if self.current_method and self.current_method != "main" and scope["global"][self.current_class].find_method(self.current_method).si_kind == "static": raise IllegalMemberAccess(ast)
            call_method  = D96_utils.find_method(self.current_class, ast.method.name, scope["global"], self.inheritance)
            if call_method is None: raise Undeclared(Method(), ast.method.name)
            if call_method.kind != "method": raise Undeclared(Method(), ast.method.name)
            if call_method.si_kind == "static": raise IllegalMemberAccess(ast)
            if type(call_method.type) != VoidType: raise TypeMismatchInStatement(ast) 
            # Check type param
            argument_type = [self.visit(param, scope) for param in ast.param]
            if not D96_utils.check_param_type(call_method, argument_type, self.inheritance): raise TypeMismatchInStatement(ast)
            # return call_method.type
            return

        # Static method
        if isinstance(ast.obj, Id):
            if "$" in ast.method.name:
                if ast.obj.name not in scope["global"]: 
                    # If a variable --> Cannot access to static
                    if D96_utils.find_local(ast.obj.name, scope["local"]): raise IllegalMemberAccess(ast)
                    # If not a variable --> Undeclare class
                    raise Undeclared(Class(), ast.obj.name)
                
                call_method = D96_utils.find_method(ast.obj.name, ast.method.name, scope["global"], self.inheritance)
                if call_method is None: raise Undeclared(Method(), ast.method.name)
                if call_method.kind != "method": raise Undeclared(Method(), ast.method.name)
                if call_method.si_kind == "instance": raise IllegalMemberAccess(ast)
                if type(call_method.type) != VoidType: raise TypeMismatchInStatement(ast) 
                # Check type param
                argument_type = [self.visit(param, scope) for param in ast.param]
                if not D96_utils.check_param_type(call_method, argument_type, self.inheritance): raise TypeMismatchInStatement(ast)
                # return call_method.type
                return
            
            obj_type = D96_utils.find_local(ast.obj.name, scope["local"])
            if obj_type:
                if isinstance(obj_type, D96_type): obj_type = obj_type.type
                call_method = D96_utils.find_method(obj_type.classname.name, ast.method.name, scope["global"], self.inheritance)
                if call_method is None: raise Undeclared(Method(), ast.method.name)
                if call_method.kind != "method": raise Undeclared(Method(), ast.method.name)
                if call_method.si_kind == "static": raise IllegalMemberAccess(ast)
                if type(call_method.type) != VoidType: raise TypeMismatchInStatement(ast) 
                # Check type param
                argument_type = [self.visit(param, scope) for param in ast.param]
                if not D96_utils.check_param_type(call_method, argument_type, self.inheritance): raise TypeMismatchInStatement(ast)
                # return call_method.type
                return
            # Not a local --> A class or Undeclare
            if ast.obj.name in scope["global"]: raise IllegalMemberAccess(ast)
            raise Undeclared(Identifier(), ast.obj.name)

        # Normal ID or Expr --> Instance
        obj_type = self.visit(ast.obj, scope)
        if isinstance(obj_type, D96_type): obj_type = obj_type.type
        if type(obj_type) != ClassType: raise TypeMismatchInStatement(ast)
        call_method = D96_utils.find_attribute(obj_type.classname.name, ast.method.name, scope["global"], self.inheritance)
        if call_method is None: raise Undeclared(Method(), ast.method.name)
        if call_method.kind != "method": raise Undeclared(Method(), ast.method.name)
        if call_method.si_kind == "static": raise IllegalMemberAccess(ast)
        if type(call_method.type) != VoidType: raise TypeMismatchInStatement(ast) 
        # Check type param
        argument_type = [self.visit(param, scope) for param in ast.param]
        if not D96_utils.check_param_type(call_method, argument_type, self.inheritance): raise TypeMismatchInStatement(ast)
        # return call_method.type
