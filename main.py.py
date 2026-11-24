tasks = []


def add_task():
    t = input("Task title: ").strip()
    if t:
        tasks.append({"title": t, "done": False})
        print("Added.")


def list_tasks():
    if not tasks:
        print("No tasks.")
        return
    for i, item in enumerate(tasks, 1):
        mark = "Done" if item["done"] else "Pending"
        print(f"{i}. {item['title']} - {mark}")


def mark_done():
    list_tasks()
    try:
        idx = int(input("Task number: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Updated.")
    except ValueError:
        pass


def remove_task():
    list_tasks()
    try:
        idx = int(input("Task number: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("Removed.")
    except ValueError:
        pass


def run():
    while True:
        print("\n1. Add\n2. List\n3. Complete\n4. Delete\n5. Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            add_task()
        elif ch == "2":
            list_tasks()
        elif ch == "3":
            mark_done()
        elif ch == "4":
            remove_task()
        elif ch == "5":
            break


if __name__ == "__main__":
    run()
