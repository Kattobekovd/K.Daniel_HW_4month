from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models, forms


#Редактирование crud, получение список постов
def Book_list_edit_view(request):
    if request.method == 'GET':
        post_object = models.Book.objects.all()
        return render(
            request,
            'crud/book_list_edit.html',
            {'post_object': post_object}
        )
#ЗДесь функция на редактирование обявлений из списка
def update_book_view(request, id):
    post_id = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=post_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные успешно Отредактирована!! <a href = /post_list/ > На список обьявлений книг </a>')
    else:
        form = forms.BookForm(instance=post_id)
    return render(
        request,
        template_name='crud/book_update.html',
        context={'form': form, 'post_id': post_id}
    )

#Удаление crud, здесь мы получаем листы
def Book_list_delete_view(request):
    if request.method == 'GET':
        post_object = models.Book.objects.all()
        return render(
            request,
            'crud/book_list_delete.html',
            {'post_object': post_object}
        )

# здесь функция на удаление постов из листа
def Book_drop_view(request, id):
    post_id = get_object_or_404(models.Book, id=id)
    post_id.delete()
    return HttpResponse('Данные успешно Удалены!! <a href = /post_list/ > На список обьявлений книг </a>')


#Добавление crud
def creat_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные успешно отправлены!! <a href = /post_list/ > На список обьявлений книг </a>')
    else:
        form = forms.BookForm()
    return render(
        request,
        'crud/create_book.html',
        {'form':form}
    )


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
