# how to create a class in python
#       constructor is a method with same name as a class
#           - A constructor is called while creating an object of a class
# class calculator:
#     user_name = None
#     def __init__(self,name = None):
#         self.user_name = name
#     def add(self,x, y):
#         return x+y
#     def sub(self,x, y):
#         return x-y
#     def mul(self,x, y):
#         return x*y
#
#
# obj1 = calculator()
# print(obj1.add(2,6))
# print(obj1.user_name)


class animal:
    legs = None
    eys = None
    tail = None
    ears = None
    color = None

    def voice(self):
        print("------------")
    def walk(self):
        print("Animal is walking...")

    def get_legs(self):
        return self.legs
    def get_ears(self):
        return self.ears
    def set_legs(self,legs):
        self.legs = legs
    def set_ears(self,ears):
        self.ears = ears

class dog(animal):
    def __init__(self,leg,eyes,ears,tail,color):
        self.legs = leg
        self.tail = tail
        self.eys = eyes
        self.color = color
        self.ears = ears
    def voice(self):
        print("Dog is barking.....(Bhaw Bhaw ..)")

class cat(animal):
    def __init__(self,leg,eyes,ears,tail,color):
        self.legs = leg
        self.tail = tail
        self.eys = eyes
        self.color = color
        self.ears = ears

objectanimal = animal()
objectdog = dog(4,2,2,1,'white')
objectdog.set_ears(5)
print(objectanimal.get_legs())
print(objectdog.get_legs())

objectdog.voice()