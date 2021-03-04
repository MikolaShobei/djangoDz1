from django.shortcuts import render
import os
import json

from .models import User

# Create your views here.
db_path = os.path.join("users", 'db.json')


def users(request, **kwargs):

    with open(db_path, "w") as file:
        json.dump(kwargs, file)

    with open(db_path, 'r') as file:

        users_list = json.load(file)

    return render(request, 'users/home.html', {"users": users_list})



def home(request):
    file = open(db_path)
    users_list = [item for item in json.load(file)]
    file.close()

    return render(request, 'users/home.html', {"users": users_list})
