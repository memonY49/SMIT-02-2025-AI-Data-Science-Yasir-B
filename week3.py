"""
a = 11

if a > 6:
    if a%2 == 0:
        print("a is greater than 6 and it s even")
    else:
        print("a is greater than 6 and it is odd")
else:
    print("a is not greater than 6")

name = "abc"
email = "abc@123.com"
password = "abc123"

useremailin = input("Please Enter Your Email: ")
userpassin = input("Please Enter your password: ")

if email == useremailin:
    if password == userpassin:
        print("Name:",name)
        print("Email:",email)
    else:
        print("password is not matched")
else:
    print("Email not found")

#create variables to store user data like Name,Phone,Email and
#Password than check if Email stored in variable is matched to given "email"
#than check same condition for password if the password is also matched than
#print all details of a user


#Take an amount as input from user and print how many notes will come from atm.



a = int(input("Please Enter Value to compare: "))

if a < 6:
    print("a is less than 6")
elif a > 6:
    print("a is greater than 6")
elif a == 6:
    print(" a is equal to 6")
  """
'''
amount = int(input("Enter your amount: "))#Taking input from user

if amount%10 == 0:
    notesin5000 = int(amount/5000)
    amount = amount%5000
    notesin1000 = int(amount/1000)
    amount = amount%1000
    notesin500 = int(amount/500)

    print("Notes of 5000: ",notesin5000)
    print("Notes of 1000: ",notesin1000)
    print("Notes of 500: ",notesin500)
else:
    print("invailed amount")




userdetails = ["ahmed","Ali",41303230423023,"abc@gmail.com","abc123"]

useremailin = input("Please Enter Your Email: ")
userpassin = input("Please Enter Your Password: ")

if useremailin == userdetails[3] and userpassin == userdetails[4]:
    print("Name: ",userdetails[0])
    print("FName: ",userdetails[1])
    print("CNIC: ",userdetails[2])
    print("Email: ",userdetails[3])

'''
'''
userdetails = ["ahmed","Ali",41303230423023,"abc@gmail.com","abc123"]

userdetails[0] = "rizwan"

print(userdetails)


NoofNotes = [0,0,0]


amount = int(input("Enter your amount: "))#Taking input from user

if amount%10 == 0:
    NoofNotes[0] = int(amount/5000)
    amount = amount%5000
    NoofNotes[1] = int(amount/1000)
    amount = amount%1000
    NoofNotes[2] = int(amount/500)

    print(NoofNotes)
else:
    print("invailed amount")
'''

MyList = {"ag","ac","a","ab"}
#MyList.append(10)
#MyList.insert(2,10)
#MyList.clear()
#MyList1 = MyList.copy()
#MyList.extend([1,4,6])
#MyList.pop()
#print(MyList.count(6))
#print(MyList1)
#MyList.pop()
#MyList.pop()
#MyList.pop()
#MyList.remove(4)
#MyList.reverse()
#MyList.sort()
print(MyList)

#Task: create Multi List for 5 companys containing 5 names of cars,
#show a menu to user to select Company names and it shows all the available cars
#of that selected company





carData = [[["Corolla",2012,1500000,"GLI"],
            ["Corolla",2010,1500000,"GLI"],
            ["Corolla",2011,1500000,"GLI"]],
           [["Aulto",2008,100000,"VXR"],
            ["Aulto",2008,100000,"VXR"],
            ["Aulto",2008,100000,"VXR"]]]

data = [[["Corolla",2012,1500000,"GLI"],
         ["Corolla",2012,1500000,"GLI"],
         ["Corolla",2012,1500000,"GLI"]],
        [["Aulto",2008,100000,"VXR"],
         ["Aulto",2008,100000,"VXR"],
         ["Aulto",2008,100000,"VXR"]]]



print("1.Toyota")
print("2.Suzuki")

userin = int(input())
if userin == 1:
    print("1.",data[0][0][0])
    print("2.",data[0][1][0])
    print("3.",data[0][1][0])
    userin = int(input())
    if userin == 1:
        print("Name:",data[0][0][0])
        print("Year:",data[0][0][1])
        print("Price:",data[0][0][2])
elif userin == 2:
    print("1.",data[1][0][0])
    print("2.",data[1][1][0])
    print("2.",data[1][1][0])
    userin = int(input())

















