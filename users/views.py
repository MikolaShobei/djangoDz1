from django.shortcuts import render
import os
import json

from .models import User

# Create your views here.
db_path = os.path.join("users", 'db.json')


def user(request, **kwargs):

    with open(db_path, "w") as file:
        json.dump(kwargs, file)

    with open(db_path, 'r') as file:

        users_list = json.load(file)

    return render(request, 'users/user.html', {"users": users_list})



def home(request):
    hello = "Привіт!! " \
            "Введи в адресний рядок: ім`я/вік/стать"


    return render(request, 'users/home.html', {"hello": hello})
