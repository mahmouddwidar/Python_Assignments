

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))

print('operation = "+" Or "-" Or "*" Or "/" Or "%"')
operation = input("Enter the operation: ").strip()



if operation == "+":

    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":

    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")

elif operation == "%":
    
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")

else:
    print("Please Enter a correct operation!")