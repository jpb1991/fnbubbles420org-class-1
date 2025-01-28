ChatGPT generated this readme.md file.

The tasklist.py python program outputs two tasks to a list and displays the contents of the list.
# Task List Application

This is a simple task list application written in Python. It allows you to add tasks with titles and descriptions, and then list those tasks.

## Features

- Add tasks with a title and description.
- List all added tasks with their titles and descriptions.

## Code Overview

### `add_task(task_title, description)`
This function adds a task to the `tasks_list` with a specified title and description.

**Parameters:**
- `task_title`: The title of the task.
- `description`: A short description of the task.

### `list_tasks()`
This function prints all the tasks in the `tasks_list` along with their titles and descriptions.

## Example Usage

```python
task_list = []

def add_task(task_title, description):
    tasks_list.append({"title": task_title, "describe": description})

def list_tasks():
    for task in tasks_list:
        print(f"Applied to {task['title']} at {task['describe']}")

add_task("1. Write programs", "Code three programs entirely from scratch.")
add_task("2. Create README.MD file", "Create README.MD file on github.")
list_tasks()

Installation

1. Clone or download the repository.
2. Ensure you have Python 3 installed.
3. Run the script.

License

This project is licensed under the MIT License.
