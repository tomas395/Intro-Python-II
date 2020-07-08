class Player():

    def __init__(self, name, current_room):
        self.current_room = current_room

    def move_to(self, c_direction):
        if c_direction == 'n':
            room_index = 0
        elif c_direction == 'e':
            room_index = 1
        elif c_direction == 's':
            room_index = 2
        elif c_direction == 'w':
            room_index = 3

        if self.current_room.exits[room_index] == None:
            print("\033[1;31;40mYou cannot move in that direction!\n")
            return None
        else:
            return self.current_room.exits[room_index]
