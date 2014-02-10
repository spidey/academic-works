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

#ifndef FILE_HEADER
#define FILE_HEADER

#include "common.h" //error_t
#include <stdio.h> //FILE

//Read the number of _lines in _file
error_t fCountLines(FILE *_file, ulong *_lines);
//Read the current line from _file into _line
error_t fGetLine(FILE *_file, char **_line);

#endif
