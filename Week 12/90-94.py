# -------------------------------
# -------------90-94-------------
# -------------------------------

# -------------------------------
# ---------Assignment-1----------
# -------------------------------


NUM = int(input("Add Your Number: "))

# Your Code Here
if type(NUM) != int():
    raise Exception("Only Number Allowed")
elif NUM == 0:
    raise ValueError("Number Must Be Larger Than 0")
elif NUM > 9 or NUM < -9:
    raise IndexError("Only One Character Allowed")
else:
    print("#" * 20)
    print(f"The Number Is {NUM}")
    print("#" * 20)

# -------------------------------
# ---------Assignment-2----------
# -------------------------------

LETTER = input("Add Letter From A to Z: ")


# if len(LETTER) > 1:
# print("You Must Write One Character Only")
# elif LETTER != LETTER.upper():
# print("The Letter Not In A - Z")
# else:
# print(f"You Typed {LETTER}")


# -------------------------------
# ---------Assignment-3----------
# -------------------------------


def calculate(num1: int, num2: int) -> int:
    return num1 + num2


print(calculate(20, 30))
