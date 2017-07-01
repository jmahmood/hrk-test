from django.http import HttpResponse
import logging

from django.views.decorators.csrf import csrf_exempt

from .models import Birthday


def index(request):
    q = Birthday.objects.all()
    sorted_birthdays = sorted(q)
    sorted_birthday_output = ["<li>{0} - {1}</li>".format(f.realname, f.bd) for f in sorted_birthdays]

    logging.warning("Most Recent Birthday: {0} - {1}".format(sorted_birthdays[0].realname, sorted_birthdays[0].bd))
    return HttpResponse('<ul>' + "\n".join(sorted_birthday_output) + '</ul>')


@csrf_exempt
def log(request):
    if request.method == 'POST' and request.get_host() == "still-basin-26156.herokuapp.com":
        logging.warning("Hello World (From still-basin-26156.herokuapp.com)")

    return HttpResponse("")