from django.shortcuts import HttpResponse, render
import datetime
import random
import time


def hello(requests):
    return render(requests, "third_app/hello.html")


def greeting(requests):
    context_dict = {"user": [{
        "name": "Lilit",
        "surname": "Harutyunyan",
        "is_verified": True
        }, {
        "name": "Hayk",
        "surname": "Petrosyan",
        "is_verified": False
        }]}
    return render(requests, "third_app/hello_python_world.html", context=context_dict)


def null(requests):
    return HttpResponse("<h1>Hello Django World</h1>")


def my_font(requests):
    num = random.randint(1, 5)
    shrift = f"<h{num}> Name: Lilit Surname: Harutyunyan<h{num}>"
    return HttpResponse(shrift)


def introduction(requests):
    return HttpResponse("<h1>It's my first work, which includes some interesting Django project ideas</h1>")


def current_datetime(requests):
    current_date = datetime.date.today()
    current_time = datetime.datetime.today().time()
    return HttpResponse(f"<h1>date: {current_date}, time: {current_time}</h1>")


def my_dictionary(requests):
    my_dict = {}
    my_nums = range(1, 16)
    for i in my_nums:
        my_dict[i] = i * 2
    return HttpResponse(my_dict)
