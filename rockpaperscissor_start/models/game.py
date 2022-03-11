# class Game():

# def __init__(self,player_1, player_2):
#         self.player_1 = player_1
#         self.player_2 = player_2

def lets_play(player1choice, player2choice):
        if player1choice == "paper" and player2choice == "scissors":
            return "Player 2 wins!"
        elif player1choice == "scissors" and player2choice == "rock":
            return "Player 2 wins"
        elif player1choice == "rock" and player2choice == "paper":
            return "Player 2 wins"
        elif player1choice == "scissors" and player2choice == "paper":
            return "Player 1 wins"
        elif player1choice == "rock" and player2choice == "scissors":
            return "Player 1 wins"
        elif player1choice == "paper" and player2choice == "rock":
            return "Player 1 wins"
        elif player1choice == player2choice:
            return "Oops, try again!"