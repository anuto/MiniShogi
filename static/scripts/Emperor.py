from Piece import Piece

class Emperor(Piece):
	def __init__(self, team):
		self.name = 'Emperor'
		self.team = team
		Piece.__init__(self, team)

	def get_moves(self, x, y, board):
		moves = []

		for x_coord in range(-1, 2):
			for y_coord in range(-1, 2):
				if self.check(x_coord + x, y_coord + y, board):
					moves += [(x_coord + x, y_coord + y)]
		print "emp moves: " + str(moves)
		return moves
