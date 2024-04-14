# s = 'poython'

# print(s.capitalize())

# print(s)

# print(s.count('p'))

# print(s.endswith('w'))

# print(s.startswith('h', 3))

# print(s.index('o'))

# print(s.rindex('o'))

# print(s.upper())

# print(s.lower())

# my_tuple=(1,2,3)
# my_tuple1=1,2,3


# age = int(input('What is you name?'))
# if age < 18:
#    print('You are a kid')
# else:
#    print('You are adult')

# k = 0
# while k < 5:
#    print(f'The value of k is{k}')
#    k += 1

# x = 'spam'
# while x:
#    print(x, end=' ')
#    x = x[1:]

# x = 10
# while x:
#    x -= 1
#    if x % 2 == 0:
#        continue
#    print(x)

# while True:
#    name = input('Enter your name: ')
#    if name == 'stop':
#        break
#    age = input('Enter your age: ')
#    print('Hello', name, '=>', int(age) ** 2)

# print('out of while')

# OBJETIVE: Write a program that repeatedly asks the user to enter a number. If the number is positive,
# add it to a running total. If the number is negative, stop the loop and print the final total.
suma = 0
while True:
    num = int(input('Enter a number: '))
    if num < 0:
        print(suma)
        break
    suma += num


