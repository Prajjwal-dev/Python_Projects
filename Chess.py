import tkinter as tk
import random

# Define constants
BOARD_SIZE = 8
SQUARE_SIZE = 60
WHITE = "white"
BLACK = "black"
HIGHLIGHT_COLOR = "yellow"  # Color to highlight the selected piece
TEXT_COLOR_WHITE = "black"
TEXT_COLOR_BLACK = "white"

INITIAL_POSITION = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

class ChessGame:
    def __init__(self, root, mode="two-player"):
        self.root = root
        self.root.title("Chess Game")
        self.board = INITIAL_POSITION
        self.canvas = tk.Canvas(root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE)
        self.canvas.pack()
        self.selected_square = None
        self.turn = "white"  # White goes first
        self.mode = mode  # Mode can be "two-player" or "vs-computer"
        self.draw_board()
        self.draw_pieces()
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        colors = [WHITE, BLACK]
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                color = colors[(row + col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags=f"square_{row}_{col}")

    def draw_pieces(self):
        piece_images = {
            'r': "♜", 'n': "♞", 'b': "♝", 'q': "♛", 'k': "♚", 'p': "♟",
            'R': "♖", 'N': "♘", 'B': "♗", 'Q': "♕", 'K': "♔", 'P': "♙"
        }
        colors = [WHITE, BLACK]
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.board[row][col]
                if piece != ".":  # If there's a piece in the current position
                    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                    y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                    background_color = colors[(row + col) % 2]
                    text_color = TEXT_COLOR_BLACK if background_color == BLACK else TEXT_COLOR_WHITE
                    self.canvas.create_text(x, y, text=piece_images[piece], font=("Arial", 24), fill=text_color, tags="piece")

    def highlight_square(self, row, col):
        """Highlight the selected square."""
        self.canvas.delete("highlight")
        x1 = col * SQUARE_SIZE
        y1 = row * SQUARE_SIZE
        x2 = x1 + SQUARE_SIZE
        y2 = y1 + SQUARE_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=HIGHLIGHT_COLOR, tags="highlight")
        self.draw_board()
        self.draw_pieces()

    def on_click(self, event):
        col = event.x // SQUARE_SIZE
        row = event.y // SQUARE_SIZE
        if self.selected_square:
            old_row, old_col = self.selected_square
            if (row, col) != self.selected_square and self.is_valid_move(old_row, old_col, row, col):
                self.move_piece(old_row, old_col, row, col)
                self.selected_square = None
                self.canvas.delete("highlight")
                if self.mode == "vs-computer" and self.turn == "black":
                    self.computer_move()
            else:
                self.selected_square = None
                self.canvas.delete("highlight")
        else:
            piece = self.board[row][col]
            if self.is_valid_selection(row, col):
                self.selected_square = (row, col)
                self.highlight_square(row, col)

    def is_valid_selection(self, row, col):
        """Check if the selected piece belongs to the current player."""
        piece = self.board[row][col]
        if self.turn == "white" and piece.isupper():
            return True
        elif self.turn == "black" and piece.islower():
            return True
        return False

    def is_valid_move(self, old_row, old_col, new_row, new_col):
        """Placeholder function to check if the move is valid (implement rules later)."""
        piece = self.board[old_row][old_col]
        target = self.board[new_row][new_col]
        return (piece.isupper() and not target.isupper()) or (piece.islower() and not target.islower())

    def move_piece(self, old_row, old_col, new_row, new_col):
        piece = self.board[old_row][old_col]
        self.board[new_row][new_col] = piece
        self.board[old_row][old_col] = "."
        self.canvas.delete("all")
        self.draw_board()
        self.draw_pieces()
        self.switch_turn()

    def switch_turn(self):
        """Switch the turn between players."""
        self.turn = "black" if self.turn == "white" else "white"

    def computer_move(self):
        """Simple computer move - picks a random valid move."""
        valid_moves = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.board[row][col]
                if piece.islower():
                    for new_row in range(BOARD_SIZE):
                        for new_col in range(BOARD_SIZE):
                            if self.is_valid_move(row, col, new_row, new_col):
                                valid_moves.append((row, col, new_row, new_col))
        if valid_moves:
            old_row, old_col, new_row, new_col = random.choice(valid_moves)
            self.move_piece(old_row, old_col, new_row, new_col)

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root, mode="vs-computer")  # Change to "two-player" for two-player mode
    root.mainloop()
