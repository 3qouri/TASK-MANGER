import os 


#file to store tasks
FILE_NAME = "tasks.txt"
def load_tasks():
    
    tasks={}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks[task] = status == "done"
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task, done in tasks.items():
            status = "done" if done else "not done"
            file.write(f"{task}|{status}\n")
# add a new task
def add_task(tasks, task):
    title=input("Enter task title: ")
    task_id=max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "done": False}
    print(f"Task '{title}' added.")
    
    



#view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task_id, task in tasks.items():
        status = "✓" if task["done"] else "✗"
        print(f"{task_id}. [{status}] {task['title']}")
        
        
        
# mark task as done
def mark_task_done(tasks, task_id):
    if task_id in tasks:
        tasks[task_id]["done"] = True
        print(f"Task '{tasks[task_id]['title']}' marked as done.")
    else:
        print("Task not found.")
        
        
# delete a task
def delete_task(tasks, task_id):
    if task_id in tasks:
        title = tasks[task_id]['title']
        del tasks[task_id]
        print(f"Task '{title}' deleted.")
    else:
        print("Task not found.")
# main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks, tasks)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as done: "))
            mark_task_done(tasks, task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
                 
                 
                 
                 
main()             