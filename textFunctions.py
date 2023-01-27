# Jordan Davis
# Python Simple Maze Game
# 01/27/2023

# Import required libraries
import time
import sys


# Creates a typing effect for printing text to user
def typeOutPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def gameIntro():
    typeOutPrint('Welcome! This is a simple game where you can traverse between rooms and grab items. '
                 '\nYou have woken up in a strange mansion and you can hear howling wolves really close by. '
                 '\nYou run for the for the exits but no matter how hard you try, you can\'t escape the mansion. '
                 '\nYou can hear the door holding the wolves back start to break and you know that you need to '
                 '\nprepare for the fight of your life. '
                 'The goal of the game is to move about the rooms collecting items \nwithout running into '
                 'the wolves scratching at the door of the cellar before you collect them all.\n')


def instruction():  # Welcome message and instructions
    print()
    print('Move commands are: \'go South\', \'go North\', \'go West\', \'go East\'')
    print('If the room has an item, you can grab the item and add it to the inventory by typing \'grab item\'')
    print('You can exit the game anytime by typing \'exit\'')


def status(current_room, items, inventory, rooms):  # Output separator and room status
    print()
    print('--------------------')
    print('You are in the', current_room)
    if current_room in items and items[current_room] not in inventory:
        print('In this room you see {}'.format(rooms[current_room]['item']))
    print('Inventory:', inventory)


def winningMessage():
    print()
    typeOutPrint('You cautiously approach the door leading to the cellar. '
                 'You can hear the rustling of fur and the \'clink\''
                 ' sound\n of claws hitting hardwood floors. First, you take a minute to '
                 'flip through the book you found, '
                 '\nfinding anything you can about the weaknesses of wolves. Next, you take a big gulp of whiskey '
                 '\nto get some liquid courage because this fight is going to be rough. You stuff the sleep aids into '
                 '\nthe slabs of meat to use both a distraction and '
                 'to *hopefully* knock a few wolves out. For protection,'
                 '\nYou tape portions of the curtains you found around your arms and legs for cushion. '
                 '\nWith your sword and knife in hand, you are as ready as you\'ll ever be. You descend the stairs...'
                 )
    typeOutPrint('CLASH -- ')
    typeOutPrint('GROWL -- ')
    typeOutPrint('WHINE -- ')
    typeOutPrint('AHHHHHHHHHHHH! -- ')
    typeOutPrint('SQUELCH\n')
    typeOutPrint('You lay on the ground, breaths heavy and hard, blood seeping out from wounds on your right arm '
                 '\nand across your ribs. There are the bodies of three wolves lying around you, '
                 '\nnot a one with a heartbeat. You are victorious. Now, if only you can figure out'
                 ' how to get out of this \nforsaken house...')
    print()


def losingMessage(inventory, items):
    print()
    typeOutPrint('Well, you only found {}'.format((len(inventory))) + ' of {}'.format(len(items)) + ' items. '
                 'Without all of the items, you went into this '
                 '\narduous battle ill-prepared. The wolves tore your body into shreds and ate your corpse.')
    print()
