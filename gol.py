import time
import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

grid = []
size = 32


def loop():
	init()
	while True:
		time.sleep(0.5)
		update()
		printgrid()


def init():
	global grid
	for i in range(size):
		grid.append([False for i in range(size)])

	# create a pulsar
	grid[3][5] = True
	grid[3][6] = True
	grid[3][7] = True
	grid[3][11] = True
	grid[3][12] = True
	grid[3][13] = True
	grid[5][3] = True
	grid[6][3] = True
	grid[7][3] = True
	grid[5][8] = True
	grid[6][8] = True
	grid[7][8] = True
	grid[5][10] = True
	grid[6][10] = True
	grid[7][10] = True
	grid[5][15] = True
	grid[6][15] = True
	grid[7][15] = True
	grid[8][5] = True
	grid[8][6] = True
	grid[8][7] = True
	grid[8][11] = True
	grid[8][12] = True
	grid[8][13] = True
	grid[10][5] = True
	grid[10][6] = True
	grid[10][7] = True
	grid[10][11] = True
	grid[10][12] = True
	grid[10][13] = True
	grid[11][3] = True
	grid[12][3] = True
	grid[13][3] = True
	grid[11][8] = True
	grid[12][8] = True
	grid[13][8] = True
	grid[11][10] = True
	grid[12][10] = True
	grid[13][10] = True
	grid[11][15] = True
	grid[12][15] = True
	grid[13][15] = True
	grid[15][5] = True
	grid[15][6] = True
	grid[15][7] = True
	grid[15][11] = True
	grid[15][12] = True
	grid[15][13] = True


def update():
	global grid
	def getNeighbors(x, y):
		nbrs = []
		try:
			if grid[x - 1][y]:
				nbrs.append(True)
		except IndexError:
			pass
		try:
			if grid[x - 1][y - 1]:
				nbrs.append(True)
		except IndexError:
			pass
		try:
			if grid[x - 1][y + 1]:
				nbrs.append(True)
		except IndexError:
			pass
		try:
			if grid[x][y - 1]:
				nbrs.append(True)
		except IndexError:
			pass
		try:
			if grid[x][y + 1]:
				nbrs.append(True)
		except IndexError:
			pass
		try:
			if grid[x + 1][y - 1]:
				nbrs.append(True)
		except IndexError:
			pass
		try:
			if grid[x + 1][y]:
				nbrs.append(True)
		except IndexError:
			pass
		try:
			if grid[x + 1][y + 1]:
				nbrs.append(True)
		except IndexError:
			pass
		return len(nbrs)

	newgrid = [[False for n in range(size)] for _n in range(size)]

	for x in range(size):
		for y in range(size):
			neighbors = getNeighbors(x, y)
			if grid[x][y] and neighbors <= 1:
				newgrid[x][y] = False
			if grid[x][y] and 2 <= neighbors <= 3:
				newgrid[x][y] = True
			if grid[x][y] and neighbors > 3:
				newgrid[x][y] = False
			if not grid[x][y] and neighbors == 3:
				newgrid[x][y] = True
	grid = newgrid


def printgrid():
	delete_last_lines()
	global grid
	for x in range(size):
		xstr = ''
		for y in range(size):
			if grid[x][y]:
				xstr += '■ '
			else:
				xstr += '□ '
		print(xstr)


def delete_last_lines(n=size):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


loop()
