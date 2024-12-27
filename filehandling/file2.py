import os
def readfile(newfile):
    if(os.path.exists(newfile)):
        file=open(newfile,"r")
        data=file.read()
        createfile(data)
        file.close()
    else:
        print("File already exits")


    
def createfile(data):
    file=open('abc.txt','w')
    file.write(data)
    print("content copy successflly")
    file.close()
        
def main():
    print("Create a file : ")
    newfile=input()
    readfile(newfile)
if __name__=="__main__":
    main()