// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

lexer grammar MagmaLexer;

LANGLE
    : '<'
    ;

RANGLE
    : '>'
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

LSQUARE
    : '['
    ;

RSQUARE
    : ']'
    ;

COLON
    : ':'
    ;

COMMA
    : ','
    ;

PIPE
    : '|'
    ;

EQ
    : '='
    ;

DEF
    : ':='
    ;

MULT
    : '*'
    ;

EXP
    : '^'
    ;

NEWLINE
    : '\n'
    ;

BOOLEAN
    : 'true'
    | 'false'
    ;

INT
    // integer part forbis leading 0s (e.g. `01`)
    : '0'
    | [1-9] [0-9]*
    ;

DECIMAL
    : [1-9][0-9]* '.' [0-9]+
    | '0' '.' [0-9]+
    ;

RECORD
    : 'rec'
    ;

RECORD_FORMAT
    : 'recformat'
    ;

ORDER
    : 'Order'
    ;

TIME
    : 'Time'
    ;

STRING_UQ
    : [a-zA-Z0-9]+ (' ' [a-zA-Z0-9]+)+
    ;

ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

WS
    : [ \t\r]+ -> skip
    ;