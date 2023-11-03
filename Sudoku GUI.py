import tkinter as tk

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=("Arial", 14), textvariable=self.grid[i][j])
                entry.grid(row=i, column=j)
        
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, columnspan=9)

    def solve_sudoku(self):
        puzzle = [[0 for _ in range(9)] for _ in range(9)]
        
        # Get the current values from the GUI grid
        for i in range(9):
            for j in range(9):
                value = self.grid[i][j].get()
                if value.isdigit() and int(value) in range(1, 10):
                    puzzle[i][j] = int(value)
        
        if self.solve(puzzle):
            # Update the GUI grid with the solved puzzle
            for i in range(9):
                for j in range(9):
                    self.grid[i][j].set(puzzle[i][j])
        else:
            print("No solution exists for the given puzzle.")

    def solve(self, puzzle):
        # Find an empty cell (with value 0) in the puzzle
        empty_cell = self.find_empty_cell(puzzle)
        if empty_cell is None:
            return True
        
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(puzzle, row, col, num):
                puzzle[row][col] = num

                if self.solve(puzzle):
                    return True
                
                puzzle[row][col] = 0  # Reset the value if it leads to a dead-end
        
        return False

    def find_empty_cell(self, puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, puzzle, row, col, num):
        # Check if the number is already present in the row
        for j in range(9):
            if puzzle[row][j] == num:
                return False
        
        # Check if the number is already present in the column
        for i in range(9):
            if puzzle[i][col] == num:
                return False
        
        # Check if the number is already present in the 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if puzzle[box_row + i][box_col + j] == num:
                    return False
        
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
