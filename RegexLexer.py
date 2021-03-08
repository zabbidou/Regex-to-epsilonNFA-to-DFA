# Generated from Regex.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write(")\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\5\2\24\n\2\3\3\6\3\27\n\3\r\3\16\3\30")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\"\n\7\r\7\16\7#\3\7\3")
        buf.write("\7\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\5\3")
        buf.write("\2,,\5\2\13\f\17\17\"\"\3\2c|\2+\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\3\23\3\2\2\2\5\26\3\2\2\2\7\32\3\2\2\2\t\34")
        buf.write("\3\2\2\2\13\36\3\2\2\2\r!\3\2\2\2\17\'\3\2\2\2\21\24\7")
        buf.write(",\2\2\22\24\5\5\3\2\23\21\3\2\2\2\23\22\3\2\2\2\24\4\3")
        buf.write("\2\2\2\25\27\t\2\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26")
        buf.write("\3\2\2\2\30\31\3\2\2\2\31\6\3\2\2\2\32\33\7~\2\2\33\b")
        buf.write("\3\2\2\2\34\35\7*\2\2\35\n\3\2\2\2\36\37\7+\2\2\37\f\3")
        buf.write("\2\2\2 \"\t\3\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2")
        buf.write("\2\2$%\3\2\2\2%&\b\7\2\2&\16\3\2\2\2\'(\t\4\2\2(\20\3")
        buf.write("\2\2\2\6\2\23\30#\3\b\2\2")
        return buf.getvalue()


class RegexLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STAR = 1
    DOUBLESTAR = 2
    OR = 3
    OPEN = 4
    CLOSED = 5
    WHITESPACE = 6
    VAR = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "STAR", "DOUBLESTAR", "OR", "OPEN", "CLOSED", "WHITESPACE", 
            "VAR" ]

    ruleNames = [ "STAR", "DOUBLESTAR", "OR", "OPEN", "CLOSED", "WHITESPACE", 
                  "VAR" ]

    grammarFileName = "Regex.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


