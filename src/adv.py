   # item_choice = input('Choose [get] or [drop] followed by item name')
# print(item_choice)

# #try:
#     #direction= str(direction_choice)

#     #if direction_choice == 'n':
#         #player.current_room = player.current_room.n_to
#         #print(room.name, room.description, room.item, item_choice)
#         #if item_choice == f"get {item.name}":
#             #on_take(item.name)
#             #add item to player inventory
#         #if item_choice == f"drop {item.name}":
#             #on_drop(item.name)
#             #leave item in room invenory
#         # if item_choice != f"get {item.name}" or f"drop {item.name}":
#         #     print("Unknown Command",item_choice)

from room import Room
from player import Player
from item import Item

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


# Declare all the items
item = {
    'anthrax':  Item("Anthrax",
                     """A serious infectious disease. This will kill in 2 turns, but do be careful it is highly contagious"""),

    'bazooka':    Item("Bazooka", """Anti-tank rocket launcher to blow your enemies away."""),

    'gun': Item("Gun", """A short barrelled fire arm, that is great for wounding enemies"""),

    'sword':   Item("Sword", """A long metal blade, that can cause major injuries."""),

    'diamond': Item("Diamond", """A precious stone worth more than you make in a year, right at your finger tips"""),
}

# Link item to room

room['outside'].items_loc = [item['anthrax']]
room['foyer'].items_loc = [item['sword']]
room['overlook'].items_loc = [item['bazooka']]
room['narrow'].items_loc = [item['gun']]
room['treasure'].items_loc = [item['diamond']]


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

# item_choice = input('Choose [get] or [drop] followed by item name')
# print(item_choice)

def new_player():
    Player.name = "You"
    Player.current_room = room['outside']
    print(f'{Player.name} you are located {Player.current_room}')

new_player()


def player_options():
    direction_choice = input(f'Choose [n] North, [s] South, [e] East, [w] West, [q] Quit:')

    try:
        if direction_choice == 'n':
            if Player.current_room.n_to == '':
                print(f'Ran into wall please choose a different direction')
            else:
                Player.current_room = Player.current_room.n_to
                print(Player.current_room)
            player_options()
                    
        elif direction_choice == 's':
            if Player.current_room.s_to == '':
                print(f'Ran into wall please choose a different direction')
            else:
                Player.current_room = Player.current_room.s_to
                print(Player.current_room)
            player_options()

        elif direction_choice == 'e':
            if Player.current_room.e_to == '':
                print(f'Ran into wall please choose a different direction')
            else:
                Player.current_room = Player.current_room.e_to
                print(Player.current_room)
            player_options()

        elif direction_choice == 'w':
            if Player.current_room.w_to == '':
                print(f'Ran into wall please choose a different direction')
            else:
                Player.current_room = Player.current_room.w_to
                print(Player.current_room)
            player_options()

        elif direction_choice == 'q':
            print('Thanks for playing.')
            #add break point    
    except ValueError:
        print(f'Please enter a valid choice')

player_options()



