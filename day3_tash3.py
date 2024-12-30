list1=[]
totallist=int(input("total no of list :"))
for i in range(totallist):
    addlist=int(input())
    list1.append(addlist)
    
maximum=list1[0]
minimum=list1[0]
sum=0
for n in list1:
    if n>maximum:
       maximum=n
    if n< minimum:
      minimum=n
    sum=sum+n

        
print(list1)
print("maximum : ",maximum)
print("Minimum :",minimum)
print("Total : ",sum)
    
    