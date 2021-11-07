#!/usr/bin/env python3

from random import randint

# creating the deck of cards
suits = {
    0: 'Clubs',
    1: 'Diamonds',
    2: 'Hearts',
    3: 'Spades'
}

cards = {
    0: 'Ace',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Jack',
    11: 'Queen',
    12: 'King'
}

deckInHand = []

NUM_CARDS_IN_DECK = 52
currentNumCards = NUM_CARDS_IN_DECK


finishedDrawingCards = False
firstCardDrawn = False
exitOption = 'n'
finalDeckValue = 0
x = randint(0, 3)  # random integer 0 to 3 to pick suit
y = randint(0, 12)  # random integer 0 to 12 to pick card


def CalculateHandValue(valueToAdd):
    global finalDeckValue
    finalDeckValue += valueToAdd
    return finalDeckValue


def DrawCards(num_of_cards, list_dealt=[]):
    for z in range(num_of_cards):

        myCard = "{} of {}".format(cards[y], suits[x])
        CalculateHandValue(y)
        if myCard not in list_dealt:
            list_dealt.append(myCard)
        else:
            num_of_cards = num_of_cards - z
            return DrawCards(num_of_cards, list_dealt)

    return list_dealt


print("Welcome to the card party! \n")

firstCard = DrawCards(1, deckInHand)

i = 0

for x in firstCard:
    i += 1
    currentNumCards -= 1
    if i == len(firstCard):
        if not firstCardDrawn:
            firstCardDrawn = True
            print("Here is your first card: \n" + "{0}".format(str(x)))
            deckInHand.append(x)
            break
        else:
            print(str(x))

choice = input("Would you like another card? (y or n) ").lower()

while not finishedDrawingCards:
    if choice == 'y':
        cardDrawn = DrawCards(1, deckInHand)
        j = 0
        for x in cardDrawn:
            j += 1
            currentNumCards -= 1
            if j == len(cardDrawn):
                print(str(x))

    elif choice == exitOption:
        finishedDrawingCards = True
        print("Final hand value: {}".format(finalDeckValue))
        print(deckInHand)
        break



