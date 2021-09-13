#William Wang
#9-10-21
#tipper program

bill = float(input('How much is your restaurant bill?\n>'))

percents = [15, 20]

for x in percents:
    total = ((x/100)+1) * bill
    print(f'total with {x}% tip = ${round(total, 2)}')