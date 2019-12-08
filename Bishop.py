from Piece import Piece

class Bishop(Piece):
	def __init__(self, team):
		self.name = 'Bishop'
		self.team = team
	
	def get_moves(self, x, y, board):
		moves = []

		for i in range(5):
			x_coord = x - i
			y_coord = y - i
			if self.check(x_coord, y_coord, board):
				moves += [(x_coord, y_coord)]
				if not self.is_blocked(x_coord, y_coord, board):
					break

		for i in range(5):
			x_coord = x + i
			y_coord = y + i
			if self.check(x_coord, y_coord, board):
				moves += [(x_coord, y_coord)]
				if not self.is_blocked(x_coord, y_coord, board):
					break

		for i in range(5):
			x_coord = x + i
			y_coord = y - i
			if self.check(x_coord, y_coord, board):
				moves += [(x_coord, y_coord)]
				if not self.is_blocked(x_coord, y_coord, board):
					break

		for i in range(5):
			x_coord = x - i
			y_coord = y + i
			if self.check(x_coord, y_coord, board):
				moves += [(x_coord, y_coord)]
				if not self.is_blocked(x_coord, y_coord, board):
					break

		return moves
