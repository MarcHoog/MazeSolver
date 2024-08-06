from cell import Cell
from time import sleep
import random

class Maze:
    
    def __init__(self, 
                 window,
                 x,
                 y, 
                 num_rows, 
                 num_cols, 
                 cell_width, 
                 cell_height,
                 seed=None):
        
        self._window = window
        self._x = x
        self._y = y
        
        self._num_rows = num_rows
        self._num_cols = num_cols
        
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._cells = []
        
        if seed is not None:
            random.seed(seed)
        
        self._create_cells()


    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._window, self._cell_width, self._cell_height)
                row.append(cell)
                
            self._cells.append(row)


    def draw(self):        
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
                self._animate()


    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw(x=self._x + j * self._cell_width, 
                  y=self._y + i * self._cell_height)
        self._animate()
        
    def _animate(self):
        self._window.redraw()
        sleep(0.02)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)
    
    def _get_possible_directions(self, i, j):
        directions = []
        if i > 0 and not self._cells[i - 1][j].visited:
            directions.append((-1, 0))
        if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
            directions.append((1, 0))
        if j > 0 and not self._cells[i][j - 1].visited:
            directions.append((0, -1))
        if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
            directions.append((0, 1))
        return directions
        
    # Make this but then with a stack 
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        
        while True:
            possible_directions = self._get_possible_directions(i, j)
            if not possible_directions:
                return 
        
            direction = random.choice(possible_directions)
            next_i = i + direction[0]
            next_j = j + direction[1]
            
            
            if direction == (-1, 0):
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][j].has_bottom_wall = False
            elif direction == (1, 0):
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][j].has_top_wall = False
            elif direction == (0, -1):
                self._cells[i][j].has_left_wall = False
                self._cells[i][next_j].has_right_wall = False
            elif direction == (0, 1):
                self._cells[i][j].has_right_wall = False
                self._cells[i][next_i].has_left_wall = False

            self._break_walls_r(next_i, next_j)