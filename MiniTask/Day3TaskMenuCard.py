menuCard = ['dosa','idly','biriyani']

def display():
    for i in range(len(menuCard)):
        print(menuCard[i])

def add(value):
    menuCard.append(value)
    print('Item added successfully')
    display()

def update(oldValue,newValue):
    for i in range(len(menuCard)):
        if(menuCard[i]==oldValue):
            index = menuCard.index(oldValue)
            menuCard.remove(oldValue)
            menuCard.insert(index, newValue)
            display()
            print('Item updated successfully')
            return
        
    print('Enter a correct food item !')

def delete(value):
    for i in range(len(menuCard)):
        if(menuCard[i]==value):
            index = menuCard.index(value)
            menuCard.pop(index)
            display()
            print('Item deleted successfully')
            return
    print('Enter a correct food item !')       

def main():

    print('Select an option:','\n','1.Display','\n','2.Add','\n','3.Update','\n','4.Delete')
    number = int(input())
    if(number==1):
        display()
    elif(number==2):
        value = input('what you want to add in menucard:')
        add(value)
    elif(number==3):
        display()
        oldValue = input('Enter a value to update:')
        newValue = input('Enter a value to replace:')
        update(oldValue,newValue)
    elif(number==4):
        deletevalue = input('Enter a value to delete:')
        delete(deletevalue)
        

if __name__ == '__main__':
    main()


==========================================================================

def add(value1,value2):
    return value1+value2
def sub(value1,value2):
    return value1-value2
def Multi(value1,value2):
    return value1*value2
def Div(value1,value2):
    return value1/value2
def exp(value1,value2):
    return value1**value2

def main():
    value1=int(input('Enter the value 1: '))
    value2=int(input('Enter the value 2: '))
    print('1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Exponent')
    userValue=int(input())
    if userValue==1:
        print('Add:',add(value1,value2))
    elif userValue==2:
        print('Sub:',sub(value1,value2))
    elif userValue==3:
        print('Multiplication:',Multi(value1,value2))
    elif userValue==4:
            print('Division:',Div(value1,value2))
    elif userValue==5:
        print('Exponential:',exp(value1,value2))
    else:
        print('Invalid option....')
main()
