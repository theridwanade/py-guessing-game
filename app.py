import random

def computer_guess(x = 10):
  number = random.randint(1, x)
  while True:
    guessed_number = int(input("Enter your guess: "))
    if number == guessed_number:
      print("You guessed right!")
      break
    elif guessed_number > number:
      print("You guessed to high")
    elif guessed_number < number:
      print("You guessed to low")
    else:
      print("Man are you even playing, yah wrong!")

def human_guess(x = 10):
  low = 1
  high = x
  feedback = ''

  while feedback != 'c':
    guess = random.randint(low, high)
    feedback = input(f"Is {guess} is too high (H), low (L), or correct (C). Enter the corret letter: ").lower()
    if feedback == "h":
      high = guess - 1
    elif feedback == "l":
      low = guess + 1

  print(f"Correct number {guess} is your secret number")




def main():
  mode = str(input("Enter game mode C(computer) / H(human): ")).lower()
  if(mode == "c"):
    computer_guess()
  elif(mode == "h"):
    human_guess()
  else:
    print("choose between computer mode and human mode")
    main()


main()