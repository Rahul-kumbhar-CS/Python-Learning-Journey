#WAP to check if a list contains a palindrome elements or not.
#1.[1,2,3,2,1]
#2.[1,"abc","abc",1]

#1.:-
list=[1,2,3,2,1]
copy_list=list.copy()
copy_list.reverse()
if(list==copy_list):
    print("The list contains palindrome elements.")
else:
    print("The list does not contain palindrome elements.")

#2.:-
print("\n#2.:")
list2=[1,"abc","abc",1]
copy_list2=list2.copy()
copy_list2.reverse()
if(list2==copy_list2):
    print("The list contains palindrome elements.")
else:
    print("The list does not contain palindrome elements.")