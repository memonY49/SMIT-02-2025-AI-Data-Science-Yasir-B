
"""
data = {"Toyota":{"Corolla1":{"Name":"","Year":"","Model":""},
                  "Corolla2":{"Name":"","Year":"","Model":""},
                  "Corolla3":{"Name":"","Year":"","Model":""}}}



data1 ={"Toyota":{"car1":{"Name":"","Year":"","Model":""},
                  "car2":{"Name":"","Year":"","Model":""},
                  "car3":{"Name":"","Year":"","Model":""}},
        "Suziki":{"car1":{"Name":"","Year":"","Model":""},
                  "car2":{"Name":"","Year":"","Model":""},
                  "car3":{"Name":"","Year":"","Model":""}},
        "Kia":  {"car1":{"Name":"","Year":"","Model":""},
                  "car2":{"Name":"","Year":"","Model":""},
                  "car3":{"Name":"","Year":"","Model":""}}}




my_dict = {"Name":"Yasir",
           "FName":"Nawaz",
           "Phone":"0304-5874767386",
           "Age":28,
           "CNIC":"41305-656555668-2"}

my_list = [[1,4,5,7],
           [3,6,8],
           [2,7,9]]

print(list(my_dict.keys()))
print(my_dict.values())
print(my_dict.items())
print(len(my_dict))
print(len(my_list[1]))

n = 5
for counter in range(1,n):
    print(" "*(n-counter),end = "")
    print("* "*counter)
    

my_list = [22,44,6,2,66,9,434,32,6,5,3,6,768,9,5,33,2,66,9,5]


counter = 0
while counter < len(my_list):
    print(my_list[counter])
    counter += 1 



userdetails = [["ahmed","Ali",41303230423023,"abc1@gmail.com","abc123"],
               ["ahmed","Ali",41303230423023,"abc2@gmail.com","abc123"],
               ["ahmed","Ali",41303230423023,"abc3@gmail.com","abc123"],
               ["ahmed","Ali",41303230423023,"abc4@gmail.com","abc123"],
               ["ahmed","Ali",41303230423023,"abc5@gmail.com","abc123"]]

useremail = input("Please Enter your Email: ")
userpass = input("Please Enter your Password: ")

for i in range(0,len(userdetails)):
    if useremail == userdetails[i][3]:
        if userdetails[i][4] == userpass:
            print(userdetails[i])
            break
        else:
            print("Password is incorrect")
else:
    print("Email not found")
            


my_list = {"A":1,"B":2,"C":3,"D":4}

for key, value in my_list.items():
    print(key, value)
"""
#Task 5:

data ={"Toyota":{"car1":{"Name":"car1","Year":"2000","Model":"A"},
                  "car2":{"Name":"car2","Year":"2010","Model":"B"},
                  "car3":{"Name":"car3","Year":"2012","Model":"C"}},
        "Suziki":{"car1":{"Name":"car1","Year":"2000","Model":"A"},
                  "car2":{"Name":"car2","Year":"2010","Model":"B"},
                  "car3":{"Name":"car3","Year":"2012","Model":"C"}},
        "Kia":  {"car1":{"Name":"car1","Year":"2000","Model":"A"},
                  "car2":{"Name":"car2","Year":"2010","Model":"B"},
                  "car3":{"Name":"car3","Year":"2012","Model":"C"}}}


for index in range(0,len(data.keys())):
    print(index+1,list(data.keys())[index])

company_select = input("Select your company")

for index in range(len(data[company_select])):
    print(index+1,list(data[company_select].keys())[index])

car_select = input("Select your company")

for key, value in data[company_select][car_select].items():
    print(key+": ",value)

    
























































