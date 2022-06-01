"""
    @author: Huynh Thanh Dat
    HCMUT
    Principle Of Program Language
    Assignment 4
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
from CodeGenError import *

"""
    Use class Enviroment for store class scope (global) and local scope
    API is better than Assignment 3
"""


class Attribute:
    def __init__(self, name, type, init_value=None):
        self.name = name
        self.type = type
        self.init_value = init_value


class Method:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Local:
    def __init__(self, name, type, index):
        self.name = name
        self.type = type
        self.index = index


class Enviroment:
    def __init__(self, global_env={}, local_env=[{}]):
        self.global_env = global_env
        self.local_env = local_env

    def enter_class(self, class_name):
        self.global_env[class_name] = Class_scope()

    def enter_scope(self):
        self.local_env = [{}] + \
            self.local_env if self.local_env is not None else [{}]

    def exit_scope(self):
        self.local_env.pop(0)

    def insert_local(self, local_id, local_type):
        self.local_env[0][local_id] = local_type

    def insert_attribute(self, class_name, attribute_name, attribute_type):
        return self.global_env[class_name].insert_attribute(
            attribute_name, attribute_type
        )

    def insert_method(self, class_name, method_name, method_type):
        return self.global_env[class_name].insert_method(method_name, method_type)

    def find_local(self, id):
        for local_scope in self.local_env:
            if id in local_scope:
                return local_scope[id]
        return None

    def find_attribute(self, class_name, attribute_name):
        return self.global_env[class_name].find_attribute(attribute_name)

    def find_method(self, class_name, method_name):
        return self.global_env[class_name].find_method(method_name)

    def copy(self):
        return Enviroment(self.global_env, self.local_env.copy())


class Class_scope:
    def __init__(self, attribute={}, method={}):
        self.attribute = attribute
        self.method = method

    def insert_attribute(self, attribute_name, attribute_type):
        self.attribute[attribute_name] = attribute_type

    def insert_method(self, method_name, method_type):
        self.method[method_name] = method_type

    def find_attribute(self, attribute_name):
        if attribute_name in self.attribute:
            return self.attribute[attribute_name]
        return None

    def find_method(self, method_name):
        if method_name in self.method:
            return self.method[method_name]
        return None


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Scope:
    def __init__(self, frame, env):
        self.frame = frame
        self.env = env


class Access:
    def __init__(self, frame, env, is_left, is_first):
        self.frame = frame
        self.env = env
        self.is_left = is_left
        self.is_first = is_first


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int
        self.value = value


class Class_name(Val):
    def __init__(self, value, si_kind=None):
        # value: String
        self.value = value
        self.si_kind = si_kind


class CodeGenerator:
    """
    All attribute and method will be access via field access and method invovation
    Can save attribute, method and local in different place
    """

    def __init__(self):
        self.library = "io"

    def init(self):
        global_env = {
            "io": Class_scope(
                {},
                {
                    "getInt":       Method("getInt", MType([], IntType())),
                    "putInt":       Method("putInt", MType([IntType()], VoidType())),
                    "putIntLn":     Method("putIntLn", MType([IntType()], VoidType())),
                    "getFloat":     Method("getFloat", MType([], FloatType())),
                    "putFloat":     Method("putFloat", MType([FloatType()], VoidType())),
                    "putFloatLn":   Method("putFloatLn", MType([FloatType()], VoidType())),
                    "getBool":      Method("getBool", MType([], BoolType())),
                    "putBool":      Method("putBool", MType([BoolType()], VoidType())),
                    "putBoolLn":    Method("putBoolLn", MType([BoolType()], VoidType())),
                    "putString":    Method("putString", MType([StringType()], VoidType())),
                    "putStringLn":  Method("putStringLn", MType([StringType()], VoidType())),
                    "putLn":        Method("putLn", MType([], VoidType())),
                },
            )
        }
        return Enviroment(global_env, None)

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String
        env = self.init()
        gc = CodeGenVisitor(ast, env, dir_)
        gc.visit(ast, None)


# Because all type or declare fail is caught at checker --> Get class env before run for easy test, same as Java
class CodeGenVisitor(BaseVisitor):
    def __init__(self, ast, env, dir_):
        self.ast = ast
        self.env = env
        self.path = dir_
        self.instance_attribute = None
        self.static_attribute = None
        self.current_method_return_type = None
        self.class_name = None
        self.parent_class_name = None

    def visitProgram(self, ast, o):
        for class_decl in ast.decl:
            self.visit(class_decl, self.env)

    def visitClassDecl(self, ast, o):
        # o is self.env
        o.enter_class(ast.classname.name)
        self.instance_attribute_list = []
        self.static_attribute_list = []
        self.class_name = ast.classname.name
        self.emitter = Emitter(self.path + "/" + self.class_name + ".j")
        self.parent_class_name = "java/lang/Object"
        if ast.parentname is not None:
            self.parent_class_name = ast.parentname.name

        self.emitter.printout(
            self.emitter.emitPROLOG(self.class_name, self.parent_class_name)
        )
        has_default_init = False
        attribute_decl_list = []
        method_decl_list = []
        constructor = None
        # Sort mem, Jasmin places all fields before methods
        for mem in ast.memlist:
            if type(mem) is MethodDecl:
                if mem.name.name == "Constructor":
                    if len(mem.param) == 0:
                        has_default_init = True
                    constructor = mem
                else:
                    method_decl_list.append(mem)
            else:
                attribute_decl_list.append(mem)

        for attribute_decl in attribute_decl_list:
            self.visit(attribute_decl, o)

        # Order of method is not important, but first gen constructor to init an object of current class in later method
        if constructor is not None:
            self.visit(constructor, o)
        # Gen default instance constructor and static constructor
        if not has_default_init:
            self.gen_default_instance_constructor(o)
        self.gen_default_class_contructor(o)

        for method_decl in method_decl_list:
            self.visit(method_decl, o)

        self.emitter.emitEPILOG()

    def gen_default_instance_constructor(self, o):
        o.enter_scope()
        frame = Frame("<init>", VoidType())
        self.gen_method(
            MethodDecl(Instance(), Id("<init>"), [], Block([])),
            Scope(frame, o),
            frame,
        )
        o.exit_scope()

    def gen_default_class_contructor(self, o):
        o.enter_scope()
        frame = Frame("<clinit>", VoidType())
        self.gen_method(
            MethodDecl(Instance(), Id("<clinit>"), [], Block([])),
            Scope(frame, o),
            frame,
        )
        o.exit_scope()

    def visitAttributeDecl(self, ast, o):
        attribute_name = (
            ast.decl.variable.name
            if isinstance(ast.decl, VarDecl)
            else ast.decl.constant.name
        )
        attribute_type = (
            ast.decl.varType if isinstance(
                ast.decl, VarDecl) else ast.decl.constType
        )
        is_static = True if isinstance(ast.kind, Static) else False
        is_final = False if isinstance(ast.decl, VarDecl) else False
        init_value = (
            ast.decl.varInit if isinstance(
                ast.decl, VarDecl) else ast.decl.value
        )
        if type(ast.kind) is Static:
            self.emitter.printout(
                self.emitter.emitSTATIC(
                    attribute_name, attribute_type, is_final, init_value
                )
            )
        else:
            self.emitter.printout(
                self.emitter.emitINSTANCE(
                    attribute_name, attribute_type, is_final, init_value
                )
            )
        attribute = Attribute(attribute_name, attribute_type, init_value)
        if is_static:
            self.static_attribute_list.append(attribute)
        else:
            self.instance_attribute_list.append(attribute)
        o.insert_attribute(self.class_name, attribute_name, attribute)

    def visitMethodDecl(self, ast, o):
        if ast.name.name == "Constructor":
            ast.name.name = "<init>"
        frame = Frame(ast.name.name, None)
        o.enter_scope()
        self.gen_method(ast, Scope(frame, o), frame)
        # print("Stack after:", ast.name.name, frame.getStackSize())
        o.insert_method(
            self.class_name,
            ast.name.name,
            Method(
                ast.name.name,
                MType(
                    [param.varType for param in ast.param],
                    self.current_method_return_type,
                ),
            ),
        )
        o.exit_scope()

    def gen_method(self, method, o, frame):
        self.current_method_return_type = None
        code = ""
        is_main = method.name.name == "main" and len(method.param) == 0
        is_static = True if type(method.kind) is Static or is_main else False
        param_type = (
            [ArrayType(0, StringType())]
            if is_main
            else [param.varType for param in method.param]
        )
        frame.enterScope(True)
        # Method param:
        if method.name.name == "<init>" or not is_static:
            index = frame.getNewIndex()
            code += self.emitter.emitVAR(
                index,
                "this",
                ClassType(Id(self.class_name)),
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        elif is_main:
            index = frame.getNewIndex()
            code += self.emitter.emitVAR(
                index,
                "args",
                ArrayType(0, StringType()),
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        for param in method.param:
            code += self.visit(param, o)

        code += self.emitter.emitLABEL(frame.getStartLabel(), frame)
        # Method body
        if method.name.name == "<init>":
            # code += self.emitter.emitREADVAR("this", ClassType(Id(self.class_name)), 0, frame)
            code += self.emitter.emitTHIS(frame)
            code += self.emitter.emitINVOKESPECIAL(
                frame, self.parent_class_name +
                "/<init>", MType([], VoidType())
            )
            for instance_attribute in self.instance_attribute_list:
                if instance_attribute.init_value is None:
                    continue
                # code += self.emitter.emitREADVAR("this", ClassType(Id(self.class_name)), 0, frame)
                code += self.emitter.emitTHIS(frame)
                init_code, init_type = self.visit(
                    instance_attribute.init_value, Access(
                        frame, self.env, False, False)
                )
                code += init_code
                code += self.emitter.emitPUTFIELD(
                    self.class_name + "." + instance_attribute.name,
                    instance_attribute.type,
                    frame,
                )
        elif method.name.name == "<clinit>":
            for static_attribute in self.static_attribute_list:
                if static_attribute.init_value is None:
                    continue
                init_code, init_type = self.visit(
                    static_attribute.init_value, Access(
                        frame, self.env, False, False)
                )
                code += init_code
                code += self.emitter.emitPUTSTATIC(
                    self.class_name + "." + static_attribute.name,
                    static_attribute.type,
                    frame,
                )
        for inst in method.body.inst:
            code += self.visit(inst, o)
        if self.current_method_return_type is None:
            self.current_method_return_type = VoidType()

        mtype = MType(param_type, self.current_method_return_type)
        code = self.emitter.emitMETHOD(
            method.name.name, mtype, is_static, frame) + code
        code += self.emitter.emitLABEL(frame.getEndLabel(), frame)

        # Gen a default return at end if method is void type
        if type(self.current_method_return_type) is VoidType:
            code += self.emitter.emitRETURN(VoidType(), frame)
        code += self.emitter.emitENDMETHOD(frame)
        self.emitter.printout(code)
        frame.exitScope()

    def visitVarDecl(self, ast, o):
        index = o.frame.getNewIndex()
        o.env.insert_local(
            ast.variable.name, Local(ast.variable.name, ast.varType, index)
        )
        code = self.emitter.emitVAR(
            index,
            ast.variable.name,
            ast.varType,
            o.frame.getStartLabel(),
            o.frame.getEndLabel(),
            o.frame,
        )
        if ast.varInit is not None:
            code += self.visit(Assign(ast.variable, ast.varInit), o)
        return code

    def visitConstDecl(self, ast, o):
        index = o.frame.getNewIndex()
        o.env.insert_local(ast.constant.name, Local(ast.varType, index))
        code = self.emitter.emitVAR(
            index,
            ast.constant.name,
            ast.constType,
            o.frame.getStartLabel(),
            o.frame.getEndLabel(),
            o.frame,
        )
        if ast.value is not None:
            code += self.visit(Assign(ast.constant, ast.value), o)
        return code

    def visitUnaryOp(self, ast, o):
        body_code, body_type = self.visit(ast.body, o)
        if ast.op == "-":
            return body_code + self.emitter.emitNEGOP(body_type, o.frame), body_type
        return body_code + self.emitter.emitNOT(body_type, o.frame), body_type

    def visitBinaryOp(self, ast, o):
        left_code, left_type = self.visit(ast.left, o)
        right_code, right_type = self.visit(ast.right, o)
        return_type = left_type
        if (
            type(left_type) is FloatType
            or type(right_type) is FloatType
            or ast.op == "/"
        ):
            return_type = FloatType()
            if type(left_type) is IntType:
                left_code += self.emitter.emitI2F(o.frame)
            if type(right_type) is IntType:
                right_code += self.emitter.emitI2F(o.frame)
        if ast.op in ["+", "-"]:
            return (
                left_code
                + right_code
                + self.emitter.emitADDOP(ast.op, return_type, o.frame),
                return_type,
            )
        if ast.op in ["*", "/"]:
            return (
                left_code
                + right_code
                + self.emitter.emitMULOP(ast.op, return_type, o.frame),
                return_type,
            )
        if ast.op == "%":
            return left_code + right_code + self.emitter.emitMOD(o.frame), return_type
        if ast.op == "&&":
            return left_code + right_code + self.emitter.emitANDOP(o.frame), return_type
        if ast.op == "||":
            return left_code + right_code + self.emitter.emitOROP(o.frame), return_type
        if ast.op in [">", ">=", "<", "<=", "!=", "==", "==."]:
            return (
                left_code
                + right_code
                + self.emitter.emitREOP(ast.op, return_type, o.frame),
                BoolType(),
            )
        if ast.op == "+.":
            #   invokedynamic 0:makeConcatWithConstants(Ljava/lang/String;)Ljava/lang/String;
            # 	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
            return (
                left_code
                + right_code
                + self.emitter.emitINVOKEVIRTUAL(
                    "java/lang/String/concat",
                    MType([StringType()], StringType()),
                    o.frame,
                ),
                StringType(),
            )

    def visitNewExpr(self, ast, o):
        code = self.emitter.emitNEW(ast.classname.name, ast.param, o.frame)
        code += self.emitter.emitDUP(o.frame)

        # Default constructor
        if len(ast.param) == 0:
            code += self.emitter.emitINVOKESPECIAL(
                o.frame, ast.classname.name + "/<init>", MType([], VoidType())
            )
            return code, ClassType(ast.classname)

        init = o.env.find_method(ast.classname.name, "<init>")

        if init is None:
            raise IllegalRuntimeException("Cannot find <init>!")

        for i in range(len(ast.param)):
            argument_code, argument_type = self.visit(ast.param[i], o)
            code += argument_code
            if (
                type(argument_type) is IntType
                and type(init.type.partype[i]) is FloatType
            ):
                code += self.emitter.emitI2F(o.frame)

        code += self.emitter.emitINVOKESPECIAL(
            o.frame, ast.classname.name + "/<init>", init.type
        )
        return code, ClassType(ast.classname)

    def visitAssign(self, ast, o):
        # Field access assignment will be controlled in field access
        if type(ast.lhs) is FieldAccess:
            return self.visit(ast.lhs, (Access(o.frame, o.env, True, True), ast.exp))[0]
        # Array cell is same as field access
        if type(ast.lhs) is ArrayCell:
            return self.visit(ast.lhs, (Access(o.frame, o.env, True, True), ast.exp))[0]
        right_code, right_type = self.visit(
            ast.exp, Access(o.frame, o.env, False, True)
        )
        left_code, left_type = self.visit(
            ast.lhs, Access(o.frame, o.env, True, True))
        code = right_code
        if type(right_type) is IntType and type(left_type) is FloatType:
            code += self.emitter.emitI2F(o.frame)
        return code + left_code

    def visitFieldAccess(self, ast, o):
        value = None
        if type(o) is tuple:
            value = o[1]
            o = o[0]
        code = ""
        is_static = False
        class_name = None
        obj_code, obj_type = self.visit(
            ast.obj, Access(o.frame, o.env, False, False))
        if type(ast.obj) is Id:
            if "$" in ast.fieldname.name:
                is_static = True
                class_name = ast.obj.name
            elif obj_code is None or obj_type is None:  # Not a ID
                is_static = True
                class_name = ast.obj.name
            else:  # A local ID
                is_static = False
                class_name = obj_type.classname.name
                code += obj_code
        else:  # Self literal or expression
            is_static = False
            class_name = obj_type.classname.name
            code += obj_code
        # Find attribute type
        attribute = o.env.find_attribute(class_name, ast.fieldname.name)
        if attribute is None:
            raise IllegalRuntimeException("Cannot find attribute!")

        if o.is_left and o.is_first:  # Write
            value_code, value_type = self.visit(
                value, Access(o.frame, o.env, False, True)
            )
            code += value_code
            code += (
                self.emitter.emitPUTSTATIC(
                    class_name + "/" + ast.fieldname.name, attribute.type, o.frame
                )
                if is_static
                else self.emitter.emitPUTFIELD(
                    class_name + "/" + ast.fieldname.name, attribute.type, o.frame
                )
            )
        else:
            code += (
                self.emitter.emitGETSTATIC(
                    class_name + "/" + ast.fieldname.name, attribute.type, o.frame
                )
                if is_static
                else self.emitter.emitGETFIELD(
                    class_name + "/" + ast.fieldname.name, attribute.type, o.frame
                )
            )
        return code, attribute.type

    def visitArrayCell(self, ast, o):
        value = None
        if type(o) is tuple:
            value = o[1]
            o = o[0]
        code, arr_type = self.visit(
            ast.arr, Access(o.frame, o.env, False, True))
        arr_type = arr_type.eleType
        for i in range(len(ast.idx) - 1):
            idx_code, idx_type = self.visit(
                ast.idx[i], Access(o.frame, o.env, False, True)
            )
            code += idx_code
            code += self.emitter.emitALOAD(arr_type, o.frame)
            arr_type = arr_type.eleType
        idx_code, idx_type = self.visit(
            ast.idx[-1], Access(o.frame, o.env, False, True)
        )
        if o.is_left:

            value_code, value_type = self.visit(
                value, Access(o.frame, o.env, False, True)
            )
            code += idx_code + value_code + \
                self.emitter.emitASTORE(arr_type, o.frame)
        else:
            code += idx_code + self.emitter.emitALOAD(arr_type, o.frame)
        return code, arr_type

    def visitBlock(self, ast, o):
        o.env.enter_scope()
        code = ""
        for inst in ast.inst:
            code += self.visit(inst, o)
        o.env.exit_scope()
        return code

    def visitIf(self, ast, o):
        code, expr_type = self.visit(
            ast.expr, Access(o.frame, o.env, False, True))
        label_false = o.frame.getNewLabel()
        label_end = o.frame.getNewLabel()
        code += self.emitter.emitIFFALSE(label_false, o.frame)
        code += self.visit(ast.thenStmt, o)
        code += self.emitter.emitGOTO(label_end, o.frame)
        code += self.emitter.emitLABEL(label_false, o.frame)
        if ast.elseStmt is not None:
            code += self.visit(ast.elseStmt, o)
        code += self.emitter.emitLABEL(label_end, o.frame)
        return code

    def visitFor(self, ast, o):
        code = ""
        if ast.expr3 is None:
            ast.expr3 = IntLiteral(1)
        expr1_code, _ = self.visit(
            ast.expr1, Access(o.frame, o.env, False, True))
        expr2_code, _ = self.visit(
            ast.expr2, Access(o.frame, o.env, False, True))
        expr3_code, _ = self.visit(
            ast.expr3, Access(o.frame, o.env, False, True))
        id_write_code, _ = self.visit(ast.id, Access(
            o.frame, o.env, True, True))  # Write code
        id_read_code, _ = self.visit(ast.id, Access(
            o.frame, o.env, False, True))  # Read code
        # Virtual stack size at here is 3: exp1, exp2, exp3

        label_start_loop = o.frame.getNewLabel()
        label_check_condition_down = o.frame.getNewLabel()
        label_loop_body = o.frame.getNewLabel()
        label_update_down = o.frame.getNewLabel()
        # Assign init value for scalar variable:
        code += expr1_code
        code += id_write_code

        o.frame.enterLoop()
        # Check condition
        # Check down or up
        code += self.emitter.emitLABEL(label_start_loop, o.frame)
        code += expr1_code
        code += expr2_code
        code += self.emitter.emitREOP(">", IntType(), o.frame)  # Loop down
        code += self.emitter.emitIFTRUE(label_check_condition_down, o.frame)

        # Condition for loop up
        code += id_read_code
        code += expr2_code
        code += self.emitter.emitREOP(">", IntType(), o.frame)
        o.frame.push()
        code += self.emitter.emitIFTRUE(o.frame.getBreakLabel(), o.frame)
        code += self.emitter.emitGOTO(label_loop_body, o.frame)

        # Condition for loop down
        code += self.emitter.emitLABEL(label_check_condition_down, o.frame)
        code += id_read_code
        code += expr2_code
        o.frame.push()
        o.frame.push()
        code += self.emitter.emitREOP("<", IntType(), o.frame)
        code += self.emitter.emitIFTRUE(o.frame.getBreakLabel(), o.frame)

        # Loop body
        code += self.emitter.emitLABEL(label_loop_body, o.frame)
        code += self.visit(ast.loop, o)

        code += self.emitter.emitLABEL(o.frame.getContinueLabel(), o.frame)

        # Update scalar variable
        # Check update is up or down
        code += expr1_code
        code += expr2_code
        o.frame.push()
        o.frame.push()
        code += self.emitter.emitREOP(">", IntType(), o.frame)  # Loop down
        code += self.emitter.emitIFTRUE(label_update_down, o.frame)

        # Update up
        code += id_read_code
        code += expr3_code
        o.frame.push()
        code += self.emitter.emitADDOP("+", IntType(), o.frame)
        code += id_write_code
        code += self.emitter.emitGOTO(label_start_loop, o.frame)

        # Update down
        code += self.emitter.emitLABEL(label_update_down, o.frame)
        code += id_read_code
        code += expr3_code
        o.frame.push()
        code += self.emitter.emitADDOP("-", IntType(), o.frame)
        code += id_write_code
        code += self.emitter.emitGOTO(label_start_loop, o.frame)
        code += self.emitter.emitLABEL(o.frame.getBreakLabel(), o.frame)
        o.frame.exitLoop()
        return code

    def visitBreak(self, ast, o):
        return self.emitter.emitGOTO(o.frame.getBreakLabel(), o.frame)

    def visitContinue(self, ast, o):
        return self.emitter.emitGOTO(o.frame.getContinueLabel(), o.frame)

    def visitReturn(self, ast, o):
        code, expr_type = (
            self.visit(ast.expr, Access(o.frame, o.env, False, True))
            if ast.expr
            else ("", VoidType())
        )
        code += self.emitter.emitRETURN(expr_type, o.frame)
        if self.current_method_return_type is None:
            self.current_method_return_type = expr_type
        return code

    def visitCallExpr(self, ast, o):
        code = ""
        is_static = False
        class_name = None
        obj_code, obj_type = self.visit(ast.obj, o)
        if type(ast.obj) is Id:
            if "$" in ast.method.name:
                is_static = True
                class_name = ast.obj.name
            elif obj_code is None or obj_type is None:  # Not a ID
                is_static = True
                class_name = ast.obj.name
            else:  # A local ID
                is_static = False
                class_name = obj_type.classname.name
                code += obj_code
        else:  # Self literal or expression
            is_static = False
            class_name = obj_type.classname.name
            code += obj_code

        # Find return type
        method = o.env.find_method(class_name, ast.method.name)
        if method is None:
            raise IllegalRuntimeException("Cannot find method!")

        for i in range(len(ast.param)):
            argument_code, argument_type = self.visit(
                ast.param[i], Access(o.frame, o.env, False, True)
            )
            code += argument_code
            if (
                type(argument_type) is IntType
                and type(method.type.partype[i]) is FloatType
            ):
                code += self.emitter.emitI2F(o.frame)

        code += (
            self.emitter.emitINVOKESTATIC(
                class_name + "/" + ast.method.name, method.type, o.frame
            )
            if is_static
            else self.emitter.emitINVOKEVIRTUAL(
                class_name + "/" + ast.method.name, method.type, o.frame
            )
        )
        return code, method.type.rettype

    def visitCallStmt(self, ast, o):
        code = ""
        is_static = False
        class_name = None
        obj_code, obj_type = self.visit(ast.obj, o)
        if type(ast.obj) is Id:
            if "$" in ast.method.name:
                is_static = True
                class_name = ast.obj.name
            elif obj_code is None or obj_type is None:  # Not a ID
                is_static = True
                class_name = ast.obj.name
            else:  # A local ID
                is_static = False
                class_name = obj_type.classname.name
                code += obj_code
        else:  # Self literal or expression
            is_static = False
            class_name = obj_type.classname.name
            code += obj_code

        # Find return type
        method = o.env.find_method(class_name, ast.method.name)
        if method is None:
            raise IllegalRuntimeException("Cannot find method!")
        for i in range(len(ast.param)):
            argument_code, argument_type = self.visit(
                ast.param[i], Access(o.frame, o.env, False, True)
            )
            code += argument_code
            if (
                type(argument_type) is IntType
                and type(method.type.partype[i]) is FloatType
            ):
                code += self.emitter.emitI2F(o.frame)
        code += (
            self.emitter.emitINVOKESTATIC(
                class_name + "/" + ast.method.name, method.type, o.frame
            )
            if is_static
            else self.emitter.emitINVOKEVIRTUAL(
                class_name + "/" + ast.method.name, method.type, o.frame
            )
        )
        if type(method.type.rettype) is not VoidType:
            code += self.emitter.emitPOP(o.frame)
        return code

    def visitId(
        self, ast, o
    ):  # ID only for local variable, attribute or method use access
        local = o.env.find_local(ast.name)
        if local is None:
            return None, None
        # Write
        if o.is_left:
            return (
                self.emitter.emitWRITEVAR(
                    ast.name, local.type, local.index, o.frame),
                local.type,
            )
        # Read
        return (
            self.emitter.emitREADVAR(
                ast.name, local.type, local.index, o.frame),
            local.type,
        )

    def visitIntLiteral(self, ast, o):
        return self.emitter.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emitter.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        return (
            self.emitter.emitPUSHCONST(str(ast.value), BoolType(), o.frame),
            BoolType(),
        )

    def visitStringLiteral(self, ast, o):
        return (
            self.emitter.emitPUSHCONST(
                '"' + str(ast.value) + '"', StringType(), o.frame
            ),
            StringType(),
        )

    def visitArrayLiteral(self, ast, o):
        code = ""
        element_type = None
        o.frame.push()  # Virtual emit array, need emit after because we don't know type of element at this line
        for i in range(len(ast.value)):
            code += self.emitter.emitDUP(o.frame)
            code += self.emitter.emitPUSHICONST(i, o.frame)
            element_code, element_type = self.visit(ast.value[i], o)
            code += element_code
            code += self.emitter.emitASTORE(element_type, o.frame)
        o.frame.pop()  # Reset frame
        array_type = ArrayType(len(ast.value), element_type)
        code = self.emitter.emitARRAY(array_type, o.frame) + code
        return code, array_type

    def visitNullLiteral(self, ast, o):
        return self.emitter.emitNULL(o.frame), NullLiteral()

    def visitSelfLiteral(self, ast, o):
        return self.emitter.emitTHIS(o.frame), ClassType(Id(self.class_name))
