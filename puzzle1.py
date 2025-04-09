import tkinter as tk
from tkinter import messagebox
import random

class PuzzleGame:
    def __init__(self, master, size=3):
        self.master = master
        master.title("3x3 Puzzle Game")
        self.size = size
        self.buttons = []
        self.empty_tile = size * size - 1
        self.board = list(range(1, size * size)) + [0]  # 0 represents the empty tile
        self.shuffle_board()
        self.create_widgets()

    def shuffle_board(self):
        # Simple shuffling algorithm
        for _ in range(1000):
            possible_moves = self.get_valid_moves(self.board.index(0))
            if possible_moves:
                move = random.choice(possible_moves)
                self.move_tile(move)

    def create_widgets(self):
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        for i in range(self.size):
            row_buttons = []
            for j in range(self.size):
                index = i * self.size + j
                value = self.board[index]
                text = str(value) if value != 0 else ""
                button = tk.Button(
                    self.button_frame,
                    text=text,
                    width=5,
                    height=2,
                    font=('Arial', 20),
                    command=lambda idx=index: self.move(idx)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def get_valid_moves(self, empty_index):
        row, col = divmod(empty_index, self.size)
        moves = []
        # Check adjacent tiles
        if row > 0:
            moves.append((row - 1) * self.size + col)  # Up
        if row < self.size - 1:
            moves.append((row + 1) * self.size + col)  # Down
        if col > 0:
            moves.append(row * self.size + col - 1)  # Left
        if col < self.size - 1:
            moves.append(row * self.size + col + 1)  # Right
        return moves

    def move(self, clicked_index):
        empty_index = self.board.index(0)
        valid_moves = self.get_valid_moves(empty_index)

        if clicked_index in valid_moves:
            self.move_tile(clicked_index)
            self.update_buttons()
            if self.check_win():
                messagebox.showinfo("Congratulations!", "You solved the puzzle!")

    def move_tile(self, clicked_index):
        empty_index = self.board.index(0)
        self.board[empty_index], self.board[clicked_index] = self.board[clicked_index], self.board[empty_index]

    def update_buttons(self):
        for i in range(self.size):
            for j in range(self.size):
                index = i * self.size + j
                value = self.board[index]
                text = str(value) if value != 0 else ""
                self.buttons[i][j].config(text=text)

    def check_win(self):
        target_board = list(range(1, self.size * self.size)) + [0]
        return self.board == target_board

if __name__ == '__main__':
    root = tk.Tk()
    game = PuzzleGame(root)
    root.mainloop()