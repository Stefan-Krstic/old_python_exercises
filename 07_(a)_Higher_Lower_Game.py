from 07_(b)_game_data import logo, vs, data
import random
import os

game_over = False

score = 0
r1 = random.choice(data)
r2 = random.choice(data)
print(logo)
print(f"Compare A: {r1['name']}, a {r1['description']}, from {r1['country']}. With numb: {r1['follower_count']}    ")
print(vs)
print(f"Against B: {r2['name']}, a {r2['description']}, from {r2['country']}. With numb: {r2['follower_count']}    ")

while game_over == False: 
  a1 = r1['follower_count']
  b2 = r2['follower_count']

  pick = input("Who has more followers? Type 'A' or 'B':  ").lower()
  
  if pick == 'a':
    if a1 > b2:
      score += 1
      r1 = r1
      r2 = random.choice(data)
      os.system('cls' if os.name == 'nt' else 'clear')
      print(logo)
      print(f"You're right! Current score: {score}")
      print(f"Compare A: {r1['name']}, a {r1['description']}, from {r1['country']}. With numb: {r1['follower_count']}    ")
      print(vs)
      print(f"Against B: {r2['name']}, a {r2['description']}, from {r2['country']}. With numb: {r2['follower_count']}    ")
      
    elif a1 <= b2:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True
      
  elif pick == 'b':
    if a1 < b2:
      score += 1
      r1 = r2
      r2 = random.choice(data)
      os.system('cls' if os.name == 'nt' else 'clear')
      print(logo)
      print(f"You're right! Current score: {score}")
      print(f"Compare A: {r1['name']}, a {r1['description']}, from {r1['country']}. With numb: {r1['follower_count']}    ")
      print(vs)
      print(f"Against B: {r2['name']}, a {r2['description']}, from {r2['country']}. With numb: {r2['follower_count']}    ")
    elif a1 >= b2:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True
  else:
    print("Wrong input!")
