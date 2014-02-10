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
#include <stdio.h> //Input/Output
#include <limits.h> //Data types limits
#include "common.h" //Common constants and data types
#include "file.h" //Function prototypes and return values
#include "lineVector.h" //Function prototypes

//Read a _file and create a _lineVector with the file _lines
error_t CreateLineVector(FILE *_file, lineVector **_lineVector){
	lineVectorLineIndex_t size;
	lineVectorLineIndex_t currentLine = 0;
	error_t error = E_OK; //0
	char **lines;

	//Error handling
	if(!_file){
		return E_NULL_FILE_POINTER;
	}
	if(feof(_file)){
		return E_END_REACHED;
	}

	//Read the number of lines from _file into size and handle errors
	if((error = fCountLines(_file, &size))){
		return error;
	}

	//Initialize _lineVector
	*_lineVector = (lineVector*)malloc(sizeof(lineVector));
	(*_lineVector)->Size = size;
	(*_lineVector)->Lines = (char**)malloc(size*sizeof(char*));
	lines = (*_lineVector)->Lines; //Just to save some dereferencing

	//Fill _lineVector->Lines
	while(!error && currentLine < size && currentLine < ULONG_MAX){
		error = fGetLine(_file, &lines[currentLine++]);
	}

	//If everything goes OK, return E_OK, default value.
	return error;
}
//Destroy a _lineVector
error_t DestroyLineVector(lineVector **_lineVector){
	lineVectorLineIndex_t size = (*_lineVector)->Size;
	lineVectorLineIndex_t current = 0;
	char **lines = (*_lineVector)->Lines; //Saving some pointer operations

	//Clear all lines of _lineVector->Lines
	while(current < size){
		free(lines[current++]);
	}
	//Clear the line vector itself
	free(lines);
	//Clear _lineVector itself
	free(*_lineVector);
	*_lineVector = NULL;

	return E_OK;
}
//Print a _lineVector to _file with _lineBreakBefore style
error_t PrintLineVector(lineVector *_lineVector, FILE *_file, bool _lineBreakBefore){
	lineVectorLineIndex_t current;
	lineVectorLineIndex_t size = _lineVector->Size;
	char **lines = _lineVector->Lines;
	char *lineBreakBeforeFormat = "\n%s";
	char *lineBreakAfterFormat = "%s\n";
	char *printfFormat;

	if(_lineBreakBefore){
		printfFormat = lineBreakBeforeFormat;
	}else{
		printfFormat = lineBreakAfterFormat;
	}

	for(current = 0; current < size; current++){
		fprintf(_file, printfFormat, lines[current]);
	}

	return E_OK;
}
