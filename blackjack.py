#!/usr/bin/env python
import numpy as np
import random

from collections import Counter
import operator

"""
A Simulation to determine the probabilities of if you should hit, stand, double down, split, and insurance.

GOAL:

The goal of BlackJack is to have a total of 21 with any number of cards.


---- Rules of BlackJack ----

K,Q,J each are 10
2-10 are the value of their number.
Aces can either be 11 or 1.

Blackjack is 21 with an Ace and a 10 valued card. 3:2 payout

Hit - You recieve more cards till satisfied with the hand.
Stand - You are content with your hand.
Double Down - Allowed to after two cards are dealth and he will get one more card before going to stand but allows to increase wage.

Split - Only if the two cards have the same value you can split them as two seperate hands and recieve one card for each hand.

Surrender - Is offered when the dealer upcard is either an ace value or 10 value.
Push - When the dealer and the player has the same value. (No money is exchanged)
"""

def construct_deck(number_of_decks=1):

    """
    Creates a list of all of the possible values that are in a single deck.

    deck is an empty array.
    royals are the King, Queen and Jack which are appended into the deck.
    Ace is also appended later on depending on how many number of decks are provided to the function.

    A standard deck contains 52 cards which is how many elements deck will have if construct_deck is given 1 as an argument.

    If number_of_decks is given to be 2 than two decks will be in deck and so on.
    """

    deck = []
    royals = ["K", "Q", "J"]
    ace = "A"

    for i in range(0,4*number_of_decks):

        for i in range(2,11):
            deck.append(i)

        for royal in royals:
            deck.append(royal)

        deck.append(ace)

    return deck

def shuffle_deck(deck):

    """
    Shuffles the deck randomly. Producing a shuffled deck. Shuffle_deck requires a deck which can be constructed from the construct_deck function.
    """

    random.shuffle(deck)
    return deck

def count_hand(array):
    """
    Given an array counts up the total value of the hand.
    Fix up the count_hand function so that it can correctly determine when to
    treat an Ace as a 1 and when to treat it as a 11.
    """

    count = 0

    for i in array:
        if isinstance(i, int):
            count+=i

        else:
            if "K" == i:
                count+=10
            elif "Q" == i:
                count+=10
            elif "J" == i:
                count+=10
            else:
                if count+11 > 21:
                    count+=1
                else:
                    count+=11

    return count

def outcome_for_first_hand_value(iterations=100, number_of_decks=1, number_of_cards=2):

    counter = []

    for i in range(0, iterations):

        deck = construct_deck(number_of_decks)
        shuffled_deck = shuffle_deck(deck)

        count = count_hand(shuffled_deck[0:number_of_cards])
        counter.append(count)


    for key, value in reversed(sorted(dict(Counter(counter)).items(), key=operator.itemgetter(1))):  # It is now in order from highest probability to lowest.

        print(key, " => ", round((value/iterations)*100, 3), "%")

    return Counter(counter)



def main():

    # deck = construct_deck()
    # shuffled_deck = shuffle_deck(deck)
    # print(shuffled_deck)

    # count = count_hand(shuffled_deck[0:2])
    # print(count)

    print(outcome_for_first_hand_value(50000, 1, 1))

if __name__=="__main__":
    main()
