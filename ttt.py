# @Author Zhihan Jiang
# Attempt on implementing a naive tic-tac-toe
import random

# Switching Player
def switch_player():
	global MoveSide
	if(MoveSide == 'White'):
		MoveSide = 'Black'
	else:
		MoveSide = 'White'
	print(f'{MoveSide} Turn')


def place_stone(x, y, value):
	global MoveSide
	global Placed
	Placed = True
	Board[x][y] = value
	print(f'{MoveSide[0:5]} is going to place at {x}{y}')

# Attempts on Printing the Board
def print_board():
	[[print(Board[x][y], end=' ') if y < 2 else print(Board[x][y]) for y in range(board_width)] for x in range(board_height)]


def get_value_by_side(code_verse=None):
	global MoveSide
	if code_verse:
		if MoveSide == 'Black':
			return 4
		else:
			return 1
	if MoveSide == 'Black':
		return 1
	elif MoveSide == 'White':
		return 4
	else:
		print('Please Check MoveSide global')
		return 'Please Check MoveSide global'


# Level 1: Check Rows
# 1.1 check horizontal
def check_row_H():
	global MoveSide, WinSide
	for x in range(board_height):
		if sum(Board[x]) == 2*get_value_by_side():
			print(f'Decisive Move Deteced, Horizontal Row {x} to be Completed by {MoveSide}:')
			Board[x] = [2*get_value_by_side(), 2*get_value_by_side(), 2*get_value_by_side()]
			WinSide = MoveSide

# 1.2 check vertical
def check_row_V():
	global MoveSide, WinSide
	value = get_value_by_side()
	for y in range(board_width):
		if Board[0][y] + Board[1][y] + Board[2][y] == 2*value:
			print(f'Decisive Move Deteced, Vertical Row {y} to be Completed by {MoveSide}:')
			for temp in range(3):
				if Board[temp][y] == 0:
					place_stone(temp, y, value)
			WinSide = MoveSide

# 1.3 check diagonal
def check_row_D():
	global MoveSide, WinSide
	value = get_value_by_side()
	if sum(Board[i][i] for i in range(3)) == 2*value:
		print(f'Decisive Move Deteced, Diagonal Row \ to be Completed by {MoveSide}:')
		for temp in range(3):
			if Board[temp][temp] == 0:
				place_stone(temp, temp, value)
		WinSide = MoveSide
	elif sum(Board[i][2-i] for i in range(3)) == 2*value:
		print(f'Decisive Move Deteced, Diagonal Row / to be Completed by {MoveSide}:')
		for temp in range(3):
			if Board[temp][2-temp] == 0:
				place_stone(temp, 2-temp, value)
		WinSide = MoveSide

# Level 2: Counter Rows
# 2.1 check horizontal
def counter_row_H():
	global MoveSide, WinSide
	value_opp = get_value_by_side('1')
	value = get_value_by_side()
	for x in range(board_height):
		if sum(Board[x]) == 2*value_opp:
			print(f'Decisive Move to be Countered, Horizontal Row {x} to be Completed by {MoveSide}:')
			for index, row_item in enumerate(Board[x]):
				if row_item == 0:
					place_stone(x, index, value)



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
	place_stone(int(choice[0]), int(choice[1]), get_value_by_side())




# Board Initialization
board_width, board_height = 3, 3;
Board = [[0 for x in range(board_width)] for y in range(board_height)]
print('Board Initialization Complete')

MoveSide = 'Black'
WinSide = ''
Placed = False

# Game begin

# Board[0][0] = 1
# Board[0][2] = 1
# Board[1][0] = 1

while(WinSide == ''):
	check_row_H()

	if WinSide == '':
		check_row_V()

	if WinSide == '':
		check_row_D()
	
	if WinSide == '':
		counter_row_H()

	if WinSide == '' and not Placed:
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
	Placed = False