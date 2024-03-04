import random
import math

class SudokuGenerate:
    def __init__(self, N, K):
        # Initialize the SudokuGenerate class with grid size N and number of digits to remove K
        self.N = N
        self.K = K

        # Square root of N
        SRNd = math.sqrt(N)
        self.SRN = int(SRNd)  # Size of each sub-grid (square root of N)
        self.mat = [[0 for _ in range(N)] for _ in range(N)]  # Initialize the Sudoku grid

    def fillValues(self):
        # Fill the Sudoku grid
        # fill diagonal of SRN x SRN
        self.fillDiagonal()
        # Fill remaining blocks
        self.fillRemaining(0, self.SRN)
        # Remove random digits
        self.removeKDigits()

    def fillDiagonal(self):
        # Fill the diagonal blocks of the Sudoku grid with random numbers
        for i in range(0, self.N, self.SRN):
            self.fillBox(i, i)
        
    def unUsedInBox(self, rowStart, colStart, num):
        # Check if a number is unused in a given sub-grid
        for i in range(self.SRN):
            for j in range(self.SRN):
                if self.mat[rowStart + i][colStart + j] == num:
                    return False
        return True
    
    def fillBox(self, row, col):
        # Fill a particular box of the Sudoku grid with random numbers
        num = 0
        for i in range(self.SRN):
            for j in range(self.SRN):
                while True:
                    num = self.randomGenerator(self.N)  # Generate a random number
                    if self.unUsedInBox(row, col, num):
                        break
                self.mat[row + i][col + j] = num
     
    def randomGenerator(self, num):
        # Generate a random number between 1 and num
        return math.floor(random.random() * num + 1)
     
    def checkIfSafe(self, i, j, num):
        # Check if it's safe to place a number at a given position in the Sudoku grid
        return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and self.unUsedInBox(i - i % self.SRN, j - j % self.SRN, num))
     
    def unUsedInRow(self, i, num):
        # Check if a number is unused in the given row
        for j in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True
     
    def unUsedInCol(self, j, num):
        # Check if a number is unused in the given column
        for i in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True
     
    
    def fillRemaining(self, i, j):
        # Recursively fill the remaining cells of the Sudoku grid
        # Check if we have reached the end of the matrix
        if i == self.N - 1 and j == self.N:
            return True
     
        # Move to the next row if we have reached the end of the current row
        if j == self.N:
            i += 1
            j = 0
     
        # Skip cells that are already filled
        if self.mat[i][j] != 0:
            return self.fillRemaining(i, j + 1)
     
        # Try filling the current cell with a valid value
        for num in range(1, self.N + 1):
            if self.checkIfSafe(i, j, num):
                self.mat[i][j] = num
                if self.fillRemaining(i, j + 1):
                    return True
                self.mat[i][j] = 0
         
        # No valid value was found, so backtrack
        return False
 
    # Choose random value and remove the value
    def removeKDigits(self):
        # Remove K random digits from the filled Sudoku grid
        count = self.K
 
        while (count != 0):
            i = self.randomGenerator(self.N) - 1
            j = self.randomGenerator(self.N) - 1
            if (self.mat[i][j] != 0):
                count -= 1
                self.mat[i][j] = 0
     
        return
    
    # Print the grid
    def printSudoku(self):
        # Print the Sudoku grid
        for i in range(self.N):
            for j in range(self.N):
                print(self.mat[i][j], end=" ")
            print()

    # Save grid to be used by solver
    def saveToFile(self, filename):
        # Save the generated Sudoku grid to a file
        with open(filename, 'w') as file:
            for row in self.mat:
                file.write(' '.join(map(str, row)) + '\n')
 
# Driver code
if __name__ == "__main__":
    N = 9  # Size of the Sudoku grid
    K = 40  # Number of digits to remove
    sudoku = SudokuGenerate(N, K)  # Create an instance of SudokuGenerate class
    sudoku.fillValues()  # Fill the Sudoku grid with values
    sudoku.printSudoku()  # Print the generated Sudoku grid
    sudoku.saveToFile("sudoku_grid.txt")  # Save the generated Sudoku grid to a file