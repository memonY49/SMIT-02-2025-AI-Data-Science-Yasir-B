import math

# factorials = []
# with open('factorial_input.txt', 'r') as myfile:
#     data = myfile.readlines()
#     factorials = [str(math.factorial(int(value.strip())))+'\n' for value in data]
#
# with open("factorial_output.txt", 'w') as myfile:
#     myfile.writelines(factorials)


# w/hpow2

with open('bmi_input.csv', 'r') as myfile:
    data = myfile.readlines()
    data.pop(0)
    for user in data:
        user_name, w, h = user.strip().split(',')
        h = float(h)/100
        BMI = float(w)/math.pow(h,2)
        print(f"BMI of user {user_name} is {BMI}")




