.source Program.java
.class public Program
.super java/lang/Object
.field static $a F
.field a F

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_1
	i2f
	putfield Program.a F
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_1
	i2f
	putstatic Program.$a F
Label1:
	return
.limit stack 1
.limit locals 0
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
	iconst_2
	i2f
	putfield Program/a F
	aload_1
	getfield Program/a F
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
