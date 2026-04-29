
secret = 7

while True:
    guess = int(input("Guess number (1-10): "))

    if guess == secret:
        print("You Win 🎉")
        break
    else:
        print("Try Again")