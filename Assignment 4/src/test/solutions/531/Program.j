.source Program.java
.class public Program
.super java/lang/Object
.field x I
.field y F
.field static $x I
.field static $y F

.method public <init>(I)V
.var 0 is this LProgram; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_1
	putfield Program.x I
	aload_0
	iconst_1
	i2f
	putfield Program.y F
	aload_0
	bipush 100
	putfield Program/x I
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_1
	putfield Program.x I
	aload_0
	iconst_1
	i2f
	putfield Program.y F
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_1
	putstatic Program.$x I
	iconst_1
	i2f
	putstatic Program.$y F
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x LProgram; from Label0 to Label1
	new Program
	dup
	invokespecial Program/<init>()V
	astore_1
.var 2 is y LProgram; from Label0 to Label1
	new Program
	dup
	iconst_1
	invokespecial Program/<init>(I)V
	astore_2
	aload_1
	getfield Program/x I
	invokestatic io/writeInt(I)V
	aload_2
	getfield Program/x I
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method
