## Instance Constructor - <init>
- <init> khởi tạo đối tượng cần dup vì <init> là Void, không trả về đối tượng được khởi tạo và là instance_method
--> Địa chỉ đối tượng nằm ở đỉnh stack bị mất sau khi chạy init 
--> Nếu muốn có một đối tượng được trả về sau khi init, cần dup địa chỉ đối tượng đó (của cùng 1 đối tượng)
--> Do cùng là địa chỉ 1 đối tượng nên mọi thay đổi trong this của đối tượng tương ứng địa chỉ dup cũng sẽ thay đổi  chính đối tượng tương ứng địa chỉ nằm ở đỉnh stack (new Class) sau khi chạy hàm init

new Class   # Address   |   Cùng 1 đối tượng với dup
dup         # Address   |
invokespecial <init>
--> Sau khi chạy dup mất (init là void type), nhưng mọi thay đổi của dup đều sẽ phản ánh ở new Class vì là cùng 1 đối tượng

- Tương tự đối với khởi tạo Array 
----------------------------------------------------------------------------------------------------------------------------
## Class Constructor - <clinit>
- Khởi tạo các static attribute
- Tự chạy, không cần gọi thủ công như <init>
----------------------------------------------------------------------------------------------------------------------------

class Get_class_enviroment_visitor(BaseVisitor):
    def __init__(self, ast, env, dir_):
        self.ast = ast
        self.env = env
        self.path = dir_
        self.class_name = None
    
    def visitProgram(self, ast, env):
        env = []
        for class_decl in ast.decl: self.visit(class_decl, env)
        return env
    def visitClassDecl(self, ast, env):
        self.class_name = ast.classname.name
        for mem in ast.mem: env = [self.visit(mem, env)] + env
    
    def visitAttributeDecl(self, ast, env):
        attribute_name = ast.decl.variable.name if isinstance(ast.decl, VarDecl) else ast.decl.constant.name
        attribute_type = ast.decl.varType if isinstance(ast.decl, VarDecl) else ast.decl.constType
        init_value = ast.decl.varInit if isinstance(ast.decl, VarDecl) else ast.decl.value
        return Symbol(attribute_name, attribute_type, Class_name(self.class_name, ast.kind), init_value)
    
    def visitMethodDecl(self, ast, env):
        return Symbol(ast.name.name, MType([param.varType for param in ast.param], self.current_method_return_type), Class_name(self.class_name, ast.kind))
