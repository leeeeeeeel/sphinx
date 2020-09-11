import tkinter as tk

class Tile(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.bg = 'red'


class Sudoku(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('sudoku player')

        self.tiles = []
        for i in range(3):
            self.tiles.append([])
            for j in range(3):
                new_tile = Tile(self)
                new_tile.grid(row=i, column=j)
                self.tiles[i].append(new_tile)