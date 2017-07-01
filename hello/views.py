import requests
from django.shortcuts import render
from django.http import HttpResponse
import logging

from .models import Birthday


def index(request):
    q = Birthday.objects.all()
    sorted_birthdays = sorted(q)
    sorted_birthday_output = ["<li>{0} - {1}</li>".format(f.realname, f.bd) for f in sorted_birthdays]

    logging.warning("Most Recent Birthday: {0} - {1}".format(sorted_birthdays[0].realname, sorted_birthdays[0].bd))
    return HttpResponse('<ul>' + "\n".join(sorted_birthday_output) + '</ul>')


def log(request):
    if request.method == 'POST':
        logging.warning("Remote post received")
        logging.warning(request.POST)

    else:
        logging.warning("Invalid get or other kind of request")

    return HttpResponse("hello world")