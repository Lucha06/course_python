"""
Implement the Collatz Conjecture: Start with a number n, and repeatedly apply the rule n → n/2 if n is even
or n → 3n + 1 if n is odd. Print the sequence until n becomes 1.
"""

m1 = int(input('Enter a number: '))
if m1 == 1:
    print('Thiss the end')
else:
    while m1 != 1:
        if m1 % 2 == 0:
            m1 = m1/2
            print(m1)
        else:
            m1 = m1 * 3 + 1
            print()