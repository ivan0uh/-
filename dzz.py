def print_params(a=1, b="строка", c=True):
    print(a, b, c)


values_list = [12, "stone", False]
values_dict = {"a": 2, "b": 3, "c": 5}

print_params(**values_dict)
print_params(*values_list)

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)
