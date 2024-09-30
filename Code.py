#Number Guessing Game
import random
print("............................NUMBER GUESSING GAME............................")
def line():
  print("----------------------------------------------------------------------------")
def play_again():
  play=input("Do you want to play again? (Y/N): ").lower()
  if play=="n":
    print("Thanks for playing!")
    line()
  else:
    game()
def game():
  line()
  guess=int(input("Enter number of trials:"))
  low_limit=int(input("Enter the lower limit:"))
  up_limit=int(input("Enter the upper limit:"))
  line()
  try:
    num=random.randint(low_limit,up_limit)
    i=0
    while i<guess and low_limit<=up_limit:
      enter_number=int(input("Guess a number between {} and {}:".format(low_limit, up_limit)))
      if enter_number==num:
        print("Congratulations! You guessed the number")
        line()
        play_again()
      elif enter_number<num:
        print("Too low, try again!")
        line()
      else:
        print("Too high, try again!")
        line()
      i+=1
      if i==guess:
        print("No guesses left")
        print("Number is",num)
        line()
        play_again()
  except ValueError:
    print("Invalid Input. Please enter a valid range.")
    line()
    game()
game()
