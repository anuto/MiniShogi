from flask import Flask, Blueprint, render_template, request, redirect, url_for
from static.scripts import main
from static.scripts import Board 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def index():
	b = Board.Board()
	b.initialize()
	# board_state = b.board_state()
	board_state = b.board_state_for_html()
	return render_template('index.html', board=board_state)

@app.route('/get_valid_moves/<pos>')
def valid_moves(pos):
	valid_squares = b.valid_moves_from_html(pos)
	return render_template("index.html", board=board_state, valid_squares=valid_squares)

if __name__ == "__main__":
 	app.run()