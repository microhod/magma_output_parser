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
        4,1,24,209,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,3,0,38,8,0,1,1,1,1,1,1,
        3,1,43,8,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,3,1,54,8,
        1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,2,1,2,3,2,64,8,2,1,2,3,2,67,
        8,2,1,2,1,2,1,2,3,2,72,8,2,1,2,5,2,75,8,2,10,2,12,2,78,9,2,1,2,3,
        2,81,8,2,1,2,3,2,84,8,2,1,2,1,2,1,2,1,2,3,2,90,8,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,102,8,3,1,3,1,3,1,4,1,4,1,4,3,4,109,
        8,4,1,4,5,4,112,8,4,10,4,12,4,115,9,4,1,5,1,5,1,5,1,5,1,5,3,5,122,
        8,5,1,6,1,6,1,6,1,6,5,6,128,8,6,10,6,12,6,131,9,6,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,143,8,8,1,9,1,9,1,9,1,9,5,9,149,8,
        9,10,9,12,9,152,9,9,1,9,1,9,1,10,4,10,157,8,10,11,10,12,10,158,1,
        11,1,11,1,11,1,11,5,11,165,8,11,10,11,12,11,168,9,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,3,12,177,8,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,5,13,186,8,13,10,13,12,13,189,9,13,1,14,1,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,5,15,200,8,15,10,15,12,15,203,9,15,1,16,1,
        16,1,16,1,16,1,16,0,1,26,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,0,1,1,0,12,13,220,0,37,1,0,0,0,2,39,1,0,0,0,4,89,1,0,0,
        0,6,91,1,0,0,0,8,105,1,0,0,0,10,116,1,0,0,0,12,123,1,0,0,0,14,132,
        1,0,0,0,16,142,1,0,0,0,18,144,1,0,0,0,20,156,1,0,0,0,22,160,1,0,
        0,0,24,171,1,0,0,0,26,178,1,0,0,0,28,190,1,0,0,0,30,192,1,0,0,0,
        32,204,1,0,0,0,34,38,1,0,0,0,35,38,3,2,1,0,36,38,5,0,0,1,37,34,1,
        0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,1,1,0,0,0,39,48,3,4,2,0,40,
        41,5,14,0,0,41,43,3,32,16,0,42,40,1,0,0,0,42,43,1,0,0,0,43,44,1,
        0,0,0,44,45,5,14,0,0,45,47,3,4,2,0,46,42,1,0,0,0,47,50,1,0,0,0,48,
        46,1,0,0,0,48,49,1,0,0,0,49,53,1,0,0,0,50,48,1,0,0,0,51,52,5,14,
        0,0,52,54,3,32,16,0,53,51,1,0,0,0,53,54,1,0,0,0,54,58,1,0,0,0,55,
        57,5,14,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,
        0,0,59,3,1,0,0,0,60,58,1,0,0,0,61,63,5,5,0,0,62,64,5,12,0,0,63,62,
        1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,67,5,14,0,0,66,65,1,0,0,0,
        66,67,1,0,0,0,67,68,1,0,0,0,68,76,3,16,8,0,69,71,5,8,0,0,70,72,5,
        14,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,75,3,16,8,0,
        74,69,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,80,1,
        0,0,0,78,76,1,0,0,0,79,81,5,14,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,
        83,1,0,0,0,82,84,5,12,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,0,
        0,0,85,86,5,6,0,0,86,90,1,0,0,0,87,88,5,5,0,0,88,90,5,6,0,0,89,61,
        1,0,0,0,89,87,1,0,0,0,90,5,1,0,0,0,91,92,5,18,0,0,92,93,5,1,0,0,
        93,94,5,19,0,0,94,95,5,1,0,0,95,96,3,8,4,0,96,97,5,2,0,0,97,98,5,
        9,0,0,98,99,5,14,0,0,99,101,3,12,6,0,100,102,5,14,0,0,101,100,1,
        0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,2,0,0,104,7,1,0,
        0,0,105,113,3,10,5,0,106,108,5,8,0,0,107,109,5,14,0,0,108,107,1,
        0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,112,3,10,5,0,111,106,1,
        0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,9,1,0,
        0,0,115,113,1,0,0,0,116,121,5,23,0,0,117,118,5,7,0,0,118,119,5,23,
        0,0,119,120,5,3,0,0,120,122,5,4,0,0,121,117,1,0,0,0,121,122,1,0,
        0,0,122,11,1,0,0,0,123,129,3,14,7,0,124,125,5,8,0,0,125,126,5,14,
        0,0,126,128,3,14,7,0,127,124,1,0,0,0,128,131,1,0,0,0,129,127,1,0,
        0,0,129,130,1,0,0,0,130,13,1,0,0,0,131,129,1,0,0,0,132,133,5,23,
        0,0,133,134,5,11,0,0,134,135,3,16,8,0,135,15,1,0,0,0,136,143,5,16,
        0,0,137,143,5,15,0,0,138,143,3,18,9,0,139,143,3,6,3,0,140,143,3,
        4,2,0,141,143,3,30,15,0,142,136,1,0,0,0,142,137,1,0,0,0,142,138,
        1,0,0,0,142,139,1,0,0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,17,1,
        0,0,0,144,145,5,1,0,0,145,150,5,16,0,0,146,147,5,8,0,0,147,149,5,
        16,0,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,
        0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,154,5,2,0,0,154,19,1,0,
        0,0,155,157,3,22,11,0,156,155,1,0,0,0,157,158,1,0,0,0,158,156,1,
        0,0,0,158,159,1,0,0,0,159,21,1,0,0,0,160,161,5,3,0,0,161,166,5,16,
        0,0,162,163,5,8,0,0,163,165,5,16,0,0,164,162,1,0,0,0,165,168,1,0,
        0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,166,1,0,
        0,0,169,170,5,4,0,0,170,23,1,0,0,0,171,172,5,20,0,0,172,173,5,10,
        0,0,173,176,5,16,0,0,174,175,5,10,0,0,175,177,3,26,13,0,176,174,
        1,0,0,0,176,177,1,0,0,0,177,25,1,0,0,0,178,179,6,13,-1,0,179,180,
        5,16,0,0,180,187,1,0,0,0,181,182,10,1,0,0,182,183,3,28,14,0,183,
        184,3,26,13,2,184,186,1,0,0,0,185,181,1,0,0,0,186,189,1,0,0,0,187,
        185,1,0,0,0,187,188,1,0,0,0,188,27,1,0,0,0,189,187,1,0,0,0,190,191,
        7,0,0,0,191,29,1,0,0,0,192,193,5,22,0,0,193,194,5,14,0,0,194,195,
        3,24,12,0,195,196,5,14,0,0,196,201,3,20,10,0,197,198,5,14,0,0,198,
        200,3,20,10,0,199,197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,
        202,1,0,0,0,202,31,1,0,0,0,203,201,1,0,0,0,204,205,5,21,0,0,205,
        206,5,7,0,0,206,207,5,17,0,0,207,33,1,0,0,0,24,37,42,48,53,58,63,
        66,71,76,80,83,89,101,108,113,121,129,142,150,158,166,176,187,201
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
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 40
                        self.match(MagmaParser.NEWLINE)
                        self.state = 41
                        self.export_duration()


                    self.state = 44
                    self.match(MagmaParser.NEWLINE)
                    self.state = 45
                    self.array() 
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 51
                self.match(MagmaParser.NEWLINE)
                self.state = 52
                self.export_duration()


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 55
                self.match(MagmaParser.NEWLINE)
                self.state = 60
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
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(MagmaParser.LSQUARE)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 62
                    self.match(MagmaParser.MULT)


                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 65
                    self.match(MagmaParser.NEWLINE)


                self.state = 68
                self.value()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 69
                    self.match(MagmaParser.COMMA)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==14:
                        self.state = 70
                        self.match(MagmaParser.NEWLINE)


                    self.state = 73
                    self.value()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 79
                    self.match(MagmaParser.NEWLINE)


                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 82
                    self.match(MagmaParser.MULT)


                self.state = 85
                self.match(MagmaParser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(MagmaParser.LSQUARE)
                self.state = 88
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
            self.state = 91
            self.match(MagmaParser.RECORD)
            self.state = 92
            self.match(MagmaParser.LANGLE)
            self.state = 93
            self.match(MagmaParser.RECORD_FORMAT)
            self.state = 94
            self.match(MagmaParser.LANGLE)
            self.state = 95
            self.record_formats()
            self.state = 96
            self.match(MagmaParser.RANGLE)
            self.state = 97
            self.match(MagmaParser.PIPE)
            self.state = 98
            self.match(MagmaParser.NEWLINE)
            self.state = 99
            self.defs()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 100
                self.match(MagmaParser.NEWLINE)


            self.state = 103
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
            self.state = 105
            self.record_format()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 106
                self.match(MagmaParser.COMMA)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 107
                    self.match(MagmaParser.NEWLINE)


                self.state = 110
                self.record_format()
                self.state = 115
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
            self.state = 116
            self.match(MagmaParser.ID)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 117
                self.match(MagmaParser.COLON)
                self.state = 118
                self.match(MagmaParser.ID)
                self.state = 119
                self.match(MagmaParser.LPAREN)
                self.state = 120
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
            self.state = 123
            self.def_()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 124
                self.match(MagmaParser.COMMA)
                self.state = 125
                self.match(MagmaParser.NEWLINE)
                self.state = 126
                self.def_()
                self.state = 131
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
            self.state = 132
            self.match(MagmaParser.ID)
            self.state = 133
            self.match(MagmaParser.DEF)
            self.state = 134
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
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(MagmaParser.INT)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(MagmaParser.BOOLEAN)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.group()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.record()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.array()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
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
            self.state = 144
            self.match(MagmaParser.LANGLE)
            self.state = 145
            self.match(MagmaParser.INT)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 146
                self.match(MagmaParser.COMMA)
                self.state = 147
                self.match(MagmaParser.INT)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
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
            self.state = 156 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 155
                self.permutation_part()
                self.state = 158 
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
            self.state = 160
            self.match(MagmaParser.LPAREN)
            self.state = 161
            self.match(MagmaParser.INT)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 162
                self.match(MagmaParser.COMMA)
                self.state = 163
                self.match(MagmaParser.INT)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
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
            self.state = 171
            self.match(MagmaParser.ORDER)
            self.state = 172
            self.match(MagmaParser.EQ)
            self.state = 173
            self.match(MagmaParser.INT)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 174
                self.match(MagmaParser.EQ)
                self.state = 175
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
            self.state = 179
            self.match(MagmaParser.INT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MagmaParser.Int_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expression)
                    self.state = 181
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 182
                    self.int_operation()
                    self.state = 183
                    self.int_expression(2) 
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 190
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
            self.state = 192
            self.match(MagmaParser.STRING_UQ)
            self.state = 193
            self.match(MagmaParser.NEWLINE)
            self.state = 194
            self.order_calculation()
            self.state = 195
            self.match(MagmaParser.NEWLINE)
            self.state = 196
            self.permutation()
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 197
                    self.match(MagmaParser.NEWLINE)
                    self.state = 198
                    self.permutation() 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 204
            self.match(MagmaParser.TIME)
            self.state = 205
            self.match(MagmaParser.COLON)
            self.state = 206
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
         




