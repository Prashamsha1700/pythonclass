#reverse string
my_string ="Hello"
rev = my_string[::-1]
print(rev)

#to rev without slicing
string = "Hello"
rev =""
for char in string:
    rev = char + rev
    print(rev)