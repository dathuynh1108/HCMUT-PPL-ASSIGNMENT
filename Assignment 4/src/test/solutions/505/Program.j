.source Program.java
.class public Program
.super java/lang/Object
.field a Ljava/lang/String;

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc "Huynh Thanh Dat"
	putfield Program.a Ljava/lang/String;
Label1:
	return
.limit stack 2
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
.var 1 is a Ljava/lang/String; from Label0 to Label1
	ldc "Huynh Thanh Dat"
	astore_1
	aload_1
	invokestatic io/writeStr(Ljava/lang/String;)V
.var 2 is d LProgram; from Label0 to Label1
	new Program
	dup
	invokespecial Program/<init>()V
	astore_2
	aload_2
	getfield Program/a Ljava/lang/String;
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method
