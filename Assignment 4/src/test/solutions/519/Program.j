.source Program.java
.class public Program
.super java/lang/Object

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	sipush 1000
	istore_1
.var 2 is a I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is b I from Label0 to Label1
	bipush 10
	istore_3
.var 4 is $protect_expr2 I from Label0 to Label1
.var 5 is $protect_expr3 I from Label0 to Label1
	iload_3
	istore 4
	iconst_1
	istore 5
	iload_2
	istore_1
Label2:
	iload_2
	iload 4
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label3
	iload_1
	iload 4
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label7
	goto Label4
Label3:
	iload_1
	iload 4
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label7
Label4:
	iload_1
	invokestatic io/writeInt(I)V
	iload_2
	iconst_1
	isub
	istore_2
	iload_3
	iconst_1
	isub
	istore_3
Label6:
	iload_2
	iload 4
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label5
	iload_1
	iload 5
	iadd
	istore_1
	goto Label2
Label5:
	iload_1
	iload 5
	isub
	istore_1
	goto Label2
Label7:
Label1:
	return
.limit stack 3
.limit locals 6
.end method
