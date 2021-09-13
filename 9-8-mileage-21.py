#William Wang
#9-10-21
#finds the cost for filling the tank of a new car and it's range on one tank of gas

class carClass:
    def __init__(self):
        self.type = input("What car did you get?\n>")
        self.capacity = float(input(f"How many gallons can the {self.type} hold in its tank?\n>"))
        self.mpg = float(input(f'How many miles per gallon does the {self.type} get?\n>'))
        self.ppg = float(input(f'How much do you expect to pay per gallon of gas?\n>'))
        self.range = self.mpg * self.capacity
        self.cost = self.capacity * self.ppg
#defines object 'car' with as the class 'carClass'
car = carClass()

print(f'A brand new {car.type} can travel {round(car.range,2)} on one tank of gas.\n')
print(f'It will cost ${round(car.cost,2)} to fill the rank')