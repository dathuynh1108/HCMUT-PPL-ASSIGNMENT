// Student ID: 1910110
// Student Name: Huynh Thanh Dat
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
// program structure
program: class_declaration+ EOF;
class_declaration : .;

// FRAGMENT:
fragment DEC_INTEGER_LITERAL: '0'| [1-9_][0-9_]* ;
fragment OCT_INTEGER_LITERAL: '0' [0-7_]+;
fragment BIN_INTEGER_LITERAL: '0'[bB] [0-1_]+;
fragment HEX_INTEGER_LITERAL: '0'[xX] [0-9A-Fa-f_]+;

fragment STRING_CHAR: ~([\b\t\n\f\r'"\\]) | ESCAPE_SEQUENCE | DOUBLE_QUOTE_CHAR;
fragment ESCAPE_SEQUENCE: '\\' [btnfr'\\];
fragment DOUBLE_QUOTE_CHAR: '\'"';
fragment ILLEGAL_SEQUENCE: '\\' ~[btnfr'\\] | ~'\\' ;
// LEXER:
/********************** COMMENT ***********************/
COMMENT: '##' .*? '##'-> skip;
/********************* KEY WORDS **********************/
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
/********************* TYPES **********************/
CLASS: 'class';
ARRAY: 'Array';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
NULL: 'Null';
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

LCB: '{';
RCB: '}';

/******************** IDENTIFIERS *********************/
// ID before LITERAL: _NUMBER is ID, not INTEGER_LITERAL
ID: ('$')?[_a-zA-Z][_a-zA-Z0-9]*;
/********************* LITERALS ***********************/
INTEGER_LITERAL: (DEC_INTEGER_LITERAL | OCT_INTEGER_LITERAL | HEX_INTEGER_LITERAL | BIN_INTEGER_LITERAL)
{
	self.text = self.text.translate(str.maketrans('','','_'))
};


STRING_LITERAL: '"' STRING_CHAR* '"' {
	self.text = self.text[1:-1]
};
BOOLEAN_LITERAL: TRUE | FALSE;
INDEXED_ARRAY: 'Array' '(' () ')';






/*********************** SKIP *************************/
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines


/*********************** ERRORS *************************/
UNTERMINATED_COMMENT: '##' ((~'#'~'#') | (.?)) EOF {
	raise UNTERMINATED_COMMENT(self.text)
};
ILLEGAL_ESCAPE
    : '"' STRING_CHAR* ILLEGAL_SEQUENCE
    {
        raise ILLEGAL_ESCAPE(self.text[1:])
    }
;
ERROR_TOKEN: . {
        raise ERROR_TOKEN(self.text)
    }
;