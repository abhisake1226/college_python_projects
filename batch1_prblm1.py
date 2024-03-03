#write a Python function expanding (numlist), that takes as argument a list of integers, numlist[], and returns True if the absolute difference between each adjacent pair
#of elements strictly decreases; and False otherwise. Write a driver program to test the function. The function should handle necessary validation checks.
# Example: [2,3,5,9,15,24] returns False
#[2,3,4,6] returns False
#[2,10,16,20] returns True

def expanding (numlist):
    if len(numlist)<2:
        print("Error: List must contain at least two elements..")
        return False
    prev_dif = abs(numlist[1]-numlist[0])
    for i in range(2,len(numlist)):
        cur_dif = abs(numlist[i]-numlist[i-1])
        if cur_dif >= prev_dif:
            return False
        prev_dif = cur_dif
    return True
#driver program
num_list1 = [1,3,7,2,9]
num_list2 = [5,1,4,6,7]
result1 = expanding(num_list1)
result2 = expanding(num_list2)
print("Result for num_list1: ",result1)
print("Result for num_list2: ",result2)