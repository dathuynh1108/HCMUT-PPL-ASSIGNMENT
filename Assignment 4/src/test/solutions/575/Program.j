.source Program.java
.class public Program
.super java/lang/Object

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
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

.method public sort([II)V
.var 0 is this LProgram; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
.var 2 is size I from Label0 to Label1
Label0:
.var 3 is i I from Label0 to Label1
.var 4 is j I from Label0 to Label1
.var 5 is $protect_expr2 I from Label0 to Label1
.var 6 is $protect_expr3 I from Label0 to Label1
	iload_2
	iconst_2
	isub
	istore 5
	iconst_1
	istore 6
	iconst_0
	istore_3
Label2:
	iconst_0
	iload 5
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label3
	iload_3
	iload 5
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label7
	goto Label4
Label3:
	iload_3
	iload 5
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label7
Label4:
.var 7 is min_index I from Label0 to Label1
	iload_3
	istore 7
.var 8 is min I from Label0 to Label1
	aload_1
	iload_3
	iaload
	istore 8
.var 9 is $protect_expr2 I from Label0 to Label1
.var 10 is $protect_expr3 I from Label0 to Label1
	iload_2
	iconst_1
	isub
	istore 9
	iconst_1
	istore 10
	iload_3
	iconst_1
	iadd
	istore 4
Label14:
	iload_3
	iconst_1
	iadd
	iload 9
	if_icmple Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label15
	iload 4
	iload 9
	if_icmple Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label19
	goto Label16
Label15:
	iload 4
	iload 9
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label19
Label16:
	aload_1
	iload 4
	iaload
	aload_1
	iload 7
	iaload
	if_icmpge Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label28
	iload 4
	istore 7
	aload_1
	iload 4
	iaload
	istore 8
	goto Label29
Label28:
Label29:
Label18:
	iload_3
	iconst_1
	iadd
	iload 9
	if_icmple Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifgt Label17
	iload 4
	iload 10
	iadd
	istore 4
	goto Label14
Label17:
	iload 4
	iload 10
	isub
	istore 4
	goto Label14
Label19:
.var 11 is temp I from Label0 to Label1
	aload_1
	iload_3
	iaload
	istore 11
	aload_1
	iload_3
	aload_1
	iload 7
	iaload
	iastore
	aload_1
	iload 7
	iload 11
	iastore
Label6:
	iconst_0
	iload 5
	if_icmple Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifgt Label5
	iload_3
	iload 6
	iadd
	istore_3
	goto Label2
Label5:
	iload_3
	iload 6
	isub
	istore_3
	goto Label2
Label7:
.var 12 is $protect_expr2 I from Label0 to Label1
.var 13 is $protect_expr3 I from Label0 to Label1
	iload_2
	iconst_1
	isub
	istore 12
	iconst_1
	istore 13
	iconst_0
	istore_3
Label34:
	iconst_0
	iload 12
	if_icmple Label40
	iconst_1
	goto Label41
Label40:
	iconst_0
Label41:
	ifgt Label35
	iload_3
	iload 12
	if_icmple Label42
	iconst_1
	goto Label43
Label42:
	iconst_0
Label43:
	ifgt Label39
	goto Label36
Label35:
	iload_3
	iload 12
	if_icmpge Label44
	iconst_1
	goto Label45
Label44:
	iconst_0
Label45:
	ifgt Label39
Label36:
	aload_1
	iload_3
	iaload
	invokestatic io/writeInt(I)V
Label38:
	iconst_0
	iload 12
	if_icmple Label46
	iconst_1
	goto Label47
Label46:
	iconst_0
Label47:
	ifgt Label37
	iload_3
	iload 13
	iadd
	istore_3
	goto Label34
Label37:
	iload_3
	iload 13
	isub
	istore_3
	goto Label34
Label39:
Label1:
	return
.limit stack 4
.limit locals 14
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is o LProgram; from Label0 to Label1
	new Program
	dup
	invokespecial Program/<init>()V
	astore_1
	aload_1
	bipush 10
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 9
	iastore
	dup
	iconst_2
	bipush 8
	iastore
	dup
	iconst_3
	bipush 7
	iastore
	dup
	iconst_4
	bipush 6
	iastore
	dup
	iconst_5
	iconst_5
	iastore
	dup
	bipush 6
	iconst_4
	iastore
	dup
	bipush 7
	iconst_3
	iastore
	dup
	bipush 8
	iconst_2
	iastore
	dup
	bipush 9
	iconst_1
	iastore
	bipush 10
	invokevirtual Program/sort([II)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method
