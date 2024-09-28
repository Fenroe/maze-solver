from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    print("Hi banana!")
    win = Window(800, 600)
    cell = Cell(200, 300, 200, 300, win)
    cell.draw((max(cell.y1, cell.y2), min(cell.x1, cell.x2)), (min(cell.y1, cell.y2), max(cell.x1, cell.x2)))
    win.wait_for_close()

if __name__ == "__main__":
    main()