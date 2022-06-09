;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Tue Jun 07 11:09:26 ICT 2022

.source D96Class.java
.class public D96Class
.super java/lang/Object

.field public static a I
.field public b I
.field private c I

.method public <init>()V
.limit stack 2
.limit locals 1
.var 0 is this LD96Class; from Label0 to Label1

Label0:
.line 2
	aload_0
	invokespecial java/lang/Object/<init>()V
.line 4
	aload_0
	iconst_1
	putfield D96Class.b I
.line 5
	aload_0
	iconst_1
	putfield D96Class.c I
Label1:
	return

.end method

.method static method()I
.limit stack 1
.limit locals 0

.line 7
	iconst_1
	ireturn

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 4
.limit locals 2
.var 0 is arg0 [Ljava/lang/String; from Label0 to Label1

Label0:
.line 10
	iconst_3
	newarray float
	dup
	iconst_0
	fconst_1
	fastore
	dup
	iconst_1
	fconst_2
	fastore
	dup
	iconst_2
	ldc 3.0
	fastore
	astore_1
Label1:
.line 11
	return

.end method

.method static <clinit>()V
.limit stack 1
.limit locals 0

.line 3
	bipush 100
	putstatic D96Class.a I
	return

.end method
