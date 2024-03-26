from datetime import date

students_details = {}


def handle_student_details():
    for _ in range(2):
        student_id = input("Enter the student ID (or 'q' to quit): ")
        if student_id == 'q':
            break

        if student_id not in students_details:
            name = input("Enter the student name: ")
            students_details[student_id] = {"name": name}
            print("Student details added successfully.")
        else:
            print("Student ID already exists. Please try again.")
        print()


def handle_subjects():
    subjects = {}
    while True:
        course_code = input("Enter the course code (or 'q' to quit): ")
        if course_code == 'q':
            break

        course_name = input("Enter the course name: ")
        subjects[course_code] = course_name
        print("Subject added successfully.")
        print()

    return subjects


def enter_marks(subjects):
    student_id = input("Enter the student ID: ")
    if student_id in students_details:
        student = students_details[student_id]
        entered_subjects = set()
        while entered_subjects != set(subjects.keys()):
            course_code = input("Enter the course code: ")
            if course_code not in subjects:
                print("Invalid course code. Please enter a valid course code.")
                print()
                continue

            mark = int(input("Enter the mark for course {} of student with ID {}: ".format(course_code, student_id)))
            student[course_code] = mark
            entered_subjects.add(course_code)
    else:
        print("Invalid student ID. Please try again.")


def generate_report_card(subjects):
    student_id = input("Enter the student ID: ")
    if student_id in students_details:
        student = students_details[student_id]
        report_card = f"""\
        ---------------------------
        {student["name"]}'s Report Card
        ---------------------------
        School: USIU-Africa
        Education to take you places
        Date: {date.today()}
        Student ID: {student_id}
        Student Name: {student["name"]}

        Marks:
        """
        total_marks = 0
        for course_code, mark in student.items():
            if course_code != "name":
                course_name = subjects.get(course_code, "Unknown")
                report_card += f"{course_name} ({course_code}): {mark}\n"
                total_marks += mark
        average_marks = total_marks / len(subjects)
        report_card += f"\nAverage Marks: {average_marks}\n"
        if average_marks >= 80:
            report_card += "Recommendation: Excellent\n"
        elif average_marks >= 60:
            report_card += "Recommendation: Good\n"
        else:
            report_card += "Recommendation: Needs Improvement\n"
        report_card += "---------------------------\n"
        print(report_card)
    else:
        print("Student ID not found. Please try again.")


def print_report_card(subjects):
    for student_id, student in students_details.items():
        print("Student ID: {}".format(student_id))
        print("Student Name: {}".format(student["name"]))
        print("Marks:")
        total_marks = 0
        for course_code, mark in student.items():
            if course_code != "name":
                course_name = subjects.get(course_code, "Unknown")
                print("{} ({}): {}".format(course_name, course_code, mark))
                total_marks += mark
        average_marks = total_marks / len(subjects)
        print("Average Marks: {}".format(average_marks))
        if average_marks >= 80:
            print("Recommendation: Excellent")
        elif average_marks >= 60:
            print("Recommendation: Good")
        else:
            print("Recommendation: Needs Improvement")
        print()


def main():
    subjects = {}
    while True:
        print("----- STUDENT REPORT CARD SYSTEM -----")
        print("1. Enter Student Details")
        print("2. Enter Subjects")
        print("3. Enter Marks")
        print("4. Generate Report Card")
        print("5. Print Report Card")
        print("6. Quit")
        print()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            handle_student_details()
        elif choice == "2":
            subjects = handle_subjects()
        elif choice == "3":
            enter_marks(subjects)
        elif choice == "4":
            generate_report_card(subjects)  # Pass the subjects dictionary as an argument
        elif choice == "5":
            print_report_card(subjects)  # Pass the subjects dictionary as an argument
        elif choice == "6":
            print("Thank you for using the Student Report Card System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()