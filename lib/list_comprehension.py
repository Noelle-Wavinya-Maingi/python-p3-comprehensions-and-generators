#!/usr/bin/env python3

def return_evens(num_list):
    evens = [number for number in num_list if number % 2 == 0]
    return evens


def make_exclamation(sentence_list):
    exclamation = [sentence + "!" for sentence in sentence_list]
    return exclamation


print(return_evens([1, 2, 3, 5, 7, 22]))
print(make_exclamation(["Hello"]))
