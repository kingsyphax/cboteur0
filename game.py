#!/usr/bin/env python3

import sys
import os
import random
import time
from deck import Deck

NUM_SABOTEURS = {3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4}
GOALS = [] #COMPLETE

def main():
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

        print("Your cards: %s" % ", ".join(player_cards[current_player]))

        time.sleep(1)
        input("Press Enter to continue")
        current_player = current_player % num_players + 1


if __name__ == "__main__":
    main()
