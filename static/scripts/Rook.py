from Piece import Piece

class Rook(Piece):
	def __init__(self, team):
		self.name = 'Rook'
		self.team = team		
		Piece.__init__(self, team, ["King Dragon"])

	def get_moves(self, x, y, board):
		moves = []
		for col in range(5):
			occupied = self.check(x - col, y, board)
			if self.check(x - col, y, board):
				moves += [(x - col, y)]
				if not self.is_blocked(board, x - col, y):
					break

		for col in range(5):
			if self.check(x + col, y, board):
				moves += [(x + col, y)]
				if not self.is_blocked(board, x + col, y):
					break
		for row in range(5):
			if self.check(x, y + row, board):
				moves += [(x, y + row)]
				if not self.is_blocked(board, x, y + row):
					break

		for row in range(5):
			if self.check(x, y - row, board):
				moves += [(x, y - row)]
				if not self.is_blocked(board, x, y - row):
					break
			
		return moves

