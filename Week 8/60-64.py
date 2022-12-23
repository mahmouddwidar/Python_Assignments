#-------------------------------
#-------------60-64-------------
#-------------------------------

#-------------------------------
#---------Assignment-1----------
#-------------------------------

def get_score(**subjects):
    for sub, value in subjects.items():
        print(f"{sub} => {value}")

get_score(Math=90, Science=80, Language=70)


#-------------------------------
#---------Assignment-2----------
#-------------------------------

def get_people_scores(name="defaultName", **skills):
    if name == "defaultName":
        for student_key, student_value in skills.items():
            print(f"{student_key} => {student_value}")
    elif len(skills) == 0:
        print(f"hello {name} You Have No Scores To Show")
    else:
        print(f"hello {name} This Is Your Score Table:")
        for student_key, student_value in skills.items():
            print(f"{student_key} => {student_value}")
#-------------------------------
#---------Assignment-3----------
#-------------------------------

scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}

def get_the_scores(name = "DefaultName", **subjects):
  if name == "DefaultName":
    for sub, degree in subjects.items():
      print(f"{sub} => {degree}")
  elif len(subjects) == 0:
    print(f"Hello {name} You Have No Scores To Show")
  else:
    print(f"Hello {name} This Is Your Score Table:")
    for sub, degree in subjects.items():
      print(f"{sub} => {degree}")