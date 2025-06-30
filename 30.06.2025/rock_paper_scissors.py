import random

choices = ['rock', 'paper', 'scissors']
user = input("Rock, Paper, or Scissors? ").lower()
computer = random.choice(choices)
print(f"Computer chose {computer}")
if user == computer:
    print("Tie!")
elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("Computer wins!")