#!/usr/bin/env python3


# P. johnson
# 10//2021
# Use dictionaries and lists to create a deck of cards (no Jokers!).
# Random cards are selected from the deck, stored in a hand (list),
# and the face value of the cards is accumulated.
# The hand and sum of the card values is displayed.

import random

# seed the random number generator
random.seed(42) #the meaning of life!

# useful constants
MAX_CARDS = 52
SUITS_PER_DECK = 4

# data structures for cards
# a suit is a dictionary containing cardname : cardvalue pairs
cards = {
    "Ace": 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5,
    "6" : 6, "7" : 7, "8" : 8, "9" : 9,
    "10" : 10, "Jack" : 10,
    "Queen" : 10, "King" : 10
}

# 4 dictionaries, one for each suit. Each dictionary contains
# a  "header" entry with a "suit_name" key and the name of that suit,
# followed by a "cards" key containing a cards_suit dictionary
cards_clubs = {
    "suit_name" : "clubs",
    "cards" : cards
}

cards_diamonds = {
    "suit_name" : "diamonds",
    "cards" : cards
}

cards_hearts = {
    "suit_name" : "hearts",
    "cards" : cards
}

cards_spades = {
    "suit_name" : "spades",
    "cards" : cards
}

# a list of 4 suits which comprise the entire deck
deck = [ cards_clubs, cards_diamonds, cards_hearts, cards_spades ]

# accumulate the hand value,
# store the cards in the hand, and
# keep track of cards already selected
hand_value = 0
hand = []
cardsDrawn = [-1] #no duplicates!
suit_index = 0
# seed play variable to enter while loop
play = "y"

card_found = False  # flag for the while loop
card_index = 1  # needs to match the random number card_to_find

suit_index = 0  # index each of the four suits in the deck


# welcome the user
print("Welcome to the card dealer!")
print("Here is your first card: ")

def main(play):
    # loop until they are done
    while (play == "y"):
        card_to_find = -1  # control variable to enter validation while loop


        # get a random card that hasn't been drawn before
        while card_to_find in cardsDrawn:
            card_to_find = random.randint(1, MAX_CARDS)  # randint not like range()!!

        cardsDrawn.append(card_to_find)  # keeps track of cards drawn

        pickACard(card_found)

        if len(hand) < MAX_CARDS:
            play = input("Would you like another card? (y or n) ")
        else:
            print("All cards should have been drawn.")
            play = "n"


def pickACard(card_found):
    while card_found == False and suit_index < SUITS_PER_DECK:

        # another way to do this is with a for loop, skipping the suit_index
        suit = deck[suit_index].get('cards')

        # iterate through each suit until desired card is found
        # use card_index as a counter to keep track of position in the deck
        for cards in suit:

            # if we found our card, print it, set flag, and break for loop
            if card_index == card_to_find:

                # get the card
                card = suit.get(cards)

                # flag the while loop that we are done
                card_found = True

                # modify accumulator
                hand_value += card

                # append hand info to hand list and show card to user
                card_str = f"{cards} of {deck[suit_index].get('suit_name')}"
                hand.append(card_str)
                print(card_str)
                break

            # else increment the card_index and get the next card
            else:
                card_index += 1

        # get next suit
        suit_index += 1

main(play)

print("final hand value =", hand_value)
print("final hand: ", hand)
