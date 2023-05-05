from django.contrib import admin
from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    # Path food/ from urls.py on website project
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('<int:item_id>/', views.detail, name='detail'),
    # Add items
    path('add', views.create_item, name="create_item"),
]