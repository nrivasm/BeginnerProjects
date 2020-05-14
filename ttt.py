import numpy as np
import sys

 # Setup
board = np.array([["[]","[]","[]"], ["[]","[]","[]"], ["[]","[]","[]"]])
numbers = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2)}

 # Functions
def check_win():
	diagonal_one = np.array([board[0,0], board[1,1], board[2,2]])
	diagonal_two = np.array([board[0,2], board[1,1], board[2,0]])
	win = np.array([False, False, False])
	symbol = "X"
	for i in range(2):
		for i in range(3):
			if diagonal_one[i] == symbol:
				win[i] = True
			else:
				win[i] = False
		if win[0] == True and win[1] == True and win[2] == True:
			print(symbol + " Won!")
			sys.exit()
		for i in range(3):
			if diagonal_two[i] == symbol:
				win[i] = True
			else:
				win[i] = False
		if win[0] == True and win[1] == True and win[2] == True:
			print(symbol + " Won!")
			sys.exit()
		for i in range(0, 3):
			rows_win = (board[i, :] == symbol).all()
			cols_win = (board[:, i] == symbol).all()
        
			if rows_win or cols_win:
				print(symbol + " won!")
				sys.exit()
		symbol = "O"

def ask_coordinates():
	if i%2 == 0:
		symbol = "O"
	else:
		symbol = "X"
	if np.count_nonzero(board == symbol) == 3:
		tile_take = input("Tile to take: ")
		try:
			tt = int(tile_take)
		except:
			print("That is not a tile!")
			ask_coordinates() 
		if tt < 1 or tt > 9:
			print("That is not a tile!")
			ask_coordinates()
		if board[numbers.get(tt)] == symbol:
			board[numbers.get(tt)] = "[]"
			print(str(board[0, :]))
			print(str(board[1, :]))
			print(str(board[2, :]))
		else:
			print("That tile isn't yours")
			ask_coordinates
	tile = input("Tile: ")
	try:
		num = int(tile)
	except:
		print("That is not a tile!")
		ask_coordinates() 
	if num < 1 or num > 9:
		print("That is not a tile!")
		ask_coordinates()
	if board[numbers.get(num)] != "X" and board[numbers.get(num)] != "O":
		board[numbers.get(num)] = symbol
		print_board()
	else:
		print("That tile is already in use!")
		ask_coordinates()

def print_board():
	print(str(board[0, :]))
	print(str(board[1, :]))
	print(str(board[2, :]))
	check_win()

print_board()
for i in range(1,1000):
	ask_coordinates()
	
