from django.urls import path
from . import views

urlpatterns = [
    path('create_book/',views.BookCreateView.as_view(),name='add_books'),
    path('about_me/', views.about_me_view),
    path('about_my_friend/', views.about_my_friend_view),
    path('this_time/', views.this_time_view),
    path('post_list/', views.PostLIstView.as_view(),name='post_list'),
    path('post_list/delete/', views.BookListDeleteView.as_view(),name='delete_books' ),
    path('post_list_edit/', views.BookUpdateListView.as_view(),name='edit_books' ),
    path('post_list/<int:id>/', views.PostDetailView.as_view()),
    path('post_list/<int:id>/delete/', views.BookDropDeleteView.as_view()),
    path('post_list/<int:id>/update/', views.BookEditView.as_view()),
    path('search/', views.SearchView.as_view(),name='search'),
]
