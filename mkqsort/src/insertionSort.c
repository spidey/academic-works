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

//Sort _stringVector. For each string, ignore first _offset characters.
void InsertionSort(char **_stringVector, ulong _size, uint _offset){
	char **fLSI; //firstLevelStringIterator
	char **sLSI; //secondLevelStringIterator
	char *lSCI; //leftStringCharIterator
	char *rSCI; //rightStringCharIterator
	char *tmp; //For swapping

	//Loop from second element to last. fLSI is the string to be inserted
	for(fLSI = _stringVector+1; --_size > 0; fLSI++){
		//Loop from the fLSI to the second element, ordering the vector
		for(sLSI = fLSI; sLSI > _stringVector; sLSI--){
			//Loop 'till *lSCI != *rSCI
			for(lSCI=*(sLSI-1)+_offset, rSCI=*sLSI+_offset; *lSCI==*rSCI && *lSCI!=0; lSCI++, rSCI++);
			//If lSCI <= rSCI, string is in place, sLSI current iteration done!
			if(*lSCI <= *rSCI){
				break;
			}
			//Swap values only if lSCI > rSCI and continue iterating sLSI
			tmp = *(sLSI-1);
			*(sLSI-1) = *sLSI;
			*sLSI = tmp;
		}
	}
	return;
}
