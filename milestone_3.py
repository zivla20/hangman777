import random

word_list = ["raspberry", "mango", "pineapple", "blackberry", "grape"]
word = random.choice(word_list)

def ask_for_input():
#This function checks if the input is valid.
  condition = True 
  while condition == True:
    guess = input("Please enter a single character: ")
    if len(guess) == 1 and guess.isalpha():
      condition = False
    else:
      print("Invalid letter. Please enter a single aphabetical character.")
  
  return guess

def check_guess(guess):
  guess = guess.lower()
  if guess in word:
    print(f"Good guess! {guess} is in the word.")
    check_guess(guess)
  else:
    print("Sorry, {guess} is not in the word. Try again.")



