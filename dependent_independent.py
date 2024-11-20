import random

def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def draw_ace_twice():
    deck = list(range(1, 53))  # Represent cards from 1 to 52
    first_ace = None
    second_ace = None

    # Draw the first ace
    while deck:
        card = draw_card(deck)
        if card % 13 == 1:  # Ace is represented by cards 1, 14, 27, 40
            first_ace = card
            print(f"First ace drawn: {first_ace}")
            break

    # Draw the second ace
    while deck:
        card = draw_card(deck)
        if card % 13 == 1:
            second_ace = card
            print(f"Second ace drawn: {second_ace}")
            break

    if not first_ace or not second_ace:
        print("Could not draw two aces.")

# Simulate drawing two aces
draw_ace_twice()