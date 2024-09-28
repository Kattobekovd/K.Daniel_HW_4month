from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, FormView
from . import models, forms


class ParserFormVIew(FormView):
    template_name = 'parser/parser_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('ДАННЫЕ ВЗЯТЫ')
        else:
            return super(ParserFormVIew, self).post(request, *args, **kwargs)


class RezkaFilmLIstView(ListView):
    template_name = 'parser/rezka_list.html'
    model = models.RezkaFilm

    def get_queryset(self):
        return self.model.objects.all()