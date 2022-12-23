#-------------------------------------
#------------------1------------------
#-------------------------------------

new_file = open(r"C:\Users\al-kamel\Desktop\Python\assign.py", "w")
import os

for files in range(1, 51):
    new_file = open(f"C:/Users/al-kamel/Desktop/Python/txt{files}.txt", "w")
    new_file.write(f"Elzero Web School => {files}")

os.remove("C:/Users/al-kamel/Desktop/Python/txt25.txt")
new_25 = open("C:/Users/al-kamel/Desktop/Python/special-text.txt", "w")
new_25.write("")

#-------------------------------------
#------------------3------------------
#-------------------------------------


new_file = open(r"C:\Users\al-kamel\Desktop\Python\txt1.txt", "a")

with open(r"C:\Users\al-kamel\Desktop\Python\txt1.txt", "r") as txt1:
    linesnum = len(txt1.readlines())
    print(f"Number Of Lines Is => {linesnum}")

    data = txt1.read()
    print(f"Number Of Words Is => ", len(data.split()))

    data = txt1.read().replace(" ", "")
    print("Number Of Chars Is => ", len(data))

    data = txt1.read()
    print("Number Of 'l' Char Is => ", data.count("l"))


#-------------------------------------
#------------------4------------------
#-------------------------------------


import os

for files in range(41, 51):
    os.remove(f"txt{files}.txt")