def recursive_hcf(a, b):
    '''Recursive function to find the H.C.F. of two numbers'''
    if b==0:
        return a
    else:
        return recursive_hcf(b, a%b)


def find_hcf_of_elements(intlist):
    '''Function to find the HCF of the first and fifth elements of a list.'''
    try:
        first_element = intlist[0]
        fifth_element = intlist[4]

        hcf = recursive_hcf(first_element, fifth_element)
        print(f"HCF of the {first_element} and {fifth_element} is :{hcf}")

    except (NameError, IndexError):
        print("Error: Please provide a valid list with at least 5 integers.")
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
    except ValueError:
        print("Error: Invalid value in the list . Please provide integers only.")

if __name__=="__main__":
    try:
        intlist = list(map(int,input("Enter a list of itergers separated by space:").split()))

        #check if the list has atleast 5 elements
        if len(intlist)>=5:
            find_hcf_of_elements(intlist)
        else:
            print("Error: Please provide a valid list with at least 5 integers.")

    except ValueError:
            print("Error: Invalid value in the list . Please provide integers separated by space.")
