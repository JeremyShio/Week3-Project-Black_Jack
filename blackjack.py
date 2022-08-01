# ---> HOW TO PLAY BLACKJACK?!? <---

# In the casino version, the house is the dealer (a "permanent bank"). The dealer is in charge of running all aspects of the game, from shuffling and dealing the cards to handling all bets.
# -> OBJECTIVE OF THE GAME <-
# Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
# -> CARD VALUES AND SCORING <-
# It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.
# -> BETTING <-
# Before the deal begins, each player places a bet, in chips, in front of them in the designated area. Minimum and maximum limits are established on the betting, and the general limits are from $2 to $500.
# -> THE SHUFFLE <-
# The dealer thoroughly shuffles portions of the pack until all the cards have been mixed and combined.
# -> THE DEAL <-
# The dealer receives one card face up and one card face down. Each player, receives two cards face up.
# -> THE PLAY <-
# The player goes first and must decide whether to "stand" (not ask for another card) or "hit" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly). Thus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stand on the total (if it is 21 or under), or goes "bust" (if it is over 21). In the latter case, the player loses and the dealer collects the bet wagered. The dealer then turns to the next player to their left and serves them in the same manner.
# -> THE DEALER <-
# When the dealer has served every player, the dealers face-down card is turned up. If the total is 17 or more, it must stand. If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.
# -> SIGNALING INTENTIONS <-
# When a player's turn comes, they can "Hit" or can get another card.  Alternatively the player can decide to "Stand" or NOT get another card.
# -> BASIC STRATEGY <-
# Winning tactics in Blackjack require that the player play each hand in the optimum way, and such strategy always takes into account what the dealer's upcard is. When the dealer's upcard is a good one, a 7, 8, 9, 10-card, or ace for example, the player should not stop drawing until a total of 17 or more is reached. When the dealer's upcard is a poor one, 4, 5, or 6, the player should stop drawing as soon as he gets a total of 12 or higher. The strategy here is never to take a card if there is any chance of going bust.

# ---> SOME COMMENTS!!! <---

# What do we need?! ᕙ(⇀‸↼‶)ᕗ
# ***Asking coding Bulbasaur***
# We need... (๑•̀ㅂ•́)و
# Cards with suits and values (each card has it's own value based on suit/value)
# Deck to hold cards (52 cards in deck, 1 card of each suit/value)
# Player can hold cards (Both cards shown FACE UP)
# Name, Money for player (Money for player can run out/go to 0)
# Can check name and money of player
# Dealer can hold cards (Player with name "Dealer" - NPC/Computer)
# First card FACE UP, second card FACE DOWN for dealer
# No money for dealer, casino has infinite $$$
# Play game, table up to 6 players 
# Winner after game, can make new game

# ---> PSUEDO CODE?!? <---

# -> Class - Card <-
# suit (4)
# value (13)
# -> Class - Deck <-
# cards (52)
# -> Class - Player <-
# cards (2)
# name
# money(check and +/-)
# bet
# -> Sub - Dealer <-
# cards (2 - 1 face up/1 face down)
# First card face up, second card face down
# -> Class - Game <-
# menu
# num of players
# game winner
# new game

# ---> CODE HERE!!! <---

import random

# -> Card: suit, value <-
class Card:
    # List defining Card suit/value (Ordered from lowest suit/value to highest suit/value)
    suits = ['♣', '♦', '♥', '♠']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    # Make card suit and card value (Can reference self.suit/self.value)
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    # __lt__() method to apply sorting or order to card suit/value (Sorting/order based on order in suits/values list)
    def __lt__(self, other):
        # If player is given 2 cards with the same value... (Pair of Ace's)
        if self.value == other.value:
            # ...then we order cards by suit based on the order in suits list (Ordered from lowest to highest suit)
            return self.suit < other.suit
        # If player card values are not the same... (Ace, 7)
        else:
            #...then we order cards by value based on the order in the values list (Ordered from lowest to highest value)
            return self.value < other.value
    # __str__() method to display string representation of card value followed by card suit (Ace of ♠'s)
    def __str__(self):
        return f"|{Card.values[self.value]} of {Card.suits[self.suit]}'s| "
# -> Deck: Cards <-
class Deck:
    # Make empty list to hold cards (deck)
    def __init__ (self):
        self.deck = []
        # Limit set to 4 different card suits
        for suit in range(4):
            # Limit set to 13 different card values
            for value in range(13):
                # Adding cards to the deck (52 cards - 1 of each suit/value)
                self.deck.append(Card(suit, value))
        # Shuffling the deck with shuffle function
        self.shuffle()
    # __len__() method to display card count in deck
    def __len__(self):
        return len(self.deck)
    # add_card() function to add cards to the deck
    def add_card(self, card):
        self.deck.append(card)
    # pop_card() function to move cards from the deck to the player
    def pop_card(self):
        return self.deck.pop()
    # shuffle() function to reorganize or randomize cards in deck
    def shuffle(self):
        random.shuffle(self.deck)
# -> Player(Deck): Cards, Name, Money, Bet <-
class Player(Deck):
    # Player has name, money, and an empty list to hold cards (hand)
    def __init__ (self, name):
        self.hand = []
        self.name = name
        self.money = 500
    # __str__() method to display string representation of each card in player's hand
    def __str__(self):
        # Calling string on each card in player's hand
        return ' '.join([str(card) for card in self.hand])
    # get_name() function to display name of player
    def get_name(self):
        return self.name()
    # check_money() function to display money of player
    def check_money(self):
        return f"Balance: ${self.money:.2f}"
    # bet_money() function for player to bet money
    def bet_money(self):
        # Minimum bet set to $100, Maximum bet set to self.money
        for check in range(100, {self.money}):
            check = input(f"""How much would you like to bet?
Minimum Bet: $100.00
Maximum Bet(Balance): ${self.money:.2f}
""").strip()
            if check in range(100, {self.money}):
                # Converting bet input to an interger
                self.bet = int(check)
                # Subtracting bet from player's money stash
                self.money -= self.bet
                return f"""Bet Amount: ${self.bet:.2f}
Balance: ${self.money:.2f}"""
            # If input is outside of range(100, {self.money})
            else:
                check = input(f"""Balance: ${self.money:.2f}
Please enter a valid bet: """).strip()
    # win_money() function to give money to player if they win
    def win_money(self):
        # Casino payout is 1.5x player's bet
        won_bet = self.bet * 1.5
        # Adding winnings to player's money stash
        self.money += won_bet
        return f"Outstanding move! You're new balance is: ${self.money}"
    # deal_card() function to deal card to player
    def deal_card(self, card):
        # pop_card function used to take card from deck
        Deck.pop_card()
        # Adding card to player hand
        self.hand.append(card)
    # check_card() function to calculate total of self.hand
    def check_cards(self, hand):
        # Card total starts at 0
        card_total = 0
        # Place to keep count of our ace's valued at 11
        ace_11 = 0
        for card in hand:
            # For cards with values already given ('2', '3', '4'...)
            if card in range(11):
                card_total += card
            # For face or monarchy cards who's value is 10
            elif card in ['J', 'Q', 'K']:
                card_total += 10
            # For ace who's value is 11
            else:
                card_total += 11
                ace_11 += 1
        # If hand is bust (over 21 due to the value of ace being 11)...
        while ace_11 and card_total > 21:
            # ...then we switch the ace to a value of 1
            card_total -= 10
            ace_11 -= 1
        # Returning card total after calculations
        return card_total()
    def player_cards(self):
        return self.hand()
# -> Dealer(Deck): Cards, Hand <-        
class Dealer(Deck):
    # Dealer has name and an empty list to hold cards (hand)
    def __init__ (self, Casino_Dealer):
        self.hand = []
        self.name = Casino_Dealer
    # __str__() method to display string representation of each card in dealer's hand
    def __str__(self):
        # Calling string on each card in dealer's hand
        return ' '.join([str(card) for card in self.hand])
    # deal_card() function to deal card to dealer
    def deal_card(self, card):
        # pop_card function used to take card from deck
        Deck.pop_card()
        # Adding card to dealer hand 
        self.hand.append(card)
    # check_card() function to calculate total of self.hand
    def check_cards(self, hand):
        # Card total starts at 0
        card_total = 0
        # Place to keep count of our ace's valued at 11
        ace_11 = 0
        for card in hand:
            # For cards with values already given ('2', '3', '4'...)
            if card in range(11):
                card_total += card
            # For face or monarchy cards who's value is 10
            elif card in ['J', 'Q', 'K']:
                card_total += 10
            # For ace who's value is 11
            else:
                card_total += 11
                ace_11 += 1
        # If hand is bust (over 21 due to the value of ace being 11)...
        while ace_11 and card_total > 21:
            # ...then we switch the ace to a value of 1
            card_total -= 10
            ace_11 -= 1
        # Returning card total after calculations
        return card_total()
    # Dealer's first card is FACE UP, second card is FACE DOWN
    def dealer_cards(self):
        # When dealer hand is 2 cards, only the first card is revealed
        if len (self.hand) == 2:
            return self.hand(0)
        # When dealer hand is larger than 2 cards, all cards are revealed
        elif len(self.hand) > 2:
            return self.hand()
# -> Game: Menu, Rules, 
class Game:
    # For nav_menu() -> Quit
    playing = True
    while playing:
        def __init__(self):
            # New instance of Deck() for Game deck
            deck = Deck()
            # List for player names
            players = []
        def nav_menu(self):
            # List of options for user to select from
            print("""♣♦♥♠♣♦♥♠♣♦♥♠ Jeremy's Black Jack ♣♦♥♠ Main Menu ♣♦♥♠♣♦♥♠♣♦♥♠

To continue, select a number from the list of options below:

1. Play - New Game of Black Jack
2. View - Black Jack Rules
3. Quit - WARNING!!! Ends the current game!!!
""")
            print()
            option = input("Please select your option: ").strip()
            # Options to call functions created above
            if option == '1':
                Game.seat_player()
            elif option == '2':
                print("""
♣♦ OBJECTIVE OF THE GAME ♥♠
Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.

♣♦ CARD VALUES AND SCORING ♥♠
It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.

♣♦ BETTING ♥♠
Before the deal begins, each player places a bet, in chips, in front of them in the designated area.
Minimum and maximum limits are established on the betting, and the general limits are from $2 to $500.

♣♦ THE SHUFFLE ♥♠
The dealer thoroughly shuffles portions of the pack until all the cards have been mixed and combined.

♣♦ THE DEAL ♥♠
The dealer receives one card face up and one card face down. Each player, receives two cards face up.

♣♦ THE PLAY ♥♠
The player goes first and must decide whether to "Stand" (not ask for another card).
Or "Hit" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly).
Thus, a player may stand on the two cards originally dealt to them.
Or they may ask the dealer for additional cards, one at a time...
...until deciding to stand on the total (if it is 21 or under), or goes "bust" (if it is over 21).
In the latter case, the player loses and the dealer collects the bet wagered.
The dealer then turns to the next player to their left and serves them in the same manner.

♣♦ THE DEALER ♥♠
When the dealer has served every player, the dealers face-down card is turned up.
If the total is 17 or more, it must stand. If the total is 16 or under, they must take a card.
The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.
If the dealer has an ace, and counting it as 11 would bring the total to 17 or more...
...(but not over 21), the dealer must count the ace as 11 and stand.
The dealer's decisions are automatic on all plays, whereas the player can always take one or more cards.

♣♦ SIGNALING INTENTIONS ♥♠
When a player's turn comes, they can "Hit" or can get another card.
Alternatively the player can decide to "Stand" or NOT get another card.

♣♦ BASIC STRATEGY ♥♠
Winning tactics in Blackjack require that the player play each hand in the optimum way.
Such strategy always takes into account what the dealer's upcard is.
When the dealer's upcard is a good one, a 7, 8, 9, 10-card, or ace for example.
The player should not stop drawing until a total of 17 or more is reached.
When the dealer's upcard is a poor one, 4, 5, or 6.
The player should stop drawing as soon as he gets a total of 12 or higher.
The strategy here is never to take a card if there is any chance of going bust.
""")
            elif option == '3':
                playing = False
            else:
                option = input("""We're sorry, we did not recognize that option.

Please select a number from the list of options:

1. Play - New Game of Black Jack
2. View - Black Jack Rules
3. Quit - WARNING!!! Ends the current game!!!
""").strip()
        # seat_player() function to choose number of players in a new game
        def seat_player():
            #clear_output()
            chair = input("""Up to 6 players on each table!
Enter number of players: """).strip()
            if chair == '1':
                print(f"1 chair has been added to the table! ")
            elif chair == '2':
                print(f"2 chairs have been added to the table! ")
            elif chair == '3':
                print(f"3 chairs have been added to the table! ")
            elif chair == '4':
                print(f"4 chairs have been added to the table! ")
            elif chair == '5':
                print(f"5 chairs have been added to the table! ")
            elif chair == '6':
                print(f"6 chairs have been added to the table! ")
            else:
                chair = input("""Please enter a valid number of players.
Enter: 1, 2, 3, 4, 5, or 6 """).strip()
            # Converting chair input to interger
            p = int(chair)
            # Adding player name based on interger
            for name in range(p):
                name = input("Enter player name: ").title()
                # Adding player name to players list
                if len(name) >= 1:
                    Game.players.append(Player({name}))
                else:
                    name = input("Please enter a valid player name: ").title()
        def play_game():
            # Dealing 2 cards to dealer and each player
            for c in range(2):
                Player.deal_card
                Dealer.deal_card
            # For player to Stay or Hit
            player_move = True
            # For dealer Stay or Hit
            dealer_move = True
            while player_move or dealer_move:
                # First card of Dealer is FACE UP second card is FACE DOWN
                print(f"Dealer's cards are {Dealer.dealer_cards} and ??? ")
                # Player's name, card, and card total are given
                print(f"{Player.get_name}'s cards: {Player.player_cards}Card Total: {Player.check_cards} ")
                if player_move:
                    # Allowing players to either Stay or Hit, Forcing dealer to hit when below 17
                    player_bet = True
                    while player_bet:
                        pass
                        #Player.bet_money()
                        # List of in-game options for user to selection from
                        move = input("""To continue, select a number from the list of options below:

1. Stay - Do NOT take another card / Pass Move
2. Hit - TAKE another card / Add (1) card to hand!
3. Name - Show your player name
4. Money - Shows your current balance
5. Cards - Shows your current cards in hand
6. Card Total - Calculate the total for cards in hand
7. Quit - WARNING!!! Ends the current game!!!
""")
                        # Dealer is fored to STAY if hand is > 16
                        if Dealer.check_cards > 16:
                            dealer_move = False
                        # If dealer hand is not > 16 then dealer is forced to HIT
                        else:
                            # Limited to 1 card added at a given time
                            for c in range(1):
                                Dealer.deal_card
                        # Player Stay's, breaks move loop
                        if move == '1':
                            player_move = False
                        elif move == '2':
                            # Limited to 1 card added at a given time
                            for c in range(1):
                                Player.deal_card
                        # Options to call functions created above
                        elif move == '3':
                            Player.get_name()
                        elif move == '4':
                            Player.check_money()
                        elif move == '5':
                            Player.player_cards()
                        elif move == '6':
                            Player.check_cards()
                        # Player quit's current game session, breaks play loop
                        elif move == '7':
                            break
                        else:
                            move = input("""We're sorry, we did not recognize that option.

Please select a number from the list of options:

1. Stay - Do NOT take another card / Pass Move
2. Hit - TAKE another card / Add (1) card to hand!
3. Name - Show your player name
4. Money - Shows your current balance
5. Cards - Shows your current cards in hand
6. Card Total - Calculate the total for cards in hand
7. Quit - WARNING!!! Ends the current game!!!
""")
                        # If player's hand is >= 21, breaks move loop
                        if Player.check_cards >= 21:
                            break
                        # If dealers's hand is >= 21, breaks move loop
                        elif Dealer.check_cards >= 21:
                            break
                    # If player's hand is == 21
                    if Player.check_cards == 21:
                        print(f"Congradulations {Player.get_name}, you have Black Jack for a total of 21! Woohoo! ")
                    # If dealer's hand is == 21
                    elif Dealer.check_cards == 21:
                        print("The dealer has Black Jack for a total of 21! ")
                    # If player's hand is > 21
                    elif Player.check_cards > 21:
                        print(f"{Player.get_name}'s card total: {Player.check_cards}")
                        print(f"You bust!")
                    # If dealer's hand is > 21
                    elif Dealer.check_cards > 21:
                        print(f"Dealers card total: {Dealer.check_cards}| {Player.get_name}'s card total: {Player.check_cards} ")
                        print("Dealer bust!")
                    # Calculating winner, by checking whoever is closest to 21(Player wins if they are closer than player to 21)
                    elif 21 - Player.check_cards < 21 - Dealer.check_cards:
                        print(f"Dealers card total: {Dealer.check_cards}| {Player.get_name}'s card total: {Player.check_cards} ")
                        print(f"{Player.get_name} Wins! ")
                        print()
                        Player.win_money()
                        print()
                        Player.check_money()
                        break
                    # Dealer wins if they are closer than player to 21
                    elif 21 - Dealer.check_cards < 21 - Player.check_cards:
                        print(f"Dealers card total: {Dealer.check_cards}| {Player.get_name}'s card total: {Player.check_cards} ")
                        print("Dealer Wins! ")
                        print()
                        Player.check_money()
                        break
                    # Asking player if they would like to play another round
                    new_round = input("""Would you like to play another round?

To continue, select a number from the list of options below: 

1. Yes - Play another round
2. Quit - WARNING!!! Ends the current game!!!
""")
                    if new_round == '1':
                        playing = True
                    elif new_round == '2':
                        print("Thank you for playing! We hope to see you soon! ")
                        break
# WHY DOES GAME NOT RUN!?!?!!? D;
Game()