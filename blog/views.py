from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def about_me_view(request):
    return HttpResponse("Меня зовут Даниель, мне 20, я из Токмака")


def about_my_friend_view(request):
    return HttpResponse("Моего друга зовут Кутман, ему 21, и он тоже из Токмака")


def this_time_view(request):
    this_time = datetime.time(datetime.now())
    return HttpResponse(this_time)
