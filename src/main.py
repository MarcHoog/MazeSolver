from graphics import Window
from cell import Cell 

def main():
    window = Window(800, 600)
    cell1 = cell = Cell(window, 100, 100, 200, 200)
    cell2 = cell = Cell(window, 100, 100, 300, 200)
    cell3 = cell = Cell(window, 100, 100, 400, 200)
    cell1.has_left_wall = False
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell1.draw_move(cell2, undo=True)
    window.wait_to_close()
    
if __name__ == '__main__':
    main()