from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me_view),
    path('about_my_friend/', views.about_my_friend_view),
    path('this_time/', views.this_time_view),
    path('post_list/', views.post_list),
    path('post_list/<int:id>/', views.post_detail),
]
