import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text="", width=10, height=3,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.buttons[row][col].cget("text") == "" and self.check_winner() is False:
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
                self.reset_board()
            elif all(cell != "" for row in self.board for cell in row):
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
                self.board[row][col] = ""

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToe().run()