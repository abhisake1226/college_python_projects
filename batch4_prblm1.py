"""Write a Python function to remove all occurrences of a given item from a list. 
 Write a Python function that takes two lists and returns True  if they have at least one common members"""


def remove_all_occurrences(lst, item):
    while item in lst:
        lst.remove(item)


def have_common_member(list1, list2):
    return any(item in list2 for item in list1)


# Test the function
my_list = [1, 2, 3, 4, 2, 5, 2]
print("Original list:",my_list)
remove_all_occurrences(my_list, 2)
print("List after removing all occurrences of 2:", my_list)

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print("Do lists have at least one common member?", have_common_member(list1, list2))

