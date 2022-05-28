.source D96Class.java
.class public D96Class
.super java/lang/Object
.field static $a I
.field a I

.method public method(ILjava/lang/String;)V
.var 0 is this LD96Class; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y Ljava/lang/String; from Label0 to Label1
Label0:
.var 3 is a I from Label0 to Label1
	iconst_1
	ineg
None.var 4 is b I from Label0 to Label1
	iconst_1
NoneLabel1:
	return
.limit stack 2
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_1
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
