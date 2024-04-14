"""
It is commonly said that one human year is equivalent to 7 dog years.
However, this simple conversion fails to recognize that dogs reach adulthood in approximately two years.
As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years,
and then count each additional human year as 4 dog years.
Write a program that implements the conversion from human years to dog years described in the previous explanation.
Ensure that your program works correctly for conversions of less than two human years and for conversions of two or
more human years. Your program should display an appropriate error message if the user enters a negative number.
"""

e = int(input('What is your age?: '))
c = 0
f = 0
if e > 0:
    if (e >= 2):
        a = e - 2
        b = a * 7
        c = b + 21
        print(f'Your canine age is {c}')
    elif e == 1:
        d = e - 1
        g = d * 7
        f = g + 10.5
        print(f'Your canine age is {f}')
    else:
        print(f'Your canine age is {e}')
else:
    print(f'Your age is wrong')