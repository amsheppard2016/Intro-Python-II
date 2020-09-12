# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__ (self, name, description, n_to = '', s_to = '', e_to = '', w_to = '', room_items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.room_items = room_items

    def print_room(self):
        length = len(self.room_items)
        i = 0

        while i < length:
            print(self.room_items[i])
            i += 1

    def __str__(self):
            return f'{self.name}, {self.description}'
    