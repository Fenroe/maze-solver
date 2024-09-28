from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        top_left = self._cells[0][0]
        top_left.has_top_wall = False
        self._draw_cell(0, 0)
        bottom_right = self._cells[self._num_cols - 1][self._num_rows - 1]
        bottom_right.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            neighbour_left = None
            neighbour_top = None
            neighbour_right = None
            neighbour_bottom = None
            if i - 1 > -1:
                neighbour_left = self._cells[i - 1][j]
            if j - 1 > -1:
                neighbour_top = self._cells[i][j - 1]
            if i + 1 < self._num_cols:
                neighbour_right = self._cells[i + 1][j]
            if j + 1 < self._num_rows:
                neighbour_bottom = self._cells[i][j + 1]
            if neighbour_left and neighbour_left.visited == False:
                to_visit.append(neighbour_left)
            if neighbour_bottom and neighbour_bottom.visited == False:
                to_visit.append(neighbour_bottom)
            if neighbour_right and neighbour_right.visited == False:
                to_visit.append(neighbour_right)
            if neighbour_top and neighbour_top.visited == False:
                to_visit.append(neighbour_top)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            next_cell = to_visit[random.randrange(0, len(to_visit))]
            if next_cell == neighbour_left:
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i, j)
                next_cell.has_right_wall = False
                self._draw_cell(i - 1, j)
                self._break_walls_r(i - 1, j)
            if next_cell == neighbour_right:
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i, j)
                next_cell.has_left_wall = False
                self._draw_cell(i + 1, j)
                self._break_walls_r(i + 1, j)
            if next_cell == neighbour_top:
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i, j)
                next_cell.has_bottom_wall = False
                self._draw_cell(i, j - 1)
                self._break_walls_r(i, j - 1)
            if next_cell == neighbour_bottom:
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i, j)
                next_cell.has_top_wall = False
                self._draw_cell(i, j + 1)
                self._break_walls_r(i, j + 1)
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False