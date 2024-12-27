list=[]
listinput=int(input("Enter the total number list input : "))
for i in range(listinput):
    addlist=input()
    list.append(addlist)
print(list)
count=0
searchinput=input("Enter an element to search its count : ")
for i in list:
    if searchinput in i:
        count = count+1
print("Total Number Of Occurence : ",count)
    
    
