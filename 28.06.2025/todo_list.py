# Simple CLI-based to-do list
def manage_todo():
    todos = []
    while True:
        action = input("Add, view, remove, or exit: ").lower()
        if action == "add":
            todos.append(input("Enter task: "))
        elif action == "view":
            print("Tasks:", todos)
        elif action == "remove":
            task = input("Task to remove: ")
            todos.remove(task) if task in todos else print("Task not found")
        elif action == "exit":
            break

if __name__ == "__main__":
    manage_todo()