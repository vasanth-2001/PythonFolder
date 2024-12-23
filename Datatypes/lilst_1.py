# collection of values
# create a list 
employee_id=[101,102,103,101] #Homogeneous/same value,allow duplilcates
print('List of id',employee_id)
mixed_type=['Shubham',123,89.9,True]
#hetrogeneous/different type
print('Employee :',mixed_type)

#Index:Access value
#positive index(base 0)
#Negative index(-1)

print('Accessing value of 0th position:',mixed_type[0])
print('Accessing value of 1th position:',mixed_type[1])
print('Accessing value of 2th position:',mixed_type[2])
print('Accessing value of 3th position:',mixed_type[3])

#len()-->return sizee of the object
print('size',len(mixed_type))

# Accessing from negative index 
print('Accessing value of 3th position:',mixed_type[-1])
print('Accessing value of 2th position:',mixed_type[-2])
print('Accessing value of 1th position:',mixed_type[-3])
print('Accessing value of 0th position:',mixed_type[-4])

