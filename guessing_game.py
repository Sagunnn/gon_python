secret_number= 5
guess_count=0
guess_limit=3

while guess_count < guess_limit:
    guess_number=int(input("Guess: "))
    if guess_number == secret_number:
        print("You Win!")
        break
    else:
        print("Your guess was wrong")
