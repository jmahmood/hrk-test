import requests
from django.shortcuts import render
from django.http import HttpResponse
import logging

from .models import Birthday

def index(request):
    q = Birthday.objects.all()
    sorted_output = ["<li>{0} - {1}</li>".format(f.realname, f.bd) for f in sorted(q)]

    logging.warning("Most Recent Birthday: ")
    logging.warning(sorted_output[0])
    return HttpResponse('<ul>' + "\n".join(sorted_output) + '</ul>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

