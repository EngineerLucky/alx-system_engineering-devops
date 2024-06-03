#!/usr/bin/python3
"""This Python script, exports data in the JSON format."""

if __name__ == "__main__":

    import json
    import requests
    import sys

    uId = sys.argv[1]

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(uId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(uId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[uId] = taskList

    filename = uId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
