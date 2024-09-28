from line import Line
from point import Point

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def configure_line(self, edge_1, edge_2):
        point_1 = Point(edge_1[0], edge_1[1])
        point_2 = Point(edge_2[0], edge_2[1])
        line = Line(point_1, point_2)
        return line
    
    def draw(self, top_left, bottom_right):
        if self.has_left_wall:
            line = self.configure_line(top_left, (top_left[1], bottom_right[0]))
            self.__win.draw_line(line, "black")
        if self.has_right_wall:
            line = self.configure_line((top_left[0], bottom_right[1]), bottom_right)
            self.__win.draw_line(line, "black")
        if self.has_top_wall:
            line = self.configure_line(top_left, (top_left[0], bottom_right[1]))
            self.__win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = self.configure_line((top_left[1], bottom_right[0]), bottom_right)
            self.__win.draw_line(line, "black")
        