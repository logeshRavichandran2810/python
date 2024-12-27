list1=[]
totallist=int(input("total no of list :"))
for i in range(totallist):
    addlist=int(input())
    list1.append(addlist)
    maximum=list1[0]
    if list1[i]>maximum:
        maximum=list1[i]
    minimum=list1[0]
    if list1[i]<minimum:
        minimum=list1[i]
    
print(list1)
print("maximum : ",maximum)
print("Minimum :",minimum)
sum=0
for i in list1:
    sum=sum+i
print("Total : ",sum)
        
    
    