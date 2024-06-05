import random

class Hangman:

  def __init__(self, word_list, num_lives = 5):
    self.num_lives = int(num_lives)
    self.word_list = word_list
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.list_of_guesses = []
    
