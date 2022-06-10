.source D96Class.java
.class public D96Class
.super java/lang/Object
.field a [I
.field static $a [I

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	bipush 9
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	dup
	iconst_3
	bipush 9
	iastore
	dup
	iconst_4
	bipush 9
	iastore
	putfield D96Class.a [I
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	bipush 9
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	dup
	iconst_3
	bipush 9
	iastore
	dup
	iconst_4
	bipush 9
	iastore
	putstatic D96Class.$a [I
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public method([I)V
.var 0 is this LD96Class; from Label0 to Label1
.var 1 is x [I from Label0 to Label1
Label0:
.var 2 is a [I from Label0 to Label1
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
	astore_2
.var 3 is b [I from Label0 to Label1
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
	astore_3
	aload_0
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
	putfield D96Class/a [I
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
	putstatic D96Class/$a [I
	aload_1
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
	aload_2
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
	aload_3
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
	aload_0
	getfield D96Class/a [I
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
	getstatic D96Class/$a [I
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 5
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is d LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_1
	aload_1
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
	invokevirtual D96Class/method([I)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method
