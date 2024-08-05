from graphics import Window, Line, Point

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