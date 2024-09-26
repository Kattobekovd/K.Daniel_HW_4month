from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from . import models

@method_decorator(cache_page(60 *15), name='dispatch')
def cloths_list_view(request):
    if request.method == 'GET':
        cloth_adults = models.Cloth.objects.filter(tags__name='Для взрослых').order_by('-id')
        cloth_pensioners = models.Cloth.objects.filter(tags__name='Для пенсионеров').order_by('-id')
        cloth_children = models.Cloth.objects.filter(tags__name='Для детей').order_by('-id')
        return render(
            request,
            template_name='cloths_list.html',
            context={
                'cloth_adults':cloth_adults,
                'cloth_pensioners':cloth_pensioners,
                'cloth_children':cloth_children
            }
        )