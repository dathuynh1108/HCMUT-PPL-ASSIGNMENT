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
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 7
	iastore
	dup
	iconst_3
	bipush 6
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
	iconst_4
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_1
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	aastore
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 7
	iastore
	dup
	iconst_3
	bipush 6
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
	iconst_4
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_1
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	aastore
	iconst_0
	aaload
	iconst_0
	iaload
	i2f
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 7
.limit locals 1
.end method
