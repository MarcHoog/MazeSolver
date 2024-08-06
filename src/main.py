from graphics import Window
from cell import Cell 
from maze import Maze

def main():
    window = Window(900, 900)
    maze = Maze(window, 50, 50, 25, 25, 32, 32)
    maze.draw()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    window.wait_to_close()
    
if __name__ == '__main__':
    main()