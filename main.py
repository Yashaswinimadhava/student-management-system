
import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read student data. Starting empty.")
    return {}


students = load_students()


def save_students():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter student name: ").strip()
    age_text = input("Enter age: ").strip()
    course = input("Enter course: ").strip()
    marks_text = input("Enter marks (0-100): ").strip()

    try:
        age = int(age_text)
        marks = float(marks_text)
        if age <= 0 or not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Please enter a positive age and marks from 0 to 100.")
        return

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }
    save_students()
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    for student_id, details in students.items():
        print(f"\nID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Course: {details['course']}")
        print(f"Marks: {details['marks']}")


def search_student():
    student_id = input("Enter student ID to search: ").strip()

    if student_id in students:
        print("\nStudent details:")
        for key, value in students[student_id].items():
            print(f"{key.title()}: {value}")
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter student ID to update: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    print("Press Enter to keep the current value.")

    name = input(f"Name [{student['name']}]: ").strip()
    age_text = input(f"Age [{student['age']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    marks_text = input(f"Marks [{student['marks']}]: ").strip()

    try:
        age = int(age_text) if age_text else student["age"]
        marks = float(marks_text) if marks_text else student["marks"]
        if age <= 0 or not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Invalid age or marks. No changes saved.")
        return

    student["name"] = name or student["name"]
    student["age"] = age
    student["course"] = course or student["course"]
    student["marks"] = marks

    save_students()
    print("Student updated successfully!")


def delete_student():
    student_id = input("Enter student ID to delete: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    confirm = input("Are you sure? (yes/no): ").strip().lower()
    if confirm == "yes":
        del students[student_id]
        save_students()
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
