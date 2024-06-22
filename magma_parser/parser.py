from antlr4 import CommonTokenStream, FileStream
from dataclasses import dataclass
from magma_parser.generated.MagmaLexer import MagmaLexer
from magma_parser.generated.MagmaParser import MagmaParser
from magma_parser.generated.MagmaParserVisitor import MagmaParserVisitor


@dataclass
class Record:
    fields: dict[str, any]


@dataclass
class GroupRep:
    n: int
    x: int


@dataclass
class Permutation:
    parts: list[tuple[int]]


@dataclass
class GroupRepDesc:
    permutations: list[Permutation]


class RecordOutputsVisitor(MagmaParserVisitor):
    def visitOutputs(self, ctx: MagmaParser.OutputsContext):
        return [ self.visit(element) for element in ctx.array() ]

    def visitArray(self, ctx: MagmaParser.ArrayContext):
        return [ self.visit(element) for element in ctx.value() ]
    
    def visitRecord(self, ctx: MagmaParser.RecordContext):
        format_field_names = set(self.visit(ctx.record_formats()))
        field_definitions: list[MagmaParser.DefContext] = ctx.defs().def_()

        fields = {}
        for field_def in field_definitions:
            name = field_def.ID().getText()
            # skip fields which weren't in the format
            if name not in format_field_names:
                continue

            fields[name] = self.visit(field_def.value())

        return Record(fields)
    
    def visitRecord_formats(self, ctx: MagmaParser.Record_formatsContext):
        return [ self.visit(element) for element in ctx.record_format() ]
    
    def visitRecord_format(self, ctx: MagmaParser.Record_formatContext):
        return ctx.ID(0).getText()
        
    def visitValue(self, ctx: MagmaParser.ValueContext):
        if ctx.INT():
            return self.visitInt(ctx.INT())
        if ctx.BOOLEAN():
            return bool(ctx.BOOLEAN().getText())

        return super().visitValue(ctx)
    
    def visitGroup(self, ctx: MagmaParser.GroupContext):
        nums = ctx.INT()

        return GroupRep(
            n=self.visitInt(nums[0]),
            x=self.visitInt(nums[1])
        )
    
    def visitRepresentation_description(self, ctx: MagmaParser.Representation_descriptionContext):
        return GroupRepDesc(
            permutations=[ self.visit(element) for element in ctx.permutation() ]
        )
    
    def visitPermutation(self, ctx: MagmaParser.PermutationContext):
        return Permutation(parts=[ self.visit(element) for element in ctx.permutation_part()])
    
    def visitPermutation_part(self, ctx: MagmaParser.Permutation_partContext):
        return [ self.visitInt(element) for element in ctx.INT()]
    
    def visitInt(self, ctx):
        return int(ctx.getText())


def parse_file(path: str) -> list[list[Record]]:
    lexer = MagmaLexer(FileStream(path))
    parser = MagmaParser(CommonTokenStream(lexer))

    return RecordOutputsVisitor().visit(parser.outputs())
