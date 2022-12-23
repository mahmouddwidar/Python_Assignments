#-------------------------------------
#-------------While Loop--------------
#---------------47-50-----------------

#-------------Assignment-1------------

num = int(input("Enter a Positive Number: "))

printed_numbers = num - 2

if num > 0:
    #Loop
    while num > 1:
        num -= 1
        # To Ignore a number
        if num == 6:
            continue
        print(num)
    else:
        print(f"{printed_numbers} Numbers Printed Successfully.")
    

else:
    print(f"Number {num} Is Not Larger Than 0")



#-------------Assignment-3------------

# Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

num = 0
while skills:

  # Type The Code Here in One Line
  
  if num < len(skills):
    print(skills[num])
    num += 1


#-------------Assignment-4------------

my_friends = []
maxmium_friends = 4

name = input("Enter your friend name: ").strip()


if name == name.upper():
    print("Invalid Name")

else:
    while maxmium_friends >= 1 and maxmium_friends <= 4:
        my_friends.append(name.capitalize())
        print(f"Friend {name} Added => 1st Letter Become Capital")
        maxmium_friends -= 1
        print(f"Names Left in List Is {maxmium_friends}")
        #igoner entering the last name
        if maxmium_friends == 0:
            continue
        name = input("Enter your friend name: ").strip()

    else:
        print("List is full.")


print(my_friends)