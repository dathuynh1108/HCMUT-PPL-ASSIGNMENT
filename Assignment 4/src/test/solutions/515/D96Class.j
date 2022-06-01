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

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
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
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "False"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label9
Label8:
	iconst_1
	iconst_4
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	ldc "False"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label13
Label12:
	iconst_1
	iconst_1
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	ldc "True"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label17
Label16:
Label17:
Label13:
Label9:
Label5:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
