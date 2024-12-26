def add(num1,num2):
    return num1+num2
def sub(num1,num2):
        return num1-num2
def mul(num1,num2):
        return num1*num2
def div(num1,num2):
        return num1/num2
def floordiv(num1,num2):
        return num1//num2
def pow(num1,num2):
        return num1**num2

def main(option):
    if(option==1):
        print(f"{num1} + {num2} = {add(num1,num2)}")
    
    elif(option==2):
        print(f"{num1} - {num2} = {sub(num1,num2)}")
        # sub(num1,num2)
    elif(option==3):
        print(f"{num1} * {num2} = {mul(num1,num2)}")
        # mul(num1,num2)
    elif(option==4):
        print(f"{num1} / {num2} = {div(num1,num2)}")
        # div(num1,num2)
    elif(option==5):
        print(f"{num1} // {num2} = {floordiv(num1,num2)}")
        # floordiv(num1,num2)
    elif(option==6):
        print(f"{num1} ** {num2} = {pow(num1,num2)}")
        # pow(num1,num2)
    else:
        print("Enter the only above option 1/2/3/4/5/6 ")
    

if __name__=="__main__":
    num1=int(input("Enter your 1st number : "))
    num2=int(input("Enter your 2nd number : "))
    print("\n 1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.FloorDivision\n6.Power")
    option=int(input("Enter your option : "))
    main(option)