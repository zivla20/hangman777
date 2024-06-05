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
      for idx, letter in enumerate(self.word):
        if guess == letter:
          self.word_guessed[idx] = guess
      self.num_letters -= 1
    else:
      print(f"Sorry, {guess} is not in the word.")
      self.num_lives -= 1
      print(f"You have {self.num_lives} lives left.")

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

def play_game(word_list):
  num_lives = 5
  game = Hangman(word_list, num_lives)
  while True:
    if game.num_lives == 0:
      print("You lost!")
      break
    elif game.num_letters > 0:
      game.ask_for_input()
    else:
      print("Congratulations. You won the game!")
      break
      
word_list = ['apple', 'banana', 'cherry']
play_game(word_list)








