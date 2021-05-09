import random
import pdb
# Global variables as a tuple and dictionary
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
# Create a card class which instantitates a new card whenever it is called
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

# instantiate a card from card class
two_hearts = Card(suits[0], ranks[0])
# print(two_hearts)
# print(suits[0])
# print(ranks[0])
# print(two_hearts.rank)
# print(two_hearts.suit)
# print(two_hearts.value)

# Create a deck class contain all the 52 cards present in one deck 
class Deck:
    def __init__(self):
        # this only happens once upon creation of a new deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Assume that the card class has already been defined
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # it is used to shuffle 52 cards of a deck
        # shuffle does not return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # remove one card from the list of 52 cards
        return self.all_cards.pop()

# instantiate a deck class
my_deck = Deck()
# print(len(my_deck.all_cards))
# print(my_deck.all_cards[0])
my_deck.shuffle()
# print(my_deck.all_cards[0])
my_card = my_deck.deal_one()
# print(my_card)

# Create a player class to create a player and play the game
class Player:
    def __init__(self, name):
        # grab the player name
        self.name = name
        # A new player has no card
        self.all_cards = []

    def remove_one(self):
        # remove one card from the list of 52 cards
        # imagine state 0 to remove from the top of the stack
        # imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# instantiate a player class
nilesh = Player('Nilesh')
# print(nilesh)
nilesh.add_cards(two_hearts)
# print(nilesh)
nilesh.add_cards([two_hearts,two_hearts,two_hearts])
# print(nilesh)

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()
# print(len(new_deck.all_cards)/2)
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# print(new_deck.all_cards)
# print(player_one.all_cards)
# print(player_two.all_cards)

# play the game
game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')
    # check to see if player is out of cards
    if len(player_one.all_cards) == 0:
        print('Player One out of cards! Game Over')
        print('PLAYER TWO WINS')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two out of cards! Game Over')
        print('PLAYER ONE WINS')
        game_on = False
        break

    # otherwise the game is still on
    # start a new round and reset the current cards on the table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        # check if player one top card is having higher value compared to player two top card
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # player 1 get both cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # No longeer at war, play next round
            at_war = False
        
        # check if player one top card is having lesser value compared to player two top card
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            # player 2 get both cards 
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No longer at war, play next round
            at_war = False

        # if both above are false, then war between two player card occurs
        else:
            print('At WAR!')
            # this condition occurs when the cards are equal
            # grab another card each and continue the current war
            # check to see if player has enough cards to play the war
            # check to see if player is out of cards
            if len(player_one.all_cards) < 5:
                print('Player One unable to play war! Game over at war!')
                print('PlAYER TWO WINS')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player Two unable to play war! Game over at war!')
                print('PLAYER ONE WINS')
                game_on = False
                break

            # other we're still in war. so add next card to play
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

# print(len(player_one.all_cards))
# print(len(player_two.all_cards))
# print(player_one_cards[-1])
# print(player_two_cards[-1])

