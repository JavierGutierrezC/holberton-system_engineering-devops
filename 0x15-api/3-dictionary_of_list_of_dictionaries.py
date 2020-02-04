#!/usr/bin/python3
"""
Dictionary of list of dictionaries
"""
import json
import requests

if __name__ == "__main__":
    get_user = requests.get("https://jsonplaceholder.typicode.com/users")
    json_user = get_user.json()
    stat = requests.get("https://jsonplaceholder.typicode.com/todos")
    json_stat = stat.json()
    with open("todo_all_employees.json", "w") as to_json:
        info = {}
        n_list = []
        usr_id = {}
        for x in json_user:
            usr_id.update({x.get("id"): x.get("username")})
            # print(usr_id)
        for y in json_stat:
            # print(json_stat)
            new_dct = {}
            user_id = y.get("userId")
            # print(user_id)
            task_com = y.get("completed")
            task_titl = y.get("title")
            if user_id in usr_id.keys():
                new_dct.update({"task": task_titl, "completed": task_com,
                                "username": usr_id[user_id]})
            # print(new_dct)
            n_list.append(new_dct)
            # print(n_list)
            info[user_id] = n_list
        json.dump(info, to_json)
