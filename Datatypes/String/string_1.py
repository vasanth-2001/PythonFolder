statement1='Good Morning'   #single quotes
statement2="Good Afternoon" #double quotes
statement3='''

            Good Evening to all

'''  # multiline statement use triple quotes

print(len(statement1))
# print(index('o'))

for i in range(2,7):
    print(statement2[i])

print("slicing : ",statement1[5:])

#using different quotes in same statement
# timing ='It"s 12.10pm'
# print('using different quotes in different statement',timing)

#using same quotes in same statement
# timing ='It\'s 12.10pm'
# print('using different quotes in same statement',timing)


name='VASANTH'
age=23
print(name+" "+str(age))

print(f'My name is {name} {age} years old')