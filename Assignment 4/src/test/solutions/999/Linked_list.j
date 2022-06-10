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
