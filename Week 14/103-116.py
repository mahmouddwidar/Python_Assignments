# -------------------------------
# -------------103-116------------
# -------------------------------

# -------------------------------
# ---------Assignment-1----------
# -------------------------------


class Game:
  # Write Class Content
  def __init__(self, name, developer, year, price_in_pounds) -> None:
    self.name = name
    self.developer = developer
    self.year = year
    self.price_in_pounds = price_in_pounds

game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds}", end="")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"



# -------------------------------
# ---------Assignment-2----------
# -------------------------------


class User:
     # Write Class Content
    def __init__(self, first_name, midlle_name, age, gender) -> None:
        self.first_name = first_name
        self.midlle_name = midlle_name
        self.age = 40 - age
        self.gender = gender
    
    
    def full_details(self):
        if self.gender == "Male":
            return f"Hello Mr {self.first_name} {self.midlle_name[0]}. [{self.age}] Years To Reach 40"
        elif self.gender == "Female":
            return f"Hello Mrs {self.first_name} {self.midlle_name[0]}. [{self.age}] Years To Reach 40"
       



user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40


# -------------------------------
# ---------Assignment-3----------
# -------------------------------


class Message:
    # Write Class Content
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def print_message():
        return "Hello From Class Message"

print(Message.print_message())

# Output
# Hello From Class Message


# -------------------------------
# ---------Assignment-4----------
# -------------------------------


class Games:
    # Write Class Content
    def __init__(self,games) -> None:
        self.games = games
        
    def show_games(self):
        if type(self.games) == str:
            print(f'I Have One Game Called "{self.games}"')
        elif type(self.games) == list:
            print("I Have Many Games:")
            for game in self.games:
                print(f"-- {game}")
        elif type(self.games) == int:
            print(f"I Have {self.games} Game.")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.


# -------------------------------
# ---------Assignment-5----------
# -------------------------------


# Main Class
class Members:

  def __init__(self, name, permission):

    self.name = name

    self.permission = permission

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):
    def __init__(self, name, permission):
        Members.__init__(self, name, permission)


# Create Moderators Class Here
class Moderators(Members):
    def __init__(self, name, permission):
       super().__init__(name, permission)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator



# -------------------------------
# ---------Assignment-6----------
# -------------------------------


class A:

  def __init__(self, one):

    self.one = one

class B(A):

  def __init__(self,one, two):
    super().__init__(one)
    self.two = two

class C(B):

  def __init__(self, one, two, three):
    super().__init__(one, two)
    self.three = three

# Write The Class Called "Text" Here
class Text(C):
    def __init__(self, one, two, three):
      super().__init__(one, two, three)

    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero