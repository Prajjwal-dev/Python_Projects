import tkinter as tk
from tkinter import messagebox
import math
import random

# Constants for the Tic-Tac-Toe board
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.current_player = PLAYER_X
        self.buttons = [[None] * 3 for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=EMPTY, font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == EMPTY and self.current_player == PLAYER_X:
            self.make_move(row, col, PLAYER_X)
            if self.check_winner() is None and not self.is_full():
                self.current_player = PLAYER_O
                self.ai_move()
                self.current_player = PLAYER_X

    def ai_move(self):
        move = self.best_move()
        if move:
            row, col = move
            self.make_move(row, col, PLAYER_O)
            if self.check_winner() is None and not self.is_full():
                self.current_player = PLAYER_X

    def make_move(self, row, col, player):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = player
            self.buttons[row][col].config(text=player)
            winner = self.check_winner()
            if winner:
                if winner == "Draw":
                    messagebox.showinfo("Game Over", "It's a draw!")
                else:
                    messagebox.showinfo("Game Over", f"The winner is {winner}!")
                self.reset_game()

    def check_winner(self):
        lines = [self.board[i] for i in range(3)]  # Rows
        lines += [[self.board[i][j] for i in range(3)] for j in range(3)]  # Columns
        lines += [[self.board[i][i] for i in range(3)]]  # Diagonal \
        lines += [[self.board[i][2 - i] for i in range(3)]]  # Diagonal /

        for line in lines:
            if line[0] != EMPTY and line[0] == line[1] == line[2]:
                return line[0]

        if all(cell != EMPTY for row in self.board for cell in row):
            return "Draw"

        return None

    def is_full(self):
        return all(cell != EMPTY for row in self.board for cell in row)

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner()
        if winner == PLAYER_X:
            return -10 + depth
        elif winner == PLAYER_O:
            return 10 - depth
        elif winner == "Draw":
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = PLAYER_O
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = EMPTY
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = PLAYER_X
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = EMPTY
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = PLAYER_O
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def reset_game(self):
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.current_player = PLAYER_X
        for row in self.buttons:
            for button in row:
                button.config(text=EMPTY)


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
