import tkinter as tk
from tkinter import messagebox

# Step 1: Setting Up the Main Window
root = tk.Tk()
root.title("Tic Tac Toe")

# Step 2: Creating the Game Board
board_frame = tk.Frame(root)
board_frame.pack()

# Create buttons for the board
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(board_frame, text="", font='normal 30', width=5, height=2,
                           command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Step 3: Initializing Game Variables
current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]
computer = 'O'

# Step 4: Defining Button Click Functionality
def on_button_click(i, j):
    global current_player
    if buttons[i][j]['text'] == '' and board[i][j] == '':
        buttons[i][j]['text'] = current_player
        board[i][j] = current_player
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            if current_player == 'X':
                current_player = 'O'
                computer_move()

# Step 5: Implementing the Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_win():
        return 1 if current_player == 'X' else -1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = computer
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score

# Step 6: Defining the Computer Move Logic
def computer_move():
    global current_player
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = computer
                score = minimax(board, 0, False)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        i, j = best_move
        buttons[i][j]['text'] = computer
        board[i][j] = computer
        if check_win():
            messagebox.showinfo("Tic Tac Toe", "Computer wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = 'X'

# Step 7: Checking for Win or Draw
def check_win():
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def check_draw():
    for row in board:
        if '' in row:
            return False
    return True

# Step 8: Resetting the Game
def reset_game():
    global current_player, board
    current_player = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for button in row:
            button.config(text='')

# Step 9: Assembling the GUI
root.mainloop()
