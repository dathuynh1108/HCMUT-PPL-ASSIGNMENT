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
	ldc 1.1
	invokestatic io/putFloatLn(F)V
	ldc 1.1
	invokestatic io/putFloat(F)V
	ldc 1.1
	ldc 1.1
	fadd
	invokestatic io/putFloat(F)V
	ldc 1.1
	ldc 1.1
	fsub
	invokestatic io/putFloat(F)V
	ldc 1.1
	ldc 1.1
	fmul
	invokestatic io/putFloat(F)V
	ldc 1.1
	ldc 1.1
	fdiv
	invokestatic io/putFloat(F)V
	iconst_1
	i2f
	invokestatic io/putFloatLn(F)V
	iconst_1
	i2f
	invokestatic io/putFloat(F)V
	iconst_1
	iconst_1
	iadd
	i2f
	invokestatic io/putFloat(F)V
	iconst_1
	iconst_1
	isub
	i2f
	invokestatic io/putFloat(F)V
	iconst_1
	iconst_1
	imul
	i2f
	invokestatic io/putFloat(F)V
	iconst_1
	i2f
	iconst_1
	i2f
	fdiv
	invokestatic io/putFloat(F)V
	ldc 1.1
	iconst_1
	i2f
	fadd
	invokestatic io/putFloat(F)V
	ldc 1.1
	iconst_1
	i2f
	fsub
	invokestatic io/putFloat(F)V
	ldc 1.1
	iconst_1
	i2f
	fmul
	invokestatic io/putFloat(F)V
	ldc 1.1
	iconst_1
	i2f
	fdiv
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
