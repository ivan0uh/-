immutable_var = ([1,2],3,4,5,6,7)
print(immutable_var)
immutable_var [0][0]=3 #можно изменять только изменямые значения, как я понял списки внутри кортеджей заключенные в []
print(immutable_var)

mutable_list = [1,2,3,'клесо']
mutable_list[3] = 4
print(mutable_list)