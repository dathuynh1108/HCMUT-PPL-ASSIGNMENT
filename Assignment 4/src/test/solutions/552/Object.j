.source Object.java
.class public Object
.super java/lang/Object
.field a I

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
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public method(LObject;)I
.var 0 is this LObject; from Label0 to Label1
.var 1 is o LObject; from Label0 to Label1
Label0:
	aload_0
	getfield Object/a I
	ireturn
Label1:
.limit stack 1
.limit locals 2
.end method
