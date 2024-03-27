from datetime import date
subjects_added = False

students_details = {}
student_details_added = False


def handle_student_details():
    # global: It is used to make changes to a global variable from a local location.
    # It is now false
    global student_details_added  # Use the global variable  # *****************

    # If student_details_added == true we print error message
    # This is so that we cannot repeat this function in the same program
    if student_details_added:
        print("Student details for this semester have already been added.")
        return

    # We take in the names and ids of 10 students
    i = 0
    while i < 10:
        student_id = input("Enter the student ID: ")

        # We check if the id entered is NOT in the system
        # If it isn't in we add it
        if student_id not in students_details:
            name = input("Enter the student name: ")
            students_details[student_id] = {"name": name}
            print("Student details added successfully.")
            i = i + 1
        # If ID is already entered we ask the user to enter another ID
        else:
            print("Student ID already exists. Please try again.")
            continue
        print()

    # After all the students are added, student_details_added is set to true
    student_details_added = True


def handle_subjects():
    # global: It is used to make changes to a global variable from a local location.
    # It is currently set to false
    global subjects_added  # Use the global variable

    # If subjects added is ever true, we print this error message instead of running the
    # function
    if subjects_added:
        print("Subjects for this semester have already been added.")
        return {}

    # otherwise subjects added when we start is false, so the function is carried out

    subjects = {}
    num_subjects = 0

    # We take in 5 subject names and codes
    while num_subjects < 5:
        course_code = input("Enter the course code for subject {}: ".format(num_subjects + 1))  # ****

        # We check if the course code entered above is in the subjects dictionary
        # if the course code exists, we re ask the user to enter course code
        if course_code in subjects:
            print("Course code already exists. Please try again.")
            continue

        course_name = input("Enter the course name for subject {}: ".format(num_subjects + 1))  # *****

        # We update our subjects dictionary => key=course code, value = course name
        subjects[course_code] = course_name
        print("Subject added successfully.")
        print()

        num_subjects += 1

    # We set subjects added global variable to true, so that this function is never
    # repeated in the same program
    subjects_added = True  # Update the flag

    return subjects


def enter_marks(subjects):
    # We endlessly enter the marks for the students . Press q to quit
    while True:  # Also while x<2 would work
        student_id = input("Enter the student ID (or 'q' to finish): ")

        # Press q to quit this loop for entering marks
        if student_id.lower() == 'q':
            break

        # We also check if the student id entered is in our students details dictionary
        # among the globals
        if student_id in students_details:  # ************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            # We access the values of the student details dictionary, naming the values students
            student = students_details[student_id]
            # entered subjects is the all the keys in students ; save for name
            entered_subjects = set(student.keys()) - {"name"}  # ********
            # remaining subjects is all the keys in subjects ; save for the subjects that are already entered
            remaining_subjects = set(subjects.keys()) - entered_subjects

            # If all subjects have been entered for a student, tell user exactly that
            if len(remaining_subjects) == 0:
                print("All subjects already have marks for student with ID {}.".format(student_id))
                continue
            # If some subjects have no mark, enter marks for such subjects
            for course_code in remaining_subjects:  # *******
                # We take in marks for subjects that have not been entered
                mark = int(
                    input("Enter the mark for course {} of student with ID {}: ".format(course_code, student_id)))
                # We update the students dictionary => key=students_details[student_id][course code]
                # value= mark
                student[course_code] = mark

            print("Marks entered successfully for student with ID {}.".format(student_id))
            print()
        else:
            print("Invalid student ID. Please try again.")  # continue?


def generate_report_card(subjects):
    student_id = input("Enter the student ID: ")

    # We check if id exists in our student details dictionary
    # If not (else) print error message
    if student_id in students_details:
        # We again tap into the 
        student = students_details[student_id]
        report_card = "----------------------------------------\n"
        report_card += "                REPORT CARD               \n"
        report_card += "----------------------------------------\n"
        report_card += "USIU-AFRICA\n"
        report_card += "Date: {}\n".format(date.today())
        report_card += "Student ID: {}\n".format(student_id)
        report_card += "Student Name: {}\n\n".format(student["name"])  # ********
        report_card += "Subjects:\n\n"
        report_card += "{:<15} {:<25} {:<10}\n".format("Course Code", "Subject Name", "Marks")  # *****
        total_marks = 0
        num_subjects = 0
        for course_code, mark in student.items():
            if course_code != "name":
                subject_name = subjects.get(course_code, "Unknown")
                if mark != "N/A":
                    total_marks += int(mark)
                    num_subjects += 1  # **********
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

                case average if 87 <= average < 90:
                    report_card += "Recommendation: Excellent\n"
                    report_card += "Grade: A-\n"

                case average if 84 <= average < 87:
                    report_card += "Recommendation: Excellent\n"
                    report_card += "Grade: B+\n"
                case average if 80 <= average < 84:
                    report_card += "Recommendation: Good\n"
                    report_card += "Grade: B\n"
                case average if 77 <= average <80:
                    report_card += "Recommendation: Good\n"
                    report_card += "Grade: B-\n"

                case average if 74 <= average < 77:
                    report_card += "Recommendation: Good\n"
                    report_card += "Grade: C+\n"

                case average if 70 <= average < 74:
                    report_card += "Recommendation: Average\n"
                    report_card += "Grade: C\n"

                case average if 67 <= average < 70:
                    report_card += "Recommendation: Average\n"
                    report_card += "Grade: C-\n"

                case average if 64 <= average < 67:
                    report_card += "Recommendation: Average\n"
                    report_card += "Grade: D+\n"

                case average if 62 <= average < 64:
                    report_card += "Recommendation: Fail\n"
                    report_card += "Grade: D\n"
                case average if 60 <= average <= 61:
                    report_card += "Recommendation: Fail\n"
                    report_card += "Grade: D-\n"

                case average if 0 <= average < 60:
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
        print("Student ID not found. Please try again.") # ****


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