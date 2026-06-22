# Generated from SolveSel.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\7\f<\n\f\f\f\16\f?\13\f\3\r\6\rB")
        buf.write("\n\r\r\r\16\rC\3\r\3\r\6\rH\n\r\r\r\16\rI\5\rL\n\r\3\16")
        buf.write("\6\16O\n\16\r\16\16\16P\3\16\3\16\2\2\17\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2")
        buf.write("\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"")
        buf.write("\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t\'\3\2")
        buf.write("\2\2\13)\3\2\2\2\r+\3\2\2\2\17\61\3\2\2\2\21\63\3\2\2")
        buf.write("\2\23\65\3\2\2\2\25\67\3\2\2\2\279\3\2\2\2\31A\3\2\2\2")
        buf.write("\33N\3\2\2\2\35\36\7?\2\2\36\4\3\2\2\2\37 \7=\2\2 \6\3")
        buf.write("\2\2\2!\"\7u\2\2\"#\7q\2\2#$\7n\2\2$%\7x\2\2%&\7g\2\2")
        buf.write("&\b\3\2\2\2\'(\7*\2\2(\n\3\2\2\2)*\7+\2\2*\f\3\2\2\2+")
        buf.write(",\7r\2\2,-\7t\2\2-.\7k\2\2./\7p\2\2/\60\7v\2\2\60\16\3")
        buf.write("\2\2\2\61\62\7,\2\2\62\20\3\2\2\2\63\64\7\61\2\2\64\22")
        buf.write("\3\2\2\2\65\66\7-\2\2\66\24\3\2\2\2\678\7/\2\28\26\3\2")
        buf.write("\2\29=\t\2\2\2:<\t\3\2\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2")
        buf.write("=>\3\2\2\2>\30\3\2\2\2?=\3\2\2\2@B\t\4\2\2A@\3\2\2\2B")
        buf.write("C\3\2\2\2CA\3\2\2\2CD\3\2\2\2DK\3\2\2\2EG\7\60\2\2FH\t")
        buf.write("\4\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2")
        buf.write("\2KE\3\2\2\2KL\3\2\2\2L\32\3\2\2\2MO\t\5\2\2NM\3\2\2\2")
        buf.write("OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\b\16\2\2S\34")
        buf.write("\3\2\2\2\b\2=CIKP\3\b\2\2")
        return buf.getvalue()


class SolveSelLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    ID = 11
    NUMBER = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'solve'", "'('", "')'", "'print'", "'*'", "'/'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "ID", "NUMBER", "WS" ]

    grammarFileName = "SolveSel.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


