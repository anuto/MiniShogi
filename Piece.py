class Piece:
	def __repr__(self):
		return (self.name)

	def check(self, x, y, board):
		if x >= 0 and x < 5 and y >= 0 and y < 5:
			current = board[y][x]
			if current == None:
				return True
			return current.team != self.team
		else:
			return False

	def is_blocked(self, board, x, y):
		if x >= 0 and y < 5 and y >= 0 and y < 5:
			current = board[y][x]
			return current == None
		else:
			return True

	def y_dir(self):
		if self.team == 1:
			return 1
		else:
			return -1