from django.db import models

TIMEZONES = ['US/Pacific', 'US/Mountain', 'US/Central', 'US/Eastern']
TIMEZONE_CHOICES = zip(TIMEZONES, TIMEZONES)


class User(models.Model):
    timezone = models.CharField(max_length=255, choices=TIMEZONE_CHOICES)


class Todo(models.Model):
    user = models.ForeignKey('app.User', on_delete=models.CASCADE)
    scheduled_datetime = models.DateTimeField()
