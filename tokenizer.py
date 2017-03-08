#!/usr/bin/env python3
# Mario Jimenez
# Tokenizer - Algorithms Project

specialCharacters = ['<', '>', '<=', '>=', '=', '*', '+', '-', '^', '|', '~',
                     '=>', '<=>', '.', ',', '{', '}', '(', ')', '..', ']',
                     '[', '/', '\\']

stringCharacters = ['\\\\', '\\t', '\\r', '\\n', '\\\'']

whitespaceCharacters = [' ', '\\t', '\\r', '\\n']


def whiteChar(c):
    return (c in " \\r\n\t\v")


print(whiteChar("\\r"))x

# for x in stringCharacters:
#     print(x)


def tokenize(String: str):

    return str


# inputString = input("Enter String:\n")

# print(tokenize(inputString))
