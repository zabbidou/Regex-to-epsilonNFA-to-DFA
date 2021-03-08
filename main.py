import sys
from nfa import *
from antlr4 import *
from RegexLexer import RegexLexer
from RegexParser import RegexParser
from RegexVisitor import RegexVisitor

input = FileStream(sys.argv[1])
lexer = RegexLexer(input)
stream = CommonTokenStream(lexer)
parser = RegexParser(stream)

tree = parser.regex()

visitor = RegexVisitor()

# construim nfa-ul
nfa = visitor.visit(tree)

# printam nfa-ul
nfa.printToFile(sys.argv[2])

# facem transformarea nfa->dfa
dfa = nfaToDfa(nfa)

# scrierea in fisier
dfa.printDFA(sys.argv[3])