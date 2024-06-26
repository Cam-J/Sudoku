# Read the Sudoku grid from the file
def readFromFile(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read each line from the file and split it into numbers
        # Convert each number to an integer and create a list for each row
        # Create a 2D grid by appending each row to a list
        grid = [[int(num) for num in line.split()] for line in file]
    return grid

# Test the readFromFile function by printing the output
print(readFromFile("sudoku_grid.txt"))

class SudokuSolver:
    def __init__(self, filename):
        # Initialize the SudokuSolver class with the grid read from the file
        self.grid = self.readFromFile(filename)
        self.N = len(self.grid)

    def readFromFile(self, filename):
        # Read the Sudoku grid from the file and return it as a 2D list
        grid = []
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Split the line into numbers and convert them to integers
                row = list(map(int, line.strip().split()))
                # Append the row to the grid
                grid.append(row)
        return grid

    # Fail safe incase shit hits the fan, want to remove this to a point where it will not fail!
    def solve(self):
        # Solve the Sudoku puzzle
        if self.solveSudoku():
            # If a solution is found, print the solved Sudoku grid
            self.printSudoku()
        else:
            # If no solution exists, print a message
            print("No solution exists for the given Sudoku grid.")

    def findEmptyLocation(self):
        # Find the first empty location (cell with 0) in the Sudoku grid
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i][j] == 0:
                    return i, j
        # If no empty location is found, return None
        return None, None

    def isValid(self, row, col, num):
        # Check if it's valid to place a number 'num' in the given row and column of the Sudoku grid
        # Check if 'num' is not already present in the same row
        if num in self.grid[row]:
            return False

        # Check if 'num' is not already present in the same column
        for i in range(self.N):
            if self.grid[i][col] == num:
                return False

        # Check if 'num' is not already present in the 3x3 sub-grid
        subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def solveSudoku(self):
        # Solve the Sudoku puzzle using backtracking
        row, col = self.findEmptyLocation()
        # If no empty location is found, the Sudoku grid is fully filled and solved
        if row is None and col is None:
            return True

        # Try placing numbers from 1 to N in the empty location
        for num in range(1, self.N + 1):
            if self.isValid(row, col, num):
                # If 'num' is valid, place it in the empty location
                self.grid[row][col] = num
                # Recursively try to solve the Sudoku grid
                if self.solveSudoku():
                    return True
                # If no solution is found, backtrack and reset the cell to 0
                self.grid[row][col] = 0
        # If no solution is found, return False
        return False

    def printSudoku(self):
        # Print the Sudoku grid
        for row in self.grid:
            print(" ".join(map(str, row)))


# Driver code
if __name__ == "__main__":
    filename = "sudoku_grid.txt"  # Change this to the name of your saved Sudoku grid file
    solver = SudokuSolver(filename)
    solver.solve()
