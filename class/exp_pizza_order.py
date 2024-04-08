"""
Your job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""

bill = 0

size = input('What is the size?: Small (S), Medium (M), Large (L): ')
pepperoni = bool(int(input('Do you want to add pepperoni?: (1) Yes, (0) No: ')))
cheese = bool(int(input('Do you want to add cheese?: (1) Yes, (0) No: ')))

if size == 'S':
    bill = bill + 15  # O bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if size == 'S' and pepperoni == '1':
    bill += 2
elif pepperoni:
    bill += 3

if cheese:
    bill +=1


print(bill)