from Emperor import Emperor
from GoldGen import GoldGen
from SilverGen import SilverGen
from Bishop import Bishop
from Rook import Rook
from Pawn import Pawn

import copy
import random

DEVELOPING = False

class Board:

	def __init__(self):
		self.board = [
			[None] * 5,
			[None] * 5,
			[None] * 5,
			[None] * 5,
			[None] * 5
		]

		self.dead_pieces = {}
		self.dead_pieces[1] = []
		self.dead_pieces[2] = []
		self.winner = None
		self.player_turn = 1

	def initialize(self):
		self.board = [
			[None] * 5,
			[None] * 5,
			[None] * 5,
			[None] * 5,
			[None] * 5
		]
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

		# self.print_board()
		self.dead_pieces = {}
		self.dead_pieces[1] = []
		self.dead_pieces[2] = []
		self.winner = None
		self.player_turn = 1

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
					row_s += str(col)
					row_s += "]"
			print (row_s)

		print("off board: " + str(self.dead_pieces[2]) + "\n")
		if DEVELOPING:
			self.print_board_names()

	def print_board_names(self):
		for i in range(5):
			s = ""
			for j in range(5):
				s += "[" + str(j) + "," + str(i) + "]"
			print(s)

	def get_player_turn(self):
		return self.player_turn

	def is_player_turn(self, inquiry):
		return inquiry == self.player_turn

	def is_valid_dead_piece(self, string_id):
		info = string_id.split("_")
		team = int(info[0][1])
		index = int(info[2])
		return self.dead_pieces[team][index].team == self.player_turn

	def is_valid_piece(self, pos):
		y = pos / 5
		x = pos % 5
		piece = self.board[y][x]
		return piece.team == self.player_turn

	def change_turn(self):
		if self.player_turn == 1:
			self.player_turn = 2
		else:
			self.player_turn = 1

	def move(self, x1, y1, x2, y2):

		curr = self.board[y1][x1]
		moves = self.get_valid_moves(y1, x1)

		if (x2, y2) in moves:
			self.board[y1][x1] = None
			other = self.board[y2][x2]
			self.check_winner(curr, other)

			if not other == None:
				self.dead_pieces[curr.team].append(other)
				other.died()
			self.board[y2][x2] = curr

		if self.check_promotion(curr, y2):
			ops = curr.promotion_ops()
			return ops

	def move_from_html(self, pos1, pos2):
		y1 = pos1 / 5
		x1 = pos1 % 5
		y2 = pos2 / 5
		x2 = pos2 % 5
		self.change_turn()
		ops = self.move(x1, y1, x2, y2)
		return self.board[y2][x2], ops

	def check_promotion(self, curr, y):
		team = curr.team
		return (team == 1 and y == 4) or (team == 2 and y == 0)

	def place_from_html(self, dead_id, pos):
		y = pos / 5
		x = pos % 5

		info = dead_id.split("_")
		team = int(info[0][1])
		index = int(info[2])
		dead_piece = self.dead_pieces[team][index]
		self.change_turn()
		self.board[y][x] = dead_piece
		print("dead index: " + str(index))
		self.dead_pieces[team].pop(index)

	def get_move(self, player):
		valid_moves = self.valid_moves(team)
		return random.choice(valid_moves)

	def place(self, piece, x, y):

		empty = self.get_empty_spaces()
		if (x, y) in empty:
			self.board[y][x] = piece[1]
			team = piece[1].team

			self.dead_pieces[team].remove(piece[1])
		else:
			raise Exception("not a valid place to place piece: " + str(piece[1]))

	def get_piece_name(self, x, y):
		return str(self.board[y][x])

	def check_winner(self, curr, other):
		other_name = str(other)
		other_piece_name = other_name[0]

		if other_piece_name == 'E':
			self.winner = curr.team

	def board_state(self):
		return self.board

	def board_state_for_html(self):
		i = 0
		mod_board = []
		for row in self.board:
			mod_row = []
			for square in row:
				mod_row += [(square, i)]
				i += 1
			mod_board.append(mod_row)
		print mod_board

		dead_html_1 = []
		for i in range(len(self.dead_pieces[1])):
			piece = self.dead_pieces[1][i]
			dead_html_1 += [(piece, i)]

		dead_html_2 = []
		for i in range(len(self.dead_pieces[2])):
			piece = self.dead_pieces[2][i]
			dead_html_2 += [(piece, i)]

		return mod_board, dead_html_1, dead_html_2

	def valid_moves_from_html(self, pos):
		num_row = pos / 5
		num_col = pos % 5
		print "row: " + str(num_row) 
		print "col: " + str(num_col)
		valid_moves = self.get_valid_moves(num_row, num_col)
		valid_squares = []
		for (x, y) in valid_moves:
			valid_squares.append(y * 5 + x)
		return valid_squares

	def empty_squares_for_html(self):
		empty_for_html = []
		empty_squares = self.get_empty_spaces()
		for (x, y) in empty_squares:
			empty_for_html.append(y * 5 + x)
		return empty_for_html

	def valid_moves(self, team):
		moves = {}
		num_row = 0
		for row in self.board:
			num_col = 0
			for col in row:
				if not col == None and col.team == team:
					moves[((num_col,  num_row), col)] = self.get_valid_moves(num_row, num_col)
				num_col += 1
			num_col = 0
			num_row += 1


		for dead_piece in self.dead_pieces[team]:
			moves[("(dead)", dead_piece)] = self.get_empty_spaces()

		return moves

	def get_valid_moves(self, num_row, num_col):
		moves = self.board[num_row][num_col].get_moves(num_col, num_row, self.board)
		return moves

	def get_empty_spaces(self):
		coords = []
		row_num = 0
		for row in self.board:
			col_num = 0
			for col in row:
				if col == None:
					coords += [(col_num, row_num)]
				col_num += 1
			row_num += 1
		return coords

	def game_over(self):
		return not self.winner == None

	def get_winner(self):
		if self.winner == None:
			raise Exception("game is not over")
		else:
			return self.winner

	def reset_board(self):
		self.initialize()

	def promote(self, piece, position):
		piece.promote(position)