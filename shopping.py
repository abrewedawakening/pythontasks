pocket_money = 100
print("You Have $100 For Your Pocket Money.")
while True:
    spend = float(input("How much would you like to spend: $ "))
    pocket_money -= spend
    confirm = input("Would you like to keep shopping? You have ${} Left ".format(pocket_money))
    if confirm == "yes" and pocket_money > 0:
        print("Ok")
    else:
        break
