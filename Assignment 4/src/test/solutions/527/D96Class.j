.source D96Class.java
.class public D96Class
.super java/lang/Object
.field static $name Ljava/lang/String;
.field static $escapeSequence Ljava/lang/String;

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
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
	ldc "Huynh Thanh Dat"
	putstatic D96Class.$name Ljava/lang/String;
	ldc "\n1910110"
	putstatic D96Class.$escapeSequence Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic D96Class/$name Ljava/lang/String;
	getstatic D96Class/$escapeSequence Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
