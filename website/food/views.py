from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello!')

def item(request):
    return HttpResponse('This is an item view')