""" Blackjack Game File """
# Import random for shuffleing, & Colorama for Colors
import random
from colorama import Fore, Style

class Blackjack():
    """ Class for the game blackjack """
    def __init__(self):
        # Betting Money
        self.money = 100
        self.dealer_money = 100

        self.money_bet = 0

        # Card Decks
        self.all_cards = [
            ["1", f"Ace - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["2", f"2 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["3", f"3 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["4", f"4 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["5", f"5 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["6", f"6 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["7", f"7 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["8", f"8 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["9", f"9 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["10", f"10 - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["11", f"Jack - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["12", f"Queen - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], ["13", f"King - {Fore.LIGHTMAGENTA_EX}Spades{Fore.RESET}"], # Spades
            ["1", f"Ace - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["2", f"2 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["3", f"3 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["4", f"4 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["5", f"5 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["6", f"6 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["7", f"7 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["8", f"8 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["9", f"9 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["10", f"10 - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["11", f"Jack - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["12", f"Queen - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], ["13", f"King - {Fore.LIGHTBLUE_EX}Diamonds{Fore.RESET}"], # Diamonds
            ["1", f"Ace - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["2", f"2 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["3", f"3 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["4", f"4 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["5", f"5 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["6", f"6 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["7", f"7 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["8", f"8 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["9", f"9 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["10", f"10 - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["11", f"Jack - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["12", f"Queen - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], ["13", f"King - {Fore.LIGHTGREEN_EX}Clubs{Fore.RESET}"], # Clubs
            ["1", f"Ace - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["2", f"2 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["3", f"3 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["4", f"4 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["5", f"5 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["6", f"6 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["7", f"7 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["8", f"8 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["9", f"9 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["10", f"10 - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["11", f"Jack - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["12", f"Queen - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"], ["13", f"King - {Fore.LIGHTRED_EX}Hearts{Fore.RESET}"]  # Hearts
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
                print(card[0])
                total += int(card[0])
            elif int(card[0]) == 1:
                if count_aces:
                    total = [total + 1, total + 11]
                else:
                    total += 11

        if not isinstance(total, list):
            total = [total]
        return total

    def deal_cards(self):
        """ Deal 2 cards to each the player and dealer & remove them from the deck """
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

    def display_begging_game_status(self):
        """ Display the game status (current bet, cards, dealer cards) """        
        # Printing current bet
        print(f"\nCurrent bet: {Fore.CYAN}{Style.BRIGHT}{self.money_bet}{Fore.RESET}{Style.NORMAL}")

        # Show player their cards
        print(f"{Style.BRIGHT}Your Cards:   Total: {Style.NORMAL}{self.find_total()}")
        for card in self.player_cards:
            print("\t", card[1])

        # Display visible dealer cards
        print(f"\n{Style.BRIGHT}Dealer Cards:{Style.NORMAL}")
        for card in self.dealer_cards:
            if card == self.dealer_cards[0]:
                print(f"\t {Fore.LIGHTBLACK_EX}(Hidden Card){Fore.RESET}")
            else:
                print("\t", card[1])

    def display_game_status(self, show_dealer_card = False):
        """ Display Current Game Status """
        # Show player their cards
        print(f"{Style.BRIGHT}Your Cards:   Total: {Style.NORMAL}{self.find_total()}")
        for card in self.player_cards:
            print("\t", card[1])

        # Display visible dealer cards
        if not show_dealer_card:
            print(f"\n{Style.BRIGHT}Dealer Cards:{Style.NORMAL}")
        else:
            print(f"\n{Style.BRIGHT}Dealer Cards: {Style.NORMAL}{self.find_total(False)}")
        for card in self.dealer_cards:
            if card == self.dealer_cards[0] and not show_dealer_card:
                print(f"\t {Fore.LIGHTBLACK_EX}(Hidden Card){Fore.RESET}")
            else:
                print("\t", card[1])

    def get_bet(self):
        """ Get how much the player wishes to bet """
        # Getting Betting amount of the player
        betting_amount = 0
        print(f"{Style.BRIGHT}Your money:{Style.NORMAL} {Fore.GREEN}{self.money}{Fore.RESET}   {Style.BRIGHT}Dealer Money:{Style.NORMAL} {Fore.LIGHTMAGENTA_EX}{self.dealer_money}{Fore.RESET}")
        while True:
            betting_amount = input(f"How much do you wish to bet? {Fore.CYAN}{Style.BRIGHT}")
            print(Fore.RESET + Style.NORMAL, end="")
            if betting_amount.isdigit():
                if int(betting_amount) <= 0:
                    print(f"You need to bet {Style.BRIGHT}higher than 0!{Style.NORMAL}")
                elif int(betting_amount) > self.dealer_money or int(betting_amount) > self.money:
                    print(f"You can't bet {Style.BRIGHT}more than you or the dealer has!{Style.NORMAL}")
                else:
                    self.money_bet = int(betting_amount)
                    break
            else:
                print("You need to bet a number!")
  

    def get_choice(self):
        """ Getting Player Choice (Getting new cards) """
        # Asking player if they wish to hit:
        while True:
            get_another = input(f"{Style.BRIGHT}Input 0{Style.NORMAL} if you wish to{Style.BRIGHT} hit{Style.NORMAL}. Press {Style.BRIGHT}anything else{Style.NORMAL} to continue. ")
            if get_another == "0":
                # Deal the card to the player, & take it from the deck
                card_dealt = random.randint(0, len(self.card_deck) - 1)
                self.player_cards.append(self.card_deck[card_dealt])
                self.card_deck.remove(self.card_deck[card_dealt])
                if all(num > 21 for num in self.find_total(True)):
                    break
                self.display_game_status(False)
            else:
                break

    def dealer_turn(self):
        """ Controling Dealers turn """
        while True:
            if self.find_total(False)[0] <= 16:
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
            print(f"{Style.BRIGHT}Would you like to change the betting amount? Current amount is{Fore.YELLOW} {self.money}{Fore.RESET}{Style.NORMAL}.")
            change_amount = input("Type 0 to change money amount. Press anything else to move on! ")
            if change_amount == "0":
                self.custom_betting_amount()
            break

        # Gameloop
        print("\n")
        while self.money > 0 and self.dealer_money > 0:
            # Print Turn Number
            print(f"\nThis is turn number {Style.BRIGHT}{self.turn_number}{Style.NORMAL}!\n")

            # Get This turn's bet
            self.get_bet()

            # Deal Cards
            self.deal_cards()

            # Display Game Status
            self.display_begging_game_status()

            # Getting Input Choice (Betting Amount, Get a new card or don't)
            self.get_choice()

            # Getting Dealer's Turn
            self.dealer_turn()

            # Show The outcome of the turns
            print("\n")
            self.display_game_status(True)

            # Checking who won that turn, & dishing out winnings
            if not self.check_win()[0] and self.check_win()[1] == "over":
                print(f"You {Style.BRIGHT}{Fore.RED}lost{Fore.RESET} {Fore.CYAN}{self.money_bet}{Fore.RESET}{Style.NORMAL} that round! {Style.BRIGHT}You went over!{Style.NORMAL}\n")
                self.apply_bet(False)
            elif self.check_win()[0] and self.check_win()[1] == "over":
                print(f"You {Style.BRIGHT}{Fore.LIGHTGREEN_EX}won{Fore.RESET} {Fore.CYAN}{self.money_bet}{Fore.RESET}{Style.NORMAL} that round! {Style.BRIGHT}Dealer went over!{Style.NORMAL}\n")
                self.apply_bet(True)
            elif not self.check_win()[0] and self.check_win()[1] == "higher":
                print(f"You {Style.BRIGHT}{Fore.RED}lost{Fore.RESET} {Fore.CYAN}{self.money_bet}{Fore.RESET}{Style.NORMAL} that round! {Style.BRIGHT}Dealer had a higher Number!{Style.NORMAL}\n")
                self.apply_bet(False)
            elif self.check_win()[0] and self.check_win()[1] == "higher":
                print(f"You {Style.BRIGHT}{Fore.LIGHTGREEN_EX}won{Fore.RESET} {Fore.CYAN}{self.money_bet}{Fore.RESET}{Style.NORMAL} that round! {Style.BRIGHT}You had a higher Number!{Style.NORMAL}\n")
                self.apply_bet(True)
            else:
                print(f"{Style.BRIGHT}Nobody won{Style.NORMAL} anything! It was a{Style.BRIGHT} tie!{Style.NORMAL}\n")
                self.apply_bet()

            # Update Turn Number
            self.turn_number += 1

            # Resetting the cards
            self.reset_cards()

        if self.money > 0:
            print(f"{Fore.GREEN}{Style.BRIGHT}You won the game!")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}You lost the game!")

# Starting Game
if __name__ == "__main__":
    blackjack = Blackjack()