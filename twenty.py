# ---------------------------------------------------------------------- 
# Miniproject: 2048 game.
# ---------------------------------------------------------------------- 

#
# This project was created for Caltech CS 1
# Problem credits, along with method boilerplates, go to Dr. Mike Vanier
#


#
# Problem 3.1
#

def make_board():
	'''
	Create a game board in its initial state.
	The board is a dictionary mapping (row, column) coordinates 
	(zero-indexed) to integers which are all powers of two (2, 4, ...).
	Exactly two locations are filled.
	Each contains either 2 or 4, with an 80% probability of it being 2.

	Arguments: none
	Return value: the board
	'''

	locations = []
	for i in range(4):
		for j in range(4):
			locations.append((i, j))
	random.shuffle(locations)
	loc_1 = locations[0]
	loc_2 = locations[1]
	val_1 = random.random()
	val_2 = random.random()
	if val_1 <= 0.8:
		val_1 = 2
	else:
		val_1 = 4
	if val_2 <= 0.8:
		val_2 = 2
	else:
		val_2 = 4
	retdict = {loc_1: val_1, loc_2: val_2}
	return retdict

#
# Problem 3.2
#

def get_row(board, row_n):
	'''
	Return a row of the board as a list of integers.
	Arguments:
	  board -- the game board
	  row_n -- the row number

	Return value: the row
	'''

	assert 0 <= row_n < 4
	ret = []
	for i in range(4):
		ret.append(board.get((row_n, i), 0))
	return ret

def get_column(board, col_n):
	'''
	Return a column of the board as a list of integers.
	Arguments:
	  board -- the game board
	  col_n -- the column number

	Return value: the column
	'''

	assert 0 <= col_n < 4
	ret = []
	for i in range(4):
		ret.append(board.get((i, col_n), 0))
	return ret

def put_row(board, row, row_n):
	'''
	Given a row as a list of integers, put the row values into the board.

	Arguments:
	  board -- the game board
	  row   -- the row (a list of integers)
	  row_n -- the row number

	Return value: none; the board is updated in-place.
	'''

	assert 0 <= row_n < 4
	assert len(row) == 4
	for i in range(4):
		if row[i] == 0:
			if (row_n, i) in board:
				del board[(row_n, i)]
		else:
			board[(row_n, i)] = row[i]


def put_column(board, col, col_n):
	'''
	Given a column as a list of integers, put the column values into the board.

	Arguments:
	  board -- the game board
	  col   -- the column (a list of integers)
	  col_n -- the column number

	Return value: none; the board is updated in-place.
	'''

	assert 0 <= col_n < 4
	assert len(col) == 4
	for i in range(4):
		if col[i] == 0:
			if (i, col_n) in board:
				del board[(i, col_n)]
		else:
			board[(i, col_n)] = col[i]
	

#
# Problem 3.3
#

def make_move_on_list(numbers):
	'''
	Make a move given a list of 4 numbers using the rules of the
	2048 game.

	Argument: numbers -- a list of 4 numbers
	Return value: the list after moving the numbers to the left.
	'''

	assert len(numbers) == 4
	nonzero = []
	for num in numbers:
		if num > 0:
			nonzero.append(num)
	leftover = 4 - len(nonzero)
	nonzero += leftover * [0]
	final = []
	i = 0
	while True:
		if i == 3:
			final.append(nonzero[i])
			break 
		elif i == 4:
			break
		elif nonzero[i] == nonzero[i+1]:
			final.append(2 * nonzero[i])
			i += 2
		else: 
			final.append(nonzero[i])
			i += 1
	final_leftover = 4 - len(final)
	final += final_leftover * [0]
	return final
#
# Problem 3.4
#

def make_move(board, cmd):
	'''
	Make a move on a board given a movement command.
	Movement commands include:

	  'w' -- move numbers upward
	  's' -- move numbers downward
	  'a' -- move numbers to the left
	  'd' -- move numbers to the right

	Arguments:
	  board  -- the game board
	  cmd    -- the command letter

	Return value: none; the board is updated in-place.
	'''

	assert cmd in ['w', 'a', 's', 'd']
	if cmd == 'w':
		for i in range(4):
			col = get_column(board, i)
			new_col = make_move_on_list(col)
			put_column(board, new_col, i)
	elif cmd == 's':
		for i in range(4):
			col = get_column(board, i)
			col.reverse()
			new_col = make_move_on_list(col)
			new_col.reverse()
			put_column(board, new_col, i)
	elif cmd == 'a':
		for i in range(4):
			row = get_row(board, i)
			new_row = make_move_on_list(row)
			put_row(board, new_row, i)
	elif cmd == 'd':
		for i in range(4):
			row = get_row(board, i)
			row.reverse()
			new_row = make_move_on_list(row)
			new_row.reverse()
			put_row(board, new_row, i)





#
# Problem 3.5
#

def game_over(board):
    '''
    Return True if the game is over i.e. if no moves can be made on the board.
    The board is not altered.

    Argument: board -- the game board
    Return value: True if the game is over, else False
    '''

    if not (len(board) == 16):
    	return False

    for cmd in ['w', 'a', 's', 'd']:
    	copied = board.copy()
    	make_move(copied, cmd)
    	if copied == board:
    		return True
    return False

#
# Problem 3.6
#

def update(board, cmd):
	'''
	Make a move on a board given a movement command.  If the board
	has changed, then add a new number (2 or 4, 90% probability it's 
	a 2) on a randomly-chosen empty square on the board.  
	If there are no empty squares, the game is over, so return False.

	Arguments:
	  board  -- the game board
	  cmd    -- the command letter

	Return value: none; the board is updated in-place.
	'''

	copied = board.copy()
	make_move(board, cmd)
	if board == copied:
		return 
	else:
		locations = []
		for i in range(4):
			for j in range(4):
				locations.append((i, j))
		loccopy = locations.copy()
		for loc in locations:
			if loc in board:
				loccopy.remove(loc)
		if len(loccopy) == 0:
			return False
		chosen = random.choice(loccopy)
		val = random.random()
		if val <= 0.8:
			val = 2
		else:
			val = 4
		board[chosen] = val


### Supplied to students:

def display(board):
	'''
	Display the board on the terminal in a human-readable form.

	Arguments:
	  board  -- the game board

	Return value: none
	'''

	s1 = '+------+------+------+------+'
	s2 = '| {:^4s} | {:^4s} | {:^4s} | {:^4s} |'

	print(s1)
	for row in range(4):
		c0 = str(board.get((row, 0), ''))
		c1 = str(board.get((row, 1), ''))
		c2 = str(board.get((row, 2), ''))
		c3 = str(board.get((row, 3), ''))
		print(s2.format(c0, c1, c2, c3))
		print(s1)

def play_game():
	'''
	Play a game interactively.  Stop when the board is completely full
	and no moves can be made.

	Arguments: none
	Return value: none
	'''

	b = make_board()
	display(b)
	while True:
		move = input('Enter move: ')
		if move not in ['w', 'a', 's', 'd', 'q']:
			print("Invalid move!  Only 'w', 'a', 's', 'd' or 'q' allowed.")
			print('Try again.')
			continue
		if move == 'q':  # quit
			return
		update(b, move)
		if not b:
			print('Game over!')
			break
		display(b)