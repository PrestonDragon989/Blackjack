""" Blackjack Game File """
import random

class Blackjack():
    """ Class for the game blackjack """
    def __init__(self):
        # Betting Money
        self.money = 100
        self.dealer_money = 100

        self.money_bet = 0

        # Card Decks
        self.all_cards = [
            ["1", "Ace - Spades"], ["2", "2 - Spades"], ["3", "3 - Spades"], ["4", "4 - Spades"], ["5", "5 - Spades"], ["6", "6 - Spades"], ["7", "7 - Spades"], ["8", "8 - Spades"], ["9", "9 - Spades"], ["10", "10 - Spades"], ["11", "Jack - Spades"], ["12", "Queen - Spades"], ["13", "King - Spades"], # Spades
            ["1", "Ace - Diamonds"], ["2", "2 - Diamonds"], ["3", "3 - Diamonds"], ["4", "4 - Diamonds"], ["5", "5 - Diamonds"], ["6", "6 - Diamonds"], ["7", "7 - Diamonds"], ["8", "8 - Diamonds"], ["9", "9 - Diamonds"], ["10", "10 - Diamonds"], ["11", "Jack - Diamonds"], ["12", "Queen - Diamonds"], ["13", "King - Diamonds"], # Diamonds
            ["1", "Ace - Clubs"], ["2", "2 - Clubs"], ["3", "3 - Clubs"], ["4", "4 - Clubs"], ["5", "5 - Clubs"], ["6", "6 - Clubs"], ["7", "7 - Clubs"], ["8", "8 - Clubs"], ["9", "9 - Clubs"], ["10", "10 - Clubs"], ["11", "Jack - Clubs"], ["12", "Queen - Clubs"], ["13", "King - Clubs"], # Clubs
            ["1", "Ace - Hearts"], ["2", "2 - Hearts"], ["3", "3 - Hearts"], ["4", "4 - Hearts"], ["5", "5 - Hearts"], ["6", "6 - Hearts"], ["7", "7 - Hearts"], ["8", "8 - Hearts"], ["9", "9 - Hearts"], ["10", "10 - Hearts"], ["11", "Jack - Hearts"], ["12", "Queen - Hearts"], ["13", "King - Hearts"]  # Hearts
        ]
        self.card_deck = self.all_cards
        self.player_cards = []
        self.dealer_cards = []

        # Turn Number
        self.turn_number = 1

        # Playing Game
        self.game_start()

    def custom_betting_amount(self):
        """ Setting New Betting Amount """
        # Getting New Betting Amount
        while True:
            new_amount = input("What will your custom betting amount be? ")
            if new_amount.isdigit:
                if int(new_amount) > 0:
                    self.money = int(new_amount)
                    self.dealer_money = int(new_amount)
                    break
            print("That is not a valid amount. Amount must be higher than zero.")

    def game_over(self):
        """ Checking to see if anyone won """
        if self.dealer_money <= 0 or self.money <= 0:
            return True
        else:
            return False

    def reset_cards(self):
        """ Shuffle Deck & Collect Cards """
        # Reseting Card Hands
        self.dealer_cards = []
        self.player_cards = []

        # Reseting Card Deck
        self.card_deck = self.all_cards

    def find_total(self, player_deck = True):
        """ Find the total value of a card deck"""
        if player_deck:
            find_value_deck = self.player_cards
            count_aces = True
        else:
            find_value_deck = self.dealer_cards
            count_aces = False

        total = 0
        for card in find_value_deck:
            if int(card[0]) >= 10:
                total += 10
            elif int(card[0]) >= 2 and int(card[0]) <= 9:
                total += int(card[0])
            elif int(card[0]) == 1:
                if count_aces:
                    total = [total + 11, total + 1]
                else:
                    total += 11

        if not isinstance(total, list):
            total = [total]
        return total

    def deal_cards(self):
        """ Deal 2 cards to each the player and dealer & remove them from the deck """
        if len(self.card_deck) < 4:  # Check if there are at least 4 cards left in the deck
            self.reset_cards()  # If there are fewer than 4 cards, reset the deck
        else:
            for _ in range(2):
                # Deal 2 cards to the dealer
                card_dealt = random.randint(0, len(self.card_deck) - 1)
                self.dealer_cards.append(self.card_deck[card_dealt])
                self.card_deck.pop(card_dealt)

            for _ in range(2):
                # Deal 2 cards to the player
                card_dealt = random.randint(0, len(self.card_deck) - 1)
                self.player_cards.append(self.card_deck[card_dealt])
                self.card_deck.pop(card_dealt)

    def display_game_status(self):
        """ Display the game status (money, dealer money, cards, dealer cards) """
        print(f"Your Money: {self.money}    Dealer Money: {self.dealer_money}")
        
        # Show player their cards
        print(f"Your Cards:   Total: {self.find_total()}")
        for card in self.player_cards:
            print("\t", card[1])

        # Display visible dealer cards
        print("\nDealer Cards:")
        for card in self.dealer_cards:
            if card == self.dealer_cards[0]:
                print("\t (Hidden Card)")
            else:
                print("\t", card[1])

    def get_choice(self):
        """ Getting Player Choice (Getting new cards, betting amount) """
        # Getting Betting amount of the player
        betting_amount = 0
        while True:
            betting_amount = input("How much do you wish to bet? ")
            if betting_amount.isdigit():
                if int(betting_amount) <= 0:
                    print("You need to bet higher than 0!")
                elif int(betting_amount) > self.dealer_money or int(betting_amount) > self.money:
                    print("You can't bet more than you or the dealer has!")
                else:
                    self.money_bet = int(betting_amount)
                    break
            else:
                print("You need to bet a number!")

        # Asking player if they wish to hit:
        while True:
            get_another = input("Input 0 if you wish to hit. Press anything else to continue. ")
            if get_another == 1:
                # Deal the card to the player, & take it from the deck
                card_dealt = random.randint(0, len(self.card_deck) - 1)
                self.player_cards.append(self.card_deck[card_dealt])
                self.card_deck.remove(self.card_deck[card_dealt])
                print(f"You have received a {self.player_cards[-1]}!")
                for score in self.find_total(True):
                    if score > 21:
                        break
            else:
                break

    def dealer_turn(self):
        """ Controling Dealers turn """
        while True:
            if not self.card_deck:
                self.reset_cards()

            if self.find_total(False)[0] >= 16:
                # Deal the card to the dealer, & take it from the deck
                card_dealt = random.randint(0, len(self.card_deck) - 1)
                self.dealer_cards.append(self.card_deck[card_dealt])
                self.card_deck.remove(self.card_deck[card_dealt])
            else:
                break


    def check_win(self):
        """ Checking Who won that round """
        # Checking to see if either player went over
        top_player_number = self.find_total(True)[0]
        low_player_number = self.find_total(True)[0]
        for score in self.find_total(True):
            if score > top_player_number:
                top_player_number = score
            if score < low_player_number:
                low_player_number = score
            if top_player_number > 21:
                top_player_number = low_player_number
        if low_player_number > 21:
            return [False, "over"]
        elif self.find_total(False)[0] > 21:
            return [True, "over"]

        for value in self.find_total(True):
            if value > self.find_total(False)[0]:
                return [True, "higher"]

        if self.find_total(False)[0] == top_player_number:
            return [True, "equal"]
        return [False, "higher"]

    def apply_bet(self, apply = None):
        """ Apply the bet to the scores """
        if apply is None:
            pass
        elif apply:
            self.money += self.money_bet
            self.dealer_money -= self.money_bet
        elif not apply:
            self.money -= self.money_bet
            self.dealer_money += self.money_bet
        self.money_bet = 0

    def game_start(self):
        """ Start Blackjack """
        # Asking if they want to have a custom betting amount
        while True:
            print(f"Would you like to change the betting amount? Current amount is {self.money}.")
            change_amount = input("Type 0 to change money amount. Press anything else to move on! ")
            if change_amount == "0":
                self.custom_betting_amount()
            break

        # Gameloop
        print("\n\n")
        while not self.game_over():
            # Print Turn Number
            print(f"This is turn number {self.turn_number}!\n")

            # Deal Cards
            self.deal_cards()

            # Display Game Status
            self.display_game_status()

            # Getting Input Choice (Betting Amount, Get a new card or don't)
            self.get_choice()

            # Getting Dealer's Turn
            self.dealer_turn()

            # Checking who won that turn, & dishing out winnings
            if not self.check_win()[0] and self.check_win()[1] == "over":
                print("You lost that round! You went over!")
                self.apply_bet(False)
            elif self.check_win()[0] and self.check_win()[1] == "over":
                print("You won that round! Dealer went over!")
                self.apply_bet(True)
            elif not self.check_win()[0] and self.check_win()[1] == "higher":
                print("You lost that round! Dealer had a higher Number!")
                self.apply_bet(False)
            elif self.check_win()[0] and self.check_win()[1] == "higher":
                print("You won that round! You had a higher Number!")
                self.apply_bet(True)
            else:
                print("Nobody won! It was a tie!")
                self.apply_bet()

            # Update Turn Number
            self.turn_number += 1

            # Resetting the cards
            self.reset_cards()

        if self.money > 0:
            print("You won the game!")
        else:
            print("You lost the game!")

# Starting Game
if __name__ == "__main__":
    blackjack = Blackjack()