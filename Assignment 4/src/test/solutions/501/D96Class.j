.source D96Class.java
.class public D96Class
.super java/lang/Object

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <clinit>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	invokestatic io/putInt(I)V
	iconst_1
	invokestatic io/putIntLn(I)V
	iconst_1
	iconst_1
	iadd
	invokestatic io/putIntLn(I)V
	iconst_1
	iconst_1
	isub
	invokestatic io/putIntLn(I)V
	iconst_1
	iconst_1
	imul
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
