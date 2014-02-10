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

#include <stdlib.h> //Memory Allocation
#include <stdio.h> //File operations
#include <limits.h> //Integral types ranges
#include "common.h" //Common constants and data types
#include "file.h" //Function prototypes

//Read the number of _lines in _file
error_t fCountLines(FILE *_file, ulong *_lines){
	ulong lines = 0;
	int current; //Using int to support EOF
	char previous = '\n';

	//Error handling
	if(!_file){
		return E_NULL_FILE_POINTER;
	}

	rewind(_file); //Go to the beginning of the file
	//While not in the end of the file or the last read character
	//wasn't a LF, indicating a non-LF-terminating last line
	while((current = fgetc(_file)) != EOF){
		if(current == '\n'){
			if(lines == ULONG_MAX){
				*_lines = lines;
				rewind(_file); //Go to the beginning of the file
				return E_TOO_MANY_LINES;
			}
			lines++; //Increment the number of lines in the file
		}
		previous = (char)current; //Updates the previous character read
	}
	//Check for non-CR/LF terminating line
	if(previous != '\n'){
		lines++;
	}

	//Fill the output variables
	*_lines = lines;
	rewind(_file); //Go to the beginning of the file

	return E_OK;
}
//Read the current line from _file into _line
error_t fGetLine(FILE *_file, char **_line){
	const uint initialLength = 81; //For 80 columns console windows
	int current; //Current char, must be int to receive EOF
	uint length_left = (initialLength - 1); //Initial buffer size
	uint length = 0; //Line length
	char *buffer = (char*)malloc(sizeof(char)*initialLength);
	char *bufferIterator = buffer;
	error_t returnValue = E_OK;

	//Error handling
	if(!_file){
		return E_NULL_FILE_POINTER;
	}
	if(feof(_file)){
		return E_END_REACHED;
	}
	if(!buffer){
		return E_NO_MEMORY;
	}

	while(1){
		if(!length_left){
			//Realloc string to a bigger memory block
			char *newBuffer = (char*)realloc(buffer, length*2*sizeof(char) + 1);
			if (newBuffer != NULL){
				buffer = newBuffer;
				//Restore bufferIterator relative position
				bufferIterator = buffer + length;
				length_left = length;
			}else{
				returnValue = E_NO_MEMORY;
				*bufferIterator = 0;
				break;
			}
		}
		length++;
		current = fgetc(_file);
		if(current == '\n' || current == EOF){
			*bufferIterator = 0; //Terminate string
			break;
		}else{
			//Error handling
			if(length == UINT_MAX){
				returnValue = E_LINE_TOO_LONG;
				*bufferIterator = 0;
				break;
			}
			length_left--;
			*bufferIterator++ = (char)current;
		}
	}

	*_line = buffer;

	return returnValue;
}
