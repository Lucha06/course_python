from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

l = int(input('¿Cuántas letras quieres que tenga tu contraseña: '))
n = int(input('¿Cuántos números quieres que tenga tu contraseña: '))
s = int(input('¿Cuántos simbolos quieres que tenga tu contraseña: '))

x = []
y = []
z = []

for _ in range(l):
    x1 = choice(letters)
    x = x.append

for _ in range(2):
    y = choice(numbers)

for _ in range(2):
    z = choice(symbols)

print(x)
print(l, n, s)
