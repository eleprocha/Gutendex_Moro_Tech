from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path(r'',views.example),
    path(r'gm', views.index),
    path(r'review',views.book_review),
    path(r'combine',views.example2),
    path(r'g',views.specificbook)
]
