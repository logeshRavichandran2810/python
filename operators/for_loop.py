# when we need to repeat a block of code for fixed no of time we use for loop
num=10
for i in range(num):
    print(i,end=' ') 
print("\n")
print("-"*50)

for i in range(20,1,-3):
    print(i)
print("-"*50) 

food=['idly','dosa','biriyani','dal']
for i in range(len(food)):
    print(food[i],'-',i)
print("-"*50)     

for i in food:
    print(i)
print("-"*50) 
