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

.method public method_1()LProgram;
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	areturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	astore_1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	ineg
	iastore
	dup
	iconst_1
	iconst_2
	ineg
	iastore
	dup
	iconst_2
	iconst_3
	ineg
	iastore
	dup
	iconst_3
	iconst_4
	ineg
	iastore
	dup
	iconst_4
	iconst_5
	ineg
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
.var 3 is $protect_expr2 I from Label0 to Label1
.var 4 is $protect_expr3 I from Label0 to Label1
	iconst_4
	istore_3
	iconst_1
	istore 4
	iconst_0
	istore_2
Label2:
	iconst_0
	iload_3
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label3
	iload_2
	iload_3
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label7
	goto Label4
Label3:
	iload_2
	iload_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label7
Label4:
	aload_1
	iload_2
	iaload
	invokestatic io/writeInt(I)V
Label6:
	iconst_0
	iload_3
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label5
	iload_2
	iload 4
	iadd
	istore_2
	goto Label2
Label5:
	iload_2
	iload 4
	isub
	istore_2
	goto Label2
Label7:
Label1:
	return
.limit stack 4
.limit locals 5
.end method
