# Project 2: Security Gate Bouncer
# This script demonstrates If/Else logic and integer math.

# 1. Collect user data
name = input("What is your name? ")
age = int(input("What is your age? "))

# 2. Check if the user meets the age requirement (21)
if age >= 21:
  print(f"Welcome in, {name}!")
else: 
  # Calculate the difference if they are too young
  years_to_adult = 21 - age
  print(f"Sorry {name}, come back in {years_to_adult} years.")
