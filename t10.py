# input : 123
# output : 3+2+1 = 6
num=int(input("Enter a number : "))
n=str(num)
size=len(n)
sum=0
for i in range(size):
    n=num%10
    sum = sum+n
    num = num//10
print(sum)

# or 

a=input()
c=0
for i in a:
    c+=int(i)
print(c)

# input : 1234
# output : 1+2+3+4 = 10