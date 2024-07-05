my_dict = {'Ivan': 1999, 'Elena': 1997, 'Angelina':2005}

print(my_dict)
print(my_dict ['Ivan'])
print(my_dict.get ('Alexandr'))
my_dict.update({'Elvira': 1977, 'Alexey': 1976})
print(my_dict)
del my_dict['Angelina']
print(my_dict)

my_set = {1,1,3,3,4,4,4,4,4,8,8}
print(my_set)
my_set.update ({14,15})
print(my_set)
my_set.discard(4)
print(my_set)
