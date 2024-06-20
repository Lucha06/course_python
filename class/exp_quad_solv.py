"""
Write a lambda function that calculates the roots of a quadratic equation ax^2+bx+c=0.
Assume that the discriminant is always non-negative.
"""

quad = lambda a, b, c: ((-b + pow(pow(b, 2)-4*a*c, 1/2))/(2*a),(-b - pow(pow(b, 2)-4*a*c, 1/2))/(2*a))
print(quad(2,2,0))
print((lambda a, b, c: ((-b + pow(pow(b, 2)-4*a*c, 1/2))/(2*a),(-b - pow(pow(b, 2)-4*a*c, 1/2))/(2*a)))(2,2,0))
