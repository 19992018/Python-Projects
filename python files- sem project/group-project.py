from datetime import date

# This addition will make our work easier when demonstrating to Prof
# We can change no_of_students to 10 0r 2 depending on what prof wants
no_of_students = 2
students_details = {}
no_of_subjects = 2


def handle_student_details():
    # changed for loop to while loop
    # so that continue statement added in line 23 takes user back to beginning of loop
    # instead of taking user back to main menu of 6 items as the previous program did
    # I had to use a while loop because CONTINUE wasn't working well with the for loop
    count = 0
    while count < no_of_students:
        student_id = input("Enter the student ID (or 'q' to quit): ")
        if student_id == 'q':
            break

        if student_id not in students_details:
            name = input("Enter the student name: ")
            students_details[student_id] = {"name": name}
            print("Student details added successfully.")
        else:
            print("Student ID already exists. Please try again.")
            continue
        print()
        count = count + 1


def handle_subjects():
    subjects = {}

    # I changed the loop from while true because Prof said we use a fixed number of subjects
    # minimum 5 subjects... but for testing purposes no_of_subjects (line 7) is 2
    subjects_count = 0
    while subjects_count < no_of_subjects:
        # The following 3 lines may or may not be necessary now that we're not using while True
        course_code = input("Enter the course code (or 'q' to quit): ")
        if course_code == 'q':
            break

        course_name = input("Enter the course name: ")
        subjects[course_code] = course_name
        print("Subject added successfully.")
        print()
        subjects_count = subjects_count + 1

    print("You have entered all needed subjects")
    return subjects


def enter_marks(subjects):
    list_of_ids = students_details.keys()
    len_of_list = len(list_of_ids)
    for each_id in range(len_of_list):
        student_id = input("Enter the student ID: ")

        if student_id in students_details:
            student = students_details[student_id]
            track_subjects = []
            # Kindly explain this part where you have used a set/ sets
            entered_subjects = set()
            # Kindly explain this while condition
            while entered_subjects != set(subjects.keys()):
                course_code = input("Enter the course code: ")
                if course_code not in track_subjects:
                    track_subjects.append(course_code)
                    if course_code not in subjects:
                        print("Invalid course code. Please enter a valid course code.")
                        print()
                        continue

                    # Kindly explain .format(course_code, student_id)
                    mark = int(input("Enter the mark for course {} of student with ID {}: ".format(course_code, student_id)))
                    student[course_code] = mark
                    entered_subjects.add(course_code)
                else:
                    print("Course already entered")
                    continue
        else:
            print("Invalid student ID. Please try again.")


def generate_report_card(subjects):
    student_id = input("Enter the student ID: ")
    if student_id in students_details:
        student = students_details[student_id]

        # Is f""" used to create multiline comments
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
            # why are we checking if course_code != "name"
            if course_code != "name":
                # why use the parameter "Unknown"
                course_name = subjects.get(course_code, "Unknown")
                report_card += f"\n\t\t{course_name} ({course_code}): {mark}\n"
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
        print(students_details)


if __name__ == "__main__":
    main()
