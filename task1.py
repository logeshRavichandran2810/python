# swap without 3rd variable
# a="nir"
# b="log"
# a,b=b,a
# print(a)
# print(b)

# swap using 3rd variable
# a="nir"
# b="log"
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

a=int(input("Enter total Amount :"))
b=int(input("Enter total no of share :"))
c=int(input("Enter your tip amount:"))
share=(a+c)/b
print("-"*50)
print("individual share :",share)