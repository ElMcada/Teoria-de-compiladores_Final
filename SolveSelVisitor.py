from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SolveSelParser import SolveSelParser
else:
    from SolveSelParser import SolveSelParser

class SolveSelVisitor(ParseTreeVisitor):

    def visitRoot(self, ctx:SolveSelParser.RootContext):
        return self.visitChildren(ctx)

    def visitEcuacion(self, ctx:SolveSelParser.EcuacionContext):
        return self.visitChildren(ctx)

    def visitResolver(self, ctx:SolveSelParser.ResolverContext):
        return self.visitChildren(ctx)
    
    def visitMostrar(self, ctx:SolveSelParser.MostrarContext):
        return self.visitChildren(ctx)

    def visitMulDiv(self, ctx:SolveSelParser.MulDivContext):
        return self.visitChildren(ctx)
    
    def visitAddSub(self, ctx:SolveSelParser.AddSubContext):
        return self.visitChildren(ctx)

    def visitParens(self, ctx:SolveSelParser.ParensContext):
        return self.visitChildren(ctx)

    def visitAtom(self, ctx:SolveSelParser.AtomContext):
        return self.visitChildren(ctx)

    def visitCoeffVar(self, ctx:SolveSelParser.CoeffVarContext):
        return self.visitChildren(ctx)

    def visitSoloVar(self, ctx:SolveSelParser.SoloVarContext):
        return self.visitChildren(ctx)

    def visitSoloNum(self, ctx:SolveSelParser.SoloNumContext):
        return self.visitChildren(ctx)
del SolveSelParser