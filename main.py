def handle_student_details():
    students_details = {}
    count = 1
    while (count <= 3):
        one_student = {}
        name = input("Key in the name of the student: ")
        id_no = input("Key in the id number of the student: ")
        print(" ")

        one_student["name"]=name
        students_details[id_no] = one_student
        print(students_details)

        count = count + 1

    print(students_details)
    return students_details


def handle_subjects():
    estvalue = handle_student_details()
    print("VALUE IS: ", estvalue)

    subjects = []
    count = 0
    while count<5:
        subject = input("Key in subject: ")
        subjects.append(subject)
        print(subjects)
        count = count+1

    # for x in estvalue:
    #     for subject in subjects:
    #         estvalue[x][subject] = None
    # print("NEW VALUE IS: ", estvalue)

    for x in estvalue:
        for subject in subjects:
            mark = input("Key in " + subject + " mark for student with id " + x + " ")
            estvalue[x][subject] = mark

    print("NEW VALUE IS: ", estvalue)


handle_subjects()









