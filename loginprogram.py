ans = print("Hello, lets make you an account with Lev")
username_input = input("Please ener a username: ")
password_input = input("Please enter a password: ")
print("Thanks for making an account with Lev, Please login.")
count = 0
while count < 3:
    username_guess = input("Username: ")
    password_guess = input("Password: ")
    if username_guess == username_input and password_guess == password_input:
        print("Welcome")
        break
    else:
        print("Access Denied")
    count += 1

