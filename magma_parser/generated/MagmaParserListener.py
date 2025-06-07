# Generated from grammar/MagmaParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MagmaParser import MagmaParser
else:
    from MagmaParser import MagmaParser

# This class defines a complete listener for a parse tree produced by MagmaParser.
class MagmaParserListener(ParseTreeListener):

    # Enter a parse tree produced by MagmaParser#magma.
    def enterMagma(self, ctx:MagmaParser.MagmaContext):
        pass

    # Exit a parse tree produced by MagmaParser#magma.
    def exitMagma(self, ctx:MagmaParser.MagmaContext):
        pass


    # Enter a parse tree produced by MagmaParser#outputs.
    def enterOutputs(self, ctx:MagmaParser.OutputsContext):
        pass

    # Exit a parse tree produced by MagmaParser#outputs.
    def exitOutputs(self, ctx:MagmaParser.OutputsContext):
        pass


    # Enter a parse tree produced by MagmaParser#array.
    def enterArray(self, ctx:MagmaParser.ArrayContext):
        pass

    # Exit a parse tree produced by MagmaParser#array.
    def exitArray(self, ctx:MagmaParser.ArrayContext):
        pass


    # Enter a parse tree produced by MagmaParser#record.
    def enterRecord(self, ctx:MagmaParser.RecordContext):
        pass

    # Exit a parse tree produced by MagmaParser#record.
    def exitRecord(self, ctx:MagmaParser.RecordContext):
        pass


    # Enter a parse tree produced by MagmaParser#record_formats.
    def enterRecord_formats(self, ctx:MagmaParser.Record_formatsContext):
        pass

    # Exit a parse tree produced by MagmaParser#record_formats.
    def exitRecord_formats(self, ctx:MagmaParser.Record_formatsContext):
        pass


    # Enter a parse tree produced by MagmaParser#record_format.
    def enterRecord_format(self, ctx:MagmaParser.Record_formatContext):
        pass

    # Exit a parse tree produced by MagmaParser#record_format.
    def exitRecord_format(self, ctx:MagmaParser.Record_formatContext):
        pass


    # Enter a parse tree produced by MagmaParser#defs.
    def enterDefs(self, ctx:MagmaParser.DefsContext):
        pass

    # Exit a parse tree produced by MagmaParser#defs.
    def exitDefs(self, ctx:MagmaParser.DefsContext):
        pass


    # Enter a parse tree produced by MagmaParser#def.
    def enterDef(self, ctx:MagmaParser.DefContext):
        pass

    # Exit a parse tree produced by MagmaParser#def.
    def exitDef(self, ctx:MagmaParser.DefContext):
        pass


    # Enter a parse tree produced by MagmaParser#value.
    def enterValue(self, ctx:MagmaParser.ValueContext):
        pass

    # Exit a parse tree produced by MagmaParser#value.
    def exitValue(self, ctx:MagmaParser.ValueContext):
        pass


    # Enter a parse tree produced by MagmaParser#group.
    def enterGroup(self, ctx:MagmaParser.GroupContext):
        pass

    # Exit a parse tree produced by MagmaParser#group.
    def exitGroup(self, ctx:MagmaParser.GroupContext):
        pass


    # Enter a parse tree produced by MagmaParser#permutation.
    def enterPermutation(self, ctx:MagmaParser.PermutationContext):
        pass

    # Exit a parse tree produced by MagmaParser#permutation.
    def exitPermutation(self, ctx:MagmaParser.PermutationContext):
        pass


    # Enter a parse tree produced by MagmaParser#permutation_part.
    def enterPermutation_part(self, ctx:MagmaParser.Permutation_partContext):
        pass

    # Exit a parse tree produced by MagmaParser#permutation_part.
    def exitPermutation_part(self, ctx:MagmaParser.Permutation_partContext):
        pass


    # Enter a parse tree produced by MagmaParser#int_expression.
    def enterInt_expression(self, ctx:MagmaParser.Int_expressionContext):
        pass

    # Exit a parse tree produced by MagmaParser#int_expression.
    def exitInt_expression(self, ctx:MagmaParser.Int_expressionContext):
        pass


    # Enter a parse tree produced by MagmaParser#int_operation.
    def enterInt_operation(self, ctx:MagmaParser.Int_operationContext):
        pass

    # Exit a parse tree produced by MagmaParser#int_operation.
    def exitInt_operation(self, ctx:MagmaParser.Int_operationContext):
        pass


    # Enter a parse tree produced by MagmaParser#relation.
    def enterRelation(self, ctx:MagmaParser.RelationContext):
        pass

    # Exit a parse tree produced by MagmaParser#relation.
    def exitRelation(self, ctx:MagmaParser.RelationContext):
        pass


    # Enter a parse tree produced by MagmaParser#multiline_value.
    def enterMultiline_value(self, ctx:MagmaParser.Multiline_valueContext):
        pass

    # Exit a parse tree produced by MagmaParser#multiline_value.
    def exitMultiline_value(self, ctx:MagmaParser.Multiline_valueContext):
        pass


    # Enter a parse tree produced by MagmaParser#export_duration.
    def enterExport_duration(self, ctx:MagmaParser.Export_durationContext):
        pass

    # Exit a parse tree produced by MagmaParser#export_duration.
    def exitExport_duration(self, ctx:MagmaParser.Export_durationContext):
        pass



del MagmaParser