data = [[["Corolla",2012,1500000,"GLI"],
         ["Corolla1",2012,1500000,"GLI"],
         ["Corolla2",2012,1500000,"GLI"]],
        [["Aulto",2008,100000,"VXR"],
         ["Aulto",2008,100000,"VXR"],
         ["Aulto",2008,100000,"VXR"]]]



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














    
