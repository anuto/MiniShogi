from flask import Flask, Blueprint, render_template, request, redirect, url_for
from static.scripts import main
from static.scripts import Board 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
b = Board.Board()
b.initialize()
valid_squares = None
board_state = b.board_state_for_html()
selected = None

@app.route('/')
def index():
	# board_state = b.board_state()
	return render_template('index.html', board=board_state, valid_squares=valid_squares, selected=selected)

@app.route('/get_valid_moves/<int:pos>')
def valid_moves(pos):

	if not selected or (valid_squares and pos not in valid_squares):
		global valid_squares
		valid_squares = b.valid_moves_from_html(pos)
		global selected
		# TODO: not strictly speaking true. could be an immobilized piece.
		if valid_squares:
			selected = pos
		else:
			selected = None
		return redirect("/")
	else:
		b.move_from_html(selected, pos)
		global valid_squares
		valid_squares = None
		global board_state
		board_state = b.board_state_for_html()
		global selected
		selected = None
		return redirect("/")


if __name__ == "__main__":
 	app.run()