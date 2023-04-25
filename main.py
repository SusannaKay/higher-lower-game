from art import logo, vs
import random
from game_data import data
import replit

a = {}
b = {}
score = 0
game_over = False

def check_answer(a,b, score):
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  if answer == "a": 
    if a.get("follower_count") > b.get("follower_count"):
      score += 1
      replit.clear()
      print(logo)
      print(f"You're right! Current Score: {score}")
      return 1
    else: 
      replit.clear()
      print(logo)
      print(f"Sorry, that's wrong! Final score: {score}")
      return 0
  elif answer == "b":
    if b.get("follower_count") > a.get("follower_count"):
      score += 1
      replit.clear()
      print(logo)
      print (f"You're right! Current Score: {score}")
      
      return 2
    else: 
      replit.clear()
      print(logo)
      print (f"Sorry, that's wrong! Final score: {score}")
      return 0


print(logo)
a = random.choice(data)
  
while game_over == False:
    
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
  b = random.choice(data)
  if b == a:
    b = random.choice(data)
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
  x = check_answer(a,b,score)
  
  if x == 0:
      game_over = True
  elif x == 1:
      score += 1
    
  elif x == 2:
      score += 1
      a = b
      b = {}
