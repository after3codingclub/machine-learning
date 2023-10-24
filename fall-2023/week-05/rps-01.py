import random

arr=['scissors','rock','paper']

p1 = input("enter rock, paper, or scissors")
p2 = random.choice(arr)

if p1 == "rock" and p2 == "scissors":
  print("rock vs scissors "+ " p1 wins")
elif p1 == "paper" and p2 == "scissors":
  print("paper vs scissors "+" p2 wins")
elif p1 == "scissors" and p2 == "scissors":
  print("scissors vs scissors "+ "tie")
elif p1 == "rock" and p2 == "paper":
  print("rock vs paper "+" p2 wins")
elif p1 == "paper" and p2 == "paper":
  print("paper vs paper "+" tie")
elif p1 == "scissors" and p2 == "paper":
  print("scissors vs paper"+" p1 wins")
elif p1 == "rock" and p2 == " rock":
  print("rock vs rock "+" tie")
elif p1 == "paper" and p2 == " rock":
  print("paper vs rock "+" p1 wins")
elif p1 == "scissors" and p2 == "rock":
  print("scissors vs rock "+" p2 wins")
else:
  print("invalid input")
