# Class: CIST 2742 Python Programming I
# Term: Fall 2023
# Instructor: Chris Bishop
# Description: Solution to Final Exam
# Author: Ingrid Pimentel
#

import random

def main():

	#Set players names
	player1_name, player2_name = get_player_names()

	#Deck of cards
	deck = create_deck()

	#Remaining cards to draw
	remaining_cards = list(deck.keys())

	player1_wins = 0
	player2_wins = 0
	ties = 0
	round_number = 1

	#Loop for rounds
	while len(remaining_cards) >= 2:
		print(f"\n=== Round {round_number} ===")

		player1_hand = []
		player2_hand = []

		player1_value = 0
		player2_value = 0

		#Deal cards to each player
		while len(remaining_cards) >= 2 and player1_value <= 21 and player2_value <= 21:

			#Deal to player 1
			card1 = deal_one_card(remaining_cards)
			player1_hand.append(card1)
			player1_value = calculate_hand_value(player1_hand, deck)

			#Deal to player 2
			if len(remaining_cards) == 0:
				break
			card2 = deal_one_card(remaining_cards)
			player2_hand.append(card2)
			player2_value = calculate_hand_value(player2_hand, deck)

			#Show hands and value
			print(f"\n{player1_name} was dealt: {card1}")
			print(f"{player1_name} hand: ", player1_hand)
			print(f"{player1_name} value: ", player1_value)

			print(f"\n{player2_name} was dealt: {card2}")
			print(f"{player2_name} hand: ", player2_hand)
			print(f"{player2_name} value: ", player2_value)

			#Check busted
			if player1_value > 21 and player2_value >21:
				print("\nBoth players exced 21. No winner this round!")
				ties += 1
				break
			elif player1_value > 21:
				print(f"\n{player1_name} exceeded 21. {player2_name} wins this round!")
				player2_wins += 1
				break
			elif player2_value > 21:
				print(f"\n{player2_name} exceeded 21. {player1_name} wins this round!")
				player1_wins += 1
				break

		round_number += 1

		#If out of cards
		if player1_value <= 21 and player2_value <= 21 and len(remaining_cards) < 2:
			print("\nNot enough cards left to continue this round!")
			ties += 1
			break

	#Game over
	print("\n=== Game Over: No more cards in the deck ===")
	print(f"{player1_name} wins: ", player1_wins)
	print(f"{player2_name} wins:", player2_wins)
	print("Rounds with no winner: ", ties)

def get_player_names():
	p1 = input("Player 1: ").strip()
	if p1 == "":
		p1= "Player 1"

	p2 = input("Player 2: ").strip()
	if p2 == "":
		p2 = "Player 2"

	return p1, p2

#Create a dictionary 
def create_deck():
	deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}
	return deck

def deal_one_card(remaining_cards):
	card = random.choice(remaining_cards)
	remaining_cards.remove(card)
	return card

def calculate_hand_value(hand, deck):
	total = 0
	aces = 0

	for card in hand:
		if "Ace" in card:
			aces += 1
			total += 1
		else: 
			total += deck[card]

	for _ in range(aces):
		if total + 10 <= 21:
			total += 10

	return total

if __name__ == '__main__':
	main()