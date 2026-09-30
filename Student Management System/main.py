import json
try:
    with open("students.json","r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []
def add_student():
    student_id = input("Enter Student id:")
    name = input("Enter Name:")
    age = int(input("Enter Age:"))
    branch = input("Enter Branch:")
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "branch":branch
    }
    students.append(student)
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)
    print("student added successfully!")
def view_students():
    print("\n... student details...")
    if len(students) == 0:
        print("no students found.")
    else:
        for student in students:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            print("....................")
def search_students():
    student_id = input("Enter student id to search:")
    for student in students:
        if student["id"] == student_id:
            print("\nStudent found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            return
    print("Student not found.")
def update_student():
    student_id = input("Enter student id to update:")
    for student in students:
        if student["id"] == student_id:
            print("Student Found!")
            student["name"]=input("enter new name:")
            student["age"]=int(input("enter new age:" ))
            student["branch"]=input("enter new branch:")

            with open("students.json","w") as file:
                json.dump(students,file,indent=4)
            print("student updated successfully!")
            return
    print("Student not found.")
def delete_student():
    student_id = input("Enter student id to delete:")
    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            with open("students.json","w") as file:
                json.dump(students,file,indent=4)
            print("student deleted successfully!")
            return
    print("student not found.")
while True:
    print("\n.... Student Management Systgem ....")
    print("1.Add Student")
    print("2.View Student")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.Exit")

    choice=input("Enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice == "3":
        search_students()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice=="6":
        print("Thank you")
        break
    else:
        print("Invalid Choice")
