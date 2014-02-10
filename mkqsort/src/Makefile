#Copyright © 2009 Claudio Roberto França Pereira
#Universidade Federal do Espírito Santo - Estrutura de Arquivos
#
#This file is part of mkqsort.
#
#mkqsort is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#mkqsort is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with mkqsort. If not, see <http://www.gnu.org/licenses/>.

PROJECT = mkqsort

CC = gcc
CFLAGS = -Wall
OBJECTS = common.o file.o lineVector.o insertionSort.o threeWayRadixQuickSort.o main.o
BUILD_PATH = ../build

all: mkqsort

mkqsort: ${OBJECTS}
	mkdir -p $(BUILD_PATH)
	${CC} ${CFLAGS} -o $(BUILD_PATH)/$@ $(addprefix $(BUILD_PATH)/, $+)
	@echo
	@echo Build complete! Binary generated at $(BUILD_PATH)/$(PROJECT).

%.o : %.c
	${CC} ${CFLAGS} -c $+ -o $(BUILD_PATH)/$@

clean:
	rm -f $(addprefix ${BUILD_PATH}/, ${OBJECTS} ${PROJECT})
	rmdir $(BUILD_PATH)
	@echo
	@echo Clean complete.
