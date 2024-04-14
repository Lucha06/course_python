"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
All three sides of an equilateral triangle have the same length.
An isosceles triangle has two sides that are the same length, and a third side that is a different length.
If all sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that
states the triangle’stype.
"""
print('Please insert the measurements of each side of the triangle separately as indicated')
m1 = input('What is the measure of the first side of the triangle??: ')
m2 = input('What is the measure of the second side of the triangle? ')
m3 = input('What is the measure of the third side of the triangle??: ')

if m1 == m2 and m2 == m3 :
    print("Your triangle is equilateral")
elif m1 == m2 or m1 == m3 or m2 == m3:
    print('Your triangle is isosceles')
else:
    print('Your triangle is scalene')
