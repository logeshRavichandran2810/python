Menu=['Dal','Paneer','Kofta','Tawa paneer','Rice','Roti']
size=len(Menu)
for i in range(size):
    print(Menu[i])

author_name=('J K Rowling','Rachel Aaron','Hans Aarud','Verna Aardema')
size=len(author_name)
for i in range(size):
    print(author_name[i])

Timing='it\'s 7.30am'
for i in Timing:
    print(i,end="")

# Alternate Method

Menu=[]
size=int(input("Enter the size of the list : "))
print("Enter the values : ")
for i in range(size):
    value=input()
    Menu.append(value)
print("Menu = " ,Menu)