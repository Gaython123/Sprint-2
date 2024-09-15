import statistics

list_of_students = {}



grades_of_student = []
while True:
    user_command = input(" print 'help' to get all options")

    match user_command:
        case 'help':
            print("Welcome to the 'Students Grades Managment System'. To proceed choose an option(1-6):\n"
                  "1. Add a new student\n"
                  "2. Assign a grade to a student\n"
                  "3. View all students and their grades\n"
                  "4. Calculate average grade for a student\n"
                  "5. Find the student with the highest average grade\n"
                  "6. Exit the program")
        case '1':
            name_of_student = input("Enter the preferred student name")


            if name_of_student in list_of_students:
                print("The student is already in the list")

            else:
                print(f"{name_of_student} has been added successfully")
                list_of_students[name_of_student + "_grades"] = []

        case '2':
            name_of_student = input("Enter student name")

            if name_of_student + "_grades" in list_of_students:
                pass

                grade_of_student = int(input(f"Enter grade '(1-12)' for '{name_of_student}': "))
                list_of_students[name_of_student + "_grades"].append(grade_of_student)

                if grade_of_student >= 1 and grade_of_student <= 12:
                    print(f"You have added '{grade_of_student}' to '{name_of_student}' successfully")

                else:
                    print("Chosen grade cannot be added")

            if name_of_student + "_grades" not in list_of_students:
                print("The person doesnt belong to this list")

        case '3':
            if len(list_of_students) == 0:
                print("There are no students in the list")

            else:
                print(list_of_students)

        case '4':
            name_of_student = input("Enter student name")
            if name_of_student + "_grades" in list_of_students:

                grades = list_of_students[name_of_student + "_grades"]
                average_student_grade = statistics.mean(grades)
                print(average_student_grade)


            else:
                pass
                print("The student is not in the list")

        







