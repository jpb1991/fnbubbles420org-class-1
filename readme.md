Python Programs Overview

Program 1: Task Management

```python
task_list = []

def add_task(task_title, description):
    task_list.append({"title": task_title, "description": description})

def list_tasks():
    for task in task_list:
        print(f"Applied to {task['title']} at {task['description']}")

add_task("1. Write programs", "Code three programs entirely from scratch.")
add_task("2. Create README.MD file", "Create README.MD file on github.")
list_tasks()
```

Program 2: Weather API Request

```python
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')
city = 'London'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error fetching weather data: {response.status_code}')
```

Program 3: Calculate Leftover Money

```
total_money = 400.25
work_money = 300.14
spending_money = 29.99
utility_money = 100.20
leftover_money = total_money + work_money - spending_money - utility_money
print("${:.2f} is how much money that is left over.".format(leftover_money))
```
