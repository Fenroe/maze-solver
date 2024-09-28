from line import Line
from point import Point

class Cell:
    def __init__(self, win):
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        self_center_x = (self.x1 + self.x2) // 2
        self_center_y = (self.y1 + self.y2) // 2
        to_cell_center_x = (to_cell.x1 + to_cell.x2) // 2
        to_cell_center_y = (to_cell.y1 + to_cell.y2) // 2
        self_point = Point(self_center_x, self_center_y)
        to_cell_point = Point(to_cell_center_x, to_cell_center_y)
        draw_move_line = Line(self_point, to_cell_point)
        fill_color = "red"
        if undo == True:
            fill_color = "gray"
        self._win.draw_line(draw_move_line, fill_color)