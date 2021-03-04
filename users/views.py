from django.shortcuts import render
import os
import json

from .models import User

# Create your views here.
db_path = os.path.join("users", 'db.json')


def user(request, **kwargs):
    try:
        with open(db_path, "r") as file:
            users_list = [item for item in json.load(file)]
            users_list.append(kwargs)
            users_list1 = [User(**item) for item in users_list]

        json_users_list = json.dumps(users_list)

        with open(db_path, "w") as file:
            file.write(json_users_list)

    except Exception as err:
        with open(db_path, 'w') as file:
            file.write(json.dumps([]))

        with open(db_path, "r") as file:
            users_list = [item for item in json.load(file)]
            users_list.append(kwargs)
            users_list1 = [User(**item) for item in users_list]

        json_users_list = json.dumps(users_list)

        with open(db_path, "w") as file:
            file.write(json_users_list)
        print(err)
    finally:
        pass


    return render(request, 'users/user.html', {"users": users_list1})


def home(request):
    return render(request, 'users/home.html')
