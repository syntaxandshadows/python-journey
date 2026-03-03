name = input("Whats your name? ")
movie = input("Whats the movies name? ")
age = int(input("How old are you? "))


if age < 13:
    price = 8
elif age <= 64:
    price = 12
else:
    price = 10


print(f"Ticket for {movie} confirmed. That will be ${price}. Enjoy!")
