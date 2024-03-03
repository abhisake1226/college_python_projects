def main():
    #input two stes of city names
    S1 = set(input("Enter names of cities for set S1 (separated by spaces): ").split())
    S2 = set(input("Enter names of cities for set S2 (separated by spaces): ").split())

    #find union, intersection, and symmetric difference of the two sets
    union_set = S1.union(S2)
    intersection_set = S1.intersection(S2)
    symmetric_difference_set = S1.symmetric_difference(S2)

    #Display union, intersection, and symmetric difference
    print("Union of S1 and S2: ",union_set)
    print("Inetrsection of S1 and S2: ",intersection_set)
    print("Symmetric difference of S1 and S2: ",symmetric_difference_set)

    #Display elements of S1 in upper case and S2 in lower case
    print("Elements of S1 in upper case:")
    for city in S1:
        print(city.upper())

    print("Elements of S2 in lower case:")
    for city in S2:
        print(city.lower())


if __name__=="__main__":
    main()
