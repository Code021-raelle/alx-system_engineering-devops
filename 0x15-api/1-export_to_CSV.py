#!/usr/bin/python3
"""
This script fetches an employee's TODO list progress from a REST API
and exports it to a CSV file.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit

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

    # Writing data to CSV file
    csv_file_name = '{}.csv'.format(employee_id)
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(
                ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STASUS', 'TASK_TITLE'])

        for task in todo_data:
            writer.writerow([employee_id, employee_name, task[
                'completed'], task['title']])
