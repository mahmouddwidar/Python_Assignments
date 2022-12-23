#Assignment 3


age = int(input("Enter your Age: "))


months = age * 12
weeks = months * 4
days = weeks * 7 
hours = days * 24
mins = hours * 60
secs = mins * 60

if age > 10 and age < 100:

    print(f"Your Age In Months Is {months:,} Months")
    print(f"Your Age In Months Is {weeks:,} Weeks")
    print(f"Your Age In Months Is {days:,} Days")
    print(f"Your Age In Months Is {hours:,} Hours")
    print(f"Your Age In Months Is {mins:,} Mins")
    print(f"Your Age In Months Is {secs:,} Secs")
else:
    print("Your age is Invalid")