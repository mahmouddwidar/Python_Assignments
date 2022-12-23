# -------------------------------
# -------------72-75-------------
# -------------------------------

# -------------------------------
# ---------Assignment-1----------
# -------------------------------


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# def remove_chars(txt):
# return txt[1:-1].strip().capitalize()


for name in map(lambda txt: txt[1:-1].strip().capitalize(), friends_map):
    print(name)


# -------------------------------
# ---------Assignment-2----------
# -------------------------------


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


for name in filter(lambda txt: txt.endswith("m"), friends_filter):
    print(name)


# -------------------------------
# ---------Assignment-3----------
# -------------------------------


from functools import reduce

nums = [2, 4, 6, 2]
result = reduce(lambda num1, num2: num1 * num2, nums)

print(result)


# -------------------------------
# ---------Assignment-4----------
# -------------------------------


skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for counter, skill in enumerate(filter(lambda txt: isinstance(txt, str), skills), 50):
    print(f"{counter} - {skill}")


