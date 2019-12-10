from Piece import Piece
from GoldGen import GoldGen
from SilverGen import SilverGen

class Pawn(SilverGen):

	def __init__(self, team):
		self.name = 'Pawn'
		Piece.__init__(self, team, ["GoldGen", "SilverGen"])

	def get_moves(self, x, y, board):
		if not self.promoted:
			moves = []
			y_coord = y + self.y_dir()

			if self.check(x, y_coord, board):
				moves += [(x, y_coord)]
			return moves

		else:
			if self.promoted == "GoldGen":
				return GoldGen.get_moves(self, x, y, board)
			elif self.promoted == "SilverGen":
				return SilverGen.get_moves(self, x, y, board)
			else:
				raise Exception("unknown promotion: " + self.promoted)