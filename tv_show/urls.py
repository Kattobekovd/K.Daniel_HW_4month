from django.urls import path
from . import views


urlpatterns = [
    path('movie_list/', views.MovieLIstView.as_view(), name='movie_list'),
    path('movie_detail/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('create_movie/', views.MovieCreateView.as_view(), name='create_movie'),
    path('update_movie//<int:id>/', views.MovieListUpdateView.as_view(), name='update_movie'),
    path('update_list/', views.MovieDetailUpdateView.as_view(), name='update_list'),
    path('delete_movie/', views.MovieListDeleteView.as_view(), name='delete_movie'),
    path('delete_movie_list//<int:id>/', views.MovieDropDeleteView.as_view(), name='delete_movie_list'),
    ]