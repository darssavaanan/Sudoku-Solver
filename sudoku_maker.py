import tkinter as tk
import numpy as np

class SudokuGUI:
    
    def __init__(self, master, puzzle):
        self.master = master
        self.master.title("Sudoku Puzzle")
        self.entries = []
        self.puzzle = puzzle

        self.create_grid()
        self.populate_grid()
        

    def create_grid(self):
        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(self.master, width=5, justify='center', font=('Arial', 18),fg = 'red')
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def populate_grid(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.puzzle[i][j]))
                    self.entries[i][j].config(state='readonly')
            

# Sample Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Initialize Tkinter and create the Sudoku GUI
root = tk.Tk()
sudoku_gui = SudokuGUI(root, puzzle)
root.mainloop()