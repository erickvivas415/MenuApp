from django.contrib import admin
from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    # Path food/ from urls.py on website project
    #path('', views.index, name='index'), #Replaced to use class views
    path('', views.IndexClassView.as_view(), name='index'),
    path('item/', views.item, name='item'),
    path('<int:item_id>/', views.detail, name='detail'),
    # Add items
    path('add', views.create_item, name="create_item"),
    # Update items
    path('update/<int:id>/', views.update_item, name="update_item"),
    # Delete
    path('delete/<int:id>/', views.delete_item, name="delete_item"),
]