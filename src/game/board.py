# Manage playing grid and wall position

class Board:
    def __init__(self, size=10):
        self.size = size 
        self.horizontal_walls = set()
        self.vertical_walls = set()

    def in_bounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size
    
