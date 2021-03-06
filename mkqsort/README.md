mkqsort - MultiKey QuickSort
============================

**mkqsort** will sort all lines of the input file and print them ordered, using the **MultiKey QuickSort** algorythm, also known as **Three Way Radix QuickSort**. The program has the limitation of only one input file can be read at a time, so if you need to sort several files you'll have to run **mkqsort** on each of this files, or cat them together before using **mkqsort**.

COMPILATION
-----------
**mkqsort** uses the make program for automatic building of the program binary. The requirements for building it are:

- gcc
- standard C library
- make


Many \*nix OS's come bundled with these packages. If you don't have all packages installed, a quick and simple search in your OS repository or package management system will assist you in the process of downloading, unpacking and installing the requirements.

After the requirements are met, just change the current directory to */path/to/mkqsort/source/src* and execute *make*:

    $ cd /path/to/mkqsort/source/src
    $ make

You can also run `make clean` to delete temporary binary files. Just make sure you've copied *../bin/mkqsort* somewhere else, or it will be deleted.

INSTALLATION
------------

**mkqsort** doesn't need to be installed. It's a stand-alone binary file. If it's your wish, you can move the program to any of the directories listed in your `PATH` environment variable, like */usr/bin* or */usr/local/bin*, so you can run it just by typing `mkqsort` instead of `/path/to/binary/mkqsort`.

USAGE
-----

**mkqsort** is self explanatory, if you run it specifying invalid arguments, the program auto-diagnoses itself and prints the error message along with the usage syntax:

`$ mkqsort [-s] <input_file>`

The `-s` option stands for silent mode. Using silent mode makes the program print only the ordered lines in the file, supressing time and cpu cost info.

SUPPORT
-------
For suggestions, corrections, critics, doubts or help using **mkqsort**, send me an
e-mail at __spidey@gmail.com__. I'll be glad to answer you the best I can. Just make sure you start the e-mail's subject with **[mkqsort]** for fast identification.
