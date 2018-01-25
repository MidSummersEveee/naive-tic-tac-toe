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


# Level 1: Check Decisive Win Rows
# 1.1 check horizontal
def check_row_H():
	global MoveSide, WinSide
	for x in range(board_height):
		if sum(Board[x]) == 2*get_value_by_side():
			print(f'Decisive Move, Horizontal Row {x} to be Completed by {MoveSide}:')
			Board[x] = [2*get_value_by_side(), 2*get_value_by_side(), 2*get_value_by_side()]
			WinSide = MoveSide

# 1.2 check vertical
def check_row_V():
	global MoveSide, WinSide
	value = get_value_by_side()
	for y in range(board_width):
		if Board[0][y] + Board[1][y] + Board[2][y] == 2*value:
			print(f'Decisive Move, Vertical Row {y} to be Completed by {MoveSide}:')
			for temp in range(3):
				if Board[temp][y] == 0:
					place_stone(temp, y, value)
			WinSide = MoveSide

# 1.3 check diagonal
def check_row_D():
	global MoveSide, WinSide
	value = get_value_by_side()
	if sum(Board[i][i] for i in range(3)) == 2*value:
		print(f'Decisive Move, Diagonal Row \ to be Completed by {MoveSide}:')
		for temp in range(3):
			if Board[temp][temp] == 0:
				place_stone(temp, temp, value)
		WinSide = MoveSide
	elif sum(Board[i][2-i] for i in range(3)) == 2*value:
		print(f'Decisive Move, Diagonal Row / to be Completed by {MoveSide}:')
		for temp in range(3):
			if Board[temp][2-temp] == 0:
				place_stone(temp, 2-temp, value)
		WinSide = MoveSide

# Level 2: Counter Rows
# 2.1 block horizontal
def counter_row_H():
	global MoveSide, WinSide
	value_opp = get_value_by_side('1')
	value = get_value_by_side()
	for x in range(board_height):
		if sum(Board[x]) == 2*value_opp:
			print(f'Decisive Block, Horizontal Row {x} to be Completed by {MoveSide}:')
			for index, row_item in enumerate(Board[x]):
				if row_item == 0:
					place_stone(x, index, value)

# 2.2 block vertical
def counter_row_V():
	global MoveSide, WinSide
	value_opp = get_value_by_side('1')
	value = get_value_by_side()
	for y in range(board_width):
		if Board[0][y] + Board[1][y] + Board[2][y] == 2*value_opp:
			print(f'Decisive Block, Vertical Row {y} to be Completed by {MoveSide}:')
			for temp in range(3):
				if Board[temp][y] == 0:
					place_stone(temp, y, value)

# 1.3 block diagonal
def counter_row_D():
	global MoveSide, WinSide
	value_opp = get_value_by_side('1')
	value = get_value_by_side()
	if sum(Board[i][i] for i in range(3)) == 2*value_opp:
		print(f'Decisive Block, Diagonal Row \ to be Completed by {MoveSide}:')
		for temp in range(3):
			if Board[temp][temp] == 0:
				place_stone(temp, temp, value)
	elif sum(Board[i][2-i] for i in range(3)) == 2*value_opp:
		print(f'Decisive Block, Diagonal Row / to be Completed by {MoveSide}:')
		for temp in range(3):
			if Board[temp][2-temp] == 0:
				place_stone(temp, 2-temp, value)

# Level 3: Flock
def flock():
	move_space = []
	for x in range(board_height):
		for y in range(board_width):
			if Board[x][y] < 1:
				move_space.append("".join([str(x), str(y)]))
	for choice in move_space:
		if check_all_rows_by_point(int(choice[0]), int(choice[1])):
			print('Flock!!!!!')
			place_stone(int(choice[0]), int(choice[1]), get_value_by_side())
			break

# Level 4: Counter Flock
def counter_flock():
	move_space = []
	for x in range(board_height):
		for y in range(board_width):
			if Board[x][y] < 1:
				move_space.append("".join([str(x), str(y)]))
	for choice in move_space:
		print(f'inspecting {choice[0]}{choice[1]}')
		# if check_all_rows_by_point(int(choice[0]), int(choice[1]), counter="Yes") and foresee_if_safe_to_counter(int(choice[0]), int(choice[1])):
		if foresee_if_safe_to_counter(int(choice[0]), int(choice[1])) and check_all_rows_by_point(int(choice[0]), int(choice[1]), counter="Yes"):
			print('Counter Flock!!!!!')
			place_stone(int(choice[0]), int(choice[1]), get_value_by_side())
			break



def foresee_if_safe_to_counter(x,y):
	Board[x][y] = get_value_by_side()
	print("Experimenting")
	# print_board()
	opp_move_space = []
	for i in range(board_height):
		for j in range(board_width):
			if Board[i][j] < 1:
				opp_move_space.append("".join([str(i), str(j)]))
	# print(f'Oppent Move Space should be {opp_move_space}')
	for choice in opp_move_space:
		if check_all_rows_by_point(int(choice[0]), int(choice[1]), counter='Yes'):
			print('Foresee Opponent Flock!!!!!')
			Board[x][y] = 0
			print('Experiment Done, Recovered')
			return False
	Board[x][y] = 0
	# print_board()
	print('Experiment Done, Recovered')




# check if the position has potential to made a flock
def check_all_rows_by_point(x, y, counter=None):
	
	if counter:
		value = get_value_by_side('1')
	else:
		value = get_value_by_side()

	grade = 0
	if sum(Board[x]) == value:
		grade += 1
	if sum(Board[temp][y] for temp in range(3)) == value:
		grade += 1

	if x != 1 and y != 1:
		if x == y:
			if sum(Board[i][i] for i in range(3)) == value:
				grade += 1
		else:
			if sum(Board[2-i][i] for i in range(3)) == value:
				grade += 1

	if x == 1 and y == 1:
		if sum(Board[i][i] for i in range(3)) == value:
			grade += 1
		if sum(Board[2-i][i] for i in range(3)) == value:
			grade += 1

	if grade >= 2:
		return True



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





def place_at_reachable_corners():
	global MoveSide
	corner_space = []
	random_space = []
	for x in range(board_height):
		for y in range(board_width):
			if Board[x][y] < 1 and x != 1 and y != 1:
				corner_space.append("".join([str(x), str(y)]))
	if len(corner_space) != 0:
		choice = random.choice(corner_space)
		print("Go Corner")
		place_stone(int(choice[0]), int(choice[1]), get_value_by_side())
	else:
		for x in range(board_height):
			for y in range(board_width):
				if Board[x][y] < 1:
					random_space.append("".join([str(x), str(y)]))

		choice = random.choice(random_space)
		print('Go Random, should be middle edge')
		place_stone(int(choice[0]), int(choice[1]), get_value_by_side())





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

	if '11' in random_space:
		print('Go for center')
		place_stone(1, 1, get_value_by_side())
	elif '20' in random_space and '02' not in random_space:
		print('Against Opposite Corner')
		place_stone(2, 0, get_value_by_side())
	elif '02' in random_space and '20' not in random_space:
		print('Against Opposite Corner')
		place_stone(0, 2, get_value_by_side())
	elif '00' in random_space and '22' not in random_space:
		print('Against Opposite Corner')
		place_stone(0, 0, get_value_by_side())
	elif '22' in random_space and '00' not in random_space:
		print('Against Opposite Corner')
		place_stone(2, 2, get_value_by_side())
	# elif len([item in items if int(item[0]) == ])
	




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
		counter_row_V()

	if WinSide == '' and not Placed:
		counter_row_D()

	# FLOCK !
	if WinSide == '' and not Placed:
		flock()

	# COUNTER FLOCK !
	if WinSide == '' and not Placed:
		counter_flock()

	if WinSide == '' and not Placed:
		RandomMove()

	if WinSide == '' and not Placed:
		place_at_reachable_corners()
	
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