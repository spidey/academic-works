/* Copyright © 2009 Claudio Roberto França Pereira
Universidade Federal do Espírito Santo - Estrutura de Arquivos

This file is part of mkqsort.

mkqsort is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

mkqsort is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with mkqsort. If not, see <http://www.gnu.org/licenses/>. */

#include "common.h"
#include "insertionSort.h"
#include "threeWayRadixQuickSort.h"

//Sort _stringVector's _size elements, using the _offset'th character of the strings as reference
void ThreeWayRadixQuickSort(char **_stringVector, ulong _size, uint _offset){
	char **a, **b, **c, **d;
	char pivot = *(*_stringVector+_offset); //First string is the pivot
	char *tmp, **sI1, **sI2; //tmp -> For inline swap | sI -> string Iterator, for inline vector swap
	long diff; //difference
	ulong lSS, rSS; //leftSideSize and rightSideSize

	if(_size <= 10){
		InsertionSort(_stringVector, _size, _offset);
		return;
	}

	a = b = _stringVector+1; //Start after the pivot
	c = d = _stringVector+_size-1;

	while(1){
		while(b <= c){ //Iterate from the left to the right
			diff = *(*b+_offset) - pivot;
			if(diff < 0){ //Pass over lesser chars
				b++;
			}else if(!diff){ //Send equal chars to the beginning
				//Inline StringSwap
				tmp = *a;
				*a = *b;
				*b = tmp;
				//End of inline swap
				a++;
				b++;
			}else{ //Stop on greater chars
				break;
			}
		}
		while(b <= c){ //Iterate from the right to the left
			diff = *(*c+_offset) - pivot;
			if(diff > 0){ //Pass over greater chars
				c--;
			}else if(!diff){ //Send equal chars to the end
				//Inline StringSwap
				tmp = *c;
				*c = *d;
				*d = tmp;
				//End of inline swap
				c--;
				d--;
			}else{ //Stop on lesser chars
				break;
			}
		}
		if(b>c){ //If b and c have crossed, stop iterating
			break;
		}else{ //If b and c haven't crossed yet, swap them
			//Inline StringSwap
			tmp = *b;
			*b = *c;
			*c = tmp;
			//End of inline swap
			b++;
			c--;
		}
	}

	//Swaps beginning-a with a-b
	lSS = a-_stringVector;
	rSS = b-a;
	if(lSS < rSS){
		diff = lSS;
	}else{
		diff = rSS;
	}
	//Inline StringVectorSwap
	sI1 = _stringVector;
	sI2 = b-diff;
	while(diff){
		tmp = *sI1;
		*sI1++ = *sI2;
		*sI2++ = tmp;
		diff--;
	}
	//End of inline StringVectorSwap

	//Swaps c-d with d-ending
	lSS = d-c;
	rSS = _stringVector+_size-d-1;
	if(lSS < rSS){
		diff = lSS;
	}else{
		diff = rSS;
	}
	//Inline StringVectorSwap
	sI1 = c+1;
	sI2 = _stringVector+_size-diff;
	while(diff){
		tmp = *sI1;
		*sI1++ = *sI2;
		*sI2++ = tmp;
		diff--;
	}
	//End of inline StringVectorSwap

	//Call ThreeWayRadixQuickSort recursevely
	if((lSS = b-a)){ //Left side, lesser chars
		ThreeWayRadixQuickSort(_stringVector, lSS, _offset);
	}
	if(pivot){ //Middle only if pivot is not the '\0' character
		ThreeWayRadixQuickSort(_stringVector+lSS, a+_size-d-1, _offset+1);
	}
	if((rSS = d-c)){ //Right side, greater chars
		ThreeWayRadixQuickSort(_stringVector+_size-rSS, rSS, _offset);
	}

	return;
}
