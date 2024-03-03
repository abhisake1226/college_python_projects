#QuickSort
def quicksort(arr):
    if len(arr)<= 1:
        return arr
    else:
        pivot=arr[0]
        less_than_pivot = [x for x in arr[1:] if x<=pivot]
        greater_than_pivot = [x for x in arr[1:] if x> pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

    #test the function

arr = list(map(int, input("Enter elements in array separated by spaces.").split()))
sorted_arr = quicksort(arr)

print("Sorted Array: ",sorted_arr)
