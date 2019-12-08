from Piece import Piece

class SilverGen(Piece):
	def __init__(self, team):
		self.name = 'SilverGen'
		self.team = team

	def get_moves(self, x, y, board):
		return []

	def get_moves(self, x, y, board):
		coords = [
			(x - 1, y + self.y_dir()),
			(x, y + self.y_dir()),
			(x + 1, y + self.y_dir()),
			(x + 1, y + -1 * self.y_dir()),
			(x - 1, y + -1 * self.y_dir())
		]

		moves = []
	
		for coord in coords:
			if self.check(coord[0], coord[1], board):
				moves += [coord]
		return moves
