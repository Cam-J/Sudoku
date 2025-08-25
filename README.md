# 🔢 Sudoku Generator & Solver (Python)

A simple, pure-Python project to **generate** Sudoku puzzles and **solve** them via backtracking.  
Supports configurable grid size (default 9×9) and difficulty by removing a chosen number of digits.

---

## ✨ Features
- ✅ Generate valid Sudoku boards
- 🎚️ Control difficulty by removing `K` cells
- 💾 Save puzzles to a text file (space-separated rows)
- 🧩 Solve saved puzzles from file
- 🐍 Pure Python — **no external dependencies**

---

## 📁 Project Structure

```text
.
├─ SudokuGenerate.py   # Generator class (create & save puzzles)
├─ SudokuSolver.py     # Solver class (load & solve puzzles)
├─ sudoku_main.py      # Convenience script to generate then optionally solve
├─ sudoku_grid.txt     # Example output file (generated puzzle)
└─ README.md
```
---

## 🛠 Requirements
- Python **3.x** (3.8+ recommended)  
- No external libraries needed  

---

## 🚀 Quick Start

```bash
# Generate a puzzle and optionally solve it (guided prompt)
python sudoku_main.py

# Run Generator directly
python SudokuGenerate.py

# Run solver directly
python SudokuSolver.py
```
---

## Config
Configuration is controlled by:
- `N`: grid size (default 9; must be perfeact such that sqrt(N) is an integer.
- `K`: number of cells to remove. (40 for a moderate puzzle)

 ```python
N = 9
K = 40
```
---

## Notes
🧪 Notes & Limitations

- The generator assumes N is a perfect square (e.g., 9 where sqrt(9) = 3) to form valid sub-grids.
- Higher K → fewer givens → generally harder puzzles.
- Random removal does not guarantee a unique solution (common for simple generators). The solver still finds a valid one if it exists.

---

## Contribution
Contributions are welcome!
Open an issue or submit a PR to add features like:
- Unique-solution enforcement
- Difficulty grading
- CLI interface
- Benchmarking / performance improvements


