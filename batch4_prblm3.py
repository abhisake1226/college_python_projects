#(a) Python program to find the power of a number (i.e., N^P) using recursion:

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

#(b)Program to create a function "show_employee" to accept the employee's name and salary and display both:
def show_employee(name, salary):
    print("Employee Name:", name)
    print("Employee Salary:", salary)



# Test the function
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")


employee_name = input("Enter employee's name: ")
employee_salary = float(input("Enter employee's salary: "))
show_employee(employee_name, employee_salary)
