import random
from hangman_art import *
from hangman_words import *

print(logo)
print('Welcome to the hangman game actuarial science version')

palabra = random.choice(words)
print(palabra)


def letter(r):
    lista = []
    sim = 0
    for x in palabra:
        if x == ' ':
            lista.append(' ')
        else:
            sim += 1
            lista.append('_')
    return lista

    lis = ''
    for y in lista:
        if y == ' ':
            lis += ' '
        else:
            lis += '_'
    print(lis)
    return lis


def making_blanks(palabra):

letter(1)