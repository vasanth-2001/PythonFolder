
class Bank:
    def __init__(self):
        self.main_balance=50000
    def withDraw(self):
        Withdraw_amount=int(input('Enter the amount to withdraw: '))
        self.main_balance-=Withdraw_amount
        return f'The amount with drawn: {Withdraw_amount} main balance is: {self.main_balance}'
    def availableAmount(self):
        return f'The available amount is {self.main_balance}'
    def DepositAmount(self):
        amount=int(input('Enter the amount to deposit: '))
        self.main_balance+=amount
        return f'The available balance is: {self.main_balance}'

def main():
    obj1=Bank()
    print('1.withdraw\n2.available amount\n3.deposit amount')
    user_input=int(input('Enter the choice: '))

    if user_input==1:
        print(obj1.withDraw())
    elif user_input==2:
        print(obj1.availableAmount())
    elif user_input==3:
        print(obj1.DepositAmount())
    else:
        print('Invalid option...')

if __name__=='__main__':
    main()