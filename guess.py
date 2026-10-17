import random

num = random.randint(1, 100)
tries = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    tries += 1

    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print(f"Congratulations! You got it in {tries} tries!")
        break
