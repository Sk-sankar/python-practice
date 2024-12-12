
class_list = []

def adding_student():
    name = input("Enter name of the student: ")
    qualification = input("Enter the qualification: ")
    age = int(input("Enter the age of the student: "))


    while True:
        student_number = input("Enter the student phone number (10 digits): ")
        if len(student_number) == 10 and student_number.isdigit():
            student_number = int(student_number)
            break
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")

    parent_name = input("Enter the parent name: ")

    while True:
        parent_number = input("Enter the parent's phone number (10 digits): ")
        if len(parent_number) == 10 and parent_number.isdigit():
            parent_number = int(parent_number)
            break
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")

    date_of_joining = input("Enter the date of joining: ")

    student = {
        "name": name,
        "qualification": qualification,
        "age": age,
        "student_number": student_number,
        "parent_name": parent_name,
        "parent_number": parent_number,
        "date_of_joining": date_of_joining
    }
    class_list.append(student)
    print(f"Student {name} added successfully!\n")


def view_students():
    if not class_list:
        print("No students in the class.\n")
    else:
        print(f"{'Name':<20} {'Qualification':<20} {'Age':<5} {'Student Number':<15} {'Parent Name':<20} {'Parent Number':<15} {'Date of Joining':<15}")
        print("-" * 155)
        for student in class_list:
            print(f"{student['name']:<20} {student['qualification']:<20} {student['age']:<5} {student['student_number']:<15} {student['parent_name']:<20} {student['parent_number']:<15} {student['date_of_joining']:<15}")
        print()

def remove_student():
    student_name = input("Enter the name or student number of the student to remove: ")
    for student in class_list:
        if student_name.lower() == student['name'].lower() or student_name == str(student['student_number']):
            class_list.remove(student)
            print(f"Student {student['name']} removed successfully!\n")
            return
    print(f"No student found with name or student number '{student_name}'.\n")

def main_menu():
    while True:
        print("Classroom Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Remove Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            adding_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            print("Exiting the Classroom Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main_menu()
