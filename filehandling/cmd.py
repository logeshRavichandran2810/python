# argument that are given after the name of a program in cmd shell of the os
from sys import *
def add(val1,val2):
    return val1+val2
def main():
    print("Application Name : ",argv[0])
    if(len(argv)!=3):
        print("Enter two Nunber")
        exit()
    print("First Number : ",argv[1])
    print("Second Number : ",argv[2])
    print("Additon : ",add(int(argv[1]),int(argv[2])))
    if(len(argv)!=3):
        print("Enter two Nunber")
if __name__=="__main__":
    main()