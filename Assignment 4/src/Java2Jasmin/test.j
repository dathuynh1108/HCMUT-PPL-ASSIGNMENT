;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Mon May 30 10:57:09 ICT 2022

.source test.java
.class public test
.super java/lang/Object

.field public static a I
.field public b I
.field private c I

.method  <init>(I)V
.limit stack 2
.limit locals 2
.var 0 is this Ltest; from Label0 to Label1
.var 1 is arg0 I from Label0 to Label1

Label0:
.line 6
	aload_0
	invokespecial java/lang/Object/<init>()V
.line 4
	aload_0
	iconst_1
	putfield test.b I
.line 5
	aload_0
	iconst_1
	putfield test.c I
Label1:
.line 6
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 0
.limit locals 1
.var 0 is arg0 [Ljava/lang/String; from Label0 to Label0

Label0:
.line 8
	return

.end method

.method public instance_method()I
.limit stack 4
.limit locals 3
.var 0 is this Ltest; from Label1 to Label2

Label1:
.line 10
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	astore_1
.line 11
	iconst_1
	istore_2
.line 12
	iload_2
	iconst_1
	if_icmpne Label0
	iconst_1
	ireturn
Label0:
.line 13
	iconst_2
Label2:
	ireturn

.end method

.method public static static_method()V
.limit stack 0
.limit locals 0

.line 15
	return

.end method

.method static <clinit>()V
.limit stack 1
.limit locals 0

.line 3
	bipush 100
	putstatic test.a I
	return

.end method
