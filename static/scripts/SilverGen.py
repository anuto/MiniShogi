from Piece import Piece
from GoldGen import GoldGen
class SilverGen(GoldGen):
	def __init__(self, team):
		self.name = 'SilverGen'
		self.team = team
		Piece.__init__(self, team, ["SilverGen", "GoldGen"])

	def get_moves(self, x, y, board):
		return []

	def get_moves(piece, x, y, board):
		coords = [
			(x - 1, y + Piece.y_dir(piece)),
			(x, y + Piece.y_dir(piece)),
			(x + 1, y + Piece.y_dir(piece)),
			(x + 1, y + -1 * Piece.y_dir(piece)),
			(x - 1, y + -1 * Piece.y_dir(piece))
		]

		moves = []
	
		for coord in coords:
			if Piece.check(piece, coord[0], coord[1], board):
				moves += [coord]
		return moves
