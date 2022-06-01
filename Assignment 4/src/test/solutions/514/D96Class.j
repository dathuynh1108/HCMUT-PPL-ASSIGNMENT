.source D96Class.java
.class public D96Class
.super java/lang/Object

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

.method public <clinit>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "False"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label5
Label4:
	iconst_1
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "True"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label9
Label8:
	ldc "False"
	invokestatic io/putString(Ljava/lang/String;)V
Label9:
Label5:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
