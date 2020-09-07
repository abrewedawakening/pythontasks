while True:
    answer = input("True Or False? Sharks are mammals. ").strip().lower()
    if answer == "true":
        print("Correct!")
        break
    elif answer == "false":
        print("Sorry, You Are Incorrect!")
        break
    else:
        print("Please Enter a valid answer!")
