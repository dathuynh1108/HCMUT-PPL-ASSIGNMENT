.source Program.java
.class public Program
.super java/lang/Object
.field static $a I
.field static $b I
.field static $x F
.field static $y F

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
	iconst_1
	putstatic Program.$a I
	iconst_1
	putstatic Program.$b I
	iconst_1
	i2f
	putstatic Program.$x F
	ldc 1.0
	putstatic Program.$y F
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public method()V
.var 0 is this LProgram; from Label0 to Label1
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
	getstatic Program/$a I
	iload_2
	iadd
	invokestatic io/writeInt(I)V
	getstatic Program/$a I
	iload_1
	iadd
	invokestatic io/writeInt(I)V
	getstatic Program/$b I
	iload_2
	iadd
	invokestatic io/writeInt(I)V
	getstatic Program/$a I
	iload_2
	iadd
	invokestatic io/writeInt(I)V
	getstatic Program/$a I
	getstatic Program/$b I
	iadd
	invokestatic io/writeInt(I)V
	getstatic Program/$a I
	i2f
	fload_3
	fadd
	invokestatic io/writeFloat(F)V
	getstatic Program/$a I
	i2f
	fload 4
	fadd
	invokestatic io/writeFloat(F)V
	getstatic Program/$x F
	iload_1
	i2f
	fadd
	invokestatic io/writeFloat(F)V
	getstatic Program/$x F
	iload_2
	i2f
	fadd
	invokestatic io/writeFloat(F)V
	getstatic Program/$x F
	getstatic Program/$y F
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
.var 1 is d LProgram; from Label0 to Label1
	new Program
	dup
	invokespecial Program/<init>()V
	astore_1
	aload_1
	invokevirtual Program/method()V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
