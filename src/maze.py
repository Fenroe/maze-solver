from cell import Cell
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.create_cells()

    def create_cells(self):
        self.cells = [[Cell(self.win) for _ in range(0, self.num_cols)] for _ in range(0, self.num_rows)]
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                self.draw_cell(i, j)

    def draw_cell(self, i, j):
        top = self.y1 - (self.cell_size_y * i)
        left = self.x1 + (self.cell_size_x * j)
        bottom = top - self.cell_size_y
        right = left + self.cell_size_x
        self.cells[i][j].draw(left, top, right, bottom)
        self.animate()


    def animate(self):
        self.win.redraw()
        sleep(0.05)