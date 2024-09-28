from tkinter import Canvas

class Line:
    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2

    def draw(self, canvas, fill_color):
        x1 = self.__point_1.x
        x2 = self.__point_2.x
        y1 = self.__point_1.y
        y2 = self.__point_2.y
        canvas.create_line(x1, x2, y1, y2, fill=fill_color, width=2)
    