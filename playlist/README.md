# Playlist - a simple exercise on Object Oriented Programming
**Playlist** is a simple project that uses the Java language to implement a
simple hierarchy of classes: a generic *Media* class with only title and length
fields, and *Song* and *Video* subclasses, which adds more fields and may
override *Media*'s *getLength* method. To manipulate objects of those classes,
there is a final *Playlist* class which implements the entrypoint of the
program, creating a collection of medias and printing their total length.

## Files
Documentation for the project is on the *doc/* subfolder. The PDF file
describes the tasks that were implemented. Source code is in *src/*.

## Compilation
This project depends only on Java's standard JDK. To compile it, use *javac*.

    $ cd src/
    $ javac *.java

## Running
To run the compiled code, calling **Playlist**'s main function, use *java*.

    $ java Playlist
