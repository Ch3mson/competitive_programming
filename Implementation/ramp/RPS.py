"""
Given a string representing results of two-player rock paper scissors game, the first letter means the number of game rounds, the second and third mean shapes which the players form in the first round, the pattern keeps going for each round.

For example, 5RPSS... means 5 rounds, in the first round, Player 1 forms rock and Player 2 forms paper, and a player who wins 3 rounds wins.

Find who is the winner in such a string.
"""

# constraints of how many rounds? -> multiple digits 
# assume that the string provided is valid (no mismatch between number of rounds and the rounds presneted)
# case sensitivity? don't need to handle that 
# are ties possible? or only 1 winner?

# 1. process teh string -> iterate through the string until we reach a non-digit character (c.isdigit()) -> set this to the number of rounds and set the game string to a separate data member 
# 2. iterate through each "round" (i, i + 1). determine the winner of that round + acccumulate points for each player 
#    at the end of the rounds, return the result depending on the points of that player 
#    we can also pre-emptively return the winner if the number of wins is greater than half (rounded down) of the total number of rounds 

# cases
# player 1 wins 
# player 2 wins 
# ties:
#   round ties + even number of wins 
#   all round ties (i.e. r vs r)
#   even number of wins  

from enum import Enum

import unittest

class RPSResult(str, Enum):
	P1 = "player 1"
	P2 = "player 2"
	TIE = "tie"

class RPSMove(str, Enum):
	R = "R"
	P = "P"
	S = "S"

class RPSGame:
	def __init__(self, game: str):
		rounds = ""

		for c in game:
			if not c.isdigit():
				break

			rounds += c
		
		self.rounds = int(rounds)
		self.games = game[len(rounds):]

		self.p1_wins = 0
		self.p2_wins = 0
	
	def determine_round(self, p1: str, p2: str):
		if p1 == p2:
			return RPSResult.TIE
	
		if (
			p1 == RPSMove.R.value and p2 == RPSMove.S.value or 
			p1 == RPSMove.S.value and p2 == RPSMove.P.value or 
			p1 == RPSMove.P.value and p2 == RPSMove.R.value
		):
			self.p1_wins += 1
			return RPSResult.P1 if self.p1_wins > self.rounds // 2 else RPSResult.TIE
		
		self.p2_wins += 1
		return RPSResult.P2 if self.p2_wins > self.rounds // 2 else RPSResult.TIE
	
	def determine_winner(self):
		for i in range(0, len(self.games) - 1, 2):
			winner = self.determine_round(self.games[i], self.games[i+1])

			if winner in {RPSResult.P1, RPSResult.P2}:
				return winner
		
		return RPSResult.TIE
			
class TestRPSGame(unittest.TestCase):
	def test_p1_wins(self):
		self.app = RPSGame("5RSPRSPPSSS")
		assert self.app.determine_winner() == RPSResult.P1
	
	def test_p2_wins(self):
		self.app = RPSGame("11SRRPPSRSPRSPPPSSSRRPPS")
		assert self.app.determine_winner() == RPSResult.P2
	
	def test_all_ties(self):
		self.app = RPSGame("3RRSSPP")
		assert self.app.determine_winner() == RPSResult.TIE
	
	def test_tie_from_all_wins(self):
		self.app = RPSGame("4RSSRPSSP")
		assert self.app.determine_winner() == RPSResult.TIE

	def test_tie_from_wins_and_ties(self):
		self.app = RPSGame("6RSSRPSSPRRSS")
		assert self.app.determine_winner() == RPSResult.TIE

if __name__ == "__main__":
	unittest.main()
