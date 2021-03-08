# Regex-to-epsilonNFA-to-DFA
Homework for Formal Languages and Automata. We had to use the code from the previous homework ([eNFA to DFA](https://github.com/zabbidou/epsilon-NFA-to-DFA)) and add the Regex-eNFA part. I chose to use ANTLR4 for easier implementation

# Romanian readme

## RE $\rightarrow$ NFA

Am ales pentru implementarea mea să generez un parser prin ANTLR4, cu
design pattern-ul `visitor`, exact ca în exemplul de la curs.

### Gramatica
Gramatica pe care am folosit-o este:

```
regex : concat_regex | regex OR concat_regex;
concat_regex : star_regex | concat_regex star_regex;
star_regex : atom | atom STAR;

atom: variable | inner;
variable: VAR;
inner: OPEN regex CLOSED;
```

Pe scurt, am făcut o ierarhie a operațiilor, pentru a ne asigura că se respectă
ordinea lor:

() $\rightarrow$ star $\rightarrow$ concat $\rightarrow$ reunion

Pentru a face parantezele să fie primele, le-am trecut ca fiind `atom`. Acestea
se vor evalua primele deoarece sunt la *"baza"* arborelui de parcurgere.
Pe aceeași idee, am pornit de la general la particular în regulile gramaticii,
adică de la operații cu *"prioritate"* redusă la operații cu *"prioritate"*
ridicată.

### Visitor

Am folosit același design pattern prezentat la curs, visitor.

Pentru fiecare operație, există o funcție de visit. A fost foarte
ușoară implementarea fix pentru că mi-am definit o regulă pentru
fiecare operație.

### Construcția propriu zisă

Pentru construcția NFA-ului, m-am gândit să folosesc regulile de
constuctie ale lui Thompson.

Astfel, eu construiesc la fiecare pas un NFA nou.

Făcând o analogie cu cursul, în care am implementat evaluarea operațiilor
aritmetice: pentru evaluarea **atomului**, adică o singură literă (sau un număr, 
pentru operații aritmetice), avem cazul de bază: returnăm un NFA care
acceptă doar acea literă (în cazul de la curs, returnăm numărul sub formă de int).

De exemplu, am avea visitVariable care primește litera *'a'*. Ce returnăm va avea forma:

&nbsp;
![](cazul_de_baza.png)\
&nbsp;

Pentru **concatenare**, primim 2 NFA-uri (venite practic din recursivitate)
și le prelucrăm astfel:

&nbsp;
![](concat.png)\
&nbsp;

Pentru **reuniune**, adică simbolul `'|'`, avem regula:

&nbsp;
![](or.png)\
&nbsp;

Iar pentru **Kleene star** avem:

&nbsp;
![](star.png)\
&nbsp;

### Prelucrarea NFA-urilor

Pentru a îmi face viața mai ușoară, mi-am făcut câteva funcții
ajutătoare în modulul NFA (tema 2).

#### CreateAtomNFA

În tema 2, aveam crearea NFA-ului inițial cu citire din fișier. Ce citeam
din fișier era tokenizat și pus într-o listă. Pentru a nu modifica foarte
mult implementarea, funcția asta practic hardcodeaza o listă de input
pentru a reprezenta un NFA care recunoaște doar un simbol dat.

Lista de input arată așa:

`[[nr stari], lista_stari_finale, [stare, simbol, stare_urmatoare]]`

Astfel, pentru un simbol dat, va arăta așa:

`[['2'], ['1'], ['0', symbol, '1']]`

#### offsetStatesByN

Când prelucrăm două NFA-uri (sau unul, în cazul **Kleene star**), trebuie
ca NFA-ul rezultat să păstreze convenția numirii stărilor (numere
consecutive, începând de la 0.)

Cele 2 NFA-uri primite păstrează și ele convenția, deci, dacă le-am
prelucra așa, simplu, am avea stări cu același nume.

Astfel, mi-am făcut o funcție ajutătoare care practic redenumeste
toate stările unui NFA și le offseteaza cu N (le adaugă la numărul
lor N).

#### Funcții pentru operațiile între NFA-uri

Pentru fiecare operator, am definit o funcție a clasei care returnează
NFA-ul rezultat.

Pentru **Kleene star**, de exemplu, funcția prelucrează doar NFA-ul `self`. Îi offseteaza stările cu 1 (deoarece adăugăm o stare la început
și una la final) și leagă noile stări cu epsilon tranziții de stările
inițiale ale NFA-ului.

Pentru **reuniune**, offsetam primul NFA cu 1, pentru că adăugăm o
singură stare la început, iar al doilea NFA cu `nfa1.nrOfStates + 1`,
deoarece denumirea stărilor trebuie să continue de la ultima stare a
primului NFA. Noua stare de final va fi adăugată la final.

Pentru **concatenare**, nu mai offsetam primul NFA (în graficul de mai sus
se vede că starea nouă inițială coincide cu starea veche inițială a 
primului NFA). Al doilea NFA îl offsetam cu `nfa1.nrOfStates - 1`,
deoarece `nfa1.final` trebuie să coincidă cu `nfa2.start`.
Setăm starea nouă finală că fiind ultima stare a NFA-ului 2.

# NFA $\rightarrow$ DFA

Am atașat și README-ul pentru tema 2 (*NFAtoDFA.pdf*), care intră în mai multe detalii
despre transformarea NFA $\rightarrow$ DFA.

Pe scurt, algoritmul este:

```
Începem cu E(0). Îl adăugăm în coadă și în set.

Cât timp coada nu este vidă (mai avem stări de prelucrat):
    
    Scoatem o stare din coadă.
    
    Pentru fiecare simbol din alfabet:

        Căutăm toate stările în care poți ajunge din starea curentă
        cu simbolul curent și le punem într-un set, care simbolizează
        starea din DFA.

        Verificăm în set-ul cu stările deja găsite (dfaStates) dacă
        am mai găsit starea asta sau nu.

            Dacă nu am mai găsit-o, o punem în coadă pentru a o
            prelucra și în set pentru a ține-o minte.

```
