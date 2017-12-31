from tkinter import *
from twenty import *

# Execute this file to play the game

class Circle:
	'''template for the Circle object'''
	def __init__(self, canvas, center, size, val):
		self.canvas = canvas
		self.center = center
		self.size = size
		(x, y) = center
		x1 = x - size / 2 + 100
		y1 = y - size / 2 + 100
		x2 = x + size / 2 + 100
		y2 = y + size / 2 + 100
		if val == 0:
			self.handle = canvas.create_oval(x1, y1, x2, y2, outline="#4b738e"\
				, fill="#99ddff")
		if not (val == 0):
			if val == 2:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#66ccff")
			elif val == 4:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#1ab2ff")
			elif val == 8:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#0099e6")
			elif val == 16:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#0088cc")
			elif val == 32:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#0077b3")
			elif val == 64:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#006699")
			elif val == 128:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#005580")
			elif val == 256:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#004466")
			elif val == 512:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#00334d")
			elif val == 1024:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#002233")
			elif val == 2048:
				self.handle = canvas.create_oval(x1, y1, x2, y2, \
					outline="#4b738e", fill="#00111a")
			canvas.create_text(x+100, y+100, text=str(val), \
				fill="white", font=('Verdana', 50))



def visual_display(board):
	'''Created the board GUI from the dictionary of board values'''
	c.delete("all")
	c.create_rectangle(0, 0, game_size, game_size, fill="#4b738e")
	visual_board = {}
	for item in board:
		cent = (item[1] * square_size + square_size / 2, item[0] * square_size\
		 + square_size / 2)
		visual_board[item] = Circle(c, cent, circle_size, board[item])
	all_locations = {}
	for i in range(4):
		for j in range(4):
			all_locations[(i,j)] = 0
	for item in all_locations:
		if not (item in board):
			cent = (item[1] * square_size + square_size / 2, item[0] * \
				square_size + square_size / 2)
			visual_board[item] = Circle(c, cent, circle_size, \
				all_locations[item])


b = make_board()

def w_update(event):
	''' Moves the board up'''
	update(b, 'w')
	if game_over(b):
		c.create_text(400, 400, text="Game Over!")
		root.quit()
	visual_display(b)

def a_update(event):
	''' Moves the board left'''
	update(b, 'a')
	if game_over(b):
		c.create_text(400, 400, text="Game Over!")
		root.quit()
	visual_display(b)

def s_update(event):
	''' Moves the board down'''
	update(b, 's')
	if game_over(b):
		c.create_text(400, 400, text="Game Over!")
		root.quit()
	visual_display(b)

def d_update(event):
	''' Moves the board right'''
	update(b, 'd')
	if game_over(b):
		c.create_text(400, 400, text="Game Over!")
		root.quit()
	visual_display(b)

if __name__ == '__main__':
	root = Tk()
	root.geometry('800x800')
	square_size = 150
	circle_size = 100
	game_size = 800
	c = Canvas(root, width=game_size, height=game_size)
	c.pack()
	visual_display(b)
	root.bind('<w>', w_update)
	root.bind('<a>', a_update)
	root.bind('<s>', s_update)
	root.bind('<d>', d_update)
	visual_display(b)
	root.mainloop()