def main():
    set1 = set(map(int, input("Enter elements of first set separated by spaces: ").split()))
    set2 = set(map(int, input("Enter elements of second set separated by spaces: ").split()))

    # Union operation
    union_set = sorted(set1.union(set2))
    print("Union of set1 and set2:", union_set)

    # Intersection operation
    intersection_set = sorted(set1.intersection(set2))
    print("Intersection of set1 and set2:", intersection_set)

    # Set difference operation
    difference_set = sorted(set1.difference(set2))
    print("Difference of set1 and set2:", difference_set)

    #Python program to find the maximum number in a set:
    my_set = set(map(int, input("Enter elements of the set separated by spaces: ").split()))
    max_number = find_max_number(my_set)
    print("Maximum number in the set:", max_number)


def find_max_number(my_set):
    if len(my_set) == 0:
        return None
    else:
        return max(my_set)



if __name__ == "__main__":
    main()


