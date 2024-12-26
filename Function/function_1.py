# def add(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1-num2
# def main():
#     print(f"Addition of {n1,n2} is {add(n1,n2)}")
#     print(f"Subtraction of {n1,n2} is {sub(n1,n2)}")

def function(num1,num2):
    addition = num1+num2
    subtraction = num1 - num2
    return addition,subtraction
    

if __name__=="__main__":
    n1=int(input("Enter a 1st number : "))
    n2=int(input("Enter a 2nd number : "))
    # main()
    addition,subtrtaction=function(n1,n2)
    print("Addition : ",addition)
    print("Subtraction : ",subtrtaction)