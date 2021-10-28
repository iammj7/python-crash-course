cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()  # sorting A-Z
print(cars)

# You can reverse the sort
cars.sort(reverse=True)  # list will be in reverse order Z-A
print(cars)

# Sorting a list with temporarily with sorted() fucntion
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# printing a list in reverse order
print(">>> Printing the list in reverse order <<<<")
cars.reverse()  # applying reverse method to cars
print(cars)

# finding the length of a list
len(cars)  # this will return total items in the list as int
