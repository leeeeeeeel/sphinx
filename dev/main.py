from tkinter import Tk

from sudoku import Sudoku

def main():
    root = Tk()
    a, b = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (a, b))
    sudoku = Sudoku(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    