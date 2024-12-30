def count(ListValue,search):
    count=0
    for i in range(len(ListValue)):
        if(search==ListValue[i]):
            count=count+1
    return count
def main():
    length=int(input("How many number you want too add in list : "))
    ListValue=[]
    print('enter the values')
    for i in range(length):
        ListValue.append(int(input()))
    search =int(input("what number you want to search"))
    print(search," is repeating in",count(ListValue,search),"times")
if __name__ == "__main__":
    main()