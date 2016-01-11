import random

class Deck:

    DESCRIPTIONS = {"Read Spec" : "Peeks at a goal to check if correct or not",\
        "Add Code" : "Adds a line of code",\
        "Add Code - Assignment or Initialization" : "Add an Assignment or Initialization",\
        "Add Code - Arithmetic or other Basic Functions" : "Add Arithmetic Function or another Function Call",\
        "Add Code - Print or Return" : "Add a Print or Return Statement",\
        "Add Code - Conditional or Loop" : "Add an If, While, or For Statement along with its logic",\
        "Add Code - Anything" : "Add any line of code",\
        "Modify Lines" : "Modifies code",\
        "Modify Lines - Change Constants" : "Change constants on any lines",\
        "Modify Lines - Change Variables" : "Modify a variable name to another one",\
        "Modify Lines - Change Functions" : "Change a function call or an arithmetic operator",\
        "Modify Line - Change Line" : "Modify any line",\
        "Nuke" : "Deletes up to 3 lines of code.",\
        "Dead Battery" : "Traps a player",\
        "Disconnected WiFi" : "Traps a player",\
        "Stack Overflow Down" : "Everyone has a 1/2 chance of skipping their turn after playing card",\
        "Charger" : "Removes a Dead Battery trap",\
        "Internet Cafe" : "Removes a Disconnected Wifi trap",\
        "Go to Soda" : "Removes a Dead Battery and a Disconnected Wifi trap",\
        "Code Guide" : "Makes a single player immune to Stack Overflow Down effect",\
        "Stack Overflow Restored" : "Can not be skipped. Removes all effects of ongoing Stack Overflow Down.",\
        "Run" : "Runs the code. After 3 run cards are played total, the game ends and winner is decided."}

    def __init__(self):
        """ 
        List of cards and descriptions for Deck:

        Read Spec               - Peeks at a goal to check if correct or not
        (Rethink Plan           - Changes 2 of the 3 goals to different random ones.)
        Add Line                - Adds a line of code (or n characters)
        Modify Lines            - Modifies code (or < n characters)
        Nuke                    - Deletes up to 3 lines of code.
        Dead Battery            - Traps a player
        Disconnected WiFi       - Traps a player
        Stack Overflow Down     - Traps a player (special). Everyone else has a 1/2 chance of skipping their turn after playing card.
        Charger                 - Removes a Dead Battery trap
        Internet Cafe           - Removes a Disconnected Wifi trap
        Go to Soda              - Removes a Dead Battery and a Disconnected Wifi trap 
        Code Guide              - Makes a single player immune to Stack Overflow Down effect
        Stack Overflow Restored - Can not be skipped. Removes all effects of ongoing Stack Overflow Down.
        (Compile/Run)           - Runs the code. After 3? run cards are played total, the game ends and winner is decided.
        Currently 100 cards total
        """

        self.cards = ["Read Spec"] * 7 \
        + ["Add Code - Assignment or Initialization"] * 5 \
        + ["Add Code - Arithmetic or other Basic Functions"] * 5 \
        + ["Add Code - Print or Return"] * 5 \
        + ["Add Code - Conditional or Loop"] * 5 \
        + ["Add Code - Anything"] * 4 \
        + ["Modify Lines - Change Constants"] * 4 \
        + ["Modify Lines - Change Variables"] * 4 \
        + ["Modify Lines - Change Functions"] * 4 \
        + ["Modify Line - Change Line"] * 4 \
        + ["Nuke"] * 5 \
        + ["Dead Battery"] * 5 \
        + ["Disconnected WiFi"] * 5 \
        + ["Stack Overflow Down"] * 3 \
        + ["Charger"] * 5 \
        + ["Internet Cafe"] * 5 \
        + ["Go to Soda"] * 5 \
        + ["Code Guide"] * 5 \
        + ["Stack Overflow Restored"] * 3 \
        + ["Run Code"] * 12

        self.discarded = []

        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop()
        if len(self.cards) == 0:
            self.cards = self.discarded
            self.discarded = []
            random.shuffle(self.cards)
        return card

    def discard(self, card):
        self.discarded += list(card)

    def view_discard(self):
        return self.discarded

    def info(self, card):
        return Deck.DESCRIPTIONS[card]

        





