players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #printing players only index from 0 to 2 not including 3

print(players[1:4]) # prints from list 2 , 3 item

print(players[:4])# prints from list 0to 3 item not including 4th

print(players[2:]) # prints from list 2nd item to end of the list

print(players[-3:]) # prints last 3 items


# looping through a slice

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())


