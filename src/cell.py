from graphics import Window, Line, Point

class Cell:
    
    def __init__(self,window, width, height):
        self._window = window        

        self._width = width
        self._height = height
        
        self._x = None
        self._y = None
                
        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
    def draw(self, x, y, fill_color='black'):
        
        self._x = x
        self._y = y
        
        _x2 = x + self._width
        _y2 = y + self._height        
        if self.has_left_wall:
            self._window.draw_line(Line(Point(self._x,self._y), Point(self._x, _y2)), fill_color)
        else:
            self._window.draw_line(Line(Point(self._x, self._y), Point(self._x, _y2)), "white")        
    
        if self.has_right_wall:
            self._window.draw_line(Line(Point(_x2, self._y), Point(_x2, _y2)), fill_color)
        else:
            self._window.draw_line(Line(Point(_x2, self._y), Point(_x2, _y2)), "white")
            
        if self.has_top_wall:
            self._window.draw_line(Line(Point(self._x, self._y), Point(_x2, self._y)), fill_color)
        else:
            self._window.draw_line(Line(Point(self._x, self._y), Point(_x2, self._y)), "white")
        
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(self._x, _y2), Point(_x2, _y2)), fill_color)
        else:
            self._window.draw_line(Line(Point(self._x, _y2), Point(_x2, _y2)), "white")
       
    def draw_move(self, to_cell, undo=False):
        
        if undo:
            color = 'red'
        else:
            color = 'gray'
        
        center =  Point(self._x + self._width // 2, self._y + self._height // 2)
        to_center = Point(to_cell._x + to_cell._width // 2, to_cell._y + to_cell._height // 2)    
        
        self._window.draw_line(Line(center, to_center), color)
        
    def __str__(self):
        return f'Cell(x={self._x}, y={self._y}, width={self._width}, height={self._height})'
    
    def __repr__(self):
        return str(self)