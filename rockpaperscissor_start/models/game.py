class Game():

    def __init__(self):
        pass


    def lets_play(self, player1, player2):
        if player1.choice == "paper" and player2.choice == "scissors":
            return "Player 2 wins!"
        elif player1.choice == "scissors" and player2.choice == "rock":
            return "Player 2 wins"
        elif player1.choice == "rock" and player2.choice == "paper":
            return "Player 2 wins"
        elif player1.choice == "scissors" and player2.choice == "paper":
            return "Player 1 wins"
        elif player1.choice == "rock" and player2.choice == "scissors":
            return "Player 1 wins"
        elif player1.choice == "paper" and player2.choice == "rock":
            return "Player 1 wins"
        elif player1.choice == player2.choice:
            return "Oops try again"
