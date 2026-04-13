import random


def create_deck():
    """
    Creates and returns a deck of 52 cards

    Returns:
        deck: a list of all the cards in a standard deck 
    """
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append(f"{rank} of {suit}")
    random.shuffle(deck)  
    return deck


def deal_cards(deck, players):
    '''
    Deals 2 cards to each player and returns a list of player hands and the remaining deck

    Args:
        deck: the current deck of cards
        players: the number of players in the game

    Returns:
        player_hands: a list of lists, where each inner list represents a player's hand
        deck: the remaining deck after dealing
    '''

    player_hands = []
    for i in range(len(players)):
        hand = []
        hand.append(f"Player {i + 1}'s hand")
        for j in range(2):
            hand.append(deck.pop())
        player_hands.append(hand)
    return player_hands, deck


def deal_river(deck):
    '''
    Deals the river cards and returns a list of the river cards and the remaining deck
    Args:
    deck: the current deck of cards

    Returns:
    river_cards: a list of the river cards
    deck: the remaining deck after dealing the river cards
    '''
    river_cards = []
    for i in range(3):
        river_cards.append(deck.pop())
    return river_cards, deck


def add_river_card(deck, river_cards):
    '''
    Deals an additional river card and returns the updated list of river cards and the remaining deck
    Args:
    deck: the current deck of cards

    Returns:
    river_cards: the updated list of river cards with the new card added
    deck: the remaining deck after dealing the additional river card
    '''
    river_cards.append(deck.pop())
    return river_cards, deck





    
        