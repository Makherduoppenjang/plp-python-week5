secret_number = 12
attempts = 0
guessed_correctly = False

print("I'm thinking of a number between 1 and 20.")

while not guessed_correctly:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        guessed_correctly = True
        print(f"Congratulations! You got it in {attempts} tries!")
