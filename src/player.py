# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name="player1", current_room="outside", items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f'{self.name} is in the {self.current_room} with {self.items}'

#     def print_location:
#         print(f'You are in {self.current_room}')
    
#     def print_inventory:
#         print(f'You have {self.items} in your inventory')

#     def add_item:
        # pass
#     def drop_item:
        # pass