import numpy as np 

def row_column_box_check(row,column,num):
    
    global sudoku # the changes in sudoku must be reflected
    
    # check if number exists in row
    for i in range(9): 
        if sudoku[row][i] == num:
            return False
    
    # check if number exists in column
    for i in range(9): 
        if sudoku[i][column] == num:
            return False
    
    box_x = (column // 3)*3
    box_y = (row // 3)*3
    
    # check if number exists in 3x3 box
    for i in range(3):
        for j in range(3):
            if sudoku[box_y+i][box_x+j] == num:
                return False
    
    return True

def solution():
    
    global sudoku # the changes in sudoku must be reflected
    
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                for num in range(1,10):
                    if row_column_box_check(row, column, num):
                        sudoku[row][column] = num
                        solution()
                        sudoku[row][column] = 0
                return
    print(np.matrix(sudoku))
    print('Other possible solutions')

# Sample sudoku puzzle
sudoku = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

solution()      
    