# Write a program to find and print all prime numbers between 1 and 100

for s in range(1,101):
   div = 0
   for _ in range(1,101):
       if s % _ == 0:
           div += 1
   if div <= 2:
        print(s, end=' ')
   else:
        continue
