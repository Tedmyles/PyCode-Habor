import tkinter as tk
from tkinter import messagebox, ttk

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        # Entry widgets with styling
        for i in range(9):
            for j in range(9):
                entry = ttk.Entry(root, width=3, font=('Arial', 16), justify='center', textvariable=self.grid[i][j], style='Sudoku.TEntry')
                entry.grid(row=i, column=j)
                entry.bind('<Key>', lambda e, row=i, col=j: self.validate_input(e, row, col))

        # Solve and Reset buttons
        solve_button = ttk.Button(root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4, pady=10)

        reset_button = ttk.Button(root, text="Reset", command=self.reset_sudoku)
        reset_button.grid(row=9, column=5, pady=10)

        # Styling
        self.style = ttk.Style()
        self.style.configure('Sudoku.TEntry', padding=5)

    def validate_input(self, event, row, col):
        char = event.char
        if not (char.isdigit() and len(char) == 1):
            return "break"

    def solve_sudoku(self):
        if self.solve():
            self.show_solution()
        else:
            messagebox.showinfo("Error", "No solution exists!")

    def reset_sudoku(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j].set('')

    def solve(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in map(str, range(1, 10)):
            if self.is_safe(row, col, num):
                self.grid[row][col].set(num)

                if self.solve():
                    return True

                self.grid[row][col].set('')  # Backtrack if the current assignment doesn't lead to a solution

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if not self.grid[i][j].get():
                    return i, j
        return None

    def is_safe(self, row, col, num):
        return (
            self.is_safe_row(row, num) and
            self.is_safe_col(col, num) and
            self.is_safe_box(row - row % 3, col - col % 3, num)
        )

    def is_safe_row(self, row, num):
        return num not in [self.grid[row][col].get() for col in range(9)]

    def is_safe_col(self, col, num):
        return num not in [self.grid[row][col].get() for row in range(9)]

    def is_safe_box(self, start_row, start_col, num):
        return num not in [
            self.grid[row][col].get()
            for row in range(start_row, start_row + 3)
            for col in range(start_col, start_col + 3)
        ]

    def show_solution(self):
        messagebox.showinfo("Sudoku Solver", "Solution found!")
        for i in range(9):
            for j in range(9):
                self.grid[i][j].set(self.grid[i][j].get())

if __name__ == "__main__":
    root = tk.Tk()
    sudoku_solver = SudokuSolver(root)
    root.mainloop()
