#!/usr/bin/python3
"""
This script fetches and displays an employee's TODO list progress
from a REST API
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetching employee data
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    # Extracting necessary information
    employee_name = user_data.get('name')
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get('completed')]
    num_done_tasks = len(done_tasks)

    # Displaying the progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t", task.get('title'))
