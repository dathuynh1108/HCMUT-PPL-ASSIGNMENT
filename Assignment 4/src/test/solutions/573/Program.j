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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is linked_list LLinked_list; from Label0 to Label1
	new Linked_list
	dup
	invokespecial Linked_list/<init>()V
	astore_1
.var 2 is i I from Label0 to Label1
.var 3 is $protect_expr2 I from Label0 to Label1
.var 4 is $protect_expr3 I from Label0 to Label1
	bipush 20
	istore_3
	iconst_1
	istore 4
	iconst_1
	istore_2
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
	iload_2
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
	iload_2
	iload_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label7
Label4:
	aload_1
	new Node
	dup
	aconst_null
	iload_2
	invokespecial Node/<init>(LNode;I)V
	invokevirtual Linked_list/insert(LNode;)V
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
	iload_2
	iload 4
	iadd
	istore_2
	goto Label2
Label5:
	iload_2
	iload 4
	isub
	istore_2
	goto Label2
Label7:
	aload_1
	invokevirtual Linked_list/traverse()V
	aload_1
	iconst_1
	invokevirtual Linked_list/delete(I)V
	aload_1
	bipush 20
	invokevirtual Linked_list/delete(I)V
	aload_1
	bipush 10
	invokevirtual Linked_list/delete(I)V
	aload_1
	invokevirtual Linked_list/traverse()V
Label1:
	return
.limit stack 6
.limit locals 5
.end method
