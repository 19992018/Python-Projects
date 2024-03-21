from datetime import datetime
now = datetime.now().strftime('%a %d %b %Y, %I:%M%p')
print(now)


def handle_student_details():
    students_details = {}
    count = 1
    while count <= 2:
        one_student = {}
        name = input("Key in the name of the student: ")
        id_no = input("Key in the id number of the student: ")
        print(" ")

        one_student["name"] = name

        students_details[id_no] = one_student
        print(students_details)
        print(" ")

        count = count + 1

    print(students_details)
    return students_details


def handle_subjects():
    est_value = handle_student_details()
    print("VALUE IS: ", est_value)

    subjects = []
    count = 0
    while count < 2:
        subject = input("Key in subject: ")
        subjects.append(subject)
        print(subjects)
        print(" ")
        count = count+1

    # for x in est_value:
    #     for subject in subjects:
    #         est_value[x][subject] = None
    # print("NEW VALUE IS: ", est_value)

    for x in est_value:
        add = 0
        for subject in subjects:
            mark = input("Key in " + subject + " mark for student with id " + x + " ")
            est_value[x][subject] = mark
            add = add+int(mark)

        print("total for id:" + x + " =" + str(add))
        avg = int(add)/2
        print("average for id:" + x + " =" + str(avg))
        print(" ")
        est_value[x]["total"] = add
        est_value[x]["average"] = add/2
    print("NEW VALUE IS: ", est_value)
    return est_value


def grade_generator():
    est_subjects = handle_subjects()
    print("DICTIONARY NOW DISPLAYS: " + str(est_subjects))

    for key in est_subjects:
        average = est_subjects[key]['average']

        match average:
            case average if 90 <= average <= 100:
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
    return est_subjects


def print_report_card():
    get_info = grade_generator()
    print(get_info)
    id_list = get_info.keys()

    while True:
        get_id = input("Key in id: ")
        if get_id not in id_list:
            print("Invalid id")
        else:
            print("id: " + get_id)
            for item in get_info[get_id].items():
                print(item)

        print(" ")


print_report_card()
