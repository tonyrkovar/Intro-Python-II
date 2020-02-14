from room import Room
from player import Player
from item import Item, Sword, Armor

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = Player('Synicale', room['outside'])
print(f"hello {player.name}\n\nYou find yourself in {player.current_room.name}\n\n{player.current_room.description}")


short_sword = Sword("Short Sword", "A short sword to fight your foes", 5)
iron_armor = Armor('Iron Armor', "A piece of armor to protect your shoulders", 10)


room['foyer'].add_loot(short_sword)
room['overlook'].add_loot(iron_armor)
commands = ['n','s','w','e', 'take sword', 'get sword', 'take armor', 'get armor', "drop armor", 'drop sword']

run = True
while run == True:
    cmd = input("What do you do? ")
    if len(cmd) == 1: 
        if cmd in commands[:4]:
            
            player.move(cmd)

            if len(player.current_room.items):
                print(f'\nYou spot {player.current_room.items[0].name} laying on the ground.')

        elif cmd == "q":

            print("Goodbye, coward.")
            run = False

        elif cmd == 'i':

            if len(player.inventory) > 0:
                player.get_inventory()

            elif len(player.inventory) == 0:
                print(f"Your inventory is empty")

    elif len(cmd) > 1:

        if cmd in commands[4:6]:
            if len(player.current_room.items) > 0:
                print(f'\nYou pickup the {player.current_room.items[0].name}, maybe there is a scabbard nearby')
                player.grab_item(player.current_room.items[0]) 
                player.current_room.items.remove(player.current_room.items[0]) 
            else:
                print(f"There is nothing here")

        elif cmd in commands[6:8]:

            if len(player.current_room.items) > 0:
                print(f'\nYou put the {player.current_room.items[0].name} on')
                player.grab_item(player.current_room.items[0]) 
                player.current_room.items.remove(player.current_room.items[0]) 

            else:
                print(f"There is nothing here")

        elif cmd in commands[8:]:

            if cmd == "drop armor":
                print(f"You remove the armor and slam it on the ground")
                player.drop_item("Iron Armor")

            if cmd == "drop sword":
                player.drop_item('Short Sword')
                print(f"You drive the sword into the ground and leave it behind.")

        elif cmd == "inventory":
            player.get_inventory()

    else:
        print(f'\nPlease say something I can understand {player.name}')
