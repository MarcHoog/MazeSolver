from graphics import Window, Line, Point

class Cell:
    
    def __init__(self,window, width, height, x, y):
        self._window = window        

        self._width = width
        self._height = height
        
        self._x = x
        self._y = y
        
        self._x2 = x + width
        self._y2 = y + height
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
    def draw(self, fill_color='black'):
        if self.has_left_wall:
            self._window.draw_line(Line(Point(self._x, self._y), Point(self._x, self._y2)), fill_color)
        if self.has_right_wall:
            self._window.draw_line(Line(Point(self._x2, self._y), Point(self._x2, self._y2)), fill_color)
        if self.has_top_wall:
            self._window.draw_line(Line(Point(self._x, self._y), Point(self._x2, self._y)), fill_color)
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(self._x, self._y2), Point(self._x2, self._y2)), fill_color)
    
    def __get_move_color(self, undo):
        if undo:
            return 'red'
        else:
            return 'gray'
    
    def draw_move(self, to_cell, undo=False):
        center =  Point(self._x + self._width // 2, self._y + self._height // 2)
        to_center = Point(to_cell._x + to_cell._width // 2, to_cell._y + to_cell._height // 2)    
        
        self._window.draw_line(Line(center, to_center), self.__get_move_color(undo))
        
    def __str__(self):
        return f'Cell(x={self._x}, y={self._y}, width={self._width}, height={self._height})'
    
    def __repr__(self):
        return str(self)