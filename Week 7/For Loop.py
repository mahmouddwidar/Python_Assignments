#----------------------------------
#-------------For-Loop-------------
#--------------51-55---------------

#-----------Assigment-1------------

# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)

#Process
x = 0
for num in my_nums:
    if num % 5 == 0:
        x += 1
        
        print(f" {x} => {num} ")

else:
    print("All Numbers Printed")


# Needed Output
"1 => 20"
"2 => 15"
"3 => 5"
"All Numbers Printed"


#----------------------------------
#-----------Assigment-2------------
#----------------------------------


for num in range(1,21):

    if num == 6 or num == 8 or num == 12:
        continue

    print(str(num).zfill(2))

else:
    print("All Numbers Printed")



#----------------------------------
#-----------Assigment-3------------
#----------------------------------

# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

grades = {
    'A' : 100,
    'B' : 80,
    'C' : 40
}

total = 0
for subject, rank in my_ranks.items():
  print(f"My Rank in {subject} Is {rank} And This Equal {grades[rank]} Points.")

  total += grades[rank]
  print(f"Total Points Is {total}")
  




# Needed Output
"My Rank in Math Is A And This Equal 100 Points"
"My Rank in Science Is B And This Equal 80 Points"
"My Rank in Drawing Is A And This Equal 100 Points"
"My Rank in Sports Is C And This Equal 40 Points"
"Total Points Is 320"
  


#----------------------------------
#-----------Assigment-4------------
#----------------------------------


# Input

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

grades = {
  "A": 100,
  "B": 80,
  "C": 40,
  "D": 20
}



for main_key, main_value in students.items():
  print("------------------------------")
  print(f"-- Student Name => {main_key}")
  print("------------------------------")

  total = 0
  for subject, rank in main_value.items():
    print(f"- {subject} => {grades[rank]} Points")
    total += grades[rank]
  
  print(f"Total Points For {main_key} Is {total}")    




# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"