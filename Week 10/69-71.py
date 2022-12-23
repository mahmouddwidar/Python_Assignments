#----------------------------
#--------------1-------------
#----------------------------


values = (0, 1, 2)

# the cond. is True bcze any() accept any true value not condition that Values should be True
if any(values):
    my_var = 0

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# The first cond. all(my_list[:4]) is True so it will print "Good"
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")


#----------------------------
#--------------2-------------
#----------------------------


v = 40

my_range = list(range(v))

print(sum(my_range, 40) + pow(40, 40, 40))  # 820


#----------------------------
#--------------3-------------
#----------------------------


n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good


#----------------------------
#--------------4-------------
#----------------------------


def my_all(l):
  return all(l)

#-----------------------

def my_any(l):
  return any(l)

#-----------------------

def my_min(l):
    return min(l)

#-----------------------

def my_max(l):
    return max(l)