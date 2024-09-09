from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


def post_detail(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(models.Book, id=id)
        return render(
            request,
            template_name='post_detail.html',
            context={'post_id': post_id}
        )


def post_list(request):
    if request.method == 'GET':
        post_object = models.Book.objects.all()
        return render(
            request,
            template_name='post_list.html',
            context={'post_object': post_object}
        )


def about_me_view(request):
    return HttpResponse("Меня зовут Даниель, мне 20, я из Токмака")


def about_my_friend_view(request):
    return HttpResponse("Моего друга зовут Кутман, ему 21, и он тоже из Токмака")


def this_time_view(request):
    this_time = datetime.time(datetime.now())
    return HttpResponse(this_time)
