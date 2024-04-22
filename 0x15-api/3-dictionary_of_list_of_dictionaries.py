#!/usr/bin/python3
"""
Exports all tasks from all employees to JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    todo_all_employees = {}
    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')
        url = "https://jsonplaceholder.typicode.com/todos?userId=" + user_id
        tasks = requests.get(url).json()

        todo_all_employees[user_id] = []
        for task in tasks:
            task_info = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed'),
            }
            todo_all_employees[user_id].append(task_info)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_all_employees, json_file)
