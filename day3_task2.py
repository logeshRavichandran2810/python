list=[]
totalquestion=int(input("Enter a Toatal Number of Questions to Ask :"))
for i in range(totalquestion):
    addquestion=input()
    list.append(addquestion)
# print(list)
print("Questions Asked by User are given below ")
for i in range(totalquestion):
    print(f"{i+1}.{str(list[i])}")
    
