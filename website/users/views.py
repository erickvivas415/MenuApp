from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account is created")
            return redirect('login') # return redirect('food:index')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})