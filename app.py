from flask import Flask, render_template, request, redirect, url_for, session
from game_logic import Game

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    player_name = request.form.get('player_name').strip()
    if player_name:
        session['player_name'] = player_name
        game = Game(player_name)
        session['game'] = game.to_dict()
        return redirect(url_for('game'))
    return render_template('index.html', error="Please enter a valid name.")

@app.route('/game')
def game():
    if 'game' not in session:
        return redirect(url_for('index'))
    game = Game.from_dict(session['game'])
    game.display_location()
    return render_template('game.html', game=game)

@app.route('/move/<direction>')
def move(direction):
    if 'game' not in session:
        return redirect(url_for('index'))
    game = Game.from_dict(session['game'])
    game.move(direction)
    session['game'] = game.to_dict()
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True)
