from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player
import random

@app.route('/rules')
def rules():
    return render_template('rules.html', title='Rules')

@app.route('/<player1choice>/<player2choice>')
def juego(player1choice, player2choice):
    player1 = Player("Player1", player1choice)
    player2 = Player("Player2", player2choice)
    game = Game()
    result = game.lets_play(player1, player2)

    return render_template('index.html', title='Home', player1=player1, player2=player2, result=result)
