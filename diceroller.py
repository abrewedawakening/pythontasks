print("Welcome To The Dice Roller!")
while True:
    print("Please press enter to roll the dice")
    user_confirm = input("Press Enter: ")
    if user_confirm == "":
        import random
        n = random.randint(1,6)
    print(n)



