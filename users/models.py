from django.db import models


# Create your models here.
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

