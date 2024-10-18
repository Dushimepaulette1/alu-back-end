#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    user_id = int(argv[1])  # Ensure the user ID is treated as an integer
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)).json()
    
    # Get the employee name correctly
    employee_name = user.get('name')
    completed_tasks = [task.get('title') for task in todo if task.get('completed')]

    # Output the result in the specified format
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), len(todo)))
    for task in completed_tasks:
        print("\t {}".format(task))

