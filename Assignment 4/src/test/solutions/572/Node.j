.source Node.java
.class public Node
.super java/lang/Object
.field next LNode;
.field data I

.method public <init>(LNode;I)V
.var 0 is this LNode; from Label0 to Label1
.var 1 is next LNode; from Label0 to Label1
.var 2 is data I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aconst_null
	putfield Node.next LNode;
	aload_0
	iconst_0
	putfield Node.data I
	aload_0
	aload_1
	putfield Node/next LNode;
	aload_0
	iload_2
	putfield Node/data I
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LNode; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aconst_null
	putfield Node.next LNode;
	aload_0
	iconst_0
	putfield Node.data I
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
