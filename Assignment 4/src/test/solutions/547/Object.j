.source Object.java
.class public Object
.super java/lang/Object
.field a I
.field static $a I

.method public <init>()V
.var 0 is this LObject; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_1
	putfield Object.a I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_1
	putstatic Object.$a I
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public method()I
.var 0 is this LObject; from Label0 to Label1
Label0:
	aload_0
	getfield Object/a I
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static $method()I
Label0:
	getstatic Object/$a I
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method
