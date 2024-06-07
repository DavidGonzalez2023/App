from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'templates/core/home.html',)


def about(request):
    return render(request,'templates/core/about.html',)


def contact(request):
    return render(request,'templates/core/contact.html',)


def portfolio(request):
    return render(request,'templates/core/portfolio.html',)
