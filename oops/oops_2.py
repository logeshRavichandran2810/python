class Bank_Account:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print("---------your Name-----------")
        print(f"First name:{self.fname} Last name:{self.lname}")
def main():
    exc=Bank_Account('loki','rock')
    exc.display()
if __name__=="__main__":
    main()