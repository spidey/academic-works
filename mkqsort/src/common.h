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

#ifndef COMMON_HEADER
#define COMMON_HEADER

//file.c and lineVector.c errors
#define E_OK 0
#define E_NULL_FILE_POINTER 1
#define E_LINE_TOO_LONG 2
#define E_TOO_MANY_LINES 3
#define E_END_REACHED 4
//main.c errors
#define E_INVALID_ARGUMENTS 101
#define E_NO_INPUT_FILE 102
#define E_FILE_NOT_FOUND 103

typedef unsigned int error_t;
typedef unsigned int uint;
typedef unsigned long ulong;
typedef enum{FALSE = 0, TRUE = 1} bool;

//Print _error information
void PrintError(error_t _error);
//Print _text to stderr
void Debug(const char *_text);

#endif
