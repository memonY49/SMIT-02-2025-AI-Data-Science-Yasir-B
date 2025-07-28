import os

# print(os.getcwd())
# os.chdir('data')
# os.chdir('data')
# w  = open("abc.txt",'w')
#
# w.write("abcd")
#
# w.close()
# i = 0
# for dir in os.listdir(path = '.'):
#     if os.path.splitext(dir)[1] == '.py':
#         print(dir)
#         i+=1
# print(f'total .py files are :{i}')


# os.mkdir("DataSet/A/data.txt")

# print(os.listdir(path='DataSet/A'))
# for path, dir, files in os.walk('database'):
#     print(f"Path:{path}")
#     print(f"Dirs:{dir}")
#     print(f"Files:{files}")
#     print("*"*10)
# #

# print(os.path.join(os.getcwd(),'DataSetnsbjhbvjhkdsv'))

# os.rmdir('DataSet/C')
# os.rename('DataSet','database')

def add(filename, datalist):
    with open(filename,'a') as file:
        data = listtostring(datalist)
        file.write(data+'\n')
# add('data.txt',['name','fname','cnic','phone','email','pass'])
def listtostring(data):
    stringdata = ''
    for i, v in enumerate(data):
        if i == 0:
            stringdata = stringdata + v
        else:
            stringdata = stringdata + ',' + v
    return stringdata


def find_data(filename, email):
    with open(filename, 'r') as file:
        for index, line in enumerate(file.readlines()):
            user = line.strip().split(',')
            if user[5] == email.lower():
                return (user,index)
        else:
            return ([],-1)

# print(find_data('data.txt','abc2@gmail.com'))

def update(filename, email, updatevalue):
    user = find_data(filename, email)
    with open(filename, 'r+') as file:
        data = file.readlines()
        data[user[1]] = listtostring(updatevalue)+'\n'
        file.seek(0)
        file.writelines(data)

update('data.txt', 'abc9@gmail.com', ['Yasir9','Nawaz','43123-334242344-3','0304-4453453534','adhbbjgvgvsdhbsbdhbvjvjhbd','xyz@gmail.com','abc123'])
