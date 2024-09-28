from window import Window
from point import Point
from line import Line

def main():
    print("Hi banana!")
    win = Window(800, 600)
    point_1 = Point(69, 23)
    point_2 = Point(100, 50)
    line = Line(point_1, point_2)
    win.draw_line(line, "pink")
    win.wait_for_close()

if __name__ == "__main__":
    main()