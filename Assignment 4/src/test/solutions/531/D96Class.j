.source D96Class.java
.class public D96Class
.super java/lang/Object
.field x I
.field y F
.field static $x I
.field static $y F

.method public <init>(I)V
.var 0 is this LD96Class; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_1
	putfield D96Class.x I
	aload_0
	iconst_1
	i2f
	putfield D96Class.y F
	aload_0
	bipush 100
	putfield D96Class/x I
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
	iconst_1
	putfield D96Class.x I
	aload_0
	iconst_1
	i2f
	putfield D96Class.y F
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_1
	putstatic D96Class.$x I
	iconst_1
	i2f
	putstatic D96Class.$y F
Label1:
	return
.limit stack 1
.limit locals 0
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
	aload_1
	getfield D96Class/x I
	invokestatic io/putInt(I)V
	aload_2
	getfield D96Class/x I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method
