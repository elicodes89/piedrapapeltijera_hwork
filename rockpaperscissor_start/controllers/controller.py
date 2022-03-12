from flask import render_template, request
from app import app
from models.game import lets_play
from models.player import Player



# @app.route('/<player1choice>/<player2choice>')
# def juego(player1choice, player2choice):
#     player1 = Player("Player1", player1choice)
#     player2 = Player("Player2", player2choice)
#     return lets_play(player1, player2)
    # return player2choice

@app.route('/<player1choice>/<player2choice>')
def juego(player1choice, player2choice):
    player1 = Player("Player1", player1choice)
    player2 = Player("Player2", player2choice)
    result = lets_play(player1, player2)

    return render_template('index.html', title='Home', player1=player1, player2=player2, result=result)
