def longest_monotonic_chain(lst, order):
    longest_chain = []
    current_chain = [lst[0]]
    for i in range(1, len(lst)):
        if (order == "ascending" and lst[i] >= lst[i-1]) or (order == "descending" and lst[i] <= lst[i-1]):
            current_chain.append(lst[i])
        else:
            if len(current_chain) > len(longest_chain):
                longest_chain = current_chain
            current_chain = [lst[i]]
    if len(current_chain) > len(longest_chain):
        longest_chain = current_chain
    return longest_chain if len(longest_chain) > 1 else "NIL"

n = int(input("Enter the number of elements in the list: "))
lst = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
order = input("Enter 'ascending' or 'descending' for the order: ")

result = longest_monotonic_chain(lst, order)
print("Longest chain of monotonically", order, "values:", result)
