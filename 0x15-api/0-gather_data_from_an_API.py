#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv

if __name__ == "__main__":
    get_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1]))
    # print(get_user.json())
    get_name = (get_user.json().get("name"))
    # print(get_name)
    g_task = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
    .format(argv[1]))
    # print(g_task.text)
    json_task = g_task.json()
    # print(len(json_task))
    len_task = len(json_task)
    x = 0
    task_title = []
    for task in json_task:
        # print(task)
        task_completes = task.get("completed")
        # print(task_completes)
        if task_completes == True:
            task_title.append(task.get("title"))
            print(task_title)
            x += 1
            # print(x)
    print("Employee {} is done with tasks({}/{}):".format(get_name, x,
                                                          len_task))
    for title in task_title:
        # print(task_title)
        print("\t {}".format(title))
