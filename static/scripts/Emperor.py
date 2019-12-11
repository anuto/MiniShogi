from Piece import Piece

class Emperor(Piece):
	def __init__(self, team):
		self.name = 'Emperor'
		self.team = team
		Piece.__init__(self, team)

	def get_moves(self, x, y, board):
		return []

	def get_moves(self, x, y, board):
		moves = []
		for i in range(2):
			for j in range(2):
				if self.check(x + 2 * i - 1, y + 2 * j - 1, board):
					moves += [(x + 2 * i - 1, y + 2 * j - 1)]
		return moves
