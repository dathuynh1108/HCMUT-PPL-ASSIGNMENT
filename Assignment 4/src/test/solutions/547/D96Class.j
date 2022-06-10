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
.var 1 is o LObject; from Label0 to Label1
	new Object
	dup
	invokespecial Object/<init>()V
	astore_1
	aload_1
	getfield Object/a I
	invokestatic io/writeInt(I)V
	getstatic Object/$a I
	invokestatic io/writeInt(I)V
	aload_1
	invokevirtual Object/method()I
	invokestatic io/writeInt(I)V
	invokestatic Object/$method()I
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
