"""
In this exercise, you will create a program that reads a letter of the alphabet from the user.
If the user enters a,e,i,o or u then your program should display a message indicating that the entered letter is a vowel
If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y
is a consonant. Otherwise, your program should display a message indicating that the letter is a consonant.
"""
m = input('Enter a letter: ').upper()

if m == 'A' or m == 'E' or m == 'I' or m == 'O' or m == 'U':
    print('Letter is a vowel')
elif m == 'Y':
    print('Sometimes y is a vowel, and sometimes y is a consonant')
else:
    print('Letter is a consonant')
    