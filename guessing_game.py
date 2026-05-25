secret_number = 67
guess = int(input("Guess the number: "))
if guess == secret_number:
    print("Congratulations!!! You guessed correctly.")
else:
    print("Wrong guess. Try again.")