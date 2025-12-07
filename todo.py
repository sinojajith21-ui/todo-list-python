def show_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()

        if tasks:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t.strip()}")
        else:
            print("No tasks yet!")

    except FileNotFoundError:
        print("No tasks yet!")


def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added!")


def main():
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task(input("Enter task: "))
        else:
            break


main()
