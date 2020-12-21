# Hangman Game
# OOP

# Import
import random

# Board
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Class
class Hangman:

	# Constructor
	def __init__(self, word):
		self.word = word
		self.guessed_letters = []
		self.missed_letters = []

	# Method to check letter
	def guess(self, letter):
		if letter in self.word and letter not in self.guessed_letters:
			self.guessed_letters.append(letter)
		else:
			self.missed_letters.append(letter)

	# Method to check if game is over
	def hangman_over(self):
		return len(self.missed_letters) == 6 or self.hangman_won()



	# Method to check if player won
	def hangman_won(self):
		if "_" not in self.hide_word():
			return True
		return False

	# Method that hides starting letters on board
	def hide_word(self):
		hidden = []
		for i in self.word:
			if i in self.guessed_letters:
				hidden.append(i)
			else:
				hidden.append('_')

		return hidden

	# Method to check game status and print board
	def print_game_status(self):
		print(board[len(self.missed_letters)])
		print(f"Word: {self.hide_word()}")
		print(f"Missed: {self.missed_letters}")


# Function to get a word from word bank
def rand_word():
	with open("words.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0, len(bank))].strip()


# Main function
def main():
	# Object class Hangman
	game = Hangman(rand_word())

	# While game's still running, prints status, ask for input, check input
	while not game.hangman_over():
		game.print_game_status()
		letter = input("\nEnter a letter: ")
		while not letter.strip().isalpha() or letter == "":
			print("You must enter one alphabetical character")
			letter = input("\nEnter a letter: ")
		game.guess(letter)

	# Checks game status
	game.print_game_status()

	# Prints message according to status
	if game.hangman_won():
		print('\nYou won!!')
	else:
		print('\nGame over! You lost.')
		print('The word is ' + game.word)


# Start
if __name__ == "__main__":
	main()
