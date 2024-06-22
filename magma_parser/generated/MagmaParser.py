# Generated from grammar/MagmaParser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,200,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,3,0,38,8,0,1,1,1,1,1,1,
        1,1,1,1,3,1,45,8,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,2,1,2,3,2,55,
        8,2,1,2,3,2,58,8,2,1,2,1,2,1,2,3,2,63,8,2,1,2,5,2,66,8,2,10,2,12,
        2,69,9,2,1,2,3,2,72,8,2,1,2,3,2,75,8,2,1,2,1,2,1,2,1,2,3,2,81,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,93,8,3,1,3,1,3,1,4,
        1,4,1,4,3,4,100,8,4,1,4,5,4,103,8,4,10,4,12,4,106,9,4,1,5,1,5,1,
        5,1,5,1,5,3,5,113,8,5,1,6,1,6,1,6,1,6,5,6,119,8,6,10,6,12,6,122,
        9,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,134,8,8,1,9,1,9,
        1,9,1,9,5,9,140,8,9,10,9,12,9,143,9,9,1,9,1,9,1,10,4,10,148,8,10,
        11,10,12,10,149,1,11,1,11,1,11,1,11,5,11,156,8,11,10,11,12,11,159,
        9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,168,8,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,5,13,177,8,13,10,13,12,13,180,9,13,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,191,8,15,10,15,12,15,
        194,9,15,1,16,1,16,1,16,1,16,1,16,0,1,26,17,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,0,1,1,0,12,13,209,0,37,1,0,0,0,2,39,1,0,
        0,0,4,80,1,0,0,0,6,82,1,0,0,0,8,96,1,0,0,0,10,107,1,0,0,0,12,114,
        1,0,0,0,14,123,1,0,0,0,16,133,1,0,0,0,18,135,1,0,0,0,20,147,1,0,
        0,0,22,151,1,0,0,0,24,162,1,0,0,0,26,169,1,0,0,0,28,181,1,0,0,0,
        30,183,1,0,0,0,32,195,1,0,0,0,34,38,1,0,0,0,35,38,3,2,1,0,36,38,
        5,0,0,1,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,1,1,0,0,0,39,
        49,3,4,2,0,40,44,5,14,0,0,41,42,3,32,16,0,42,43,5,14,0,0,43,45,1,
        0,0,0,44,41,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,48,3,4,2,0,47,
        40,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,3,1,0,0,
        0,51,49,1,0,0,0,52,54,5,5,0,0,53,55,5,12,0,0,54,53,1,0,0,0,54,55,
        1,0,0,0,55,57,1,0,0,0,56,58,5,14,0,0,57,56,1,0,0,0,57,58,1,0,0,0,
        58,59,1,0,0,0,59,67,3,16,8,0,60,62,5,8,0,0,61,63,5,14,0,0,62,61,
        1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,66,3,16,8,0,65,60,1,0,0,0,
        66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,67,1,
        0,0,0,70,72,5,14,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,
        75,5,12,0,0,74,73,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,6,
        0,0,77,81,1,0,0,0,78,79,5,5,0,0,79,81,5,6,0,0,80,52,1,0,0,0,80,78,
        1,0,0,0,81,5,1,0,0,0,82,83,5,18,0,0,83,84,5,1,0,0,84,85,5,19,0,0,
        85,86,5,1,0,0,86,87,3,8,4,0,87,88,5,2,0,0,88,89,5,9,0,0,89,90,5,
        14,0,0,90,92,3,12,6,0,91,93,5,14,0,0,92,91,1,0,0,0,92,93,1,0,0,0,
        93,94,1,0,0,0,94,95,5,2,0,0,95,7,1,0,0,0,96,104,3,10,5,0,97,99,5,
        8,0,0,98,100,5,14,0,0,99,98,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,
        0,101,103,3,10,5,0,102,97,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,
        0,104,105,1,0,0,0,105,9,1,0,0,0,106,104,1,0,0,0,107,112,5,23,0,0,
        108,109,5,7,0,0,109,110,5,23,0,0,110,111,5,3,0,0,111,113,5,4,0,0,
        112,108,1,0,0,0,112,113,1,0,0,0,113,11,1,0,0,0,114,120,3,14,7,0,
        115,116,5,8,0,0,116,117,5,14,0,0,117,119,3,14,7,0,118,115,1,0,0,
        0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,13,1,0,0,0,
        122,120,1,0,0,0,123,124,5,23,0,0,124,125,5,11,0,0,125,126,3,16,8,
        0,126,15,1,0,0,0,127,134,5,16,0,0,128,134,5,15,0,0,129,134,3,18,
        9,0,130,134,3,6,3,0,131,134,3,4,2,0,132,134,3,30,15,0,133,127,1,
        0,0,0,133,128,1,0,0,0,133,129,1,0,0,0,133,130,1,0,0,0,133,131,1,
        0,0,0,133,132,1,0,0,0,134,17,1,0,0,0,135,136,5,1,0,0,136,141,5,16,
        0,0,137,138,5,8,0,0,138,140,5,16,0,0,139,137,1,0,0,0,140,143,1,0,
        0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,
        0,0,144,145,5,2,0,0,145,19,1,0,0,0,146,148,3,22,11,0,147,146,1,0,
        0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,21,1,0,0,
        0,151,152,5,3,0,0,152,157,5,16,0,0,153,154,5,8,0,0,154,156,5,16,
        0,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,
        0,0,158,160,1,0,0,0,159,157,1,0,0,0,160,161,5,4,0,0,161,23,1,0,0,
        0,162,163,5,20,0,0,163,164,5,10,0,0,164,167,5,16,0,0,165,166,5,10,
        0,0,166,168,3,26,13,0,167,165,1,0,0,0,167,168,1,0,0,0,168,25,1,0,
        0,0,169,170,6,13,-1,0,170,171,5,16,0,0,171,178,1,0,0,0,172,173,10,
        1,0,0,173,174,3,28,14,0,174,175,3,26,13,2,175,177,1,0,0,0,176,172,
        1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,27,1,
        0,0,0,180,178,1,0,0,0,181,182,7,0,0,0,182,29,1,0,0,0,183,184,5,22,
        0,0,184,185,5,14,0,0,185,186,3,24,12,0,186,187,5,14,0,0,187,192,
        3,20,10,0,188,189,5,14,0,0,189,191,3,20,10,0,190,188,1,0,0,0,191,
        194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,31,1,0,0,0,194,192,
        1,0,0,0,195,196,5,21,0,0,196,197,5,7,0,0,197,198,5,17,0,0,198,33,
        1,0,0,0,22,37,44,49,54,57,62,67,71,74,80,92,99,104,112,120,133,141,
        149,157,167,178,192
    ]

class MagmaParser ( Parser ):

    grammarFileName = "MagmaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'('", "')'", "'['", "']'", 
                     "':'", "','", "'|'", "'='", "':='", "'*'", "'^'", "'\\n'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'rec'", "'recformat'", 
                     "'Order'", "'Time'" ]

    symbolicNames = [ "<INVALID>", "LANGLE", "RANGLE", "LPAREN", "RPAREN", 
                      "LSQUARE", "RSQUARE", "COLON", "COMMA", "PIPE", "EQ", 
                      "DEF", "MULT", "EXP", "NEWLINE", "BOOLEAN", "INT", 
                      "DECIMAL", "RECORD", "RECORD_FORMAT", "ORDER", "TIME", 
                      "STRING_UQ", "ID", "WS" ]

    RULE_magma = 0
    RULE_outputs = 1
    RULE_array = 2
    RULE_record = 3
    RULE_record_formats = 4
    RULE_record_format = 5
    RULE_defs = 6
    RULE_def = 7
    RULE_value = 8
    RULE_group = 9
    RULE_permutation = 10
    RULE_permutation_part = 11
    RULE_order_calculation = 12
    RULE_int_expression = 13
    RULE_int_operation = 14
    RULE_representation_description = 15
    RULE_export_duration = 16

    ruleNames =  [ "magma", "outputs", "array", "record", "record_formats", 
                   "record_format", "defs", "def", "value", "group", "permutation", 
                   "permutation_part", "order_calculation", "int_expression", 
                   "int_operation", "representation_description", "export_duration" ]

    EOF = Token.EOF
    LANGLE=1
    RANGLE=2
    LPAREN=3
    RPAREN=4
    LSQUARE=5
    RSQUARE=6
    COLON=7
    COMMA=8
    PIPE=9
    EQ=10
    DEF=11
    MULT=12
    EXP=13
    NEWLINE=14
    BOOLEAN=15
    INT=16
    DECIMAL=17
    RECORD=18
    RECORD_FORMAT=19
    ORDER=20
    TIME=21
    STRING_UQ=22
    ID=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MagmaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def outputs(self):
            return self.getTypedRuleContext(MagmaParser.OutputsContext,0)


        def EOF(self):
            return self.getToken(MagmaParser.EOF, 0)

        def getRuleIndex(self):
            return MagmaParser.RULE_magma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMagma" ):
                listener.enterMagma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMagma" ):
                listener.exitMagma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMagma" ):
                return visitor.visitMagma(self)
            else:
                return visitor.visitChildren(self)




    def magma(self):

        localctx = MagmaParser.MagmaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_magma)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.outputs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(MagmaParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.ArrayContext)
            else:
                return self.getTypedRuleContext(MagmaParser.ArrayContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.NEWLINE)
            else:
                return self.getToken(MagmaParser.NEWLINE, i)

        def export_duration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.Export_durationContext)
            else:
                return self.getTypedRuleContext(MagmaParser.Export_durationContext,i)


        def getRuleIndex(self):
            return MagmaParser.RULE_outputs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputs" ):
                listener.enterOutputs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputs" ):
                listener.exitOutputs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputs" ):
                return visitor.visitOutputs(self)
            else:
                return visitor.visitChildren(self)




    def outputs(self):

        localctx = MagmaParser.OutputsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_outputs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.array()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 40
                self.match(MagmaParser.NEWLINE)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 41
                    self.export_duration()
                    self.state = 42
                    self.match(MagmaParser.NEWLINE)


                self.state = 46
                self.array()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUARE(self):
            return self.getToken(MagmaParser.LSQUARE, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.ValueContext)
            else:
                return self.getTypedRuleContext(MagmaParser.ValueContext,i)


        def RSQUARE(self):
            return self.getToken(MagmaParser.RSQUARE, 0)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.MULT)
            else:
                return self.getToken(MagmaParser.MULT, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.NEWLINE)
            else:
                return self.getToken(MagmaParser.NEWLINE, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.COMMA)
            else:
                return self.getToken(MagmaParser.COMMA, i)

        def getRuleIndex(self):
            return MagmaParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MagmaParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(MagmaParser.LSQUARE)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 53
                    self.match(MagmaParser.MULT)


                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 56
                    self.match(MagmaParser.NEWLINE)


                self.state = 59
                self.value()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 60
                    self.match(MagmaParser.COMMA)
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==14:
                        self.state = 61
                        self.match(MagmaParser.NEWLINE)


                    self.state = 64
                    self.value()
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 70
                    self.match(MagmaParser.NEWLINE)


                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 73
                    self.match(MagmaParser.MULT)


                self.state = 76
                self.match(MagmaParser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(MagmaParser.LSQUARE)
                self.state = 79
                self.match(MagmaParser.RSQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECORD(self):
            return self.getToken(MagmaParser.RECORD, 0)

        def LANGLE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.LANGLE)
            else:
                return self.getToken(MagmaParser.LANGLE, i)

        def RECORD_FORMAT(self):
            return self.getToken(MagmaParser.RECORD_FORMAT, 0)

        def record_formats(self):
            return self.getTypedRuleContext(MagmaParser.Record_formatsContext,0)


        def RANGLE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.RANGLE)
            else:
                return self.getToken(MagmaParser.RANGLE, i)

        def PIPE(self):
            return self.getToken(MagmaParser.PIPE, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.NEWLINE)
            else:
                return self.getToken(MagmaParser.NEWLINE, i)

        def defs(self):
            return self.getTypedRuleContext(MagmaParser.DefsContext,0)


        def getRuleIndex(self):
            return MagmaParser.RULE_record

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord" ):
                listener.enterRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord" ):
                listener.exitRecord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord" ):
                return visitor.visitRecord(self)
            else:
                return visitor.visitChildren(self)




    def record(self):

        localctx = MagmaParser.RecordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MagmaParser.RECORD)
            self.state = 83
            self.match(MagmaParser.LANGLE)
            self.state = 84
            self.match(MagmaParser.RECORD_FORMAT)
            self.state = 85
            self.match(MagmaParser.LANGLE)
            self.state = 86
            self.record_formats()
            self.state = 87
            self.match(MagmaParser.RANGLE)
            self.state = 88
            self.match(MagmaParser.PIPE)
            self.state = 89
            self.match(MagmaParser.NEWLINE)
            self.state = 90
            self.defs()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 91
                self.match(MagmaParser.NEWLINE)


            self.state = 94
            self.match(MagmaParser.RANGLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_formatsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def record_format(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.Record_formatContext)
            else:
                return self.getTypedRuleContext(MagmaParser.Record_formatContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.COMMA)
            else:
                return self.getToken(MagmaParser.COMMA, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.NEWLINE)
            else:
                return self.getToken(MagmaParser.NEWLINE, i)

        def getRuleIndex(self):
            return MagmaParser.RULE_record_formats

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord_formats" ):
                listener.enterRecord_formats(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord_formats" ):
                listener.exitRecord_formats(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord_formats" ):
                return visitor.visitRecord_formats(self)
            else:
                return visitor.visitChildren(self)




    def record_formats(self):

        localctx = MagmaParser.Record_formatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_record_formats)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.record_format()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 97
                self.match(MagmaParser.COMMA)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 98
                    self.match(MagmaParser.NEWLINE)


                self.state = 101
                self.record_format()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.ID)
            else:
                return self.getToken(MagmaParser.ID, i)

        def COLON(self):
            return self.getToken(MagmaParser.COLON, 0)

        def LPAREN(self):
            return self.getToken(MagmaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MagmaParser.RPAREN, 0)

        def getRuleIndex(self):
            return MagmaParser.RULE_record_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord_format" ):
                listener.enterRecord_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord_format" ):
                listener.exitRecord_format(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord_format" ):
                return visitor.visitRecord_format(self)
            else:
                return visitor.visitChildren(self)




    def record_format(self):

        localctx = MagmaParser.Record_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_record_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MagmaParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 108
                self.match(MagmaParser.COLON)
                self.state = 109
                self.match(MagmaParser.ID)
                self.state = 110
                self.match(MagmaParser.LPAREN)
                self.state = 111
                self.match(MagmaParser.RPAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def def_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.DefContext)
            else:
                return self.getTypedRuleContext(MagmaParser.DefContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.COMMA)
            else:
                return self.getToken(MagmaParser.COMMA, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.NEWLINE)
            else:
                return self.getToken(MagmaParser.NEWLINE, i)

        def getRuleIndex(self):
            return MagmaParser.RULE_defs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefs" ):
                listener.enterDefs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefs" ):
                listener.exitDefs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefs" ):
                return visitor.visitDefs(self)
            else:
                return visitor.visitChildren(self)




    def defs(self):

        localctx = MagmaParser.DefsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_defs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.def_()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 115
                self.match(MagmaParser.COMMA)
                self.state = 116
                self.match(MagmaParser.NEWLINE)
                self.state = 117
                self.def_()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MagmaParser.ID, 0)

        def DEF(self):
            return self.getToken(MagmaParser.DEF, 0)

        def value(self):
            return self.getTypedRuleContext(MagmaParser.ValueContext,0)


        def getRuleIndex(self):
            return MagmaParser.RULE_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDef" ):
                listener.enterDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDef" ):
                listener.exitDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDef" ):
                return visitor.visitDef(self)
            else:
                return visitor.visitChildren(self)




    def def_(self):

        localctx = MagmaParser.DefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MagmaParser.ID)
            self.state = 124
            self.match(MagmaParser.DEF)
            self.state = 125
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MagmaParser.INT, 0)

        def BOOLEAN(self):
            return self.getToken(MagmaParser.BOOLEAN, 0)

        def group(self):
            return self.getTypedRuleContext(MagmaParser.GroupContext,0)


        def record(self):
            return self.getTypedRuleContext(MagmaParser.RecordContext,0)


        def array(self):
            return self.getTypedRuleContext(MagmaParser.ArrayContext,0)


        def representation_description(self):
            return self.getTypedRuleContext(MagmaParser.Representation_descriptionContext,0)


        def getRuleIndex(self):
            return MagmaParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MagmaParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(MagmaParser.INT)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(MagmaParser.BOOLEAN)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.group()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.record()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.array()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 132
                self.representation_description()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LANGLE(self):
            return self.getToken(MagmaParser.LANGLE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.INT)
            else:
                return self.getToken(MagmaParser.INT, i)

        def RANGLE(self):
            return self.getToken(MagmaParser.RANGLE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.COMMA)
            else:
                return self.getToken(MagmaParser.COMMA, i)

        def getRuleIndex(self):
            return MagmaParser.RULE_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup" ):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)




    def group(self):

        localctx = MagmaParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MagmaParser.LANGLE)
            self.state = 136
            self.match(MagmaParser.INT)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 137
                self.match(MagmaParser.COMMA)
                self.state = 138
                self.match(MagmaParser.INT)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(MagmaParser.RANGLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PermutationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def permutation_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.Permutation_partContext)
            else:
                return self.getTypedRuleContext(MagmaParser.Permutation_partContext,i)


        def getRuleIndex(self):
            return MagmaParser.RULE_permutation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPermutation" ):
                listener.enterPermutation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPermutation" ):
                listener.exitPermutation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPermutation" ):
                return visitor.visitPermutation(self)
            else:
                return visitor.visitChildren(self)




    def permutation(self):

        localctx = MagmaParser.PermutationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_permutation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.permutation_part()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Permutation_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MagmaParser.LPAREN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.INT)
            else:
                return self.getToken(MagmaParser.INT, i)

        def RPAREN(self):
            return self.getToken(MagmaParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.COMMA)
            else:
                return self.getToken(MagmaParser.COMMA, i)

        def getRuleIndex(self):
            return MagmaParser.RULE_permutation_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPermutation_part" ):
                listener.enterPermutation_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPermutation_part" ):
                listener.exitPermutation_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPermutation_part" ):
                return visitor.visitPermutation_part(self)
            else:
                return visitor.visitChildren(self)




    def permutation_part(self):

        localctx = MagmaParser.Permutation_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_permutation_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MagmaParser.LPAREN)
            self.state = 152
            self.match(MagmaParser.INT)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 153
                self.match(MagmaParser.COMMA)
                self.state = 154
                self.match(MagmaParser.INT)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(MagmaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Order_calculationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(MagmaParser.ORDER, 0)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.EQ)
            else:
                return self.getToken(MagmaParser.EQ, i)

        def INT(self):
            return self.getToken(MagmaParser.INT, 0)

        def int_expression(self):
            return self.getTypedRuleContext(MagmaParser.Int_expressionContext,0)


        def getRuleIndex(self):
            return MagmaParser.RULE_order_calculation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrder_calculation" ):
                listener.enterOrder_calculation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrder_calculation" ):
                listener.exitOrder_calculation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrder_calculation" ):
                return visitor.visitOrder_calculation(self)
            else:
                return visitor.visitChildren(self)




    def order_calculation(self):

        localctx = MagmaParser.Order_calculationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_order_calculation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(MagmaParser.ORDER)
            self.state = 163
            self.match(MagmaParser.EQ)
            self.state = 164
            self.match(MagmaParser.INT)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 165
                self.match(MagmaParser.EQ)
                self.state = 166
                self.int_expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MagmaParser.INT, 0)

        def int_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.Int_expressionContext)
            else:
                return self.getTypedRuleContext(MagmaParser.Int_expressionContext,i)


        def int_operation(self):
            return self.getTypedRuleContext(MagmaParser.Int_operationContext,0)


        def getRuleIndex(self):
            return MagmaParser.RULE_int_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_expression" ):
                listener.enterInt_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_expression" ):
                listener.exitInt_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_expression" ):
                return visitor.visitInt_expression(self)
            else:
                return visitor.visitChildren(self)



    def int_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MagmaParser.Int_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_int_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MagmaParser.INT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MagmaParser.Int_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expression)
                    self.state = 172
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 173
                    self.int_operation()
                    self.state = 174
                    self.int_expression(2) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Int_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(MagmaParser.MULT, 0)

        def EXP(self):
            return self.getToken(MagmaParser.EXP, 0)

        def getRuleIndex(self):
            return MagmaParser.RULE_int_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_operation" ):
                listener.enterInt_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_operation" ):
                listener.exitInt_operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_operation" ):
                return visitor.visitInt_operation(self)
            else:
                return visitor.visitChildren(self)




    def int_operation(self):

        localctx = MagmaParser.Int_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_int_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Representation_descriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_UQ(self):
            return self.getToken(MagmaParser.STRING_UQ, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.NEWLINE)
            else:
                return self.getToken(MagmaParser.NEWLINE, i)

        def order_calculation(self):
            return self.getTypedRuleContext(MagmaParser.Order_calculationContext,0)


        def permutation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.PermutationContext)
            else:
                return self.getTypedRuleContext(MagmaParser.PermutationContext,i)


        def getRuleIndex(self):
            return MagmaParser.RULE_representation_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepresentation_description" ):
                listener.enterRepresentation_description(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepresentation_description" ):
                listener.exitRepresentation_description(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepresentation_description" ):
                return visitor.visitRepresentation_description(self)
            else:
                return visitor.visitChildren(self)




    def representation_description(self):

        localctx = MagmaParser.Representation_descriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_representation_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MagmaParser.STRING_UQ)
            self.state = 184
            self.match(MagmaParser.NEWLINE)
            self.state = 185
            self.order_calculation()
            self.state = 186
            self.match(MagmaParser.NEWLINE)
            self.state = 187
            self.permutation()
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 188
                    self.match(MagmaParser.NEWLINE)
                    self.state = 189
                    self.permutation() 
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Export_durationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME(self):
            return self.getToken(MagmaParser.TIME, 0)

        def COLON(self):
            return self.getToken(MagmaParser.COLON, 0)

        def DECIMAL(self):
            return self.getToken(MagmaParser.DECIMAL, 0)

        def getRuleIndex(self):
            return MagmaParser.RULE_export_duration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExport_duration" ):
                listener.enterExport_duration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExport_duration" ):
                listener.exitExport_duration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExport_duration" ):
                return visitor.visitExport_duration(self)
            else:
                return visitor.visitChildren(self)




    def export_duration(self):

        localctx = MagmaParser.Export_durationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_export_duration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MagmaParser.TIME)
            self.state = 196
            self.match(MagmaParser.COLON)
            self.state = 197
            self.match(MagmaParser.DECIMAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.int_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def int_expression_sempred(self, localctx:Int_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




