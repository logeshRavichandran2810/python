num=int(input("Enter a number : "))
n=str(num)
size=len(n)
sum=0
for i in range(size):
    n=num%10
    sum = sum+n
    num = num//10
print(sum)