# Report card viewing date is required
from datetime import datetime


# Function takes in name and id of students
def handle_student_details():
    # empty dictionary that will store student's id as key 
    # value of this empty dictionary will be another dictionary that stores name and subjects...
    students_details = {}
    
    # Loop helps us get students' data
    count = 1
    while count <= 2:
        print("KEY IN STUDENT DETAILS (10 students)")
        # Dictionary will have a fixed key "name" and value is actual name of the student
        one_student = {}
        name = input("Key in the name of the student: ")
        id_no = input("Key in the id number of the student: ")
        print(" ")

        # update one student dictionary whose fixed key is "name" and value is actual name of the student
        one_student["name"] = name

        # update student details dictionary, setting its key to id taken in and its value to the one student ...
        # ...dictionary created above
        students_details[id_no] = one_student
        print(students_details)
        print(" ")

        count = count + 1

    print(students_details)
    
    # return the students details dictionary so that it can be used every time this function is called 
    return students_details


# This function enables the user to key in the subjects and subject scores per student
# The function also calculates the total score and average per student
def handle_subjects():
    # We call the function handle students details for it to run and return student details dictionary
    # We give the function's return a new value, est_students_details
    est_students_details = handle_student_details()
    print("VALUE IS: ", est_students_details)

    print(" ")
    print("KEY IN SUBJECTS (5 subjects): ")

    # This empty list will store subjects entered as the loop below it runs
    subjects = []
    count = 0
    while count < 2:
        subject = input("Key in subject: ")
        # Each subject entered are appended/added to the subjects array
        subjects.append(subject)
        print(subjects)
        print(" ")
        count = count+1

    # We loop through the keys(x)  in est_students_details dictionary
    # The keys are ids
    for x in est_students_details:
        add = 0
        # KEYING IN THE SUBJECT MARKS FOR EACH STUDENT ID
        for subject in subjects:
            mark = input("Key in " + subject + " mark for student with id " + x + " ")
            # updating the est_students_details' (nested) dictionary to have a key called subject ...
            # ... whose value is mark entered
            est_students_details[x][subject] = mark
            # calculating total per student id by adding the marks with every loop iteration
            add = add+int(mark)

        print("total for student id  " + x + " =" + str(add))
        # calculate average
        avg = int(add)/2
        print("average for student id " + x + " =" + str(avg))
        print(" ")
        est_students_details[x]["total"] = add
        est_students_details[x]["average"] = add/2
    print("NEW VALUE IS: ", est_students_details)
    # return the updated dictionary which now has the subjects
    return est_students_details


#  This function generates grade per student depending on average obtained from previous function
def grade_generator():
    # call the handle_subjects function
    # This enables you to get its return value (our updated dictionary with subjects>...)
    # we call our returned value est_subjects
    est_subjects = handle_subjects()
    print("DICTIONARY NOW DISPLAYS: " + str(est_subjects))  # Just printing handle subjects to see what it is

    print(" ")

    # Loop through the keys (ids) in est_subjects
    for key in est_subjects:
        # set average to the nested dictionary's value of key average
        average = est_subjects[key]['average']

        # use match case to give a letter grade and recommendation depending on average
        match average:
            case average if 90 <= average <= 100:
                # add new keys grade and recommendation to est_subjects nested dictionary giving them values
                est_subjects[key]['grade'] = 'A'
                est_subjects[key]['Recommendation'] = 'Excellent'

            case average if 87 <= average <= 89:
                est_subjects[key]['grade'] = 'A-'
                est_subjects[key]['Recommendation'] = 'Excellent'

            case average if 84 <= average <= 86:
                est_subjects[key]['grade'] = 'B+'
                est_subjects[key]['Recommendation'] = 'Excellent'

            case average if 80 <= average <= 83:
                est_subjects[key]['grade'] = 'B'
                est_subjects[key]['Recommendation'] = 'Good'

            case average if 77 <= average <= 79:
                est_subjects[key]['grade'] = 'B-'
                est_subjects[key]['Recommendation'] = 'Good'

            case average if 74 <= average <= 76:
                est_subjects[key]['grade'] = 'C+'
                est_subjects[key]['Recommendation'] = 'Good'

            case average if 70 <= average <= 73:
                est_subjects[key]['grade'] = 'C'
                est_subjects[key]['Recommendation'] = 'Average'

            case average if 67 <= average <= 69:
                est_subjects[key]['grade'] = 'C-'
                est_subjects[key]['Recommendation'] = 'Average'

            case average if 64 <= average <= 66:
                est_subjects[key]['grade'] = 'D+'
                est_subjects[key]['Recommendation'] = 'Average'

            case average if 62 <= average <= 63:
                est_subjects[key]['grade'] = 'D'
                est_subjects[key]['Recommendation'] = 'Fail'

            case average if 60 <= average <= 61:
                est_subjects[key]['grade'] = 'D-'
                est_subjects[key]['Recommendation'] = 'Fail'

            case average if 0 <= average <= 59:
                est_subjects[key]['grade'] = 'F'
                est_subjects[key]['Recommendation'] = 'Fail'

            case _:
                print("Average value not catered for")
                print("There must be an error in your entries")
                print(" ")

    print(est_subjects)
    # return the dictionary that now has grade and recommendation
    return est_subjects


# This function enables the student to view their performance/ report card
def print_report_card():
    # We call grade_generator function() and store its value as get_info
    get_info = grade_generator()
    print(get_info)
    # create a list out of the get_info dictionary keys
    id_list = get_info.keys()

    print(" ")
    print("GET YOUR REPORT CARD ")

    while True:
        print(" ")
        get_id = input("Key in id: ")
        print(" ")
        print("USIU REPORT CARD")
        # Check if id entered by user exists or not in the list of ids
        if get_id not in id_list:
            print("Key in a valid ID")
            continue
        else:
            print("Student's id: " + get_id)
            for item in get_info[get_id].items():
                print(str(item[0]) + " : " + str(item[1]))
        now = datetime.now().strftime('%a %d %b %Y, %I:%M%p')
        print("Date and time viewed: " + now)

        print(" ")


print_report_card()
