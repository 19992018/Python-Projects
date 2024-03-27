from datetime import date

students_details = {}


def handle_student_details():
    i = 0
    while i < 2:
        student_id = input("Enter the student ID: ")

        if student_id not in students_details:
            name = input("Enter the student name: ")
            students_details[student_id] = {"name": name}
            print("Student details added successfully.")
            i = i + 1  # *************************
        else:
            print("Student ID already exists. Please try again.")
            continue
        print()


def handle_subjects():
    subjects = {}
    num_subjects = 0  # Counter variable

    while num_subjects < 2:  # Update while loop condition
        course_code = input("Enter the course code for subject {}: ".format(num_subjects + 1))  # *******************

        if course_code in subjects:
            print("Course code already exists. Please try again.")
            continue

        course_name = input("Enter the course name for subject {}: ".format(num_subjects + 1))

        subjects[course_code] = course_name
        print("Subject added successfully.")
        print()

        num_subjects += 1  # Increment the counter

    return subjects


def enter_marks(subjects):
    while True:  # Also while x<2 would work
        student_id = input("Enter the student ID (or 'q' to finish): ")

        if student_id.lower() == 'q':
            break

        if student_id in students_details:
            student = students_details[student_id]
            entered_subjects = set(student.keys()) - {"name"}  # ********************
            remaining_subjects = set(subjects.keys()) - entered_subjects

            if len(remaining_subjects) == 0:
                print("All subjects already have marks for student with ID {}.".format(student_id))
                continue

            for course_code in remaining_subjects:  # *******************8
                mark = int(
                    input("Enter the mark for course {} of student with ID {}: ".format(course_code, student_id)))
                student[course_code] = mark

            print("Marks entered successfully for student with ID {}.".format(student_id))
            print()
        else:
            print("Invalid student ID. Please try again.")  # continue?


def generate_report_card(subjects):
    student_id = input("Enter the student ID: ")
    if student_id in students_details:
        student = students_details[student_id]
        report_card = "----------------------------------------\n"
        report_card += "                REPORT CARD               \n"
        report_card += "----------------------------------------\n"
        report_card += "USIU-AFRICA\n"
        report_card += "Date: {}\n".format(date.today())
        report_card += "Student ID: {}\n".format(student_id)
        report_card += "Student Name: {}\n\n".format(student["name"])  # ********************
        report_card += "Subjects:\n\n"
        report_card += "{:<15} {:<25} {:<10}\n".format("Course Code", "Subject Name", "Marks")  # *************
        total_marks = 0
        num_subjects = 0
        for course_code, mark in student.items():
            if course_code != "name":
                subject_name = subjects.get(course_code, "Unknown")
                if mark != "N/A":
                    total_marks += int(mark)
                    num_subjects += 1  # ******************************
                report_card += "{:<15} {:<25} {:<10}\n".format(course_code, subject_name, mark)
        report_card += "\n----------------------------------------\n"
        if num_subjects > 0:
            average = total_marks / num_subjects
            report_card += "Total Marks:    {}\n".format(total_marks)
            report_card += "Average Marks:  {:.2f}\n".format(average)
            report_card += "----------------------------------------\n"

            match average:
                case average if 90 <= average <= 100:
                    report_card += "Recommendation: Excellent\n"
                    report_card += "Grade: A\n"

                case average if 87 <= average <= 89:
                    report_card += "Recommendation: Excellent\n"
                    report_card += "Grade: A-\n"

                case average if 84 <= average <= 86:
                    report_card += "Recommendation: Excellent\n"
                    report_card += "Grade: B+\n"
                case average if 80 <= average <= 83:
                    report_card += "Recommendation: Good\n"
                    report_card += "Grade: B\n"
                case average if 77 <= average <= 79:
                    report_card += "Recommendation: Good\n"
                    report_card += "Grade: B-\n"

                case average if 74 <= average <= 76:
                    report_card += "Recommendation: Good\n"
                    report_card += "Grade: C+\n"

                case average if 70 <= average <= 73:
                    report_card += "Recommendation: Average\n"
                    report_card += "Grade: C\n"

                case average if 67 <= average <= 69:
                    report_card += "Recommendation: Average\n"
                    report_card += "Grade: C-\n"

                case average if 64 <= average <= 66:
                    report_card += "Recommendation: Average\n"
                    report_card += "Grade: D+\n"

                case average if 62 <= average <= 63:
                    report_card += "Recommendation: Fail\n"
                    report_card += "Grade: D\n"
                case average if 60 <= average <= 61:
                    report_card += "Recommendation: Fail\n"
                    report_card += "Grade: D-\n"

                case average if 0 <= average <= 59:
                    report_card += "Recommendation: Fail\n"
                    report_card += "Grade: F\n"
                case _:
                    report_card += "Average value not catered for"
                    report_card += "There must be an error in your entries"
                    report_card += " "

        else:
            report_card += "No marks entered for any subjects.\n"
        print(report_card)
    else:
        print("Student ID not found. Please try again.")


def main():
    subjects = {}
    while True:
        print("----- STUDENT REPORT CARD SYSTEM -----")
        print("1. Enter Student Details")
        print("2. Enter Subjects")
        print("3. Enter Marks")
        print("4. Generate Report Card")
        print("5. Quit")
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
        # Pass the subjects dictionary as an argument
        elif choice == "5":
            print("Thank you for using the Student Report Card System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
