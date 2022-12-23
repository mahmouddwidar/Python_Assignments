#-------------------------------
#-------------56-59-------------
#-------------------------------

#-------------------------------
#---------Assignment-1----------
#-------------------------------


def calculate( num1, num2, parameter  ):
    
    
    if parameter == "Add" or parameter == "A" or parameter == "+":
        return num1 + num2
    elif parameter == "Subtract" or parameter == "S" or parameter == "-":
        return num1 - num2
    elif parameter == "Multiply" or parameter == "M" or parameter == "*":
        return num1 * num2
    else: #if the user didn't input the paramter make the default sum
        print("We Added the 2 numbers bec. u didn't give any parameter")
        return num1 + num2


print(calculate(float(input("Entet num1: ")), float(input("Enter num2: ")),str(input("Enter a parameter: ").capitalize().strip())  ))





#-------------------------------
#---------Assignment-2----------
#-------------------------------

def addition(*numbers):
    total = 0
    for num in numbers:
        if num == 10:
            continue

        total += num
    return total


#-------------------------------
#---------Assignment-3----------
#-------------------------------

def show_skills(name, *skills):
    
    for skill in skills:
        print(f"Hello {name} Your Skills Is")
        print(f"- {skill}")
    else:
        print(f"Hello {name}, You Have No Skills To Show")



#-------------------------------
#---------Assignment-4----------
#-------------------------------


def say_hello(name ="Unknown", age ="Unknown", country ="Unknown"):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"
