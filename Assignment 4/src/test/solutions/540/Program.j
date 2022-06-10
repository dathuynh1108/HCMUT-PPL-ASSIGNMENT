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
.var 1 is a [F from Label0 to Label1
	iconst_4
	newarray float
	dup
	iconst_0
	iconst_1
	i2f
	fastore
	dup
	iconst_1
	ldc 2.0
	fastore
	dup
	iconst_2
	iconst_3
	i2f
	fastore
	dup
	iconst_3
	ldc 4.0
	fastore
	astore_1
	aload_1
	iconst_0
	faload
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method
