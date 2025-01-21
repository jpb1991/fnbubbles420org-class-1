tasks_list = []

def add_task(task_title, description):
    tasks_list.append({"title": task_title, "describe": description})

def list_tasks():
    for task in tasks_list:
        print(f"Applied to {task['title']} at {task['describe']}")

add_task("1. Write programs", "Code three programs entirely from scratch.")
add_task("2. Create README.MD file", "Create README.MD file on github.")
list_tasks()
