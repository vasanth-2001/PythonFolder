# set method:
# we can't accessing set by using index
mixed_type={True,12,34}
# add : will add an element
mixed_type.add('vasanth')
print('add method',mixed_type)

#discard/pop/remove
# discard_method=mixed_type.discard('vasanth')  
# print('Discard method :',mixed_type)
# discard_method=mixed_type.remove('vasanth')
# print('remove method :',mixed_type)
discard_method=mixed_type.pop()     # it will remove any value randomly
print('pop method :',mixed_type)

#intersection
company={'Cognizant','Infosy','ChangePond','TCS'}
itcompany={'TATA','Infosy','Neosoft','TCS'}

inter_method=company.intersection(itcompany)
print('intersection method',inter_method)

# intersection using operator
inter_method=company&itcompany
print('intersection method using operator',inter_method)

#union
union_method=company.union(itcompany)
print('union method',union_method)

#union using operator
union_method=company | itcompany
print('union method using operator',union_method)

# upadate method -->
company={'Cognizant','Infosy','ChangePond','TCS'}
print(company)
update_com={'fedielity','ZOHO'}
company.update(update_com)
print('update method :',company)

#difference ()
fruit={'apple','orange','grapes','pineapple'}
morefruit={'watermelon','grapes','apple','jackfruit'}
diff_method=fruit.difference(morefruit)
print("difference method :",diff_method)

#difference using operator
diff_method=morefruit - fruit
print("difference method using operator:",diff_method)