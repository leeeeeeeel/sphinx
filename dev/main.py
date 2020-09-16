from tkinter import Tk

from sudoku import Sudoku

def main():
    root = Tk()
    
    s = root.winfo_screenheight()
    root.geometry("{0}x{0}+0+0".format(int(s-s/10)))
    root.resizable(width=False, height=False)

    sudoku = Sudoku(root)
    root.mainloop()

if __name__ == "__main__":
    main()