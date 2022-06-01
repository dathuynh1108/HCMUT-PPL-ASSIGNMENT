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
	ldc "Huynh Thanh Dat"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	ldc "1910110"
	invokestatic io/putString(Ljava/lang/String;)V
	invokestatic io/putLn()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
