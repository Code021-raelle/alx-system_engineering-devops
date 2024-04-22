#!/usr/bin/python3
"""
This script fetches an employee's TODO list progress from a REST API
and exports it to a JSON file.
"""

import json
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
    employee_name = user_data.get('username')

    # Creating JSON data
    json_data = {str(employee_id): []}
    for task in todo_data:
        json_data[str(employee_id)].append({
            'task': task['title'],
            'completed': task['completed'],
            'username': employee_name
        })

    # Writing data to JSON file
    json_file_name = '{}.json'.format(employee_id)
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Data exported to", json_file_name)
