# Generated from Regex.g4 by ANTLR 4.7.2
from antlr4 import *
from nfa import *
if __name__ is not None and "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegexParser#regex.
    def visitRegex(self, ctx:RegexParser.RegexContext):
        or_symbol = ctx.OR()
        concat = ctx.concat_regex()

        # daca avem cazul regex OR concat_regex
        if or_symbol:
            r = ctx.regex()

            regex = self.visit(r)
            conc = self.visit(concat)

            resultNFA = conc.reunion(regex)
        # daca nu, avem doar concat_regex
        else:
            resultNFA = self.visit(concat)
        
        return resultNFA

    # Visit a parse tree produced by RegexParser#concat_regex.
    def visitConcat_regex(self, ctx:RegexParser.Concat_regexContext):
        concat = ctx.concat_regex()
        star = ctx.star_regex()
        
        # daca avem cazul concat_regex star_regex
        if concat:
            nfa1 = self.visit(concat)
            nfa2 = self.visit(star)

            resultNFA = nfa1.concatenate(nfa2)
        # daca nu, avem doar star_regex
        else:
            resultNFA = self.visit(star)

        return resultNFA

    # Visit a parse tree produced by RegexParser#star_regex.
    def visitStar_regex(self, ctx:RegexParser.Star_regexContext):
        atom = ctx.atom()
        star = ctx.STAR()
        
        # daca avem STAR
        if star:
            regex = self.visit(atom)
            resultNFA = regex.star()
        # daca nu, avem doar atom
        else:
            resultNFA = self.visit(atom)

        return resultNFA

    # Visit a parse tree produced by RegexParser#atom.
    def visitAtom(self, ctx:RegexParser.AtomContext):
        var = ctx.variable()
        inner = ctx.inner()

        nfa = None

        # daca atomul este variabila
        if var:
            nfa = self.visit(var)

        # sau daca atomul este un inner_regex
        if inner:
            nfa = self.visit(inner)

        return nfa

    # Visit a parse tree produced by RegexParser#variable.
    def visitVariable(self, ctx:RegexParser.VariableContext):
        # stim ca aici avem doar o variabila, cream NFA-ul de baza
        return createAtomNFA(str(ctx.VAR()))

    # Visit a parse tree produced by RegexParser#inner.
    def visitInner(self, ctx:RegexParser.InnerContext):
        # stim ca aici sigur avem un regex intre paranteze, deci
        # ignoram parantezele si tratam mai departe regexul
        regex = ctx.regex()
        return self.visit(regex)


del RegexParser