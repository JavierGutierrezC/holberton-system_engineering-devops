#!/usr/bin/python3
"""
Export to CSV
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    get_id = argv[1]
    get_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1]))
    user_name = get_user.json().get("username")
    # print(user_name)
    tstat = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(argv[1]))
    json_stat = tstat.json()
    n_list = []
    info = {}
    with open(get_id + ".json", "w") as to_json:
        for x in json_stat:
            new_dct = {}
            usr_id = x.get("userId")
            # print(usr_id)
            task_com = x.get("completed")
            task_titl = x.get("title")
            if get_id == str(usr_id):
                new_dct.update({"task": task_titl, "completed": task_com,
                                "username": user_name})
            # print(new_dct)
                n_list.append(new_dct)
            # print(n_list)
        info[get_id] = n_list
        json.dump(info, to_json)
