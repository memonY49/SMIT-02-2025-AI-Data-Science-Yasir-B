"""
student_data = {"st1":{"Math":60,"Chemistry":70,"Urdu":40,"Bio":50,"Sindhi":80},
                "st2":{"Math":65,"Chemistry":70,"Urdu":45,"Bio":50,"Sindhi":80},
                "st3":{"Math":60,"Chemistry":75,"Urdu":40,"Bio":45,"Sindhi":70}}



count = 0

while count < len(student_data):
    st_Id = list(student_data.keys())[count]
    sub_marks = list(student_data.values())[count]
    print("Student Id:",st_Id)
    obtain_marks = 0
    j = 0
    while j < len(sub_marks):
        sub = list(sub_marks.keys())[j]
        marks = list(sub_marks.values())[j]
        print(sub,marks)
        obtain_marks += marks
        j+=1
    print("Obtain marks:",obtain_marks)
    obtain_per = (obtain_marks/500)*100
    print("%:",obtain_per)
    if obtain_per >=80:
        print("Grade:","A")
    elif obtain_per >=60 and obtain_per <=79:
        print("Grade:","B")
    elif obtain_per >=40 and obtain_per <=59:
        print("Grade:","C")
    else:
        print("Grade:","Fail")
    count+=1
"""










"""
for key, value in student_data.items():
    print("*"*100)
    print(key)
    obtain_marks = 0
    for sub, marks in value.items():
        print(sub,marks)
        obtain_marks += marks
    print("Obtain marks:",obtain_marks)
    print("Ttal marks:",500)
    obtain_per = (obtain_marks/500)*100
    print("%:",obtain_per)
    
    if obtain_per >=80:
        print("Grade:","A")
    elif obtain_per >=60 and obtain_per <=79:
        print("Grade:","B")
    elif obtain_per >=40 and obtain_per <=59:
        print("Grade:","C")
    else:
        print("Grade:","Fail")


    print("*"*10)
    print("Student Id:",st_id)
    total_marks = 0
    for sub, marks in st_marks.items():
        total_marks = total_marks + marks
        print(sub+":",marks)
    print("Obtain Marks:",total_marks)
    print("Total Marks:",500)
    print("Total %:",100.0)
    print("Obtain %:",(total_marks/500)*100)
    print("*"*10)




i = 0
while i < 5:
    print("i=",i)
    j = 0
    while j < 5:
        print("j=",j)
        j+=1
    print(i,j)
    i+=1
    


for i in range(0,5):
    for j in range(0,5):
        print(i,j)
    print("-",i,j)
"""

while True:
    try:
        number = int(input("Please Enter you number to check:"))
    
        if number % 2 == 0:
            print("The number is Even")
        else:
            print("The number is Odd")
        Exit = False
        while True:
            userin = input("press y to continue and n to exit.")
            if userin == 'y':
                break
            elif userin == 'n':
                Exit = True
                break
            else:
                print("invalid input!!")
                continue
        if Exit:
            break
    except:
        print("invailed number!!")
    











#ask user to input a number and check the number is even or odd,
#than ask the user again to continue for the next number or exit.
















