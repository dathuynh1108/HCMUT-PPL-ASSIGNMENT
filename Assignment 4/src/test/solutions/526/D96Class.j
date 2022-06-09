.source D96Class.java
.class public D96Class
.super java/lang/Object
.field static $a I
.field static $b I
.field static $x F
.field static $y F

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

.method public static <clinit>()V
Label0:
	iconst_1
	putstatic D96Class.$a I
	iconst_1
	putstatic D96Class.$b I
	iconst_1
	i2f
	putstatic D96Class.$x F
	ldc 1.0
	putstatic D96Class.$y F
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public method()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is x F from Label0 to Label1
	iconst_1
	i2f
	fstore_3
.var 4 is y F from Label0 to Label1
	ldc 1.0
	fstore 4
	getstatic D96Class/$a I
	iload_2
	iadd
	invokestatic io/writeInt(I)V
	getstatic D96Class/$a I
	iload_1
	iadd
	invokestatic io/writeInt(I)V
	getstatic D96Class/$b I
	iload_2
	iadd
	invokestatic io/writeInt(I)V
	getstatic D96Class/$a I
	iload_2
	iadd
	invokestatic io/writeInt(I)V
	getstatic D96Class/$a I
	getstatic D96Class/$b I
	iadd
	invokestatic io/writeInt(I)V
	getstatic D96Class/$a I
	i2f
	fload_3
	fadd
	invokestatic io/writeFloat(F)V
	getstatic D96Class/$a I
	i2f
	fload 4
	fadd
	invokestatic io/writeFloat(F)V
	getstatic D96Class/$x F
	iload_1
	i2f
	fadd
	invokestatic io/writeFloat(F)V
	getstatic D96Class/$x F
	iload_2
	i2f
	fadd
	invokestatic io/writeFloat(F)V
	getstatic D96Class/$x F
	getstatic D96Class/$y F
	fadd
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is d LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_1
	aload_1
	invokevirtual D96Class/method()V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
