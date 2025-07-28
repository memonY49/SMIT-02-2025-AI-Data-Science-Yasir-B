import math

# print(math.pow(2,1))
# print(math.sqrt(100))
# print(math.isqrt(25))
# print(math.factorial(20))
# print(math.pi)
# print(math.nan)
# print(math.prod([0,2,4,5,7,8,9]))

# def areaOfCircle(r):
#     return math.pi*math.pow(r,2)
#
# userin = float(input("Enter circle Radius: "))
#
# print(areaOfCircle(userin))

print(math.floor(5.7))


#Check if a number is a perfect sqrt or not.

def is_perfect_sqrt(number):
    n_sqrt = math.floor(math.sqrt(number))
    return math.pow(n_sqrt,2) == number


# print(math.sqrt(0))
# print(is_perfect_sqrt(26))
#check distance between two points.

def check_distance(point1, point2):
    x_c = math.pow(point2[0] - point1[0],2)
    y_c = math.pow(point2[1] - point1[1],2)
    return math.sqrt(x_c + y_c)

x1 = float(input("Enter X value for point 1:"))
y1 = float(input("Enter y value for point 1:"))
x2 = float(input("Enter X value for point 2:"))
y2 = float(input("Enter y value for point 2:"))

print(check_distance((x1,y1),(x2,y2)))



