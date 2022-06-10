.source Program.java
.class public Program
.super Object
.field a LObject;

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial Object/<init>()V
	aload_0
	new Object
	dup
	invokespecial Object/<init>()V
	putfield Program.a LObject;
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public some_method()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
.var 1 is a LObject; from Label0 to Label1
	new Object
	dup
	invokespecial Object/<init>()V
	astore_1
	aload_1
	invokevirtual Object/method()I
	invokestatic io/writeInt(I)V
	new Object_2
	dup
	invokespecial Object_2/<init>()V
	astore_1
	aload_1
	invokevirtual Object/method()I
	invokestatic io/writeInt(I)V
	new Object_3
	dup
	invokespecial Object_3/<init>()V
	astore_1
	aload_1
	invokevirtual Object/method()I
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is o LObject; from Label0 to Label1
	new Program
	dup
	invokespecial Program/<init>()V
	astore_1
	aload_1
	invokevirtual Object/some_method()V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
