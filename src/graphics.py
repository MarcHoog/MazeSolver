from tkinter import Tk, BOTH, Canvas

class Point:
    
    def __init__(self, x, y):
        self.x = x # x coordinate Horizontal
        self.y = y # y coordinate Vertical


class Line:
    
    def __init__(self, start:Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, 
                           self.end.x, self.end.y, 
                           fill=fill_color)


class Cell:
    
    def __init__(self,window, width, height, x, y):
        self.window = window        

        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.x2 = x + width
        self.y2 = y + height
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
    def draw(self, fill_color):
        if self.has_left_wall:
            self.window.draw_line(Line(Point(self.x, self.y), Point(self.x, self.y2)), fill_color)
        if self.has_right_wall:
            self.window.draw_line(Line(Point(self.x2, self.y), Point(self.x2, self.y2)), fill_color)
        if self.has_top_wall:
            self.window.draw_line(Line(Point(self.x, self.y), Point(self.x2, self.y)), fill_color)
        if self.has_bottom_wall:
            self.window.draw_line(Line(Point(self.x, self.y2), Point(self.x2, self.y2)), fill_color)
        
    def __str__(self):
        return f'Cell(x={self.x}, y={self.y}, width={self.width}, height={self.height})'
    
    def __repr__(self):
        return str(self)

class Window:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.__running = False

        self.__root = Tk()
        self.__root.title("MazeSolver 3000")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, width=width, height=height, bg='white')
        self.__canvas.pack(fill=BOTH, expand=True)

        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_to_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        
    def close(self):
        self.__running = False
        return self.__running
    
    def draw_line(self, line:Line, fill_color):
        line.draw(self.__canvas, fill_color)
    