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
        print(" ")

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
        print(" ")
        count = count+1

    # for x in estvalue:
    #     for subject in subjects:
    #         estvalue[x][subject] = None
    # print("NEW VALUE IS: ", estvalue)

    for x in estvalue:
        add=0
        for subject in subjects:
            mark = input("Key in " + subject + " mark for student with id " + x + " ")
            estvalue[x][subject] = mark
            add = add+int(mark)

        print("total for id:" + x + " =" + str(add))
        avg = int(add)/5
        print("average for id:" + x + " =" + str(avg))
        print(" ")
        estvalue[x]["total"] = add
        estvalue[x]["average"] = add/5
    print("NEW VALUE IS: ", estvalue)



handle_subjects()









