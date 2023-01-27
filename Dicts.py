# Jordan Davis
# Python Simple Maze Game
# 01/27/2023

# The dictionary links a room to other rooms
rooms = {
    'Great Hall': {'south': 'Hallway', 'west': 'Dining Room', 'east': 'Library', 'north': 'Ballroom'},
    'Hallway': {'north': 'Great Hall', 'east': 'Cellar', 'west': 'Guest Bedroom',
                'south': 'Guest Bathroom', 'item': 'Tape'},
    'Cellar': {'west': 'Hallway'},
    'Dining Room': {'east': 'Great Hall', 'north': 'Kitchen', 'item': 'Serrated Knife'},
    'Kitchen': {'south': 'Dining Room', 'east': 'Ballroom', 'item': 'Slabs of Meat'},
    'Guest Bedroom': {'east': 'Hallway'},
    'Guest Bathroom': {'north': 'Hallway', 'item': 'Sleep Aids'},
    'Library': {'west': 'Great Hall', 'north': 'Private Study', 'item': 'Book on Wolves'},
    'Private Study': {'south': 'Library', 'item': 'Glass of Whiskey'},
    'Ballroom': {'south': 'Great Hall', 'west': 'Kitchen', 'north': 'Sitting Room'},
    'Sitting Room': {'south': 'Ballroom', 'east': 'Master Bedroom', 'item': 'Curtains'},
    'Master Bedroom': {'east': 'Sitting Room', 'south': 'Private Study', 'north': 'Master Bathroom', 'item': 'Sword'},
    'Master Bathroom': {'south': 'Master Bedroom'}
}

# Dictionary of all items in the game and where they are located
items = {
    'Dining Room': 'Serrated Knife',
    'Library': 'Book on Wolves',
    'Kitchen': 'Slabs of Meat',
    'Guest Bathroom': 'Sleep Aids',
    'Master Bedroom': 'Sword',
    'Sitting Room': 'Curtains',
    'Private Study': 'Glass of Whiskey',
    'Hallway': 'Tape'
}