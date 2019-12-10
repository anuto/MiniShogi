from Piece import Piece

class GoldGen(Piece):
	def __init__(self, team):
		self.name = 'GoldGen'
		self.team = team
		Piece.__init__(self, team)

	def get_moves(piece, x, y, board):
		coords = [
			(x - 1, y),
			(x + 1, y),
			(x - 1, y + Piece.y_dir(piece)),
			(x, y + Piece.y_dir(piece)),
			(x + 1, y + Piece.y_dir(piece)),
			(x, y + -1 * Piece.y_dir(piece))
		]

		moves = []
	
		for coord in coords:
			if Piece.check(piece, coord[0], coord[1], board):
				moves += [coord]
		return moves

