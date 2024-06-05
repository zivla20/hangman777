import random

class Hangman:

  def __init__(self, word_list, num_lives = 5):
    self.num_lives = int(num_lives)
    self.word_list = word_list
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.list_of_guesses = []
    
  def check_guess(self, guess):
    guess = guess.lower()
    if guess in self.word:
      print(f"Good guess! {guess} is in the word.")
      return True
    else:
      print("Sorry, {guess} is not in the word. Try again.")
      return False

  def ask_for_input(self):
  #This function checks if the input is valid. 
    while True:
      guess = input("Please enter a single character: ")
      if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please enter a single aphabetical character.")
      elif guess in self.list_of_guesses:
        print("You already tried that letter!")
      else:
        self.check_guess(guess)
        self.list_of_guesses.append(guess)
        break

word_list = ['apple', 'banana', 'cherry']
game = Hangman(word_list)
game.ask_for_input()








