
# initialize logical space
maze = []
reachable = []

# read from file
path = 'maze.txt'
# path = 'small.txt'
with open(path, 'r') as source:
	lines = source.readlines()
	for line in lines:
		if len(line.strip().split()) > 5:
			maze.append([int(bit) for bit in line.strip().split()])

# check integrity
print(len(maze))
print(len(maze[0]))


# add the given point into input's reachable group
def take_note_of(x, y):
	reachable.append([x, y])

# check if the given position is a free path
def check_position(x, y):
	if maze[x][y] == 1:
		return False
	else:
		return True

# check if a position is noted
def check_noted(x, y):
	for item in reachable:
		if x == item[0] and y == item[1]:
			return True
	return False

# DFS
def move_to(x, y):
	# mark self
	take_note_of(x, y)
	
	# print(f'x: {x}, y: {y}')

	if x == 37 and y == 77:
		print('Did hit it!!!!!!!!!!!!!!!!!!!!!!!!')

	# check left
	if y > 0:
		if check_position(x, y-1) and not check_noted(x, y-1):
			move_to(x, y-1)

	# check up
	if x > 0:
		if check_position(x-1, y) and not check_noted(x-1, y):
			move_to(x-1, y)

	# check right
	if y < 80:
		if check_position(x, y+1) and not check_noted(x, y+1):
			move_to(x, y+1)

	# check down
	if x < 80:
		if check_position(x+1, y) and not check_noted(x+1, y):
			move_to(x+1, y)


# get reachable group of first input
move_to(1, 75)

# for item in reachable:
# 	print(f'{item} : {maze[item[0]][item[1]]}')


# check if second input is in that group
if check_noted(37, 77):
	print("Yes, we find it")
else:
	print("Sorry, not reachable")

# print(maze[1][75])
# print(maze[37][77])