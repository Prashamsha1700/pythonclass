# stores data  in key-value pairs
# mutable (can be changed)
# keys must be unique
# values can be any data type
student ={
    "name": "Ram",
    "age": 20,
    "class": 10
}

print(student["name"])
print(student["age"])
# student["name"] ="ABC School"
# print(student)
# # student["age"] = 21

# print(student)
# del student["class"]
 
# print(student)

# print(student.keys())     #ALL keys
# print(student.values())   #ALL values
print(student.items())    #Key-value pairs