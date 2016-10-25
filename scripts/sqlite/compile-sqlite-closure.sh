#!/bin/bash


# get sqlite amalgamation from git if not present
if [[ ! -d ./amalgamation ]]
then
    git clone \
        https://github.com/azadkuh/sqlite-amalgamation.git \
        ./amalgamation
fi

# get sqlite closure extension from git if not present
if [[ ! -d ./closure ]]
then
    git clone \
        https://gist.github.com/coleifer/7f3593c5c2a645913b92 \
        ./closure
fi

# compile sqlite closure extension shared objet
gcc -g -fPIC \
    -I./amalgamation \
    -shared ./closure/closure.c \
    -o ./closure.so
