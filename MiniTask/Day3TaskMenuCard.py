menuCard = ['Dosa','Idly','Biriyani']

def display():
    for i in range(len(menuCard)):
        print(menuCard[i])

def add(value):
    menuCard.append(value)
    print('Dish added successfully')
    display()

def update(preValue,updateValue):
    for i in range(len(menuCard)):
        if(menuCard[i]==preValue):
            indexNum = menuCard.index(preValue)
            menuCard.remove(preValue)
            menuCard.insert(indexNum, updateValue)
            display()
            print('Dish updated successfully')
            return
        
    print('Enter a correct food item which you replace')

def delete(value):
    for i in range(len(menuCard)):
        if(menuCard[i]==value):
            deleteIndex = menuCard.index(value)
            menuCard.pop(deleteIndex)
            display()
            print('Item deleted successfully')
            return
    print('Enter a correct item to delete')       

def main():

    print('Select an option:\n','1.Display\n','2.Add\n','3.Update\n','4.Delete\n')
    number = int(input())
    if(number==1):
        display()
    elif(number==2):
        value = input('what you want to add in menucard:')
        add(value)
    elif(number==3):
        display()
        preValue = input('which item want  to update:')
        updateValue = input('Enter new item to replace:')
        update(preValue,updateValue)
    elif(number==4):
        deletevalue = input('Which item you want to delete:')
        
        delete(deletevalue)
        

if __name__ == '__main__':
    main()

