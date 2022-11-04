from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    contacts = [{'prenom':'marc', 'nom':'dupont'}, {'prenom':'antoine', 'nom':'dupuis'}]
    return render(request, 'blog/index.html', {'contacts': contacts})

def update(request):
    return HttpResponse('<h1> update </h1>')

def create(request):
    return render(request, 'blog/create.html')