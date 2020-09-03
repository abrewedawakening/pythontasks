while True:
    import random
    answer = random.randint(1,6)
    guess = int(input("Guess the number: "))
    if guess == answer:
        print("Correct!")
    else:
        print("Sorry, Wrong Answer")
