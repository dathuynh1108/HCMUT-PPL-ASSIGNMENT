;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Fri Jun 10 12:54:33 ICT 2022

.source D96Class.java
.class public D96Class
.super java/lang/Object


.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this LD96Class; from Label0 to Label1

Label0:
.line 2
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 2
.limit locals 2
.var 0 is arg0 [Ljava/lang/String; from Label0 to Label1

Label0:
.line 4
	new Dog
	dup
	invokespecial Dog/<init>()V
	astore_1
.line 5
	aload_1
	invokevirtual Animal/eat()V
Label1:
.line 6
	return

.end method
