import tkinter as tk

class ChessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")
        self.geometry("400x400")
        
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        
        self.selected_piece = None
        self.create_board()
        
    def create_board(self):
        for i in range(8):
            for j in range(8):
                label = tk.Label(self, text=self.board[i][j], font=("Arial", 16))
                label.grid(row=i, column=j, padx=5, pady=5)
                label.bind("<Button-1>", lambda event, row=i, col=j: self.on_click(row, col))
                
    def on_click(self, row, col):
        if not self.selected_piece:
            piece = self.board[row][col]
            if piece != ' ':
                self.selected_piece = (row, col)
        else:
            self.move_piece(row, col)

    def move_piece(self, to_row, to_col):
        from_row, from_col = self.selected_piece
        piece = self.board[from_row][from_col]
        
        # Simple move: copy the piece to the new position
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = ' '
        
        # Update the GUI
        self.update_board()
        
        # Reset the selected piece
        self.selected_piece = None
    
    def update_board(self):
        # Update the labels to reflect the new board state
        for i in range(8):
            for j in range(8):
                self.children[f'!label{i}_{j}'].config(text=self.board[i][j])

# Cambio3: Crear otra instancia de ChessGame (added change)
chess_game_2 = ChessGame()
chess_game_2.mainloop()

