"""
Positions on a chess board are identified by a letter and a number.
The letter identifies the column, while the number identifies the row,as shown here:
https://cdn2.vectorstock.com/i/1000x1000/53/21/a-chessboard-white-and-bla-vector-22415321.jpg
Write a program that reads a position from the user.
So, for example if the user enters 'a1' then your program should report that the square is black.
if the user enters 'd5' then your program should report that the square is white
"""

r = input('What is your letter?: ').upper()
s = int(input('What is your number?: '))

if r == 'A' or r == 'C' or r == 'E' or r == 'G':
    if s == 8 or s == 6 or s == 4 or s == 2:
        print('The square is white')
    elif s == 1 or s == 3 or s == 5 or s == 7:
        print('The square is black')
    else:
        print('The data is incorrect')
elif r == 'B' or r == 'D' or r == 'F' or r == 'H':
    if s == 8 or s == 6 or s == 4 or s == 2:
        print('The square is black')
    elif s == 1 or s == 3 or s == 5 or s == 7:
        print('The square is white')
    else:
        print('The data is incorrect')
else:
    print('The data is incorrect')