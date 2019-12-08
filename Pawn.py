from Piece import Piece

class Pawn(Piece):
	def __init__(self, team):
		self.name = 'Pawn'
		self.team = team

	def get_moves(self, x, y, board):
		moves = []
		y_coord = y + self.y_dir()

		if self.check(x, y_coord, board):
			moves += [(x, y_coord)]
		
		return moves