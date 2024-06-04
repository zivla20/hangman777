condition = True 

while condition == True:
  guess = input("Please enter a single character: ")
  if len(guess) == 1 and guess.isalpha():
    condition == False
  else:
    print("Invalid letter. Please enter a single aphabetical character.")
