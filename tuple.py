# to convert list into tuples
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)
my_tuple = tuple(my_string)
print(my_tuple)

# to convert tuple into string
my_tuple = ('H', 'e', 'l', 'l', 'o')

my_string =''.join(my_tuple)
print(my_string)


# to convert tuple into dict
my_tuple =(('name', 'Ram'), ('age', 20), ('class', 10))
my_dict = dict(my_tuple)
print(my_dict)


# to convert dict into list
my_dict ={"name": "Ram", "age": 20, "class": 10}
my_list = list(my_dict.items())
print(my_list)

