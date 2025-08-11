# # how to create a class in python
# #       constructor is a method with same name as a class
# #           - A constructor is called while creating an object of a class
# # class calculator:
# #     user_name = None
# #     def __init__(self,name = None):
# #         self.user_name = name
# #     def add(self,x, y):
# #         return x+y
# #     def sub(self,x, y):
# #         return x-y
# #     def mul(self,x, y):
# #         return x*y
# #
# #
# # obj1 = calculator()
# # print(obj1.add(2,6))
# # print(obj1.user_name)
#
#
# class animal:
#     legs = None
#     eys = None
#     tail = None
#     ears = None
#     color = None
#
#     def voice(self):
#         print("------------")
#     def walk(self):
#         print("Animal is walking...")
#
#     def get_legs(self):
#         return self.legs
#     def get_ears(self):
#         return self.ears
#     def set_legs(self,legs):
#         self.legs = legs
#     def set_ears(self,ears):
#         self.ears = ears
#
# class dog(animal):
#     def __init__(self,leg,eyes,ears,tail,color):
#         self.legs = leg
#         self.tail = tail
#         self.eys = eyes
#         self.color = color
#         self.ears = ears
#     def voice(self):
#         print("Dog is barking.....(Bhaw Bhaw ..)")
#
# class cat(animal):
#     def __init__(self,leg,eyes,ears,tail,color):
#         self.legs = leg
#         self.tail = tail
#         self.eys = eyes
#         self.color = color
#         self.ears = ears
#
# objectanimal = animal()
# objectdog = dog(4,2,2,1,'white')
# objectdog.set_ears(5)
# print(objectanimal.get_legs())
# print(objectdog.get_legs())
#
# objectdog.voice()

# class person:
#     Name = None
#     Age = None
#     def __init__(self, n, a):
#         self.Name = n
#         self.Age = a
#
# class student2(person):
#     Roll = None
#     Grade = None
#     def __init__(self, Name, Age, Roll_no, Grade):
#         super().__init__(Name, Age)
#         self.Grade = Grade
#         self.Roll = Roll_no
#
#
# obj = student2("abc",23,12,'A')
# obj1 = student2("abc",23,12,'A')
# print(obj.format())

class student:
    Name = None
    Roll = None
    class_name = None
    def __init__ (self, Name, Roll, CN):
        self.Name = Name
        self.Roll = Roll
        self.class_name = CN
    def __str__(self):
        return f"{self.Name}({self.Roll})"
    def __repr__(self):
        return f"{self.Name}({self.Roll})"
    def __int__(self):
        return int(self.Roll)
class university:
    students = []

    def __len__(self):
        return len(self.students)
    def __repr__(self):
        self.display()
        return ""
    def add_student (self, student):
        self.students.append(student)
    def remove_student(self, roll):
        for index, stud in enumerate(self.students):
            if stud.Roll == roll:
                self.students.pop(index)
    def display(self):
        for stud in self.students:
            print(f"Name:{stud.Name}\nRoll:{stud.Roll}")
            print("-------------")
    def backup(self):
        with open("data.txt", 'w') as file:
            data = []
            for stud in self.students:
                data.append(f"{stud.Name},{stud.Roll},{stud.class_name}\n")
            file.writelines(data)


# stud1 = student("Yasir","0001","DSAI")
# stud2 = student("Yasir1","0002","DSAI")
# stud3 = student("Yasir2","0003364783783489","DSAI")
# my_uni = university()
# my_uni.add_student(stud1)
# my_uni.add_student(stud2)
# my_uni.add_student(stud3)
# # my_uni.remove_student("0001")
# # print(len(my_uni))
# # print(int(stud3))
#
# print(my_uni)

#
# class bank:
#     amount = None
#     holder_name = None
#     def __init__(self, amount, name):
#         self.amount = amount
#         self.holder_name = name
#     def __repr__(self):
#         return f"Account title: {self.holder_name}\nAccount balance:{self.amount}"
#     def __sub__(self, other):
#         self.amount -=other
#         return "Transection is succsesfull"
#     def __add__(self, other):
#         self.amount += other
#         return "Transection is succsesfull"
#     def __radd__(self, other):
#         self.amount += other
#         return "Transection is succsesfull"
# myacount = bank(100000, "Yasir Nawaz")
# myacount2 = bank(100000, "Yasir Nawaz")
# print(myacount-10000)
# print(myacount.amount)
# print(myacount2+myacount)
# # str(myacount)




# def display_message(message):
#     def decorate():
#         print("Wellcome")
#         print(message)
#         print("Bye")
#     decorate()


# def my_decorator(func):
#     def wrapper():
#         print("wrape before function call")
#         result = func()
#         print("wrape after function call")
#         return result
#     return wrapper

# def display_message():
#     print("hello")
# def my_name():
#     print("Yasir")
# my_decorator(display_message)

# decorater_func = my_decorator(my_name)
# decorater_func()



# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print(f"Welcome to SMIT....{kwargs['name']}")
#         if kwargs['name'] == 'yasir':
#             result = func(*args,**kwargs)
#         else:
#             result = None
#         print("Thank You...")
#         return result
#     return wrapper
#
# @my_decorator
# def display_name(name,fname= "Nawaz"):
#     print("hello")

# display_name(name = 'yasgir')



amount = 50000
account_title = "Yasir"

def confirmation(func):
    def wrapper(*args,**kwargs):
        confirm = input(f"Do you want to continue {func.__name__} transaction (y/n)")
        if confirm.lower() == 'y':
            result = func(*args,**kwargs)
            print("Transaction Completed.......")
        else:
            result = None
            print("Transaction cancelled......")
        print("Thank You for visiting......")
        return result
    return wrapper


@confirmation
def deposit(value,amount):
    amount += value
    return amount

@confirmation
def check_bl():
    print(amount)

@confirmation
def withdrawal(value,amount):
    amount -=value
    return amount


amount = withdrawal(10000,amount)
check_bl()















