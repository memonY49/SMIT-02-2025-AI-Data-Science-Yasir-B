
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

data ={"Cars":{"Toyota":{"Corolla1":{"Name":"Corolla1","Year":2008,"Model":"XLI","Price":1200000},
                 "Corolla2":{"Name":"Corolla2","Year":2008,"Model":"XLI","Price":1200000},
                 "Corolla3":{"Name":"Corolla3","Year":2008,"Model":"XLI","Price":1200000}},
               "Suzuki":{"Alto1":{"Name":"Alto1","Year":2008,"Model":"VXR","Price":1200000},
                 "Alto2":{"Name":"Alto2","Year":2008,"Model":"VXR","Price":1200000},
                 "Alto3":{"Name":"Alto3","Year":2008,"Model":"VXR","Price":1200000}}},
       "Bikes":{"Toyota":{"Corolla1":{"Name":"Corolla1","Year":2008,"Model":"XLI","Price":1200000},
                 "Corolla2":{"Name":"Corolla2","Year":2008,"Model":"XLI","Price":1200000},
                 "Corolla3":{"Name":"Corolla3","Year":2008,"Model":"XLI","Price":1200000}},
                "Suzuki":{"Alto1":{"Name":"Alto1","Year":2008,"Model":"VXR","Price":1200000},
                 "Alto2":{"Name":"Alto2","Year":2008,"Model":"VXR","Price":1200000},
                 "Alto3":{"Name":"Alto3","Year":2008,"Model":"VXR","Price":1200000}}}}

for index, comp in enumerate(data.keys()):
    print(index+1, comp)
usercomp = input("Please Enter your Company Name: ").capitalize()
if usercomp in data.keys():
    for index, car in enumerate(data[usercomp].values()):
        print(index+1, car["Name"])
    usercar = input("Please Enter your Car Name: ").capitalize()
    if usercar in data[usercomp].keys():
        car = data[usercomp][usercar]
        print("Name:",car["Name"])
        print("Year:",car["Year"])
        print("Model:",car["Model"])
        print("Price:",car["Price"])

























































