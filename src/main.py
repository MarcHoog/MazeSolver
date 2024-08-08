from graphics import Window
from cell import Cell 
from maze import Maze

def main():
    window = Window(1800, 1800)
    maze = Maze(window, 50, 50, 100,100 , 16, 16)
    maze.draw()
    maze.solve()
    window.wait_to_close()
    
if __name__ == '__main__':
    main()