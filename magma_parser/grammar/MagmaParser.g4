// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

parser grammar MagmaParser;
options { tokenVocab=MagmaLexer; }

magma
    :
    | outputs
    | EOF
    ;

outputs
    : array (('\n' export_duration)? '\n' array)* ('\n' export_duration)? '\n'*
    ;

array
    : '[' '*'? '\n'? value (',' '\n'? value)* '\n'? '*'? ']'
    | '[' ']'
    ;

record
    : RECORD '<' RECORD_FORMAT '<' record_formats '>' '|' '\n' defs '\n'? '>'
    ;

record_formats
    : record_format (',' '\n'? record_format)*
    ;

record_format
    : ID (':' ID '(' ')')?
    ;

defs
    : def (',' '\n' def)*
    ;

def
    : ID DEF value
    ;

value
    : INT
    | BOOLEAN
    | group
    | record
    | array
    | representation_description
    ;

group
    : '<' INT (',' INT)* '>'
    ;

permutation
    : permutation_part+
    ;

permutation_part
    : '(' INT (',' INT)* ')'
    ;

order_calculation
    : ORDER '=' INT ('=' int_expression)?
    ;

int_expression
    : INT
    | int_expression int_operation int_expression
    ;

int_operation
    : '*'
    | EXP
    ;

representation_description
    : STRING_UQ '\n' order_calculation '\n' permutation ('\n' permutation)*
    ;

export_duration
    : TIME ':' DECIMAL
    ;
