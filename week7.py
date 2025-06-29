#equation = input("enter your equation for evaluate:")
#result = eval(equation)
#print(equation,"=",result)

"""

def evaluat_equation(equation):
    result = 0
    if "+" in equation:
        values = equation.split("+")
        result = int(values[0])+int(values[1])
    elif "-" in equation:
        values = equation.split("-")
        result = int(values[0])-int(values[1])
    elif "*" in equation:
        values = equation.split("*")
        result = int(values[0])*int(values[1])
    elif "/" in equation:
        values = equation.split("/")
        result = int(values[0])/int(values[1])
    elif "%" in equation:
        values = equation.split("%")
        result = int(values[0])%int(values[1])
        
    return result


#userin = input()
#print(userin,"=",evaluat_equation(userin))







def login(account, pin,data):
    for user in data:
        if account == user['acount_no'] and pin == user['Pin']:
            return user
            break
    else:
        print("User Not Found!!")
    


def withdraw(current_user):
    amount = int(input("Enter ammount to withdraw: "))
    if amount < current_user["Balance"]:
        if amount%500 == 0:
            current_user["Balance"] = current_user["Balance"] - amount
            return current_user
        
    else:
        print("")

def deposit(current_user):
    amount = int(input("Enter ammount to withdraw: "))
    if amount%10 == 0:
        current_user["Balance"] = current_user["Balance"] + amount
        return current_user
        
    
        

def balance(current_user):
    print("Balance:",current_user["Balance"])




userdata = [{"Name":"Yasir","Balance":40000,"Pin":1234,"acount_no":'0122738192'},
            {"Name":"Yasir1","Balance":40000,"Pin":1934,"acount_no":'0122938192'},
            {"Name":"Yasir2","Balance":40000,"Pin":1834,"acount_no":'0122038192'}]


account_no = input("Enter your account no: ")
pin_code = int(input("Enter your pin code: "))

user = login(account_no, pin_code,userdata)

if user != None:
    while True:
        print("1.Withdraw")
        print("2.Deposit")
        print("3.Check Balance")
        print("0.Exit")
        menu = int(input("Select your operation"))
        if  menu == 1:
            withdraw(user)
        elif  menu == 2:
            deposit(user)
        elif  menu == 3:
            balance(user)
        elif menu == 0:
   


#create a list of dic containing 5 user bank acounts
#ask user to enter account no and pin to log in to your atm
#create two fuctions withdraw and check balance
#and show tham as a menu to user to select operations to perform.


mystr = "          676576 56576123 24234          "
t = "teacher"
s = "student"
cl = "AI/DS"

print(mystr.istitle())
print(mystr.count("y"))
print(mystr[:4])
print(mystr.startswith("Y"))
#print(mystr.index("g"))
message = "My name is {name} and im a {pro}".format(pro = s, name = mystr)
message1 = f"My Name is {mystr} and I'm Teaching {cl}"
print(message1)
print(mystr.isnumeric())
                                

newstr = "29/06/2025"
date = newstr.split("0")
print(newstr.join(["abc"]))

print(newstr.replace("/","_"))

print("abCdEfG".swapcase())
print(newstr[:-5])

"""


userdatetime = input("Enter Date and time as 02/10/2025 04:20:30:PM: ")
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
userdatetime = userdatetime.split(" ")
data = userdatetime[0].split("/")
time = userdatetime[1].split(":")

userselection = int(input("1.Day\n2.Month\n3.Year\n4.Hour\n5.Min\n6.Seconds\nEnter your selection:"))

if userselection == 1:
    print(f"Todays Day is:{data[0]}")
elif userselection == 2:
    print(f"Todays Day is:{month[int(data[1])-1]}")
elif userselection == 3:
    print(f"Todays Day is:{data[2]}")
elif userselection == 4:
    print(f"Todays Day is:{time[0]}")
elif userselection == 5:
    print(f"Todays Day is:{time[1]}")
elif userselection == 6:
    print(f"Todays Day is:{time[2]}")
























