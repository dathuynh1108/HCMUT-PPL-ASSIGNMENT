// Student ID: 1910110
// Student Name: Huynh Thanh Dat
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
// ----------------------------------  PARSER  -------------------------------------------
// program structure
program: class_declaration* EOF;

class_declaration : CLASS class_name (COLON class_name)? LCB class_body RCB;
class_name: ID; // ALERT! NOT COMPLETE
class_body: (attribute_declaration | method_declaration | constructor_declaration | destructor_declaration)*;

attribute_declaration: (VAR | VAL) (ID | DOLLAR_ID)(COMMA (ID | DOLLAR_ID))* COLON type_name initialization? SEMI;

method_declaration: (ID | DOLLAR_ID) LP list_of_parameters? RP block_statement;
constructor_declaration: CONSTRUCTOR LP list_of_parameters? RP block_statement;
destructor_declaration: DESTRUCTOR LP RP block_statement;

list_of_parameters: parameter_declaration(SEMI parameter_declaration)*;
parameter_declaration: (ID)(COMMA ID)* COLON type_name;


literal: array_literal | primitive_literal;

primitive_literal: INTEGER_LITERAL | FLOAT_LITERAL | STRING_LITERAL | BOOLEAN_LITERAL;
array_literal: indexed_array | multi_demensional_array;

indexed_array: ARRAY LP list_of_expressions? RP;

multi_demensional_array: ARRAY LP array_literal_list? RP;
array_literal_list  : array_literal (COMMA array_literal)*; 


type_name: primitive_type | array_type | class_type;  // can it has class type
primitive_type: INTEGER | FLOAT | STRING | BOOLEAN;
array_type: ARRAY LSB (primitive_type | array_type) COMMA INTEGER_LITERAL RSB;
class_type: ID;

initialization: 'Chua lam';


/***************************** STATEMENT ******************************/
block_statement: LCB statement* RCB;
statement   : variable_and_const_declaration
            | assign_statement
            | if_statement
            | foreach_statement
            //| while_statement           
            | break_statement
            | continue_statement
            | return_statement  
            | method_invocation_statement  
            ;



variable_and_const_declaration: (VAR | VAL) ID (COMMA ID)* COLON type_name initialization? SEMI;

assign_statement: left_hand_side ASSIGN expression SEMI;
left_hand_side  : ID 
                | DOLLAR_ID 
                | element_expression
                | instance_attribute_access
                | static_attribute_access
                ;

if_statement: IF LP expression RP block_statement // 1 if
            | IF LP expression RP block_statement else_statement // 1 if 1 else
            | IF LP expression RP block_statement elseif_statement+ // 1 if multi elseif
            | IF LP expression RP block_statement elseif_statement+ else_statement // 1 if multi elseif 1 elseif
            ;
elseif_statement: ELSEIF LP expression RP block_statement;
else_statement: ELSE block_statement;

foreach_statement: FOREACH LP (ID | DOLLAR_ID) IN expression DOUBLE_DOT expression (BY expression)? RP block_statement;
break_statement: BREAK SEMI;
continue_statement: CONTINUE SEMI;
return_statement: RETURN expression SEMI | RETURN SEMI;
method_invocation_statement: (instance_method_invocation | static_method_invocation) SEMI;


/***************************** EXPRESSION ******************************/
/*
    Tách expression từ dưới lên --> string op đầu tiên
    New expression(a+b)
*/
expression  :   string_expression;
string_expression   :   relation_expression STRING_ADD relation_expression
                    |   relation_expression STRING_EQUAL relation_expression
                    |   relation_expression
                    ;
relation_expression :   logical_expression EQUAL logical_expression
                    |   logical_expression NOT_EQUAL logical_expression
                    |   logical_expression LT logical_expression
                    |   logical_expression LTE logical_expression
                    |   logical_expression GT logical_expression
                    |   logical_expression GTE logical_expression
                    |   logical_expression
                    ;

logical_expression  :   logical_expression AND adding_expression  
                    |   logical_expression OR adding_expression 
                    |   adding_expression
                    ;

adding_expression   :   adding_expression ADD multiplying_expression
                    |   adding_expression SUB multiplying_expression
                    |   multiplying_expression
                    ;

multiplying_expression  :   multiplying_expression MUL negative_expression
                        |   multiplying_expression DIV negative_expression
                        |   multiplying_expression MOD negative_expression
                        |   negative_expression
                        ;

negative_expression :   NOT negative_expression
                    |   sign_expression
                    ;

sign_expression     :   SUB sign_expression
                    |   index_expression
                    ;
index_expression:   'Chưa biết làm :)';
element_expression: expression index_operator;
index_operator  :   LSB expression RSB
                |   LSB expression RSB index_operator
                ;

operand :   DOLLAR_ID
        |   ID
        |   literal
        |   LP expression RP
        ; // Chưa xong





member_access_expression    :   instance_attribute_access
                            |   static_attribute_access
                            |   instance_method_invocation
                            |   static_method_invocation
                            ;
instance_attribute_access: expression DOT ID;
static_attribute_access: class_name DOUBLE_COLON DOLLAR_ID;
instance_method_invocation: expression DOT ID LP list_of_expressions? RP;
static_method_invocation: class_name DOUBLE_COLON DOLLAR_ID LP list_of_expressions? RP;

object_creation_expression: NEW ID LP list_of_expressions RP;




list_of_expressions: expression (COMMA expression)*;





// ----------------------------------  LEXER  -------------------------------------------
/********************** FRAGMENT ***********************/
fragment COMMENT_CHAR: ~'#' | '#'~'#';

// [1-9]('_'*[0-9])* | '0'
fragment DEC_INTEGER_LITERAL:  [1-9]('_'*[0-9])* | '0';
fragment OCT_INTEGER_LITERAL: '0' [0-7]+;
fragment BIN_INTEGER_LITERAL: '0'[bB] [0-1]+;
fragment HEX_INTEGER_LITERAL: '0'[xX] [0-9A-Fa-f]+;

fragment STRING_CHAR    : ~([\b\t\n\f\r'"\\]) 
                        | ESCAPE_SEQUENCE 
                        | DOUBLE_QUOTE_CHAR;
fragment ESCAPE_SEQUENCE: '\\' [btnfr'\\];
fragment DOUBLE_QUOTE_CHAR: '\'"';
fragment ILLEGAL_SEQUENCE   : '\\' ~[btnfr'\\]  
                            | '\'' ~["] 
                            //| ~'\\' // \ + invalid or ' + invalid or \ 
                            ;
fragment SIGN: [+-];
fragment FLOAT_INTEGER_PART: [0-9][0-9_]*; // Only decimal base --> 0 at first is dec
fragment FLOAT_DECIMAL_PART: '.' FLOAT_INTEGER_PART?;
fragment FLOAT_EXPONENT_PART: [eE] SIGN? FLOAT_INTEGER_PART;

/********************** COMMENT ***********************/
COMMENT: '##' COMMENT_CHAR* '##' -> skip;
/********************* KEY WORDS **********************/
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
fragment TRUE: 'True';
fragment FALSE: 'False';
VAR: 'Var';
VAL: 'Val';
SELF: 'Self';
RETURN: 'Return';
IN: 'In';
BY: 'By';
NEW: 'New';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NULL: 'Null';
/********************* TYPES **********************/
CLASS: 'Class';
ARRAY: 'Array';
INTEGER: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
/********************* LITERALS ***********************/
INTEGER_LITERAL : (
                DEC_INTEGER_LITERAL 
                | OCT_INTEGER_LITERAL 
                | HEX_INTEGER_LITERAL 
                | BIN_INTEGER_LITERAL
) {
    self.text = self.text.translate(str.maketrans('','','_'))
}; // remove _ character


STRING_LITERAL: '"' STRING_CHAR* '"' {
	self.text = self.text[1:-1]
}; // remove open and close string
BOOLEAN_LITERAL: TRUE | FALSE;
FLOAT_LITERAL   : (
                FLOAT_INTEGER_PART FLOAT_DECIMAL_PART FLOAT_EXPONENT_PART?
                | FLOAT_INTEGER_PART FLOAT_EXPONENT_PART
                | FLOAT_DECIMAL_PART FLOAT_EXPONENT_PART

) {
    self.text = self.text.translate(str.maketrans('','','_'))
};







/********************* OPERATORS **********************/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
NOT_EQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
STRING_EQUAL: '==.';
STRING_ADD: '+.';

/******************** SEPARATORS **********************/
LP: '(' ;
RP: ')' ;

LSB: '[';
RSB: ']';

DOT: '.';
DOUBLE_DOT: '..';
COMMA: ',';
SEMI: ';';
COLON: ':';
DOUBLE_COLON: '::';

LCB: '{';
RCB: '}';

/******************** IDENTIFIERS *********************/
//_NUMBER is ID, not INTEGER_LITERAL
ID: [_a-zA-Z][_a-zA-Z0-9]*;
DOLLAR_ID: ('$')[_a-zA-Z][_a-zA-Z0-9]*;

/*********************** SKIP *************************/
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines


/*********************** ERRORS *************************/
// NOT(##) = NOT(#) OR # NOT(#)
// 1. ## NOT(##) EOF
// 2. ## NOT(#) #EOF ---- CASE # BEFORE EOF --> NOT(##) EOF CAN'T CATCH
UNTERMINATED_COMMENT    : (
                        '##' COMMENT_CHAR* EOF
                        | '##' ~'#'* '#' EOF
)  {
	raise UnterminatedComment()
};

/*UNCLOSE_STRING: '"' STRING_CHAR* ( [\b\t\n\f\r"'\\] | EOF ) {
    y = str(self.text)
    possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
    if y[-1] in possible:
        raise UncloseString(y[1:-1])
    else:
        raise UncloseString(y[1:])
}; */
UNCLOSE_STRING: '"' STRING_CHAR* {
    raise UncloseString(self.text[1:]);
};
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_SEQUENCE {
    raise IllegalEscape(self.text[1:])
};
ERROR_TOKEN: . {
    raise ErrorToken(self.text)
};