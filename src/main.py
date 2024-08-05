from graphics import Window, Line, Point

def main():
    window = Window(800, 600)
    line1 = Line(Point(100, 100), Point(200, 200))
    line2 = Line(Point(200, 200), Point(300, 100))
    line3 = Line(Point(300, 100), Point(400, 200))
    window.draw_line(line1, 'red')
    window.draw_line(line2, 'green')
    window.draw_line(line3, 'blue')
    window.wait_to_close()
    
if __name__ == '__main__':
    main()