import tkinter as tk
import numpy as np

class SudokuGUI:
    
    # Initialize the sudoku board
    def __init__(self, master, puzzle):
        self.master = master
        self.master.title("Sudoku Puzzle")
        self.entries = []
        self.puzzle = puzzle

        self.create_grid()
        self.populate_grid()

        # Add the "Show Solution" button
        self.solve_button = tk.Button(self.master, text="Show Solution", command=self.show_solution)
        self.solve_button.grid(row=10, columnspan=9, pady=10)

    # Creating the 9 x 9 sudoku grid
    def create_grid(self):
        
        for i in range(9):
            row_entries = []
            for j in range(9):
                # frame is made to seperate each 3 x 3 grid
                frame = tk.Frame(self.master, borderwidth=2, relief="solid")
                frame.grid(row=i, column=j, padx=(1, 1 if (j + 1) % 3 != 0 else 5), pady=(1, 1 if (i + 1) % 3 != 0 else 5))
                # for user typing value
                entry = tk.Entry(frame, width=5, justify='center', font=('Arial', 18), fg='red')
                entry.pack(padx=1, pady=1)
                entry.bind("<KeyRelease>", self.on_key_release)
                row_entries.append(entry)
            self.entries.append(row_entries)

    # Populating the grid with numbers
    def populate_grid(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.puzzle[i][j]))
                    self.entries[i][j].config(state='readonly', fg='black')

    def on_key_release(self, event):
        widget = event.widget
        if widget.get() != '':
            widget.config(fg='red')
 
    # Displaying the solution when clicked 
    def show_solution(self):
        solved_puzzle = np.copy(self.puzzle)
        # Display only if there is a solution
        if self.solve(solved_puzzle):
            k = 0
            for i in range(9):
                for j in range(9):
                    if k<n:
                        # black color for already displayed numbers
                        if L[k] == [i,j]:
                            self.entries[i][j].config(state='normal')
                            self.entries[i][j].delete(0, tk.END)
                            self.entries[i][j].insert(0, str(solved_puzzle[i][j]))
                            self.entries[i][j].config(state='readonly', fg='black')
                            k+=1
                        # green color for non displayed numbers
                        else:
                            self.entries[i][j].config(state='normal')
                            self.entries[i][j].delete(0, tk.END)
                            self.entries[i][j].insert(0, str(solved_puzzle[i][j]))
                            self.entries[i][j].config(state='readonly', fg='green')
                    else:
                        self.entries[i][j].config(state='normal')
                        self.entries[i][j].delete(0, tk.END)
                        self.entries[i][j].insert(0, str(solved_puzzle[i][j]))
                        self.entries[i][j].config(state='readonly', fg='green')
        else:
            print("No solution exists!")

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.row_column_box_check(board, num, (row, col)):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = 0

        return False

    def row_column_box_check(self, board, num, pos):
        # Check row
        for i in range(9):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(9):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = (pos[1] // 3)*3
        box_y = (pos[0] // 3)*3

        for i in range(box_y , box_y + 3):
            for j in range(box_x, box_x + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)  # row, col
        return None

# Sample Sudoku puzzle (0 represents empty cells)

'''
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
'''


print("Welcome to the Sudoku Solver. Give a row-wise input of the sudoku puzzle; type 0 if the cell is empty")
puzzle = []
for i in range(9):
    print("Type the numbers with spaces of row ",i+1," :")
    puzzle.append(list(map(int,input().split())))

L = []


for i in range(9):
    for j in range(9):
        if puzzle[i][j] != 0:
            L.append([i,j])
n = len(L)

# Initialize Tkinter and create the Sudoku GUI
root = tk.Tk()
sudoku_gui = SudokuGUI(root, puzzle)
root.mainloop()