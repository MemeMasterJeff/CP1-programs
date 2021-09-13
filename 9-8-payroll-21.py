#William Wang & Sophia Hayes
#9-8-21
#calculates payroll for each employee after a week

#defins the employee class
try:
    class employee:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay
            #inputted/calculated values
            self.rate = float(input(f'How many hours did {self.name} work?\n>'))
            self.gross = self.pay * self.rate
            self.social = 0.07 * self.gross
            self.tax = 0.15 * self.gross
            #calculates net pay
            self.net = self.gross - (self.tax + self.social)
    #defines objects
    employee1 = employee("Everett Dombrowski", float(8.35))
    employee2 = employee('Anagha Nittalia', float(15.50))
    employee3 = employee('Luke Olsen', float(13.25))
    employee4 = employee('Emily Lubek', float(13.50))
    #defines lists
    people = [employee1.name, employee2.name, employee3.name, employee4.name]
    payRate = [employee1.pay, employee2.pay, employee3.pay, employee4.pay]
    hours = [employee1.rate, employee2.rate, employee3.rate, employee4.rate]
    grossPay = [employee1.gross, employee2.gross, employee3.gross, employee4.gross]
    socialSecurity = [employee1.social, employee2.social, employee3.social, employee4.social]
    federalTax = [employee1.tax, employee2.tax, employee3.tax, employee4.tax]
    netPay = [employee1.net, employee2.net, employee3.net, employee4.net]

    #used a for loop that iterates through multiple lists to print 4 different sets of information
    for a, b, c, d, e, f, g in zip(people, payRate, hours, grossPay, socialSecurity, federalTax, netPay):
        print("{:<15}{:>15}".format("Name:", a))
        print("{:<12}{:>15}".format("Pay Rate:", b))
        print("{:<12}{:>15}".format("Hours worked", c))
        print("{:<12}{:>15}\n".format("Gross pay:", f'${d}'))
        print("{:<20}".format("Deductions"))
        print("{:<19}{:<18}".format("\t\tSocial Security:", f'${round(e, 2)}'))
        print("{:<19}{:<18}\n".format("\t\tFederal Tax:", f'${round(f,2)}'))
        print("{:<25}{:<18}".format("Net Pay:", f'${round(g,2)}'))
        print("{:<40}\n".format("----------------------------------"))
        print(f"Miller Co.\n440 W.Aurora Avenue\nNaperville, IL.60565\n\n")
        print('{:<40}{:>20}'.format(f"Pay to the Order of: {a}", f'${round(f,2)}\n'))
        print('{:>80}'.format("----------------------------------"))
        print('{:>80}\n\n'.format('Mr. Miller, the Boss'))
    input('press enter key to exit')
except:
    print('program errored out, please check your inputs.')