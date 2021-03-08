# Generated from Regex.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\64\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3\3\4\3\4\3")
        buf.write("\4\3\4\5\4(\n\4\3\5\3\5\5\5,\n\5\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\2\4\2\4\b\2\4\6\b\n\f\2\2\2\61\2\16\3\2\2\2\4\31")
        buf.write("\3\2\2\2\6\'\3\2\2\2\b+\3\2\2\2\n-\3\2\2\2\f/\3\2\2\2")
        buf.write("\16\17\b\2\1\2\17\20\5\4\3\2\20\26\3\2\2\2\21\22\f\3\2")
        buf.write("\2\22\23\7\5\2\2\23\25\5\4\3\2\24\21\3\2\2\2\25\30\3\2")
        buf.write("\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\3\3\2\2\2\30\26\3")
        buf.write("\2\2\2\31\32\b\3\1\2\32\33\5\6\4\2\33 \3\2\2\2\34\35\f")
        buf.write("\3\2\2\35\37\5\6\4\2\36\34\3\2\2\2\37\"\3\2\2\2 \36\3")
        buf.write("\2\2\2 !\3\2\2\2!\5\3\2\2\2\" \3\2\2\2#(\5\b\5\2$%\5\b")
        buf.write("\5\2%&\7\3\2\2&(\3\2\2\2\'#\3\2\2\2\'$\3\2\2\2(\7\3\2")
        buf.write("\2\2),\5\n\6\2*,\5\f\7\2+)\3\2\2\2+*\3\2\2\2,\t\3\2\2")
        buf.write("\2-.\7\t\2\2.\13\3\2\2\2/\60\7\6\2\2\60\61\5\2\2\2\61")
        buf.write("\62\7\7\2\2\62\r\3\2\2\2\6\26 \'+")
        return buf.getvalue()


class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'|'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "STAR", "DOUBLESTAR", "OR", "OPEN", "CLOSED", 
                      "WHITESPACE", "VAR" ]

    RULE_regex = 0
    RULE_concat_regex = 1
    RULE_star_regex = 2
    RULE_atom = 3
    RULE_variable = 4
    RULE_inner = 5

    ruleNames =  [ "regex", "concat_regex", "star_regex", "atom", "variable", 
                   "inner" ]

    EOF = Token.EOF
    STAR=1
    DOUBLESTAR=2
    OR=3
    OPEN=4
    CLOSED=5
    WHITESPACE=6
    VAR=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RegexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat_regex(self):
            return self.getTypedRuleContext(RegexParser.Concat_regexContext,0)


        def regex(self):
            return self.getTypedRuleContext(RegexParser.RegexContext,0)


        def OR(self):
            return self.getToken(RegexParser.OR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_regex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)



    def regex(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.RegexContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_regex, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.concat_regex(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegexParser.RegexContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_regex)
                    self.state = 15
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 16
                    self.match(RegexParser.OR)
                    self.state = 17
                    self.concat_regex(0) 
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Concat_regexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_regex(self):
            return self.getTypedRuleContext(RegexParser.Star_regexContext,0)


        def concat_regex(self):
            return self.getTypedRuleContext(RegexParser.Concat_regexContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_concat_regex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_regex" ):
                return visitor.visitConcat_regex(self)
            else:
                return visitor.visitChildren(self)



    def concat_regex(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.Concat_regexContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_concat_regex, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.star_regex()
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegexParser.Concat_regexContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_concat_regex)
                    self.state = 26
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 27
                    self.star_regex() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Star_regexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(RegexParser.AtomContext,0)


        def STAR(self):
            return self.getToken(RegexParser.STAR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_star_regex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar_regex" ):
                return visitor.visitStar_regex(self)
            else:
                return visitor.visitChildren(self)




    def star_regex(self):

        localctx = RegexParser.Star_regexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_star_regex)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.atom()
                self.state = 35
                self.match(RegexParser.STAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(RegexParser.VariableContext,0)


        def inner(self):
            return self.getTypedRuleContext(RegexParser.InnerContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = RegexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.variable()
                pass
            elif token in [RegexParser.OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.inner()
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

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(RegexParser.VAR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = RegexParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(RegexParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InnerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(RegexParser.OPEN, 0)

        def regex(self):
            return self.getTypedRuleContext(RegexParser.RegexContext,0)


        def CLOSED(self):
            return self.getToken(RegexParser.CLOSED, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_inner

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInner" ):
                return visitor.visitInner(self)
            else:
                return visitor.visitChildren(self)




    def inner(self):

        localctx = RegexParser.InnerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inner)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(RegexParser.OPEN)
            self.state = 46
            self.regex(0)
            self.state = 47
            self.match(RegexParser.CLOSED)
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
        self._predicates[0] = self.regex_sempred
        self._predicates[1] = self.concat_regex_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def regex_sempred(self, localctx:RegexContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def concat_regex_sempred(self, localctx:Concat_regexContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




