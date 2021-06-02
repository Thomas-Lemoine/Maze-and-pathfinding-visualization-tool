from maze import TURQUOISE
import pygame
import math
from queue import PriorityQueue
import time
import random

def draw(win, grid):
    for row_lst in grid:
        for node in row_lst:
            node.draw(win)
    pygame.display.update()

def cost(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return int(10*((abs(x2 - x1)**2 + abs(y2 - y1)**2)**(1/2)))

def reconstruct_path(came_from, current, draw, show_visualization, speed_factor):
    count = 0
    current_ = current
    while current_ in came_from:
        count += 1
        current_ = came_from[current_]

    new_count = 0
    while current in came_from:
        new_count += 1
        current = came_from[current]

        ratio = new_count / count
        Bluecolor = (255 - (ratio*255)) if show_visualization else 0
        
        if ratio <= 0.5:
            current.make_color((255,255*2*ratio, Bluecolor))
        else:
            ratio -= 0.5
            current.make_color((255 - (2*255*ratio), 255, Bluecolor))
        if show_visualization and (new_count%speed_factor == 0):
            draw()
    draw()
    
def algorithm(draw, grid, start, starts, end, show_visualization, speed_factor):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, random.choice(starts)))
    came_from = {}
    viewed = []

    dist_score = {node: cost(end.get_pos(), node.get_pos()) for row in grid for node in row}

    open_set_hash = {start for start in starts}
    count = 0
    while not open_set.empty():
        count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[2]
        viewed.append(current)
        open_set_hash.remove(current)

        if current == end: #make path
            reconstruct_path(came_from,end, draw, show_visualization, speed_factor)
            draw()
            return True 
        
        neighbors_lst = [neighbor for neighbor in current.neighbors if not neighbor in viewed]
        for neighbor in neighbors_lst: 
            came_from[neighbor] = current
            if neighbor not in open_set_hash:
                count += 1
                open_set.put((dist_score[neighbor], count, neighbor))
                open_set_hash.add(neighbor)
                if show_visualization:
                    neighbor.make_open()
            if count % speed_factor == 0:
                if show_visualization:
                    draw()

        if show_visualization:
            current.make_closed()

    
    return False

def move_start(start, grid):
    new_starts = []
    for neighbor in start.outer_neighbors:
        if (neighbor.comes_from == start) or (start.comes_from == neighbor): #They are connected
            n_row, n_col = neighbor.row, neighbor.col
            s_row, s_col = start.row, start.col
            if n_row > s_row:
                new_starts.append(grid[start.row + 1][start.col])
            if n_row < s_row:
                new_starts.append(grid[start.row - 1][start.col])
            if n_col > s_col:
                new_starts.append(grid[start.row][start.col + 1])
            if n_col < s_col:
                new_starts.append(grid[start.row][start.col - 1])
            break
    return new_starts

def main(pygame, win, grid, start, end, bool_show_visualization, speed_factor):
    run = True
    starts = move_start(start, grid)
    while run:
        draw(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            run = not algorithm(lambda: draw(win, grid), grid, start, starts, end, bool_show_visualization, speed_factor)

    start.make_start()
    end.make_end()
        
    draw(win, grid)

