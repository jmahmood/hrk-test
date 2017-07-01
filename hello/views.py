import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

def index(request):
    q = Greeting.objects.all()
    for f in q:
        print(f)
    return HttpResponse('<pre>' + q[0] + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

