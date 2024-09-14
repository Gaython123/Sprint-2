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

            if len(name_of_student) >= 1:
                print(f"{name_of_student} has been added successfully")
                list_of_students[name_of_student] = name_of_student

            elif len(list_of_students) == 0:
                print("You have not added a student yet")

        case '2':
            name_of_student = input("Enter student name")

            if name_of_student not in list_of_students:
                print("The person doesnt belong to this list")
            else:
                pass

            grade_of_student = int(input(f"Enter grade '(1-12)' for {name_of_student}: "))

            if grade_of_student >= 1 and grade_of_student <= 12:
                print(f"You have added {grade_of_student} to {name_of_student} successfully")

                for name_of_student in list_of_students:
                    grades_of_student.append(grade_of_student)
                    list_of_students[name_of_student] = grades_of_student

            else:
                print("Chosen grade cannot be added")


        case '3':
            print(list_of_students)





