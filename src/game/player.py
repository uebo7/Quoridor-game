# storage for player position
# walls remaining
# goal_state
# valid move

class Player:
    def __init__(self, row, col, color, goal_row):
        self.row = row
        self.col = col
        self.color = color

        self.walls = 10
        self.goal_row = goal_row

    def move_down(self):
        self.row += 1

    def move_up(self):
        self.row -= 1

    def move_left(self):
        self.col -= 1

    def move_right(self):
        self.col += 1

    def has_won(self):
        return self.row == self.goal_row

    def get_position(self):
        return (self.row, self.col)

    def use_wall(self):
        if self.walls > 0:
            --self.walls
            return True
        return False

    # def can_move(self):
        # check boundaries


    
        
        
    