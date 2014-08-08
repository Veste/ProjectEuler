## Goal: Find the highest product of 4 adjacent numbers in the grid

## Method: As long as we check incrementally, we only need to check right,
#    down, and diagonally right/down (incrementing from the top left corner)
grid_file = "grid.txt"

with open(grid_file) as gf:
	grid_lines = gf.readlines()
#end with grid file

grid = []

for line in grid_lines:
	grid_line = []
	for num in line.split():
		grid_line.append(int(num))
	#end for num in line
	grid.append(grid_line)
#end for line in grid

#for i in range(len(grid)):
#	grid_line = grid[i]
#	for j in range(len(grid_line)):
#		num = grid_line[j]
#		print("%02d " % num, end="")
#	#end for each column
#	print()
#end for each line

height = len(grid)
width = len(grid[0])
p_len = 4
largest_prod = 1788696

for i in range(height):
	for j in range(width):
		vertical = i + p_len > height
		if not vertical:
			prod = 1
			for k in range(p_len):
				prod *= grid[i+k][j]
			#end for k
			largest_prod = max(largest_prod, prod)
		#end if vertical
		
		horizontal = j + p_len > width
		if not horizontal:
			prod = 1
			for k in range(p_len):
				prod *= grid[i][j+k]
			#end for k
			largest_prod = max(largest_prod, prod)
		#end if horizontal
		
		if not vertical and not horizontal:
			prod = 1
			for k in range(p_len):
				prod *= grid[i+k][j+k]
			#end for k
			largest_prod = max(largest_prod, prod)
		#end if down+right
		
		if i - p_len >= 0 and not horizontal:
			prod = 1
			for k in range(p_len):
				prod *= grid[i-k][j+k]
			#end for k
			largest_prod = max(largest_prod, prod)
	#end for width
#end for height

print("Largest product is %d" % largest_prod)
