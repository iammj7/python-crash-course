
#

motorcycle = ['honda', 'yamaha', 'suzuku']
print(motorcycle)

# MODIFYING or REPLACE ELEMENTS IN A LIST
motorcycle[0] = 'ducati'
print(motorcycle)

#  ADDING ELEMENTS TO A LIST
#  APPEND METHOD ADDS NEW ITEM TO THE END OF THE LIST
motorcycle.append('ducati')
print(motorcycle)

#  INSERTING ELEMENTS INTO A LIST USING INSERT
motorcycle.insert(0, 'ducati')
print(motorcycle)

#  REMOVING AN ELEMENTS FROM  LIST USING DEL
del motorcycle[0]  # using del function by list name and value of element.
print(motorcycle)

#  REMOVING AN ITEM USING POP()
#  AND ASSIGN THAT ITEM TO NEW VAR
#  THIS WILL REMOVE LAST ITEM IN THE LIST
popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)

#  POPPING FROM ANY POSITION
first_owned = motorcycle.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#  REMOVE AN ITEM BY VALUE
motorcycle.remove('yamaha')
print(motorcycle)
