# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():

    def __init__(self, name, current_room):
        self.current_room = current_room

    def move_to(self, direction):
        if direction == 'n':
            room_index = 0
        elif direction == 'e':
            room_index = 1
        elif direction == 's':
            room_index = 2
        elif direction == 'w':
            room_index = 3

        if self.current_room.exits[room_index] == None:
            print("\033[1;32;40m You cannot move in that direction.\n")
            return None
        else: 
            return self.current_room.exits[room_index]






