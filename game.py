#!/usr/bin/env python

import sys

NUM_SABOTEURS = {3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4}

def main():
    if len(sys.argv) > 1:
        num_players = int(sys.argv[-1])
        current_player = 1

        print("There are %d players" % num_players)
    else:
        print("Please provide a number of players")
        return


    while True: # game loop
        print("Current player: Player %d" % current_player)

        pass


if __name__ == "__main__":
    main()
