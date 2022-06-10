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

.method public method()[I
.var 0 is this LProgram; from Label0 to Label1
Label0:
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
	areturn
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is d LProgram; from Label0 to Label1
	new Program
	dup
	invokespecial Program/<init>()V
	astore_1
	aload_1
	invokevirtual Program/method()[I
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
	aload_1
	invokevirtual Program/method()[I
	iconst_0
	iaload
	i2f
	invokestatic io/writeFloat(F)V
.var 2 is a [I from Label0 to Label1
	aload_1
	invokevirtual Program/method()[I
	astore_2
	aload_2
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method
