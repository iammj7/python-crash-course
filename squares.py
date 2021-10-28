squares = [] # this is an empty list
for value in range(1, 11):
    square = value ** 2 # for each value * 4 or ** 2
    squares.append(square) # finally appending 
    # u can also use squares.append(value **2) instead creating new square var

print(squares)

# simple statistics with a list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# get the min least number from a list
min(digits)

# get max number from a list
max(digits)

# List comprehensions

squares = [value**2 for value in range(1,11)]
print(squares)
