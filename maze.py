
# initialize logical space
maze = []
reachable = []

# read from file
path = 'maze.txt'
with open(path, 'r') as source:
	lines = source.readlines()
	for line in lines:
		if len(line.strip().split()) > 5:
			maze.append([int(bit) for bit in line.strip().split()])

# check integrity
# print(len(maze))
# print(len(maze[0]))


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



# function to perform a check
def exp(x1, y1, x2, y2):

	# check inputs
	if maze[x1][y1] + maze[x2][y2] > 0:
		print(f'There is no path between ({x1}, {y1}) and ({x2}, {y2}).')
		reachable = []
		return

	# call DFS
	move_to(x1, y1)
	if check_noted(x2, y2):
		print(f'There is at least one path between ({x1}, {y1}) and ({x2}, {y2}).')
	else:
		print(f'There no path between ({x1}, {y1}) and ({x2}, {y2}).')
	reachable = []


print(maze[8][79])
print(maze[39][40])
# exp(4, 20, 79 ,66)

# exp(1, 34, 15, 47)
# exp(1, 2, 3, 39)
# exp(0, 0, 3, 77)
# exp(1, 75, 8, 79)
exp(1, 75, 39, 40)