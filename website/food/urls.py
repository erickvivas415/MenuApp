from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path food/ from urls.py on website project
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('<int:item_id>/', views.detail, name='detail'),
]