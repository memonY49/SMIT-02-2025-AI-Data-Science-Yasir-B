data = [[["Toyota","Corolla",2012,1500000,"GLI"],
         ["Toyota","Corolla1",2012,1500000,"GLI"],
         ["Toyota","Corolla2",2012,1500000,"GLI"]],
        [["Suzuki","Aulto1",2008,100000,"VXR"],
         ["Suzuki","Aulto2",2008,100000,"VXR"],
         ["Suzuki","Aulto3",2008,100000,"VXR"]],
        [["Kia","Aulto",2008,100000,"VXR"],
         ["Kia","Aulto",2008,100000,"VXR"],
         ["Kia","Aulto",2008,100000,"VXR"]],
        [["Honda","Aulto",2008,100000,"VXR"],
         ["Honda","Aulto",2008,100000,"VXR"],
         ["Honda","Aulto",2008,100000,"VXR"]]]


while True:
    companies = [comp[0][0] for comp in data]
    print(0,"Exit")
    for index,comp in enumerate(companies):
        print(index+1,comp)
    usercomp = int(input("Please Select your Company: "))
    if usercomp == 0:
        break
    elif usercomp > 0 and usercomp <= len(data):
        for index, car in enumerate(data[usercomp-1]):
            print(index+1, car[1])
        usercar = int(input("Please Select your Car: "))
        if usercar > 0 and usercar <= len(data[usercomp-1]):
            print("Name:",data[usercomp-1][usercar-1][1])
            print("Year:",data[usercomp-1][usercar-1][2])
            print("Model:",data[usercomp-1][usercar-1][3])
            print("Price:",data[usercomp-1][usercar-1][4])
        else:
            print("Invailed selection of a car")
    else:
        print("Invailed selection of a company")














"""
print("1.Toyota")
print("2.Suzuki")

userin = int(input())
if userin == 1:
    print("1.",data[0][0][0])
    print("2.",data[0][1][0])
    print("3.",data[0][2][0])
    userin = int(input())
    if userin == 1:
        print("Name:",data[0][0][0])
        print("Year:",data[0][0][1])
        print("Price:",data[0][0][2])
    elif userin == 2:
        print("Name:",data[0][1][0])
        print("Year:",data[0][1][1])
        print("Price:",data[0][1][2])
    elif userin == 3:
        print("Name:",data[0][2][0])
        print("Year:",data[0][2][1])
        print("Price:",data[0][2][2])
elif userin == 2:
    print("1.",data[1][0][0])
    print("2.",data[1][1][0])
    print("3.",data[1][2][0])
    userin = int(input())
    if userin == 1:
        print("Name:",data[1][0][0])
        print("Year:",data[1][0][1])
        print("Price:",data[1][0][2])
    elif userin == 2:
        print("Name:",data[1][1][0])
        print("Year:",data[1][1][1])
        print("Price:",data[1][1][2])
    elif userin == 3:
        print("Name:",data[1][2][0])
        print("Year:",data[1][2][1])
        print("Price:",data[1][2][2])

"""












    
