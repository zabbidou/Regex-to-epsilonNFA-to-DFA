import sys
from typing import NewType

# variabila pentru a memora inchiderile epsilon ale tuturor starilor
epsilon = []
# alfabetul NFA-ului
alphabet = set()
# helper pt redenumirea starilor DFA-ului
statesRename = {}
# helper pt redenumirea starilor DFA-ului
stateIndex = 0

class NFA:
    def __init__(self, l = None):
        if l is None: # empty constructor
            self.nrOfStates = 0
            self.final = 0
            self.trans = {}
        else:
            # numarul de stari
            self.nrOfStates = int(l[0][0])
            # lista de stari finale
            self.final = int(l[1][0])
            # tranzitiile
            self.trans = {}

            # luam fiecare lista si o impartim in stare, simbol, iar ce a ramas intra in lista next_states
            for state, symbol, *next_states in l[2:]:
                self.trans[(int(state), symbol)] = list(map(int, next_states))
                if symbol != "eps":
                    alphabet.add(symbol)

    def reunion(self, nfa2: 'NFA') -> 'NFA':
        nfa1 = self
        # tinem minte start si end de la fiecare (ca sa fie mai usor)
        # de urmarit codul
        start1 = 0
        start2 = 0
        end1 = nfa1.nrOfStates - 1
        end2 = nfa2.nrOfStates - 1

        # offsetam cu 1
        nfa1.offsetStatesByN(1)
        start1 = 1
        end1 = end1 + 1

        # codificam starile nfa-ului 2 in continuarea celor din nfa1
        nfa2.offsetStatesByN(nfa1.nrOfStates + 1)
        start2 = nfa1.nrOfStates + 1
        end2 = nfa1.nrOfStates + nfa2.nrOfStates

        # construim noul NFA, combinand starile/tranzitiile din cele 2 nfa-uri
        # si facand legaturile cu noile start/end
        resultNFA = NFA()

        newFinal = end2 + 1

        newTrans = nfa1.trans.copy()
        newTrans[(0, 'eps')] = [start1, start2]
        newTrans.update(nfa2.trans)
        newTrans[(end1, 'eps')] = [newFinal]
        newTrans[(end2, 'eps')] = [newFinal]

        resultNFA.final = newFinal
        resultNFA.nrOfStates = newFinal + 1
        resultNFA.trans = newTrans

        return resultNFA

    def concatenate(self, nfa2: 'NFA') -> 'NFA':
        nfa1 = self
        # atribuirea asta arata asa ciudat pt ca am erori ciudate de la python
        # desi stiu ca final e int, python tot protesteaza ca e lista... DESI NU E
        newFinal = int(nfa1.final + nfa2.final)

        # punem starile nfa-ului 2 in continuarea nfa-ului 1
        # -1 pentru ca ultima stare din nfa1 trebuie sa se suprapuna
        # cu prima stare din nfa2
        nfa2.offsetStatesByN(nfa1.nrOfStates - 1)

        # unim cele 2 nfa-uri
        newTrans = nfa1.trans.copy()
        newTrans.update(nfa2.trans)

        resultNFA = NFA()
        resultNFA.final = newFinal
        resultNFA.nrOfStates = int(newFinal) + 1
        resultNFA.trans = newTrans

        return resultNFA

    def star(self) -> 'NFA':
        nfa = self
        # offsetam cu 1 pt ca adaugam un nou start
        nfa.offsetStatesByN(1)

        # adaugam starea de final
        newFinal = int(nfa.final + 1)

        # unim noile stari cu cele 4 epsilon tranzitii
        newTrans = nfa.trans.copy()
        newTrans[(0, 'eps')] = [1, int(newFinal)]
        newTrans[(nfa.final, 'eps')] = [1, int(newFinal)]

        resultNFA = NFA()
        resultNFA.final = newFinal
        resultNFA.trans = newTrans
        resultNFA.nrOfStates = int(newFinal) + 1

        return resultNFA

    def offsetStatesByN(self, n):
        newStates = {}
        
        for (state, symbol), next_states in self.trans.items():
            newStates[(state + n, symbol)] = list(map(lambda x: x + n, next_states))

        self.trans = newStates
        self.final = self.final + n

    # special pt tema3, stim ca avem o singura stare finala
    def printToFile(self, file):
        out = open(file, "w")
        print(self.nrOfStates, file = out)
        print(self.final, file = out)
        
        for ((state, symbol), nextState) in self.trans.items():
            print(state, symbol, file = out, end=' ')
            print(*nextState, sep=' ', file = out)

    def __str__(self):
        return ("NFA:\nnr states: " + str(self.nrOfStates) + "\nfinal states: "
                 + str(self.final) + "\ntranzitii: " + str(self.trans))

class DFA:
    def __init__(self):
        # numarul de stari
        self.nrOfStates = 0
        # lista de stari finale
        self.final = []
        # tranzitiile
        self.trans = {}
        # helper pentru redenumire
        self.newTrans = {}

    def __str__(self):
        return ("DFA:\nnr states: " + str(self.nrOfStates) + "\nfinal states: "
                 + str(self.final) + "\ntranzitii: " + str(self.trans))

    # adaugarea unei tranzitii
    def addTransition(self, state, symbol, nextState):
        self.trans[(state, symbol)] = nextState

    # redenumirea starilor si completarea informatiilor despre DFA
    def finalTouches(self, nfa):
        self.nrOfStates = len(statesRename)
        # daca starea x a DFA-ului contine o stare a NFA-ului care e finala,
        # atunci si starea x este finala in DFA.
        for (state, key) in statesRename.items():
            for substate in state:
                if substate == nfa.final:
                    self.final.append(key)

        # redenumire
        for ((state, symbol), value) in self.trans.items():
            self.newTrans[(statesRename[state], symbol)] = statesRename[value]

        self.trans = self.newTrans

    # scrierea in fisier
    def printDFA(self, file):
        out = open(file, "w")
        print(self.nrOfStates, file = out)
        print(*self.final, file = out, sep = " ")
        
        for ((state, symbol), nextState) in self.trans.items():
            print(state, symbol, nextState, file = out)

dfa = DFA()

# citirea din fisier
def readNFA(name):
    file = open(name, "r")
    l = list(map(lambda a: a.strip("\n").split(" "), file.readlines()))
    return l

# facem un NFA care recunoaste un singur simbol
#
#       sym
#    0 -----> (1) 
#    ^         ^
# initial    final
def createAtomNFA(symbol):
    l = [['2'], ['1'], ['0', symbol, '1']]
    return NFA(l)

def createNFA(l):
    return NFA(l)

# returneaza starile in care poti ajunge din starea "state" pe epsilon
def getEpsilonTrans(state, nfa):
    for (st, sym) in nfa.trans:
        if st == state and sym == "eps":
            return nfa.trans[(st, sym)]

    return []

# calculeaza inchiderea epsilon
def getEpsilonClosure(state, nfa):
    eps = {state}
    queue = []
    queue.extend(getEpsilonTrans(state, nfa))
    queue.append(state)
    eps.update(queue)

    while queue != []:
        currentState = queue.pop()
        queue += [x for x in getEpsilonTrans(currentState, nfa) if x not in eps]
        eps.update(queue)

    return eps

# calculeaza o stare a DFA-ului
def getDfaState(state, sym, nfa):
    newState = set()
    for st in state:
        if (st, sym) in nfa.trans:
            for nextState in nfa.trans[(st, sym)]:
                newState.update(epsilon[nextState])
            
    return tuple(newState)

# algoritmul principal de constructie
def constructDFA(nfa):
    global dfa
    global stateIndex
    global statesRename
    queue = []
    queue.append(epsilon[0])
    dfaStates = set()
    dfaStates.add(epsilon[0])
    statesRename[epsilon[0]] = stateIndex
    stateIndex += 1

    while queue != []:
        currentState = queue.pop()

        for sym in alphabet:
            newState = getDfaState(currentState, sym, nfa)
            dfa.addTransition(currentState, sym, newState)

            if newState not in dfaStates:
                dfaStates.add(newState)
                queue.append(newState)
                statesRename[newState] = stateIndex
                stateIndex += 1
    return dfa

def nfaToDfa(nfa) -> DFA:
    dfa = DFA()

    # calculam inchiderile epsilon
    for i in range(nfa.nrOfStates):
        epsilon.append(tuple(getEpsilonClosure(i, nfa)))

    # construim DFA-ul
    dfa = constructDFA(nfa)
    # formatarea output-ului
    dfa.finalTouches(nfa)

    return dfa

if __name__ == "__main__":
    # am lasat aici un caz simplu cu care am testat daca merge
    # constructia nfa-ului rezultat
    nfa1 = createAtomNFA('a')

    nfa2 = createAtomNFA('b')

    nfa = nfa1.concatenate(nfa2)

    # calculam inchiderile epsilon
    for i in range(nfa.nrOfStates):
        epsilon.append(tuple(getEpsilonClosure(i)))

    # construim DFA-ul
    dfa = constructDFA()
    # formatarea output-ului
    dfa.finalTouches()
    # scrierea in fisier
    dfa.printDFA(sys.argv[2])
