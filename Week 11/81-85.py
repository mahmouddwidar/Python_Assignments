# -------------------------------
# -------------81-85-------------
# -------------------------------

# -------------------------------
# ---------Assignment-1----------
# -------------------------------


def reverse_string(my_string):
    # Your Code Here
    yield my_string[-1::-1]

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)

#-------------------------------------------------


def reverse_string(my_string):
    length = len(my_string)
    for i in range(length - 1, -1, -1):
        yield my_string[i]


# For loop to reverse the string
for char in reverse_string("Elzero"):
    print(char)


# -------------------------------
# ---------Assignment-2----------
# -------------------------------


def myDecorator(func):
    def nestedfunc():
        print("Sugar Added From Decorators")
        func()
        print("####################")

    return nestedfunc()


@myDecorator
def make_tea():
    print("Tea Created")


@myDecorator
def make_coffe():
    print("Coffe Created")
