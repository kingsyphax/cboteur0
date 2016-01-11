#!/usr/bin/env python3

import sys
import os
import random
import time

NUM_SABOTEURS = {3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4}
GOALS = [] #COMPLETE

def main():
    # GET NUMBER OF PLAYERS
    if len(sys.argv) > 1:
        num_players = int(sys.argv[-1])
        current_player = 1

        print("There are %d players" % num_players)
    else:
        print("Please provide a number of players")
        return

    # SET UP PLAYERS AND GAME ENVIRONMENT
    goal = [] #random 3 from goals
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

    # TELL WHO IS DA SABOTEUR and draw the cards
    for player in players:
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        input("If you are player %d, press Enter" % player)
        if player in saboteurs:
            print("You are a SABOTEUR")
        else:
            print("You are a MINER")
        player_conditions[player] = []
        player_hand = []
        while len(player_hand) < 5:
            player_hand.append(deck.draw())
        player_cards[player] = player_hand

    # DO GAME
    while True: # game loop
        print("Current player: Player %d" % current_player)
        print(player_cards[player])

        pass


if __name__ == "__main__":
    main()
