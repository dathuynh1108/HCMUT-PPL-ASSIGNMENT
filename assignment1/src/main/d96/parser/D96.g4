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
program: class_declaration+ EOF;
class_declaration : .;
// ----------------------------------  LEXER  -------------------------------------------
/********************** FRAGMENT ***********************/
fragment COMMENT_CHAR: ~'#' | '#'~'#';

// [1-9](_*[0-9])* | '0'
fragment DEC_INTEGER_LITERAL:  '0' | [1-9][0-9_]*;
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
                            | ~'\\'; // \ + invalid or ' + invalid or \ 

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
VAR: 'var';
VAL: 'val';
/********************* TYPES **********************/
CLASS: 'class';
ARRAY: 'Array';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
NULL: 'Null';


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





/******************** IDENTIFIERS *********************/
//_NUMBER is ID, not INTEGER_LITERAL
ID: ('$')?[_a-zA-Z][_a-zA-Z0-9]*;






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
COMMA: ',';
SEMI: ';';
COLON: ':';

LCB: '{';
RCB: '}';

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
	raise UNTERMINATED_COMMENT()
};

UNCLOSE_STRING: '"' STRING_CHAR* ( [\b\t\n\f\r"'\\] | EOF ) {
    y = str(self.text)
    possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
    if y[-1] in possible:
        raise UNCLOSE_STRING(y[1:-1])
    else:
        raise UNCLOSE_STRING(y[1:])
}; 
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_SEQUENCE {
    raise ILLEGAL_ESCAPE(self.text[1:])
};
ERROR_TOKEN: . {
    raise ERROR_TOKEN(self.text)
};