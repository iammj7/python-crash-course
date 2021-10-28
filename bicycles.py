# square brackets ([]) indicate a list, and individual elements in the list are 
#separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Access item in list
print(bicycles[0]) # this prints the first item in the list
# You can use string methods with lists
print(bicycles[0].title()) # prints first item as titlecase
# the list index start at 0, Not 1
print(bicycles[1])
print(bicycles[2])
# accessing the last item in the list
print(bicycles[-1]) # -1 will return the last item in the list

# using individual values from a list
message = f"My first bicycles was a {bicycles[0].title()}."
print(message)

