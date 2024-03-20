def get_student():
    id_no = int(input("Student's Id no: "))
    name = input("Student's name: ").capitalize()
    return id_no, name

def handle_error():
    if get_student() == "end" or 0:
        if len(store_student(id_no=get_student(), name=get_student())) < 3:
            print("Number of students has to be 10 or more.")
            return continue
        else:
            return break


def store_student(id_no, name):
    students_stored = {}
    id_no, name = get_student()
    while True:
        handle_error()
        get_student()
        students_stored[id_no] = name
        print(students_stored)
        return students_stored


def execute():
    get_student()
    store_student(id_no=get_student(), name=get_student())

execute()









