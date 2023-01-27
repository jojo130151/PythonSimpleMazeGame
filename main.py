# Jordan Davis
# Python Simple Maze Game
# 01/27/2023

# Import other files that hold functions and dictionaries
from textFunctions import gameIntro, instruction, losingMessage, winningMessage, status
from Dicts import rooms, items

current_room = 'Great Hall'  # Set start room

gameIntro()

inventory = []  # Create an empty inventory for the user to use

# Main gameplay loop
while current_room != 'exit':
    instruction()
    status(current_room, items, inventory, rooms)
    # Get user command and split into list
    user_command = input('Enter your move: ').lower()
    user_command = user_command.split()
    # Use if, else-if, and else statements to control movement based on command
    if 'go' in user_command:  # Move rooms or output invalid direction
        if user_command[1] in rooms[current_room]:
            current_room = rooms[current_room][user_command[1]]
            if current_room == 'Cellar':
                if len(inventory) == len(items):
                    winningMessage()
                else:
                    losingMessage(inventory, items)
                current_room = 'exit'
        elif user_command[1] not in rooms[current_room]:
            print('\nTry a different direction.')
    elif 'grab' in user_command:
        if current_room in items:
            inventory.append(items[current_room])
        else:
            print('\nThere is no item in this room.')
    elif 'exit' in user_command:  # Allows for the loop to exit when 'exit' is in command
        current_room = 'exit'
    else:  # Output for invalid commands
        print('\nPlease enter a valid command.')
# Print goodbye message
print('\nThank you for playing!')
