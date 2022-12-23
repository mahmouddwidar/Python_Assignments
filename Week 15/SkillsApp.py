# Date: 17/Dec.(12)/2022 => Saturday
# Time: 2:17 pm
#Coding By "Mahmoud Dwidar"

input_message = """
What do you want to do?
"S" => Show All Siklls.
"A" => Add A New Sikll.
"D" => Delete A Sikll.
"U" => Update Sikll Progress.
"Q" => Quit The App.
Choose An Option: 
"""
user_input = input(input_message).strip().lower()

# User ID
uid = 1

# Importing SQLite Module
import sqlite3

# Connecting to Data
db = sqlite3.connect(r"D:\Python\Videos ElZero\15\Assignments\app.db")

# Setting up Cursor
cr = db.cursor()

# Setting up tables
cr.execute("CREATE TABLE IF NOT EXISTS skills(skill_name TEXT, progress INTEGER, user_id INTEGER)")

def commit_and_close():
    """Saving (Committing) The Data and Closing The Connection To Database"""
    db.commit() # Save The data
    db.close() # Close the Connection
    print("The connection Is Closed.")


commands_list = ["s", "a", "d", "u", "q"]

#Define The Methods
def show_skills():
    """Showing The Saved Data in Database By User Define"""
    cr.execute(f"SELECT * FROM skills WHERE user_id = '{uid}'")
    results = cr.fetchall()
    print(f"You Have {len(results)} Skills.")
    if len(results) > 0:
        print("Showing Skills With Progress: ")
    for row in results:
        print(f"Skill => {row[0]}, ", end=" ")
        print(f"Progress => {row[1]}%")
    commit_and_close()

def add_skill():
    """Adding New Skills To Database By User"""
    skill_name = input("Insert The Skill Name: ").strip().capitalize()
    cr.execute(f"SELECT skill_name FROM skills WHERE skill_name = '{skill_name}' AND user_id = '{uid}'")
    result = cr.fetchone()
    if result == None:
        progress = input("Insert Your Progress in \"%\": ").strip()
        # Inserting Data to The Table
        cr.execute(f"INSERT INTO skills(skill_name, progress, user_id) VALUES('{skill_name}', '{progress}', '{uid}')")
        print("The Skill Has Been Added Successfully.")
        commit_and_close()
    else:
        print("You Can't Add This Skill, It's Already Exists.")
        print("But you can Update it (\"Yes\" or \"No\")")
        print("Write \"y\" (yes) or \"n\" (no).")
        check_update = input("Enter your Choice: ").strip().capitalize()
        if check_update == "Y" or check_update == "Yes":
            new_progress = input("Write the New Progress: ").strip()
            cr.execute(f"UPDATE skills SET progress = '{new_progress}' WHERE skill_name = '{skill_name}' AND user_id = '{uid}'")
            print("The Skill Has Been Updated Successfully.")
            commit_and_close()
        elif check_update == "N" or check_update == "No":
            print("the App Is Closed.")
            commit_and_close()
        else:
            print("Please, Enter A Valid Answer.")


def delete_skill():
    """Deleting A Skill By the User"""
    skill_name = input("Insert The Skill Name: ").strip().capitalize()

    # Deleting Data From The Table
    cr.execute(f"DELETE FROM skills WHERE skill_name = '{skill_name}' AND user_id = '{uid}'")
    print("The Skill Has Been Deleted.")
    commit_and_close()

def update_skill():
    """Updating Skill Progress"""
    skill_name = input("Write Your Skill: ").strip().capitalize()
    new_progress = input("Write the New Progress: ").strip()
    cr.execute(f"UPDATE skills SET progress = '{new_progress}' WHERE skill_name = '{skill_name}' AND user_id = '{uid}'")
    print("The Skill Has Been Updated Successfully.")
    commit_and_close()

# Check the user Input
if user_input in commands_list:
    # print(f"Command Is Found \"{user_input}\"")
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skill()
    elif user_input == "d":
        delete_skill()
    elif user_input == "u":
        update_skill()
    else:
        print("the App Is Closed.")
        commit_and_close()
else:
    print(f"Sorry The Command \"{user_input}\" Is Not Found.")
