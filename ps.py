import random

class sweeper:
    def __init__(self,length,width,num_mines):
        self.length = length
        self.width = width
        self.num_mines=num_mines
        self.num_checked = 0
        # Tracks the amount of mines adjacent to each square. If a square is a mine, it is -1.
        self.mines = [[0 for i in range(width)] for j in range(length)]
        # Tracks if a square has been checked, including adjacent squares that do not have nearby mines.
        self.checked = [[0 for i in range(width)] for j in range(length)]
    
    # Initalizes the class once the starting square is set.
    def generate_mines(self,init_l,init_w):
        bomb = 0
        while bomb < self.num_mines:
            i = random.randrange(self.length)
            j = random.randrange(self.width)
            if (not(i == init_l and j == init_w) and self.mines[i][j] == 0):
                self.mines[i][j] = -1
                bomb += 1
        for i in range(self.length):
            for j in range(self.width):
                if (self.mines[i][j] == 0):
                    self.mines[i][j] = self.count_mines(i,j)
        self.set_checked(init_l,init_w)

    # Counts the adjacent mines to a square. 
    def count_mines(self,l,w):
        count = 0
        for i in range(l-1,l+2):
            for j in range(w-1,w+2):
                if (i >= 0 and i < self.length and j >= 0 and j < self.width):
                    if (self.mines[i][j] == -1):
                        count += 1
        return count

    # Sets a square to checked. if self.mines is 0 then it will also set adjacent squares to checked recursively.   
    def set_checked(self,l,w):
        self.checked[l][w] = 1
        self.num_checked += 1
        if (self.mines[l][w] == 0):
            for i in range(l-1,l+2):
                for j in range(w-1,w+2):
                    if (i >= 0 and i < self.length and j >= 0 and j < self.width):
                        if (self.mines[i][j] != -1 and self.checked[i][j] == 0):
                            self.set_checked(i,j)
    def check_win(self):
        return self.num_checked == (self.length * self.width) - self.num_mines