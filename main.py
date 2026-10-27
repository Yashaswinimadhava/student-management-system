
students = {}

def add_student():
    student_id = input("Enter student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    for student_id, details in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])
        print("Marks:", details["marks"])


def search_student():
    student_id = input("Enter student ID to search: ")

    if student_id in students:
        print(students[student_id])
    else:
        print("Student not found.")


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
