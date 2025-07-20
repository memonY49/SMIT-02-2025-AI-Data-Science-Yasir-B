with open("data.txt",'r') as myfile:
    # data = []
    #
    # for line in myfile.readlines():
    #     temp = line.strip().split(',')
    #     data.append({"Name":temp[0],
    #                  "Fname":temp[1],
    #                  "Cnic":temp[2],
    #                  "Phone":temp[3],
    #                  "Add":temp[4],
    #                  "Email":temp[5],
    #                  "Pass":temp[6]})
    #
    # useremail = input('Enter your email:')
    # userpass = input('Enter your Pass:')
    #
    # for user in data:
    #     if useremail == user['Email'] and userpass == user['Pass']:
    #         print(f'Name:{user["Name"]}')
    #         print(f'FName:{user["Fname"]}')
    #         print(f'CNIC:{user["Cnic"]}')
    #         print(f'Phone:{user["Phone"]}')
    #         print(f'Add:{user["Add"]}')
    #         print(f'Email:{user["Email"]}')
    print(myfile.writelines())


