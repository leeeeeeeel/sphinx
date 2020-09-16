import tkinter as tk

SMALL_LENGHT = 3
BIG_LENGHT = 6

TOTAL_LENGHT = SMALL_LENGHT * BIG_LENGHT

class Number(tk.Button):
    def __init__(self, parent, i, j, *args, **kwargs):
        super().__init__(parent)

        self.i = i
        self.j = j

        self.initUI()
    
    def initUI(self):
        self.number = self.i * SMALL_LENGHT + self.j + 1

        self.configure(
            bg = "#404040", 
            fg = "#ec1325", 
            text = self.number,
            highlightbackground='#373737', 
            borderwidth=1, 
            relief='solid',
            command=self.select
        )


    def select(self):
        self.master.ret(self.number)

class Tile(tk.Button):
    def __init__(self, i, j, *args, **kwargs):
        super().__init__()

        self.i = i
        self.j = j

        self.initUI()
    
    def initUI(self):
        self.number = None

        mosaic_i = int(self.i / SMALL_LENGHT)
        mosaic_j = int(self.j / SMALL_LENGHT)

        if (mosaic_i + mosaic_j) % 2 == 0:
            bgcolor = '#373737'
        else:
            bgcolor = '#585858'

        self.m = mosaic_i * BIG_LENGHT + mosaic_j

        self.configure(
            bg = bgcolor, 
            fg = "#ec1325", 
            highlightbackground='#373737', 
            borderwidth=1, 
            relief='solid',
            command=self.select,
        )

    def select(self):
        self.master.selected_tile = (self.i, self.j)
       
        root = self.master
        mouse_x = root.winfo_pointerx() - root.winfo_rootx()
        mouse_y = root.winfo_pointery() - root.winfo_rooty()

        Chooser(self.master, self, mouse_x, mouse_y)

    def set_number(self, number):
        if self.number == number:
            self.number = None
            self.configure(text='')
        else:
            self.number = number
            self.configure(text=number)

class Sudoku(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('sudoku player')

        self.selected_tile = None

        self.init_grid()

    def init_grid(self, s=9):
        self.tiles = []
        for i in range(TOTAL_LENGHT):
            tk.Grid.rowconfigure(self.master, i, weight=1)
            tk.Grid.columnconfigure(self.master, i, weight=1)
            self.tiles.append([])
            for j in range(TOTAL_LENGHT):
                new_tile = Tile(i=i, j=j)
                new_tile.grid(row=i, column=j, sticky=tk.N+tk.S+tk.E+tk.W)
                self.tiles[i].append(new_tile)

class Chooser(tk.Toplevel):
    def __init__(self, parent, tile, mouse_x, mouse_y):
        tk.Toplevel.__init__(self, parent)
        self.tile = tile
        self.initUI(mouse_x, mouse_y)   

    def initUI(self, mouse_x, mouse_y):
        s = 80
        self.geometry("{0}x{1}+{2}+{3}".format(s, s+42, mouse_x, mouse_y))
        self.focus_set()

        self.result = None 

        self.init_numbers()

    def init_numbers(self):
        for i in range(SMALL_LENGHT):
            tk.Grid.rowconfigure(self, i, weight=1)
            tk.Grid.columnconfigure(self, i, weight=1)
            for j in range(SMALL_LENGHT):
                new_number = Number(parent=self, i=i, j=j)
                new_number.grid(row=i, column=j, sticky=tk.N+tk.S+tk.E+tk.W)

    def ret(self, number):
        self.withdraw()
        self.update_idletasks()

        self.tile.set_number(number)

        self.master.focus_set()
        self.destroy()
