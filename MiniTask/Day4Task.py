def minimum(ListValue):
    smallest=ListValue[0]
    for i in range(len(ListValue)):
        if(ListValue[i]<smallest):
            smallest=ListValue[i]
    return smallest

def maximum(ListValue):
    # print(ListValue)
    largest=ListValue[0]
    for i in range(len(ListValue)):
        if(ListValue[i]>largest):
            largest=ListValue[i]
    return largest

def Addition(ListValue):
    add=0
    for i in range(len(ListValue)):
        add=add+ListValue[i]
    return add

def main():
    length=int(input("How many number you want too add in list : "))
    ListValue=[]
    print('enter the values')
    for i in range(length):
        ListValue.append(int(input()))
    print("Maximum Value is :",maximum(ListValue))
    print("Minimum Value is :",minimum(ListValue))
    print("Addition Value is :",Addition(ListValue))

if __name__ == '__main__':
    main()