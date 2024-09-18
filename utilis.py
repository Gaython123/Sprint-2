from idlelib.editor import keynames


def print_menu():
    print("Welcome to the 'Students Grades Managment System'. To proceed choose an option(1-6):\n"
                  "1. Add a new student\n"
                  "2. Assign a grade to a student\n"
                  "3. View all students and their grades\n"
                  "4. Calculate average grade for a student\n"
                  "5. Find the student with the highest average grade\n"
                  "6. Exit the program")

def add_student(list_of_students):
    name_of_student = input("Enter the preferred student name")

    if name_of_student in list_of_students:
        print("The student is already in the list")

    else:
        print(f"{name_of_student} has been added successfully")
        list_of_students[name_of_student + "_grades"] = []

def add_grade(list_of_students):
    name_of_student = input("Enter student name")

    if name_of_student + "_grades" in list_of_students:

        grade_of_student = int(input(f"Enter grade '(1-12)' for '{name_of_student}': "))
        
        if 1 <= grade_of_student <= 12:
            print(f"You have added '{grade_of_student}' to '{name_of_student}' successfully")
            list_of_students[name_of_student + "_grades"].append(grade_of_student)

        else:
            print("Chosen grade cannot be added")

    if name_of_student + "_grades" not in list_of_students:
        print("The person doesnt belong to this list")

def print_list_of_students(list_of_students):
    if len(list_of_students) == 0:
        print("There are no students in the list")

    else:
        print(list_of_students)

    numbers = [1, 5, 15, 24, 92]
def average(numbers):
    average = sum(numbers)/len(numbers)
    return average

def calculating_average(list_of_students):
    name_of_student = input("Enter student name")

    if name_of_student + "_grades" in list_of_students:
        grades = list_of_students[name_of_student + "_grades"]

        if len(grades) == 0:
            print(f"There are no grades for '{name_of_student}'")

        else:
            print(f"The average grade for {name_of_student} is {average(grades)}")

    else:
        print(f"'{name_of_student}' is not in the list")


def the_highest_average(list_of_students):
    if len(list_of_students) == 0:
        print("There are no students in the list")
        
    else:
        grades = list_of_students[name_of_student + "_grades"]
        for i in list_of_students.values():
            a = average(grades)
            b = 0
            if b > a:
                a = b
                print(a)
                #print(f"{a} is the highest average grade for {list_of_students.get(keynames)}")
        
            



