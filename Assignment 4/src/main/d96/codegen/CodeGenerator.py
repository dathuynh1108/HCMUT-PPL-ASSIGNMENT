"""
    @author: Huynh Thanh Dat
"""
# from StaticCheck import *
# from StaticError import *
########################################################################
from main.d96.utils.AST import *
from main.d96.checker.StaticCheck import *
from main.d96.checker.StaticError import *
########################################################################
from Emitter import Emitter
from Frame import Frame 
from abc import ABC, abstractmethod

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, type, value = None, init_value = None):
        self.name = name
        self.type = type
        self.value = value
        self.init_value = init_value

class CodeGenerator():
    def __init__(self):
        self.library = "io"

    def init(self):
        return [    
                    Symbol("getInt", MType([], IntType()), Class_name(self.library)),
                    Symbol("putInt", MType([IntType()], VoidType()), Class_name(self.library)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), Class_name(self.library)),
                    
                    Symbol("getFloat", MType([], FloatType()), Class_name(self.library)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), Class_name(self.library)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), Class_name(self.library)),

                    Symbol("getBool", MType([], BoolType()), Class_name(self.library)),
                    Symbol("putBool", MType([BoolType()], VoidType()), Class_name(self.library)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), Class_name(self.library)),

                    # Symbol("getString", MType([], StringType()), Class_name(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), Class_name(self.library)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), Class_name(self.library)),
                    Symbol("putLn", MType([], VoidType()), Class_name(self.library)),
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String
        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class Scope():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access(): 
    def __init__(self, frame, sym, is_left, is_first):
        self.frame = frame
        self.sym = sym
        self.is_left = is_left
        self.is_first = is_first

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value

class Class_name(Val):
    def __init__(self, value):
        #value: String
        self.value = value

class CodeGenVisitor(BaseVisitor):
    def __init__(self, ast, env, dir_):
        self.ast = ast
        self.env = env
        self.path = dir_
        self.instance_attribute = None
        self.static_attribute = None
        self.current_method_return_type = None
        self.class_name = None
        # self.emitter = Emitter(self.path + "/" + self.class_name + ".j")

    def visitProgram(self, ast, o):
        for class_decl in ast.decl: self.visit(class_decl, o)
        return o

    def visitClassDecl(self, ast, o):
        self.instance_attribute_list = []
        self.static_attribute_list =  []
        self.class_name = ast.classname.name
        self.emitter = Emitter(self.path+"/" + self.class_name + ".j")
        parent_name = "java/lang/Object"
        if ast.parentname is not None: parent_name = ast.parentname.name   
        self.emitter.printout(self.emitter.emitPROLOG(self.class_name, parent_name)) 
        for mem in ast.memlist: self.env = [self.visit(mem, None)] + self.env 
        # Gen instance constructor and static constructor
        self.gen_method(MethodDecl(Instance(), Id("<init>"), [], Block([])), Scope(o, self.env), Frame("<init>", VoidType()))
        self.gen_method(MethodDecl(Instance(), Id("<clinit>"), [], Block([])), Scope(o, self.env), Frame("<clinit>", VoidType()))
        self.emitter.emitEPILOG()

    def visitAttributeDecl(self, ast, o):
        attribute_name = ast.decl.variable.name if isinstance(ast.decl, VarDecl) else ast.decl.constant.name
        attribute_type = ast.decl.varType if isinstance(ast.decl, VarDecl) else ast.decl.constType
        is_static = True if isinstance(ast.kind, Static) else False
        is_final = False if isinstance(ast.decl, VarDecl) else False
        init_value = ast.decl.varInit if isinstance(ast.decl, VarDecl) else ast.decl.value
        if type(ast.kind) == Static: self.emitter.printout(self.emitter.emitSTATIC(attribute_name, attribute_type, is_final, init_value))
        else: self.emitter.printout(self.emitter.emitINSTANCE(attribute_name, attribute_type, is_final, init_value))
        symbol = Symbol(attribute_name, attribute_type, Class_name(self.class_name), init_value)
        if is_static: self.static_attribute_list.append(symbol)
        else: self.instance_attribute_list.append(symbol)
        return symbol

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name.name, None)
        if ast.name.name == "Constructor": ast.name.name = "<init>"
        self.gen_method(ast, Scope(frame, self.env.copy()), frame)
        return Symbol(ast.name.name, MType([param.varType for param in ast.param], self.current_method_return_type), Class_name(self.class_name))

    def gen_method(self, method, o, frame):
        self.current_method_return_type = None
        code = ""
        is_main = method.name.name == "main" and len(method.param) == 0
        is_static = True if method.kind is Static or is_main else False
        param_type = [ArrayType(0, StringType())] if is_main else [param.varType for param in method.param]
        frame.enterScope(True)
        # Method param:
        if method.name.name == "<init>" or not is_static:
            index = frame.getNewIndex()
            code += self.emitter.emitVAR(index, "this", ClassType(Id(self.class_name)), frame.getStartLabel(), frame.getEndLabel(), frame)
        elif is_main:
            index = frame.getNewIndex()
            code += self.emitter.emitVAR(index, "args", ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame)
        
        for param in method.param: code += self.visit(param, o)

        code += self.emitter.emitLABEL(frame.getStartLabel(), frame)
        # Method body
        if method.name.name == "<init>": 
            #code += self.emitter.emitREADVAR("this", ClassType(Id(self.class_name)), 0, frame)
            code += self.emitter.emitTHIS(frame)
            code += self.emitter.emitINVOKESPECIAL(frame)
            for instance_attribute in self.instance_attribute_list: 
                if instance_attribute.init_value is None: continue
                # code += self.emitter.emitREADVAR("this", ClassType(Id(self.class_name)), 0, frame)
                code += self.emitter.emitTHIS(frame)
                init_code, init_type = self.visit(instance_attribute.init_value, Access(frame, self.env, False, False))
                code += init_code
                code += self.emitter.emitPUTFIELD(self.class_name + "." + instance_attribute.name, instance_attribute.type, frame)
        elif method.name.name == "<clinit>": 
            for static_attribute in self.static_attribute_list:
                if static_attribute.init_value is None: continue
                init_code, init_type = self.visit(static_attribute.init_value, Access(frame, self.env, False, False))
                code += init_code
                code += self.emitter.emitPUTSTATIC(self.class_name + "." + static_attribute.name, static_attribute.type, frame)
        else: 
            for stmt in method.body.inst: code += self.visit(stmt, o)
        if self.current_method_return_type is None: self.current_method_return_type = VoidType()
        
        mtype = MType(param_type, self.current_method_return_type)
        code = self.emitter.emitMETHOD(method.name.name, mtype, is_static, frame) + code
        code += self.emitter.emitLABEL(frame.getEndLabel(), frame)

        if type(self.current_method_return_type) is VoidType: code += self.emitter.emitRETURN(VoidType(), frame)
        code += self.emitter.emitENDMETHOD(frame)
        self.emitter.printout(code)
        frame.exitScope()
    

    def visitVarDecl(self, ast, o):
        index = o.frame.getNewIndex()
        o.sym = [Symbol(ast.variable.name, ast.varType, Index(index))] + o.sym
        code =  self.emitter.emitVAR(index, ast.variable.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        if ast.varInit is not None: code += self.visit(Assign(ast.variable, ast.varInit), o)
        return code
    
    def visitConstDecl(self, ast, o):
        index = o.frame.getNewIndex()
        o.sym = [Symbol(ast.constant.name, ast.constType, Index(index))] + o.sym
        code = self.emitter.emitVAR(index, ast.constant.name, ast.constType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        if ast.value is not None: code += self.visit(Assign(ast.constant, ast.value), o)
        return code
    
    def visitUnaryOp(self, ast, o):
        body_code, body_type = self.visit(ast.body, o)
        if ast.op == '-': return body_code + self.emitter.emitNEGOP(body_type, o.frame), body_type
        return body_code + self.emitter.emitNOT(body_type, o.frame), body_type


    def visitAssign(self, ast, o):
        right_code, right_type = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        left_code, left_type = self.visit(ast.lhs, Access(o.frame, o.sym, True, True))
        code = right_code
        if type(right_type) is IntType and type(left_type) is FloatType: code += self.emitter.emitI2F(o.frame)
        return code + left_code


    def visitReturn(self, ast, o):
        return_code = ""
        expr_code, expr_type = self.visit(ast.expr, Access(o.frame, o.sym, False, True)) if ast.expr else "", VoidType()
        if self.current_method_return_type is None: self.current_method_return_type = expr_type
        return return_code
    
    def visitId(self, ast, o):
        return "None", "None"
    
    def visitIntLiteral(self, ast, o):
        return self.emitter.emitPUSHICONST(ast.value, o.frame), IntType()

    
