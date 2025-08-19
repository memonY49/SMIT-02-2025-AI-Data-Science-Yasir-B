# Types of Methods:
# 1. Instance Method
# 2. Class Methods
# 3. Static Methods
# Instance Methods:
# Class Methods:
#
# Static methods:
#

class Student:
    school = 'SMIT school'
    def __init__(self, name, age , roll):
        self.name = name
        self.age = age
        self.roll = roll

    def display(self):
        return f"Student name: {self.name},Roll No: {self.roll}"

    @classmethod
    def get_age(cls,name,birth_year,roll):
        current_year = 2025
        age = current_year - birth_year
        return cls(name,age,roll)

    @staticmethod
    def get_school_name(school):
        return f"School name is: {school}"


s1 = Student('Yasir',20,'0012')
# print(Student.get_age("ali",2000))
# print(s1.display())
s2 = Student.get_age('Ali',2001,'0013')
print(Student.get_school_name("SMIT School"))
print(s2.display())

# instence level: instence and class
# class level: only class
# static leve: this an indepentend method placed inside a class


# Create a class named as DataBase_Conn
# Create a Data.txt file to store user data.
# Add two instance level methods (Login, Signup, "check_email_already_registered")
# Add cls level method (EmailGen)
# Add Static method(Pass_validate)


class DataBase_Conn:
    def __init__(self, File):
        self.file = File
    def Login(self, Email, Pass):
        with open(self.file, 'r') as file:
            for line in file.readlines():
                user = line.strip().split(',')
                if user[2] == Email and user[3] == Pass:
                    print(user)
                    break
            else:
                print("User Not Found......")
    def Signup(self, Name, Fname, Pass):
        email = self.EmailGen(Name,Fname)
        with open(self.file, 'a') as file:
            user = f"{Name},{Fname},{email},{Pass}\n"
            file.write(user)

    @classmethod
    def EmailGen(cls, name, fname):
        return f"{name}{fname}@SMIT.com"

    @staticmethod
    def Pass_validate(Pass):
        if len(Pass) >= 8:
            return True
        return False


db = DataBase_Conn('data.txt')



while True:
    print("1. Login")
    print("2. Signup")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Email = input("Enter your email: ")
        Pass = input("Enter Your Pass: ")
        if DataBase_Conn.Pass_validate(Pass):
            db.Login(Email,Pass)
        else:
            print('Invalid Password....')
    elif choice == 2:
        Name = input("Enter your Name: ")
        Fname = input("Enter your Father Name: ")
        Pass = input("Enter Your Pass: ")
        if DataBase_Conn.Pass_validate(Pass):
            db.Signup(Name, Fname, Pass)
        else:
            print('Invalid Password....')
    elif choice == 3:
        break









