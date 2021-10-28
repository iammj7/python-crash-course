motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# changing  element in a list
motorcycles[0] = 'ducati'
print(motorcycles)

print(motorcycles) # now ducati replaced in position 0

# Adding Elements to a list
motorcycles.append('ducati') # append method add the item to the end of a list
print(motorcycles)

# inserting element in a list
motorcycles.insert(0, 'honda') # using insert metho we can add item with position number
print(motorcycles)

# removing elements from a list using del
del motorcycles[0] # this will completely delete the item from list

# removing an item using the pop() method
# using this method we can save the deleted item into a variable
# pop() method delete the last item in the list if u don't pass item index
popped_item = motorcycles.pop()

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# poping item with index number
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


# removing item by value with remove method
motorcycles.remove('ducati') #this will remove item ducati in the list

