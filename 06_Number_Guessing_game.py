import random
  
lista = []
for i in range(1, 101):
  lista.append(i)
a = random.choice(lista)
c = int(input("Pick difficalty - for Normal type 1, for HARD type 2:  "))
d = 0
print(c)
print(d)

if c == 1:
  d += 10
elif c == 2:
  d += 5
else:
  d = 0
  print("Wrong! Enter 1 or 2 for difficalty: ")

print(f"You have {d} attempts remaining to guess the number.")
b = int(input("Guess number between 1 and 100: "))

for i in range(0, d):
  if b > a:
    b = int(input(f"Number {b} is higher than guessed, try with lower: "))
    d -= 1
    print(f"You have {d} attempts remaining to guess the number.")
  elif b < a:
    b = int(input(f"Number {b} is lower than guessed, try with higher: "))
    d -= 1
    print(f"You have {d} attempts remaining to guess the number.")
  elif b == a:
    print(f"YOU WON, good job! My guessed number was: {a}")
    break
  else:
    print("ERROR - wrong input!")
    break
