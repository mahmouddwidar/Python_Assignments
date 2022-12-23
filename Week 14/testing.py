Name = str(input("Enter your Name: ")).capitalize()
Age = int(input("Enter your Age: "))
Gender = str(input("Enter your Gender: ")).capitalize()
Country = str(input("Enter your Country: ")).capitalize()
Phone_Number = str(input("Enter your Phone Number: "))

class User:
    def __init__(self, name, age, gender, country, phone_number) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.country = country
        self.phone_number = phone_number

    def just_name(self):
        return f"Hello {self.name}"
    
    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr. {self.name}"
        elif self.gender == "Female":
            return f"Hello Ms. {self.name}"
        else:
            return f"Hello {self.name}"

    def check_phone_number(self):
        import re
        phone_number = self.phone_number
        result = re.findall(r"^\d{4}-?\d{3}-?\d{4}$", phone_number)
        if result:
            return "Valid Number"
        else:
            return "Not Valid Number"

    def get_all_info(self):
        infos = [self.name, self.age, self.gender, self.country, self.phone_number]
        print("This the all info. we got about you.")
        info = 0
        for count,info in enumerate(range(len(infos)), 1):
            print(f"{count}- {infos[info]}") 
            info += 1
            


user_one_atri = User(Name, Age, Gender, Country, Phone_Number)
print(user_one_atri.just_name())
print(user_one_atri.name_with_title())
print(user_one_atri.check_phone_number())
print(user_one_atri.get_all_info())