from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


# Create your models here.
class Birthday(models.Model):
    realname = models.CharField(default='', max_length=255)
    bd = models.DateField('Birthday')


class TrueBirthday(models.Model):
    realname = models.CharField(default='', max_length=255)
    bd = models.DateField('Birthday')
