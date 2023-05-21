from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, 'index.html', {'request': request})


def contact(request):
     return render(request, 'contact.html', {'request': request})


def clients(request):
     return render(request, 'clients.html', {'request': request})


def about(request):
     return render(request, 'about.html', {'request': request})


