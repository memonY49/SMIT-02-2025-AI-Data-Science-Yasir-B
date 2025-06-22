def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def dev(a,b):
    print(a/b)
    
def mod(a=2,yasir=2):
    print(a%yasir)

while True:
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. dev")
    print("5. mod")
    print("0. exit")
    
    userin = int(input("Select your operation: "))
    value1 = int(input("Enter Value one: "))
    value2 = int(input("Enter Value two: "))
    if userin == 1:
        add(value1,value2)
    elif userin == 2:
        sub(value1,value2)
    elif userin == 3:
        mul(value1,value2)
    elif userin == 4:
        dev(value1,value2)
    elif userin == 5:
        mod()
    elif userin == 0:
        break
    else:
        print(  "Invalied input")










