#!/usr/bin/env python3

def return_evens(num_list):
    even_int=[n for n in num_list if n % 2==0]
    return even_int


def make_exclamation(sentence_list):
    exclamated=[st + "!" for st in sentence_list ]
    return exclamated

result= return_evens([0,1,3,5,7,8,9,10])
print(result)

string_list =  make_exclamation(["Hello", "World"])
print(string_list )