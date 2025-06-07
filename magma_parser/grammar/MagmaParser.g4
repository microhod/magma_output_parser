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
    | multiline_value
    ;

group
    : '<' INT (',' INT)* '>'
    | UNKNOWN
    ;

permutation
    : permutation_part+
    ;

permutation_part
    : '(' INT (',' INT)* ')'
    ;


int_expression
    : INT
    | int_expression int_operation int_expression
    ;

int_operation
    : '*'
    | EXP
    ;

relation
    : GENERATOR EXP INT EQ IDENDITY
    ;

// TODO: investigate making the parser indentation-aware to remove the need for these special cases
multiline_value
    : STRING_UQ ('=' int_expression)? '\n' (ID '=' INT ('=' int_expression)? | ID '-' ID ':') (('\n' relation ',')* '\n' relation | ('\n' permutation)+)
    ;

export_duration
    : TIME ':' DECIMAL
    ;
