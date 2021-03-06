from django.db import models
from datetime import date
import datetime
import logging

class Birthday(models.Model):
    """Celebs and their birthdays!"""
    realname = models.CharField(default='', max_length=255)
    bd = models.DateField('Birthday')

    def __cmp__(self, other):
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        current_date = datetime.datetime.now().day

        next_bd_year = current_year
        next_bd_month = self.bd.month
        next_bd_day = self.bd.day

        if (next_bd_month < current_month or (next_bd_month == current_month and next_bd_day < current_date)):
            next_bd_year = current_year + 1

        next_bd = date(next_bd_year, next_bd_month, next_bd_day)


        cmp_bd_year = current_year
        cmp_bd_month = other.bd.month
        cmp_bd_day = other.bd.day

        if (cmp_bd_month < current_month or (cmp_bd_month == current_month and cmp_bd_day < current_date)):
            cmp_bd_year = current_year + 1

        cmp_bd = date(cmp_bd_year, cmp_bd_month, cmp_bd_day)

        if next_bd == cmp_bd:
            return 0

        if next_bd > cmp_bd:
            return 1

        return -1


    def __unicode__(self):
        return self.realname

class TrueBirthday(models.Model):
    realname = models.CharField(default='', max_length=255)
    bd = models.DateField('Birthday')
