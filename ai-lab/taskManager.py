myTasks = []

def printTasks():
    counter = 1
    print("Current tasks: ")
    for task in myTasks:
        print(f"{counter}. {task}")
        counter += 1
    print()

def addTask(newTask):
    myTasks.append(newTask)
    return f"{newTask} added !\n"

def removeTask(pos):
    lenOfTasks = len(myTasks)
    if(pos < 1 or pos > lenOfTasks ):
        return "Invalid task !!!"
    removedTask = myTasks.pop(pos-1)
    return f"{removedTask} is removed !\n"

options = "1. Add task\n2. View Tasks\n3. Remove Task\n4. Exit"
welcomeMsg = "Welcome to task manager!!!"

while True:
    print(welcomeMsg)
    print(options)
    optionInput = int(input("Select operation: "))
    if optionInput == 1:
        newTask = input("Give task to add: ")
        message = addTask(newTask)
        print(message)
    elif optionInput == 2:
        printTasks()
    elif optionInput == 3:
        position = int(input("Enter task number: "))
        message = removeTask(position)
        print(message)
    elif optionInput == 4:
        exit(1)
    else:
        print("Invalid Input")