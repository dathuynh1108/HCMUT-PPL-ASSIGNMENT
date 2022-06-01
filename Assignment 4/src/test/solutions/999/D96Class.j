.source D96Class.java
.class public D96Class
.super java/lang/Object
.field static $true Z
.field static $false Z

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
	iconst_1
	putstatic D96Class.$true Z
	iconst_0
	putstatic D96Class.$false Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic D96Class/$true Z
	getstatic D96Class/$false Z
	iand
	invokestatic io/putBool(Z)V
	getstatic D96Class/$true Z
	iconst_1
	iand
	invokestatic io/putBool(Z)V
	getstatic D96Class/$true Z
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	getstatic D96Class/$false Z
	iand
	invokestatic io/putBool(Z)V
	getstatic D96Class/$true Z
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iconst_1
	iand
	invokestatic io/putBool(Z)V
	getstatic D96Class/$true Z
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBool(Z)V
	getstatic D96Class/$false Z
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBool(Z)V
	getstatic D96Class/$true Z
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBool(Z)V
	getstatic D96Class/$false Z
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 7
.limit locals 1
.end method
