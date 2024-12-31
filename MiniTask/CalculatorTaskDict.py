def add(num1,num2):
    return f'Addition: {num1+num2}'
def sub(num1,num2):
    return f'Subtraction: {num1-num2}'
def mul(num1,num2):
    return f'Multiplication: {num1*num2}'
def div(num1,num2):
    return f'Division: {num1/num2}'





def main():
    print('1.+','2.-','3./','4.*',end='\n')
    option=int(input('Enter the option: '))
    value1=int(input('Enter the value1: '))
    value2=int(input('Enter the value2: '))
    operation={1:add,2:sub,3:div,4:mul}
    if option==1:
        print(operation[1](value1,value2))
    elif option==2:
        print(operation[2](value1,value2))
    elif option==3:
        print(operation[3](value1,value2))
    elif option==4:
        print(operation[4](value1,value2))
main()