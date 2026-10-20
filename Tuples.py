#tuple is built in data type in python which is used to store multiple items in a single variable.
#Tuples are created using parentheses () and it is immutable, meaning that once a tuple is created, its elements cannot be changed, added, or removed.
tup=(1,2,3,"apple",3.14,3)
print(type(tup))
print(tup)     #output: (1, 2, 3, 'apple', 3.14, 3)
print(tup.index(2))  #This will return the index of the first occurrence of 2 in the tuple, which is 1.
print(tup.count(3))  #This will return the number of occurrences of 3 in the tuple, which is 2.
print(tup)