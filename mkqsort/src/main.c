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

#include <stdio.h> //Input/Output
#include <string.h> //Options parsing
#include <time.h> //Time sorting process
#include "common.h" //Common constant and type definitions
#include "lineVector.h" //lineVector definition file
#include "threeWayRadixQuickSort.h" //Sorting algorythm

int main(int argc, char **argv){
	FILE *file;
	error_t error = E_OK; //0
	lineVector *LineVector;
	lineVectorLineIndex_t size;
	char **lines;
	bool verbose = TRUE;
	clock_t time;

	if(argc == 3){
		if(!strcmp(argv[1], "-s")){
			verbose = FALSE;
		}else{
			error = E_INVALID_ARGUMENTS;
		}
	}else if((argc == 2 && !strcmp(argv[1], "-s")) || argc == 1){
		error = E_NO_INPUT_FILE;
	}else if(argc > 3){
		error = E_INVALID_ARGUMENTS;
	}

	if(error){
		PrintError(error);
		fprintf(stderr, "Usage: %s [-s] input_file\n", argv[0]);
		return error;
	}

	file = fopen(argv[argc-1], "r");
	if(!file){
		PrintError(E_NO_INPUT_FILE);
		fprintf(stderr, "Usage: %s [-s] input_file\n", argv[0]);
		return error;
	}

	//Error handling
	if((error = CreateLineVector(file, &LineVector))){
		PrintError(error);
		return error;
	}

	//Preparing variables for sorting
	size = LineVector->Size;
	lines = LineVector->Lines;

	//Initialize timer
	time = clock();
	//Sort lineVector
	ThreeWayRadixQuickSort(lines, size, 0);
	//Update timer
	time = clock() - time;

	if(verbose){
		printf("Total clicks\t%d\n", (int)time);
		printf("Total secs\t%4.3lf\n\n\n", (double)time/CLOCKS_PER_SEC);
		printf("Resultado da ordenacao");
		PrintLineVector(LineVector, stdout, TRUE); //Print using NL-before style
	}else{
		PrintLineVector(LineVector, stdout, FALSE); //Print using NL-after style
	}

	//Destroy LineVector
	DestroyLineVector(&LineVector);

	return E_OK;
}
