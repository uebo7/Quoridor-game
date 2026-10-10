# storage for player position and walls remaining

class Player:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move_down(self):
        self.row += 1

    def move_up(self):
        self.row -= 1

    def move_left(self):
        self.col -= 1

    def move_right(self):
        self.col += 1

    
        
        
    