# @Author Zhihan Jiang
# Attempt on implementing a naive tic-tac-toe
import random

# Board Initialization
board_width, board_height = 3, 3;
Board = [[0 for x in range(board_width)] for y in range(board_height)]
print('Board Initialization Complete')

MoveSide = 'Black Turn'

# NOTE: THE FUNCTION MUST BE CALLED AFTER CURRENT PLAYER PLAYCING
# THEIR STONES
def set_move_side(side):
	print_board()
	global MoveSide
	MoveSide = side
	print(side)


def place_stone(x, y, value):
	Board[x][y] = value

# Attempts on Printing the Board
# [[print(Board[x][y], end='') for x in range(board_width)] for y in range(board_height)]

# for x in range(board_height):
# 	[print(Board[x][y], end='') if y < 2 else print(Board[x][y]) for y in range(board_width)]

def print_board():
	[[print(Board[x][y], end=' ') if y < 2 else print(Board[x][y]) for y in range(board_width)] for x in range(board_height)]




# Level 1: Check Rows
# 1.1 check horizontal
def check_row_H():
	global MoveSide
	# print('Display Horizontal Sums')
	# [print(sum(Board[x])) for x in range(board_height)]
	if MoveSide == 'Black Turn':
		for x in range(board_height):
			if sum(Board[x]) == 2:
				print(f'Decisive Move Deteced, Horizontal Row {x} to be Completed by {MoveSide[0:5]}:')
				Board[x] = [1, 1, 1]
				set_move_side('White Turn')
	else:
		for x in range(board_height):
			if sum(Board[x]) == 8:
				print(f'Decisive Move Deteced, Horizontal Row {x} to be Completed by {MoveSide[0:5]}:')
				Board[x] = [4, 4, 4]
				set_move_side('Black Turn')



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
	print(random_space)
	if len(random_space) == 0:
		print("Game Over")
		return

	choice = random.choice(random_space)
	print(f'{MoveSide[0:5]} is going to place at {choice}')

	if MoveSide == 'Black Turn':
		place_stone(int(choice[0]), int(choice[1]), 1)
		set_move_side('White Turn')
	else:
		place_stone(int(choice[0]), int(choice[1]), 4)
		set_move_side('Black Turn')



# Game begin

Board[0][0] = 1
Board[0][2] = 1
Board[1][0] = 1

# print_board()

set_move_side('Black Turn')


# check_row_H()

# RandomMove()

while(check_board_has_empty()):
	check_row_H()
	RandomMove()
print("All places have been occupied, Game Over!")