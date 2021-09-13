#William Wang
#9-10-21
#Challenge program
from datetime import date
#defines a couple objects
d0 = date(2009, 9, 25)
class currentDate:
    def __init__(self):
        self.year = int(input("what is the year?\n>"))
        self.month = int(input('what is the month?\n>'))
        self.day = int(input('what is the day of the month?\n>'))
dateclass = currentDate()
d1 = date(dateclass.year, dateclass.month, dateclass.day)
#finds time from 9-25-2009 to inputted date
delta = d1-d0

#finds the final printing variables
distanceM = 16637000000 + (delta.days * 917784)
distanceK = distanceM * 1.609344
distanceAU = distanceM/92955887.6
roundTripTime = 2*((distanceK * 1000)/299792458)


print(f'At your date, Voyager 1 is {format(distanceM, ",f")} miles away, which is {format(distanceK, ",f")} in kilometers, and is also {format(distanceAU, ",f")} in astonomical units.\n The round-trip time for a signal sent to Voyager is {round(roundTripTime, 2)} seconds.')