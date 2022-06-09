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
.var 1 is a [[I from Label0 to Label1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	aastore
	dup
	iconst_1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	aastore
	astore_1
	aload_1
	iconst_1
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 6
	iastore
	dup
	iconst_1
	bipush 7
	iastore
	dup
	iconst_2
	bipush 8
	iastore
	dup
	iconst_3
	bipush 9
	iastore
	dup
	iconst_4
	bipush 10
	iastore
	aastore
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
.var 4 is $protect_expr2 I from Label0 to Label1
.var 5 is $protect_expr3 I from Label0 to Label1
	iconst_1
	istore 4
	iconst_1
	istore 5
	iconst_0
	istore_2
Label2:
	iconst_0
	iload 4
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label3
	iload_2
	iload 4
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label7
	goto Label4
Label3:
	iload_2
	iload 4
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label7
Label4:
.var 6 is $protect_expr2 I from Label0 to Label1
.var 7 is $protect_expr3 I from Label0 to Label1
	iconst_4
	istore 6
	iconst_1
	istore 7
	iconst_0
	istore_3
Label14:
	iconst_0
	iload 6
	if_icmple Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label15
	iload_3
	iload 6
	if_icmple Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label19
	goto Label16
Label15:
	iload_3
	iload 6
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label19
Label16:
	aload_1
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/writeInt(I)V
Label18:
	iconst_0
	iload 6
	if_icmple Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifgt Label17
	iload_3
	iload 7
	iadd
	istore_3
	goto Label14
Label17:
	iload_3
	iload 7
	isub
	istore_3
	goto Label14
Label19:
Label6:
	iconst_0
	iload 4
	if_icmple Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifgt Label5
	iload_2
	iload 5
	iadd
	istore_2
	goto Label2
Label5:
	iload_2
	iload 5
	isub
	istore_2
	goto Label2
Label7:
Label1:
	return
.limit stack 7
.limit locals 8
.end method
