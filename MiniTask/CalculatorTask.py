
def add(value1,value2):
    return value1+value2
def sub(value1,value2):
    return value1-value2
def Mul(value1,value2):
    return value1*value2
def Div(value1,value2):
    return value1/value2
def exp(value1,value2):
    return value1**value2

def main():
    Number1=int(input('Enter the Number 1: '))
    Number2=int(input('Enter the Number 2: '))
    print('1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Exponent')
    userValue=int(input())
    if userValue==1:
        print('Add:',add(Number1,Number2))
    elif userValue==2:
        print('Sub:',sub(Number1,Number2))
    elif userValue==3:
        print('Multiplication:',Mul(Number1,Number2))
    elif userValue==4:
            print('Division:',Div(Number1,Number2))
    elif userValue==5:
        print('Exponential:',exp(Number1,Number2))
    else:
        print('Invalid option....')
main()