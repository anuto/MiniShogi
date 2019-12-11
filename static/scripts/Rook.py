from Piece import Piece

class Rook(Piece):
	def __init__(self, team):
		self.name = 'Rook'
		self.team = team		
		Piece.__init__(self, team, ["King Dragon"])

	def get_moves(self, x, y, board):
		moves = []
		seen_enemy = False
		moves += self.get_range_of_moves()
			
		return moves

	def get_range_of_moves(self, x, y, board):
		moves = []
		seen_enemy = False
		for col in range(5):
			empty = self.is_empty(x, y, board)
			if empty: 
				moves += [(x, y)]
			elif self.on_same_team(x, y, board) or seen_enemy:
				return moves
			else:
				moves += [(x, y)]
				seen_enemy = True
		return moves

