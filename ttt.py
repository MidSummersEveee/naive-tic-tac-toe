# @Author Zhihan Jiang
# Attempt on implementing a naive tic-tac-toe
import random


# Switching Player
def switch_player():
	global MoveSide
	if(MoveSide == 'White Turn'):
		MoveSide = 'Black Turn'
	else:
		MoveSide = 'White Turn'
	print(MoveSide)


def place_stone(x, y, value):
	Board[x][y] = value

# Attempts on Printing the Board
# for x in range(board_height):
# 	[print(Board[x][y], end='') if y < 2 else print(Board[x][y]) for y in range(board_width)]
def print_board():
	[[print(Board[x][y], end=' ') if y < 2 else print(Board[x][y]) for y in range(board_width)] for x in range(board_height)]



# Level 1: Check Rows
# 1.1 check horizontal
def check_row_H():
	global MoveSide, WinSide
	# print('Display Horizontal Sums')
	# [print(sum(Board[x])) for x in range(board_height)]
	if MoveSide == 'Black Turn':
		for x in range(board_height):
			if sum(Board[x]) == 2:
				print(f'Decisive Move Deteced, Horizontal Row {x} to be Completed by {MoveSide[0:5]}:')
				Board[x] = [1, 1, 1]
				WinSide = "Black"
	else:
		for x in range(board_height):
			if sum(Board[x]) == 8:
				print(f'Decisive Move Deteced, Horizontal Row {x} to be Completed by {MoveSide[0:5]}:')
				Board[x] = [4, 4, 4]
				WinSide = "White"

# 1.2 check vertical
def check_row_V():
	global MoveSide, WinSide
	if MoveSide == 'Black Turn':
		for y in range(board_width):
			if Board[0][y] + Board[1][y]+ Board[2][y] == 2:
				print(f'Decisive Move Deteced, Vertical Row {y} to be Completed by {MoveSide[0:5]}:')
				for temp in range(3):
					place_stone(temp, y, 1)
				WinSide = "Black"
	else:
		for y in range(board_width):
			if Board[0][y] + Board[1][y]+ Board[2][y] == 8:
				print(f'Decisive Move Deteced, Vertical Row {y} to be Completed by {MoveSide[0:5]}:')
				for temp in range(3):
					place_stone(temp, y, 4)
				WinSide = "White"

# 1.3 check diagonal
def check_row_D():
	global MoveSide, WinSide
	if MoveSide == 'Black Turn':
		if Board[0][0] + Board[1][1]+ Board[2][2] == 2:
			print(f'Decisive Move Deteced, Diagonal Row \ to be Completed by {MoveSide[0:5]}:')
			for temp in range(3):
				place_stone(temp, y, 1)
			WinSide = "Black"
	else:
		if Board[0][2] + Board[1][1]+ Board[2][0] == 8:
			print(f'Decisive Move Deteced, Diagonal Row / to be Completed by {MoveSide[0:5]}:')
			for temp in range(3):
				place_stone(temp, y, 4)
			WinSide = "White"




# Check if the board is full
def check_board_has_empty():
	unoccupied = []
	for x in range(board_height):
		for y in range(board_width):
			if Board[x][y] < 1:
				unoccupied.append('1')
	if len(unoccupied) == 0:
		return False
	else:
		return True


# Random Placing Method
def RandomMove():
	global MoveSide
	random_space = []
	# [[random_space.append("".join([str(x), str(y)])) if Board[x][y] < 1 for x in range(board_width)] for y in range(board_height)]
	for x in range(board_height):
		for y in range(board_width):
			if Board[x][y] < 1:
				random_space.append("".join([str(x), str(y)]))
	# print(random_space)
	if len(random_space) == 0:
		print("Game Over")
		return

	choice = random.choice(random_space)
	print(f'{MoveSide[0:5]} is going to place at {choice}')

	if MoveSide == 'Black Turn':
		place_stone(int(choice[0]), int(choice[1]), 1)
	else:
		place_stone(int(choice[0]), int(choice[1]), 4)




# Board Initialization
board_width, board_height = 3, 3;
Board = [[0 for x in range(board_width)] for y in range(board_height)]
print('Board Initialization Complete')

MoveSide = 'Black Turn'
WinSide = ''

# Game begin

# Board[0][0] = 1
# Board[0][2] = 1
# Board[1][0] = 1

while(WinSide == ''):
	check_row_H()

	if WinSide == '':
		check_row_V()
	
	if WinSide == '':
		RandomMove()
	
	if WinSide != '':
		print_board()
		print(f'Game Over! {WinSide} Win!')
		break
	
	if not check_board_has_empty():
		WinSide = 'Draw'
		print_board()
		print(f'Game Over! {WinSide}!')
		break

	print_board()
	switch_player()