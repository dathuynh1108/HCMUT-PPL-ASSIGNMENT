.source Linked_list.java
.class public Linked_list
.super java/lang/Object
.field head LNode;
.field tail LNode;
.field size I

.method public <init>()V
.var 0 is this LLinked_list; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aconst_null
	putfield Linked_list.head LNode;
	aload_0
	aconst_null
	putfield Linked_list.tail LNode;
	aload_0
	iconst_0
	putfield Linked_list.size I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public insert(LNode;)V
.var 0 is this LLinked_list; from Label0 to Label1
.var 1 is node LNode; from Label0 to Label1
Label0:
	aload_0
	getfield Linked_list/size I
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	aload_0
	aload_1
	putfield Linked_list/head LNode;
	aload_0
	aload_1
	putfield Linked_list/tail LNode;
	aload_0
	aload_0
	getfield Linked_list/size I
	iconst_1
	iadd
	putfield Linked_list/size I
	goto Label5
Label4:
	aload_0
	getfield Linked_list/tail LNode;
	aload_1
	putfield Node/next LNode;
	aload_0
	aload_1
	putfield Linked_list/tail LNode;
	aload_0
	aload_0
	getfield Linked_list/size I
	iconst_1
	iadd
	putfield Linked_list/size I
Label5:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public delete(I)V
.var 0 is this LLinked_list; from Label0 to Label1
.var 1 is data I from Label0 to Label1
Label0:
.var 2 is i I from Label0 to Label1
.var 3 is current LNode; from Label0 to Label1
	aload_0
	getfield Linked_list/head LNode;
	astore_3
	aload_3
	getfield Node/data I
	iload_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	aload_0
	aload_0
	getfield Linked_list/head LNode;
	getfield Node/next LNode;
	putfield Linked_list/head LNode;
	aload_0
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	putfield Linked_list/size I
	return
	goto Label5
Label4:
Label5:
.var 4 is $protect_expr2 I from Label0 to Label1
.var 5 is $protect_expr3 I from Label0 to Label1
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	istore 4
	iconst_1
	istore 5
	iconst_1
	istore_2
Label6:
	iconst_1
	iload 4
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label7
	iload_2
	iload 4
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label11
	goto Label8
Label7:
	iload_2
	iload 4
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label11
Label8:
	aload_3
	getfield Node/next LNode;
	getfield Node/data I
	iload_1
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
	aload_3
	aload_3
	getfield Node/next LNode;
	getfield Node/next LNode;
	putfield Node/next LNode;
	aload_0
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	putfield Linked_list/size I
	iload_2
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	if_icmpne Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label24
	aload_0
	aload_3
	putfield Linked_list/tail LNode;
	goto Label25
Label24:
Label25:
	return
	goto Label21
Label20:
	aload_3
	getfield Node/next LNode;
	astore_3
Label21:
Label10:
	iconst_1
	iload 4
	if_icmple Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifgt Label9
	iload_2
	iload 5
	iadd
	istore_2
	goto Label6
Label9:
	iload_2
	iload 5
	isub
	istore_2
	goto Label6
Label11:
Label1:
	return
.limit stack 3
.limit locals 6
.end method

.method public traverse()V
.var 0 is this LLinked_list; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is current LNode; from Label0 to Label1
	aload_0
	getfield Linked_list/head LNode;
	astore_2
.var 3 is $protect_expr2 I from Label0 to Label1
.var 4 is $protect_expr3 I from Label0 to Label1
	aload_0
	getfield Linked_list/size I
	istore_3
	iconst_1
	istore 4
	iconst_1
	istore_1
Label2:
	iconst_1
	iload_3
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label3
	iload_1
	iload_3
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label7
	goto Label4
Label3:
	iload_1
	iload_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label7
Label4:
	aload_2
	getfield Node/data I
	invokestatic io/writeInt(I)V
	aload_2
	getfield Node/next LNode;
	astore_2
Label6:
	iconst_1
	iload_3
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label5
	iload_1
	iload 4
	iadd
	istore_1
	goto Label2
Label5:
	iload_1
	iload 4
	isub
	istore_1
	goto Label2
Label7:
Label1:
	return
.limit stack 3
.limit locals 5
.end method
