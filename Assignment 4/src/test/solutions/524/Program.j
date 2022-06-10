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
.var 1 is a I from Label0 to Label1
	iconst_2
	istore_1
.var 2 is b I from Label0 to Label1
	bipush 10
	istore_2
	iload_1
	iload_2
	isub
	i2f
	iload_2
	i2f
	iload_1
	i2f
	fdiv
	iload_2
	i2f
	fmul
	fadd
	ldc 0.1
	fadd
	invokestatic io/writeFloat(F)V
	iload_1
	iload_2
	iload_1
	imul
	iload_2
	irem
	iadd
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method
