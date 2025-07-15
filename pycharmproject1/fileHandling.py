myfile = open("data.txt","r")

# myfile.write("Yasir222,Nawaz,43123-334242344-3,0304-4453453534,adhbbjgvgvsdhbsbdhbvjvjhbd\n")


# for line in myfile.readlines():
#     print(line.replace("\n","").split(",")[2])
#
# # print(myfile.readlines()[2].replace("\n","").split(",")[2])


# name  =  input("Enter Name:")
# fname  =  input("Enter Father Name:")
# Phone  =  input("Enter Name:")
# Cnic  =  input("Enter Name:")
# Email  =  input("Enter Name:")
# Pass  =  input("Enter Name:")
#
# for i in range(0,10):
#     myfile.write(f"{name},{fname},{Cnic},{Phone},{Email},{Pass}\n")


# myfile.write("Yasir10,Nawaz,43123-334242344-3,0304-4453453534,adhbbjgvgvsdhbsbdhbvjvjhbd,abc@gmail.com,abc123")
# myfile.seek(0)
data = [line.replace("\n","").split(",") for line in myfile.readlines()]

# for line in myfile.readlines():
#     data.append(line.replace("\n","").split(","))


print(data)

myfile.close()