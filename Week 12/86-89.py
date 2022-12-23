# -------------------------------
# -------------86-89-------------
# -------------------------------

# -------------------------------
# ---------Assignment-1----------
# -------------------------------


my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []
final_string = []
for data in zip(my_list, my_tuple):
    # Write Your Code Here
    my_data += list(data)
    final_string = "".join(map(str, my_data))

print(final_string.capitalize())

# -------------------------------
# ---------Assignment-2----------
# -------------------------------


my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # Write Your Code Here
    my_data += item1, item2, item3
    final_string = "".join(map(str, my_data))

final_string = final_string[1:3], final_string[4:6], final_string[7:9]
final_string = "".join(map(str, final_string))
print(final_string.capitalize())

# -------------------------------
# ---------Assignment-3----------
# -------------------------------


from PIL import Image, ImageOps

im = Image.open(r"D:\Python\Videos ElZero\12\Assignments\elzero.png")
# im.show()

# Getting " L"
box = (400, 0, 800, 400)
new = im.crop(box)
new.save(r"D:\Python\Videos ElZero\12\Assignments\Lletter.png")

# Converting the photo
convertedImage = new.convert("L")
convertedImage.save(r"D:\Python\Videos ElZero\12\Assignments\Lmode.png")

# cutting the whole lower row
myBox = (0, 400, 1200, 800)
lowerRow = im.crop(myBox)
# Converting the color
newLook = lowerRow.convert("L")
# Rolling ot rotating the Row
rotating = newLook.rotate(180)
rotating.show()

# -------------------------------
# ---------Assignment-4----------
# -------------------------------


def say_hello_to(name):
    """
    "parameter(someone) => Person Name"
    "Function To Say Hello To Anyone"
    """
    print(f"Hello {name}!")


help(say_hello_to)





