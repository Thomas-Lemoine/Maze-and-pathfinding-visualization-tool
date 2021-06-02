import Greedy_pathfinding
import maze
import pygame

WIDTH = 1000
HEIGHT = 750

#COLS = 20
#ROWS = 15

COLS = 20
ROWS = 15
SHOW_VISUALIZATION = True
SPEED_FACTOR = 8 #n approximately speeds the visualization by n times (keep as an int)

#Note : If the visualization is off, we can make the size of the maze much greater.

if __name__ == "__main__":
    pygame, win, grid, start, end = maze.main(WIDTH, HEIGHT, ROWS, COLS, SHOW_VISUALIZATION, SPEED_FACTOR)
    Greedy_pathfinding.main(pygame, win, grid, start, end, SHOW_VISUALIZATION, SPEED_FACTOR)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()