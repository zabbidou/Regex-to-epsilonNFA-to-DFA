grammar Regex;

regex : concat_regex | regex OR concat_regex;
concat_regex : star_regex | concat_regex star_regex;
star_regex : atom | atom STAR;

atom: variable | inner;
variable: VAR;
inner: OPEN regex CLOSED;

STAR : '*' | DOUBLESTAR;
DOUBLESTAR : [*]+;
OR : '|';
OPEN : '(';
CLOSED : ')';

WHITESPACE : [ \t\r\n]+ -> skip;

VAR : [a-z];

