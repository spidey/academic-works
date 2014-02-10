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

#include <stdio.h>
#include "common.h"

//Print _error information
void PrintError(error_t _error){
	switch(_error){
		case E_NULL_FILE_POINTER:
			fprintf(stderr, "Null file pointer. Nothing done.\n");
			break;
		case E_LINE_TOO_LONG:
			fprintf(stderr, "Line too long. Function halted.\n");
			break;
		case E_TOO_MANY_LINES:
			fprintf(stderr, "Too many lines in the file. Function halted.\n");
			break;
		case E_END_REACHED:
			fprintf(stderr, "End of file reached. Nothing done.\n");
			break;
		case E_INVALID_ARGUMENTS:
			fprintf(stderr, "Invalid arguments. Nothing done.\n");
			break;
		case E_NO_INPUT_FILE:
			fprintf(stderr, "No input file. Nothing done.\n");
			break;
		case E_FILE_NOT_FOUND:
			fprintf(stderr, "File not found. Nothing done.\n");
			break;
		case E_OK:
			fprintf(stderr, "All OK.\n");
			break;
		case E_NO_MEMORY:
			fprintf(stderr, "No memory to continue processing file.\n");
			break;
		default:
			fprintf(stderr, "Unkown error ocurred.\n");
			break;
	}
	return;
}
//Print _text to stderr
void Debug(const char *_text){
	fprintf(stderr, "%s\n", _text);
	return;
}

