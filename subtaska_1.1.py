list_of_tasks = {}


while True:
    print()
    user_command = input("print 'help' to see all options")


    match user_command:
        case 'help':
            print('- help -> get the list of the commands \n1 -> Add a new task \n2 -> View all tasks \n3 -> Delete a task \n4 -> Exit')

        case '1':
            new_task = input("Create a new task")
            task_number = len(list_of_tasks) + 1
            list_of_tasks[task_number] = new_task
            print(f"'{new_task}' is added to the list!")



        case '2':
            print(f"{list_of_tasks}")
            if len(list_of_tasks) == 0: #if list_of_tasks = []
                print("The list is empty!")


        case '3':
            print(f"{list_of_tasks}")
            a = int(input("Please input the number of the task you want to delete"))
            list_of_tasks.pop(a)
            print("The task was deleted successfully!")

        case '4':
            break

        case _:
            print("Invalid input")