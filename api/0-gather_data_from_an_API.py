#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    u = int(argv[1])  # Ensure the user ID is treated as an integer
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(u)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".fomat(u)
    u = requests.get(user_url).json()
    todo = requests.get(todo_url).json()
    employee_name = u.get('name')
    completed_tasks = [task.get('title') for task in todo if task.get('comp')]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todo)))
    for task in completed_tasks:
        print("\t {}".format(task))
