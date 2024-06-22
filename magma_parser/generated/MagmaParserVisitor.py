# Generated from grammar/MagmaParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MagmaParser import MagmaParser
else:
    from MagmaParser import MagmaParser

# This class defines a complete generic visitor for a parse tree produced by MagmaParser.

class MagmaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MagmaParser#magma.
    def visitMagma(self, ctx:MagmaParser.MagmaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#outputs.
    def visitOutputs(self, ctx:MagmaParser.OutputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#array.
    def visitArray(self, ctx:MagmaParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#record.
    def visitRecord(self, ctx:MagmaParser.RecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#record_formats.
    def visitRecord_formats(self, ctx:MagmaParser.Record_formatsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#record_format.
    def visitRecord_format(self, ctx:MagmaParser.Record_formatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#defs.
    def visitDefs(self, ctx:MagmaParser.DefsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#def.
    def visitDef(self, ctx:MagmaParser.DefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#value.
    def visitValue(self, ctx:MagmaParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#group.
    def visitGroup(self, ctx:MagmaParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#permutation.
    def visitPermutation(self, ctx:MagmaParser.PermutationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#permutation_part.
    def visitPermutation_part(self, ctx:MagmaParser.Permutation_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#order_calculation.
    def visitOrder_calculation(self, ctx:MagmaParser.Order_calculationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#int_expression.
    def visitInt_expression(self, ctx:MagmaParser.Int_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#int_operation.
    def visitInt_operation(self, ctx:MagmaParser.Int_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#representation_description.
    def visitRepresentation_description(self, ctx:MagmaParser.Representation_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MagmaParser#export_duration.
    def visitExport_duration(self, ctx:MagmaParser.Export_durationContext):
        return self.visitChildren(ctx)



del MagmaParser