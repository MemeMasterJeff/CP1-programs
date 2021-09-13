mice = 4
bones = 5
cats = 6
dogs = 7
nabber = 0

dogs = dogs * dogs
cats = (dogs + dogs) - (cats + cats)
petFood = (bones * dogs) + mice * cats

dogNabber = cats - dogs
catNabber = cats - mice

dogs = dogs % 10
cats = cats - nabber

animals = float('1' + '2')
food = mice + nabber
everything = str(animals) * food

print(dogs)
print(cats)
print(petFood)
print(dogNabber)
print(catNabber)
print(animals)
print(food)
print(everything)