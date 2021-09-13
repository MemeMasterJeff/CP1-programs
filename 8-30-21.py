#William Wang
#8-30-21
#Jay deegan
#nobody
#Challenge program
#Compares cost of two colleges, taking into account the finacial aid you could receive

#asks users for college names
try:
    College1 = input("What is one of the colleges you want to attend?\n>")
    College2 = input("What is another college you want to attend?\n>")

    #asks about tuition
    tuition1 =float(input(f"how much is tuition at {College1}?\n>"))
    tuition2 = float(input(f"how much is tuition at {College2}?\n>"))
    #asks about room and board
    rb1 = float(input(f"what is the cost of room and board at {College1}?\n>"))
    rb2 = float(input(f"what is the cost of room and board at {College2}?\n>"))

   #finds the amount of financial aid received
    financialaid1 = input(f"are you receiving any financial aid/scholarships for {College1}? y/n\n>")
    if financialaid1 == 'n':
        financialaid1 = float(0)
    elif financialaid1 == 'y':
        financialaid1 = float(input("how much are you getting?\n>"))
    else:
        print("please put y or n")

    #find the amount of financial aid for college2
    financialaid2 = input(f'are you receiving any financial aid/scholarships for {College2}? y/n\n>')
    if financialaid2 == 'n':
        financialaid2 = float(0)
    elif financialaid2 == 'y':
        financialaid2 = float(input("how much are you getting?\n>"))
    else:
        print("please put y or n")

    #addition part
    total1 = tuition1 + rb1 - financialaid1
    total2 = tuition2 + rb2 - financialaid2

    print("{:^40}".format("_____Summary of college costs_____"))
    print("{:<10}{:>15}{:>15}".format("Institution", College1, College2))
    print("{:<10}{:>15.2f}${:>15.2f}$".format("Tuition",tuition1, tuition2))
    print("{:<10}{:>15.2f}${:>15.2f}$".format("housing",rb1, rb2))
    print("{:<10}{:>15.2f}${:>15.2f}$".format("Aids",financialaid1, financialaid2))
    print("{:<10}{:>15.2f}${:>15.2f}$".format("Total",total1, total2))

    #finding lower cost
    if total1 > total2:
        difference1 = str(total1 - total2)
        print(College2 + " costs $" + difference1 + " less than " + College1)
    elif total2 > total1:
        difference2 = str(total2 - total1)
        print(College1 + " costs $" + difference2 + " less than " + College2)
    else:
        print("both institutions cost the same to attend.")
except:
    print('Please make sure you entered the right kind of values, the code errored out.')
