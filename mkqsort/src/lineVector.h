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

#ifndef LINE_VECTOR_HEADER
#define LINE_VECTOR_HEADER

#include <stdio.h>
#include "common.h"

typedef char **lineVectorLines_t;
typedef unsigned long lineVectorLineIndex_t;
typedef unsigned int lineVectorCharIndex_t;
typedef struct{
	lineVectorLineIndex_t Size;
	lineVectorLines_t Lines;
}lineVector;

//Read a _file and create a _lineVector with the file _lines
error_t CreateLineVector(FILE *_file, lineVector **_lineVector);
//Destroy a _lineVector
error_t DestroyLineVector(lineVector **_lineVector);
//Print a _lineVector to _file with _lineBreakBefore style
error_t PrintLineVector(lineVector *_lineVector, FILE *_file, bool _lineBreakBefore);

#endif
