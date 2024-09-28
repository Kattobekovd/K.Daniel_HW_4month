from msilib.schema import ListView
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models, forms


class MovieLIstView(generic.ListView):
    template_name = 'movie_list.html'
    context_object_name = 'post_object'
    model = models.Movie
    def get_queryset(self):
        return self.model.objects.all().order_by('id')


class MovieDetailView(generic.DetailView):
    template_name = 'movie_detail.html'
    context_object_name = 'post_id'

    def get_queryset(self,**kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=post_id)


class MovieCreateView(generic.CreateView):
    template_name = 'crud_tvshow/movie_create_movie.html'
    form_class = forms.MovieForm
    success_url = '/movie_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(MovieCreateView, self).form_valid(form=form)


class MovieListDeleteView(generic.ListView):
    template_name = 'crud_tvshow/movie_delete.html'
    context_object_name = 'post_object'
    model = models.Movie

    def get_queryset(self):
        return self.model.objects.all().order_by('id')


class MovieDropDeleteView(generic.DeleteView):
    template_name = 'crud_tvshow/movie_drop_delete.html'
    success_url = '/movie_list/'

    def get_object(self, *args, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=post_id)


class MovieListUpdateView(generic.ListView):
    template_name = 'crud_tvshow/movie_list_update.html'
    context_object_name = 'post_object'
    model = models.Movie

    def get_queryset(self):
        return self.model.objects.all().order_by('id')


class MovieDetailUpdateView(generic.UpdateView):
    template_name = 'crud_tvshow/movie_detail_update.html'
    form_class = forms.MovieForm
    success_url = '/movie_list/'

    def get_object(self, *args, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=post_id)