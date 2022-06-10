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
	iconst_1
	invokestatic io/writeInt(I)V
	iconst_1
	invokestatic io/putInt(I)V
	iconst_1
	invokestatic io/printInt(I)V
	iconst_1
	invokestatic io/writeIntLn(I)V
	iconst_1
	invokestatic io/putIntLn(I)V
	iconst_1
	invokestatic io/printIntLn(I)V
	iconst_1
	invokestatic io/$writeInt(I)V
	iconst_1
	invokestatic io/$putInt(I)V
	iconst_1
	invokestatic io/$printInt(I)V
	iconst_1
	invokestatic io/$writeIntLn(I)V
	iconst_1
	invokestatic io/$putIntLn(I)V
	iconst_1
	invokestatic io/$printIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
