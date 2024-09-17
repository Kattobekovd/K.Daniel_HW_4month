from django.urls import path
from . import views

urlpatterns = [
    path('create_book/',views.creat_book_view,name='add_books'),
    path('about_me/', views.about_me_view),
    path('about_my_friend/', views.about_my_friend_view),
    path('this_time/', views.this_time_view),
    path('post_list/', views.post_list),
    path('post_list/delete/', views.Book_list_delete_view,name='delete_books' ),
    path('post_list_edit/', views.Book_list_edit_view,name='edit_books' ),
    path('post_list/<int:id>/', views.post_detail),
    path('post_list/<int:id>/delete/', views.Book_drop_view),
    path('post_list/<int:id>/update/', views.update_book_view)
]
