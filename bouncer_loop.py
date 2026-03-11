active = True

while active == True:
  name = input("What's your name? (or type 'quit'): ")

if name == "quit":
  active = False
  print("Goodbye")
else:
  age = int(input("What's your age?"))
  if age >= 21:
      print(f"Welcome to the club, {name}!"
  else:
      print(f"Sorry {name}, you are too young.")
