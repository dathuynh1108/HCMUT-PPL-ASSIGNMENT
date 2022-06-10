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

.method public static $method(LAnimal;)V
.var 0 is a LAnimal; from Label0 to Label1
Label0:
	ldc "OK"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a LAnimal; from Label0 to Label1
	new Animal
	dup
	invokespecial Animal/<init>()V
	astore_1
.var 2 is b LAnimal; from Label0 to Label1
	new Dog
	dup
	invokespecial Dog/<init>()V
	astore_2
.var 3 is c LDog; from Label0 to Label1
	new Dog
	dup
	invokespecial Dog/<init>()V
	astore_3
	aload_1
	invokestatic Program/$method(LAnimal;)V
	aload_2
	invokestatic Program/$method(LAnimal;)V
	aload_3
	invokestatic Program/$method(LAnimal;)V
	new Animal
	dup
	invokespecial Animal/<init>()V
	invokestatic Program/$method(LAnimal;)V
	new Dog
	dup
	invokespecial Dog/<init>()V
	invokestatic Program/$method(LAnimal;)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method
