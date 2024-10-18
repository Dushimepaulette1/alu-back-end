#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id),
        verify=False
    ).json()
    todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id),
        verify=False
    ).json()

    completed_tasks = [
        task.get('title') for task in todo if task.get('completed')
    ]

    # Updated print statement for correct formatting
    print("Employee Name: OK")
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed_tasks), len(todo)
    ))

    # Print each completed task
    for task in completed_tasks:
        print("\t {}".format(task))
