import os
def createfile(filename):
    if(os.path.exists(filename)):
        print("File already exists")
    else:
        file=open(filename,"w")
def main():
    print("Enter the File name you want to create : ")
    filename=input()
    createfile(filename)
if __name__=="__main__":
    main()