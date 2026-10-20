#List is a built in data type in python which is used to store multiple items in a single variable. 
# Lists are created using square brackets [] and can contain elements of different data types.
my_list=[1,4,5,"apple",3.14]
print(my_list)     #output: [1, 4, 5, 'apple', 3.14]
print(my_list[0])  #output: 1
print(my_list[4])  #List indexing starts from 0, so this will output: 3.14
print(my_list[-2])  #Negative indexing starts from the end of the list, so this will output: 3.14
print(my_list[0:4])  #List slicing, this will output: [1, 4, 5, 'apple']
print(my_list[1:])  #This will output: [4, 5, 'apple', 3.14]
print(my_list)


#List methods:
print("List methods:")
my_list.append("banana")   #This will add "banana" to the end of the list.
print(my_list)
#my_list.sort()    #This will sort the list in ascending order. However, since the list contains different data types, it will raise a TypeError. To sort a list, all elements must be of the same data type.
my_list2=[1,2,3,5,4]
print(my_list2)
my_list2.sort()  
print(my_list2) 
my_list2.sort(reverse=True)      #This will sort the list in descending order.
print(my_list2)
my_list2.reverse()  #This will reverse the order of the list.
my_list2.insert(2,6)  #This will insert 6 at index 2.
print(my_list2)
my_list2.remove(3)  #This will remove the first occurrence of 3 from the list.
my_list2.pop(4)  #This will remove the element at index 4 and return it.
print(my_list2) 
