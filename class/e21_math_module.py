# Import the math module (as you want)
import math
from math import *
e = fsum([1, 2, 2, 3])
print(e)

# Make the Poisson distribution. The user must enter the parameters. Then print out the result
n = 9
lam = 2
o = factorial(n)
e1 = exp(lam)
print(e1)
r = (e1 ** (-lam)) / o
print(r)

# Make an iterable with some numbers to calculate the product of all those numbers
a = [1, 2, 3, 4]
print(math.prod(a))

# From two iterables, calculate the sum of the product of values
b = [1, 2, 3, 4]
c = [5, 6, 7, 8]
print(sumprod(b, c))

# Calculate the GCD of two numbers that user gives
print(gcd(3, 4, 5))


# Make the binomial distribution. The user must enter the values: n, x, p. Then print out the result
n = int(input('Enter a value of n: '))
x = int(input('Enter a value of n: '))
p = float(input('Enter a value of n: '))
d = comb(n, x)
p1 = p ** x
p2 = (1-p) ** (n-x)
result = d * p1 * p2
print(result)

# The user enter a float number, and then the ceiling of that number must appear in the screen, as
# "the ceiling of x is y "
f = float(input('Enter a number: '))
print(ceil(f))


# Choose two functions from the math documentation to make exercises like the previous
print(gamma(pi))
print(ulp(.555))
