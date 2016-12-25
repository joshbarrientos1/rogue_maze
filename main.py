from __future__ import print_function

def print_maze(maze):
	for i in maze:
		for x in i:
			print(x, end='')
		print()

def find_current_position(maze):
	height = len(maze)
	for index_y, val_y in enumerate(maze):
		for index_x, val_x in enumerate(val_y):
			if val_x == '0':
				return [index_x, height - index_y]

def validate_move(maze, direction):
	print("You need to build this")

def update_current_position(maze, direction):
	current_position = find_current_position(maze)
	if direction == "w":
		current_position = [current_position[0], current_position[1] + 1]
	elif direction == "s":
		current_position = [current_position[0], current_position[1] - 1]
	elif direction == "a":
		current_position = [current_position[0] - 1, current_position[1]]
	elif direction == "d":
		current_position = [current_position[0] + 1, current_position[1]]
	return current_position

maze = [["0", ".", ".", "X"], ["X", "X", ".", "X"], ["!", ".", ".", "X"]];
print("Starting Point")
print(find_current_position(maze));
print("New Point")
print(update_current_position(maze, "a"))
