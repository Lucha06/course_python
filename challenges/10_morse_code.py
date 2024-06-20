from playsound3 import playsound
from time import sleep

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}
word = input('Enter a word: ').upper()


def letter(string):
    wor1 = " "
    for x in word:
        if x == " ":
            wor1 += (" ")
        else:
            for y in MORSE_CODE_DICT:
                if x == y:
                    wor1 += (MORSE_CODE_DICT[x])
    for z in wor1:
        if z == '.':
            playsound("short.wav")
            print(z, end="")
            sleep(0.5)
        elif z == " ":
            print(z, end="")
            sleep(3)
        else:
            playsound("long.wav")
            print(z, end="")
            sleep(0.5)


letter(word)


