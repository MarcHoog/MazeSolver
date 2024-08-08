from cell import Cell
import random
from time import sleep
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
        self._break_entrance_and_exit()
        self._break_walls_dfs(0, 0)
        self._reset_visited_cells()

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._window, self._cell_width, self._cell_height)
                row.append(cell)
                
            self._cells.append(row)

    def _reset_visited_cells(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

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
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)
    
    def _break_walls_dfs(self, start_i, start_j):
        stack = [(start_i, start_j)]
        self._cells[start_i][start_j].visited = True

        while stack:
            i, j = stack[-1]  # Look at the top of the stack
            
            possible_directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((-1, 0))
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((1, 0))
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((0, -1))
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append((0, 1))

            if possible_directions:
                # Choose a random direction from the possible ones
                direction = random.choice(possible_directions)
                next_i = i + direction[0]
                next_j = j + direction[1]

                # Break the wall between the current cell and the chosen next cell
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
                    self._cells[i][next_j].has_left_wall = False

                # Mark the next cell as visited and push it onto the stack
                self._cells[next_i][next_j].visited = True
                stack.append((next_i, next_j))

            else:
                # If no directions are possible, backtrack by popping from the stack
                stack.pop()
                   
    def solve(self):     
        # End cell we have to reach
        finish = (self._num_rows - 1, self._num_cols - 1)
        stack = [(0, 0)]
        self._cells[0][0].visited = True

        while stack:
            i, j = stack[-1]  # Look at the top of the stack
            possible_directions = []
            
            if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_top_wall:
                possible_directions.append((-1, 0))
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_bottom_wall:
                possible_directions.append((1, 0))
            if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_left_wall:
                possible_directions.append((0, -1))
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_right_wall:
                possible_directions.append((0, 1))
            
            if possible_directions:
                
                direction = random.choice(possible_directions)
                next_i = i + direction[0]
                next_j = j + direction[1]
                
                if (next_i, next_j) == finish:
                    stack.append((next_i, next_j))
                    self._cells[i][j].draw_move(self._cells[next_i][next_j], undo=False)
                    break
                
                
                self._cells[i][j].draw_move(self._cells[next_i][next_j], undo=False)
                self._cells[next_i][next_j].visited = True
                stack.append((next_i, next_j))
                self._animate()
            
            else:
            # If no directions are possible, backtrack by popping from the stack
            # And making the line from the current to the previous object red py passing undo=True
            # THis isn't overwriting the previosly made gray line
                stack.pop()
                prev_i, prev_j = stack[-1]
                self._cells[i][j].draw_move(self._cells[prev_i][prev_j], undo=True)
                self._animate()                
                
        
    