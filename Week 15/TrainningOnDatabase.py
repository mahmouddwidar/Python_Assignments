import sqlite3

def get_all_data():

    try:
        # Connect to the Database and adding the file path
        db = sqlite3.connect(r"D:\Python\Videos ElZero\15\Assignments\login.db")
        print("Connected to Database Successfully.")

        #Setting up the Cursor
        cr = db.cursor()

        # Fetch Data from Database
        cr.execute("SELECT * FROM users")

        # Assign Data to a Variable
        result = cr.fetchall()

        # Printing Number Of Rows in the Database
        print(f"Database Has {len(result)} Rows.")

        #Showing Data
        print("Show Data: ")

        #Looping on the list of data (Tuple)
        for row in result:
            print(f"userID => {row[0]},", end=" ")
            print(f"UserName => {row[1]}.")

    except sqlite3.Error as er:

        # Printing Error Message if couldn't get the data
        print(f"Error while Connecting: {er}")

    finally:
        if db:
            db.close()
            print("Connection to Database is closed.")




# Running The Function
get_all_data()