#!/usr/bin/python3
"""
Export to CSV
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    get_id = argv[1]
    get_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1]))
    # print(get_user.text)
    user_name = get_user.json().get("username")
    # print(user_name)
    tstat = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(argv[1]))
    json_stat = tstat.json()
    # print(json_stat)
    csv_file = open(argv[1] + ".csv", "w")
    new_f = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for x in json_stat:
        # print(x)
        if get_id == str(x.get("userId")):
            task_com = x.get("completed")
            task_titl = x.get("title")
            # print(task_com)
            # print(task_titl)
            new_f.writerow([get_id, user_name, task_com, task_titl])
