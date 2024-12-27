import calculator
def main(option):
    if(option==1):
        print("-"*40)
        print(f"{num1} + {num2} = {calculator.add(num1,num2)}")
    
    elif(option==2):
        print("-"*40)
        print(f"{num1} - {num2} = {calculator.sub(num1,num2)}")
        # sub(num1,num2)
    elif(option==3):
        print("-"*40)
        print(f"{num1} * {num2} = {calculator.mul(num1,num2)}")
        # mul(num1,num2)
    elif(option==4):
        print("-"*40)
        print(f"{num1} / {num2} = {calculator.div(num1,num2)}")
        # div(num1,num2)
    elif(option==5):
        print("-"*40)
        print(f"{num1} // {num2} = {calculator.floordiv(num1,num2)}")
        # floordiv(num1,num2)
    elif(option==6):
        print("-"*40)
        print(f"{num1} ** {num2} = {calculator.pow(num1,num2)}")
        # pow(num1,num2)
    else:
        print("Enter the only above option 1/2/3/4/5/6 ")
    
if __name__=="__main__":
    num1=int(input("Enter your 1st number : "))
    num2=int(input("Enter your 2nd number : "))
    print("\n 1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.FloorDivision\n6.Power")
    option=int(input("Enter your option : "))
    main(option)