from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')


def buy(request):
    return render(request, 'buy.html')


def apple(request):
    return render(request, 'apple.html')

@login_required
def afia(request):
    return render(request, 'my-afia.html')
