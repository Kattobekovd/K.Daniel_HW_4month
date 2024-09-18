from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views import generic
from . import models, forms

# Функция на кнопку Поиск по названием книг
class SearchView(generic.ListView):
    template_name = 'post_list.html'
    context_object_name = 'post_object'
    paginate_by = 10 #Это количество постов на одну страницу

    def get_queryset(self):
        return models.Book.objects.filter(title__icontains=self.request.GET.get('q')).order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


#Редактирование crud, получение список постов
class BookUpdateListView(generic.ListView):
    template_name = 'crud/book_list_edit.html'
    context_object_name = 'post_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('id')


#ЗДесь функция на редактирование обявлений из списка
class BookEditView(generic.UpdateView):
    template_name = 'crud/book_update.html'
    form_class = forms.BookForm
    success_url = '/post_list_edit/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, pk=post_id)


#Удаление crud, здесь мы получаем листы
class BookListDeleteView(generic.ListView):
    template_name = 'crud/book_list_delete.html'
    context_object_name = 'post_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('id')

# здесь происходит удаление с подтверждением
class BookDropDeleteView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/post_list/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)


#Добавление crud
class BookCreateView(generic.CreateView):
    template_name = 'crud/create_book.html'
    form_class = forms.BookForm
    success_url = '/post_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


# Вывод полной информации
class PostDetailView(generic.DetailView):
    template_name = 'post_detail.html'
    context_object_name = 'post_id'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)


# Вывод не полной информации
class PostLIstView(generic.ListView):
    template_name = 'post_list.html'
    context_object_name = 'post_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('id')


def about_me_view(request):
    return HttpResponse("Меня зовут Даниель, мне 20, я из Токмака")


def about_my_friend_view(request):
    return HttpResponse("Моего друга зовут Кутман, ему 21, и он тоже из Токмака")


def this_time_view(request):
    this_time = datetime.time(datetime.now())
    return HttpResponse(this_time)
