from random import choice, random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


n = input('Elige una opción entre rock(r) paper(p) o scissors(s) ')
print('Tu elección es: ')
if n == 'p':
    print('''
    Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
)
elif n == 'r':
    print('''
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

else:
    print('''
    Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


a = ['s', 'r', 'p']
x = choice(a)

print('Mi elección es: ')
if x == 'p':
    print('''
    Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
)
elif x == 'r':
    print('''
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

else:
    print('''
    Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if n == x:
    print('Empataste')
elif n == 'p' and x == 'r':
    print('Ganaste')
elif n == 'p' and x == 's':
    print('Perdiste')
elif n == 's' and x == 'p':
    print('Ganaste')
elif n == 's' and x == 'r':
    print('Perdiste')
elif n == 'r' and x == 'p':
    print('Perdiste')
elif n == 'r' and x == 's':
    print('Ganaste')
