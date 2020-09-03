sport_hours = 0
print("Welcome to the weekly excercise calculator!")
monday =float(input("How many hours of excercise did you do on Monday: "))
sport_hours += monday
tuesday = float(input("How many hours of excercise did you do on Tuesday: "))
sport_hours += tuesday
wednesday = float(input("How many hours of excercise did you do on Wednesday: "))
sport_hours += wednesday
thursday = float(input("How many hours of excercise did you do on Thursday: "))
sport_hours += thursday
friday = float(input("How many hours of excercise did you do on Friday: "))
sport_hours += friday
saturday =float(input("How many hours of excercise did you do on Saturday: "))
sport_hours += saturday
sunday = float(input("How many hours of excercise did you do on Sunday: "))
sport_hours += sunday
if sport_hours < 10:
    print("You did not do enough excercise week!")
elif sport_hours >= 10 and sport_hours <= 25:
    print("You did enough excercise week!")
elif sport_hours >= 26 and sport_hours <= 168:
    print("You did a lot of excercise this week!")
else:
    print("That is impossible!")
