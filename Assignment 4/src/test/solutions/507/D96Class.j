.source D96Class.java
.class public D96Class
.super java/lang/Object
.field a I
.field static $a I

.method public <init>(I)V
.var 0 is this LD96Class; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield D96Class.a I
	ldc "<init>"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield D96Class.a I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public <clinit>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	iconst_1
	putstatic D96Class.$a I
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_1
.var 2 is y LD96Class; from Label0 to Label1
	new D96Class
	dup
	iconst_1
	invokespecial D96Class/<init>(I)V
	astore_2
Label1:
	return
.limit stack 3
.limit locals 3
.end method
