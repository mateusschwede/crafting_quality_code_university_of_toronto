WALL = '#'
HALL = '.'
SPROUT = '@'
LEFT = -1
RIGHT = 1
NO_CHANGE = 0
UP = -1
DOWN = 1
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'

class Rat: #Rat caught in a maze
    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        self.row = row
        self.col = col

    def eat_sprout(self):
        self.num_sprouts_eaten += 1

    def __str__(self):
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol,self.row,self.col,self.num_sprouts_eaten)

class Maze: #2D maze
    def __init__(self, maze, rat_1, rat_2):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = self.number_sprouts_start()

    def number_sprouts_start(self):
        c = 0
        for row in self.maze:
            for val in row:
                if val == SPROUT:
                    c += 1
        return c

    def is_wall(self, row, column):
        return self.maze[row][column] == WALL

    def update_maze(self): #Update the rats position in the maze
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

    def get_character(self, row, column):
        self.update_maze()
        return self.maze[row][column]

    def move(self, rat ,vertical ,horizontal):
        if self.is_wall(rat.row + vertical, rat.col +horizontal) == False:
            self.maze[rat.row][rat.col] = HALL
            rat.set_location(rat.row + vertical, rat.col +horizontal)
            if self.maze[rat.row][rat.col] == SPROUT:
                rat.num_sprouts_eaten += 1
                self.maze[rat.row][rat.col] = HALL
                self.num_sprouts_left -= 1
            return False
        else:
            return True

    def __str__(self):
        self.update_maze()
        result = ''
        for line in self.maze:
            for value in line:
                result += value
            result += '\n'
        result += str(self.rat_1) + '\n'
        result += str(self.rat_2) + '\n'
        return result