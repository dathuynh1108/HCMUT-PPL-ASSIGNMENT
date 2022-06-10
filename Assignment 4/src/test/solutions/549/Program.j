.source Program.java
.class public Program
.super Object
.field a I
.field static $a I

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial Object/<init>()V
	aload_0
	iconst_2
	putfield Program.a I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_2
	putstatic Program.$a I
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public method()I
.var 0 is this LProgram; from Label0 to Label1
Label0:
	iconst_2
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static $method()I
Label0:
	iconst_2
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is o LProgram; from Label0 to Label1
	new Program
	dup
	invokespecial Program/<init>()V
	astore_1
	aload_1
	getfield Program/a I
	invokestatic io/writeInt(I)V
	getstatic Program/$a I
	invokestatic io/writeInt(I)V
	aload_1
	invokevirtual Program/method()I
	invokestatic io/writeInt(I)V
	invokestatic Program/$method()I
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
