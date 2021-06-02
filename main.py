import Greedy_pathfinding
import maze
import pygame

WIDTH = 1000
HEIGHT = 750

COLS = 20
ROWS = 15

SHOW_VISUALIZATION = True
SPEED_FACTOR = 10 #n approximately speeds the visualization by n times (keep as an int)

#Note : The visualization slows the speed of the program. If columns and rows are greater than ~30, increase the speed factor.

"""
INSTRUCTIONS:
Start the program, and press the two nodes that will stand as the start of the maze and its end.
Press SPACE and the maze will be created. Once it's created, you can start over by pressing c.
Once the maze has been created and you are satisfied, press SPACE again and the pathfinding algorithm will begin.
Note : This algorithm, "Greedy Best-first search", will not always find the shortest route.
"""

if __name__ == "__main__":
    pygame, win, grid, start, end = maze.main(WIDTH, HEIGHT, ROWS, COLS, SHOW_VISUALIZATION, SPEED_FACTOR)
    Greedy_pathfinding.main(pygame, win, grid, start, end, SHOW_VISUALIZATION, SPEED_FACTOR)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()