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
        4,1,28,267,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,3,0,38,8,0,1,1,1,1,1,1,
        5,1,43,8,1,10,1,12,1,46,9,1,1,1,1,1,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,1,1,1,5,1,58,8,1,10,1,12,1,61,9,1,1,1,1,1,5,1,65,8,1,10,1,
        12,1,68,9,1,1,1,5,1,71,8,1,10,1,12,1,74,9,1,1,2,1,2,3,2,78,8,2,1,
        2,3,2,81,8,2,1,2,1,2,1,2,3,2,86,8,2,1,2,5,2,89,8,2,10,2,12,2,92,
        9,2,1,2,3,2,95,8,2,1,2,3,2,98,8,2,1,2,1,2,1,2,1,2,3,2,104,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,116,8,3,1,3,1,3,1,4,1,
        4,1,4,3,4,123,8,4,1,4,5,4,126,8,4,10,4,12,4,129,9,4,1,5,1,5,1,5,
        1,5,1,5,3,5,136,8,5,1,6,1,6,1,6,1,6,5,6,142,8,6,10,6,12,6,145,9,
        6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,157,8,8,1,9,1,9,1,
        9,1,9,5,9,163,8,9,10,9,12,9,166,9,9,1,9,1,9,3,9,170,8,9,1,10,4,10,
        173,8,10,11,10,12,10,174,1,11,1,11,1,11,1,11,5,11,181,8,11,10,11,
        12,11,184,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,
        195,8,12,10,12,12,12,198,9,12,1,13,1,13,1,14,1,14,1,14,3,14,205,
        8,14,1,14,1,14,1,14,1,14,1,14,3,14,212,8,14,1,14,1,14,1,14,1,14,
        3,14,218,8,14,3,14,220,8,14,1,15,1,15,1,15,3,15,225,8,15,1,15,1,
        15,1,15,1,15,1,15,1,15,3,15,233,8,15,1,15,1,15,1,15,1,15,3,15,239,
        8,15,1,15,1,15,1,15,1,15,5,15,245,8,15,10,15,12,15,248,9,15,1,15,
        1,15,1,15,1,15,4,15,254,8,15,11,15,12,15,255,3,15,258,8,15,1,16,
        1,16,1,16,1,16,1,16,3,16,265,8,16,1,16,0,1,24,17,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,0,1,2,0,12,12,14,14,289,0,37,1,0,0,
        0,2,44,1,0,0,0,4,103,1,0,0,0,6,105,1,0,0,0,8,119,1,0,0,0,10,130,
        1,0,0,0,12,137,1,0,0,0,14,146,1,0,0,0,16,156,1,0,0,0,18,169,1,0,
        0,0,20,172,1,0,0,0,22,176,1,0,0,0,24,187,1,0,0,0,26,199,1,0,0,0,
        28,219,1,0,0,0,30,221,1,0,0,0,32,264,1,0,0,0,34,38,1,0,0,0,35,38,
        3,2,1,0,36,38,5,0,0,1,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,
        38,1,1,0,0,0,39,40,3,32,16,0,40,41,5,15,0,0,41,43,1,0,0,0,42,39,
        1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,
        46,44,1,0,0,0,47,59,3,4,2,0,48,49,5,15,0,0,49,51,3,32,16,0,50,48,
        1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,
        54,52,1,0,0,0,55,56,5,15,0,0,56,58,3,4,2,0,57,52,1,0,0,0,58,61,1,
        0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,66,1,0,0,0,61,59,1,0,0,0,62,
        63,5,15,0,0,63,65,3,32,16,0,64,62,1,0,0,0,65,68,1,0,0,0,66,64,1,
        0,0,0,66,67,1,0,0,0,67,72,1,0,0,0,68,66,1,0,0,0,69,71,5,15,0,0,70,
        69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,3,1,0,0,
        0,74,72,1,0,0,0,75,77,5,5,0,0,76,78,5,12,0,0,77,76,1,0,0,0,77,78,
        1,0,0,0,78,80,1,0,0,0,79,81,5,15,0,0,80,79,1,0,0,0,80,81,1,0,0,0,
        81,82,1,0,0,0,82,90,3,16,8,0,83,85,5,8,0,0,84,86,5,15,0,0,85,84,
        1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,89,3,16,8,0,88,83,1,0,0,0,
        89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,94,1,0,0,0,92,90,1,
        0,0,0,93,95,5,15,0,0,94,93,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,
        98,5,12,0,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,6,
        0,0,100,104,1,0,0,0,101,102,5,5,0,0,102,104,5,6,0,0,103,75,1,0,0,
        0,103,101,1,0,0,0,104,5,1,0,0,0,105,106,5,20,0,0,106,107,5,1,0,0,
        107,108,5,21,0,0,108,109,5,1,0,0,109,110,3,8,4,0,110,111,5,2,0,0,
        111,112,5,9,0,0,112,113,5,15,0,0,113,115,3,12,6,0,114,116,5,15,0,
        0,115,114,1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,118,5,2,0,
        0,118,7,1,0,0,0,119,127,3,10,5,0,120,122,5,8,0,0,121,123,5,15,0,
        0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,126,3,10,5,
        0,125,120,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,
        0,128,9,1,0,0,0,129,127,1,0,0,0,130,135,5,27,0,0,131,132,5,7,0,0,
        132,133,5,27,0,0,133,134,5,3,0,0,134,136,5,4,0,0,135,131,1,0,0,0,
        135,136,1,0,0,0,136,11,1,0,0,0,137,143,3,14,7,0,138,139,5,8,0,0,
        139,140,5,15,0,0,140,142,3,14,7,0,141,138,1,0,0,0,142,145,1,0,0,
        0,143,141,1,0,0,0,143,144,1,0,0,0,144,13,1,0,0,0,145,143,1,0,0,0,
        146,147,5,27,0,0,147,148,5,11,0,0,148,149,3,16,8,0,149,15,1,0,0,
        0,150,157,5,17,0,0,151,157,5,16,0,0,152,157,3,18,9,0,153,157,3,6,
        3,0,154,157,3,4,2,0,155,157,3,30,15,0,156,150,1,0,0,0,156,151,1,
        0,0,0,156,152,1,0,0,0,156,153,1,0,0,0,156,154,1,0,0,0,156,155,1,
        0,0,0,157,17,1,0,0,0,158,159,5,1,0,0,159,164,5,17,0,0,160,161,5,
        8,0,0,161,163,5,17,0,0,162,160,1,0,0,0,163,166,1,0,0,0,164,162,1,
        0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,167,170,5,
        2,0,0,168,170,5,18,0,0,169,158,1,0,0,0,169,168,1,0,0,0,170,19,1,
        0,0,0,171,173,3,22,11,0,172,171,1,0,0,0,173,174,1,0,0,0,174,172,
        1,0,0,0,174,175,1,0,0,0,175,21,1,0,0,0,176,177,5,3,0,0,177,182,5,
        17,0,0,178,179,5,8,0,0,179,181,5,17,0,0,180,178,1,0,0,0,181,184,
        1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,
        1,0,0,0,185,186,5,4,0,0,186,23,1,0,0,0,187,188,6,12,-1,0,188,189,
        5,17,0,0,189,196,1,0,0,0,190,191,10,1,0,0,191,192,3,26,13,0,192,
        193,3,24,12,2,193,195,1,0,0,0,194,190,1,0,0,0,195,198,1,0,0,0,196,
        194,1,0,0,0,196,197,1,0,0,0,197,25,1,0,0,0,198,196,1,0,0,0,199,200,
        7,0,0,0,200,27,1,0,0,0,201,204,5,24,0,0,202,203,5,14,0,0,203,205,
        5,17,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,206,1,0,0,0,206,207,
        5,10,0,0,207,220,5,25,0,0,208,211,5,24,0,0,209,210,5,14,0,0,210,
        212,5,17,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,
        214,5,10,0,0,214,217,5,24,0,0,215,216,5,14,0,0,216,218,5,17,0,0,
        217,215,1,0,0,0,217,218,1,0,0,0,218,220,1,0,0,0,219,201,1,0,0,0,
        219,208,1,0,0,0,220,29,1,0,0,0,221,224,5,26,0,0,222,223,5,10,0,0,
        223,225,3,24,12,0,224,222,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,
        0,226,238,5,15,0,0,227,228,5,27,0,0,228,229,5,10,0,0,229,232,5,17,
        0,0,230,231,5,10,0,0,231,233,3,24,12,0,232,230,1,0,0,0,232,233,1,
        0,0,0,233,239,1,0,0,0,234,235,5,27,0,0,235,236,5,13,0,0,236,237,
        5,27,0,0,237,239,5,7,0,0,238,227,1,0,0,0,238,234,1,0,0,0,239,257,
        1,0,0,0,240,241,5,15,0,0,241,242,3,28,14,0,242,243,5,8,0,0,243,245,
        1,0,0,0,244,240,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,
        1,0,0,0,247,249,1,0,0,0,248,246,1,0,0,0,249,250,5,15,0,0,250,258,
        3,28,14,0,251,252,5,15,0,0,252,254,3,20,10,0,253,251,1,0,0,0,254,
        255,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,258,1,0,0,0,257,
        246,1,0,0,0,257,253,1,0,0,0,258,31,1,0,0,0,259,260,5,22,0,0,260,
        261,5,7,0,0,261,265,5,19,0,0,262,263,5,26,0,0,263,265,5,7,0,0,264,
        259,1,0,0,0,264,262,1,0,0,0,265,33,1,0,0,0,35,37,44,52,59,66,72,
        77,80,85,90,94,97,103,115,122,127,135,143,156,164,169,174,182,196,
        204,211,217,219,224,232,238,246,255,257,264
    ]

class MagmaParser ( Parser ):

    grammarFileName = "MagmaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'('", "')'", "'['", "']'", 
                     "':'", "','", "'|'", "'='", "':='", "'*'", "'-'", "'^'", 
                     "'\\n'", "<INVALID>", "<INVALID>", "'unknown'", "<INVALID>", 
                     "'rec'", "'recformat'", "'Time'", "'Degree'", "<INVALID>", 
                     "'Id($)'" ]

    symbolicNames = [ "<INVALID>", "LANGLE", "RANGLE", "LPAREN", "RPAREN", 
                      "LSQUARE", "RSQUARE", "COLON", "COMMA", "PIPE", "EQ", 
                      "DEF", "MULT", "MINUS", "EXP", "NEWLINE", "BOOLEAN", 
                      "INT", "UNKNOWN", "DECIMAL", "RECORD", "RECORD_FORMAT", 
                      "TIME", "DEGREE", "GENERATOR", "IDENDITY", "STRING_UQ", 
                      "ID", "WS" ]

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
    RULE_int_expression = 12
    RULE_int_operation = 13
    RULE_relation = 14
    RULE_multiline_value = 15
    RULE_metadata = 16

    ruleNames =  [ "magma", "outputs", "array", "record", "record_formats", 
                   "record_format", "defs", "def", "value", "group", "permutation", 
                   "permutation_part", "int_expression", "int_operation", 
                   "relation", "multiline_value", "metadata" ]

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
    MINUS=13
    EXP=14
    NEWLINE=15
    BOOLEAN=16
    INT=17
    UNKNOWN=18
    DECIMAL=19
    RECORD=20
    RECORD_FORMAT=21
    TIME=22
    DEGREE=23
    GENERATOR=24
    IDENDITY=25
    STRING_UQ=26
    ID=27
    WS=28

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


        def metadata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.MetadataContext)
            else:
                return self.getTypedRuleContext(MagmaParser.MetadataContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.NEWLINE)
            else:
                return self.getToken(MagmaParser.NEWLINE, i)

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
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==26:
                self.state = 39
                self.metadata()
                self.state = 40
                self.match(MagmaParser.NEWLINE)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.array()
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 52
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 48
                            self.match(MagmaParser.NEWLINE)
                            self.state = 49
                            self.metadata() 
                        self.state = 54
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    self.state = 55
                    self.match(MagmaParser.NEWLINE)
                    self.state = 56
                    self.array() 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62
                    self.match(MagmaParser.NEWLINE)
                    self.state = 63
                    self.metadata() 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 69
                self.match(MagmaParser.NEWLINE)
                self.state = 74
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(MagmaParser.LSQUARE)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 76
                    self.match(MagmaParser.MULT)


                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 79
                    self.match(MagmaParser.NEWLINE)


                self.state = 82
                self.value()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 83
                    self.match(MagmaParser.COMMA)
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==15:
                        self.state = 84
                        self.match(MagmaParser.NEWLINE)


                    self.state = 87
                    self.value()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 93
                    self.match(MagmaParser.NEWLINE)


                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 96
                    self.match(MagmaParser.MULT)


                self.state = 99
                self.match(MagmaParser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(MagmaParser.LSQUARE)
                self.state = 102
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
            self.state = 105
            self.match(MagmaParser.RECORD)
            self.state = 106
            self.match(MagmaParser.LANGLE)
            self.state = 107
            self.match(MagmaParser.RECORD_FORMAT)
            self.state = 108
            self.match(MagmaParser.LANGLE)
            self.state = 109
            self.record_formats()
            self.state = 110
            self.match(MagmaParser.RANGLE)
            self.state = 111
            self.match(MagmaParser.PIPE)
            self.state = 112
            self.match(MagmaParser.NEWLINE)
            self.state = 113
            self.defs()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 114
                self.match(MagmaParser.NEWLINE)


            self.state = 117
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
            self.state = 119
            self.record_format()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 120
                self.match(MagmaParser.COMMA)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 121
                    self.match(MagmaParser.NEWLINE)


                self.state = 124
                self.record_format()
                self.state = 129
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
            self.state = 130
            self.match(MagmaParser.ID)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 131
                self.match(MagmaParser.COLON)
                self.state = 132
                self.match(MagmaParser.ID)
                self.state = 133
                self.match(MagmaParser.LPAREN)
                self.state = 134
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
            self.state = 137
            self.def_()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 138
                self.match(MagmaParser.COMMA)
                self.state = 139
                self.match(MagmaParser.NEWLINE)
                self.state = 140
                self.def_()
                self.state = 145
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
            self.state = 146
            self.match(MagmaParser.ID)
            self.state = 147
            self.match(MagmaParser.DEF)
            self.state = 148
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


        def multiline_value(self):
            return self.getTypedRuleContext(MagmaParser.Multiline_valueContext,0)


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
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(MagmaParser.INT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(MagmaParser.BOOLEAN)
                pass
            elif token in [1, 18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.group()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.record()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 154
                self.array()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 155
                self.multiline_value()
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

        def UNKNOWN(self):
            return self.getToken(MagmaParser.UNKNOWN, 0)

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
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(MagmaParser.LANGLE)
                self.state = 159
                self.match(MagmaParser.INT)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 160
                    self.match(MagmaParser.COMMA)
                    self.state = 161
                    self.match(MagmaParser.INT)
                    self.state = 166
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 167
                self.match(MagmaParser.RANGLE)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(MagmaParser.UNKNOWN)
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
            self.state = 172 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 171
                self.permutation_part()
                self.state = 174 
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
            self.state = 176
            self.match(MagmaParser.LPAREN)
            self.state = 177
            self.match(MagmaParser.INT)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 178
                self.match(MagmaParser.COMMA)
                self.state = 179
                self.match(MagmaParser.INT)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(MagmaParser.RPAREN)
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_int_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MagmaParser.INT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MagmaParser.Int_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expression)
                    self.state = 190
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 191
                    self.int_operation()
                    self.state = 192
                    self.int_expression(2) 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_int_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not(_la==12 or _la==14):
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


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GENERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.GENERATOR)
            else:
                return self.getToken(MagmaParser.GENERATOR, i)

        def EQ(self):
            return self.getToken(MagmaParser.EQ, 0)

        def IDENDITY(self):
            return self.getToken(MagmaParser.IDENDITY, 0)

        def EXP(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.EXP)
            else:
                return self.getToken(MagmaParser.EXP, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.INT)
            else:
                return self.getToken(MagmaParser.INT, i)

        def getRuleIndex(self):
            return MagmaParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = MagmaParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(MagmaParser.GENERATOR)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 202
                    self.match(MagmaParser.EXP)
                    self.state = 203
                    self.match(MagmaParser.INT)


                self.state = 206
                self.match(MagmaParser.EQ)
                self.state = 207
                self.match(MagmaParser.IDENDITY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(MagmaParser.GENERATOR)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 209
                    self.match(MagmaParser.EXP)
                    self.state = 210
                    self.match(MagmaParser.INT)


                self.state = 213
                self.match(MagmaParser.EQ)
                self.state = 214
                self.match(MagmaParser.GENERATOR)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 215
                    self.match(MagmaParser.EXP)
                    self.state = 216
                    self.match(MagmaParser.INT)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiline_valueContext(ParserRuleContext):
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.ID)
            else:
                return self.getToken(MagmaParser.ID, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.EQ)
            else:
                return self.getToken(MagmaParser.EQ, i)

        def INT(self):
            return self.getToken(MagmaParser.INT, 0)

        def MINUS(self):
            return self.getToken(MagmaParser.MINUS, 0)

        def COLON(self):
            return self.getToken(MagmaParser.COLON, 0)

        def relation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.RelationContext)
            else:
                return self.getTypedRuleContext(MagmaParser.RelationContext,i)


        def int_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.Int_expressionContext)
            else:
                return self.getTypedRuleContext(MagmaParser.Int_expressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MagmaParser.COMMA)
            else:
                return self.getToken(MagmaParser.COMMA, i)

        def permutation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MagmaParser.PermutationContext)
            else:
                return self.getTypedRuleContext(MagmaParser.PermutationContext,i)


        def getRuleIndex(self):
            return MagmaParser.RULE_multiline_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiline_value" ):
                listener.enterMultiline_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiline_value" ):
                listener.exitMultiline_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiline_value" ):
                return visitor.visitMultiline_value(self)
            else:
                return visitor.visitChildren(self)




    def multiline_value(self):

        localctx = MagmaParser.Multiline_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_multiline_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MagmaParser.STRING_UQ)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 222
                self.match(MagmaParser.EQ)
                self.state = 223
                self.int_expression(0)


            self.state = 226
            self.match(MagmaParser.NEWLINE)
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 227
                self.match(MagmaParser.ID)
                self.state = 228
                self.match(MagmaParser.EQ)
                self.state = 229
                self.match(MagmaParser.INT)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 230
                    self.match(MagmaParser.EQ)
                    self.state = 231
                    self.int_expression(0)


                pass

            elif la_ == 2:
                self.state = 234
                self.match(MagmaParser.ID)
                self.state = 235
                self.match(MagmaParser.MINUS)
                self.state = 236
                self.match(MagmaParser.ID)
                self.state = 237
                self.match(MagmaParser.COLON)
                pass


            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 240
                        self.match(MagmaParser.NEWLINE)
                        self.state = 241
                        self.relation()
                        self.state = 242
                        self.match(MagmaParser.COMMA) 
                    self.state = 248
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                self.state = 249
                self.match(MagmaParser.NEWLINE)
                self.state = 250
                self.relation()
                pass

            elif la_ == 2:
                self.state = 253 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 251
                        self.match(MagmaParser.NEWLINE)
                        self.state = 252
                        self.permutation()

                    else:
                        raise NoViableAltException(self)
                    self.state = 255 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetadataContext(ParserRuleContext):
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

        def STRING_UQ(self):
            return self.getToken(MagmaParser.STRING_UQ, 0)

        def getRuleIndex(self):
            return MagmaParser.RULE_metadata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadata" ):
                listener.enterMetadata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadata" ):
                listener.exitMetadata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetadata" ):
                return visitor.visitMetadata(self)
            else:
                return visitor.visitChildren(self)




    def metadata(self):

        localctx = MagmaParser.MetadataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_metadata)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(MagmaParser.TIME)
                self.state = 260
                self.match(MagmaParser.COLON)
                self.state = 261
                self.match(MagmaParser.DECIMAL)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.match(MagmaParser.STRING_UQ)
                self.state = 263
                self.match(MagmaParser.COLON)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.int_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def int_expression_sempred(self, localctx:Int_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




