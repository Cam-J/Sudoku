def readFromFile(filename):
    with open(filename, 'r') as file:
        grid = [[int(num) for num in line.split()] for line in file]
    return grid

# Read the Sudoku grid from the file
sudoku_grid = readFromFile('sudoku_grid.txt')
print(sudoku_grid)