import tkinter as tk
from tkinter import messagebox
import random

# Step 1: Setting Up the Main Window
root = tk.Tk()
root.title("Tic Tac Toe 9x9")

# Step 2: Creating the Game Board
board_frame = tk.Frame(root)
board_frame.pack()

# Create buttons for the board
buttons = []
for i in range(9):
    row = []
    for j in range(9):
        button = tk.Button(board_frame, text="", font='normal 30', width=3, height=1,
                           command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Step 3: Initializing Game Variables
current_player = 'X'
board = [['' for _ in range(9)] for _ in range(9)]
computer = 'O'

# Step 4: Defining Button Click Functionality
def on_button_click(i, j):
    global current_player
    if buttons[i][j]['text'] == '' and board[i][j] == '':
        buttons[i][j]['text'] = current_player
        board[i][j] = current_player
        if check_win(current_player):
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            if current_player == 'X':
                current_player = 'O'
                computer_move()

# Step 5: Defining the Computer Move Logic
def computer_move():
    global current_player
    available_moves = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '']
    if available_moves:
        i, j = random.choice(available_moves)
        buttons[i][j]['text'] = computer
        board[i][j] = computer
        if check_win(computer):
            messagebox.showinfo("Tic Tac Toe", "Computer wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = 'X'

# Step 6: Checking for Win or Draw
def check_win(player):
    # Check rows, columns, and diagonals for five in a row
    for i in range(9):
        for j in range(5):
            if all(board[i][j+k] == player for k in range(5)):
                return True
            if all(board[j+k][i] == player for k in range(5)):
                return True
    for i in range(5):
        for j in range(5):
            if all(board[i+k][j+k] == player for k in range(5)):
                return True
            if all(board[i+4-k][j+k] == player for k in range(5)):
                return True
    return False

def check_draw():
    for row in board:
        if '' in row:
            return False
    return True

# Step 7: Resetting the Game
def reset_game():
    global current_player, board
    current_player = 'X'
    board = [['' for _ in range(9)] for _ in range(9)]
    for row in buttons:
        for button in row:
            button.config(text='')

# Step 8: Assembling the GUI
root.mainloop()
