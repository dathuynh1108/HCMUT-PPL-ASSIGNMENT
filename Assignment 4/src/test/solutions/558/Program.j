.source Program.java
.class public Program
.super java/lang/Object
.field a [F
.field static $a [F

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_5
	newarray float
	dup
	iconst_0
	bipush 9
	i2f
	fastore
	dup
	iconst_1
	bipush 9
	i2f
	fastore
	dup
	iconst_2
	bipush 9
	i2f
	fastore
	dup
	iconst_3
	bipush 9
	i2f
	fastore
	dup
	iconst_4
	bipush 9
	i2f
	fastore
	putfield Program.a [F
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_5
	newarray float
	dup
	iconst_0
	bipush 9
	i2f
	fastore
	dup
	iconst_1
	bipush 9
	i2f
	fastore
	dup
	iconst_2
	bipush 9
	i2f
	fastore
	dup
	iconst_3
	bipush 9
	i2f
	fastore
	dup
	iconst_4
	bipush 9
	i2f
	fastore
	putstatic Program.$a [F
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public method([F)V
.var 0 is this LProgram; from Label0 to Label1
.var 1 is x [F from Label0 to Label1
Label0:
.var 2 is a [F from Label0 to Label1
	iconst_5
	newarray float
	dup
	iconst_0
	iconst_1
	i2f
	fastore
	dup
	iconst_1
	iconst_2
	i2f
	fastore
	dup
	iconst_2
	iconst_3
	i2f
	fastore
	dup
	iconst_3
	iconst_4
	i2f
	fastore
	dup
	iconst_4
	iconst_5
	i2f
	fastore
	astore_2
.var 3 is b [F from Label0 to Label1
	iconst_5
	newarray float
	dup
	iconst_0
	iconst_1
	i2f
	fastore
	dup
	iconst_1
	iconst_2
	i2f
	fastore
	dup
	iconst_2
	iconst_3
	i2f
	fastore
	dup
	iconst_3
	iconst_4
	i2f
	fastore
	dup
	iconst_4
	iconst_5
	i2f
	fastore
	astore_3
	aload_0
	iconst_5
	newarray float
	dup
	iconst_0
	iconst_1
	i2f
	fastore
	dup
	iconst_1
	iconst_2
	i2f
	fastore
	dup
	iconst_2
	iconst_3
	i2f
	fastore
	dup
	iconst_3
	iconst_4
	i2f
	fastore
	dup
	iconst_4
	iconst_5
	i2f
	fastore
	putfield Program/a [F
	iconst_5
	newarray float
	dup
	iconst_0
	iconst_1
	i2f
	fastore
	dup
	iconst_1
	iconst_2
	i2f
	fastore
	dup
	iconst_2
	iconst_3
	i2f
	fastore
	dup
	iconst_3
	iconst_4
	i2f
	fastore
	dup
	iconst_4
	iconst_5
	i2f
	fastore
	putstatic Program/$a [F
	aload_1
	iconst_0
	faload
	invokestatic io/writeFloat(F)V
	aload_2
	iconst_0
	faload
	invokestatic io/writeFloat(F)V
	aload_3
	iconst_0
	faload
	invokestatic io/writeFloat(F)V
	aload_0
	getfield Program/a [F
	iconst_0
	faload
	invokestatic io/writeFloat(F)V
	getstatic Program/$a [F
	iconst_0
	faload
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 5
.limit locals 4
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
	iconst_5
	newarray float
	dup
	iconst_0
	iconst_1
	i2f
	fastore
	dup
	iconst_1
	iconst_2
	i2f
	fastore
	dup
	iconst_2
	iconst_3
	i2f
	fastore
	dup
	iconst_3
	iconst_4
	i2f
	fastore
	dup
	iconst_4
	iconst_5
	i2f
	fastore
	invokevirtual Program/method([F)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method
