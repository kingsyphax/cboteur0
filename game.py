#!/usr/bin/env python3

import sys
import os
import random
import time
from deck import Deck

NUM_SABOTEURS = {3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4}
GOALS = [] #COMPLETE

def main():
    def play_card(player_number, card):
        if card == "Read Spec":
        elif card == "Add Code - Assignment or Initialization":
        elif card == "Add Code - Arithmetic or other Basic Functions":
        elif card == "Add Code - Print or Return":
        elif card == "Add Code - Conditional or Loop":
        elif card == "Add Code - Anything":
        elif card == "Modify Lines - Change Constants":
        elif card == "Modify Lines - Change Variables":
        elif card == "Modify Lines - Change Functions":
        elif card == "Modify Line - Change Line":
        elif card == "Nuke":
        elif card == "Dead Battery":
            target = input("Choose who to trap")
        elif card == "Disconnected WiFi":
            target = input("Choose who to trap")
        elif card == "Stack Overflow Down":
        elif card == "Charger":
            target = input("Choose who to free")
        elif card == "Internet Cafe":
            target = input("Choose who to free")
        elif card == "Go to Soda":
            target = input("Choose who to free")
        elif card == "Code Guide":
            target = input("Choose who to free")
        elif card == "Stack Overflow Restored":
        elif card == "Run":
        else:

    DEBUG = False

    # GET NUMBER OF PLAYERS
    if len(sys.argv) > 1:
        if sys.argv[-1] == "-t":
            DEBUG = True
        if DEBUG:
            num_players = int(sys.argv[-2])
        else:
            num_players = int(sys.argv[-1])
        current_player = 1

        print("There are %d players" % num_players)
    else:
        print("Please provide a number of players")
        return

    # SET UP PLAYERS AND GAME ENVIRONMENT
    goal = [] # random 3 from goals
    deck = Deck()
    players = list(range(1, num_players + 1))
    player_cards = {}
    player_conditions = {}

    num_saboteurs = NUM_SABOTEURS[num_players]
    role_cards = ["saboteur"] * num_saboteurs + ["miner"] * (num_players - num_saboteurs + 1)
    random.shuffle(role_cards)

    saboteurs = []
    for player in players:
        role = role_cards.pop()
        if role == "saboteur":
            saboteurs.append(player)

        player_conditions[player] = []
        player_hand = []
        while len(player_hand) < 5:
            player_hand.append(deck.draw())
        player_cards[player] = player_hand

    # TELL WHO IS DA SABOTEUR
    if not DEBUG:
        time.sleep(1)
        for player in players:
            os.system("clear")
            time.sleep(1)
            input("If you are player %d, press Enter" % player)
            if player in saboteurs:
                print("You are a SABOTEUR")
            else:
                print("You are a MINER")

            time.sleep(1)
            input("Press Enter to continue")


        os.system("clear")
        time.sleep(1)
        print("GAME STAAAART")
        time.sleep(3)

    # DO GAME
    while True: # game loop
        os.system("clear")
        time.sleep(1)
        input("If you are player %d, press Enter" % current_player)

        print("Your cards:")
        for index, card in enumerate(player_cards[current_player]):
            print("\t%d: %s" % (index + 1, card))

        time.sleep(1)

        thing_done = False
        while not thing_done:
            card_to_do = input("Select a card (name or number): ")

            while card_to_do not in player_cards[current_player] and int(card_to_do) not in range(1, len(player_cards[current_player]) + 1):
                card_to_do = input("Card not found. Select a card: ")

            if card_to_do in player_cards[current_player]:
                card_number = player_cards[current_player].index(card_to_do) + 1
            else:
                card_number = int(card_to_do)

            card_name = player_cards[current_player][card_number - 1]
            print("%s: %s" % (card_name, deck.info(card_name)))

            time.sleep(1)

            to_do = input("What would you like to do (play, discard, cancel)? ").lower()
            while to_do not in ("play", "discard", "cancel"):
                to_do = input("Not recognized. What would you like to do? ").lower()

            if to_do == "cancel":
                pass # do nothing; will loop back around to selecting another card
            else:
                thing_done = True
                deck.discard(card_name)
                player_cards[current_player].remove(card_name)
                player_cards[current_player].append(deck.draw())
                if to_do == "play":
                    play_card(current_player, card_name)


        time.sleep(1)
        input("Press Enter to continue")
        current_player = current_player % num_players + 1


if __name__ == "__main__":
    main()
