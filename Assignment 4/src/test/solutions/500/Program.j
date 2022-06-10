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
	ldc "Huynh Thanh Dat\n"
	invokestatic io/writeStr(Ljava/lang/String;)V
	ldc "1910110\n"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
