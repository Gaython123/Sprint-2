from utilis import *

list_of_students = {}

while True:
    user_command = input(" print 'help' to get all options")

    match user_command:
        case 'help':
            print_menu()

        case '1':
            add_student(list_of_students)

        case '2':
            add_grade(list_of_students)

        case '3':
            print_list_of_students(list_of_students)

        case '4':
            calculating_average(list_of_students)

        case '5':
            the_highest_average(list_of_students, name_of_student)

        case '6':
            break


