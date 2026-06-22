# Generated from SolveSel.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4)\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\61\n\4\f\4\16\4")
        buf.write("\64\13\4\3\5\3\5\3\5\3\5\5\5:\n\5\3\5\2\3\6\6\2\4\6\b")
        buf.write("\2\4\3\2\t\n\3\2\13\f\2?\2\r\3\2\2\2\4 \3\2\2\2\6(\3\2")
        buf.write("\2\2\b9\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\17\3\2\2\2")
        buf.write("\r\13\3\2\2\2\r\16\3\2\2\2\16\20\3\2\2\2\17\r\3\2\2\2")
        buf.write("\20\21\7\2\2\3\21\3\3\2\2\2\22\23\5\6\4\2\23\24\7\3\2")
        buf.write("\2\24\25\5\6\4\2\25\26\7\4\2\2\26!\3\2\2\2\27\30\7\5\2")
        buf.write("\2\30\31\7\6\2\2\31\32\7\r\2\2\32\33\7\7\2\2\33!\7\4\2")
        buf.write("\2\34\35\7\b\2\2\35\36\5\6\4\2\36\37\7\4\2\2\37!\3\2\2")
        buf.write("\2 \22\3\2\2\2 \27\3\2\2\2 \34\3\2\2\2!\5\3\2\2\2\"#\b")
        buf.write("\4\1\2#)\5\b\5\2$%\7\6\2\2%&\5\6\4\2&\'\7\7\2\2\')\3\2")
        buf.write("\2\2(\"\3\2\2\2($\3\2\2\2)\62\3\2\2\2*+\f\6\2\2+,\t\2")
        buf.write("\2\2,\61\5\6\4\7-.\f\5\2\2./\t\3\2\2/\61\5\6\4\6\60*\3")
        buf.write("\2\2\2\60-\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3")
        buf.write("\2\2\2\63\7\3\2\2\2\64\62\3\2\2\2\65\66\7\16\2\2\66:\7")
        buf.write("\r\2\2\67:\7\r\2\28:\7\16\2\29\65\3\2\2\29\67\3\2\2\2")
        buf.write("98\3\2\2\2:\t\3\2\2\2\b\r (\60\629")
        return buf.getvalue()


class SolveSelParser ( Parser ):

    grammarFileName = "SolveSel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'solve'", "'('", "')'", 
                     "'print'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "WS" ]

    RULE_root = 0
    RULE_action = 1
    RULE_expr = 2
    RULE_term = 3

    ruleNames =  [ "root", "action", "expr", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    NUMBER=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SolveSelParser.EOF, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SolveSelParser.ActionContext)
            else:
                return self.getTypedRuleContext(SolveSelParser.ActionContext,i)


        def getRuleIndex(self):
            return SolveSelParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SolveSelParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SolveSelParser.T__2) | (1 << SolveSelParser.T__3) | (1 << SolveSelParser.T__5) | (1 << SolveSelParser.ID) | (1 << SolveSelParser.NUMBER))) != 0):
                self.state = 8
                self.action()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(SolveSelParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SolveSelParser.RULE_action

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ResolverContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SolveSelParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResolver" ):
                return visitor.visitResolver(self)
            else:
                return visitor.visitChildren(self)


    class MostrarContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SolveSelParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMostrar" ):
                return visitor.visitMostrar(self)
            else:
                return visitor.visitChildren(self)


    class EcuacionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SolveSelParser.ExprContext)
            else:
                return self.getTypedRuleContext(SolveSelParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEcuacion" ):
                return visitor.visitEcuacion(self)
            else:
                return visitor.visitChildren(self)



    def action(self):

        localctx = SolveSelParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_action)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SolveSelParser.T__3, SolveSelParser.ID, SolveSelParser.NUMBER]:
                localctx = SolveSelParser.EcuacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(SolveSelParser.T__0)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(SolveSelParser.T__1)
                pass
            elif token in [SolveSelParser.T__2]:
                localctx = SolveSelParser.ResolverContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(SolveSelParser.T__2)
                self.state = 22
                self.match(SolveSelParser.T__3)
                self.state = 23
                self.match(SolveSelParser.ID)
                self.state = 24
                self.match(SolveSelParser.T__4)
                self.state = 25
                self.match(SolveSelParser.T__1)
                pass
            elif token in [SolveSelParser.T__5]:
                localctx = SolveSelParser.MostrarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(SolveSelParser.T__5)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(SolveSelParser.T__1)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SolveSelParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SolveSelParser.ExprContext)
            else:
                return self.getTypedRuleContext(SolveSelParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SolveSelParser.ExprContext)
            else:
                return self.getTypedRuleContext(SolveSelParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SolveSelParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(SolveSelParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SolveSelParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SolveSelParser.ID, SolveSelParser.NUMBER]:
                localctx = SolveSelParser.AtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 33
                self.term()
                pass
            elif token in [SolveSelParser.T__3]:
                localctx = SolveSelParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(SolveSelParser.T__3)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(SolveSelParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 46
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SolveSelParser.MulDivContext(self, SolveSelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SolveSelParser.T__6 or _la==SolveSelParser.T__7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SolveSelParser.AddSubContext(self, SolveSelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 44
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SolveSelParser.T__8 or _la==SolveSelParser.T__9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expr(4)
                        pass

             
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SolveSelParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SoloNumContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(SolveSelParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoloNum" ):
                return visitor.visitSoloNum(self)
            else:
                return visitor.visitChildren(self)


    class CoeffVarContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(SolveSelParser.NUMBER, 0)
        def ID(self):
            return self.getToken(SolveSelParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoeffVar" ):
                return visitor.visitCoeffVar(self)
            else:
                return visitor.visitChildren(self)


    class SoloVarContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SolveSelParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SolveSelParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoloVar" ):
                return visitor.visitSoloVar(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = SolveSelParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = SolveSelParser.CoeffVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(SolveSelParser.NUMBER)
                self.state = 52
                self.match(SolveSelParser.ID)
                pass

            elif la_ == 2:
                localctx = SolveSelParser.SoloVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(SolveSelParser.ID)
                pass

            elif la_ == 3:
                localctx = SolveSelParser.SoloNumContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(SolveSelParser.NUMBER)
                pass


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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




