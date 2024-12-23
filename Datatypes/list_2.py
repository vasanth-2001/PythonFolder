# mixed_type =['shubham',45,89.67,True]

# #slicing :[start:stop(excluded)]

# print("sllicing",mixed_type[1:4])
# print("sllicing",mixed_type[1:])

# # List is a mutable object 

# mixed_type[3]=False
# print('Modifying:',mixed_type)
# mixed_type[0:3]='Aditya',23,9.3
# print('using Slicing:',mixed_type)
# del mixed_type[2]
# print('Final List:',mixed_type)


#Method

fruits=['Mango','Banana']

#append => add an element in the last
fruits.append('Orange')
print("Append Method" ,fruits)

#insert()  => adds an element at the specified position
fruits.insert(1,'Grapes')
print("insert Method:",fruits)

#extend() =>Add the list of element(or iterable values) at the current list
fruits.extend(['blackcurrent','blueberry'])
print("extend Method :",fruits)
# fruits.extend('pineapple')
# print("extend Method :",fruits)

# fruits.extend(True)                # Error
# print("extend Method :",fruits)



#pop() => removes the element of the specified position
fruits.pop(0)
print('using pop method : ',fruits)
#remove()
fruits.remove('blackcurrent')
print('using remove method : ',fruits)
city=['Mumbai','Chennai','Delhi','Chennai']
# city.remove('Chennai')
# print('Remove Method : ',city)
print(city)
index_method=city.index('Chennai')
print('Index Method',index_method)
#count
count_method =city.count('Chennai')
print('Count Method :',count_method)