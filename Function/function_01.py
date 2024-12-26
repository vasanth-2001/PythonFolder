def Demo():
    print('Inside Demo')

def Demo_01(value):
    print('Inside Demo 01:',value)

def Demo_02(value1,value2):
    print('Inside Demo 02 :',value1,value2)

def Demo_03(value1,value2):
    print('Inside Demo 03:',value1,value2)
    Add=value1+value2
    sub=value1-value2
    return Add,sub

def main():
    Demo()
    Demo_01(10)
    Demo_02(20,30)
    calculation=Demo_03(100,50)
    print("addition of 100 and 50 is :",calculation[0])
    print("subtraction of 100 and 50 is :",calculation[1])


if __name__ == '__main__':
    main()