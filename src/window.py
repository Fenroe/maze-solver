from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.__canvas = Canvas(self.__root_widget, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_is_running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()
    
    def wait_for_close(self):
        self.__window_is_running = True
        while self.__window_is_running:
            self.redraw()
    
    def close(self):
        self.__window_is_running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)