from Emperor import Emperor
from GoldGen import GoldGen
from SilverGen import SilverGen
from Bishop import Bishop
from Rook import Rook
from Pawn import Pawn

import copy

class Board:

	def __init__(self):
		self.board = [
			[None] * 5,
			[None] * 5,
			[None] * 5,
			[None] * 5,
			[None] * 5
		]
		# print self.board
		self.dead_pieces = {}
		self.dead_pieces[1] = []
		self.dead_pieces[2] = []

	def initialize(self):
		pieces = {}

		self.board[0][0] = Rook(1)
		self.board[0][1] = Bishop(1)
		self.board[0][2] = SilverGen(1)
		self.board[0][3] = GoldGen(1)
		self.board[0][4] = Emperor(1)
		self.board[1][4] = Pawn(1)

		self.board[4][4] = Rook(2)
		self.board[4][3] = Bishop(2)
		self.board[4][2] = SilverGen(2)
		self.board[4][1] = GoldGen(2)
		self.board[4][0] = Emperor(2)
		self.board[3][0] = Pawn(2)

		self.print_board()

	def print_board(self):
		print("off board: " + str(self.dead_pieces[1]))
		for row in self.board:
			row_s = ""
			for col in row:
				if col == None:
					row_s += "[  ]"
				else:
					name = col.name
					row_s += "["
					if name == 'Emperor':
						row_s += "E"
					elif name == "GoldGen":
						row_s += "G"
					elif name == "SilverGen":
						row_s += "S"
					elif name == "Bishop":
						row_s += "B"
					elif name == "Rook":
						row_s += "R"
					elif name == "Pawn":
						row_s += "P"
					else:
						raise Exception("weird piece: " + name)
					row_s += str(col.team)
					row_s += "]"
			print (row_s)

		print("off board: " + str(self.dead_pieces[2]))
		print()
		self.print_board_names()

	def print_board_names(self):
		for i in range(5):
			s = ""
			for j in range(5):
				s += "[" + str(j) + "," + str(i) + "]"
			print(s)

	def move(self, x1, y1, x2, y2):
		import pdb
		pdb.set_trace()
		curr = self.board[y1][x1]
		moves = self.get_valid_moves(x1, y1)

		if (x2, y2) in moves:
			self.board[y1][x1] = None
			other = self.board[y2][x2] 
			if not other == None:
				if curr.team == 1:
					self.dead_pieces[2].append(other)
				else:
					self.dead_pieces[1].append(other)
			self.board[y2][x2] = curr


	def valid_moves(self, team):
		moves = {}
		num_row = 0
		for row in self.board:
			num_col = 0
			for col in row:
				if not col == None and col.team == team:
					moves[((num_row, num_col), col)] = self.get_valid_moves(num_row, num_col)
				num_col += 1
			num_col = 0
			num_row += 1


		for dead_piece in self.dead_pieces[team]:
			moves[("(dead)", dead_piece)] = self.get_empty_spaces()

		return moves

	def get_valid_moves(self, num_row, num_col):
		moves = self.board[num_row][num_col].get_moves(num_col, num_row, self.board)
		return moves

	def get_empty_spaces():
		coords = []
		row_num = 0
		for row in self.board:
			col_num = 0
			for col in row:
				if col == None:
					coords += [(row_num, col_num)]
				col_num += 1
			row_num += 1
		return coords

