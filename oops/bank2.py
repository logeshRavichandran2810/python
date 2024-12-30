class Bank_Account:
    Bankname="HDFC Bank"
    ROI=5
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
    @classmethod
    def DisplayBankInfo(cls):
        print("-------Display Bank Info-------")
        print("Bank Name : ",cls.Bankname)
        print("ROI : ",cls.ROI)
    @staticmethod
    def DisplayKycInfo():
        print('Submit following Documents')
        print('1. Aadhar Card')
        print('2. Passport')
def main():
    # print("Bank name : ",Bank_Account.Bankname)
    Bank_Account.DisplayBankInfo()
    Bank_Account.DisplayKycInfo()
    exc=Bank_Account()
    exc.createaccount()
    exc.display()
if __name__=="__main__":
    main()