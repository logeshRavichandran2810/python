class Bank_Account:
    def __init__(self):
        self.Name=""
        self.Amount=0
        self.Address=""
        self.AccountNo=0
    def createaccount(self):
        self.Name=input("Enter Account Holder Name : ")
        self.Amount=int(input("Enter your Amount : "))
        self.Address=input("Enter your Address : ")
        self.AccountNo=int(input("Enter your Account Number :"))
    def display(self):
        print("---------your Account Information-----------")
        print("Account Holder Name : ",self.Name)
        print("Amount : ",self.Amount)
        print("Address : ",self.Address)
        print("Account number : ",self.AccountNo)
def main():
    exc=Bank_Account()
    exc.createaccount()
    exc.display()
if __name__=="__main__":
    main()