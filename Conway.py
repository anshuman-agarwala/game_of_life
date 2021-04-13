from random import randint
from itertools import product, starmap

class Board:
    length = 0
    breadth = 0
    board = []

    def __str__(self):
        return "\n".join([" ".join(map(str,row)) for row in self.board])

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.board = [[randint(0,1) for x in range(self.length)] for y in range(self.breadth)]

    def next_cycle(self):
        descriptive_board = starmap(self.get_neighbors, product(range(self.length),range(self.breadth)))
        board = list(starmap(self.set_state,descriptive_board))
        board = [board[self.length * x:(self.length * x) + self.length:] for x in range(self.breadth)]
        self.board = board

    def set_state(self, state, neighbors):
        if neighbors<2 and state:
            return 0
        if neighbors>3 and state:
            return 0
        if neighbors==3 and state==0 :
            return 1
        return state

    def get_neighbors(self,x, y):
        neighbors = 0
        if x>0 and self.board[x-1][y]:
            #TOP
            neighbors += 1
        if x>0 and y>0 and self.board[x-1][y-1]:
            #TOP-LEFT
            neighbors += 1
        if x>0 and y<self.breadth-1 and self.board[x-1][y+1]:
            #TOP-RIGHT
            neighbors += 1
        if y>0 and self.board[x][y-1]:
            #LEFT
            neighbors += 1
        if y<(self.breadth-1) and self.board[x][y+1]:
            #RIGHT
            neighbors += 1
        if y>0 and x<self.length-1 and self.board[x+1][y-1]:
            #BOTTOM-LEFT
            neighbors += 1
        if x<self.length-1 and self.board[x+1][y]:
            #BOTTOM
            neighbors += 1
        if x<self.length-1 and y<self.breadth-1 and self.board[x+1][y+1]:
            #BOTTOM-RIGHT
            neighbors += 1
        return self.board[x][y],neighbors

    def display_board(self):
        for row in self.board:
            for cell in row:
                print(cell,end=' ')
            print()
        print()

if __name__ == '__main__':
    board = Board(15,15)
    import os
    os.system('cls')
    print(board,'\n')
    board.next_cycle()
    os.system('cls')
    print(board,'\n')
    board.next_cycle()
    os.system('cls')
    print(board,'\n')
    board.next_cycle()
    os.system('cls')
    print(board,'\n')
    board.next_cycle()
    os.system('cls')
    print(board,'\n')
    board.next_cycle()
    board.next_cycle()
    #print(board)
