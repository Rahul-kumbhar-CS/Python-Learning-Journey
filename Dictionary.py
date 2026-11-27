#Dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed. 
#In Python, dictionaries are defined using curly braces {}.
#Each key-value pair in a dictionary is separated by a colon (:), and each pair is separated by a comma (,). 
#The keys in a dictionary must be unique and immutable, while the values can be of any data type and can be duplicated.
dict1={"name":"Rahul","age":25,"city":"Belagavi"}
print(type(dict1))
print(dict1)
print(dict1["name"])  #This will return the value associated with the key "name", which is "Rahul".

#Dictionary methods:
print(dict1.keys())  #This returns all the keys in the dictionary as a view object.
print(dict1.values())    #This returns all the values in the dictionary as a view object.
print(dict1.items())    #This returns all the key-value pairs in the dictionary as a view object of tuples.
print(dict1.get("age"))  #This will return the value associated with the key "age", which is 25.
print(dict1.pop("city"))  #This will remove the key-value pair with the key "city" from the dictionary and return its value, which is "Belagavi".
print(dict1)  #This will print the updated dictionary after removing the key-value pair with the key "city".
dict1.update({"age":26})  #This will update the value associated with the key "age" to 26.
print(dict1)
dict1.clear()  #This will remove all key-value pairs from the dictionary, making it an empty dictionary.
print(dict1)  #This will print the empty dictionary after clearing all key-value pairs.
dict1.copy()  #This will return a shallow copy of the dictionary, which is a new dictionary with the same key-value pairs as the original dictionary.
print(dict1)  #This will print the original dictionary after making a copy of it.
print(dict1.setdefault("gender","Male"))  #This will add a new key-value pair with the key "gender" and the value "Male" to the dictionary if the key does not already exist. If the key already exists, it will return its value.