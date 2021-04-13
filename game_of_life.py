import sys
import pygame
from Conway import Board

#other color =A6E3E9
class Gol:
    rows = 0
    cols = 0
    screen_height = 420
    screen_width = 600
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = Board(rows,cols)
        pygame.init()
        self.block_height = (self.screen_height - self.rows) / self.rows
        self.block_width = (self.screen_width - self.cols) / self.cols
        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE | pygame.DOUBLEBUF)

    def draw_screen(self):
        self.screen_surface.fill(pygame.Color('#E3FDFD'))

        for y in range(self.rows):
            for x in range(self.cols):
                if self.board.board[y][x]:
                    color = pygame.Color('#71C9CE')
                else:
                    color = pygame.Color('#A6E3E9')
                rect = pygame.Rect(x*(self.block_width+1), y*(self.block_height+1), self.block_width, self.block_height)
                pygame.draw.rect(self.screen_surface, color, rect)
        pygame.display.flip()
        self.board.next_cycle()
        print(self.board)
        pygame.time.delay(5000)

    def run(self):
        while True:
            for event in pygame.event.get():
                self.draw_screen()
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE| pygame.DOUBLEBUF)
                    self.block_height = (event.h - self.rows) / self.rows
                    self.block_width = (event.w - self.cols) / self.cols
                    


if __name__ == '__main__':
    obj = Gol(5,5)
    obj.run()
