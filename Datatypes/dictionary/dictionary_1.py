# # create a Dictionary
# watch_details ={
#     'Titan':6000,
#     'Fastrack':6000,
#     'Sonata':2000,
#     'Noise':6000,
#     'Titan':8000
# }
# print('Dictionary :',watch_details)
# print('Length :',len(watch_details))
# print('Accessing Values:',watch_details['Fastrack'])

# # Mutable object
# watch_details['Noise']=7000
# print('Modifying value :',watch_details)

employe_details ={
    'Name' :'Shubham',
    'jobid':123,
    'is_active':True,
    'package':7.5
}
print('Get Method :',employe_details.get('is_active'))  # it is use to get the values by using keys
print('Keys Method :',employe_details.keys())  #this method is use to get the all keys in list format
print('values Method :',employe_details.values())   #this method is use to get the all vlaues in list format
print('items Method :',employe_details.items())   # this method is use to get both keys and values in list format
pop_item=employe_details.popitem()   
print('popitem method:',employe_details)
pop=employe_details.pop('Name')
print('popitem method:',employe_details)
employe_details.update({2.4:'package'})
print('Update :',employe_details)


