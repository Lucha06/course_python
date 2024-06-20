# Generate and print the multiplication table (up to 10) for a given number

m1 = int(input('Enter a number: '))
for s in range (1, 11):
    r = m1
    r = r * s
    print(f'{m1}*{s}={r}')

