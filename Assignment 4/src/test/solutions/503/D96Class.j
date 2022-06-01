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
	invokestatic io/putBool(Z)V
	iconst_0
	invokestatic io/putBoolLn(Z)V
	iconst_1
	invokestatic io/putBool(Z)V
	iconst_0
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_1
	iand
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_0
	iand
	invokestatic io/putBool(Z)V
	iconst_0
	iconst_1
	iand
	invokestatic io/putBool(Z)V
	iconst_0
	iconst_0
	iand
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_1
	ior
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_0
	ior
	invokestatic io/putBool(Z)V
	iconst_0
	iconst_1
	ior
	invokestatic io/putBool(Z)V
	iconst_0
	iconst_0
	ior
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_2
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_2
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_2
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_2
	if_icmpeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBool(Z)V
	ldc 1.1
	iconst_2
	i2f
	fcmpl
	ifle Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBool(Z)V
	ldc 1.1
	iconst_2
	i2f
	fcmpl
	iflt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	invokestatic io/putBool(Z)V
	ldc 1.1
	iconst_2
	i2f
	fcmpl
	ifge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	invokestatic io/putBool(Z)V
	ldc 1.1
	iconst_2
	i2f
	fcmpl
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	invokestatic io/putBool(Z)V
	ldc 1.1
	iconst_2
	i2f
	fcmpl
	ifne Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	invokestatic io/putBool(Z)V
	ldc 1.1
	iconst_2
	i2f
	fcmpl
	ifeq Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	invokestatic io/putBool(Z)V
	ldc 1.1
	ldc 2.1
	fcmpl
	ifle Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	invokestatic io/putBool(Z)V
	ldc 1.1
	ldc 2.1
	fcmpl
	iflt Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	invokestatic io/putBool(Z)V
	ldc 1.1
	ldc 2.1
	fcmpl
	ifge Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	invokestatic io/putBool(Z)V
	ldc 1.1
	ldc 2.1
	fcmpl
	ifgt Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	invokestatic io/putBool(Z)V
	ldc 1.1
	ldc 2.1
	fcmpl
	ifne Label34
	iconst_1
	goto Label35
Label34:
	iconst_0
Label35:
	invokestatic io/putBool(Z)V
	ldc 1.1
	ldc 2.1
	fcmpl
	ifeq Label36
	iconst_1
	goto Label37
Label36:
	iconst_0
Label37:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
