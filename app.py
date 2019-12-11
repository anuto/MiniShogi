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
	global valid_squares
	valid_squares = b.valid_moves_from_html(pos)
	global selected
	selected = pos
	return redirect("/")

if __name__ == "__main__":
 	app.run()