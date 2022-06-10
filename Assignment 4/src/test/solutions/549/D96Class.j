.source D96Class.java
.class public D96Class
.super Object
.field a I
.field static $a I

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial Object/<init>()V
	aload_0
	iconst_2
	putfield D96Class.a I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_2
	putstatic D96Class.$a I
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public method()I
.var 0 is this LD96Class; from Label0 to Label1
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
.var 1 is o LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_1
	aload_1
	getfield D96Class/a I
	invokestatic io/writeInt(I)V
	getstatic D96Class/$a I
	invokestatic io/writeInt(I)V
	aload_1
	invokevirtual D96Class/method()I
	invokestatic io/writeInt(I)V
	invokestatic D96Class/$method()I
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
