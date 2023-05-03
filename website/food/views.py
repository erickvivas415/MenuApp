from django.shortcuts import render, HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return render(request,'food/index.html', context)

def item(request):
    return HttpResponse('This is an item view')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    template = loader.get_template('food/item.html')
    return render(request,'food/item.html', context)