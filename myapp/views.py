from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def accueil(request):
    return HttpResponse("<h1>Hey welcom to ma app 🚀</h1>")