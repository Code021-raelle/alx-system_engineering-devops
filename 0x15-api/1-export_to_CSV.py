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

    user_id = int(sys.argv[1])

    # Fetching employee data
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    file_content = []

    todo_data = requests.get(todo_url).json()

    # Extracting necessary information
    employee_name = requests.get(users_url).json()["username"]

    # Writing data to CSV file
    for todo in todo_data:
        if user_id == todo["userId"]:
            file_content.append(
                    [str(user_id), employee_name, todo["completed"],
                        todo["title"]])

        print(file_content)
        file_name = "{}.csv".format(user_id)
        with open(file_name, 'w', newline='') as csv_file:
            write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for row in file_content:
                for item in row:
                    str(item)
                write.writerow(row)
