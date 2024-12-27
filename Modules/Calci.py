import arithmetic

print('Enter the operator 1/2/3')
select =int(input())
def main():
    num1=int(input('Enter First Number : '))
    num2=int(input('Enter SECOND Number : '))
    if(select==1):
        print("add :,",arithmetic.add(num1,num2))
    elif(select==2):
        print("sub :,",arithmetic.sub(num1,num2))
    elif(select==3):
        print("mul :,",arithmetic.Mul(num1,num2))

if __name__ =='__main__':
    main()