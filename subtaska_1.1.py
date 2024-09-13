list_of_tasks = {}


while True:
    print()
    user_command = input("print 'help' to see all options")


    match user_command:
        case 'help':
            print('- help -> get the list of the commands \n1 -> Add a new task \n2 -> View all tasks \n3 -> Delete a task \n4 -> Exit')

        case '1':
            new_task = input("Create a new task")
            key = 1
            value = new_task
            list_of_tasks[key] = value

        case '2':
            print(f"{list_of_tasks}")

        case '3':
            a = int(input("Please input the number of the task"))
            list_of_tasks.pop(1)

        case '4':
            break