# Dictionary to store student names and CGPA
students = {}

# Input student names and CGPA
for i in range(1, 11):
    name = input(f"Enter full name of student {i}: ")
    cgpa = float(input(f"Enter CGPA of student {i}: "))
    students[name] = cgpa

# (a) Print names as initials with surname
print("(a) Names as initials with surname:")
for name in students.keys():
    first_initial = name[0]
    last_name = name.split()[-1]
    print(f"{first_initial}. {last_name}")

# (b) Display details of student with highest CGPA
print("\n(b) Details of student with highest CGPA:")
highest_cgpa_student = max(students, key=students.get)
print(f"Name: {highest_cgpa_student}, CGPA: {students[highest_cgpa_student]}")

# (c) Display names of students with CGPA below 3.0
print("\n(c) Names of students with CGPA below 3.0:")
below_3_cgpa_students = [name for name, cgpa in students.items() if cgpa < 3.0]
if below_3_cgpa_students:
    for name in below_3_cgpa_students:
        print(name)
else:
    print("No student has CGPA below 3.0.")
