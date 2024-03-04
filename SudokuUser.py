# Third Python file (e.g., sudoku_main.py)

from SudokuGenerate import SudokuGenerate
from SudokuSolver import SudokuSolver

def create_and_save_sudoku(N, K, filename):
    # Generate Sudoku grid
    sudoku_generator = SudokuGenerate(N, K)
    sudoku_generator.fillValues()
    sudoku_generator.saveToFile(filename)
    print("Sudoku grid generated and saved to", filename)

def solve_sudoku(filename):
    # Solve Sudoku grid
    sudoku_solver = SudokuSolver(filename)
    sudoku_solver.solve()

# Driver code
if __name__ == "__main__":
    N = 9  # Size of the Sudoku grid
    K = 40  # Number of digits to remove
    filename = "sudoku_grid.txt"  # Name of the file to save the Sudoku grid

    # Create and save Sudoku grid
    create_and_save_sudoku(N, K, filename)

    # Ask the user if they want to solve the puzzle
    solve_now = input("Do you want to solve the Sudoku puzzle now? (yes/no): ").lower()
    if solve_now == "yes":
        # Solve Sudoku grid immediately
        solve_sudoku(filename)
    elif solve_now == "no":
        print("Sudoku puzzle saved. You can solve it later by running the solver.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")