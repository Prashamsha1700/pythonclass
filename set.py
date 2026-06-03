S={1,2,3,4}
# A set is a collection of unique items.
#unordered 
# No duplicate values
fruits ={"apple", "banana", "mango"}
print(fruits)
print(type(fruits))
numbers ={1, 2, 3, 4, 4, 5}
print(numbers)
colors ={"red", "blue", "green"}
print(colors)

fruits ={"apple", "banana"}

fruits.add("mango")
numbers ={1, 1, 2, 2, 3, 3}
print(numbers)

#to remove an item from a set, we can use the remove() method
fruits.remove("banana")

print(fruits)

#to vlear a set , we can use the clear() method 
fruits.clear()

print(fruits)
 
 for item  fruits:
    print(item)


    nums = (1,2,2,3,3,4,5)
    unique_nums = set(nums)

    print(unique_nums)