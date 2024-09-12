from django.urls import path
from . import views
urlpatterns = [
    path('cloth_adulth/', views.cloths_list_view )
]