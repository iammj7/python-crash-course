#  GENERATE SQUARES AND STORE THEM IN LIST
squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)

print(squares)

#  GETTING MIN MAX SUM OF LIST OF NUMBERS
print(min(squares))
print(max(squares))
print(sum(squares))

# COMPREHENSION LIST
squares = [value**2 for value in range(1, 11)]
print(squares)
