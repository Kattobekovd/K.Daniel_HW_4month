from django.urls import path
from . import views

urlpatterns = [
    path('rezka_film_list/', views.RezkaFilmLIstView.as_view(), name='rezka_list'),
    path('start_parsing/', views.ParserFormVIew.as_view()),
]