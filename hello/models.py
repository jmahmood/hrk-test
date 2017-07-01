from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


# Create your models here.
class Birthday(models.Model):
    name = models.DateField('Birthday')
    bd = models.DateField('Birthday')
