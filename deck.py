import random.shuffle
class Deck:
	self.goals = [""]
	def __init__(self):
		""" 
		List of cards and descriptions for Deck:

		Read Spec - Peeks at a goal to check if correct or not
		(Rethink Plan - Changes 2 of the 3 goals to different random ones.)
		Add Line - Adds a line of code (or n characters)
		Modify Line - Modifies a line of code (or < n characters)
		Dead Battery - Traps a player
		Disconnected WiFi - Traps a player
		Stack Overflow Down - Traps a player (special). Everyone else has a 1/2 chance of skipping their turn after playing card.
		Charger - Removes a Dead Battery trap
		Internet Cafe - Removes a Disconnected Wifi trap
		Go to Soda - Removes a Dead Battery and a Disconnected Wifi trap 
		Code Guide - Makes a single player immune to Stack Overflow Down effect
		Stack Overflow Restored - Can not be skipped. Removes all effects of ongoing Stack Overflow Down.
		(Compile/Run) - Runs the code. After 3? run cards are played total, the game ends and winner is decided.

		"""
		self.cards = ["Read Spec"] * 5 \
		+ ["Add Line"] * 20 \
		+ ["Modify Line"] * 12 \
		+ ["Dead Battery"] * 5 \
		+ ["Disconnected WiFi"] * 5 \
		+ ["Stack Overflow Down"] * 3\
		+ ["Charger"] * 5 \
		+ ["Internet Cafe"] * 5 \
		+ ["Go to Soda"] * 5 \
		+ ["Code Guide"] * 5 \
		+ ["Stack Overflow Restored"] * 3 \
		+ ["Run Code"] * 10
		random.shuffle(self.cards)
		





