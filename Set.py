#Set is a collection of unique elements. It is unordered and mutable. 
# Sets are defined using curly braces {} or the set() function.
set={1,2,3,4,5,6,8}
print(type(set))
set.add(7)      #This will add the element 7 to the set. If the element already exists in the set, it will not be added again.
set.remove(4)   #This will remove the element 4 from the set. If the element does not exist in the set, it will raise a KeyError.
set.discard(5)  #This will remove the element 5 from the set.
print(set.pop())      #This will remove and return an arbitrary element from the set. If the set is empty, it will raise a KeyError.  
print(set)  #This will print the empty set after clearing all elements.

set2={2,4,6,8}
print("\n")
print(set2)
print(set.union(set2))  #This will return a new set that contains all unique elements from both sets.
print(set.intersection(set2))     #This will retunr a new set that contains only the elements that are common to both sets.
print(set.difference(set2))   #This will return a new set that contains only the elements that are in the first set but not in the second set.
print(set.symmetric_difference(set2))  #This will return a new set that contains only the elements that are in either of the sets but not in both.
print(set2.issubset(set))  #This will return True if the first set is a subset of the second set, meaning that all elements of the first set are also in the second set.
