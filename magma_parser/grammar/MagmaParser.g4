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
    : array (NEWLINE (export_duration NEWLINE)? array)*
    ;

array
    : LSQUARE MULT? NEWLINE? value (COMMA NEWLINE? value)* NEWLINE? MULT? RSQUARE
    | LSQUARE RSQUARE
    ;

record
    : RECORD LANGLE RECORD_FORMAT LANGLE record_formats RANGLE PIPE NEWLINE defs NEWLINE? RANGLE
    ;

record_formats
    : record_format (COMMA NEWLINE? record_format)*
    ;

record_format
    : ID (COLON ID LPAREN RPAREN)?
    ;

defs
    : def (COMMA NEWLINE def)*
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
    : LANGLE INT (COMMA INT)* RANGLE
    ;

permutation
    : permutation_part+
    ;

permutation_part
    : '(' INT (',' INT)* ')'
    ;

// TODO: support 'Order = 8 = 2^2 * 2' and 'Order = 8 = 2 * 4'
order_calculation
    : ORDER EQ INT (EQ int_expression)?
    ;

int_expression
    : INT
    | int_expression int_operation int_expression
    ;

int_operation
    : MULT
    | EXP
    ;

representation_description
    : STRING_UQ NEWLINE order_calculation NEWLINE permutation (NEWLINE permutation)*
    ;

export_duration
    : TIME COLON DECIMAL
    ;
