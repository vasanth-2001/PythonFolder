class Bank_Account:
    BankName='Hdfc Bank' #class variable
    ROI=5
    def __init__(self):
        self.Name=""    #instance variable
        self.Amount =0
        self.Address=""
        self.AccountNo=0

    def CreateAccount(self):    #instance method
        self.Name=input('Enter the Account Holder Name : ')
        self.Amount = int(input('Enter the Amount'))
        self.Address = input('Enter the Address')
        self.AccountNo=int(input('Enter Account Number'))
    
    def DisplayInformation(self):
        print("---------your Account Information-------")
        print('Account Holder Name : ',self.Name)
        print("Amount : ",self.Amount)
        print("Address : ",self.Address)
        print("AccountNo : ",self.AccountNo)

    @classmethod
    def DisplayBankInfo(cls):
        print('-------Display Bank Info-------')
        print('Bank Name',cls.BankName)
        print('ROI in FD',cls.ROI)
    @staticmethod
    def DisplayKYCInforamation():
        print('submit following Documents')
        print('1.Aadhar Card')
        print('2.Passport size photo')
        print('2.Passport size photo')
        print()

def main():
    # user_1=Bank_Account()
    # print('Creating First Account :')
    # user_1.CreateAccount()
    # user_1.DisplayInformation()
    # print()
    # user_2=Bank_Account()
    # print('Creating Second Account :')
    # user_2.CreateAccount()
    # user_2.DisplayInformation()
    # print()
    print(Bank_Account.BankName)
    Bank_Account.DisplayBankInfo()
    Bank_Account.DisplayKYCInforamation()
    
if __name__ == '__main__':
    main()