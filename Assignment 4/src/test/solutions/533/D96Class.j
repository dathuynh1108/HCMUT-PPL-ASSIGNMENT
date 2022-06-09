.source D96Class.java
.class public D96Class
.super java/lang/Object
.field x I
.field y F
.field static $x I
.field static $y F

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 123
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

.method public method_1()LD96Class;
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	areturn
Label1:
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
	aload_1
	invokevirtual D96Class/method_1()LD96Class;
	getfield D96Class/x I
	invokestatic io/writeInt(I)V
	aload_1
	invokevirtual D96Class/method_1()LD96Class;
	invokevirtual D96Class/method_1()LD96Class;
	invokevirtual D96Class/method_1()LD96Class;
	getfield D96Class/y F
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
