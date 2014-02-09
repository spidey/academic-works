% adivinhacao - a simple number guesser IA
% Copyright (C) 2009  Claudio Roberto França Pereira and classmates
%
% This program is free software: you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.
%
% You should have received a copy of the GNU General Public License
% along with this program.  If not, see <http://www.gnu.org/licenses/>.

elem(X, [X|_]) :- !.
elem(X, [_|L]) :- elem(X, L).

adivinha(X) :- write('Ola, '), write(X), writeln('.'), writeln('Pense em um numero entre 0 e 31.'), getOdd(A), getGreaterThanSixteen(B), getSecondBit(C), getFourthBit(B, D), getThirdBit(E), write('Voce pensou no numero '), R is A+B+C+D+E, writeln(R).

getOdd(1) :- writeln('O numero que voce pensou e impar? S/N'), get0(Odd), get0(_), elem(Odd, [83, 115]), !.
getOdd(0).

getGreaterThanSixteen(16) :- writeln('O numero que voce pensou e maior que 16? S/N'), get0(Greater), get0(_), elem(Greater, [83, 115]), !.
getGreaterThanSixteen(0).

getSecondBit(2) :- writeln('O numero que voce pensou esta nesta lista de numeros? S/N'), writeln('2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31'), get0(SecondBit), get0(_), elem(SecondBit, [83, 115]), !.
getSecondBit(0).

getThirdBit(4) :- writeln('O numero que voce pensou esta nesta lista de numeros? S/N'), writeln('4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31'), get0(ThirdBit), get0(_), elem(ThirdBit, [83, 115]), !.
getThirdBit(0).

getFourthBit(16, 0) :- writeln('O numero que voce pensou e menor que 24? S/N'), get0(FourthBit), get0(_), elem(FourthBit, [83, 115]), !.
getFourthBit(16, 8).
getFourthBit(0, 8) :- writeln('O numero que voce pensou e maior que 7? S/N'), get0(FourthBit), get0(_), elem(FourthBit, [83, 115]), !.
getFourthBit(0, 0).
