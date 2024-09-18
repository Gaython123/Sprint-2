from utils1 import *
list_of_tasks = {}

while True:
    user_command = input("print 'help' to see all options")

    match user_command:
        case 'help':
            help_command()

        case '1':
            new_task(list_of_tasks)

        case '2':
            view_all_tasks(list_of_tasks)

        case '3':
            delete_task(list_of_tasks)
            
        case '4':
            break

        case _:
            error()