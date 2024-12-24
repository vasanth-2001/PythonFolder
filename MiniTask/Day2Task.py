#Accessing value
fruits=['mango',['fruitpulp','mixedpulp'],'banana',('apple','grapes')]
print(fruits[0])
print(fruits[1])
print(fruits[1][0])
print(fruits[1][1])
print(fruits[3][0])
print(fruits[3][1])


# Iterate over a for loop using range function
menu=['Panner','chindamani chicken','mutton biriyani','Pepper fry','Dosa','poori']
author_name=('j k rowling','rachel aaron','hans aanrud','verna aardema')

for i in range(len(menu)):
    print(menu[i])
print('*'*100)
for i in range(len(author_name)):
    print(author_name[i])


timing='It\'s 7.30am'
for i in range(len(timing)):
    print(timing[i])
    

#Take input from user and display as shown below

EmployeeName=input("Enter Employee Name : ")
EmployeeSalary=int(input("Enter Salary : "))
Company=input("Company : ")

print(EmployeeName," ",EmployeeSalary," ",Company)


#Based on string
print('print(\'Hello World\')')
print('\'E:\ChangePondNewBatch\Python\'')

# Based on List
# create a dynamic list which contains 5 elementsof float type 
floatList=[]
size=int(input("Enter the no of float value: "))
print("Enter the float values")
for i in range(size):
    floatList.append(float(input()))
print(floatList)

# create a dynamic list which contains 5 elementsof string type 
stringList=[]
size=int(input("Enter the no of String value: "))
print("Enter the String values")
for i in range(size):
    stringList.append(str(input()))
print(stringList)

# iterate over a while loop

menu=['Panner','chindamani chicken','mutton biriyani','Pepper fry','Dosa','poori']
author_name=('j k rowling','rachel aaron','hans aanrud','verna aardema')
timing='It\'s 7.30am'
i=0
while(i<len(menu)):
    print(menu[i])
    i+=1

while(i<len(author_name)):
    print(author_name[i])
    i+=1

while(i<len(timing)):
    print(timing[i])
    i+=1


# Range Function(for loop/while loop)
for i in range(3,16,3):
    print(i,end=" ")
print()
for i in range(12,0,-3):
    print(i,end=" ")
i=3

while i in range(16):
    print(i,end=" ")
    i=i+3
print()
i=12
while i in range(1,13):
    print(i,end=" ")
    i=i-3


# List Method:
menu=['Panner','chindamani chicken','mutton biriyani','Pepper fry','Dosa','poori']
menu[4]='Chappati'
print(menu)
menu[0:2]='idly','ragi'
print(menu)


#iterate over a foor loop
fruits=['mango',['fruitpulp','mixedpulp'],'banana',('apple','grapes')]
for i in range(len(fruits)):
    print(fruits[i])