import random

def create_deck():
    card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    card_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck_cards = [(suit, value) for suit in card_suits for value in card_values]
    random.shuffle(deck_cards)
    return deck_cards

def draw_card(deck_cards):
    return deck_cards.pop()

deck = create_deck()
card = draw_card(deck)
print(card)