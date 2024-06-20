# s = 'python'

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

"""
OBJETIVE: Write a program that repeatedly asks the user to enter a number. If the number is positive,
add it to a running total. If the number is negative, stop the loop and print the final total.
"""
import statistics

# suma = 0
# while True:
#     num = int(input('Enter a number: '))
#     if num < 0:
#         print(suma)
#         break
#     suma += num


"""
List Manipulation with user Input 
Objetive: Create a program that allows the user to build a list of even numbers.
If the user enters an add number, skip adding it to the list 
The user decides when to stop 
"""

# list1 = []
# while True:
#     let = bool(int(input('Do you want to continue?: 1 YES, 0 NO')))
#     if not let:
#         break
#     x = int(input('Enter a number: '))
#     if x % 2 == 0:
#         list1.append(x)
# print(list1)

"""
Password Checker
Objetive: Write a program that repeatedly asks the user to enter a password.
Stop asking when the correct password ('python123') is entered
"""

# while True:
#     password = 'python123'
#     num = input('Enter a password: ')
#     if num == password:
#         print('The password is correct')
#         break

"""
Factorial Calculation 
Objetive: Write a program to calculate the factorial of a given number.
"""

# n = int(input('Enter a number: '))
# fact = 1
# if n == 1 or n == 0:
#     print(f'The factorial is {fact}')
# else:
#     for m in range(1,n+1):
#         fact = fact * m
#     print(f'The factorial is {fact}')

"""
Funciones: encapsular la logica
PUEDO ACCEDER A UNA VARIABLE  ATRAVES DE LA FUNCION PERO NO MODIFICARLA
Funcion Paradigm Precedural Paradigm 
"""

# x = 0
# x += 1
# print(x)

# a = 0
#
#
# def increment_by_n(n):
#     a = 0
#     a += n
#     return a
#
#
# print(a, increment_by_n(5))
# print(a)

# a = 0


# def increment_by_n(n):
#     global a
#     a += n
#     return a
#
#
# print(a, increment_by_n(5))
# print(a)

"""
Argumento: Cuando usamos la función, valor puesto en el método (NOMBRE)
        Keyword
        Positional argument     
Parámetro: Cuando nosotros hacemos la función (VARIABLES)
"""

# MODULOOOOOOOOOOOOOOOOOS

"""
Modulo: contiene funciones, clases y variables 
Libreria es un conjunto de modulos 
    En phyton se instala la libreria de 'Python Standard Library' y veremos los móduos 'random' 'statistics' y 'math'
Paqueteria: organiza modulos relacionados  tambien contiene funciones, clases y variables 
"""

# names = ['jake', 'esteban', 'fred', 'Tim']  # Lista
#
# corrected_names = map(lambda name : name.title(), names) # iterator
#
# # print(list(corrected_names))
#
# for item in corrected_names:
#     print(item)

# for item in map(
#                  lambda x, y, z: 2*x**y-z,
#                  [1, 2, 3],
#                  [0.1, 0.2, 0.3],
#                  [1, 2]):
#     print(item)

# my_grades = [
#     ('algebra', 8.8),
#     ('calculo diferencia', 2.0),
#     ('calculo actuarial II', 9.4),
#     ('calculo integral', 8.2),
#     ('teoria de la probabilidad', 1.0)
# ]
#
# test1 = lambda grad: grad[1] >= 3
#
# # print(test1(my_grades[0])
#
# x = filter(test1, my_grades)
# print(list(x))

# def f(*args):
#     print(args)
#
# f(1,2,3,4,5,6)


# def my_func(*numbers):
#     return (numbers)
#
# a = my_func(1,2,3,4,5)
# print(a)

# def my_func(*numbers, **letters):
#     return numbers, letters
#
# b = my_func(1, 2, 3, 4, a=1, b=5)
# print(b)

# a = (1, 2, 3, 4)  # Packing
# print(a)
#
# b, c, d, e = a  # Unpacking
# print(b)

"""
ITERABLE: Debe contener el método '__iter__'
    PEP 3132
"""

# my_range = range(7)
# print(my_range)
# print(*my_range)
# my_list = [1, 2, 3, 4]
# print(*my_list)
#
# days = ['monday', 'tuesday', 'wendnesday', 'thursday', 'friday']  # Packing
#
# a, b, c, d, e = days
# print(a)
# # rest, school, free = days  # Error
# *rest, school, free = days
# print(rest)
# print(school)
# print(free)

"""
COMPREHENSION: completo conocimiento y entendimiento del significado de algo
"""

"""
DUNDER METHOD '_init_.py' solo lo puede usar python.
"""

"""
IMPORTAR LIBRERIAS 
import 'nombre de la libreria'
import 'nombre del módulo'
import 'nombre de la libreria' as 'nombre que yo quiero
from 'nombre de la libreria' import 'nombre del módulo' as 'nombre que yo quiero
Si hablamos d el alibreria de python debemos de colocar ''nombre del modulo'.'variable a la que quiero acceder' para poder hacer uso de ellas o bien 
importar el modulo 'from 'Nombre del módulo' import *'
"""

# import numpy
# e = numpy.e
# print(e)
# pi = numpy.pi
# print(pi)
#
# import numpy as np
# e = np.e
# print(e)
# pi = np.pi
# print(pi)

"""
CLASS es un boceto del objeto, crea al objeto cuando lo llamo
Si tengo CLASS en la documentación primero hago la instancia y despues accedo a traves del nombre de la instancia 
"""

# import statistics
#
# my_norm = statistics.NormalDist()
# print(my_norm)
#
# my_normal = statistics.NormalDist()
# my_normal2 = statistics.NormalDist(2,1)
# print(my_normal.mean)
# print(my_normal2.variance)


"""
DICCIONARIO: Tiene 'key : value' accedemos a traves de la llave 'Nombre del diccionario [Nombre de la llave]'
"""










