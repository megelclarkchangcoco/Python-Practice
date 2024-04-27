import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increase_score(self):
        self.score += 1

class CardGame:
    def __init__(self):
        self.player = None
        self.bot_score = 0
        self.player_score = 0

    def start(self):
        print("Welcome to Random Lucky Nine!")
        choice = int(input("1. Want to Play\n2. Cancel\nUser Input: "))
        if choice == 1:
            self.player = Player(input("Input Your Name: "))
            self.play_round()
        else:
            print("Game canceled.")

    def play_round(self):
        print("Let's Play the Game!")
        while True:
            print("1. Pick Card\n2. Cancel")
            choice = int(input("User Choice: "))
            if choice == 1:
                self.pick_card()
            elif choice == 2:
                break
            else:
                print("Invalid choice! Please choose again.")

    def pick_card(self):
        player_cards = [random.randint(1, 10), random.randint(1, 10)]
        bot_cards = [random.randint(1, 10), random.randint(1, 10)]
        player_total = sum(player_cards)
        bot_total = sum(bot_cards)

        print(f"Your cards are {player_cards}, total: {player_total}")
        print(f"Bot's cards are {bot_cards}, total: {bot_total}")

        if player_total > 9:
            print("You Lose, the bot wins!")
            self.bot_score += 1
        elif bot_total > 9:
            print("You Win!")
            self.player.increase_score()
        elif player_total == bot_total:
            print("It's a draw!")
        else:
            print("No winner in this round.")

        self.display_score()

    def display_score(self):
        print("Score:")
        print(f"{self.player.name}: {self.player.score}")
        print(f"Bot: {self.bot_score}")

        if self.bot_score == 3:
            print("The Game Winner is Bot")
        if self.player.score == 3:
            print("The Game Winner Is You " + self.player)

# Main
game = CardGame()
game.start()
