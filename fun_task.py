# write a program to calculate area of a circle (Pi r**2)
# positional arument
# first arg positional second default
# keyword argument
# first arg keyword,second default

def area(pi,radius):
    return pi * radius**2
def main():
    result=area(pi,rad)
    print("positional argument : ",result)
    result=area(pi,radius=15)
    print("1st positional argument 2nd default argument: ",result)
    result=area(pi=3.14,radius=3)
    print("Keyword argument: ",result)
    result=area(pi=3.1,radius=4)
    print("1st keyword arg 2nd default: ",result)
    
if __name__=="__main__":
    pi=3.14
    rad=int(input("Enter a radius : "))
    main()
    
