import sys
import pygame
import numpy as np
from numpy import sqrt
from time import sleep

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (100, 100, 100)
BLUE  = (0, 191, 255)
GREEN = (34,139,34)
RED   = (220,20,60)

WINDOW_SIZE = [1000, 700]

class Node():
    """A node class for A* search"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 # PATH-COST to the node
        self.h = 0 # heuristic to the goal: straight-line distance hueristic
        self.f = 0 # evaluation function f(n) = g(n) + h(n)

    def __eq__(self, other):
        return self.position == other.position

class Maze():
    def __init__(self, board_size, grid_size, origin, player_initial_pos, goal):
        self.board_size = board_size
        self.grid_size  = grid_size
        self.origin = origin
        self.maze_data = np.zeros((board_size, board_size), dtype=int)
        self.current_pos = player_initial_pos
        self.goal = goal
        # Initiating board
        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(WHITE)
        # Draw start and goal
        idy, idx = self.current_pos
        rect = pygame.Rect(origin[0] + idx*grid_size, origin[1] + idy*grid_size, grid_size, grid_size)
        pygame.draw.rect(SCREEN, BLUE, rect)
        pygame.draw.rect(SCREEN, WHITE, rect, 2)
        self.DrawGoal()
        self.solve_btn_pos  = (800, 50)
        self.solve_btn_size = (100, 50)
        self.DrawButton(self.solve_btn_pos, self.solve_btn_size, "Solve")
        self.reset_btn_pos  = (800, 200)
        self.reset_btn_size = (100, 50)
        self.DrawButton(self.reset_btn_pos, self.reset_btn_size, "Reset")

    def DrawGrid(self):
        """Initiate maze with given parameters"""
        origin = self.origin
        board_size = self.board_size
        grid_size = self.grid_size
        for idy in range(board_size):
            for idx in range(board_size):
                rect = pygame.Rect(origin[0] + idx*grid_size, origin[1] + idy*grid_size, grid_size, grid_size)
                pygame.draw.rect(SCREEN, BLACK, rect, 1)

    def EventManager(self):
        """Button Manager"""
        for event in pygame.event.get():
            # Check for quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse click (obstacle setting)
            if event.type == pygame.MOUSEBUTTONDOWN:
                (pos_x, pos_y) = pygame.mouse.get_pos()
                legit_mouse_press = (  (pos_x > self.origin[0]) & (pos_x < self.origin[0] + self.board_size*self.grid_size)
                         & (pos_x > self.origin[1]) & (pos_x < self.origin[1] + self.board_size*self.grid_size) & (pos_x != self.goal[1])
                         & (pos_y != self.goal[0]))
                if (legit_mouse_press):
                    idx = (pos_x - self.origin[0]) // self.grid_size
                    idy = (pos_y - self.origin[1]) // self.grid_size
                    self.maze_data[idy][idx] = 1 - self.maze_data[idy][idx]
                    self.MazeUpdate(idx, idy)

                # Screen button checking
                else:
                    sol_x, sol_y = self.solve_btn_pos
                    sol_w, sol_h = self.solve_btn_size
                    res_x, res_y = self.reset_btn_pos
                    res_w, res_h = self.reset_btn_size
                    if (((pos_x > sol_x) & (pos_x < sol_x + sol_w)) & ((pos_y > sol_y) & (pos_y < sol_y + sol_h))):
                        self.CallSolver()
                    elif (((pos_x > res_x) & (pos_x < res_x + res_w)) & ((pos_y > res_y) & (pos_y < res_y + res_h))):
                        self.ResetMaze()
                
            # Check for player's control (WASD)
            if event.type == pygame.KEYDOWN:
                if event.unicode == "w":
                    if (self.current_pos[0] > 0):
                        temp_pos = [self.current_pos[0] - 1, self.current_pos[1]]
                        if (self.maze_data[temp_pos[0], temp_pos[1]] == 0):
                            previous_pos = self.current_pos
                            self.current_pos = [self.current_pos[0] - 1, self.current_pos[1]]
                            self.DrawPlayerPosition(previous_pos)
                if event.unicode == "s":
                    if (self.current_pos[0] < self.board_size - 1):
                        temp_pos = [self.current_pos[0] + 1, self.current_pos[1]]
                        if (self.maze_data[temp_pos[0], temp_pos[1]] == 0):
                            previous_pos = self.current_pos
                            self.current_pos = [self.current_pos[0] + 1, self.current_pos[1]]
                            self.DrawPlayerPosition(previous_pos)
                if event.unicode == "a":
                    if (self.current_pos[1] > 0):
                        temp_pos = [self.current_pos[0], self.current_pos[1] - 1]
                        if (self.maze_data[temp_pos[0], temp_pos[1]] == 0):
                            previous_pos = self.current_pos
                            self.current_pos = [self.current_pos[0], self.current_pos[1] - 1]
                            self.DrawPlayerPosition(previous_pos)
                if event.unicode == "d":
                    if (self.current_pos[1] < self.board_size - 1):
                        temp_pos = [self.current_pos[0], self.current_pos[1] + 1]
                        if (self.maze_data[temp_pos[0], temp_pos[1]] == 0):
                            previous_pos = self.current_pos
                            self.current_pos = [self.current_pos[0], self.current_pos[1] + 1]
                            self.DrawPlayerPosition(previous_pos)
        pygame.display.update()

    def MazeUpdate(self, idx, idy):
        """Redraw Maze to fit matrix data"""
        origin = self.origin
        grid_size = self.grid_size
        grid_state = self.maze_data[idy][idx]
        rect = pygame.Rect(origin[0] + idx*grid_size, origin[1] + idy*grid_size, grid_size, grid_size)
        if (grid_state == 0):
            pygame.draw.rect(SCREEN, WHITE, rect)
        else:
            pygame.draw.rect(SCREEN, BLACK, rect)
            pygame.draw.rect(SCREEN, WHITE, rect, 2)

    def DrawPlayerPosition(self, previous_pos):
        """Draw player's current position"""
        idy, idx = previous_pos
        origin = self.origin
        grid_size = self.grid_size
        rect = pygame.Rect(origin[0] + idx*grid_size, origin[1] + idy*grid_size, grid_size, grid_size)
        pygame.draw.rect(SCREEN, WHITE, rect)
        idy, idx = self.current_pos
        rect = pygame.Rect(origin[0] + idx*grid_size, origin[1] + idy*grid_size, grid_size, grid_size)
        pygame.draw.rect(SCREEN, BLUE, rect)
        pygame.draw.rect(SCREEN, WHITE, rect, 2)

    def DrawSolvedPath(self, path):
        """Just some meaningless placeholder"""
        if path is not None:
            for path_pos in path:
                idy, idx = path_pos[0], path_pos[1]
                rect = pygame.Rect(self.origin[0] + idx*self.grid_size, self.origin[1] + idy*self.grid_size, self.grid_size, self.grid_size)
                pygame.draw.rect(SCREEN, GREEN, rect)
                pygame.draw.rect(SCREEN, WHITE, rect, 2)
                pygame.time.delay(500)
                pygame.display.update()

    def DrawGoal(self):
        idy, idx = self.goal[0], self.goal[1]
        rect = pygame.Rect(self.origin[0] + idx*self.grid_size, self.origin[1] + idy*self.grid_size, self.grid_size, self.grid_size)
        pygame.draw.rect(SCREEN, RED, rect)
        pygame.draw.rect(SCREEN, WHITE, rect, 2)

    def DrawButton(self, pos, dim , text):
        """Just some meaningless placeholder"""
        rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])
        pygame.draw.rect(SCREEN, BLACK, rect, 2)
        smallfont = pygame.font.SysFont('Corbel', 22)
        text = smallfont.render(text , True , BLACK)
        size = text.get_size()
        SCREEN.blit(text, (pos[0] + dim[0]/2 - (size[0]/2), pos[1] + dim[1]/2 - (size[1]/2)))

    def CallSolver(self):
        start = (int(self.current_pos[0]), int(self.current_pos[1]))
        end = (int(self.goal[0]), int(self.goal[1]))
        path = your_search_function(self.maze_data.tolist(), start, end)
        print(path)
        self.DrawSolvedPath(path)

    def ResetMaze(self):
        # Reset whole maze
        self.maze_data = np.zeros((self.board_size, self.board_size), dtype=int)
        SCREEN.fill(WHITE)
        self.DrawGrid()
        initial_pos = (0,0)
        self.current_pos = initial_pos
        origin = self.origin
        grid_size = self.grid_size
        idy, idx = initial_pos
        rect = pygame.Rect(origin[0] + idx*grid_size, origin[1] + idy*grid_size, grid_size, grid_size)
        pygame.draw.rect(SCREEN, BLUE, rect)
        pygame.draw.rect(SCREEN, WHITE, rect, 2)
        self.DrawGoal()
        self.solve_btn_pos  = (800, 50)
        self.solve_btn_size = (100, 50)
        self.DrawButton(self.solve_btn_pos, self.solve_btn_size, "Solve")
        self.reset_btn_pos  = (800, 200)
        self.reset_btn_size = (100, 50)
        self.DrawButton(self.reset_btn_pos, self.reset_btn_size, "Reset")

    def UpdateMazeAll(self):
        # Update whole maze based on maze data 
        board_size = self.board_size
        origin     = self.origin
        grid_size  = self.grid_size
        for idy in range(board_size):
            for idx in range(board_size):
                rect = pygame.Rect(origin[0] + idx*grid_size, origin[1] + idy*grid_size, grid_size, grid_size)
                if self.maze_data[idy][idx] == 1:
                    pygame.draw.rect(SCREEN, BLACK, rect)
                    pygame.draw.rect(SCREEN, WHITE, rect, 2)
                else:
                    pygame.draw.rect(SCREEN, WHITE, rect)
        # Redraw player and goal position
        idy, idx = self.current_pos
        rect = pygame.Rect(origin[0] + idx*grid_size, origin[1] + idy*grid_size, grid_size, grid_size)
        pygame.draw.rect(SCREEN, BLUE, rect)
        pygame.draw.rect(SCREEN, WHITE, rect, 2)
        self.DrawGoal()

def your_search_function(maze, start, end):
    """Write your own path-searching function here"""

def main():
    maze = Maze(10, 50, [50, 50], [0,0], [8,9])
    maze.maze_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],  # 1: obstacle position
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]])
    maze.UpdateMazeAll()
    while True:
        maze.DrawGrid()
        maze.EventManager()

if __name__ == '__main__':
    main()
